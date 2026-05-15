---
title: "Synthesis — 2026-05-15 (commit ebbce26)"
date: 2026-05-15
commit: ebbce2699d727492d30ec852e3d132300d9dec57
diff_base: 65f9338140c623ac6c7d1af9b4c02b0df40972cb
trigger_files: wiki/GRAPH.md,wiki/abcg2-modulators.md,wiki/aspergillus-oryzae.md,wiki/autonomous-screening-methodology.md,wiki/bio-ai-tools.md,wiki/c-utilis-uricase-cassette-compatibility-computational.md,wiki/cassette-compatibility-computational.md,wiki/chaperone-orthogonal-stacking.md,wiki/chassis-pending-interventions.md,wiki/chembl-cross-check.md,wiki/complement-c5a-gout.md,wiki/compounding-pharmacy-track.md,wiki/computational-experiments.md,wiki/cordycepin-cassette-burden-computational.md,wiki/cross-validation.md,wiki/daf-cd55-protease-stability-computational.md,wiki/daf-cd55-scr14-cassette-ranking-computational.md,wiki/daf-cd55-scr14-truncated-computational.md,wiki/delivery-route-matrix.md,wiki/engineered-koji-protocol.md,wiki/engineered-lbp-chassis.md,wiki/engineered-yeast-uricase-proposal.md,wiki/food-grade-hdaci-screen-computational.md,wiki/ginkgo-cloud-lab-evaluation.md,wiki/gout-action-guide.md,wiki/gout-kill-chain-delivery-routes.md,wiki/gsdmd-pore-delivery-paradox.md,wiki/gut-lumen-sink.md,wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md,wiki/hypotheses/H09-community-fermentation-reliability.md,wiki/hypotheses/README.md,wiki/intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md,wiki/koji-endgame-strain.md,wiki/lactoferrin-protease-stability-computational.md,wiki/lactoferrin.md,wiki/linter-design.md,wiki/medicinal-mushroom-complement-track.md,wiki/medicinal-mushroom-compound-mapping-computational.md,wiki/medicinal-mushroom-extract-sops.md,wiki/modality-chokepoint-matrix.md,wiki/open-enzyme-vision.md,wiki/open-questions.md,wiki/open-source-platform.md,wiki/paperclip-deep-dive.md,wiki/personal-genome-protocol.md,wiki/prps-purine-biosynthesis-chokepoint.md,wiki/purine-degrading-bacteria.md,wiki/self-experiment-protocol.md,wiki/sirna-urat1-modality.md,wiki/supplement-abcg2-antagonism-computational.md,wiki/supplements-stack.md,wiki/t-abcg2-suppression-evidence-mining-computational.md,wiki/t-axis-adjuvant-urate-mapping-computational.md,wiki/tcm-gout-compound-triage-computational.md,wiki/tcm-modern-rigor-intersection.md,wiki/team.md,wiki/upstream-complement-modulator-sweep-computational.md,wiki/upstream-complement-verification-rerun-computational.md,wiki/uricase-abcg2-genotype-stratification-computational.md,wiki/uricase-cassette-ranking-computational.md,wiki/uricase-protease-stability-computational.md,wiki/uricase.md,wiki/validation-experiments.md,wiki/zileuton.md
reviewer_model: deepseek/deepseek-v4-pro
reviewer_model_served_raw: deepseek/deepseek-v4-pro-20260423
reviewer_model_requested: deepseek/deepseek-v4-pro
reviewer_fallback_used: False
input_tokens: 893486
output_tokens: 8000
cost_usd: 0.3956
corpus_files: 111
---

# Synthesis — 2026-05-15
**Substrate:** Open Enzyme wiki at commit `ebbce26`
**Trigger files:** `chassis-pending-interventions.md`, `delivery-route-matrix.md`, `compounding-pharmacy-track.md`, `ginkgo-cloud-lab-evaluation.md`, `autonomous-screening-methodology.md`, `purine-degrading-bacteria.md`, `self-experiment-protocol.md`, `quantification-ladder.md`, `chaperone-orthogonal-stacking.md`, `daf-cd55-scr14-cassette-ranking-computational.md`, `lactoferrin.md`, `bio-ai-tools.md`, and ~60 other pages (full list in trigger block)
**Diff base:** `65f9338140c623ac6c7d1af9b4c02b0df40972cb`
**Reviewer:** deepseek/deepseek-v4-pro

---

## New Connections

