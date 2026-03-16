# 貢獻指南

**[English Version](./CONTRIBUTING.md)**

感謝您對本專案的關注。本文件提供貢獻指南。

## 如何貢獻

### 回報錯誤

若發現事實錯誤、過時統計數據或失效連結：

1. 開啟 Issue 描述錯誤內容
2. 註明章節編號與段落
3. 提供正確資訊及可驗證的來源

### 更新數據

統計數據與資料點需要來源驗證：

1. Fork 本倉庫
2. 更新 `data/statistics/` 中的相關 JSON 檔案
3. 確保每個資料點包含：指標、數值、單位、日期與來源 URL
4. 更新 `references/bibliography.json` 中的對應條目
5. 提交 Pull Request 並附上清晰說明

### 翻譯改進

修正或改善翻譯內容：

1. 找到 `chapters/en/` 或 `chapters/zh-TW/` 中的對應檔案
2. 確保修改與對應語言版本保持一致
3. 保留所有引用參考與資料表格

### 新增分析

提交實質性分析內容：

1. 先開啟 Issue 討論擬新增的內容
2. 遵循章節模板格式（參考任一現有章節）
3. 以 JSON 格式提供支持數據
4. 每個主要論點至少提供 3 個可驗證的參考來源

## 提交規範

本專案遵循 [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)。

```
<類型>(範圍): <描述>
```

類型：`docs`、`data`、`fix`、`feat`、`refactor`、`chore`

範例：
- `docs(ch02): update TSMC market share to Q4 2025 data`
- `data(statistics): add ch08 space capability metrics`
- `fix(references): correct broken DOI link for defense white paper`

## 資料格式標準

### 統計數據 JSON

所有統計檔案須符合 `data/schemas/statistics-schema.json` 定義。

### 時間線 CSV

欄位：`date`、`event`、`category`、`significance`、`source_id`、`notes`

### 參考文獻 JSON

每筆條目需包含：`id`、`type`、`title`、`authors`、`date`、`url`、`verified`

## 行為準則

貢獻內容應以事實為基礎、有證據支持且保持政治中立。本專案旨在提供客觀的戰略分析，而非倡導任何特定政治立場。
