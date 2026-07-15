---
type: contradiction
sweep_date: 2026-07-15
sweep_sha: eeab5b5
section_index: 1
global_index: 5
pass3_verdict: Confirmed
sweep_id: a68eaeb8939b91ac9d0bf42c
source_synthesis_sha256: 53af1a8e881d713ef1848bffb135b54373df151770468ed91af430aa101dad9b
canonical_items_sha256: 20f08e5cdb1aee45b8ae8e210dba3c1233c597013d00f26e65f8ef5db30b390f
overlap_tag: RESTATEMENT
---

# Butyrate Tier 2 assay infrastructure gap vs. workflow assumption

1. **Butyrate Tier 2 assay infrastructure gap vs. workflow assumption.** The genotype-informed supplement quantification workflow assumes a validated Tier 2 ruler for every compound class. For butyrate (and all microbiome-derived metabolites), no such Tier 2 exists — the only validated Tier 2 candidates are exposure proxies (stool SCFA panel) rather than input-potency verification. This breaks the "calibrate once at Tier 3, track batches at Tier 2" discipline for every gut-microbiome-mediated intervention (PDB, Houttuynia, prebiotic fiber). **[CHAIN-DEPTH: 2]** **[PHASE-A-MATCH: partial]** (the workflow page documents the gap but the quantification-ladder.md framework does not yet name it as a class-level limitation).  
   - *Locations:* `genotype-informed-supplement-workflow.md` §"Tier 2 assay gap for microbiome-derived metabolites", `quantification-ladder.md`, `tier-2-butyrate-assay-audit-computational.md`, `open-questions.md` §"Class-level Tier 2 assay gap for microbiome-derived metabolites"  
   - *Analysis:* The workflow successfully blocks silent underdosing for non-microbiome-mediated compounds and fails to block it for microbiome-mediated ones. The gap is not a workflow failure — it is a class-level methodology gap. Closing it for butyrate would unlock the QC loop for the entire class.

> **Pass 3 review — Confirmed.** `[OVERLAP: RESTATEMENT]` This is Item 3 restated as a Contradiction rather than a Connection — the butyrate Tier 2 assay gap vs. workflow assumption is the same substantive finding. The locations cited (`genotype-informed-supplement-workflow.md` §"Tier 2 assay gap for microbiome-derived metabolites", `quantification-ladder.md`, `tier-2-butyrate-assay-audit-computational.md`, `open-questions.md`) are all real and correctly identify the gap. The analysis that the workflow successfully blocks silent underdosing for non-microbiome compounds and fails to block it for microbiome-mediated ones is accurate. The PHASE-A-MATCH "partial" remains accurate — the workflow page documents the gap, and the quantification-ladder.md explicitly names the class-level limitation. No new content vs. Item 3; the contradiction framing is valid but the walkthrough should note the cross-reference rather than treating it as independent.
