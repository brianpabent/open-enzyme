---
title: "Synthesis — 2026-05-29 (commit HEAD)"
date: 2026-05-29
commit: HEAD
diff_base: unknown
trigger_files: (none)
reviewer_model: x-ai/grok-4.20
reviewer_model_served_raw: x-ai/grok-4.20-20260309
reviewer_model_requested: x-ai/grok-4.20
reviewer_fallback_used: False
input_tokens: 934289
output_tokens: 7624
cost_usd: 1.1869
corpus_files: 121
---

**# Synthesis — 2026-05-29**

**Substrate:** Open Enzyme wiki at commit `HEAD`  
**Trigger files:** (none specified)  
**Diff base:** unknown  
**Reviewer:** x-ai/grok-4.20

## New Connections

1. **The platform's three complementary peer tracks (koji, engineered LBP, siRNA/URAT1) + the newly formalized medicinal-mushroom-complement track collectively close every major chokepoint in the gout/NLRP3 cascade when combined with the compounding-pharmacy repurposing surface.** *Supported*. `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* `modality-chokepoint-matrix.md`, `delivery-route-matrix.md`, `chassis-pending-interventions.md`, `koji-endgame-strain.md`, `engineered-lbp-chassis.md`, `sirna-urat1-modality.md`, `medicinal-mushroom-complement-track.md`, `compounding-pharmacy-track.md`, `gout-pathophysiology.md`, `nlrp3-exploit-map.md`, `complement-c5a-gout.md`, `spm-resolution-pathway.md`, `tnfsf14-gout-target.md`, `abcg2-modulators.md`, `androgen-urate-axis.md`, `prps-purine-biosynthesis-chokepoint.md`, `uricase.md`, `lactoferrin.md`, `carnosine.md`, `theaflavins.md`, `egcg.md`, `oridonin.md`, `bhb-ketones.md`, `colchicine.md`, `disulfiram.md`, `zileuton.md`, `purine-degrading-bacteria.md`, `open-enzyme-vision.md`, `etc/open-source-platform.md`, `gout-clinical-pipeline.md`, `gout-action-guide.md`, `self-experiment-protocol.md`, `genotype-informed-supplement-workflow.md`, `personal-genome-protocol.md`, `quantification-ladder.md`, `enzyme-quantification-protocol.md`, `medicinal-mushroom-extract-sops.md`, `mechanical-flare-triggers.md`, `hypotheses/H01-ward-dual-cassette.md`, `hypotheses/H02-engineered-lbp-thesis.md`, `hypotheses/H03-sirna-urat1-thesis.md`, `hypotheses/H04-tcm-rigor-intersection.md`, `hypotheses/H05-daf-scr14-cp0-thesis.md`, `hypotheses/H06-medicinal-mushroom-complement-track.md`, `hypotheses/H07-clomid-intestinal-er-antagonism.md`, `hypotheses/H08-gut-lumen-sink-platform-thesis.md`, `hypotheses/H09-community-fermentation-reliability.md`, `computational-experiments.md` (comp-001 through comp-039), `cross-validation.md`, `tcm-gout-compound-triage-computational.md`, `daf-cd55-scr14-truncated-computational.md`, `daf-cd55-protease-stability-computational.md`, `c-utilis-uricase-cassette-compatibility-computational.md`, `cassette-compatibility-computational.md`, `chaperone-orthogonal-stacking.md`, `t-axis-adjuvant-urate-mapping-computational.md`, `t-abcg2-suppression-evidence-mining-computational.md`, `intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md`, `combined-cp0-systems-model-computational.md`, `cfh-mechanism-dissociation-cp0-candidates-computational.md`, `tier-2-butyrate-assay-audit-computational.md`, `inhaled-mrna-il1ra-pulse-computational.md`, `repeat-dose-inhaled-mrna-il1ra-pkpd-computational.md`, `abcg2-q141k-chaperone-screen-computational.md`, `lactoferrin-linker-redesign-computational.md`, `uricase-cassette-ranking-computational.md`, `food-grade-hdaci-screen-computational.md`, `upstream-complement-modulator-sweep-computational.md`, `upstream-complement-verification-rerun-computational.md`, `dual-chassis-ecn-pdb-uricase-computational.md`
   - *Page-pair linkage:* This is a **weakly-connected page pair** (and in many cases a multi-way weakly-connected graph). The modality-chokepoint-matrix and delivery-route-matrix were previously isolated from each other and from the chassis-pending-interventions page. The engineered-koji-protocol, engineered-lbp-chassis, and sirna-urat1-modality pages were treated as parallel but never explicitly composed into a unified four-track architecture. The new `medicinal-mushroom-complement-track.md` was orphaned until this synthesis. The gout-genetic-variants.md, genotype-informed-supplement-workflow.md, and personal-genome-protocol.md pages were only loosely connected to the chokepoint maps. The cross-validation.md and open-questions.md pages were not previously used as synthesis hubs. The synthesis/history/ and synthesis/strategic-reflections/ directories were never cited in the wiki pages themselves. The hypotheses/ directory was never referenced from the main pages. This synthesis is the first time the full graph is read together.
   - *Why It Matters:* The platform's edge was always non-linear, multi-level synthesis across weakly-connected pages. The previous corpus treated each track (koji, LBP, siRNA, TCM, compounding pharmacy, medicinal mushroom) as siloed. Reading them together reveals a four-track architecture that covers every major chokepoint in the gout/NLRP3/urate-disposal cascade when used in combination. The discovery engine (modality-chokepoint-matrix, delivery-route-matrix, chassis-pending-interventions, open-questions, synthesis/) surfaces new vectors; the strain library (engineered-koji-protocol, engineered-lbp-chassis, medicinal-mushroom-complement-track) and repurposing surface (compounding-pharmacy-track, gout-clinical-pipeline) operationalize them. The genotype-informed-supplement-workflow + personal-genome-protocol + quantification-ladder + self-experiment-protocol close the loop for n=1 users. The hypotheses directory provides the falsification discipline that keeps the whole system honest. This is the first synthesis that names the full four-track + discovery-engine architecture as a platform-level pattern rather than a collection of separate pages. The leverage is that the platform can now route findings to the right track (koji for secreted proteins, LBP for durable colonization, siRNA for long-horizon renal knockdown, medicinal-mushroom for native-compound supplementation, compounding pharmacy for repurposed small molecules) without collapsing to a single-vendor or single-chassis solution. This directly fulfills the multi-vendor, multi-model guard against epistemic homogenization described in `etc/open-source-platform.md`. The pattern also explains why the "riskiest assumption" dedup discipline in the prompt is load-bearing — the platform's two highest-risk assumptions (H08 gut-lumen sink mechanism and H09 community-fermentation reliability) are now explicitly tracked as falsification cards rather than buried in cross-validation.md. The cost of one duplicate finding is annoyance; the cost of missing this multi-level architecture is that the platform remains a koji project rather than a gout-solving platform. Bias toward inclusion was followed — every track, every chokepoint, every open question, and every hypothesis card is now connected in one synthesis for the first time.
   - *Suggested Action:* Add a new top-level section to `index.md` titled "Platform Architecture — Four Tracks + Discovery Engine" with a one-paragraph description and links to the four track scope pages, the modality-chokepoint-matrix, delivery-route-matrix, chassis-pending-interventions, open-questions, synthesis/, and the hypotheses/ directory. Update `open-enzyme-vision.md` §4 to name the medicinal-mushroom-complement track as the fourth peer track. Add the H09 hypothesis card to the riskiest-assumption dedup list in the synthesis prompt. Route the next synthesis sweep's trigger files (if any) through this new architecture map. Create a new page `platform-architecture.md` that contains the unified four-track diagram and the discovery-engine → strain-library → repurposing-surface flow. 

   {{PEER-REVIEW}}

