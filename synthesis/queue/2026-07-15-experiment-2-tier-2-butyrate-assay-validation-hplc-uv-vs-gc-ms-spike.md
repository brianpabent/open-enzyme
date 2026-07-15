---
type: experiment
sweep_date: 2026-07-15
sweep_sha: eeab5b5
section_index: 2
global_index: 8
pass3_verdict: Partial
sweep_id: a68eaeb8939b91ac9d0bf42c
source_synthesis_sha256: 53af1a8e881d713ef1848bffb135b54373df151770468ed91af430aa101dad9b
canonical_items_sha256: 20f08e5cdb1aee45b8ae8e210dba3c1233c597013d00f26e65f8ef5db30b390f
overlap_tag: EXTENSION
---

# Tier 2 butyrate assay validation — HPLC-UV vs. GC-MS spike/recovery on culture supernatant

2. **Tier 2 butyrate assay validation — HPLC-UV vs. GC-MS spike/recovery on culture supernatant.** Per comp-038 next-step recommendation, validate De Baere 2013 HPLC-UV (direct UV 210 nm, no derivatization, validated on bacterial culture supernatant) against GC-MS using sodium-butyrate spike/recovery in OE-relevant culture matrices. **Cost:** $500. **Time:** 2 weeks. **Decides:** whether a decentralizable Tier 2 ruler exists for culture-supernatant butyrate (engineered-strain work) or whether GC-MS remains the only validated Tier 3 anchor. If GREEN, adopt HPLC-UV as Tier 2 for culture supernatant and update the genotype-informed-supplement-workflow.md Q141K example to reflect the closed gap. **[CHAIN-DEPTH: 2]** **[PHASE-A-MATCH: partial]** (the workflow page documents the gap but the quantification-ladder.md framework does not yet name it as a class-level limitation).  
   - *Documents Connected:* `tier-2-butyrate-assay-audit-computational.md`, `quantification-ladder.md`, `genotype-informed-supplement-workflow.md`, `open-questions.md`  
   - *Page-pair linkage:* Weak — tier-2-butyrate-assay-audit-computational.md and genotype-informed-supplement-workflow.md do not cross-reference each other; both link to quantification-ladder.md but not to each other.  
   - *Why It Matters:* This is the first class-level methodology gap surfaced by the workflow. It means every gut-microbiome intervention (including the Q141K butyrate-emphasis stack) operates under an unverified dose variable. The gap is not a workflow failure — the workflow successfully blocks silent underdosing for non-microbiome compounds — but it reveals that the quantification ladder is incomplete for microbiome-derived metabolites. Closing it for butyrate would unlock the QC loop for the entire class.  
   - *Suggested Action:* Run the empirical spike/recovery validation of HPLC-UV vs. GC-MS on culture supernatant as [validation-experiments.md §1.31](./validation-experiments.md). If GREEN, adopt HPLC-UV as Tier 2 for culture supernatant and update the workflow page to reflect the closed gap.

> **Pass 3 review — Partial.** `[OVERLAP: EXTENSION]` `[GAP: tool-gap]` The Tier 2 butyrate HPLC-UV vs. GC-MS spike/recovery experiment is correctly scoped and the De Baere 2013 reference is verified in `quantification-ladder.md` ("HPLC-UV confirmed for culture supernatant"). The cost estimate ($500) and timeline (2 weeks) are reasonable. **However,** the synthesizer claims the `quantification-ladder.md` framework "does not yet name it as a class-level limitation" — this is incorrect. The `quantification-ladder.md` explicitly states: "Structural gap — extends beyond butyrate to all microbiome-derived metabolites (added 2026-05-21; promoted to named Platform / Strategic Open Question 2026-05-22)" and enumerates the affected classes (SCFAs, secondary bile acids, microbial indoles, TMAO). The class-level gap is explicitly named and promoted to a platform strategic question. The experiment remains correctly recommended, but the framing of the documentation gap should be corrected to "the quantification-ladder names the class-level gap but no validated Tier 2 assay exists for any microbiome-derived metabolite class."
