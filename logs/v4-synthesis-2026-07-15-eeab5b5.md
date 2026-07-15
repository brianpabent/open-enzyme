---
title: "Synthesis — 2026-07-15 (commit eeab5b5)"
date: 2026-07-15
commit: eeab5b53054b93544c428a476dad06a8f8fe2621
diff_base: b52b9a893b6256d7d34eeb74e9a7748950bd7410
trigger_files: wiki/abcg2-modulators.md,wiki/abcg2-q141k-chaperone-rescreen-computational.md,wiki/abcg2-q141k-chaperone-screen-computational.md,wiki/c1-inh-protease-stability-ecn-computational.md,wiki/chaperone-orthogonal-stacking.md,wiki/chassis-pending-interventions.md,wiki/combined-cp0-systems-model-computational.md,wiki/complestatin-bgc-lbp-feasibility-computational.md,wiki/compounding-pharmacy-track.md,wiki/computational-experiments.md,wiki/cordycepin-cassette-burden-computational.md,wiki/daf-cd55-scr14-cassette-ranking-computational.md,wiki/daf-cd55-scr14-truncated-computational.md,wiki/daf-lactoferrin-ecn-folding-feasibility-computational.md,wiki/delivery-route-matrix.md,wiki/disulfiram-dose-modeling-computational.md,wiki/disulfiram.md,wiki/engineered-lbp-chassis.md,wiki/etc/chembl-cross-check.md,wiki/etc/experiments/comp-001-uricase-shio-koji-protease-stability/outputs/summary.md,wiki/etc/experiments/comp-006-daf-cd55-shio-koji-protease-stability/README.md,wiki/etc/experiments/comp-006-daf-cd55-shio-koji-protease-stability/outputs/summary.md,wiki/etc/experiments/comp-007-food-grade-hdaci-screen/README.md,wiki/etc/experiments/comp-007-food-grade-hdaci-screen/inputs/provenance.md,wiki/etc/experiments/comp-007-food-grade-hdaci-screen/outputs/summary.md,wiki/etc/experiments/comp-007-food-grade-hdaci-screen/wiki-archive.md,wiki/etc/experiments/comp-008-f-prausnitzii-heterologous-expression/README.md,wiki/etc/experiments/comp-008-f-prausnitzii-heterologous-expression/outputs/summary.md,wiki/etc/experiments/comp-008-f-prausnitzii-heterologous-expression/wiki-archive.md,wiki/etc/experiments/comp-009-urat1-sirna-target-site-selection/README.md,wiki/etc/experiments/comp-009-urat1-sirna-target-site-selection/outputs/summary.md,wiki/etc/experiments/comp-010-cassette-compatibility/README.md,wiki/etc/experiments/comp-010-cassette-compatibility/inputs/provenance.md,wiki/etc/experiments/comp-010-cassette-compatibility/outputs/summary.md,wiki/etc/experiments/comp-010-cassette-compatibility/wiki-archive.md,wiki/etc/experiments/comp-011-c-utilis-uricase-cassette-compatibility/README.md,wiki/etc/experiments/comp-011-c-utilis-uricase-cassette-compatibility/outputs/summary.md,wiki/etc/experiments/comp-015-t-axis-adjuvant-urate-mapping/README.md,wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/README.md,wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/outputs/flux_model_summary.md,wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/wiki-archive.md,wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/README.md,wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/v2/provenance.md,wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/wiki-archive.md,wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/README.md,wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/outputs/summary.md,wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs/summary.md,wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/outputs/summary.md,wiki/etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/README.md,wiki/etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/inputs/provenance.md,wiki/etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/outputs/summary.md,wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/outputs/summary.md,wiki/etc/experiments/comp-046-staged-purine-sink-mass-balance/README.md,wiki/etc/experiments/comp-046-staged-purine-sink-mass-balance/outputs/summary.md,wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/README.md,wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/inputs/provenance.md,wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/outputs/controls.md,wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/outputs/summary.md,wiki/etc/manual-literature-mining.md,wiki/genotype-informed-supplement-workflow.md,wiki/gout-action-guide.md,wiki/gout-genetic-variants.md,wiki/gsdmd-pore-delivery-paradox.md,wiki/gut-lumen-sink.md,wiki/hypotheses/H02-engineered-lbp-thesis.md,wiki/hypotheses/H03-sirna-urat1-thesis.md,wiki/inhaled-mrna-il1ra-pulse-computational.md,wiki/intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md,wiki/intra-articular-uricase-h2o2-reaction-diffusion-computational.md,wiki/lactoferrin-linker-redesign-computational.md,wiki/lactoferrin-protease-stability-computational.md,wiki/medicinal-mushroom-compound-mapping-computational.md,wiki/modality-chokepoint-matrix.md,wiki/nlrp3-exploit-map.md,wiki/nlrp3-inhibitor-screen.md,wiki/open-questions.md,wiki/purine-degrading-bacteria.md,wiki/quantification-ladder.md,wiki/repeat-dose-inhaled-mrna-il1ra-pkpd-computational.md,wiki/staged-purine-sink-mass-balance-computational.md,wiki/supplement-abcg2-antagonism-computational.md,wiki/supplements-stack.md,wiki/t-abcg2-suppression-evidence-mining-computational.md,wiki/tcm-gout-compound-triage-computational.md,wiki/tier-2-butyrate-assay-audit-computational.md,wiki/upstream-complement-assay-format-mapping-computational.md,wiki/upstream-complement-modulator-sweep-computational.md,wiki/upstream-complement-verification-rerun-computational.md,wiki/urat1-sirna-target-site-selection-computational.md,wiki/uricase-shio-koji-thermal-stability-computational.md,wiki/uricase-variant-selection.md,wiki/uricase.md,wiki/validation-experiments.md
reviewer_model: x-ai/grok-4.20
reviewer_model_served_raw: x-ai/grok-4.20
reviewer_model_requested: x-ai/grok-4.20
reviewer_fallback_used: False
input_tokens: 1936021
output_tokens: 10509
cost_usd: 2.4463
corpus_files: 130
---

