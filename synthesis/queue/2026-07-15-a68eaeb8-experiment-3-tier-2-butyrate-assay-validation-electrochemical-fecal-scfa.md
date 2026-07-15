---
type: experiment
sweep_date: 2026-07-15
sweep_sha: eeab5b5
section_index: 3
global_index: 9
pass3_verdict: Defer
sweep_id: a68eaeb8939b91ac9d0bf42c
source_synthesis_sha256: 53af1a8e881d713ef1848bffb135b54373df151770468ed91af430aa101dad9b
canonical_items_sha256: 20f08e5cdb1aee45b8ae8e210dba3c1233c597013d00f26e65f8ef5db30b390f
overlap_tag: NOVEL
---

# Tier 2 butyrate assay validation — electrochemical fecal SCFA profiling vs. GC-MS (stool track)

3. **Tier 2 butyrate assay validation — electrochemical fecal SCFA profiling vs. GC-MS (stool track).** Full-text verification of Gu et al. 2026 electrochemical-ANN (PMID 42041444) confirmed GC-MS-validated fecal cohort (n=30, butyric-acid MAE 0.029 mM) — a genuine stool-specific Tier-2 candidate. Validate spike/recovery against GC-MS using real stool samples to confirm butyrate-specific performance at mM-range colonic concentrations. **Cost:** $800–1,200. **Time:** 3 weeks. **Decides:** whether a stool-specific Tier 2 ruler exists for patient-facing butyrate monitoring, or whether GC-MS remains the only validated Tier 3 anchor for stool. **[CHAIN-DEPTH: 3+]** **[PHASE-A-MATCH: no]**  
   - *Documents Connected:* `tier-2-butyrate-assay-audit-computational.md`, `quantification-ladder.md`, `genotype-informed-supplement-workflow.md`, `open-questions.md`  
   - *Page-pair linkage:* Weak — tier-2-butyrate-assay-audit-computational.md and genotype-informed-supplement-workflow.md do not cross-reference each other; both link to quantification-ladder.md but not to each other.  
   - *Why It Matters:* The Tier 2 gap for microbiome-derived metabolites is a class-level methodology bottleneck that affects every gut-microbiome-mediated intervention on the platform (PDB, Houttuynia gut-microbiota arm, prebiotic-fiber-specific stack, secondary bile acids, microbial indoles, TMAO). Closing it for butyrate unlocks the QC loop for the entire class. The electrochemical fecal SCFA platform is the most promising stool-specific Tier-2 candidate; validating it against GC-MS is the cheapest next step.  
   - *Suggested Action:* Run the empirical spike/recovery validation of the electrochemical-ANN platform vs. GC-MS on real stool samples as a follow-on to comp-038. If GREEN, adopt as Tier 2 for stool and update the workflow page to reflect the closed gap for microbiome-derived metabolites.

> **Pass 3 review — Defer.** `[OVERLAP: NOVEL]` The experiment concept is a reasonable stool-track complement to Item 8's culture-supernatant track, and the electrochemical-ANN approach is a plausible stool-specific Tier 2 candidate. However, the central claim — "Gu et al. 2026 electrochemical-ANN (PMID 42041444) confirmed GC-MS-validated fecal cohort (n=30, butyric-acid MAE 0.029 mM)" — is a world-claim I cannot verify against the corpus (the paper is not inlined, and the corpus has no entry for this PMID). The "full-text verification" is a claim about the synthesis daemon's own work, not a corpus fact. The cost ($800–1,200) and timeline (3 weeks) are synthesis-generated. `[VERIFY: lit-scan]` Gu et al. 2026 electrochemical-ANN fecal SCFA profiling; validate PMID 42041444 exists, confirm the method is GC-MS-validated on real stool, and verify the butyrate-specific MAE claim. Route to scan before committing this experiment to the queue.