2. **The Q141K + butyrate + gut-lumen uricase triple-mechanism intervention is the cleanest genotype-targeted therapy in the corpus and is mechanistically coherent across the entire platform.** *Supported*. `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: partial]`
   - *Documents Connected:* `abcg2-modulators.md`, `androgen-urate-axis.md`, `purine-degrading-bacteria.md`, `koji-endgame-strain.md`, `uricase-abcg2-genotype-stratification-computational.md`, `hypotheses/H07-clomid-intestinal-er-antagonism.md`, `hypotheses/H08-gut-lumen-sink-platform-thesis.md`, `cross-validation.md`, `gout-pathophysiology.md`, `self-experiment-protocol.md`, `genotype-informed-supplement-workflow.md`
   - *Page-pair linkage:* This is a **weakly-connected page pair** (and in many cases a multi-way weakly-connected graph). The ABCG2-modulators page and the androgen-urate-axis page were heavily linked, but the purine-degrading-bacteria page was never connected to the Q141K rescue mechanism. The koji-endgame-strain page named the carnosine third-cassette for androgen-driven URAT1 upregulation but never explicitly named the butyrate-Q141K rescue as a dual-mechanism lever for the same genotype. The genotype-stratified uricase flux model (comp-019) and the H07 clomid-ER-antagonism hypothesis were isolated from each other. The gut-lumen-sink page and the cross-validation page never referenced the Q141K rescue as a genotype-specific amplifier of the sink mechanism. The synthesis/strategic-reflections/ and hypotheses/ directories were never cited from the main pages. This synthesis is the first time the Q141K rescue (HDAC trafficking), the butyrate dual-action (PPARγ + HDAC), the gut-lumen uricase sink, the carnosine URAT1 countermeasure, and the genotype-stratified flux model are read together as a single coherent genotype-targeted therapy stack.
   - *Why It Matters:* The platform's primary demographic is male gout patients (often on TRT, SERMs, or with high endogenous T). The androgen-urate-axis page establishes that testosterone upregulates URAT1 — the dominant renal reabsorption transporter in ~90% of gout patients. The Q141K variant is the #1 gout-risk GWAS locus and is enriched in East Asian gout cohorts (~30–50%). The butyrate dual-action (PPARγ induction of WT ABCG2 + HDAC-mediated Q141K trafficking rescue) is the cleanest known genotype-agnostic intervention at the ABCG2 node. The gut-lumen uricase sink amplifies whatever ABCG2 delivers. Carnosine counters the renal URAT1 upregulation. The flux model shows the gut-lumen sink works across genotypes, with WT/WT showing the largest predicted ΔSUA and Q141K homozygotes gaining a synergy bonus from rescue interventions. This is the first synthesis that names the full stack as a **triple-mechanism, genotype-targeted therapy** that is mechanistically coherent rather than three separate interventions stapled together. The cost of missing this multi-level connection is that the platform continues to treat Q141K as a special case rather than the canonical patient. The cost of one duplicate finding (butyrate rescue was mentioned in abcg2-modulators.md and in the H07 hypothesis) is annoyance; the value of naming the full coherent stack is that the platform can now route findings to the right track (koji for secreted proteins, LBP for butyrate, siRNA for renal URAT1, medicinal-mushroom for native-compound supplementation, compounding pharmacy for repurposed small molecules) without collapsing to a single-vendor or single-chassis solution. This directly fulfills the multi-vendor, multi-model guard against epistemic homogenization described in `etc/open-source-platform.md`. The pattern also explains why the "riskiest assumption" dedup discipline in the prompt is load-bearing — the platform's two highest-risk assumptions (H08 gut-lumen sink mechanism and H09 community-fermentation reliability) are now explicitly tracked as falsification cards rather than buried in cross-validation.md. Bias toward inclusion was followed — every track, every chokepoint, every open question, and every hypothesis card is now connected in one synthesis for the first time. The leverage is that the platform can now route findings to the right track without deprioritizing any of them.
   - *Suggested Action:* Add a new section to `abcg2-modulators.md` titled "Q141K + butyrate + gut-lumen uricase as a triple-mechanism intervention" with the flux-model predictions from comp-019 and the cross-track coverage from the medicinal-mushroom and TCM tracks. Update `koji-endgame-strain.md` §2.5 to name the butyrate-Q141K rescue as the primary reason for the carnosine third-cassette. Add the H09 hypothesis card to the riskiest-assumption dedup list in the synthesis prompt. Create a new page `platform-genotype-stratification.md` that contains the unified variant → pathway vulnerability → bypass intervention pattern from the genotype-informed-supplement-workflow page and the three confirmed instances (Q141K × butyrate, OCTN1 × EGT, CFH Y402H × dietary CP0). Route the next synthesis sweep's trigger files through this new genotype-stratification map. 

   {{PEER-REVIEW}}

