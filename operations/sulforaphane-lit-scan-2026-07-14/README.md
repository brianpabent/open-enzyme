# Sulforaphane lit scan — post-2022 refresh (2026-07-14)

**Scope.** Refresh the primary literature on sulforaphane (SFN) for the gout / hyperuricemia / NLRP3-inflammation axis. The corpus's newest SFN citation is 2022 (Wang, *J Adv Res*, PMID 36371056). Goal: surface newer human/clinical data and any post-2022 mechanistic work on the three axes we already track — Nrf2 → NF-κB priming (CP1/CP2), Nrf2-independent inflammasome inhibition, and Nrf2 → ABCG2 gut-urate-sink induction.

**Why multilingual is load-bearing here.** Sulforaphane has a large Japanese research base (broccoli-sprout functional-food programs) and substantial Chinese nutraceutical/hyperuricemia literature (萝卜硫素 / 莱菔硫烷). Western-only PubMed coverage systematically undercounts both. Per OE CLAUDE.md §"Global-multilingual research by default."

**Query-framing note.** The frame audit flags a missing `traditional_formula` frame. That is **explicitly out of scope / N/A**: sulforaphane is an isolated nutraceutical, not a classical TCM/Kampo formula. East Asian coverage is carried by the **native-compound-name + species + native-pathology** frames (萝卜硫素 + 高尿酸血症/痛风; スルフォラファン + 高尿酸血症/痛風; 설포라판 + 고요산혈증/통풍). This is the documented "unless explicitly out of scope" exemption.

## P0 worklist

| # | Task | Status | Next action |
|---|------|--------|-------------|
| 1 | Western human/clinical refresh (2022→now): RCTs/trials of SFN or broccoli-sprout on urate/gout/inflammation markers; newest gout/HUA animal work | ✅ done | `trackA-western-clinical-2026-07-14.md` |
| 2 | Mechanistic depth refresh (2022→now): Nrf2-independent inflammasome, ABCG2/Q141K induction, epigenetic/HDAC, xanthine oxidase | ✅ done | `trackB-mechanistic-2026-07-14.md` |
| 3 | East Asian multilingual scan (zh/ja/ko) via local-curl + two-model counterread on load-bearing sources | ✅ done | `trackC-east-asian-2026-07-14.md` |
| 4 | Synthesis + evidence-tier delta vs. current corpus | ✅ done | `SYNTHESIS-2026-07-14.md` |
| 5 | Apply corpus edits to `wiki/` (5 proposed) | **awaiting Brian's go** | see SYNTHESIS §"Recommended corpus edits" |

## Artifact index

- `inputs/sulforaphane-query-plan.json` — native-language multi-frame query plan (output of `build_language_native_query_plan()` + native-name enrichment + frame audit).
- `outputs/` — one source-read / findings file per subagent (populated during the run).

## Discipline

- Shared library: `wiki/etc/experiments/lib/agentic_lit_synthesis.py` (`local_curl_fetch`, `counterread_source_single_model`). Subagent IS Model A; OpenRouter pays only for Model B counterread.
- Non-promotion caveats are first-class: a source that retrieves but isn't full-text or fails the agreement gate stays "discovery-positive, source-read pending" — it does NOT get promoted to an evidence tier in `wiki/`.
- Sweep daemon does NOT operate on `operations/`. Nothing here touches `wiki/` until synthesis (step 4) is reviewed with Brian.
