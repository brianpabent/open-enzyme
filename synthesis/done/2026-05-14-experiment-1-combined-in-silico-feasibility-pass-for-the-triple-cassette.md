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

---

## ✓ Actioned 2026-05-15 (closure note — comp-028 + comp-026 coupling sharpened)

The combined in silico feasibility pass is structurally already covered by **comp-028** (queued in Item 16 / 2026-05-14 Connection 1) — two-orthogonal-models requirement (chaperone framework + iWV1314 FBA) with explicit GREEN/YELLOW/RED decision rule and BioDesignBench evaluation-depth discipline.

**Pass 3's incremental ask** — explicit comp-026 coupling — landed via a one-line sharpening of comp-028's brief in `wiki/computational-experiments.md`:

- comp-028 decision rule upgraded from **two-axis** to **three-axis**: GREEN iff all three (chaperone + FBA + regulatory architecture per comp-026) pass. comp-028's verdict is now explicitly **conditional on comp-026's GREEN** — if comp-026 surfaces orthogonal-promoter requirements that the design hasn't adopted, comp-028's verdict downgrades accordingly.
- Cross-link to comp-026 added in comp-028's Informs/Cross-references column.
- Cross-link to `koji-endgame-strain.md` §3 third-cassette slot design rule added (the rule comp-028 operationalizes).

No new comp-NNN needed — comp-028 + comp-026 already exist; this item closes by tightening their coupling at the brief level.

Pass 3's "Confirmed" verdict held; the multi-axis discipline (per BioDesignBench evaluation-depth audit in `autonomous-screening-methodology.md`) is now preserved at the comp-028 brief level. Closing.