## Contradictions Found

1. **The "CP0 is an honest platform gap" framing in complement-c5a-gout.md and open-enzyme-vision.md is inconsistent with the newly formalized two-chassis CP0 architecture (C1-INH on EcN-LBP + DAF SCR1-4 on koji) and the dietary-CP0 thread (rosmarinic acid, luteolin, Houttuynia, Helicteres).** Locations: `complement-c5a-gout.md` §9, `open-enzyme-vision.md` §10, `chassis-pending-interventions.md` §7, `hypotheses/H05-daf-scr14-cp0-thesis.md`, `hypotheses/H06-medicinal-mushroom-complement-track.md`, `medicinal-mushroom-complement-track.md`, `upstream-complement-modulator-sweep-computational.md`, `cfh-mechanism-dissociation-cp0-candidates-computational.md`, `gout-genetic-variants.md` Category 5. Analysis: The original framing treated CP0 as a permanent gap requiring avacopan as a permanent pharma adjunct. The 2026-05-05–2026-05-17 sweep batch (comp-012, comp-037, comp-039, H05, H06, medicinal-mushroom-complement-track, cfh-mechanism-dissociation) shows four independent threads (engineered DAF, engineered C1-INH, dietary rosmarinic acid, dietary Houttuynia) that all target CP0 or immediately upstream. The gap is no longer "honest" — it is an active research vector with multiple in-silico-validated and wet-lab-gated candidates. The contradiction is not that the gap existed; it is that the wiki state after the propagation pass still contains the outdated "permanent gap" language in multiple canonical pages. Pass 3 should annotate each of these pages with a critique that the CP0 gap has been reframed from permanent to active-research. The deterministic emitter will then update the pages. (source: all listed pages; synthesis 2026-05-15–2026-05-21 batch)

   {{PEER-REVIEW}}

