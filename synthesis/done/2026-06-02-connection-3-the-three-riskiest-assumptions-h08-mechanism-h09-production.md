---
type: connection
sweep_date: 2026-06-02
sweep_sha: 405b50a
section_index: 3
global_index: 3
pass3_verdict: Partial
overlap_tag: RESTATEMENT
---

# The three riskiest assumptions (H08 mechanism, H09 production, dietary-CP0 PK) are now fully independent, falsifiable, and sequenced.

3. **The three riskiest assumptions (H08 mechanism, H09 production, dietary-CP0 PK) are now fully independent, falsifiable, and sequenced.** *Supported*. `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* hypotheses/H08-gut-lumen-sink-platform-thesis.md, hypotheses/H09-community-fermentation-reliability.md, open-questions.md §"Riskiest assumption #3", complement-c5a-gout.md §9.7–9.9, cross-validation.md Claim 1, cfh-mechanism-dissociation-cp0-candidates-computational.md, uricase-abcg2-genotype-stratification-computational.md (comp-019), upstream-complement-modulator-sweep-computational.md (comp-018), upstream-complement-verification-rerun-computational.md (comp-020), tier-2-butyrate-assay-audit-computational.md (comp-038), validation-experiments.md §1.14/1.25/1.28/1.30/1.31, self-experiment-protocol.md §12, genotype-informed-supplement-workflow.md, synthesis/strategic-reflections/2026-05-15-chassis-is-downstream-of-chokepoint.md
   - *Page-pair linkage:* Weakly connected pairs previously siloed (gut-lumen-sink.md ↔ complement-c5a-gout.md; cross-validation.md ↔ validation-experiments.md; hypotheses/H08 ↔ H09). Full 3+-link chain (mechanism risk + production risk + dietary-PK risk) emerges only when reading the riskiest-assumption history + the multi-track coverage maps + the comp-018/020/029/038/039 verification cascade together.
   - *Why It Matters:* Three independent failure modes now have separate killshot menus, pre-committed thresholds, and Phase 2 follow-ups. H08 (gut-lumen mechanism) can be falsified by Phase 2b RCT null without killing H09 (community-fermentation reliability). H09 can be falsified by multi-user CV >30% or strain-retention <95% at gen 5 without killing H08. Dietary-CP0 PK (RA #3) can be falsified by gut-luminal concentration below IC50 lower bound (or null UKB × AoU cross-tab) without killing either. The triplet is the platform's load-bearing risk surface; separating them prevents over-filtering (Pass 2 discipline) and allows independent progression. The dietary-CP0 arm is now the cheapest first killshot (P2-1 lit scan + comp-040 wet-lab, $0–2K); H09's multi-user pilot ($5–10K) and H08's ALLN-346 Study 202 re-analysis (FOIA) are sequenced after. This is the daemon's central non-linear synthesis: three previously scattered riskiest-assumption entries (2026-05-09, 2026-05-13, 2026-05-20) + the CP0 multi-track composition (§9.7–9.9) + the quantification-ladder methodology gap (comp-038 + genotype-informed-supplement-workflow.md step-4 caveat) compose into a single, sequenced, falsifiable platform-risk triple that was never named before. (source: all listed files; synthesis/strategic-reflections/2026-05-15-chassis-is-downstream-of-chokepoint.md)
   - *Suggested Action:* Update open-questions.md with the sequenced triplet (RA #1–3) as the new "Riskiest Assumptions" section (retired name removed per 2026-06-01 discipline). Queue comp-040 (CFH-depleted-serum MSU assay) and the ALLN-346 Study 202 re-analysis as immediate next experiments. Add the three H-cards (H08, H09, RA#3) to the hypotheses index with survival_count=0. Tag the dietary-CP0 stack in complement-c5a-gout.md §9.7–9.9 as "gated on comp-040 + biobank cross-tab".

> **Pass 3 review — Partial.** `[OVERLAP: RESTATEMENT]` `[GAP: tool-gap]` This item is a near-verbatim duplicate of item 1 — same title, same document list, same suggested actions. The underlying content is correct (the three-assumption triplet is accurately composed), but emitting the same finding twice is a synthesizer error that would create a second identical queue file and confuse the walkthrough. Recommended action: merge into item 1; do not emit as a separate file.

---

## ✓ Actioned 2026-07-13 (Item 11)

The "three riskiest assumptions falsified by one multi-user pilot" composition is a real risk **map** but not an execution plan: the three risks (H08 mechanism / H09 production / RA#3 dietary-CP0 PK) are independent, and one N=8–12 mega-assay conflates three decisions (one-experiment-one-decision). Parked with a scope + gating note at [`hypotheses/H09` §Status "Pilot parking note"](../../wiki/hypotheses/H09-community-fermentation-reliability.md): the pilot proper = H09 **P2-2** (production-reliability, N=5–10, H09-scoped); **execution gated on §1.9** (engineered strain doesn't exist yet); the **dietary-CP0 arm (RA#3) is the cheapest independent first killshot, needs no strain**, runs ahead. Marked "do not re-surface as a fresh to-do until a viable strain exists" to stop sweep re-emission. H08/H09/RA#3 standing entries already documented (closed in the 2026-07-13 batch). Closure.
