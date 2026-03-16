# CLAUDE.md - Taiwan National Strategy Project

## Overview

A bilingual (Traditional Chinese / English) policy analysis of Taiwan's multi-domain national security strategy. Structured as a think tank report with 12 chapters, 1 supplement, deep citations, and verification data.

## File Structure

- `chapters/en/` - English chapters (complete)
- `chapters/zh-TW/` - Traditional Chinese chapters (complete)
- `data/statistics/` - Per-chapter statistics in JSON format
- `data/timelines/` - Historical event timelines in CSV
- `data/comparisons/` - Cross-country comparative data in CSV
- `data/schemas/` - JSON Schema for data validation
- `references/` - Master bibliography and per-chapter reference lists
- `verification/` - Data verification reports (bilingual)

## Conventions

### File Naming

- Chapters: `NN-kebab-case-title.md` (zero-padded, e.g., `01-`, `02-`)
- Supplement: `S1-food-water-security.md`
- Statistics: `chNN-descriptor-stats.json` or `S1-descriptor-stats.json`
- References: `chNN-references.md`

### Chapter Template

Each chapter uses this structure:
1. Title with chapter number
2. Key takeaway (one-sentence summary)
3. Numbered sections with Context / Current Status / Assessment / Policy Recommendations
4. Data tables referencing statistics JSON
5. Chapter-specific references

### Data Standards

- All statistics include: metric, value, unit, date, source (name + URL), verification status
- Dates use ISO 8601 format
- Sources prefer government reports, international organizations, peer-reviewed publications

### Bilingual Parity

- Every chapter in `en/` has an exact counterpart in `zh-TW/`
- File names are identical across language directories
- Data and references are language-neutral (shared)

### Commits

Follow Conventional Commits: `docs(chNN): description` or `data(statistics): description`