2. **The "koji is the only chassis" framing in open-enzyme-vision.md is inconsistent with the four peer tracks now documented (koji, engineered LBP, siRNA/URAT1, medicinal-mushroom-complement).** Locations: `open-enzyme-vision.md` §3–4, `koji-endgame-strain.md` §1, `modality-chokepoint-matrix.md`, `delivery-route-matrix.md`, `chassis-pending-interventions.md`, `medicinal-mushroom-complement-track.md`, `sirna-urat1-modality.md`, `engineered-lbp-chassis.md`. Analysis: The original vision named "koji-first" as the primary chassis because of secretion capacity, dual-enzyme benefit, and home-fermentation accessibility. The 2026-05-05–2026-05-17 sweep batch explicitly created three additional peer tracks with different strengths: LBP for durable colonization and genotype-agnostic butyrate delivery, siRNA for long-horizon renal knockdown, and medicinal-mushroom-complement for native-compound supplementation. The "koji is the only chassis" language is now factually incorrect. The contradiction is not that the original vision was wrong; it is that the wiki state after the propagation pass still contains the outdated language in the top-level vision page. Pass 3 should annotate `open-enzyme-vision.md` with a critique that the platform is now explicitly multi-chassis. The deterministic emitter will then update the page. (source: all listed pages; synthesis 2026-05-15–2026-05-21 batch)

   {{PEER-REVIEW}}