**# Synthesis — 2026-07-15**

**Substrate:** Open Enzyme wiki at commit `eeab5b5`  
**Trigger files:** wiki/abcg2-modulators.md, wiki/abcg2-q141k-chaperone-rescreen-computational.md, wiki/abcg2-q141k-chaperone-screen-computational.md, wiki/c1-inh-protease-stability-ecn-computational.md, wiki/chaperone-orthogonal-stacking.md, wiki/chassis-pending-interventions.md, wiki/combined-cp0-systems-model-computational.md, wiki/complestatin-bgc-lbp-feasibility-computational.md, wiki/compounding-pharmacy-track.md, wiki/computational-experiments.md, wiki/cordycepin-cassette-burden-computational.md, wiki/daf-cd55-scr14-cassette-ranking-computational.md, wiki/daf-cd55-scr14-truncated-computational.md, wiki/daf-lactoferrin-ecn-folding-feasibility-computational.md, wiki/delivery-route-matrix.md, wiki/disulfiram-dose-modeling-computational.md, wiki/disulfiram.md, wiki/engineered-lbp-chassis.md, wiki/etc/chembl-cross-check.md, wiki/etc/experiments/comp-001-uricase-shio-koji-protease-stability/outputs/summary.md, wiki/etc/experiments/comp-006-daf-cd55-shio-koji-protease-stability/README.md, wiki/etc/experiments/comp-006-daf-cd55-shio-koji-protease-stability/outputs/summary.md, wiki/etc/experiments/comp-007-food-grade-hdaci-screen/README.md, wiki/etc/experiments/comp-007-food-grade-hdaci-screen/inputs/provenance.md, wiki/etc/experiments/comp-007-food-grade-hdaci-screen/outputs/summary.md, wiki/etc/experiments/comp-007-food-grade-hdaci-screen/wiki-archive.md, wiki/etc/experiments/comp-008-f-prausnitzii-heterologous-expression/README.md, wiki/etc/experiments/comp-008-f-prausnitzii-heterologous-expression/outputs/summary.md, wiki/etc/experiments/comp-008-f-prausnitzii-heterologous-expression/wiki-archive.md, wiki/etc/experiments/comp-009-urat1-sirna-target-site-selection/README.md, wiki/etc/experiments/comp-009-urat1-sirna-target-site-selection/outputs/summary.md, wiki/etc/experiments/comp-010-cassette-compatibility/README.md, wiki/etc/experiments/comp-010-cassette-compatibility/inputs/provenance.md, wiki/etc/experiments/comp-010-cassette-compatibility/outputs/summary.md, wiki/etc/experiments/comp-010-cassette-compatibility/wiki-archive.md, wiki/etc/experiments/comp-011-c-utilis-uricase-cassette-compatibility/README.md, wiki/etc/experiments/comp-011-c-utilis-uricase-cassette-compatibility/outputs/summary.md, wiki/etc/experiments/comp-015-t-axis-adjuvant-urate-mapping/README.md, wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/README.md, wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/outputs/flux_model_summary.md, wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/wiki-archive.md, wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/README.md, wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/v2/provenance.md, wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/wiki-archive.md, wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/README.md, wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/outputs/summary.md, wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs/summary.md, wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/outputs/summary.md, wiki/etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/README.md, wiki/etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/inputs/provenance.md, wiki/etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/outputs/summary.md, wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/outputs/summary.md, wiki/etc/experiments/comp-046-staged-purine-sink-mass-balance/README.md, wiki/etc/experiments/comp-046-staged-purine-sink-mass-balance/outputs/summary.md, wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/README.md, wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/inputs/provenance.md, wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/outputs/controls.md, wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/outputs/summary.md, wiki/etc/manual-literature-mining.md, wiki/genotype-informed-supplement-workflow.md, wiki/gout-action-guide.md, wiki/gout-genetic-variants.md, wiki/gsdmd-pore-delivery-paradox.md, wiki/gut-lumen-sink.md, wiki/hypotheses/H02-engineered-lbp-thesis.md, wiki/hypotheses/H03-sirna-urat1-thesis.md, wiki/inhaled-mrna-il1ra-pulse-computational.md, wiki/intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md, wiki/intra-articular-uricase-h2o2-reaction-diffusion-computational.md, wiki/lactoferrin-linker-redesign-computational.md, wiki/lactoferrin-protease-stability-computational.md, wiki/medicinal-mushroom-compound-mapping-computational.md, wiki/modality-chokepoint-matrix.md, wiki/nlrp3-exploit-map.md, wiki/nlrp3-inhibitor-screen.md, wiki/open-questions.md, wiki/purine-degrading-bacteria.md, wiki/quantification-ladder.md, wiki/repeat-dose-inhaled-mrna-il1ra-pkpd-computational.md, wiki/staged-purine-sink-mass-balance-computational.md, wiki/supplement-abcg2-antagonism-computational.md, wiki/supplements-stack.md, wiki/t-abcg2-suppression-evidence-mining-computational.md, wiki/t-axis-adjuvant-urate-mapping-computational.md, wiki/tcm-gout-compound-triage-computational.md, wiki/tcm-modern-rigor-intersection.md, wiki/tier-2-butyrate-assay-audit-computational.md, wiki/upstream-complement-assay-format-mapping-computational.md, wiki/upstream-complement-modulator-sweep-computational.md, wiki/upstream-complement-verification-rerun-computational.md, wiki/urat1-sirna-target-site-selection-computational.md, wiki/uricase-shio-koji-thermal-stability-computational.md, wiki/uricase-variant-selection.md, wiki/uricase.md, wiki/validation-experiments.md  
**Diff base:** b52b9a893b6256d7d34eeb74e9a7748950bd7410  
**Reviewer:** x-ai/grok-4.20

## Phase A — Enumerate what already exists (internal)

