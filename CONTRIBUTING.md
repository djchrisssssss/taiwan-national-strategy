# Contributing

Thank you for your interest in contributing to this project. This document provides guidelines for contributions.

## How to Contribute

### Reporting Errors

If you find factual errors, outdated statistics, or broken references:

1. Open an issue describing the error
2. Include the chapter number and section
3. Provide the correct information with a verifiable source

### Updating Data

Statistics and data points require source verification:

1. Fork the repository
2. Update the relevant JSON file in `data/statistics/`
3. Ensure every data point includes: metric, value, unit, date, and source URL
4. Update the corresponding entry in `references/bibliography.json`
5. Submit a pull request with a clear description

### Translation Improvements

For translation corrections or improvements:

1. Identify the file in `chapters/en/` or `chapters/zh-TW/`
2. Ensure changes maintain consistency with the counterpart language file
3. Preserve all citation references and data table entries

### Adding New Analysis

For substantive analytical contributions:

1. Open an issue first to discuss the proposed addition
2. Follow the chapter template format (see any existing chapter)
3. Include supporting data in JSON format
4. Provide at least 3 verifiable references per major claim

## Commit Convention

This project follows [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/).

```
<type>(scope): <description>
```

Types: `docs`, `data`, `fix`, `feat`, `refactor`, `chore`

Examples:
- `docs(ch02): update TSMC market share to Q4 2025 data`
- `data(statistics): add ch08 space capability metrics`
- `fix(references): correct broken DOI link for defense white paper`

## Data Format Standards

### Statistics JSON

All statistics files must conform to `data/schemas/statistics-schema.json`.

### Timeline CSV

Columns: `date`, `event`, `category`, `significance`, `source_id`, `notes`

### Bibliography JSON

Each entry requires: `id`, `type`, `title`, `authors`, `date`, `url`, `verified`

## Code of Conduct

Contributions should be factual, evidence-based, and politically neutral. This project aims to provide objective strategic analysis, not advocacy for any particular political position.