1. **The PDB-Engineered EcN + Compounded Disulfiram bridge forms a dual CP6 intervention spanning two delivery modalities.** *Speculative.* `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* `purine-degrading-bacteria.md`, `compounding-pharmacy-track.md`, `chassis-pending-interventions.md`, `disulfiram.md`, `engineered-lbp-chassis.md`
   - *Page-pair linkage:* The PDB page recently documented the 2,8-dioxopurine anaerobe pathway and the CBT2.0 engineered *E. coli* Nissle strain achieving −63% plasma UA in mice (Li et al. 2025, PMID 41070194). The compounding pharmacy track and chassis-pending indices independently list disulfiram (CP6b GSDMD inhibitor) as a top repurposing candidate. None of these pages, however, propose the **combination** of an engineered anaerobic PDB probiotic for sustained gut urate → SCFA conversion with a compounded oral disulfiram pill for systemic GSDMD pore blockade.
   - *Why It Matters:* This pairing covers **both branches of CP6 simultaneously** — luminal urate disposal (CP6-upstream) via PDB + pyroptotic exit blockade (CP6b) via disulfiram — through non-overlapping chassis (EcN LBP vs. small-molecule Rx). Unlike the koji uricase platform, the PDB route is substrate-augmenting (generates butyrate that induces ABCG2), and disulfiram adds a mechanistically orthogonal anti-pyroptotic effect. Together they could achieve additive flare suppression and urate lowering without requiring a single organism to carry all functions. This is a **multi-chassis, multi-compound precision stack** that exploits the fact that neither arm requires koji’s secretion machinery or aerobic fermentation.
   - *Suggested Action:* Queue a comp-NNN feasibility analysis for dual-chassis EcN (PDB cluster from CBT2.0 + PULSE’s uricase, or PDB alone) and map the additive SUA reduction predicted from comp-019 + PDB butyrate ABCG2 induction. Simultaneously, model disulfiram’s GSDMD dose window (comp-027) to ensure co-administration timing aligns with the gut transit of the EcN product.
   {{PEER-REVIEW}}

2. **CFTR-corrector pharmacology for ABCG2 Q141K creates a new small-molecule repair track orthogonal to butyrate/HDAC rescue.** *Speculative.* `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* `chassis-pending-interventions.md`, `abcg2-modulators.md`, `compounding-pharmacy-track.md`, `modality-chokepoint-matrix.md`
   - *Page-pair linkage:* The chassis-pending page now lists “Pharmacological chaperones for ABCG2 Q141K folding rescue” as a standalone intervention, explicitly citing the CFTR-corrector precedent (ivacaftor/tezacaftor/elexacaftor for ΔF508 CFTR — same ATP-binding cassette superfamily). The ABCG2 modulators page already covers Q141K rescue via HDAC inhibitors (butyrate) but not via direct pharmacological chaperones. The compounding pharmacy track could serve as the delivery route for any repurposed corrector found in a computational screen.
   - *Why It Matters:* This opens a **genotype-targeted, small-molecule repair strategy** that is entirely independent of the koji chassis and the diet-microbiome axis. If an existing CFTR-corrector or similar compound binds Q141K ABCG2 and restores apical trafficking, it could be compounded as a daily pill for Q141K-positive gout patients — a population the platform has specifically stratified. The CFTR class has proven that small molecules can rescue misfolded ABC transporters; the gap is that no one has applied this chemistry to ABCG2 Q141K.
   - *Suggested Action:* The chassis-pending entry already proposes a comp-NNN (computational screen of FDA-approved correctors against Q141K ABCG2 AlphaFold structure). Prioritize this as a $0, subagent-friendly lit scan + docking study — it is the cheapest possible entry point and could directly surface a repurposing candidate ready for compounding.
   {{PEER-REVIEW}}

