#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from pathlib import Path

import jsonschema


ROOT = Path(__file__).resolve().parents[1]
SUPPORTED_REGISTRY_STATUSES = {"reachable", "access_restricted", "missing", "other"}
BRACKETED_REFERENCE_RE = re.compile(r"\[(src-\d{3})\]")
STATISTIC_ID_RE = re.compile(r"^ch\d{2}-\d{3}$")
LEGACY_SOURCE_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
CHAPTER_TAG_RE = re.compile(r"^ch(?:0[0-9]|1[0-7])$")
VALID_EVIDENCE_TIERS = {
    "tier_1_primary",
    "tier_2_secondary",
    "tier_3_estimate",
    "tier_4_forward_looking",
}
VALID_CLAIM_TYPES = {
    "measured_statistic",
    "case_count",
    "geographic_measurement",
    "market_estimate",
    "policy_target",
    "scenario_or_timeline",
}
VALID_CONFIDENCE_LEVELS = {"high", "medium", "low"}
VALID_VERIFICATION_MODES = {
    "official_publication_check",
    "cross_source_check",
    "single_source_check",
    "registry_case_check",
    "policy_document_check",
}
EXPECTED_STATISTICS_FILES = {
    "01": "ch01-geo-statistics.json",
    "02": "ch02-semiconductor-stats.json",
    "03": "ch03-defense-stats.json",
    "04": "ch04-ew-statistics.json",
    "05": "ch05-energy-stats.json",
    "06": "ch06-food-water-stats.json",
    "07": "ch07-biosecurity-stats.json",
    "08": "ch08-comms-statistics.json",
    "09": "ch09-financial-statistics.json",
    "10": "ch10-space-statistics.json",
    "11": "ch11-ai-statistics.json",
    "12": "ch12-quantum-statistics.json",
    "13": "ch13-cognitive-statistics.json",
    "14": "ch14-ethics-stats.json",
    "15": "ch15-international-statistics.json",
    "16": "ch16-airspace-anomaly-stats.json",
}


def load_json(relative_path: str) -> object:
    return json.loads((ROOT / relative_path).read_text())


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text()


def write_json(relative_path: str, payload: object) -> None:
    (ROOT / relative_path).write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    )


def normalize_url(url: str) -> str:
    return url.rstrip("/")


def normalize_host(url: str) -> str:
    return urllib.parse.urlparse(url).netloc.lower()


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

        chapters_cited = source.get("chapters_cited", [])
        if not chapters_cited:
            errors.append(f"bibliography source {source_id} has empty chapters_cited")
        else:
            invalid_chapters = [
                chapter_id
                for chapter_id in chapters_cited
                if not CHAPTER_TAG_RE.fullmatch(chapter_id)
            ]
            if invalid_chapters:
                errors.append(
                    f"bibliography source {source_id} has invalid chapters_cited entries: "
                    + ", ".join(invalid_chapters)
                )

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
        "ids": ids,
        "status_counts": status_counts,
        "entries": entries,
        "metadata": metadata,
    }


def parse_statistic_reference_map() -> dict[str, set[str]]:
    statistic_sources: dict[str, set[str]] = {}

    for path in sorted((ROOT / "references/per-chapter").glob("ch*-references.md")):
        for raw_line in path.read_text().splitlines():
            line = raw_line.strip()
            if not line.startswith("|"):
                continue

            columns = [column.strip() for column in line.strip("|").split("|")]
            if len(columns) < 3:
                continue

            statistic_id = columns[0]
            if not STATISTIC_ID_RE.fullmatch(statistic_id):
                continue

            source_ids = set(BRACKETED_REFERENCE_RE.findall(columns[-1]))
            if source_ids:
                statistic_sources.setdefault(statistic_id, set()).update(source_ids)

    return statistic_sources


def validate_markdown_citations(
    bibliography_ids: set[str], registry_ids: set[str], errors: list[str]
) -> dict[str, int]:
    files = sorted((ROOT / "references/per-chapter").glob("ch*-references.md")) + [
        ROOT / "docs/en/full-text.md",
        ROOT / "docs/zh-TW/full-text.md",
    ]

    total_citations = 0
    unique_citations: set[str] = set()

    for path in files:
        cited_ids = set(BRACKETED_REFERENCE_RE.findall(path.read_text()))
        total_citations += len(cited_ids)
        unique_citations.update(cited_ids)

        missing_bibliography = sorted(cited_ids - bibliography_ids)
        if missing_bibliography:
            errors.append(
                f"{path.relative_to(ROOT)} cites source IDs missing from bibliography: "
                + ", ".join(missing_bibliography[:20])
            )

        missing_registry = sorted(cited_ids - registry_ids)
        if missing_registry:
            errors.append(
                f"{path.relative_to(ROOT)} cites source IDs missing from source-registry: "
                + ", ".join(missing_registry[:20])
            )

    return {
        "files_checked": len(files),
        "unique_citations": len(unique_citations),
        "citation_sets_checked": total_citations,
    }


