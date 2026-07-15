# Houttuynia polysaccharide structure→directionality lit scan (2026-07-14)

**Scope.** Resolve (as far as the literature allows) the *Houttuynia cordata* polysaccharide **fraction-directionality problem** — which structural feature predicts pro- vs anti-inflammatory — to inform wet-lab §1.30 (MSU-NLRP3 macrophage screen) Arm A selection and a pro-inflammatory-directionality safety caution, before spending $2K. Walk item 7 (Houttuynia).

**Artifact.** `logs/houttuynia-polysaccharide-structure-activity-lit-scan-2026-07-14.md`.

## Workspace
- `inputs/query-strategy.json` — multilingual query plan (`build_language_native_query_plan`, frame audit `adequate`).
- `inputs/model-config.json` — two-model translation routing (Model A = Claude subagent; Model B = DeepSeek).
- `build_query_plan.py`, `fetch_east_asian.py` — run scripts.
- `sources/` — fetched East-Asian HTML + provenance JSON (CQVIP SSR results are the load-bearing zh source; WanFang/Baidu/CNKI/ChinaXiv bot-walled — see query-log).
- `outputs/query-log.md` — full query + dogfood log.
- `outputs/translation-crosscheck-notes.md` + `outputs/*.counterread.json` — DeepSeek Model-B counterreads (both full agreement with Model A).

## Discipline
- Every load-bearing number (MW, monosaccharide ratios, CH50/IC50, receptor) grep-verified against its primary source before entering the artifact.
- Multilingual by default; `local_curl_fetch` mandatory for East-Asian hosts (dogfooded).
- Report-only: no `wiki/` or `validation-experiments.md` edits, no commit. Propagation happens in the main session after review.
