#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from pathlib import Path

import jsonschema


ROOT = Path(__file__).resolve().parents[1]
SUPPORTED_REGISTRY_STATUSES = {"reachable", "access_restricted", "missing", "other"}
BRACKETED_REFERENCE_RE = re.compile(r"\[(src-\d{3})\]")


def load_json(relative_path: str) -> object:
    return json.loads((ROOT / relative_path).read_text())


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text()


def write_json(relative_path: str, payload: object) -> None:
    (ROOT / relative_path).write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    )


def status_to_category(code: int | None) -> str:
    if code is not None and 200 <= code < 400:
        return "reachable"
    if code in {401, 403}:
        return "access_restricted"
    if code == 404:
        return "missing"
    return "other"


def fetch_status(url: str, timeout: int) -> int | None:
    if shutil.which("curl"):
        result = subprocess.run(
            [
                "curl",
                "-L",
                "-s",
                "-o",
                "/dev/null",
                "-w",
                "%{http_code}",
                "--max-time",
                str(timeout),
                "-A",
                "taiwan-national-strategy-validator/1.0",
                url,
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        code = result.stdout.strip()
        return int(code) if code.isdigit() else None

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "taiwan-national-strategy-validator/1.0"},
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.getcode()
    except urllib.error.HTTPError as exc:
        return exc.code
    except Exception:
        return None


def validate_bibliography(errors: list[str]) -> dict[str, object]:
    bibliography = load_json("references/bibliography.json")
    metadata = bibliography["metadata"]
    sources = bibliography["sources"]

    if metadata["total_sources"] != len(sources):
        errors.append(
            f"bibliography metadata total_sources={metadata['total_sources']} != actual {len(sources)}"
        )

    ids: set[str] = set()
    for source in sources:
        source_id = source["id"]
        if source_id in ids:
            errors.append(f"duplicate bibliography source id: {source_id}")
        ids.add(source_id)

    type_counts = Counter(source["type"] for source in sources)
    doi_count = sum(1 for source in sources if source.get("doi"))

    return {
        "count": len(sources),
        "ids": ids,
        "type_counts": type_counts,
        "doi_count": doi_count,
    }


def validate_source_registry(
    bibliography_ids: set[str], errors: list[str]
) -> dict[str, object]:
    registry = load_json("references/source-registry.json")
    metadata = registry["metadata"]
    entries = registry["registry"]

    if metadata["total_urls"] != len(entries):
        errors.append(
            f"source-registry metadata total_urls={metadata['total_urls']} != actual {len(entries)}"
        )

    ids: set[str] = set()
    invalid_statuses = sorted(
        {entry["status"] for entry in entries if entry["status"] not in SUPPORTED_REGISTRY_STATUSES}
    )
    if invalid_statuses:
        errors.append(
            f"source-registry contains unsupported statuses: {', '.join(invalid_statuses)}"
        )

    for entry in entries:
        source_id = entry["source_id"]
        if source_id in ids:
            errors.append(f"duplicate source-registry source_id: {source_id}")
        ids.add(source_id)
        if source_id not in bibliography_ids:
            errors.append(
                f"source-registry source_id {source_id} is missing from references/bibliography.json"
            )

    missing_registry_ids = sorted(bibliography_ids - ids)
    if missing_registry_ids:
        errors.append(
            "bibliography sources missing from source-registry: "
            + ", ".join(missing_registry_ids[:20])
        )

    status_counts = Counter(entry["status"] for entry in entries)
    if "status_counts" in metadata and metadata["status_counts"] != dict(status_counts):
        errors.append("source-registry metadata status_counts does not match registry entries")

    return {
        "count": len(entries),
        "status_counts": status_counts,
        "entries": entries,
        "metadata": metadata,
    }


def validate_statistics(errors: list[str]) -> dict[str, object]:
    schema = load_json("data/schemas/statistics-schema.json")
    validator_cls = getattr(jsonschema, "Draft202012Validator", jsonschema.Draft7Validator)
    validator = validator_cls(schema)

    total_points = 0
    verified_points = 0
    ids: set[str] = set()
    per_file_counts: dict[str, int] = {}

    for path in sorted((ROOT / "data/statistics").glob("*.json")):
        data = json.loads(path.read_text())
        validation_errors = sorted(
            validator.iter_errors(data), key=lambda err: list(err.absolute_path)
        )
        for err in validation_errors:
            location = "/".join(str(part) for part in err.absolute_path) or "<root>"
            errors.append(f"{path.name} schema error at {location}: {err.message}")

        stats = data["statistics"]
        per_file_counts[path.stem.split("-")[0]] = len(stats)
        total_points += len(stats)
        verified_points += sum(1 for stat in stats if stat.get("verified"))

        for stat in stats:
            stat_id = stat["id"]
            if stat_id in ids:
                errors.append(f"duplicate statistic id: {stat_id}")
            ids.add(stat_id)

    return {
        "total_points": total_points,
        "verified_points": verified_points,
        "per_file_counts": per_file_counts,
    }


def validate_reports(
    bibliography_summary: dict[str, object],
    registry_summary: dict[str, object],
    stats_summary: dict[str, object],
    errors: list[str],
) -> None:
    total_sources = bibliography_summary["count"]
    total_urls = registry_summary["count"]
    total_points = stats_summary["total_points"]
    verified_points = stats_summary["verified_points"]
    audit_date = registry_summary["metadata"]["last_audit"]
    status_counts = registry_summary["status_counts"]
    reachable = status_counts.get("reachable", 0)
    restricted = status_counts.get("access_restricted", 0)
    missing = status_counts.get("missing", 0)
    other = status_counts.get("other", 0)

    expectations = {
        "docs/en/verification-report.md": [
            f"| Report Date | {audit_date} |",
            f"| Total Sources | {total_sources} |",
            f"| Total Tracked URLs | {total_urls} |",
            f"| Total Data Points | {total_points} |",
            f"| URL status: `reachable` | {reachable} |",
            f"| URL status: `access_restricted` | {restricted} |",
            f"| URL status: `missing` | {missing} |",
            f"| URL status: `other` | {other} |",
            f"| All {total_sources} bibliography sources have unique `id` fields (src-001 through src-{total_sources:03d}) | PASS |",
        ],
        "docs/zh-TW/verification-report.md": [
            f"| 報告日期 | {audit_date} |",
            f"| 來源總數 | {total_sources} |",
            f"| 追蹤 URL 總數 | {total_urls} |",
            f"| 資料點總數 | {total_points} |",
            f"| URL狀態：`reachable` | {reachable} |",
            f"| URL狀態：`access_restricted` | {restricted} |",
            f"| URL狀態：`missing` | {missing} |",
            f"| URL狀態：`other` | {other} |",
            f"| 全部 {total_sources} 個來源具有唯一 `id` 欄位（src-001 至 src-{total_sources:03d}） | 通過 |",
        ],
    }

    for relative_path, snippets in expectations.items():
        text = read_text(relative_path)
        for snippet in snippets:
            if snippet not in text:
                errors.append(f"{relative_path} is missing expected snippet: {snippet}")

    if verified_points != total_points:
        errors.append(
            f"expected all data points to be verified, but only {verified_points}/{total_points} have verified=true"
        )


def audit_urls(
    timeout: int,
) -> tuple[list[dict[str, object]], Counter, Counter]:
    registry = load_json("references/source-registry.json")
    entries = registry["registry"]

    results: list[dict[str, object]] = []
    code_counts: Counter = Counter()
    category_counts: Counter = Counter()

    def check(entry: dict[str, object]) -> dict[str, object]:
        code = fetch_status(entry["url"], timeout)
        category = status_to_category(code)
        return {
            "source_id": entry["source_id"],
            "url": entry["url"],
            "http_code": code,
            "category": category,
        }

    with ThreadPoolExecutor(max_workers=12) as executor:
        futures = [executor.submit(check, entry) for entry in entries]
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            code_counts[str(result["http_code"]) if result["http_code"] is not None else "ERR"] += 1
            category_counts[result["category"]] += 1

    return sorted(results, key=lambda item: item["source_id"]), code_counts, category_counts


def sync_url_statuses(results: list[dict[str, object]]) -> None:
    payload = load_json("references/source-registry.json")
    entries = payload["registry"]
    result_map = {result["source_id"]: result for result in results}
    today = date.today().isoformat()

    for entry in entries:
        result = result_map[entry["source_id"]]
        entry["status"] = result["category"]
        entry["last_checked"] = today

    status_counts = Counter(entry["status"] for entry in entries)
    payload["metadata"]["last_audit"] = today
    payload["metadata"]["total_urls"] = len(entries)
    payload["metadata"]["audit_method"] = "automated_http_spot_check + manual_review"
    payload["metadata"]["status_counts"] = dict(status_counts)
    payload["metadata"].pop("verified_count", None)

    write_json("references/source-registry.json", payload)


def check_urls(
    timeout: int,
    enforce_registry_status: bool,
    sync_registry_status: bool,
    errors: list[str],
) -> Counter:
    results, code_counts, category_counts = audit_urls(timeout)

    if sync_registry_status:
        sync_url_statuses(results)
        registry = load_json("references/source-registry.json")
        registry_statuses = {entry["source_id"]: entry["status"] for entry in registry["registry"]}
    else:
        registry = load_json("references/source-registry.json")
        registry_statuses = {entry["source_id"]: entry["status"] for entry in registry["registry"]}

    for result in results:
        code = result["http_code"]
        http_label = code if code is not None else "ERR"
        print(f"{http_label}\t{result['category']}\t{result['source_id']}\t{result['url']}")
        if enforce_registry_status and registry_statuses[result["source_id"]] != result["category"]:
            errors.append(
                "live URL status mismatch for "
                f"{result['source_id']}: registry={registry_statuses[result['source_id']]} "
                f"live={result['category']} (http={http_label})"
            )

    return category_counts


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check-urls",
        action="store_true",
        help="Run live HTTP checks against references/source-registry.json.",
    )
    parser.add_argument(
        "--sync-url-status",
        action="store_true",
        help="Update references/source-registry.json with live URL status categories.",
    )
    parser.add_argument(
        "--enforce-url-status",
        action="store_true",
        help="Fail if live URL status categories do not match references/source-registry.json.",
    )
    parser.add_argument(
        "--url-timeout",
        type=int,
        default=8,
        help="Timeout in seconds for each URL request.",
    )
    args = parser.parse_args()

    errors: list[str] = []

    bibliography_summary = validate_bibliography(errors)
    registry_summary = validate_source_registry(bibliography_summary["ids"], errors)
    stats_summary = validate_statistics(errors)
    validate_reports(bibliography_summary, registry_summary, stats_summary, errors)

    if args.check_urls or args.sync_url_status:
        category_counts = check_urls(
            args.url_timeout,
            args.enforce_url_status,
            args.sync_url_status,
            errors,
        )
        print("url audit summary:")
        print(json.dumps(dict(category_counts), indent=2, sort_keys=True))

    if errors:
        print("validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("local consistency checks passed")
    print(
        json.dumps(
            {
                "bibliography_sources": bibliography_summary["count"],
                "tracked_urls": registry_summary["count"],
                "quantitative_data_points": stats_summary["total_points"],
                "verified_data_points": stats_summary["verified_points"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