3. **The inhaled mRNA-IL-1RA pulse bridges the chronic oral platform with acute flare termination, closing the speed-of-onset gap.** *Speculative.* `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* `delivery-route-matrix.md`, `chassis-pending-interventions.md`, `modality-chokepoint-matrix.md`, `open-enzyme-vision.md`
   - *Page-pair linkage:* The new delivery-route-matrix and chassis-pending inventory both flag inhaled mRNA-IL-1RA as a future acute-flare intervention, but they frame it as a standalone concept. The broader platform currently has no fast-acting tool — the koji uricase and NLRP3 supplement stacks are chronic-prevention modalities. The addition of a transiently-expressed IL-1 receptor antagonist delivered by pulmonary inhaler provides a **temporal complement**: chronic koji for baseline urate disposal and inflammasome dampening; inhaled mRNA pulse for aborting flares at onset.
   - *Why It Matters:* This trims the most significant functional blind spot: the inability to act quickly when a flare starts. The combination is mechanistically clean — short-lived lung expression of IL-1RA does not interfere with gut-lumen sink or chronic NLRP3 modulation. It also leverages mRNA-LNP manufacturing economics against the $300K/yr canakinumab benchmark. The temporal separation (chronic vs. pulsatile) means minimal drug-drug interaction risk.
   - *Suggested Action:* Scope a comp-NNN to estimate mRNA-IL-1RA dose requirements and LNP pulmonary delivery feasibility using published inhaled mRNA programs (CF, RSV) as prior art. Include a PK/PD model comparing inhaled mRNA area-under-curve to subcutaneous anakinra, with cost-per-flare comparison.
   {{PEER-REVIEW}}

4. **The RFdiffusion + ProteinMPNN tool gap closed by BioDesignBench directly enables lactoferrin variant engineering and future protein redesigns.** *Speculative.* `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: partial]`
   - *Documents Connected:* `lactoferrin.md`, `bio-ai-tools.md`, `autonomous-screening-methodology.md`
   - *Page-pair linkage:* The BioDesignBench evaluation (`bio-ai-tools.md` §BioDesignBench) audited OE’s computational tool stack and identified RFdiffusion and ProteinMPNN as absent from the platform, despite being canonical for structure-conditioned sequence redesign. Simultaneously, the lactoferrin dossier (`lactoferrin.md` §12, open question #13) explicitly tags RFdiffusion + ProteinMPNN as needed for future variant design work (lactoferricin constructs, host-optimized glycosylation, apo-form stabilization). This is a **precise match between an identified tool gap and a queued engineering task**, and the protein-design-mcp package (Kim & Romero 2026) makes integration straightforward.
   - *Why It Matters:* Without these tools, lactoferrin optimization for the koji chassis would rely on trial-and-error mutagenesis or limited ESM2 scoring. With them, OE can perform true computational protein redesign — designing disulfide-stabilized or protease-resistant variants tailored to the *A. oryzae* secretory environment — directly addressing the stability concerns flagged in comp-005. This is the first concrete task that justifies deploying the protein-design-mcp server.
   - *Suggested Action:* Deploy the `protein-design-mcp` package locally (already done per `bio-ai-tools.md` §BioDesignBench) and run a pilot redesign of the lactoferrin inter-lobe linker region, targeting improved shio-koji protease resistance. Use comp-030’s multi-metric concordance gate (N-of-3 ≥ 2, combining ESM2, Rosetta, and interface-metrics) to rank candidate sequences before wet-lab testing.
   {{PEER-REVIEW}}

---

## Contradictions Found

1. **The chassis-pending intervention list risks diluting the centralized home-fermentation thesis without a clear triage framework for which chassis to pursue first.** *Documents Connected:* `chassis-pending-interventions.md`, `open-enzyme-vision.md`, `open-source-platform.md`
   - *Analysis:* The platform vision explicitly positions the koji chassis as the first and primary output of the discovery engine, with the strain library as the mechanism for democratized access. The newly added chassis-pending inventory, however, aggregates seven distinct interventions (engineered EcN PDB, siRNA URAT1, LBPs, inhaled mRNA, intra-articular uricase, bacteriophage, pharmacological chaperones) that span commercial pharma, synthetic biology, and formulation chemistry — none of which are home-fermentable. While the discipline “chassis is downstream of chokepoint” is correctly articulated, the practical implication is that a growing fraction of the platform’s most promising leads now live outside the original vision of “grow at home.” There is currently no explicit decision rule for when a chassis-pending intervention should be promoted to an active peer track versus parked as a discovery-engine output.
   - *Resolution:* This is not a contradiction to be resolved by removing interventions, but a **strategic design gap** — the project needs a “chassis triage rubric” to guide resource allocation. This could be formalized as a small addition to `open-source-platform.md` or `chassis-pending-interventions.md` itself.
   {{PEER-REVIEW}}

---

## Proposed Experiments (ranked by insight per cost)

1. **Computational cross-cohort biomarker study: serum selenium, yanthine, and gout incidence.** *Cost: $0. Time: 1–2 weeks. Decides: Whether the selenium-PDB-urate axis is detectable at population scale, and whether selenium deficiency phenocopies PDB functional depletion.*
   - *Rationale:* The purine-degrading bacteria page establishes that DOPDH is selenium-dependent (27× faster with Se) and that serum yanthine is a pathway intermediate elevated in gout. Public metabolomics + GWAS datasets (UK Biobank, NHANES
