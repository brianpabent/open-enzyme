---
type: open-question
sweep_date: 2026-05-16
sweep_sha: 91acf49
section_index: 2
global_index: 13
pass3_verdict: Confirmed
overlap_tag: EXTENSION
---

# Can the genotype-informed supplement quantification workflow's Tier 2 batch QC step be extended to microbiome-derived metabolites (butyrate, SCFAs) with a validated home assay?

2. **Can the genotype-informed supplement quantification workflow's Tier 2 batch QC step be extended to microbiome-derived metabolites (butyrate, SCFAs) with a validated home assay?** The workflow's Q141K worked example uses stool SCFA panel as an indirect proxy for butyrate delivery — not a direct potency measurement. The quantification ladder's "calibrate once at Tier 3, track batches at Tier 2" discipline breaks when there's no Tier 2 assay for the compound. Is there a colorimetric, enzymatic, or breath-hydrogen proxy for colonic butyrate that could be validated against Tier 3 GC-MS? This is a methodology gap that affects not just the Q141K use case but any future intervention relying on microbiome-derived metabolites. (context: `genotype-informed-supplement-workflow.md`, `quantification-ladder.md`, `purine-degrading-bacteria.md`)

> **Pass 3 review — Confirmed.** `[OVERLAP: EXTENSION]` The methodology gap is real and correctly scoped. `genotype-informed-supplement-workflow.md` treats stool SCFA as the available but indirect Q141K/butyrate readout, while `quantification-ladder.md` defines Tier 2 as cheap batch tracking after a Tier 3 calibration, not as a universal direct-potency assay. A validated home/community Tier 2 butyrate proxy would strengthen the workflow beyond Q141K and apply to any microbiome-derived metabolite intervention.

---

**WALKED 2026-05-19 — Closed (duplicate of [[2026-05-16-connection-2-the-genotype-informed-supplement-quantification-workflow]]).**

Same Tier 2 methodology gap, framed as open question rather than connection. Named in `genotype-informed-supplement-workflow.md` Open Follow-Ups during the 2026-05-19 walkthrough; full closure context in the canonical entry.