def validate_statistics(errors: list[str]) -> dict[str, object]:
    schema = load_json("data/schemas/statistics-schema.json")
    validator_cls = getattr(jsonschema, "Draft202012Validator", jsonschema.Draft7Validator)
    validator = validator_cls(schema)

    total_points = 0
    verified_points = 0
    ids: set[str] = set()
    per_file_counts: dict[str, int] = {}
    evidence_tier_counts: Counter = Counter()
    claim_type_counts: Counter = Counter()
    confidence_counts: Counter = Counter()
    verification_mode_counts: Counter = Counter()

    actual_files = sorted(path.name for path in (ROOT / "data/statistics").glob("*.json"))
    expected_files = sorted(EXPECTED_STATISTICS_FILES.values())
    missing_files = sorted(set(expected_files) - set(actual_files))
    unexpected_files = sorted(set(actual_files) - set(expected_files))
    if missing_files:
        errors.append("missing expected statistics files: " + ", ".join(missing_files))
    if unexpected_files:
        errors.append("unexpected statistics files present: " + ", ".join(unexpected_files))

    for path in sorted((ROOT / "data/statistics").glob("*.json")):
        data = json.loads(path.read_text())
        expected_filename = EXPECTED_STATISTICS_FILES.get(data["chapter"])
        if expected_filename and path.name != expected_filename:
            errors.append(
                f"{path.name} does not match canonical filename for chapter {data['chapter']}: {expected_filename}"
            )
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

            evidence_tier = stat.get("evidence_tier")
            claim_type = stat.get("claim_type")
            confidence_level = stat.get("confidence_level")
            verification_mode = stat.get("verification_mode")

            if evidence_tier not in VALID_EVIDENCE_TIERS:
                errors.append(f"{path.name} statistic {stat_id} has invalid evidence_tier {evidence_tier!r}")
            else:
                evidence_tier_counts[evidence_tier] += 1

            if claim_type not in VALID_CLAIM_TYPES:
                errors.append(f"{path.name} statistic {stat_id} has invalid claim_type {claim_type!r}")
            else:
                claim_type_counts[claim_type] += 1

            if confidence_level not in VALID_CONFIDENCE_LEVELS:
                errors.append(
                    f"{path.name} statistic {stat_id} has invalid confidence_level {confidence_level!r}"
                )
            else:
                confidence_counts[confidence_level] += 1

            if verification_mode not in VALID_VERIFICATION_MODES:
                errors.append(
                    f"{path.name} statistic {stat_id} has invalid verification_mode {verification_mode!r}"
                )
            else:
                verification_mode_counts[verification_mode] += 1

    return {
        "total_points": total_points,
        "verified_points": verified_points,
        "per_file_counts": per_file_counts,
        "evidence_tier_counts": evidence_tier_counts,
        "claim_type_counts": claim_type_counts,
        "confidence_counts": confidence_counts,
        "verification_mode_counts": verification_mode_counts,
    }


def validate_statistics_source_links(
    registry_summary: dict[str, object],
    statistic_reference_map: dict[str, set[str]],
    errors: list[str],
) -> dict[str, int]:
    registry_entries = registry_summary["entries"]
    registry_urls = {normalize_url(entry["url"]) for entry in registry_entries}
    registry_hosts = {normalize_host(entry["url"]) for entry in registry_entries}
    registry_urls_by_id = {
        entry["source_id"]: normalize_url(entry["url"]) for entry in registry_entries
    }
    registry_hosts_by_id = {
        entry["source_id"]: normalize_host(entry["url"]) for entry in registry_entries
    }

    matched = 0
    checked = 0
    unmapped = 0

    for path in sorted((ROOT / "data/statistics").glob("*.json")):
        data = json.loads(path.read_text())
        for stat in data["statistics"]:
            checked += 1
            stat_id = stat["id"]
            source_url = stat["source"]["url"]
            normalized_url = normalize_url(source_url)
            normalized_host = normalize_host(source_url)
            mapped_source_ids = statistic_reference_map.get(stat_id, set())

            if mapped_source_ids:
                candidate_urls = {
                    registry_urls_by_id[source_id]
                    for source_id in mapped_source_ids
                    if source_id in registry_urls_by_id
                }
                candidate_hosts = {
                    registry_hosts_by_id[source_id]
                    for source_id in mapped_source_ids
                    if source_id in registry_hosts_by_id
                }

                if (
                    normalized_url not in candidate_urls
                    and normalized_host not in candidate_hosts
                ):
                    errors.append(
                        f"{path.name} statistic {stat_id} source URL does not match "
                        f"its cited reference IDs {sorted(mapped_source_ids)}"
                    )
                else:
                    matched += 1
                continue

            if normalized_url in registry_urls or normalized_host in registry_hosts:
                matched += 1
            else:
                unmapped += 1

    return {
        "checked": checked,
        "matched": matched,
        "unmapped": unmapped,
    }