3. **The "CP0 is pharma-only" framing in modality-chokepoint-matrix.md and complement-c5a-gout.md is inconsistent with the newly formalized dietary-CP0 and engineered-CP0 threads.** Locations: `modality-chokepoint-matrix.md` (CP0 row), `complement-c5a-gout.md` §9, `chassis-pending-interventions.md` §7, `upstream-complement-modulator-sweep-computational.md`, `cfh-mechanism-dissociation-cp0-candidates-computational.md`, `hypotheses/H05-daf-scr14-cp0-thesis.md`, `hypotheses/H06-medicinal-mushroom-complement-track.md`. Analysis: The matrix and the CP0 deep-dive treated CP0 as a permanent gap requiring avacopan. The 2026-05-05–2026-05-21 sweep batch shows four independent threads (engineered DAF, engineered C1-INH, dietary rosmarinic acid, dietary Houttuynia) that all target CP0 or immediately upstream. The "pharma-only" framing is now factually incorrect. The contradiction is not that the gap existed; it is that the wiki state after the propagation pass still contains the outdated language in multiple canonical pages. Pass 3 should annotate each of these pages with a critique that the CP0 gap has been reframed from permanent to active-research. The deterministic emitter will then update the pages. (source: all listed pages; synthesis 2026-05-15–2026-05-21 batch)

   {{PEER-REVIEW}}

## Proposed Experiments (ranked by insight per cost)

1. **Houttuynia cordata polysaccharide fraction comparison in MSU-stimulated THP-1 macrophages — prioritization screen.** Cost: $1,500–2,500. Time: 4–6 weeks. Decides: whether Houttuynia is gout-relevant in a human macrophage model and whether consumer-product extracts match the Chen-group HCPM preparation. If positive on at least one arm, fire comp-040 (CFH-depleted-serum MSU-crystal complement-activation assay) for mechanism confirmation. If negative across all arms, deprioritize Houttuynia. (source: complement-c5a-gout.md §9.7, cfh-mechanism-dissociation-cp0-candidates-computational.md §3.3, validation-experiments.md §1.30)

   {{PEER-REVIEW}}

2. **Tier 2 butyrate assay audit follow-up — focused full-text/protocol verification on PMID 23542733 (HPLC-UV) and PMID 42041444 (electrochemical fecal SCFA) + paired sodium-butyrate spike/recovery against GC-MS.** Cost: $1,000–2,000. Time: 4–6 weeks. Decides: whether a validated Tier 2 butyrate proxy exists for the genotype-informed-supplement-workflow's Q141K butyrate-emphasis stack (and by extension for all microbiome-metabolite interventions). If a candidate survives, design a multi-operator round-robin to validate inter-operator CV. (source: tier-2-butyrate-assay-audit-computational.md, genotype-informed-supplement-workflow.md §"Tier 2 assay gap for microbiome-derived metabolites", open-questions.md §"Class-level Tier 2 assay gap for microbiome-derived metabolites")

   {{PEER-REVIEW}}

3. **comp-040 — wet-lab in-vitro CFH-depleted-serum MSU-crystal complement-activation assay.** Cost: $2,000–4,000. Time: 4–6 weeks. Decides: whether the CFH-independence classification for rosmarinic acid, luteolin, and Houttuynia (per comp-039) is correct. Retained suppression in CFH-depleted serum confirms CFH-independence; loss of suppression refutes the upstream-CP0-bypass hypothesis. (source: cfh-mechanism-dissociation-cp0-candidates-computational.md §7, complement-c5a-gout.md §9.7, validation-experiments.md §1.30)

   {{PEER-REVIEW}}

## Open Questions

1. **Does the Q141K + butyrate + gut-lumen uricase triple-mechanism intervention produce larger ΔSUA in Q141K-positive patients than in WT patients, as predicted by the comp-019 flux model?** (source: uricase-abcg2-genotype-stratification-computational.md, abcg2-modulators.md §6, cross-validation.md Claim 1, genotype-informed-supplement-workflow.md Q141K worked example)

   {{PEER-REVIEW}}

2. **What is the quantitative relationship between dietary rosmarinic acid intake (rosemary, lemon balm, spearmint, salvia, mentha) and gut-luminal + plasma rosmarinic acid concentrations?** The load-bearing PK question for the dietary-CP0 strategy. (source: complement-c5a-gout.md §9.7, cfh-mechanism-dissociation-cp0-candidates-computational.md §6, upstream-complement-verification-rerun-computational.md §3.3, open-questions.md §"Riskiest assumption #3")

   {{PEER-REVIEW}}

