# Revision Plan

## 台灣國家戰略專案修正計劃 v1

狀態：Implemented on `codex/docs/ch16-content-strengthening`
日期：2026-03-31

> 進度摘要：Phase 1 至 Phase 5 已完成首輪落地，包含 metadata residue 清理、證據分層欄位與 validator 升級、README / 全文分層、Ch07 / Ch14 / Ch16 證據邊界補強，以及 AI 協作揭露與 PR 模板更新。

---

## 1. 目的

本修正計劃的目的，不是單純增加內容量，而是提升整體作品的：

- 結構收斂度
- 證據分層清晰度
- metadata 一致性
- 外部引用可信度
- 協作流程透明度

本次修正將優先處理已知不一致與最容易削弱可信度的問題，再進一步處理範圍分層、章節內推論邊界，以及 AI 協作揭露。

---

## 2. 主要問題

根據目前的外部閱讀回饋與專案自我檢查，主要問題如下：

1. 全文雖已形成 17 章架構，但核心戰略、治理延伸與前瞻模組之間仍可再分層。
2. 統計資料目前主要以 `verified: true` 呈現，尚未充分區分官方統計、估計值、政策目標與推論型判斷。
3. 機器可讀 metadata 與部分檔名仍有舊版 residue，會折損作品嚴整度。
4. 部分章節的 inference boundary 還不夠清楚，容易被外部讀者視為推論跨度較大。
5. 專案已實際使用 AI 協作工具，但尚未建立一致、公開、可供外部理解的揭露方式。

---

## 3. 修正原則

- 先修一致性，再修擴充性。
- 先修可驗證性，再修敘事完整性。
- 不為了降低爭議而刪除重要議題，但要清楚標示哪些屬於核心戰略、哪些屬於治理延伸、哪些屬於前瞻規劃。
- AI 工具可作為研究、整理、翻譯、編修與驗證輔助，但不得取代來源驗證、人類判讀與最終責任。

---

## 4. 修正階段

### Phase 1: Metadata 與結構一致性清理

目標：清除舊版殘留資訊，讓 repo 對外呈現與實際內容一致。

工作項目：

- 更新 `CITATION.cff`，將舊版 `twelve domains plus a supplement` 改為目前 17 章架構。
- 清理 `references/bibliography.json` 中殘留的舊式標記，例如 `S1`。
- 將 `data/statistics/ch16-forward-strategy-stats.json` 改名為與現行章名一致的檔名。
- 全 repo 搜尋舊版章節數描述，例如 `12`、`13`、`14`、`16` domains 等殘留文字。
- 檢查 `README`、verification reports、`CITATION.cff`、`CHANGELOG`、統計檔名與引用表述是否一致。

完成標準：

- 對外可見文件與機器可讀檔案都反映同一版章節結構。
- 不再出現舊版章節數、舊命名或混用描述。

### Phase 2: 證據分層與驗證標記升級

目標：讓「有來源」和「證據強度高」這兩件事分開呈現。

工作項目：

- 在 statistics schema 中新增欄位，例如：
  - `evidence_tier`
  - `claim_type`
  - `confidence_level`
  - `verification_mode`
- 將現有 `verified: true` 保留為基本欄位，但不再單獨代表證據強度。
- 在驗證報告中新增說明，區分官方統計、機構報告、商業估計、政策目標與分析推論的層級意義。
- 更新 validator，使缺少新欄位的統計資料會被標記或警告。
- 在 verification reports 中增加「可追溯性」與「證據強度」的區分表。

完成標準：

- 外部讀者能直接看出哪些資料是硬統計、哪些是估計值、哪些是分析推論。
- `verified` 不再被誤解為一律代表高強度證據。

### Phase 3: 全文範圍分層

目標：避免廣度削弱焦點，保留內容完整性但提升閱讀導向。

工作項目：

- 在 `README`、執行摘要、第 17 章統一加入三層架構：
  - 核心國安主戰略模組
  - 治理與社會韌性延伸模組
  - 前瞻與低機率高衝擊模組
- 明確說明哪些章節屬於近期政策優先事項，哪些屬於制度治理議題，哪些屬於長期前瞻規劃。
- 在章節總覽中加入簡短標記，例如 `Core`、`Governance Extension`、`Foresight Module`。