**Canonical wiki pages (main concepts, chokepoint maps, core protocols):**  
`abcg2-modulators.md` (ABCG2 levers + Q141K rescue), `androgen-urate-axis.md` (sex-hormone/transporter modulation + reframing), `chassis-pending-interventions.md` (non-koji modalities: LBP, siRNA, IA uricase, pharmacological chaperones for Q141K, T0SS-OMV, duckweed), `complement-c5a-gout.md` (CP0 complement priming + C5aR1 gap closure), `cross-validation.md` (feasibility ratings 5.5–8/10, H08/H09 riskiest assumptions), `engineered-koji-protocol.md` (§15 carnosine module, §16 lactoferrin module, H2O2 chassis-as-formulation), `engineered-lbp-chassis.md` (LBP peer track), `enzyme-deficit-deep-dive.md` (EPI + SIBO link), `enzyme-quantification-protocol.md` (tiered assay ladder), `genotype-informed-supplement-workflow.md` (5-step pipeline with Q141K example), `gout-action-guide.md` (situation-first triage + Protocol C triple-mechanism flare stack), `gout-clinical-pipeline.md` (ALLN-346 terminated, PRX-115/SSS11 active, no Phase 2b/3 for dapansutrile in gout), `gout-genetic-variants.md` (unified index + CFH Y402H stratification), `gout-multihop-research-program.md` (11 interface experiments queued), `gout-pathophysiology.md` (transporter coverage map), `gsdmd-pore-delivery-paradox.md` (comp-042 KPV selectivity falsified; transporter-orphan tracer required), `gut-lumen-sink.md` (mechanism + ALLN-346/PULSE precedent), `gut-lumen-uricase-physiologic-regime-computational.md` (comp-044 invalidates comp-019 regime), `hypotheses/H01-ward-dual-cassette.md` (dual-cassette feasibility gate), `hypotheses/H03-sirna-urat1-thesis.md` (kidney-tropic siRNA), `hypotheses/H04-tcm-rigor-intersection.md` (methodology lens), `hypotheses/H05-daf-scr14-cp0-thesis.md` (DAF SCR1-4 CP0 candidate), `hypotheses/H06-medicinal-mushroom-complement-track.md` (cultivation track), `hypotheses/H07-clomid-intestinal-er-antagonism.md` (ER-antagonism reframe), `hypotheses/H08-gut-lumen-sink-platform-thesis.md` (reopened, no valid ΔSUA prior), `hypotheses/H09-community-fermentation-reliability.md` (#2 riskiest assumption), `index.md` (dashboard), `koji-construct-design.md`, `koji-endgame-strain.md` (5 chokepoints × 4 molecules), `koji-home-fermentation.md` (wild-type baseline), `lactoferrin.md` (coverage matrix + substrate-supply synergy), `lactoferrin-linker-redesign-computational.md` (comp-034), `medicinal-mushroom-complement-track.md` (Phase 7 cultivation track), `medicinal-mushroom-compound-mapping-computational.md` (comp-014 breadth), `modality-chokepoint-matrix.md` (modality × target exploration surface), `nlrp3-exploit-map.md` (v1.2 7-chokepoint map with sub-branches), `nlrp3-inflammasome.md`, `nlrp3-inhibitor-screen.md` (Tier 1–4), `open-questions.md` (meta-index), `purine-degrading-bacteria.md` (gut as independent urate disposal organ), `purine-load-koji-vs-yeast.md` (purine-load comparison), `quantification-ladder.md` (Tier 1–4 framework), `spm-resolution-pathway.md` (CP5b), `supplements-stack.md` (stack-level contradictions + ABCG2-inhibitor risk tiers), `tcm-modern-rigor-intersection.md` (methodology lens), `theaflavins.md` (Tier 2; CP2/CP3 + URAT1/GLUT9), `tier-2-butyrate-assay-audit-computational.md` (comp-038), `tnfsf14-gout-target.md` (CP1a), `upstream-complement-modulator-sweep-computational.md` (comp-018), `validation-experiments.md` (wet-lab gates including §1.33 Gate 0, §1.9 staged dual-cassette, §1.14 butyrate/lactoferrin rescue, §1.25 DAF SCR1-4, §1.30 Houttuynia prioritization, §1.31 butyrate Tier 2 validation, §1.32 GSDMD pore selectivity probe, §1.36 luminal redox safety), `uricase.md` (H2O2 topology dependence), `uricase-variant-selection.md` (C. utilis co-primary for oral track), `uricase-cassette-ranking-computational.md` (comp-022), `uricase-topology-oxygen-peroxide-design-computational.md` (comp-045), `zileuton.md` (CP6a pharma-grade repurposing candidate).

**Synthesis history (most recent ~3):**  
- 2026-07-13-fae0e36.md (comp-047 Q141K re-screen INCONCLUSIVE; comp-031 dual-chassis invalidated; comp-038 Tier 2 butyrate audit YELLOW with full-text verification of De Baere 2013 HPLC-UV and Gu 2026 electrochemical-ANN; comp-042 KPV pore selectivity YELLOW with transporter-orphan reframe; comp-039 CFH-independence for dietary-CP0 candidates; comp-044 regime audit; comp-045 topology × oxygen × peroxide; [H08](./hypotheses/H08-gut-lumen-sink-platform-thesis.md) reopened; Tier 2 inter-operator reproducibility gap for microbiome metabolites)  
- 2026-07-01-18d3696.md (ChEMBL v37 refresh; theaflavins CB2 150 nM curated; ursolic acid 16 entries including NF-κB p65 31 nM and ROR-γ range 0.75–680 nM; curcumin DYRK2 2.5 nM; disulfiram LOXL4 59 nM; β-caryophyllene CB2 curated; resveratrol DPP-4 0.6 nM remains top)  
- 2026-06-01-8a97f95.md (RA PK scan — gut-luminal RA transient, colonic degradation to metabolites; proximal/distal split; RA #3 riskiest assumption added)

**Trigger files' frontmatter `related:` fields and inline links:** All listed trigger files cross-reference the above pages (e.g. `abcg2-modulators.md` links to `gut-lumen-sink.md`, `androgen-urate-axis.md`, `supplements-stack.md`; `chassis-pending-interventions.md` links to `modality-chokepoint-matrix.md`, `delivery-route-matrix.md`, `engineered-lbp-chassis.md`; `complement-c5a-gout.md` links to `nlrp3-exploit-map.md` and `validation-experiments.md`; `lactoferrin.md` and `koji-endgame-strain.md` cross-link to `chaperone-orthogonal-stacking.md` and `spm-resolution-pathway.md`; `gout-action-guide.md` links to `self-experiment-protocol.md` and `gout-genetic-variants.md`; `open-questions.md` links to `hypotheses/H08-gut-lumen-sink-platform-thesis.md` and `H09-community-fermentation-reliability.md`; computational comps link to `validation-experiments.md` and `computational-experiments.md`).

**Phase A baseline:** All named connections in the above files, synthesis logs, and trigger frontmatter are the already-known landscape. Single-link duplicates are dropped; multi-link compositions not in the baseline are novel.

## Phase B — Map the connection graph

**Strongly linked pairs (easy connections already found):**  
`abcg2-modulators.md` ↔ `abcg2-q141k-chaperone-rescreen-computational.md` ↔ `abcg2-q141k-chaperone-screen-computational.md` (Q141K rescue + chaperone route), `lactoferrin.md` ↔ `chaperone-orthogonal-stacking.md` ↔ `koji-endgame-strain.md` (multi-cassette burden, lactoferrin as third cassette), `gut-lumen-sink.md` ↔ `uricase.md` ↔ `gut-lumen-uricase-physiologic-regime-computational.md` (lumen-sink mechanism + comp-044/045 regime correction), `complement-c5a-gout.md` ↔ `daf-cd55-scr14-truncated-computational.md` ↔ `daf-cd55-protease-stability-computational.md` (CP0 DAF SCR1-4 + protease stability), `c1-inh-protease-stability-ecn-computational.md` ↔ `engineered-lbp-chassis.md` (LBP peer track + C1-INH).

**Weakly-connected or unconnected pairs (highest-leverage for new synthesis):**  
- `purine-degrading-bacteria.md` × `abcg2-modulators.md` (PDB butyrate → PPARγ/HDAC ABCG2 rescue is conditional on carbon fate; comp-031 invalidated, §1.37 still open)  
- `medicinal-mushroom-complement-track.md` × `chaperone-orthogonal-stacking.md` (mushroom polysaccharides vs. engineered protein burden; GLPP + cordycepin synergy still gated)  
- `tnfsf14-gout-target.md` × `supplements-stack.md` (TNFSF14 as CP1a amplifier; EGCG/theaflavins have direct HVEM data but no human gout trial)  
- `fructose-connection.md` × `tcm-modern-rigor-intersection.md` (fructose-KHK-PRPS vs. TCM XO + transporter compounds; PRPS chokepoint still under-mapped)  
- `gout-action-guide.md` × `chassis-pending-interventions.md` (IA uricase + catalase, inhaled mRNA-IL-1RA, kidney-tropic siRNA, T0SS-OMV, duckweed, pharmacological chaperones for Q141K — all remain chassis-pending; no wet-lab or clinical bridge yet)  
- `gout-genetic-variants.md` × `cfh-mechanism-dissociation-cp0-candidates-computational.md` (CFH Y402H × dietary-CP0 candidates still untested in UKB/AoU cross-tab; Phase 2 queued)  
- `gout-multihop-research-program.md` × `validation-experiments.md` (11 interface experiments still queued; §1.33 Gate 0, §1.37 PDB carbon fate, §1.36 luminal redox still open)  
- `lactoferrin.md` × `spm-resolution-pathway.md` (lactoferrin CP6b via mitophagy + CP5b macrophage polarization is indirect; direct ALX/FPR2 agonism absent; §1.30 Houttuynia prioritization screen still open)  
- `mechanical-flare-triggers.md` × `validation-experiments.md` (exertion/metabolic-overload vs mechanical-shedding still unresolved; §1.11 exertion-challenge test with serial urinary urate/Cr queued but not run)  
- `supplements-stack.md` × `tier-2-butyrate-assay-audit-computational.md` (Tier 2 butyrate exposure-proxy gap still open; no validated home Tier 2 for microbiome-derived metabolites despite comp-038 full-text verification of De Baere 2013 HPLC-UV and Gu 2026 electrochemical-ANN; §1.31 spike/recovery still wet-lab gated)

**Weak-pair bias:** The most novel synthesis will come from weakly-connected pairs above — especially PDB × ABCG2, medicinal-mushroom × chaperone-orthogonal-stacking, TNFSF14 × supplements-stack, fructose × TCM, mechanical-flare-triggers × validation-experiments, and the chassis-pending × gout-action-guide matrix.

## Phase C — Synthesize

1. **Cross-domain synergy — medicinal-mushroom + engineered-koji for dual-urate + NLRP3 coverage.** *Cordyceps militaris* whole-fermentate + *Ganoderma lucidum* GLPP (both cultivation-track) hit URAT1 + ADA + GLUT9/OAT1 + NLRP3 simultaneously; combining with engineered-koji uricase + lactoferrin (koji-track) covers renal-reabsorption, intestinal-secretion, gut-lumen degradation, and multiple NLRP3 nodes in one daily regimen. The combination is not yet tested; the 4-arm ADA half-life assay (§1.26) and the §2.6 GLPP+cordycepin wet-lab gate are both still open. **[CHAIN-DEPTH: 3+]** **[PHASE-A-MATCH: no]**  
   - *Documents Connected:* `medicinal-mushroom-complement-track.md`, `koji-endgame-strain.md`, `gout-pathophysiology.md`, `abcg2-modulators.md`, `nlrp3-exploit-map.md`, `validation-experiments.md` §1.26/§2.6  
   - *Page-pair linkage:* Weak — medicinal-mushroom-complement-track.md and koji-endgame-strain.md do not cross-reference each other; both link to modality-chokepoint-matrix.md but not to each other.  
   - *Why It Matters:* This is the first platform-level pattern that composes two peer tracks (cultivation + engineering) into a single daily regimen that hits both the urate-handling nodes (URAT1/GLUT9/OAT1/ABCG2) and multiple NLRP3 nodes (CP1/CP2/CP4/CP6b) without requiring separate products. The additivity is plausible but untested; if the ADA half-life extension and MSU-NLRP3 suppression both hold, the combined product could meaningfully reduce both UA and flare frequency in typical under-excreter patients. The H06 hypothesis card (cultivation-track viability) and the H09 community-fermentation reliability card both depend on this experiment succeeding.  
   - *Suggested Action:* Run the 4-arm ADA half-life assay (§1.26) with the fifth (koji-cordycepin + GLPP) arm as soon as the engineered-koji cordycepin strain is available; if negative, deprioritize the engineered-koji cordycepin route permanently and rely on whole-fermentate *Cordyceps* + GLPP.  

   {{PEER-REVIEW}}

2. **Platform-level pattern — substrate engineering as the lightest-leverage modality (Platform Principle 9).** The 2026-05-19 substrate-engineering lit scan showed effect sizes from 1.2× (yield) to 22× (combined precursor + induction) and 100× (erinacine C:Q ratio inversion) across species. Substrate composition is a cultivation-level lever that requires only food-grade reagents (methionine, alanine, oleic acid, cellulose, nucleosides) and does not require genetic engineering or bioreactor infrastructure. This is the cheapest way to tune compound profile without touching the genome — and it compounds with strain selection rather than competing with it. The pattern generalizes to any native-compound track (koji, medicinal mushroom, TCM). **[CHAIN-DEPTH: 3+]** **[PHASE-A-MATCH: no]**  
   - *Documents Connected:* `medicinal-mushroom-complement-track.md`, `koji-home-fermentation.md`, `tcm-modern-rigor-intersection.md`, `etc/open-source-platform.md`, `open-questions.md`  
   - *Page-pair linkage:* Weak — medicinal-mushroom-complement-track.md and koji-home-fermentation.md do not cross-reference each other; both link to quantification-ladder.md but not to each other.  
   - *Why It Matters:* This is the first platform-level pattern that operationalizes the "distributed contributor" thesis without requiring wet-lab infrastructure. A contributor can take a commercial grow kit + a $20/kg GRAS reagent (methionine) and produce a 1.7–3.1× ergothioneine boost using only kitchen equipment — exactly the accessibility thesis the platform is built on. The pattern also explains why the medicinal-mushroom track is lighter than the engineered-koji track: strain selection + substrate tuning can achieve meaningful compound-profile shifts without the multi-gene engineering burden of heterologous protein expression. The H06 hypothesis card (cultivation-track viability) and the H09 community-fermentation reliability card both depend on this pattern holding across independent operators.  
   - *Suggested Action:* Formalize the substrate-engineering protocol matrix as SOP-7 in `medicinal-mushroom-extract-sops.md` and add it to the quantification-ladder.md framework; run a small multi-operator round-robin (3 independent contributors using the same substrate kit + methionine) to validate the ±15% reproducibility target in H06 Dimension 2.  

   {{PEER-REVIEW}}

3. **Contradiction — butyrate Tier 2 assay infrastructure gap vs. workflow assumption.** The genotype-informed supplement quantification workflow assumes a validated Tier 2 ruler for every compound class. For butyrate (and all microbiome-derived metabolites), no such Tier 2 exists — the only validated Tier 2 candidates are exposure proxies (stool SCFA panel) rather than input-potency verification. This breaks the "calibrate once at Tier 3, track batches at Tier 2" discipline for every gut-microbiome-mediated intervention (PDB, Houttuynia, prebiotic fiber, secondary bile acids, microbial indoles, TMAO). **[CHAIN-DEPTH: 2]** **[PHASE-A-MATCH: partial]** (the workflow page documents the gap but the quantification-ladder.md framework does not yet name it as a class-level limitation).  
   - *Documents Connected:* `genotype-informed-supplement-workflow.md`, `quantification-ladder.md`, `tier-2-butyrate-assay-audit-computational.md`, `open-questions.md`  
   - *Page-pair linkage:* Weak — genotype-informed-supplement-workflow.md and tier-2-butyrate-assay-audit-computational.md do not cross-reference each other; both link to quantification-ladder.md but not to each other.  
   - *Why It Matters:* This is the first class-level methodology gap surfaced by the workflow. It means every gut-microbiome intervention (including the Q141K butyrate-emphasis stack) operates under an unverified dose variable. The gap is not a workflow failure — the workflow successfully blocks silent underdosing for non-microbiome compounds — but it reveals that the quantification ladder is incomplete for microbiome-derived metabolites. Closing it for one metabolite (butyrate) would unlock the QC loop for the entire class.  
   - *Suggested Action:* Run the empirical spike/recovery validation of HPLC-UV vs. GC-MS on culture supernatant (per comp-038 next-step recommendation) as [validation-experiments.md §1.31](./validation-experiments.md). If GREEN, adopt HPLC-UV as Tier 2 for culture supernatant and update the workflow page to reflect the closed gap.  

   {{PEER-REVIEW}}

4. **Platform-level pattern — substrate engineering as the lightest-leverage modality (Platform Principle 9).** The 2026-05-19 substrate-engineering lit scan showed effect sizes from 1.2× (yield) to 22× (combined precursor + induction) and 100× (erinacine C:Q ratio inversion) across species. Substrate composition is a cultivation-level lever that requires only food-grade reagents and does not require genetic engineering or bioreactor infrastructure. This is the cheapest way to tune compound profile without touching the genome — and it compounds with strain selection rather than competing with it. The pattern generalizes to any native-compound track (koji, medicinal mushroom, TCM). **[CHAIN-DEPTH: 3+]** **[PHASE-A-MATCH: no]**  
   - *Documents Connected:* `medicinal-mushroom-complement-track.md`, `koji-home-fermentation.md`, `tcm-modern-rigor-intersection.md`, `etc/open-source-platform.md`, `open-questions.md`  
   - *Page-pair linkage:* Weak — medicinal-mushroom-complement-track.md and koji-home-fermentation.md do not cross-reference each other; both link to quantification-ladder.md but not to each other.  
   - *Why It Matters:* This is the first platform-level pattern that operationalizes the "distributed contributor" thesis without requiring wet-lab infrastructure. A contributor can take a commercial grow kit + a $20/kg GRAS reagent (methionine) and produce a 1.7–3.1× ergothioneine boost using only kitchen equipment — exactly the accessibility thesis the platform is built on. The pattern also explains why the medicinal-mushroom track is lighter than the engineered-koji track: strain selection + substrate tuning can achieve meaningful compound-profile shifts without the multi-gene engineering burden of heterologous protein expression. The H06 hypothesis card (cultivation-track viability) and the H09 community-fermentation reliability card both depend on this pattern holding across independent operators.  
   - *Suggested Action:* Formalize the substrate-engineering protocol matrix as SOP-7 in `medicinal-mushroom-extract-sops.md` and add it to the quantification-ladder.md framework; run a small multi-operator round-robin (3 independent contributors using the same substrate kit + methionine) to validate the ±15% reproducibility target in H06 Dimension 2.  

   {{PEER-REVIEW}}

## Contradictions Found

1. **Butyrate Tier 2 assay infrastructure gap vs. workflow assumption.** The genotype-informed supplement quantification workflow assumes a validated Tier 2 ruler for every compound class. For butyrate (and all microbiome-derived metabolites), no such Tier 2 exists — the only validated Tier 2 candidates are exposure proxies (stool SCFA panel) rather than input-potency verification. This breaks the "calibrate once at Tier 3, track batches at Tier 2" discipline for every gut-microbiome-mediated intervention (PDB, Houttuynia, prebiotic fiber). **[CHAIN-DEPTH: 2]** **[PHASE-A-MATCH: partial]** (the workflow page documents the gap but the quantification-ladder.md framework does not yet name it as a class-level limitation).  
   - *Locations:* `genotype-informed-supplement-workflow.md` §"Tier 2 assay gap for microbiome-derived metabolites", `quantification-ladder.md`, `tier-2-butyrate-assay-audit-computational.md`, `open-questions.md` §"Class-level Tier 2 assay gap for microbiome-derived metabolites"  
   - *Analysis:* The workflow successfully blocks silent underdosing for non-microbiome-mediated compounds and fails to block it for microbiome-mediated ones. The gap is not a workflow failure — it is a class-level methodology gap. Closing it for butyrate would unlock the QC loop for the entire class.  

   {{PEER-REVIEW}}

2. **EGCG in-vitro-inhibition vs. in-vivo-favorable phenotype is not resolved.** EGCG is a functional ABCG2 inhibitor in vitro (Ki ~5–10 μM) but shows net-favorable ABCG2/URAT1/GLUT9 phenotype in hyperuricemic mice (Yu 2024 PMID 38757391). The unifying hypothesis is Nrf2-driven transcriptional up-regulation under chronic exposure, but the in vivo data are rodent and transcript-level, the Nrf2 mechanism is inferred, and the acute inhibition is real at high concentrated-extract doses. The dose-and-chronicity axis is the load-bearing variable — dietary tea plausibly favorable, mega-dose extract plausibly the opposite. **[CHAIN-DEPTH: 2]** **[PHASE-A-MATCH: yes]** (already documented in `abcg2-modulators.md` §"The supplements-stack contradiction" but the per-compound stratification was not fully resolved until the 2026-07-13 CBD-vs-flavonoid gut-degradation scan).  
   - *Locations:* `abcg2-modulators.md` §"The supplements-stack contradiction" and §"Gut-luminal metabolic stability resolves the CBD-vs-flavonoid inconsistency", `supplements-stack.md` §"Stack-level contradictions", `egcg.md` §"ABCG2 functional inhibitor warning"  
   - *Analysis:* The class warning does not stand as written — it needs per-compound stratification. Curcumin earns the strongest warning (in vivo primate); quercetin is a real but proximal-gut-only inhibitor; EGCG likely belongs with the favorable Nrf2 inducers (consistent with the theaflavins reclassification). The free luminal concentration vs. Ki(ABCG2-for-urate) per gut segment remains unmeasured for all four — the quantity every warning above ultimately depends on.  

   {{PEER-REVIEW}}

## Proposed Experiments (ranked by insight per cost)

1. **Houttuynia cordata polysaccharide fraction comparison in MSU-stimulated THP-1 macrophages — prioritization screen.** Three arms (HCPM 19.1 kDa purified RG-I fraction, crude HCP, commercial Houttuynia capsule extract) at three log-spaced doses (10, 100, 1000 μg/mL) in LPS-primed, MSU-challenged THP-1 macrophages. Primary readout IL-1β ELISA; secondary IL-6 (CP1b/TNFSF14 amplifier probe) + cell viability. **Cost:** $1,500–2,500. **Time:** 4–6 weeks. **Decides:** whether Houttuynia suppresses MSU-induced IL-1β in a gout-relevant cell model, and whether sourcing/purification matters. If positive on at least one arm, fire comp-040 next for CFH-independence mechanism confirmation. If all arms negative, deprioritize Houttuynia. **[CHAIN-DEPTH: 3+]** **[PHASE-A-MATCH: no]**  
   - *Documents Connected:* `complement-c5a-gout.md`, `nlrp3-exploit-map.md`, `upstream-complement-modulator-sweep-computational.md`, `cfh-mechanism-dissociation-cp0-candidates-computational.md`, `validation-experiments.md` §1.30, `medicinal-mushroom-extract-sops.md`  
   - *Page-pair linkage:* Weak — complement-c5a-gout.md and medicinal-mushroom-extract-sops.md do not cross-reference each other; both link to upstream-complement-modulator-sweep-computational.md but not to each other.  
   - *Why It Matters:* Houttuynia is the corpus's first dietary dual-CP0+CP1 candidate; the structure-dependent directionality (homogalacturonan → pro-inflammatory via TLR4; RG-I → anti-complement) means commercial capsules cannot be assumed equivalent to the Chen-group HCPM fraction. This screen is the cheapest discriminator of consumer-product viability before committing to the more expensive CFH-depleted serum assay (comp-040).  
   - *Suggested Action:* Run the 3-arm 3-dose THP-1/MSU IL-1β screen with the priming-only/extract-alone control arm (no MSU) to detect TLR4-priming signal. If positive on at least one arm, fire comp-040.  

   {{PEER-REVIEW}}

2. **Tier 2 butyrate assay validation — HPLC-UV vs. GC-MS spike/recovery on culture supernatant.** Per comp-038 next-step recommendation, validate De Baere 2013 HPLC-UV (direct UV 210 nm, no derivatization, validated on bacterial culture supernatant) against GC-MS using sodium-butyrate spike/recovery in OE-relevant culture matrices. **Cost:** $500. **Time:** 2 weeks. **Decides:** whether a decentralizable Tier 2 ruler exists for culture-supernatant butyrate (engineered-strain work) or whether GC-MS remains the only validated Tier 3 anchor. If GREEN, adopt HPLC-UV as Tier 2 for culture supernatant and update the genotype-informed-supplement-workflow.md Q141K example to reflect the closed gap. **[CHAIN-DEPTH: 2]** **[PHASE-A-MATCH: partial]** (the workflow page documents the gap but the quantification-ladder.md framework does not yet name it as a class-level limitation).  
   - *Documents Connected:* `tier-2-butyrate-assay-audit-computational.md`, `quantification-ladder.md`, `genotype-informed-supplement-workflow.md`, `open-questions.md`  
   - *Page-pair linkage:* Weak — tier-2-butyrate-assay-audit-computational.md and genotype-informed-supplement-workflow.md do not cross-reference each other; both link to quantification-ladder.md but not to each other.  
   - *Why It Matters:* This is the first class-level methodology gap surfaced by the workflow. It means every gut-microbiome intervention (including the Q141K butyrate-emphasis stack) operates under an unverified dose variable. The gap is not a workflow failure — the workflow successfully blocks silent underdosing for non-microbiome compounds — but it reveals that the quantification ladder is incomplete for microbiome-derived metabolites. Closing it for butyrate would unlock the QC loop for the entire class.  
   - *Suggested Action:* Run the empirical spike/recovery validation of HPLC-UV vs. GC-MS on culture supernatant as [validation-experiments.md §1.31](./validation-experiments.md). If GREEN, adopt HPLC-UV as Tier 2 for culture supernatant and update the workflow page to reflect the closed gap.  

   {{PEER-REVIEW}}

3. **Tier 2 butyrate assay validation — electrochemical fecal SCFA profiling vs. GC-MS (stool track).** Full-text verification of Gu et al. 2026 electrochemical-ANN (PMID 42041444) confirmed GC-MS-validated fecal cohort (n=30, butyric-acid MAE 0.029 mM) — a genuine stool-specific Tier-2 candidate. Validate spike/recovery against GC-MS using real stool samples to confirm butyrate-specific performance at mM-range colonic concentrations. **Cost:** $800–1,200. **Time:** 3 weeks. **Decides:** whether a stool-specific Tier 2 ruler exists for patient-facing butyrate monitoring, or whether GC-MS remains the only validated Tier 3 anchor for stool. **[CHAIN-DEPTH: 3+]** **[PHASE-A-MATCH: no]**  
   - *Documents Connected:* `tier-2-butyrate-assay-audit-computational.md`, `quantification-ladder.md`, `genotype-informed-supplement-workflow.md`, `open-questions.md`  
   - *Page-pair linkage:* Weak — tier-2-butyrate-assay-audit-computational.md and genotype-informed-supplement-workflow.md do not cross-reference each other; both link to quantification-ladder.md but not to each other.  
   - *Why It Matters:* The Tier 2 gap for microbiome-derived metabolites is a class-level methodology bottleneck that affects every gut-microbiome-mediated intervention on the platform (PDB, Houttuynia gut-microbiota arm, prebiotic-fiber-specific stack, secondary bile acids, microbial indoles, TMAO). Closing it for butyrate unlocks the QC loop for the entire class. The electrochemical fecal SCFA platform is the most promising stool-specific Tier-2 candidate; validating it against GC-MS is the cheapest next step.  
   - *Suggested Action:* Run the empirical spike/recovery validation of the electrochemical-ANN platform vs. GC-MS on real stool samples as a follow-on to comp-038. If GREEN, adopt as Tier 2 for stool and update the workflow page to reflect the closed gap for microbiome-derived metabolites.  

   {{PEER-REVIEW}}

## Most Curious Thread

The single thread I would spend the next experiment slot on is the **Houttuynia cordata polysaccharide fraction comparison in MSU-stimulated THP-1 macrophages** (§1.30). The corpus evidence supporting the hunch is the 2026-05-19 traditional-name re-scan (logs/houttuynia-cp1-dual-mechanism-lit-scan-2026-05-19.md) that surfaced HCP/HCPM/CHCP as the first dietary dual-CP0+CP1 candidate (Lu 2018 PMC5925397 CH50 79–318 µg/mL, Li 2025 PMC12254813 intestinal NLRP3/caspase-1/IL-1β/IL-18 suppression, Yu 2026 PMC12937656 TLR4-MD2 direct binding) plus the structure-dependent directionality caveat (Cheng 2014 PMC7112369 — purified 60 kDa HCP-2 is pro-inflammatory on naïve PBMCs via TLR4). The specific evidence that would refute it is a negative IL-1β suppression result across all three arms (HCPM, crude HCP, commercial capsule extract) at ≤100 μg/mL with cell viability ≥85%. The cheapest experiment that would discriminate is the 3-arm 3-dose THP-1/MSU IL-1β ELISA screen with the priming-only/extract-alone control arm (no MSU) to detect TLR4-priming signal — ~$1,500–2,500, 4–6 weeks, CRO-executable. This is idiosyncratic to me — the synthesis daemon's Pass 2 repeatedly surfaced Houttuynia as the highest-leverage dietary-CP0 candidate, but the structure-dependent directionality + the fact that no HC polysaccharide has ever been tested in an MSU/gout model makes this the single most decision-relevant experiment in the corpus right now. (source: complement-c5a-gout.md §9.7, medicinal-mushroom-complement-track.md §"Consumer-product caveat", validation-experiments.md §1.30, cfh-mechanism-dissociation-cp0-candidates-computational.md §3.3)

{{PEER-REVIEW}}

**Sources cited:**
- wiki/abcg2-modulators.md
- wiki/abcg2-q141k-chaperone-rescreen-computational.md
- wiki/abcg2-q141k-chaperone-screen-computational.md
- wiki/c1-inh-protease-stability-ecn-computational.md
- wiki/chaperone-orthogonal-stacking.md
- wiki/chassis-pending-interventions.md
- wiki/combined-cp0-systems-model-computational.md
- wiki/complestatin-bgc-lbp-feasibility-computational.md
- wiki/compounding-pharmacy-track.md
- wiki/computational-experiments.md
- wiki/cordycepin-cassette-burden-computational.md
- wiki/daf-cd55-scr14-cassette-ranking-computational.md
- wiki/daf-cd55-scr14-truncated-computational.md
- wiki/daf-lactoferrin-ecn-folding-feasibility-computational.md
- wiki/delivery-route-matrix.md
- wiki/disulfiram-dose-modeling-computational.md
- wiki/disulfiram.md
- wiki/engineered-lbp-chassis.md
- wiki/etc/chembl-cross-check.md
- wiki/etc/experiments/comp-001-uricase-shio-koji-protease-stability/outputs/summary.md
- wiki/etc/experiments/comp-006-daf-cd55-shio-koji-protease-stability/README.md
- wiki/etc/experiments/comp-006-daf-cd55-shio-koji-protease-stability/outputs/summary.md
- wiki/etc/experiments/comp-007-food-grade-hdaci-screen/README.md
- wiki/etc/experiments/comp-007-food-grade-hdaci-screen/inputs/provenance.md
- wiki/etc/experiments/comp-007-food-grade-hdaci-screen/outputs/summary.md
- wiki/etc/experiments/comp-007-food-grade-hdaci-screen/wiki-archive.md
- wiki/etc/experiments/comp-008-f-prausnitzii-heterologous-expression/README.md
- wiki/etc/experiments/comp-008-f-prausnitzii-heterologous-expression/outputs/summary.md
- wiki/etc/experiments/comp-008-f-prausnitzii-heterologous-expression/wiki-archive.md
- wiki/etc/experiments/comp-009-urat1-sirna-target-site-selection/README.md
- wiki/etc/experiments/comp-009-urat1-sirna-target-site-selection/outputs/summary.md
- wiki/etc/experiments/comp-010-cassette-compatibility/README.md
- wiki/etc/experiments/comp-010-cassette-compatibility/inputs/provenance.md
- wiki/etc/experiments/comp-010-cassette-compatibility/outputs/summary.md
- wiki/etc/experiments/comp-010-cassette-compatibility/wiki-archive.md
- wiki/etc/experiments/comp-011-c-utilis-uricase-cassette-compatibility/README.md
- wiki/etc/experiments/comp-011-c-utilis-uricase-cassette-compatibility/outputs/summary.md
- wiki/etc/experiments/comp-015-t-axis-adjuvant-urate-mapping/README.md
- wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/README.md
- wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/outputs/flux_model_summary.md
- wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/wiki-archive.md
- wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/README.md
- wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/v2/provenance.md
- wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/wiki-archive.md
- wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/README.md
- wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/outputs/summary.md
- wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs/summary.md
- wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/outputs/summary.md
- wiki/etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/README.md
- wiki/etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/inputs/provenance.md
- wiki/etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/outputs/summary.md
- wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/outputs/summary.md
- wiki/etc/experiments/comp-046-staged-purine-sink-mass-balance/README.md
- wiki/etc/experiments/comp-046-staged-purine-sink-mass-balance/outputs/summary.md
- wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/README.md
- wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/inputs/provenance.md
- wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/outputs/controls.md
- wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/outputs/summary.md
- wiki/etc/manual-literature-mining.md
- wiki/genotype-informed-supplement-workflow.md
- wiki/gout-action-guide.md
- wiki/gout-genetic-variants.md
- wiki/gsdmd-pore-delivery-paradox.md
- wiki/gut-lumen-sink.md
- wiki/hypotheses/H02-engineered-lbp-thesis.md
- wiki/hypotheses/H03-sirna-urat1-thesis.md
- wiki/inhaled-mrna-il1ra-pulse-computational.md
- wiki/intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md
- wiki/intra-articular-uricase-h2o2-reaction-diffusion-computational.md
- wiki/lactoferrin-linker-redesign-computational.md
- wiki/lactoferrin-protease-stability-computational.md
- wiki/medicinal-mushroom-compound-mapping-computational.md
- wiki/modality-chokepoint-matrix.md
- wiki/nlrp3-exploit-map.md
- wiki/nlrp3-inhibitor-screen.md
- wiki/open-questions.md
- wiki/purine-degrading-bacteria.md
- wiki/quantification-ladder.md
- wiki/repeat-dose-inhaled-mrna-il1ra-pkpd-computational.md
- wiki/staged-purine-sink-mass-balance-computational.md
- wiki/supplement-abcg2-antagonism-computational.md
- wiki/supplements-stack.md
- wiki/t-abcg2-suppression-evidence-mining-computational.md
- wiki/t-axis-adjuvant-urate-mapping-computational.md
- wiki/tcm-gout-compound-triage-computational.md
- wiki/tcm-modern-rigor-intersection.md
- wiki/tier-2-butyrate-assay-audit-computational.md
- wiki/upstream-complement-assay-format-mapping-computational.md
- wiki/upstream-complement-modulator-sweep-computational.md
- wiki/upstream-complement-verification-rerun-computational.md
- wiki/urat1-sirna-target-site-selection-computational.md
- wiki/uricase-shio-koji-thermal-stability-computational.md
- wiki/uricase-variant-selection.md
- wiki/uricase.md
- wiki/validation-experiments.md
