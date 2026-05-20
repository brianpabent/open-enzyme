---
type: connection
sweep_date: 2026-05-20
sweep_sha: 5cafe11
section_index: 5
global_index: 5
pass3_verdict: Confirmed, prioritize
overlap_tag: RESTATEMENT
---

# The Tier 2 butyrate assay gap identified in the genotype‑informed‑supplement‑quantification workflow creates a methodology bottleneck that applies across *all* future microbiome‑derived metabolite interventions (SCFAs, bile acids, indoles) — the quantification‑ladder framework currently has no validated Tier 2 home assay for any of them, which silently undermines every personalised‑medicine workflow that depends on dose‑verification of microbiome‑produced compounds.

5. **The Tier 2 butyrate assay gap identified in the genotype‑informed‑supplement‑quantification workflow creates a methodology bottleneck that applies across *all* future microbiome‑derived metabolite interventions (SCFAs, bile acids, indoles) — the quantification‑ladder framework currently has no validated Tier 2 home assay for any of them, which silently undermines every personalised‑medicine workflow that depends on dose‑verification of microbiome‑produced compounds.**  
   *Supported (by the documented absence of a butyrate colorimetric assay).* `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: partial]`

   - *Documents Connected:* `genotype-informed-supplement-workflow.md` (Tier 2 butyrate gap, worked example), `quantification-ladder.md` (the framework that needs a new assay class), `purine-degrading-bacteria.md` (butyrate concentration gap at the enterocyte nucleus), `validation-experiments.md` §1.14 (butyrate dose‑response arm that would provide the Tier 3 GC‑MS anchor).  
   - *Page‑pair linkage:* The butyrate gap is named in `genotype‑informed‑supplement‑workflow.md` but **not** connected to the broader methodological risk that any microbiome‑metabolite intervention (future engineered LBP butyrate‑boost strains, bile‑acid modulators, indole‑based AhR agonists) would face the same quantification bottleneck. The `quantification‑ladder.md` framework does not address the special problem of microbiome‑derived metabolites (where the source is not a supplement batch but an in‑vivo fermentation process).  
   - *Why It Matters:* The platform’s personalised‑medicine thesis (genotype → compound‑selection → batch‑QC → calibrated‑dose → biomarker‑tracking) breaks at the QC step for any intervention whose active molecule is produced *in situ* by gut bacteria. The workflow can verify that the precursor was administered (fiber, resistant starch, probiotic strain), but cannot verify that the downstream metabolite (butyrate) reached the target tissue at the intended concentration — the dose remains an unverified variable, indistinguishable from mechanism‑failure noise. Closing this gap with even *one* validated Tier 2 proxy (e.g., an enzyme‑coupled NADH‑readout butyrate assay calibrated against Tier 3 GC‑MS) would unlock the QC loop for every microbiome‑metabolite intervention the platform ever develops.  
   - *Suggested Action:* Add a dedicated methodology‑gap entry to `quantification‑ladder.md` (new section “Open gap: microbiome‑derived metabolites”) naming the three candidate Tier 2 paths (colorimetric, enzymatic, breath‑hydrogen proxy) and their current validation status. Queue a literature‑first desk audit (PubMed + patent search for “butyrate colorimetric assay” and “butyrate enzymatic assay”) before any wet‑lab development. Cross‑link from `genotype‑informed‑supplement‑workflow.md`.

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: RESTATEMENT]` This is a high-leverage operational fix even though the core gap is already stated in `genotype-informed-supplement-workflow.md` under “Tier 2 assay gap for microbiome-derived metabolites,” including SCFAs, bile acids, indoles, and the colorimetric / enzymatic / breath-hydrogen candidate paths. The inlined `quantification-ladder.md` does not yet carry that gap, so promoting it to the canonical quantification framework is the right single-source-of-truth move. This is low novelty but high platform-friction reduction.
