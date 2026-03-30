# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- `docs/revision-plan.md` as the repository-level remediation roadmap
- AI collaboration disclosure expectations in `README.md`, `CONTRIBUTING.md`, and a PR template

### Changed

- Statistics schema now distinguishes source traceability from evidence strength through `evidence_tier`, `claim_type`, `confidence_level`, and `verification_mode`
- Ch16 statistics file renamed to align with the current chapter title
- Bibliography chapter mappings refreshed from current per-chapter references to remove legacy supplement residue
- Validator extended to check evidence metadata, chapter tag residue, and canonical statistics filenames
- AI collaboration disclosure text now records `Claude Code (Opus 4)` and `Codex (GPT-5.4)` as concrete repository-assistance examples

- **Chapter 3 expansion: Missile Defense and Hardened Infrastructure** — Two new sections added to Asymmetric Defense chapter:
  - Section 3.5: Missile Defense and Hypersonic Threats — DF-17/DF-27 threat assessment, multi-layer defense architecture analysis (Tien Kung III, PAC-3), counter-hypersonic strategies (GPI, directed energy), detection and early warning, offensive counterforce
  - Section 3.6: Hardened Infrastructure and Underground Strategy — Chiashan AFB model, eastern strategic depth, underground munitions/fuel storage, decentralized command architecture, highway runway strips, civil defense shelter modernization (Swiss/Israeli models), critical infrastructure hardening standards
  - Three new policy recommendations (items 10-12) in renumbered Section 3.7
  - 7 new statistics (ch03-013 to ch03-019) and 7 new sources ([src-158] to [src-164])

### Fixed

- Statistics schema regex pattern updated to remove obsolete S[0-9] alternative
- Stale "fourteen core domains" references updated to "sixteen" in full-text files
- Verification report source counts updated (169 sources, 200 data points)
- **Duplicate source IDs resolved**: Ch05 nuclear energy sources [src-056]–[src-060] renumbered to [src-165]–[src-169] to eliminate collision with Ch10 (Space) and Ch12 (Quantum) sources
- **Ch14 statistics ID gaps closed**: Renumbered ch14-004→003, ch14-005→004, ch14-006→005, ch14-008→006, ch14-009→007, ch14-010→008 (sequential ch14-001 to ch14-008)
- Source type breakdown tables in verification reports updated from 95-source totals to full 169-source categorization

### Changed

- **Major chapter reordering and renumbering**: Restructured from 6 Parts to 7 Parts for improved narrative flow
  - Part IV: Resource Security & Biological Resilience (Ch5 Energy, Ch6 Food & Water, Ch7 Biological Security)
  - Part V: Communications & Economic Resilience (Ch8 Communications, Ch9 Financial, Ch10 Space)
  - Part VI: Technology & Intelligence (Ch11 AI, Ch12 Quantum, Ch13 Cognitive Defense, Ch14 Technology Ethics)
  - Part VII: International Strategy & Emerging Domains (Ch15 International, Ch16 Non-Traditional Security)
- **Chapter renumbering map**: Old Ch7→8, Ch8→9, Ch9→10, Ch10→11, Ch11→12, Ch12→13, Ch13→15, Ch14→16, Ch15→14, Ch16→7
- All statistics files, reference files, cross-chapter linkages, and section headers renumbered accordingly
- Biological Security (formerly Ch16) repositioned as Ch7, immediately after Ch6 Food & Water Security, reflecting strong agricultural bioterrorism linkage

### Added

- **New Chapter 16: Biological Security** — Dedicated chapter covering biowarfare threats, CCP biological programs and strategic intent, COVID-19 origins analysis, agricultural bioterrorism (including Reedley CA unauthorized biolab), genetic modification as a security domain, synthetic biology dual-use risks, Taiwan's biological vulnerability assessment, pandemic preparedness and response architecture, and 11 policy recommendations across three time horizons. 9 sections (16.1–16.9).
- New ch16-biosecurity-stats.json with 10 statistics entries (ch16-001 to ch16-010)
- New ch16-references.md with 15 sources ([src-142] to [src-156])
- **New Chapter 15: Technology Ethics** — Covers six domains: genetic modification and genome engineering, synthetic biology and artificial life, brain-computer interfaces and consciousness engineering ethics, end-of-life ethics and euthanasia, surrogate motherhood and reproductive technology, and autonomous weapons and AI ethics in warfare. 9 sections (15.1–15.9) with 10 policy recommendations across three time horizons.
- **New Section 10.5: Brain-Computer Interfaces and Neurocognitive Technologies** — BCI technology landscape, military/defense applications, neurocognitive warfare as emerging threat, Taiwan's strategic positioning, and cross-chapter linkages.
- 5 new sections in Chapter 12: CCP Cognitive Warfare Supply Chain (12.2), Platform-Specific Infiltration Strategies (12.4), Economic Coercion as Cognitive Warfare (12.5), Institutional Infiltration and Co-optation (12.6), Cross-Chapter Linkages (12.10)
- 8 new policy recommendations in Chapter 12 (items 11–18: offensive intelligence, platform governance, economic defense, institutional protection)
- 3 new BCI policy recommendations in Chapter 10 (items 10, 11, 13)
- 10 new statistics entries in ch12-cognitive-statistics.json (ch12-011 to ch12-020: state-generated posts, V-Dem ranking, GoLaxy documents, AI deepfakes, NSB espionage cases, Meta CIB takedowns, OpenAI disruptions, targeting database, economic coercion incidents, four-layer command structure)
- 4 new statistics entries in ch10-ai-statistics.json (ch10-011 to ch10-014: BCI market size, DARPA N3 investment, Neuralink trials, global BCI patents)
- New ch15-ethics-stats.json with 10 statistics entries (ch15-001 to ch15-010)
- New ch15-references.md with 13 sources ([src-129] to [src-141])
- 9 new sources in ch12-references.md ([src-116] to [src-124])
- 4 new sources in ch10-references.md ([src-125] to [src-128])

