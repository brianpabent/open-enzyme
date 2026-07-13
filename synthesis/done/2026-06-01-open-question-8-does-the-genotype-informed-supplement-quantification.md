---
type: open-question
sweep_date: 2026-06-01
sweep_sha: 8a97f95
section_index: 8
global_index: 16
pass3_verdict: Push back
overlap_tag: RESTATEMENT
---

# Does the genotype-informed supplement quantification workflow produce reproducible Tier 2 batch QC across multiple operators after a shared Tier 3 calibration?

8. **Does the genotype-informed supplement quantification workflow produce reproducible Tier 2 batch QC across multiple operators after a shared Tier 3 calibration?** The workflow closes the silent-underdosing failure mode for non-microbiome-mediated compounds but breaks at step 4 for microbiome-derived metabolites (butyrate/SCFA, secondary bile acids, microbial indoles, TMAO) because no Tier 2 home assay exists that is calibrated against a Tier 3 anchor at the relevant biological concentration. comp-038 (2026-05-20) confirmed this for butyrate (YELLOW: no ready-to-adopt home/colorimetric or breath-based butyrate assay surfaced). HPLC-UV is a plausible Tier 2-lab path for culture supernatants, and electrochemical fecal SCFA profiling is a promising stool-specific future direction, but both require full-text/protocol review and paired GC-MS validation before adoption. This is a class-level methodology bottleneck that affects every microbiome-metabolite intervention. The Q141K butyrate-emphasis stack is the canonical example where the gap creates a four-way n=1 attribution problem (intervention failure, dose wrong but unverifiable, exertion mechanism is metabolic-overload vs. mechanical-shedding, regression to the mean). A single multi-user community-fermentation pilot with genotype stratification (Q141K + CFH Y402H), Tier 2/3 batch QC, and event-linked biomarkers can falsify or confirm all three riskiest assumptions (H08 mechanism, H09 production reliability, RA #3 dietary-PK side) simultaneously. The pilot also resolves the Tier 2 butyrate assay gap (comp-038 YELLOW) and the Tier 2 inter-operator reproducibility gap. If successful, the platform's accessibility + mechanism thesis is de-risked; if it fails on any axis, the platform must pivot from "democratized home fermentation" to "centrally-manufactured adjunct" or "pharma-partnered discovery-engine output". The cost of one missed multi-level connection is significant — this composition is the highest-leverage single experiment in the current corpus. (Speculative — the pilot is not yet designed; the three-risk interdependence is mechanistic extrapolation from the existing risk cards.)

> **Pass 3 review — Push back.** `[OVERLAP: RESTATEMENT]` `[GAP: tool-gap]` Third duplicate of the Tier 2 inter-operator reproducibility question (same as OQ #1 and #4). Merge all three. The per-item analysis: the question is correctly drawn from `open-questions.md` and comp-038, and the gap is real, but triplicating it dilutes the queue.

---

## ✓ Actioned 2026-07-13 (batch-close)

**Duplicate of Jun-01 OQ-1** (Tier-2 inter-operator reproducibility). Merged away; canonical instance = the standing `open-questions.md` entry (see OQ-1 closure). No separate wiki work. Closure.
