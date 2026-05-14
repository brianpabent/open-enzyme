---
type: experiment
sweep_date: 2026-05-14
sweep_sha: 81e6264
section_index: 1
global_index: 6
pass3_verdict: Confirmed
overlap_tag: EXTENSION
---

# Combined in silico feasibility pass for the triple-cassette strain (uricase + lactoferrin + cordycepin).

1. **Combined in silico feasibility pass for the triple-cassette strain (uricase + lactoferrin + cordycepin).** Cost: $0 (computational). Time: 1–2 weeks. Decides: whether the triple-cassette design passes both the chaperone-orthogonal-stacking framework (PDI axis) and the iWV1314 FBA (metabolic axis) before committing wet-lab resources. Inputs: comp-022 top uricase cassette, comp-010 lactoferrin cassette, comp-023 cns1+cns2 parameters. Output: a unified feasibility verdict with predicted titers and burden metrics.

> **Pass 3 review — Confirmed.** `[OVERLAP: EXTENSION]` A unified in silico feasibility pass is justified, because the current evidence is split across axes: `uricase-cassette-ranking-computational.md` refines the uricase cassette, `chaperone-orthogonal-stacking.md` handles ER/PDI burden, and `cordycepin-cassette-burden-computational.md` handles cytosolic FBA burden. The experiment is low-cost and mainly functions as an integration check before adding a wet-lab arm; it should explicitly include the unresolved promoter/induction-interference gate that `computational-experiments.md` queues as comp-026.