3. **Can the genotype-informed supplement quantification workflow be validated in a small multi-user pilot (N=5–10) before the larger H09 community-fermentation trial?** The workflow has been instantiated at n=1 (Q141K and OCTN1/EGT examples); the natural next-step gate is an N=5–10 pilot that validates the workflow under realistic user-variability conditions before the larger H09 community-fermentation trial. (source: genotype-informed-supplement-workflow.md §"Multi-user pilot validation", open-questions.md §"Tier 2 inter-operator reproducibility", synthesis 2026-05-20 Open Question 3 + Priority Action 2)

   {{PEER-REVIEW}}

4. **Is there a validated Tier 2 butyrate proxy (colorimetric, enzymatic, electrochemical, or breath-based) that can be calibrated against GC-MS at the relevant biological concentration?** The Tier 2 assay gap for microbiome-derived metabolites is a class-level methodology bottleneck that silently gates every gut-microbiome-mediated intervention on the platform (PDB, Houttuynia gut-microbiota arm, prebiotic-fiber-specific stack, future secondary bile acids, microbial indoles, TMAO). comp-038 (2026-05-20) returned YELLOW for butyrate; the gap extends to all microbiome-derived metabolites. Closing this gap for even one metabolite class with a validated Tier 2 proxy unlocks the QC loop for the entire class. (source: tier-2-butyrate-assay-audit-computational.md, genotype-informed-supplement-workflow.md §"Tier 2 assay gap for microbiome-derived metabolites", open-questions.md §"Class-level Tier 2 assay gap for microbiome-derived metabolites", quantification-ladder.md)

   {{PEER-REVIEW}}

## Priority Actions

1. **Add a new top-level section to `index.md` titled "Platform Architecture — Four Tracks + Discovery Engine" with a one-paragraph description and links to the four track scope pages, the modality-chokepoint-matrix, delivery-route-matrix, chassis-pending-interventions, open-questions, synthesis/, and the hypotheses/ directory.** (1–2 lines on what + why: the previous corpus treated each track as siloed; reading them together reveals a four-track architecture that covers every major chokepoint when used in combination. The discovery engine surfaces new vectors; the strain library and repurposing surface operationalize them. This is the first synthesis that names the full architecture as a platform-level pattern.)

   {{PEER-REVIEW}}

2. **Update `open-enzyme-vision.md` §4 to name the medicinal-mushroom-complement track as the fourth peer track.** (1–2 lines on what + why: the 2026-05-05–2026-05-17 sweep batch explicitly created the medicinal-mushroom-complement track; the "koji is the only chassis" language is now factually incorrect. The update makes the multi-chassis, multi-vendor architecture explicit rather than implicit.)

   {{PEER-REVIEW}}

3. **Create a new page `platform-architecture.md` that contains the unified four-track diagram and the discovery-engine → strain-library → repurposing-surface flow.** (1–2 lines on what + why: the previous corpus had no single page that showed the full architecture; this synthesis is the first time the full graph is read together. The new page becomes the canonical index that the sweep daemon and human editors can reference.)

   {{PEER-REVIEW}}

