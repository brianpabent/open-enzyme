---
type: connection
sweep_date: 2026-05-16
sweep_sha: 91acf49
section_index: 2
global_index: 2
pass3_verdict: Confirmed
overlap_tag: EXTENSION
---

# The genotype-informed supplement quantification workflow (`genotype-informed-supplement-workflow.md`) and the gout genetic variants unified index (`gout-genetic-variants.md`) together form a complete pharmacogenomics decision surface — but the workflow's Q141K worked example exposes a quantification gap that the variants index doesn't address.

2. **The genotype-informed supplement quantification workflow (`genotype-informed-supplement-workflow.md`) and the gout genetic variants unified index (`gout-genetic-variants.md`) together form a complete pharmacogenomics decision surface — but the workflow's Q141K worked example exposes a quantification gap that the variants index doesn't address.** *Supported.* `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: partial]`
   - *Documents Connected:* `genotype-informed-supplement-workflow.md`, `gout-genetic-variants.md`, `abcg2-modulators.md`, `quantification-ladder.md`, `purine-degrading-bacteria.md`
   - *Page-pair linkage:* `genotype-informed-supplement-workflow.md` cross-references `gout-genetic-variants.md` (newly promoted page, 2026-05-16). But the workflow's Q141K worked example uses stool SCFA panel as a Tier 2 proxy for butyrate delivery — and `gout-genetic-variants.md` doesn't address the quantification gap for butyrate as an intervention. The variants index tells you *which* variant matters; the workflow tells you *how* to act on it; neither tells you *how to verify you delivered the intervention at the right dose* for butyrate specifically.
   - *Why It Matters:* The genotype-informed workflow is the platform's operational backbone for personalized medicine. Its Q141K worked example is the canonical use case. But the Tier 2 batch QC step for butyrate is an indirect proxy (stool SCFA), not a direct potency measurement. This is a structural gap in the workflow's verification chain for the platform's single most important genotype-stratified intervention. The gap exists because direct butyrate quantification requires GC-MS (Tier 3), and the workflow's "calibrate once at Tier 3, track batches at Tier 2" discipline breaks when there's no Tier 2 assay for the compound. This is not a failure of the workflow design — it's a genuine methodological limitation for SCFA-class interventions that the quantification ladder was not designed to address.
   - *Suggested Action:* Add a "Tier 2 gap" annotation to the Q141K worked example in `genotype-informed-supplement-workflow.md` explicitly noting that stool SCFA is an indirect proxy, not a direct potency measurement, and that this is a known limitation of the quantification ladder for microbiome-derived metabolites. Flag as an open question: "Can a Tier 2 home assay for butyrate (colorimetric, enzymatic, or breath-hydrogen proxy) be validated against Tier 3 GC-MS?" Queued in `open-questions.md`.

> **Pass 3 review — Confirmed.** `[OVERLAP: EXTENSION]` This correctly identifies a real operational gap: `genotype-informed-supplement-workflow.md` uses stool SCFA as an indirect butyrate-delivery readout, while `quantification-ladder.md` defines Tier 2 as batch tracking against a Tier 3 anchor rather than a direct GC-MS-grade metabolite assay. The suggested “Tier 2 gap” annotation is warranted because SCFA stool panels verify downstream exposure imperfectly, not supplement potency or enterocyte-nuclear butyrate concentration.

---

**WALKED 2026-05-19 — Closed (Tier 2 methodology gap named in `genotype-informed-supplement-workflow.md` Open Follow-Ups).**

Actioned:
- ✓ Added new "Tier 2 assay gap for microbiome-derived metabolites" subsection to `wiki/genotype-informed-supplement-workflow.md` Open Follow-Ups section. Names the gap explicitly: stool SCFA verifies downstream exposure, not direct potency at the relevant biological concentration. Three candidate Tier 2 paths listed (colorimetric, enzymatic, breath-hydrogen proxy), none validated as of 2026-05-19. Generalized beyond Q141K/butyrate to all microbiome-derived metabolites (SCFAs, bile acids, indoles, lactate).
- The Q141K worked-example step 4 already qualifies SCFA as "indirect proxy, not direct quantification" (line 107 of workflow.md); the new subsection elevates this from inline caveat to named methodology question tracked at the platform's quantification-ladder track.

Also closes:
- 2026-05-16 open-question-2 (same gap, framed as open question).