### Changed

- **Restructured Chapter 15 (Technology Ethics)**: Extracted biological content (Sections 15.2 Genetic Modification and 15.3 Synthetic Biology) to Chapter 16. Renumbered remaining sections (15.4→15.2 through 15.9→15.7). Updated title to "Consciousness Engineering, Reproductive Ethics, and Emerging Technology Governance". Updated policy recommendations and cross-chapter linkages.
- Statistics ch15-003 (CRISPR) and ch15-007 (cloning) moved to ch16-009 and ch16-010 respectively
- References [src-131], [src-134], [src-138] moved to Chapter 16 as [src-153], [src-154], [src-155]
- **Updated README.md**: Domain count from fifteen to sixteen, updated Ch15 description, added Ch16 row
- **Strengthened Chapter 12 (Cognitive Defense)**: Expanded from 6 sections (12.1–12.6) to 11 sections (12.1–12.11), integrating CCP cognitive warfare structural analysis including four-layer command structure, supply chain infrastructure, platform infiltration, economic coercion, and institutional co-optation
- **Renamed Chapter 12**: "Cognitive Defense" → "Cognitive Defense — CCP Cognitive Warfare, Deepfake Threats, and Social Trust Infrastructure"
- **Expanded Chapter 12 Section 12.1**: Added CCP four-layer command structure subsection (Party → Military → Enterprise → Shadow)
- **Expanded Chapter 12 Section 12.3** (formerly 12.2): Added 2024 Taiwan election AI interference case study
- **Renumbered Chapter 10**: Section 10.5 (Policy Recommendations) → 10.6 to accommodate new BCI section
- **Updated README.md**: Domain count from thirteen to fifteen, updated Ch12 description, added Ch15 row
- **Updated Executive Summary**: Revised Ch12 description and added Ch15 domain row in both languages
- **Updated cross-chapter linkages** in Ch14 to reference Ch15
- **Updated verification reports** (both languages) to reflect new chapter and data counts

### Fixed

- Fixed ch12-references.md header (incorrectly stated "Chapter 11" instead of "Chapter 12")

### Previous Changes

- **Reorganized Chapter 14**: Dissolved the catch-all "Forward Strategy" chapter; redistributed content to thematically appropriate locations
  - Controlled nuclear fusion (14.1) → Chapter 5, Section 5.5
  - Long-distance energy transmission (14.2) → Chapter 5, Section 5.6
  - National blockchain infrastructure (14.3) → Chapter 8, Section 8.5
  - UAP investigation (14.4) remains as standalone Chapter 14, renamed "Non-Traditional Security Threats"
- **Renamed Chapter 8**: "Financial Resilience" → "Financial and Digital Resilience" to reflect expanded blockchain coverage
- **Renamed Part VI**: "Society & International" → "Society, International, and Emerging Domains"; absorbed Chapter 14 (eliminated Part VII)
- **Updated Executive Summary**: Domain overview table now reflects all 14 chapters with accurate descriptions
- **Renumbered sections**: Ch5 (5.5→5.7, 5.6→5.8, 5.7→5.9) and Ch8 (8.5→8.6, 8.6→8.7) to accommodate new content

### Fixed

- Corrected cross-chapter linkage labels in Chapters 2, 3, and 4 (wrong chapter numbers/names for Communications Resilience, Cognitive Defense, and International Linkages)
- Fixed satellite communications reference in Ch7 policy recommendations (pointed to Ch8 instead of Ch9)

### Added

- 6 new policy recommendations in Chapter 5 (items 17-22: fusion funding, HVDC feasibility, international fusion R&D, superconducting cable pilot, commercial fusion participation, SBSP demonstration)
- 5 new policy recommendations in Chapter 8 (items 13-17: DID pilot, land registry pilot, post-quantum blockchain, strategy office, national blockchain deployment)
- 8 UAP-focused policy recommendations in Chapter 14 (across 3 time horizons)
- Cross-chapter linkage sections for new Ch5 and Ch8 content
- 7 new statistics entries in ch05-energy-stats.json (fusion and energy transmission data)
- 2 new statistics entries in ch08-financial-statistics.json (blockchain precedent data)
- Energy and blockchain source references added to ch05-references.md and ch08-references.md

## [1.0.0] - 2026-03-16

### Added

- Initial release of 12 chapters + 1 supplement covering Taiwan's multi-domain national strategy
- Complete bilingual content (正體中文 and English)
- Structured statistics data (JSON) with source citations for all chapters
- Historical timeline datasets (CSV)
- Cross-country comparison datasets (CSV)
- Master bibliography with 100+ annotated references
- Data verification reports (bilingual)
- JSON Schema for data validation
