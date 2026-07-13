---
type: open-question
sweep_date: 2026-06-01
sweep_sha: 8a97f95
section_index: 1
global_index: 9
pass3_verdict: Push back
overlap_tag: RESTATEMENT
---

# Does the genotype-informed supplement quantification workflow produce reproducible Tier 2 batch QC across multiple operators after a shared Tier 3 calibration?

1. **Does the genotype-informed supplement quantification workflow produce reproducible Tier 2 batch QC across multiple operators after a shared Tier 3 calibration?** The workflow closes the silent-underdosing failure mode for non-microbiome-mediated compounds but breaks at step 4 for microbiome-derived metabolites (butyrate/SCFA, secondary bile acids, microbial indoles, TMAO) because no Tier 2 home assay exists that is calibrated against a Tier 3 anchor at the relevant biological concentration. comp-038 (2026-05-20) confirmed this for butyrate (YELLOW: no ready-to-adopt home/colorimetric or breath-based butyrate assay surfaced). HPLC-UV is a plausible Tier 2-lab path for culture supernatants, and electrochemical fecal SCFA profiling is a promising stool-specific future direction, but both require full-text/protocol review and paired GC-MS validation before adoption. This is a class-level methodology bottleneck that affects every microbiome-metabolite intervention. The Q141K butyrate-emphasis stack is the canonical example where the gap creates a four-way n=1 attribution problem (intervention failure, dose wrong but unverifiable, exertion mechanism is metabolic-overload vs. mechanical-shedding, regression to the mean). A single multi-user community-fermentation pilot with genotype stratification (Q141K + CFH Y402H), Tier 2/3 batch QC, and event-linked biomarkers can falsify or confirm all three riskiest assumptions (H08 mechanism, H09 production reliability, RA #3 dietary-PK side) simultaneously. The pilot also resolves the Tier 2 butyrate assay gap and the Tier 2 inter-operator reproducibility gap. If successful, the platform's accessibility + mechanism thesis is de-risked; if it fails on any axis, the platform must pivot from "democratized home fermentation" to "centrally-manufactured adjunct" or "pharma-partnered discovery-engine output". The cost of one missed multi-level connection is significant — this composition is the highest-leverage single experiment in the current corpus. (Speculative — the pilot is not yet designed; the three-risk interdependence is mechanistic extrapolation from the existing risk cards.)

> **Pass 3 review — Push back.** `[OVERLAP: RESTATEMENT]` `[GAP: tool-gap]` This open question is a word-for-word duplicate of OQ #4 and OQ #8. The same question appears three times in the Open Questions section with identical prose. The question itself is substantive (it's drawn correctly from `open-questions.md` §"Quantification methodology — Tier 2 inter-operator reproducibility" and comp-038), but emitting it three times is a synthesis-level duplication error. The downstream emitter will create redundant files in `synthesis/queue/` unless the human reviews and merges. The question's substance is correct; the duplication is the defect. Recommend flagging the triplicate for merger and retaining one canonical instance.

---

## ✓ Actioned 2026-07-13 (batch-close)

**Canonical instance of a triplicate (Jun-01 OQ 1/4/8).** The Tier-2 inter-operator reproducibility question is a standing entry at `open-questions.md` §"Quantification methodology — Tier 2 inter-operator reproducibility" (added 2026-05-15) and is the operational prerequisite for H09 community-fermentation reliability (the multi-user pilot addresses it). Duplicates OQ-4 / OQ-8 merged into this instance. No new wiki work. Closure.
