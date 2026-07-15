# Query log — Houttuynia polysaccharide SAR lit-scan (2026-07-14)

## Query plan
`inputs/query-strategy.json` — `build_language_native_query_plan()` output, frame audit verdict `adequate` (all 4 native frames present: mechanism_native, species_original_language, traditional_formula, traditional_pathology). 272 queries across EN + zh/ja/ko.

## PubMed (bio-research MCP) — English, executed
- `Houttuynia cordata polysaccharide structure anti-inflammatory` → 6 hits
- `Houttuynia cordata polysaccharide complement` → 7 hits
- `Houttuynia cordata polysaccharide TLR4 macrophage` → 6 hits
- Targeted metadata/full-text pulls (PMID→PMC): 24528726, 29719782, 40654358, 31250410, 36252625, 35533845, 39899978, 39218180, 36549805, 26190353, 41751332

## East Asian — `local_curl_fetch()` dogfood (MANDATORY per skill)
| Host | Query | Result |
|---|---|---|
| **CQVIP** (www.cqvip.com) | 鱼腥草多糖 结构 抗炎 | **OK — 660 KB, 364× 鱼腥草, real SSR abstracts** |
| **CQVIP** | 鱼腥草 痛风 尿酸 | **OK — 680 KB; 89× 鱼腥草, 0× 多糖 (gout hits are whole-herb/ferment only)** |
| **CQVIP** | 鱼腥草多糖 尿酸钠 NLRP3 | OK — 198 KB; essentially no MSU×HCP results |
| **WanFang** (s.wanfangdata.com.cn) | 鱼腥草多糖 结构 抗炎 | Reached (200, 169 KB) but **Nuxt SPA shell — 0 rendered results** (JS-gated; results via separate XHR) |
| **Baidu Scholar** (xueshu.baidu.com) | 6 queries | Reached (200) but **redirected to CAPTCHA wall** (wappass.baidu.com/…/tuxing_v2.html, 1488 B). NOT bypassed (prohibited). |
| **CNKI** (kns.cnki.net) | 2 queries | **curl --fail → HTTP error** (bot-walled / JS-gated at HTTP layer) |
| **ChinaXiv** (www.chinaxiv.org) | 鱼腥草多糖 | **curl --fail → HTTP error** |

**Dogfood verdict:** `local_curl_fetch` reached CQVIP with genuine server-rendered content (the load-bearing East-Asian source for this scan). WanFang returned a JS shell (reached but no static results). Baidu = CAPTCHA wall even via local curl. CNKI + ChinaXiv failed at the curl layer. So for this topic CQVIP carried the zh evidence; the failures are honest bot-walls/JS-gating, not "language barrier."

## Two-model translation cross-check
DeepSeek `deepseek-chat` (Model B) counterread on the 2 load-bearing zh sources — both FULL AGREEMENT with Model A. See `translation-crosscheck-notes.md`.