完成標準：

- 讀者第一次進入 repo 就能理解哪些章節是核心、哪些是延伸。
- `README`、執行摘要與第 17 章的分類講法一致。

### Phase 4: 高爭議章節的 Inference Boundary 精修

目標：降低外部讀者對推論跨度的疑慮。

優先章節：

- Chapter 7 生物安全
- Chapter 14 科技倫理
- Chapter 16 異常空域治理與戰略前瞻

工作項目：

- 在章首增加證據邊界說明。
- 在正文中區分：
  - 已知事實
  - 合理推論
  - 情境假設
  - 政策含意
- 避免將不同證據強度的素材直接放進同一條敘事鏈。
- 對較高爭議段落加上更清楚的來源說明與限定語氣。

完成標準：

- 每章都能清楚回答哪些是可驗證事實、哪些是分析性推論。
- 外部讀者較不容易把章節視為 inference jump 過大。

### Phase 5: AI 協作工具揭露與方法透明化

目標：提高專案透明度，避免外界對研究流程產生誤解。

工作項目：

- 在 `README` 新增 `AI Collaboration Disclosure` 或 `AI 協作說明` 區塊。
- 在 `CONTRIBUTING.md` 新增 AI 協作工具揭露規範。
- 在 PR template 或 commit / PR 說明中加入：
  - 是否使用 AI 工具
  - 用於哪個環節
  - 是否經人工核對
- 在專案層級明確說明：
  - AI 工具可用於結構整理、語句修訂、翻譯、程式驗證、引用檢查與資料整理輔助
  - AI 工具不作為權威來源本身
  - 最終判讀、引文選擇、論點責任由作者或貢獻者承擔

建議揭露內容至少包含：

- 使用過哪些 AI 工具
  - 例如：ChatGPT、Claude、Codex、GitHub Copilot、Perplexity 或其他檢索輔助工具
- 使用範圍
  - 例如：文稿編修、結構調整、翻譯、validator 撰寫、引用檢查、資料整理
- 人工覆核聲明
  - 例如：所有最終文字、資料引用與政策判斷均須經人工審閱與負責

建議基準文字：

> 本專案在研究整理、語句修訂、翻譯、程式驗證與結構編修過程中，可能使用各類 AI 協作工具作為輔助，包括但不限於 ChatGPT、Claude、Codex、GitHub Copilot、Perplexity 等。AI 工具不作為事實來源本身，所有引用、數據、論點與最終發布內容，均由人工審閱與承擔責任。

完成標準：

- 外部讀者知道 AI 在本專案中扮演的是輔助角色，而非權威來源。
- 後續貢獻者有一致的揭露規範可遵循。

---

## 5. 建議 PR 拆分

- `fix(metadata): align citation, bibliography tags, and chapter file naming`
- `refactor(validation): add evidence tiers and verification labels`
- `docs(structure): layer core strategy, governance, and foresight modules`
- `docs(evidence): tighten inference boundaries in high-risk chapters`
- `docs(governance): add AI collaboration disclosure and contribution policy`

---

## 6. 執行順序

建議依下列順序執行：

1. 先合併目前已完成的結構性修正內容。
2. 優先處理 metadata residue。
3. 升級證據分層與 validator。
4. 統一全文範圍分層。
5. 最後精修高爭議章節與 AI 揭露文件。

此順序的原因是：先把專案對外可見的一致性修好，再提升證據表達能力，最後處理敘事邊界與治理說明，能用最低成本換取最大的可信度提升。

---

## 7. 預期成果

完成上述修正後，專案將更接近一個可被外部穩定引用的研究型 repo，而不只是高完成度的個人戰略分析文件。最直接的提升將體現在：

- 外部讀者第一眼的信任感
- 引用時的嚴整度
- 爭議章節的可辯護性
- 多人協作時的方法透明度
- 後續維護與擴充的可持續性

---

## 8. 備註

本計劃為工作底稿，後續可隨修正進度調整。若個別修正項在實作中出現更高優先級的相依問題，應以維持全 repo 一致性與驗證能力為優先。