def validate_tabular_sources(
    bibliography_ids: set[str], registry_ids: set[str], errors: list[str]
) -> dict[str, int]:
    files = sorted((ROOT / "data/timelines").glob("*.csv")) + sorted(
        (ROOT / "data/comparisons").glob("*.csv")
    )

    rows_checked = 0
    legacy_ids = 0

    for path in files:
        with path.open(newline="") as handle:
            reader = csv.DictReader(handle)
            if "source_id" not in (reader.fieldnames or []):
                errors.append(f"{path.relative_to(ROOT)} is missing required source_id column")
                continue

            for row_number, row in enumerate(reader, start=2):
                rows_checked += 1
                source_id = (row.get("source_id") or "").strip()

                if not source_id:
                    errors.append(
                        f"{path.relative_to(ROOT)} row {row_number} has empty source_id"
                    )
                    continue

                if source_id.startswith("src-"):
                    if source_id not in bibliography_ids:
                        errors.append(
                            f"{path.relative_to(ROOT)} row {row_number} references unknown bibliography source_id {source_id}"
                        )
                    if source_id not in registry_ids:
                        errors.append(
                            f"{path.relative_to(ROOT)} row {row_number} references unknown source-registry source_id {source_id}"
                        )
                    continue

                if not LEGACY_SOURCE_ID_RE.fullmatch(source_id):
                    errors.append(
                        f"{path.relative_to(ROOT)} row {row_number} uses malformed legacy source_id {source_id!r}"
                    )
                    continue

                legacy_ids += 1

    return {
        "files_checked": len(files),
        "rows_checked": rows_checked,
        "legacy_ids": legacy_ids,
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
    tier_1 = stats_summary["evidence_tier_counts"].get("tier_1_primary", 0)
    tier_2 = stats_summary["evidence_tier_counts"].get("tier_2_secondary", 0)
    tier_3 = stats_summary["evidence_tier_counts"].get("tier_3_estimate", 0)
    tier_4 = stats_summary["evidence_tier_counts"].get("tier_4_forward_looking", 0)
    high_conf = stats_summary["confidence_counts"].get("high", 0)
    medium_conf = stats_summary["confidence_counts"].get("medium", 0)
    low_conf = stats_summary["confidence_counts"].get("low", 0)

    expectations = {
        "docs/en/verification-report.md": [
            f"| Report Date | {audit_date} |",
            f"| Total Sources | {total_sources} |",
            f"| Total Tracked URLs | {total_urls} |",
            f"| Total Data Points | {total_points} |",
            f"| `tier_1_primary` | {tier_1} |",
            f"| `tier_2_secondary` | {tier_2} |",
            f"| `tier_3_estimate` | {tier_3} |",
            f"| `tier_4_forward_looking` | {tier_4} |",
            f"| `high` | {high_conf} |",
            f"| `medium` | {medium_conf} |",
            f"| `low` | {low_conf} |",
            f"| URL status: `reachable` | {reachable} |",
            f"| URL status: `access_restricted` | {restricted} |",
            f"| URL status: `missing` | {missing} |",
            f"| URL status: `other` | {other} |",
            f"| All {total_sources} bibliography sources have unique `id` fields (src-001 through src-{total_sources:03d}) | PASS |",
            "Evidence tiering is now tracked separately from the binary `verified` flag.",
        ],
        "docs/zh-TW/verification-report.md": [
            f"| 報告日期 | {audit_date} |",
            f"| 來源總數 | {total_sources} |",
            f"| 追蹤 URL 總數 | {total_urls} |",
            f"| 資料點總數 | {total_points} |",
            f"| `tier_1_primary` | {tier_1} |",
            f"| `tier_2_secondary` | {tier_2} |",
            f"| `tier_3_estimate` | {tier_3} |",
            f"| `tier_4_forward_looking` | {tier_4} |",
            f"| `high` | {high_conf} |",
            f"| `medium` | {medium_conf} |",
            f"| `low` | {low_conf} |",
            f"| URL狀態：`reachable` | {reachable} |",
            f"| URL狀態：`access_restricted` | {restricted} |",
            f"| URL狀態：`missing` | {missing} |",
            f"| URL狀態：`other` | {other} |",
            f"| 全部 {total_sources} 個來源具有唯一 `id` 欄位（src-001 至 src-{total_sources:03d}） | 通過 |",
            "證據層級已與二元 `verified` 旗標分開追蹤。",
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
    citation_summary = validate_markdown_citations(
        bibliography_summary["ids"], registry_summary["ids"], errors
    )
    statistic_reference_map = parse_statistic_reference_map()
    stats_summary = validate_statistics(errors)
    stats_link_summary = validate_statistics_source_links(
        registry_summary, statistic_reference_map, errors
    )
    tabular_summary = validate_tabular_sources(
        bibliography_summary["ids"], registry_summary["ids"], errors
    )
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
                "evidence_tier_1_points": stats_summary["evidence_tier_counts"].get(
                    "tier_1_primary", 0
                ),
                "evidence_tier_4_points": stats_summary["evidence_tier_counts"].get(
                    "tier_4_forward_looking", 0
                ),
                "markdown_citation_files_checked": citation_summary["files_checked"],
                "statistics_source_links_matched": stats_link_summary["matched"],
                "tabular_rows_checked": tabular_summary["rows_checked"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
