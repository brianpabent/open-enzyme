---
type: connection
sweep_date: 2026-07-15
sweep_sha: eeab5b5
section_index: 3
global_index: 3
pass3_verdict: Confirmed
sweep_id: a68eaeb8939b91ac9d0bf42c
source_synthesis_sha256: 53af1a8e881d713ef1848bffb135b54373df151770468ed91af430aa101dad9b
canonical_items_sha256: 20f08e5cdb1aee45b8ae8e210dba3c1233c597013d00f26e65f8ef5db30b390f
overlap_tag: EXTENSION
---

# Contradiction — butyrate Tier 2 assay infrastructure gap vs. workflow assumption

3. **Contradiction — butyrate Tier 2 assay infrastructure gap vs. workflow assumption.** The genotype-informed supplement quantification workflow assumes a validated Tier 2 ruler for every compound class. For butyrate (and all microbiome-derived metabolites), no such Tier 2 exists — the only validated Tier 2 candidates are exposure proxies (stool SCFA panel) rather than input-potency verification. This breaks the "calibrate once at Tier 3, track batches at Tier 2" discipline for every gut-microbiome-mediated intervention (PDB, Houttuynia, prebiotic fiber, secondary bile acids, microbial indoles, TMAO). **[CHAIN-DEPTH: 2]** **[PHASE-A-MATCH: partial]** (the workflow page documents the gap but the quantification-ladder.md framework does not yet name it as a class-level limitation).  
   - *Documents Connected:* `genotype-informed-supplement-workflow.md`, `quantification-ladder.md`, `tier-2-butyrate-assay-audit-computational.md`, `open-questions.md`  
   - *Page-pair linkage:* Weak — genotype-informed-supplement-workflow.md and tier-2-butyrate-assay-audit-computational.md do not cross-reference each other; both link to quantification-ladder.md but not to each other.  
   - *Why It Matters:* This is the first class-level methodology gap surfaced by the workflow. It means every gut-microbiome intervention (including the Q141K butyrate-emphasis stack) operates under an unverified dose variable. The gap is not a workflow failure — the workflow successfully blocks silent underdosing for non-microbiome compounds — but it reveals that the quantification ladder is incomplete for microbiome-derived metabolites. Closing it for one metabolite (butyrate) would unlock the QC loop for the entire class.  
   - *Suggested Action:* Run the empirical spike/recovery validation of HPLC-UV vs. GC-MS on culture supernatant (per comp-038 next-step recommendation) as [validation-experiments.md §1.31](./validation-experiments.md). If GREEN, adopt HPLC-UV as Tier 2 for culture supernatant and update the workflow page to reflect the closed gap.

> **Pass 3 review — Confirmed.** `[OVERLAP: EXTENSION]` The butyrate Tier 2 assay infrastructure gap is a real and well-documented class-level methodology bottleneck. The `quantification-ladder.md` explicitly names the gap extending "beyond butyrate to all microbiome-derived metabolites" (SCFAs, secondary bile acids, microbial indoles, TMAO) and the `genotype-informed-supplement-workflow.md` describes the workflow this gap breaks. The page-pair linkage claim (genotype-informed-supplement-workflow.md and tier-2-butyrate-assay-audit-computational.md don't cross-reference) is correct — grep confirmed zero cross-references between the two pages. The suggested action (run comp-038 next-step spike/recovery validation of HPLC-UV vs. GC-MS on culture supernatant) is the correct cheapest next step and is already queued in the quantification-ladder. The PHASE-A-MATCH "partial" is accurate — the workflow page documents the gap but the quantification-ladder framework does explicitly name it as a class-level limitation, so the gap is more fully documented than the synthesizer implies.