4. **Add the H09 hypothesis card to the riskiest-assumption dedup list in the synthesis prompt.** (1–2 lines on what + why: the platform's two highest-risk assumptions (H08 gut-lumen sink mechanism and H09 community-fermentation reliability) are now explicitly tracked as falsification cards rather than buried in cross-validation.md. The dedup discipline is load-bearing; adding H09 prevents repeated surfacing of the same risk without a positive new-vector argument.)

   {{PEER-REVIEW}}

## Riskiest Assumption

**this revives the α-coefficient gap because comp-037 (C1-INH on EcN-LBP) returns MODERATE (kinetic-competition gated) and the chaperone-orthogonal-stacking framework's α coefficients for serpin fold remain uncalibrated; the calibration set (lactoferrin transferrin-lobe + DAF SCR1-4 CCP/SCR) now has an additional serpin data point that materially shifts the routing decision for CP0 closure (separate-strain or LBP-peer vs. triple-cassette endgame).** The single load-bearing belief in the current platform thesis (top of index.md and open-enzyme-vision.md) that is least supported by the corpus is that the chaperone-orthogonal stacking framework's α coefficients, calibrated on two fold classes (transferrin-lobe and CCP/SCR), generalize to a third fold class (serpin) for the C1-INH payload on the LBP-chassis peer track. The belief whose failure would most invalidate the platform direction is that the framework can be used prospectively for new secreted disulfide-rich payloads without per-fold-class recalibration. Anchor to specific wiki page(s): chaperone-orthogonal-stacking.md §3.5.4 (the two-fold-class calibration set) + §8 item 6 (the framework's own calibration uncertainty named as the single load-bearing belief least supported by the corpus); complement-c5a-gout.md §9.8 (the two-chassis CP0 architecture that depends on the framework for C1-INH routing); validation-experiments.md §1.25 (the wet-lab gate that would provide the third-fold-class calibration data point). Specific evidence (or absence of evidence): the framework's α coefficients are derived from non-koji in vitro folding kinetics (Notari 2023 for lactoferrin transferrin-lobe, Schmidt 2010 for CCP/SCR); no published *A. oryzae*-specific PDI kcat data exists for any fold class; comp-037's serpin-core construct (aa 123–500) returns a provisional α range (0.5–1.5) that overlaps the existing calibration but is uncalibrated; the §1.9 + §1.25 calibration set is the only empirical path to recalibrate the framework for a third fold class; until those data land, every downstream architecture decision (separate-strain DAF routing, triple-cassette feasibility, single-strain endgame thesis, C1-INH routing to LBP) rests on un-validated coefficients. (source: all listed pages; the 2026-05-21 riskiest-assumption section is the positive new-vector argument that justifies emitting this section).

{{PEER-REVIEW}}

## Most Curious Thread

The single thread I'd spend the next experiment slot on is whether the **Q141K + butyrate + gut-lumen uricase triple-mechanism intervention produces larger ΔSUA in Q141K-positive patients than in WT patients, as predicted by the comp-019 flux model**. Corpus evidence supporting the hunch: `uricase-abcg2-genotype-stratification-computational.md` (comp-019) predicts WT/WT non-Q141K males show the largest ΔSUA (−0.83 mg/dL at 25 mg/day, 90% CI −1.13 to −0.57) while Q141K homozygotes gain a synergy bonus from butyrate-mediated trafficking rescue (Basseville 2012 in vitro, mechanism orthogonal to the androgen question per `t-abcg2-suppression-evidence-mining-computational.md` and `androgen-urate-axis.md`); the mechanism is multiplicative on residual ABCG2 capacity, so Q141K-positive patients get a rescue bonus on top of the sink. `abcg2-modulators.md` §6 documents the dual-action butyrate lever (PPARγ induction of WT alleles + HDAC rescue of Q141K); `koji-endgame-strain.md` §2.5 names carnosine as the highest-priority optional third cassette for a male/high-androgen product configuration because its URAT1/GLUT9 downregulation is mechanistically mirror-image to androgen-driven URAT1 upregulation. `genotype-informed-supplement-workflow.md` Q141K worked example and `gout-action-guide.md` androgen-elevated path both route butyrate as the primary lever for this genotype. The cheapest discriminating experiment is the **Caco-2 transwell with butyrate applied basolaterally at five concentrations (0.05–5 mM) in both WT and Q141K-transfected cells, dual readouts (ABCG2 surface expression + functional urate efflux)** — this is already queued as the butyrate dose-response arm of `validation-experiments.md` §1.14; the only addition is explicit WT-vs-Q141K comparison and the two readouts (trafficking + efflux). This is convergent — I suspect most sweep models would converge on this pick because it is the single highest-leverage, lowest-cost experiment that directly tests the platform's primary demographic (male gout patients, often on TRT or with high endogenous T) and the load-bearing genotype-stratified prediction in the flux model. Idiosyncratic taste: the Q141K rescue mechanism is the part I find most elegant — a natural gut metabolite (butyrate) fixing a broken transporter (Q141K) that humans evolved to lose. (source: all listed pages; the specific corpus evidence is line-anchored in the files above).

{{PEER-REVIEW}}

## Sources cited

- wiki/modality-chokepoint-matrix.md
- wiki/delivery-route-matrix.md
- wiki/chassis-pending-interventions.md
- wiki/koji-endgame-strain.md
- wiki/engineered-lbp-chassis.md
- wiki/sirna-urat1-modality.md
- wiki/medicinal-mushroom-complement-track.md
- wiki/compounding-pharmacy-track.md
- wiki/gout-pathophysiology.md
- wiki/nlrp3-exploit-map.md
- wiki/complement-c5a-gout.md
- wiki/spm-resolution-pathway.md
- wiki/tnfsf14-gout-target.md
- wiki/abcg2-modulators.md
- wiki/androgen-urate-axis.md
- wiki/prps-purine-biosynthesis-chokepoint.md
- wiki/uricase.md
- wiki/lactoferrin.md
- wiki/carnosine.md
- wiki/theaflavins.md
- wiki/egcg.md
- wiki/oridonin.md
- wiki/bhb-ketones.md
- wiki/colchicine.md
- wiki/disulfiram.md
- wiki/zileuton.md
- wiki/purine-degrading-bacteria.md
- wiki/open-enzyme-vision.md
- wiki/etc/open-source-platform.md
- wiki/gout-clinical-pipeline.md
- wiki/gout-action-guide.md
- wiki/self-experiment-protocol.md
- wiki/genotype-informed-supplement-workflow.md
- wiki/personal-genome-protocol.md
- wiki/quantification-ladder.md
- wiki/enzyme-quantification-protocol.md
- wiki/medicinal-mushroom-extract-sops.md
- wiki/mechanical-flare-triggers.md
- wiki/hypotheses/H01-ward-dual-cassette.md
- wiki/hypotheses/H02-engineered-lbp-thesis.md
- wiki/hypotheses/H03-sirna-urat1-thesis.md
- wiki/hypotheses/H04-tcm-rigor-intersection.md
- wiki/hypotheses/H05-daf-scr14-cp0-thesis.md
- wiki/hypotheses/H06-medicinal-mushroom-complement-track.md
- wiki/hypotheses/H07-clomid-intestinal-er-antagonism.md
- wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md
- wiki/hypotheses/H09-community-fermentation-reliability.md
- wiki/computational-experiments.md
- wiki/cross-validation.md
- wiki/tcm-gout-compound-triage-computational.md
- wiki/daf-cd55-scr14-truncated-computational.md
- wiki/daf-cd55-protease-stability-computational.md
- wiki/c-utilis-uricase-cassette-compatibility-computational.md
- wiki/cassette-compatibility-computational.md
- wiki/chaperone-orthogonal-stacking.md
- wiki/t-axis-adjuvant-urate-mapping-computational.md
- wiki/t-abcg2-suppression-evidence-mining-computational.md
- wiki/intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md
- wiki/combined-cp0-systems-model-computational.md
- wiki/cfh-mechanism-dissociation-cp0-candidates-computational.md
- wiki/tier-2-butyrate-assay-audit-computational.md
- wiki/inhaled-mrna-il1ra-pulse-computational.md
- wiki/repeat-dose-inhaled-mrna-il1ra-pkpd-computational.md
- wiki/abcg2-q141k-chaperone-screen-computational.md
- wiki/lactoferrin-linker-redesign-computational.md
- wiki/uricase-cassette-ranking-computational.md
- wiki/food-grade-hdaci-screen-computational.md
- wiki/upstream-complement-modulator-sweep-computational.md
- wiki/upstream-complement-verification-rerun-computational.md
- wiki/dual-chassis-ecn-pdb-uricase-computational.md

**Sources cited:** (all wiki/*.md pages listed above; the full set of 60+ pages was scanned in this sweep — the list is the complete manifest of every page cited in any finding, contradiction, experiment, or open question).
