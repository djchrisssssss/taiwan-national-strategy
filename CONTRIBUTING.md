# Contributing / 貢獻指南

Thank you for your interest in contributing to this project. This document provides guidelines for contributions.

感謝您對本專案的關注。本文件提供貢獻指南。

---

## How to Contribute / 如何貢獻

### Reporting Errors / 回報錯誤

If you find factual errors, outdated statistics, or broken references:

若發現事實錯誤、過時統計數據或失效連結：

1. Open an issue describing the error / 開啟 Issue 描述錯誤內容
2. Include the chapter number and section / 註明章節編號與段落
3. Provide the correct information with a verifiable source / 提供正確資訊及可驗證的來源

### Updating Data / 更新數據

Statistics and data points require source verification:

統計數據與資料點需要來源驗證：

1. Fork the repository / Fork 本倉庫
2. Update the relevant JSON file in `data/statistics/` / 更新 `data/statistics/` 中的相關 JSON 檔案
3. Ensure every data point includes: metric, value, unit, date, and source URL / 確保每個資料點包含：指標、數值、單位、日期與來源 URL
4. Update the corresponding entry in `references/bibliography.json` / 更新 `references/bibliography.json` 中的對應條目
5. Submit a pull request with a clear description / 提交 Pull Request 並附上清晰說明

### Translation Improvements / 翻譯改進

For translation corrections or improvements:

修正或改善翻譯內容：

1. Identify the file in `docs/en/` or `docs/zh-TW/` / 找到 `docs/en/` 或 `docs/zh-TW/` 中的對應檔案
2. Ensure changes maintain consistency with the counterpart language file / 確保修改與對應語言版本保持一致
3. Preserve all citation references and data table entries / 保留所有引用參考與資料表格

### Adding New Analysis / 新增分析

For substantive analytical contributions:

提交實質性分析內容：

1. Open an issue first to discuss the proposed addition / 先開啟 Issue 討論擬新增的內容
2. Follow the chapter template format (see any existing chapter) / 遵循章節模板格式（參考任一現有章節）
3. Include supporting data in JSON format / 以 JSON 格式提供支持數據
4. Provide at least 3 verifiable references per major claim / 每個主要論點至少提供 3 個可驗證的參考來源

---

## Commit Convention / 提交規範

This project follows [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/).

本專案遵循 [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)。

```
<type>(scope): <description>
```

Types 類型: `docs`, `data`, `fix`, `feat`, `refactor`, `chore`

Examples 範例:
- `docs(ch02): update TSMC market share to Q4 2025 data`
- `data(statistics): add ch08 space capability metrics`
- `fix(references): correct broken DOI link for defense white paper`

---

## Data Format Standards / 資料格式標準

### Statistics JSON / 統計數據 JSON

All statistics files must conform to `data/schemas/statistics-schema.json`.

所有統計檔案須符合 `data/schemas/statistics-schema.json` 定義。

### Timeline CSV / 時間線 CSV

Columns 欄位: `date`, `event`, `category`, `significance`, `source_id`, `notes`

### Bibliography JSON / 參考文獻 JSON

Each entry requires 每筆條目需包含: `id`, `type`, `title`, `authors`, `date`, `url`, `verified`

---

## Code of Conduct / 行為準則

Contributions should be factual, evidence-based, and politically neutral. This project aims to provide objective strategic analysis, not advocacy for any particular political position.

貢獻內容應以事實為基礎、有證據支持且保持政治中立。本專案旨在提供客觀的戰略分析，而非倡導任何特定政治立場。
