# Taiwan's Multi-Domain National Security Strategy: A Comprehensive Analysis

**Language: English** | [繁體中文](README-zh-TW.md)

---

## Read the Full Analysis

| Language | Document |
|----------|----------|
| English | **[Full Text (EN)](docs/full-text-en.md)** |
| 繁體中文 | **[全文閱讀（ZH-TW）](docs/full-text-zh-TW.md)** |

---

## Abstract

Taiwan's national security is fundamentally a systems engineering challenge. In an era of multi-domain competition, security can no longer be measured by the strength of any single defensive line; it must be assessed by the entire system's capacity to continue functioning under multiple, simultaneous, cross-domain pressures. This project presents a comprehensive analytical framework that treats Taiwan's national security as a complex adaptive system composed of thirteen interconnected domains -- from geostrategic positioning and semiconductor leverage to cognitive defense and international linkages.

Employing a systems engineering methodology grounded in interdependency analysis, nonlinear risk modeling, and adversary rationality assumptions, this study examines how failures in one domain can cascade into others, identifies structural vulnerabilities arising from geographic concentration, energy dependence, and communications fragility, and proposes policy recommendations organized by short-term (1--2 years), medium-term (3--5 years), and long-term (5--10 years) horizons. The core strategic principles -- antifragile architecture, multi-domain redundancy, and cost-imposition strategy -- aim to ensure that any coercive action against Taiwan faces prohibitively high costs across the political, military, and economic dimensions.

---

## Chapters Overview

### I. Overview

| Ch. | Domain | Description |
|:---:|--------|-------------|
| 00 | Executive Summary | Analytical framework, structural risk overview, thirteen-domain summary, core strategic principles, and methodology. |

### II. Strategic Foundation

| Ch. | Domain | Description |
|:---:|--------|-------------|
| 01 | Geostrategic Position | First Island Chain node value, Bashi Channel control, strategic waterways, and Taiwan's role as a regional public good. |
| 02 | Semiconductor Leverage | Advanced node irreplaceability, geographic concentration of fabs, talent bottlenecks, and strategic interdependence networks. |

### III. Military Defense

| Ch. | Domain | Description |
|:---:|--------|-------------|
| 03 | Asymmetric Defense | Cost-exchange ratio logic, submarine denial, unmanned systems, precision strike, and indigenous mass production. |
| 04 | Electromagnetic Spectrum Warfare | Spectrum dominance, anti-jamming communications, electronic countermeasure systems, and EW as the opening move of modern conflict. |

### IV. Critical Infrastructure

| Ch. | Domain | Description |
|:---:|--------|-------------|
| 05 | Energy Structure | Import dependence, dangerously low LNG reserves, distributed microgrids, and renewable energy transition. |
| 06 | Food & Water Security | Food self-sufficiency, water resource constraints, semiconductor ultrapure water demands, and critical infrastructure protection. |
| 07 | Communications Resilience | Submarine cable vulnerability, LEO satellite backup, high-frequency radio, and community-level mesh networks. |
| 08 | Financial Resilience | Sanctions defense, cross-border payment backup, digital asset strategies, and blockchain-based data preservation. |

### V. Technology Frontiers

| Ch. | Domain | Description |
|:---:|--------|-------------|
| 09 | Space Capabilities | Indigenous small satellite constellation, space situational awareness, and space-based communications integration. |
| 10 | AI & Distributed Computing | Intelligence fusion, autonomous defense, distributed computing architectures, and blockchain-AI integration for resilience. |
| 11 | Quantum Security | Post-quantum cryptography migration, quantum key distribution pilots, and long-term data confidentiality protection. |

### VI. Society & International

| Ch. | Domain | Description |
|:---:|--------|-------------|
| 12 | Cognitive Defense | Countering disinformation and deepfake threats, media literacy, institutional transparency, and social trust infrastructure. |
| 13 | International Linkages | Shifting from seeking protection to building indispensability through technological interdependence, intelligence cooperation, and democratic values. |

---

## Data & References

This project maintains a structured data layer to support reproducibility and verification of all analytical claims.

| Resource | Path | Description |
|----------|------|-------------|
| Statistics | `data/statistics/` | Per-chapter quantitative data (JSON). Each entry includes metric, value, unit, date, and source URL. |
| Timelines | `data/timelines/` | Historical event CSVs covering military incidents, semiconductor milestones, and infrastructure events. |
| Comparisons | `data/comparisons/` | Cross-country comparative data on defense spending, semiconductor market share, and energy dependency. |
| Bibliography | `references/bibliography.json` | Master bibliography with 100+ annotated references. |
| Source Registry | `references/source-registry.json` | Centralized registry mapping source IDs to full bibliographic entries. |
| Per-chapter References | `references/per-chapter/` | Annotated reference lists for each chapter. |
| Verification Reports | `docs/verification-report-en.md` | Data verification methodology and audit results. |

All statistics files conform to the validation schema at `data/schemas/statistics-schema.json`.

---

## Project Structure

```
taiwan-national-strategy/
├── docs/
│   ├── full-text-en.md                 # Full analysis (English)
│   ├── full-text-zh-TW.md             # 全文分析（繁體中文）
│   ├── verification-report-en.md       # Data verification report (EN)
│   └── verification-report-zh-TW.md    # 資料驗證報告（ZH-TW）
├── data/
│   ├── schemas/
│   │   └── statistics-schema.json      # JSON Schema for data validation
│   ├── statistics/                     # Per-chapter quantitative data (JSON)
│   ├── timelines/                      # Historical event timelines (CSV)
│   └── comparisons/                    # Cross-country comparisons (CSV)
├── references/
│   ├── bibliography.json               # Master bibliography
│   ├── source-registry.json            # Source ID registry
│   └── per-chapter/                    # Per-chapter reference lists
├── CHANGELOG.md
├── CITATION.cff
├── CONTRIBUTING.md
├── CONTRIBUTING-zh-TW.md
├── LICENSE
├── README.md
└── README-zh-TW.md
```

---

## How to Cite

If you use or reference this analysis, please cite it as follows:

```
djchrisssssss. (2026). Taiwan National Strategy: A Multi-Domain Resilience Framework.
https://github.com/djchrisssssss/taiwan-national-strategy
```

A machine-readable citation is available in [CITATION.cff](CITATION.cff).

**BibTeX:**

```bibtex
@misc{taiwan_national_strategy_2026,
  author       = {djchrisssssss},
  title        = {Taiwan National Strategy: A Multi-Domain Resilience Framework},
  year         = {2026},
  url          = {https://github.com/djchrisssssss/taiwan-national-strategy},
  license      = {CC-BY-4.0}
}
```

---

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on reporting errors, updating data, improving translations, and adding new analysis. All contributions must follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.

A Traditional Chinese version of the contribution guide is available at [CONTRIBUTING-zh-TW.md](CONTRIBUTING-zh-TW.md).

---

## License

This work is licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

You are free to share and adapt this material for any purpose, including commercial use, provided you give appropriate credit and indicate if changes were made. See [LICENSE](LICENSE) for full details.

---

## Disclaimer

This project constitutes independent academic analysis and does not represent the official policy position of any government, institution, or organization. The analysis is based exclusively on open-source information and is intended to contribute to public understanding of complex strategic challenges. It is not intended as advocacy for any particular policy outcome or political position. All data points are sourced and verifiable; readers are encouraged to consult the referenced materials and form their own assessments.
