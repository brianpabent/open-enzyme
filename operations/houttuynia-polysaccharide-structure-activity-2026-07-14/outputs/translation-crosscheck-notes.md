# Two-model translation cross-check notes

Protocol: subagent (Claude Opus 4.8) = Model A (in-session reading); OpenRouter pays only for Model B (DeepSeek `deepseek-chat`, Chinese-vendor, native-language depth). Transport: `curl` (this machine's Python `urllib` has no working cert store for openrouter.ai; `local_curl_fetch`-style curl transport used for the OpenRouter POST too). Raw Model B outputs in `*.counterread.json`.

## Source 1 — `cqvip_frac4_HBHP_CHHP_DAHP_CAHP` (zh, CQVIP 2021)
Load-bearing claims: 4 sequential-extraction fractions (HBHP/CHHP/DAHP/CAHP); sugar contents 66.4/63.2/60.6/62.8%; uronic acid 29.6/22.6/18.5/11.6%; HBHP & CHHP = Rha:Ara:Glc:Gal 9.7:11.9:10.6:21.4 and 11.3:17.8:7.6:18.9; DAHP & CAHP = Ara:Xyl:Glc:Gal 14.1:17.0:9.0:13.8 and 6.6:37.5:9.9:6.3; HBHP → DEAE-purified HBHP-3 (397.4 kDa) + HBHP-4 (616.7 kDa).

**Model A vs Model B: FULL AGREEMENT on every number and on all structural terms.** No `[TRANSLATION-DISAGREEMENT]`. Independent corroboration that HBHP-3 = 397.4 kDa, matching the English primary source (Zou et al. 2022, PMID 35533845) exactly.

## Source 2 — `cqvip_gout_ferment_hyperuricemia` (zh, CQVIP patent)
Load-bearing claim (scope): a "medicine-food-homology enzyme/ferment for hyperuricemia and gout" is a microbial-consortium fermentation of **15 herbs**, of which *Houttuynia cordata* is **one** (alongside corn silk, kudzu, dandelion, chicory, etc.); claims to lower blood uric acid. It is **not** a purified polysaccharide, not oral-HCP-specific, not mechanistic (no MSU/NLRP3).

**Model A vs Model B: FULL AGREEMENT.** No disagreement. Confirms the "gout–Houttuynia" hits in the zh corpus are whole-herb/multi-herb functional-food or topical (外敷) uses — **not** the polysaccharide fraction.

## Net
Neither cross-check surfaced a tier-, dose-, or mechanism-changing disagreement. The zh sources are corroborative of the English primary-source catalog, and independently confirm the central evidence gap (no HCP-fraction gout/MSU study).
