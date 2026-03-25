# CLAUDE.md - Taiwan National Strategy Project

## Overview

A bilingual (Traditional Chinese (正體中文) / English) policy analysis of Taiwan's multi-domain national security strategy. Structured as a think tank report with 16 chapters, deep citations, structured verification data, and live URL audit support.

## File Structure

- `docs/en/` - English full text and verification report
- `docs/zh-TW/` - Traditional Chinese (正體中文) full text and verification report
- `data/statistics/` - Per-chapter statistics in JSON format
- `data/timelines/` - Historical event timelines in CSV
- `data/comparisons/` - Cross-country comparative data in CSV
- `data/schemas/` - JSON Schema for data validation
- `references/` - Master bibliography and per-chapter reference lists

## Conventions

### File Naming

- Full text: `docs/<lang>/full-text.md`
- Verification: `docs/<lang>/verification-report.md`
- Statistics: `chNN-descriptor-stats.json`
- References: `chNN-references.md`

### Chapter Template

Each chapter uses this structure:
1. Title with chapter number
2. Key takeaway (one-sentence summary)
3. Numbered sections with Context / Current Status / Assessment / Policy Recommendations
4. Data tables referencing statistics JSON
5. All references consolidated at the end of the full-text document

### Data Standards

- All statistics include: metric, value, unit, date, source (name + URL), verification status
- Dates use ISO 8601 format
- Sources prefer government reports, international organizations, peer-reviewed publications

### Bilingual Parity

- Every document in `docs/en/` has an exact counterpart in `docs/zh-TW/`
- File names are identical across language directories
- Data and references are language-neutral (shared)
- README.md and CONTRIBUTING.md are bilingual (EN/ZH-TW combined)

### Commits

Follow Conventional Commits: `docs(chNN): description` or `data(statistics): description`

## Validation

- `python3 scripts/validate_repository.py`
- `python3 scripts/validate_repository.py --check-urls --enforce-url-status`
