---
title: "Open Questions — Research Index"
date: 2026-04-24
tags:
  - open-questions
  - index
  - research-queue
  - unknowns
related:
  - ../synthesis/README.md
  - index.md
  - validation-experiments.md
  - uricase.md
  - engineered-yeast-uricase-proposal.md
  - engineered-koji-protocol.md
  - koji-home-fermentation.md
  - uricase-variant-selection.md
  - protein-engineering-strategy.md
  - gi-survival-prediction.md
  - nlrp3-exploit-map.md
  - nlrp3-inflammasome.md
  - nlrp3-inhibitor-screen.md
  - gout-pathophysiology.md
  - gout-deep-dive.md
  - complement-c5a-gout.md
  - spm-resolution-pathway.md
  - tnfsf14-gout-target.md
  - egcg.md
  - carnosine.md
  - bhb-ketones.md
  - cannabinoids-terpenes.md
  - supplements-stack.md
  - cross-validation.md
  - etc/open-enzyme-vision.md
  - etc/open-source-platform.md
  - modality-chokepoint-matrix.md
  - abcg2-modulators.md
  - androgen-urate-axis.md
  - colchicine.md
  - delivery-route-matrix.md
  - ginkgo-cloud-lab-evaluation.md
sources:
  - "Aggregated from `Open Questions` sections across the Open Enzyme wiki"
status: published
---

# Open Questions — Research Index

A topic-organized index of unresolved scientific, translational, safety, and delivery questions. Each question should link to its evidence and, where possible, a discriminating experiment.

## Inclusion rule

Include a question when the answer could change a mechanism verdict, evidence tier, target population, safety boundary, delivery route, or experiment sequence. Exclude authoring history, outreach logistics, and duplicated queue state.

Research Conjectures live on the page that owns their mechanism. This page may carry a one-line title and link for discovery, but not a second copy of the premises or argument.

## Research conjectures

- **Could local lactoferrin exposure restore intestinal urate export by relieving TNFα-driven ABCG2 suppression?** See the grounded premises, unsupported leap, and discriminating co-culture observation in [ABCG2 modulators](./abcg2-modulators.md#research-conjecture-lactoferrin-could-couple-inflammatory-relief-to-urate-export).
- **Could carnosine preferentially counter an androgen-associated renal urate phenotype?** See the separate animal-model premises and the untested combined experiment in [carnosine](./carnosine.md#research-conjecture-carnosine-may-counter-an-androgen-associated-renal-urate-phenotype).
- **Could selenium availability gate microbial urate disposal even when PDB genes are present?** See the DOPDH cofactor premise and paired abundance-versus-flux test in [purine-degrading bacteria](./purine-degrading-bacteria.md#research-conjecture-selenium-availability-may-gate-microbial-urate-disposal).
- **Could a joint-retained multi-node flare intervention outperform the best single intra-articular arm?** See the route-specific premises and staged factorial in the [gout kill-chain delivery analysis](./gout-kill-chain-delivery-routes.md#research-conjecture-a-local-multi-node-flare-intervention-may-outperform-single-node-ia-blockade).

---

## Uricase / Enzyme Engineering

Questions about uricase variant selection, GI survival, protease resistance, yeast-vs-koji choice, and expression strategy.

### Variant selection and properties

- **Can a disclosed *Candida utilis* sequence candidate reproduce ALLN-346's product-specific properties?** The ALLN-346 clinical records identify an engineered UOX but do not disclose an exact clinical-product sequence that can be assumed equivalent to P78609 or another candidate. Compare accession-bound sequences directly; do not transfer ALLN-346 performance by species name. See [uricase-variant-selection.md](./uricase-variant-selection.md).
- **No human trial data identified here tests *A. flavus* UOX orally.** The combined ALLN-346 Studies 101/102 abstract reports no serious adverse events, no clinically significant safety signals, and no detectable systemic absorption during single-dose and seven-day exposure to its *C. utilis*-derived product in healthy volunteers ([Clark et al. 2022](https://doi.org/10.1136/annrheumdis-2022-eular.843)). That does not establish absence of sensitization, chronic safety, or transfer to another UOX product. **Clinical Trial; conference-abstract evidence.**
- **Vibrio vulnificus uricase expression in *S. cerevisiae*: codon optimization and titer remain unknown.** Likely feasible from sequence analysis; no peer-reviewed titer in eukaryotic hosts. See [uricase-variant-selection.md](./uricase-variant-selection.md).
- **How does repeated oral exposure to a specific UOX product affect sensitization or tolerance?** Open — route alone does not predict the immune result, and short ALLN-346 exposure cannot be transferred to another sequence, host, impurity profile, or formulation. See [uricase — oral-tolerance boundary](./uricase.md#oral-tolerance-boundary).

### GI survival and stability

- **Refolding kinetics of acid-unfolded uricase are unknown.** The enzyme's tetramer dissociates at low pH; whether it refolds after duodenal pH normalization determines real-world efficacy beyond simple in vitro survival measurements. See [gi-survival-prediction.md §§refolding](./gi-survival-prediction.md).
- **Does rice bran substrate improve or degrade uricase GI survival?** Rice bran contains phytic acid, phenolics, and fiber — could stabilize the tetramer (polyphenol-tetramer binding) or destabilize it (altered transit time). See [engineered-koji-protocol.md](./engineered-koji-protocol.md).
- **Secretion vs. intracellular expression in yeast — which preserves more active UOX at the reaction site?** Cell-wall protection, release, extracellular proteolysis, expression, oxygen and urate access, and peroxide control are all unmeasured for the complete configurations. Compare topologies directly; no fixed survival advantage or effective dose is established. See [engineered-yeast-uricase-proposal.md](./engineered-yeast-uricase-proposal.md) and validation §1.33.

### Wild-type koji baseline and EPI applications

- **What is the quantitative enzyme activity of shio-koji (units/g) vs. commercial PERT (Creon, Zenpep units per pill)?** Lab-measurable via amylase / protease / lipase assays of finished shio-koji, but not yet done. This is the key comparison that determines whether wild-type koji is a meaningful PERT-reducer or merely a condiment. **Methodology now specified in [enzyme-quantification-protocol.md](./enzyme-quantification-protocol.md)** — Tier 3 bench first-run (~$200–400 reagents, single-day session at a community-college lab) is the load-bearing experiment. See also [koji-home-fermentation.md](./koji-home-fermentation.md). (source: koji-home-fermentation.md, enzyme-quantification-protocol.md)
- **Does characterized shio-koji pretreatment change protein or lipid digestion under controlled conditions?** Start with matched in-vitro digestion and measured enzyme activity. Any PERT-sparing claim would require a regulated clinical study and cannot be established by a household observation. See [koji-home-fermentation.md](./koji-home-fermentation.md). (source: koji-home-fermentation.md)
- **What is the gastric survival of shio-koji-derived enzymes?** Hypothesis: poor without enteric coating; useful only for pre-digestion in marinade phase, not in-gut activity post-ingestion. Testable via simulated gastric fluid (SGF pH 2, pepsin, 2h). See [koji-home-fermentation.md](./koji-home-fermentation.md). (source: koji-home-fermentation.md)
- **Is lipase the limiting digestive-enzyme axis for fat malabsorption EPI when using wild-type *A. oryzae* shio-koji?** Lipase activity of *A. oryzae* shio-koji is low compared to *A. niger* or engineered strains. Quantitative comparison needed. Methodology in [enzyme-quantification-protocol.md §3.1](./enzyme-quantification-protocol.md) (p-NPP lipase assay vs. Creon-cap-equivalent reference standard). See also [koji-home-fermentation.md](./koji-home-fermentation.md), [aspergillus-oryzae.md](./aspergillus-oryzae.md). (source: koji-home-fermentation.md, enzyme-quantification-protocol.md)
- **Are there any human studies of koji-fermented diets in EPI specifically?** None identified. Would be high-value evidence. See [koji-home-fermentation.md](./koji-home-fermentation.md). (source: koji-home-fermentation.md)

### Yeast vs. koji host choice within enzyme-production tracks

- **At what expression and recovery levels does a yeast route become operationally competitive?** Existing mass-burden estimates are track-specific assumptions, not a reason to appoint a different chassis as the project default. See [engineered-yeast-uricase-proposal.md §5](./engineered-yeast-uricase-proposal.md).
- **Can the Ward 1995 *A. awamori* glucoamylase-fusion + KEX-2 architecture (>2 g/L submerged) transfer to solid-state rice koji fermentation?** The submerged-culture precedent is solid (PMID 9634791). Solid-state mass transfer, redox, and proteolysis dynamics are different. This is the specific gating experiment for the lactoferrin co-expression module. See [engineered-koji-protocol.md §16](./engineered-koji-protocol.md), [spm-resolution-pathway.md §5](./spm-resolution-pathway.md).

### Protein engineering

- **Can either geometry-verified disulfide candidate improve retained active UOX without impairing expression, assembly, or catalysis?** The second pair is not fixed; wild type, single-Cys controls, each pair, and any combination require matched testing in the selected topology. See [protein-engineering-strategy.md](./protein-engineering-strategy.md).
- **What is the minimal protease-resistant mutation set that preserves UOX activity in the selected topology?** Public ALLN-346 engineering disclosures are a candidate source of variants, but their performance must be verified against the exact disclosed parent, assay, and formulation before use. See [uricase-variant-selection.md](./uricase-variant-selection.md).

### Genotype stratification of the gut-lumen sink response

- **Does ABCG2 genotype modify response to a physiologically credible gut-lumen UOX configuration?** No valid model currently supplies a ΔSUA, genotype ordering, or dose recommendation. The comp-019 search found no Q141K-stratified uricase clinical outcome in its searched sources as of 2026-05-08; this is a bounded search result, not universal absence. Test genotype only after an exact configuration clears physiological substrate, oxygen, access, survival, transit, and peroxide gates. See [validation experiment 1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial).

### Co-engineered substrate-supply mechanisms

Strategic question across the engineering pipeline: should the chassis produce both substrate degradation (uricase) and substrate-supply enhancement (ABCG2 induction or relief of suppression)? The architecture remains plausible, but neither additivity nor genotype-independence is established. Directly measure transporter flux and UOX consumption together; do not inherit comp-019's serum-response mapping.

Three candidate routes are currently defined, each with a different chassis-level implication:

- **Butyrate co-production or co-formulation with a butyrogenic strain.** Butyrate can induce wild-type ABCG2 through PPARγ in relevant models. Whether it directly rescues Q141K surface trafficking and functional urate flux is unproven; Basseville 2012 supplies a rescue-pathway precedent, not a butyrate result. Co-formulation is therefore gated on validation §1.14 and strain-specific carbon fate.

- **Glucoraphanin co-production (Nrf2 → ABCG2 induction).** Already flagged at [abcg2-modulators.md §Engineering implications #1](./abcg2-modulators.md). Sulforaphane precursor produced in the chassis, converted to active sulforaphane by gut myrosinase from cruciferous-resident bacteria. **Mechanistic Extrapolation; *A. oryzae* glucoraphanin biosynthetic pathway feasibility not yet assessed** — multi-enzyme plant pathway, fungal-host expression unknown.

- **Lactoferrin co-expression and the TNFα–ABCG2 hypothesis.** [Engineered-koji protocol §16](./engineered-koji-protocol.md) defines the expression question. Whether compartment-matched lactoferrin changes TNFα signaling, ABCG2 surface expression, and functional urate flux is unmeasured; validation §1.14 must test the composed mechanism directly.

Decision-gate framing: a chassis that produces uricase plus a candidate supply enhancer adds engineering burden and a second uncertain biological function. The net effect could be positive, neutral, or counterproductive because transporter supply, enzyme consumption, oxygen, residence time, and compartment access interact. Do not infer super-additivity. Decide only from matched transporter-flux and UOX-consumption measurements after the uricase-alone operating regime is established.

See [abcg2-modulators.md](./abcg2-modulators.md), [gut-lumen-sink.md](./gut-lumen-sink.md), [engineered-koji-protocol.md](./engineered-koji-protocol.md).

---

## NLRP3 / Gout Biology

### Multihop program (2026-07-13)

Eleven interface questions form a unified
[gout multihop research program](./gout-multihop-research-program.md): physiological UOX
topology, staged precursor/urate sinks, the enterocyte NLRP3–PDZK1–ABCG2 paradox, luminal
redox safety, PDB carbon fate/self-niche, T0SS UOX-OMVs, fructose–NOX–ABCG2, purinergic
resolution, bile-acid FXR/TGR5 signaling, succinate compartment bifurcation, and PDB–XO
inhibitor compatibility. Concrete protocols are [validation experiments
1.33–1.43](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial).

Questions about chokepoint biology, priming mechanisms, species-gap caveats, and biomarker interpretation.

### Priming and upstream signals

- **Is complement C5a activation necessary or sufficient for MSU-triggered NLRP3 priming in clinical gout flares, or is TLR4/LPS still dominant in real patients?** Cumpelik 2016 (PMID 26245757) and Khameneh 2017 (PMID 28167912) are animal model + in vitro; human C5a-priming dominance remains to be confirmed in vivo. See [complement-c5a-gout.md §6](./complement-c5a-gout.md), [nlrp3-exploit-map.md](./nlrp3-exploit-map.md).
- **Are there patient subgroups where non-complement priming (true LPS from SIBO) dominates?** Would change stack selection per patient. See [complement-c5a-gout.md §6 Q5](./complement-c5a-gout.md).
- **Is TNFSF14/LIGHT elevation a universal feature of gout flares or a patient subtype?** Would a TNFSF14 biomarker identify responders to EGCG or CERC-002 better than generic hs-CRP? See [tnfsf14-gout-target.md](./tnfsf14-gout-target.md).
- **Does lactoferrin-based CP5b engagement eliminate the CP0 priming signal, or only suppress downstream?** See [complement-c5a-gout.md §4 Q4](./complement-c5a-gout.md).

### Chokepoint biology

- **Could an exact, qualified intervention configuration reduce flares during ULT initiation?** This is a future clinical question, not a food-use or home-production claim. An engineered configuration would first need product-specific identity, exposure, safety, containment, and preclinical efficacy gates; any later trial would use established-care prophylaxis as the controlled background. **Mechanistic Extrapolation.**
- **CP1a + CP2/CP3 synergy in vitro.** Is there a measurable synergy between kojic acid (CP1a) and colchicine (CP2/CP3) in suppressing MSU-induced IL-1β release in primary monocytes? A bead-MSU stimulation assay with combinatorial dosing would answer this. (Mechanistic Extrapolation; source: colchicine.md §8)
- **CP5b — why do gout patients' SPM levels remain low during flare?** Dietary precursor shortage, 15-LOX expression defect, or demand outpacing production? See [spm-resolution-pathway.md §6 Q1](./spm-resolution-pathway.md).
- **ALX/FPR2 polymorphisms in gout.** Are there FPR2 genetic variants associated with flare severity or tophi formation? See [spm-resolution-pathway.md §6 Q2](./spm-resolution-pathway.md).
- **Direct SPM bioassay feasibility.** SPM measurement requires LC-MS/MS at pg/mL. Practical for clinical biomarker stacks, or research-only? See [spm-resolution-pathway.md §6 Q3](./spm-resolution-pathway.md).
- **Does aggNET-mediated C5a sequestration feed back to CP0?** The resolution loop may close on itself (SPM → aggNET → C5a sequestration → reduced priming). Mechanistic elegance suggests yes; direct evidence is thin. See [spm-resolution-pathway.md §6 Q4](./spm-resolution-pathway.md).

### Chokepoint candidates from comp-014 (2026-05-06)

- **Does ADA (adenosine deaminase) warrant formal addition as a named gout chokepoint?** ADA catalyzes adenosine → inosine in purine catabolism upstream of XO. comp-014 Phase 2 (6,798 fungal compounds) identified ADA as a target with fungal-compound coverage via GLPP (*G. lucidum*) and cordycepin + native pentostatin (*C. militaris*). Pending Phase 3-6 comp-014 follow-ups for formal admit/reject decision. See [medicinal-mushroom-compound-mapping-computational.md](./medicinal-mushroom-compound-mapping-computational.md), [gout-pathophysiology.md §ADA](./gout-pathophysiology.md). (Mechanistic Extrapolation; source: medicinal-mushroom-compound-mapping-computational.md)
- **Does PINK1/mitophagy warrant formal addition as a named gout chokepoint?** PINK1 senses mitochondrial damage and recruits Parkin to initiate mitophagy, clearing damaged mitochondria before they generate the mtROS that triggers NLRP3 (CP2). NLRP3-priming-adjacent — operates upstream of CP2. comp-014 Phase 2 identified fungal compounds with PINK1-modulating activity. Pending Phase 3-6 comp-014 follow-ups for formal admit/reject decision. See [medicinal-mushroom-compound-mapping-computational.md](./medicinal-mushroom-compound-mapping-computational.md), [gout-pathophysiology.md §PINK1](./gout-pathophysiology.md). (Mechanistic Extrapolation; source: medicinal-mushroom-compound-mapping-computational.md)

### Chokepoint candidates and sub-questions from comp-018 (2026-05-08)

[comp-018 — Upstream Complement Modulator Sweep](./upstream-complement-modulator-sweep-computational.md) confirmed direct natural-product C5aR1 antagonist class triply-empty (comp-014 + §1.21 + comp-018), but found a substantial dietary / fungal / FDA-approved-drug literature one node upstream at C3 convertase (rosmarinic acid TIER-1 dietary, luteolin triple-mechanism, etc.). Two open follow-ups remain:

- **Are there compounds that *upregulate the host-side complement regulators* (Factor H, DAF/CD55, CD59, clusterin, CR1) — proteins that protect host cells from complement attack — and would such compounds provide a fundamentally different mechanism for CP0 closure?** comp-018 Phase 1's brief explicitly included regulator-expression upregulation in the target list, but the results came back direct-inhibitor-dominant; the expression-modulation thread is largely *unanswered* and worth a focused Phase 2 sub-task. The question is mechanistically distinct: direct inhibition reduces convertase activity acutely, while regulator upregulation is a chronic, transcriptionally-mediated mode of action that may behave differently in a gut-mucosa context (sustained dietary exposure → durable Factor H upregulation → chronic CP0 dampening). Anchor any Phase 2 answer to expression datasets (GTEx, HPA, GEO microarray) plus complement-functional assays — gene upregulation alone wouldn't prove C3/C5 convertase suppression in vivo. (Queued as a comp-018 Phase 2 sub-task.)
  - **Anchor compound classes worth checking:** plant-derived Nrf2 activators (sulforaphane, curcumin, EGCG — already in supplements-stack), butyrate (HDAC inhibitor, plausible Factor H induction), retinoids, dietary polyphenols generally. Cross-applies to the [food-grade HDACi screen (comp-007)](./food-grade-hdaci-screen-computational.md) — HDAC inhibitors identified for ABCG2 derepression may also induce complement-regulator expression.
  - **Cross-references:** [complement-c5a-gout.md](./complement-c5a-gout.md) (Factor H, DAF/CD55, CD59, clusterin biology), [comp-018](./upstream-complement-modulator-sweep-computational.md), [hypotheses/H05-daf-scr14-cp0-thesis.md](./hypotheses/H05-daf-scr14-cp0-thesis.md) (engineering-side DAF thread — engineered koji that *secretes* the DAF protein is a distinct mechanism from compounds that *upregulate endogenous DAF expression*).

- **Should "upstream-CP0" be formally designated as a new chokepoint class (CP-1, going further upstream) or kept as scope-expansion of CP0?** comp-018 proposes scope-expansion (working term: "upstream-CP0") with the rationale that the priming chokepoint is unitary at the mechanism level (C5a generation) and subdividing CP0 into "downstream-CP0" (C5aR1 antagonism) vs "upstream-CP0" (everything proximal) reads cleanly within the existing framework. CP-1 would imply a fundamentally different priming mechanism, which isn't the case. Final naming decision is the user's; this question is queued until enough operational substance accumulates around CP0 to make the naming load-bearing. (Source: comp-018 §"Chokepoint-class naming proposal".)

- **What is the quantitative relationship between dietary rosmarinic acid intake (rosemary, lemon balm, spearmint, salvia, mentha) and gut-luminal + plasma rosmarinic acid concentrations?** The load-bearing PK question for the dietary CP0 thread. comp-020 documented a **44× IC50 spread** across published assay formats (34 µM optimal per Englberger 1988 → 137–182 µM per Cimanga 1999 / Mu 2013); separately, human bioavailability data exists in Baba 2004 / Konishi 2005 / Nakazawa 1998 but the dietary-source → gut-luminal concentration → plasma Cmax chain is wide and incompletely characterized. Without a PK anchor, the "dietary CP0 coverage via rosmarinic acid" claim is mechanistically grounded but quantitatively unanchored. **Partially consumed by comp-029 (2026-05-16):** comp-029 used the IC50 distribution + bioavailability ranges with explicit uncertainty bounds, and the resulting YELLOW combined-CP0 verdict is partly attributable to the rosmarinic acid uncertainty (Spearman r = −0.658 for IC50 — the dominant sensitivity driver). comp-029 didn't resolve the open question; it consumed the uncertainty productively. **Resolution path:** human PK study of rosmarinic acid from dietary sources (single-dose, n=6–12, plasma + urine sampling over 24h) — proposed cost ~$15–25K. Partner / clinical-tier work, not OE-direct. Tightening comp-029's input range with measured PK data could flip the combined-CP0 verdict from YELLOW to GREEN. Until then, the dietary rosmarinic acid thread carries an explicit "PK unresolved" caveat per [`complement-c5a-gout.md` §9.7](./complement-c5a-gout.md) and [`upstream-complement-verification-rerun-computational.md`](./upstream-complement-verification-rerun-computational.md). (comp-020 documents the 44× spread; comp-029 documents the YELLOW combined-CP0 verdict.)

- **Can a matrix-specific Tier 2 assay reproduce a Tier 3 reference result across operators and batches?** Validate analytical reproducibility on controlled research material before linking any assay to genotype, exposure, or an intervention study. Prespecify identity, matrix, calibration range, spike/recovery, operator count, batch count, and an acceptance rule. Cheap or portable measurement is useful for research QC only; it does not establish a delivered human dose, target-tissue exposure, safety, or efficacy. See the [genotype-informed intervention research workflow](./genotype-informed-supplement-workflow.md) and [H09 — Community Fermentation Reliability](./hypotheses/H09-community-fermentation-reliability.md).

### Species-gap and translation

- **Does the 1,000× dapansutrile mouse-vs-human cellular IC50 gap apply to every mouse-derived NLRP3 potency claim in the wiki?** Oridonin, BHB, ursolic acid, β-caryophyllene, carnosine — all have murine efficacy as primary evidence. Translation risk is now the dominant uncertainty. See [nlrp3-inhibitor-screen.md ChEMBL appendix](./nlrp3-inhibitor-screen.md).
- **For "pathway modulator" class (quercetin, ursolic acid, BHB, KPV, carnosine, taurine), what's the correct primary-evidence yardstick?** ChEMBL IC50 doesn't exist by definition for these compounds. Is it functional IL-1β suppression in MSU-stimulated human macrophages? See.

### Biomarker interpretation

- **Is hs-CRP alone sufficient to distinguish chokepoint-specific effects in a controlled study?** No — hs-CRP is a downstream output marker. Chokepoint attribution requires prespecified, mechanism-proximal readouts and appropriate controls; candidate measures include LTB4 (CP6a), C5a (CP0), and TNFSF14 (CP1a).

---

### Chronic tophaceous gout — the adaptive-immune axis (scoped 2026-07-13; no-go for a dedicated track)

A scoping scan (Western PubMed / ClinicalTrials.gov + Chinese ChiCTR reached via local curl; two-model cross-check) tested whether the Th17/IL-17 (RORγt) adaptive-immune axis is a driver of tophus biology worth a dedicated Open Enzyme track. **Verdict: no.**

- **Th17/IL-17 is a bystander, not a driver.** Single-cell + spatial transcriptomics of tophus tissue (Xu/Dalbeth/He 2025, PMID 41107120) shows intra-tophus CD4 T cells skew *regulatory*; the destructive work is done by a tophus-exclusive **SPP1/MMP9 macrophage** subset (innate-stromal) driving matrix remodeling + osteoclast bone erosion. **Zero IL-17-blocker gout trials exist** (ClinicalTrials.gov + ChiCTR both checked). Evidence tier for Th17-as-driver: ≤ Mechanistic Extrapolation.
- **What the platform's uricase sink does for tophi (bounded honesty).** Tophus dissolution is a urate-*solubility* problem: sustained SUA <6 mg/dL (ideally <5) dissolves crystals over months (DECT −96% at 6 mo, complete ~24 mo — Pascart 2025 PMID 40139560; pegloticase −71% in ~3 mo — Araujo 2015 PMID 26509070; febuxostat −83% at 52 wk — Becker 2005 PMID 16339094). The gut-lumen sink could contribute only if it produces sustained serum lowering; no valid effect-size prior currently exists after comp-044. It also does nothing directly for the fibrous capsule + eroded-bone scaffold, which may persist after crystals clear.
- **The real (downstream) intervention nodes, if ever pursued:** RANKL/osteoclast bone erosion (denosumab repurposing candidate — with a live comparator: **ChiCTR2300069207**, baricitinib/JAK1-2 for chronic tophaceous gouty arthritis, Phase-4 RCT, primary endpoint = gouty bone erosion, Huashan/Fudan) and the SPP1-macrophage/ECM-fibrosis program (the most distinct novel biology, but no approved SPP1/MMP9 drug — untractable). TCM adjunct signal: **ChiCTR2300071056** (Jianpi Shenshi Granule + febuxostat, tophus endpoint) — sits inside the urate-solubility frame.
- **Adaptive-immune axis remains out of scope:** a peer track needs a falsifiable *driver* thesis; the adaptive-immune axis fails the driver test, and the genuinely distinct chronic-tophus biology is innate-stromal, largely downstream of the crystal burden + IL-1β the CP framework already covers, and not food-grade-engineerable. Ursolic acid's RORγt activity ([nlrp3-inhibitor-screen.md](./nlrp3-inhibitor-screen.md)) is a curiosity here, not a priority. Scan log: [`logs/chronic-tophus-adaptive-axis-scoping-scan-2026-07-13.md`](../logs/chronic-tophus-adaptive-axis-scoping-scan-2026-07-13.md).

## Compound-Specific Questions

Organized by compound, with links to supporting evidence and experiments.

### EGCG

- **Is the 86 nM proteasome IC50 reached at physiological green-tea doses?** At 0.1-0.3% oral bioavailability, unformulated green tea probably can't hit the threshold; phytosome formulations (5-10% bioavailability) plausibly can. Central translation question. See [egcg.md Open questions #1](./egcg.md).
- **Proteasome vs. IKK dose-response.** If the reframe is correct, IκBα stabilization tracks proteasome IC50 (86 nM), IKK activity requires ≥10 μM. A dose titration with both readouts falsifies or confirms. See [egcg.md Open questions #2](./egcg.md).
- **Hepatotoxicity mechanism.** Proteasome-driven, redox-driven, mitochondrial, or immune-mediated? The literature is divided. Resolve mechanism and exposure-response before comparing formulations or combinations. See [egcg.md Open questions #3](./egcg.md).
- **Does EGCG suppress TNFSF14 at the HVEM-receptor level specifically, or only through general NF-κB blockade?** Replication needed in human macrophages. See [egcg.md Open questions #4](./egcg.md), [validation-experiments.md §1.8](./validation-experiments.md).
- **Can DHA + EGCG achieve combined TNFSF14 suppression?** Orthogonal mechanisms; both already in stack. See [egcg.md Open questions #5](./egcg.md).
- **Do theaflavins and EGCG produce nonredundant pathway effects without amplifying hepatic stress?** Their mechanisms differ, but additivity and combined safety are unmeasured. Compare exact materials in a concentration matrix with pathway readouts and a prespecified hepatic-safety panel before any efficacy combination. See [theaflavins.md](./theaflavins.md) and [egcg.md Open questions #3](./egcg.md).

### Quercetin

- **Does quercetin's 300 nM ChEMBL 5-LOX IC50 translate to cellular neutrophil-chemotaxis block in a gout-relevant assay?** A zileuton head-to-head could resolve this if the question becomes decision-relevant.
- **Is quercetin + Boswellia (AKBA) redundant at 5-LOX, or complementary at IKKβ + 5-LOX?** Depends on AKBA's 5-LOX IC50 and whether the two compounds bind at the same site. ChEMBL query pending. See.

### BHB / Ketones

- **Does the ketogenic-diet-gout rat result translate to a human oral BHB dosing regimen?** The rat study used intrinsic ketogenesis (diet); exogenous BHB dosing has different PK. See [bhb-ketones.md](./bhb-ketones.md), [nlrp3-exploit-map.md](./nlrp3-exploit-map.md).
- **Does BHB's mouse-vs-human species gap follow the dapansutrile pattern?** Mouse ketogenic data may overstate BHB's required human dose. See.
- **Does androgen status shift BHB's NLRP3 concentration-response?** BHB has reported activity at multiple NLRP3 nodes ([bhb-ketones.md](./bhb-ketones.md)); direct androgen effects on NLRP3 priming remain directionally ambiguous ([androgen-urate-axis.md](./androgen-urate-axis.md) §"Beyond transporters"). Test androgen × MSU × BHB in a concentration matrix with HCAR2 expression, inflammasome readouts, and viability rather than inferring a human dose. See [validation §1.23](./validation-experiments.md) and [nlrp3-exploit-map.md](./nlrp3-exploit-map.md).

### Lactoferrin

- **Can lactoferrin be expressed as an intact, active product in solid-state *A. oryzae*?** The *A. awamori* >2 g/L precedent is submerged and single-protein. Solid-state output, processing, activity, and batch variance remain unmeasured; a useful exposure target must be derived separately. See [engineered-koji-protocol.md §16](./engineered-koji-protocol.md), [spm-resolution-pathway.md §6 Q6](./spm-resolution-pathway.md).
- **Does *A. oryzae* KEX-2 process a glucoamylase-lactoferrin fusion identically to *A. awamori*?** Critical for transferring the Ward 1995 architecture. See [engineered-koji-protocol.md §16 Risks](./engineered-koji-protocol.md).
- **Is there a dedicated gout trial of oral lactoferrin anywhere?** None identified. See [spm-resolution-pathway.md §6 Q5](./spm-resolution-pathway.md).
- **Which lactoferrin sequence and product format should enter the matched screen?** Bovine food-use history and human *Aspergillus* expression precedent answer different questions; neither transfers safety, processing, or activity to the proposed engineered configuration. See [engineered-koji-protocol.md §16](./engineered-koji-protocol.md).

### Carnosine

- **Human gout RCT evidence is absent.** Hyperuricemia rat dual-phenotype data is promising; translation to human serum uric acid / flare reduction is unknown. See [carnosine.md Open questions](./carnosine.md).
- **Any engineered-yeast carnosine titer used as a comparator needs primary-source confirmation.** Do not use the uncited internal baseline for a koji target or dose conversion. See [carnosine.md Open questions](./carnosine.md), [engineered-koji-protocol.md §15](./engineered-koji-protocol.md).
- **Koji carnosine co-expression feasibility.** No published carnosine-in-koji data; target is mechanistic extrapolation. See [engineered-koji-protocol.md §15](./engineered-koji-protocol.md), [validation-experiments.md §1.24](./validation-experiments.md).
- **Serum carnosinase (CN1) half-life limits.** Whether rapid cleavage caps peak systemic exposure below effective NLRP3-suppression concentration in humans is unresolved. Carnosinase-resistant analogs (D-carnosine, N-acetyl-carnosine) not yet gout-tested. See [carnosine.md Open questions](./carnosine.md).
- **Carnosine + uricase co-delivery: additive, synergistic, or flat?** Complementary mechanisms (renal URAT1/GLUT9 vs. luminal urate degradation). See [carnosine.md Open questions](./carnosine.md).
- **Androgen + carnosine combined experiment not yet run.** See the compact [Research Conjecture and discriminating observation](./carnosine.md#research-conjecture-carnosine-may-counter-an-androgen-associated-renal-urate-phenotype).

### Zileuton

- **Does zileuton (5-LOX inhibitor) abort or shorten gout flares in any case series or retrospective data?** Asthma patients who also have gout are a natural population to query.
- **What's the theory of action beyond 5-LOX?** Any secondary effects (redox, cytokine-modulation, neutrophil-direct) that could be advantageous or detrimental in gout context? Dossier in progress.

### Tier-4 inhibitor screen — missed gout-model data *(largely closed 2026-04-23 + 2026-05-05; one residual gap)*

- Do any other Tier-4 compounds (limonene, alpha-pinene, sulforaphane, omega-3 metabolites, EGCG/curcumin variants) have published MSU/gout animal-model data that the keyword-gated original screen missed? A 2021 MSU rat paper supports β-caryophyllene above the no-gout-evidence tier.
- **Current classification:** EGCG → Tier 2; limonene → Tier 3 supplement / Tier 4 production; sulforaphane → Tier 2–3 supplement / Tier 4 production. Candidate review must check MSU animal models, hyperuricemia rat models, human-cell NLRP3 assays, and Nrf2/NF-κB sub-μM activity for every compound — not just those with "gout" in the title.
- **Current evidence classification:**
  - **Sulforaphane:** upgraded from Tier 2–3 to **Tier 2** with two additional citations — Yang 2018 *Rheumatology* PMID 29340626 (oral SFN attenuated MSU foot-pad and air-pouch acute gout in mice) and Greaney 2015 *J Leukoc Biol* PMID 26269198 (Nrf2-independent inflammasome inhibition + in vivo gout peritonitis). Three independent in vivo gout-relevant readouts now cited.
  - **Theaflavins:** Tier 2 supplement candidate (see [theaflavins.md](./theaflavins.md)). Direct MSU peritonitis Animal Model + multi-transporter URAT1/GLUT9/OAT modulation distinct from EGCG.
  - **α-Pinene:** confirmed no direct MSU/gout animal-model data exists; Tier 4 ranking stands.
  - **d-Limonene:** Venkatesan 2025 already cited (PMID 41515190); no further re-rank.
  - **Omega-3 metabolites (RvD1, MaR1, etc.):** already cited in [`spm-resolution-pathway.md`](./spm-resolution-pathway.md); no new data.
- **Residual gap:** **Curcumin variants** (tetrahydrocurcumin, BCM-95 formulation, curcumin analogs) returned 11 PubMed hits on the 2026-05-05 audit; none qualified as direct MSU/gout animal-model evidence beyond what's already in the curcumin coverage. A targeted full-text-grep audit specifically for curcumin **derivative** activity in MSU-gout would close this last sub-question. Likely low-yield.

See [nlrp3-inhibitor-screen.md §Meta-Finding](./nlrp3-inhibitor-screen.md), [theaflavins.md](./theaflavins.md).
- **Would THCV's 20× higher CB2 affinity (Ki 7.5 nM vs. BCP 155 nM) translate to better MSU gout efficacy if dose-bridged?** Untested. THCV has cannabis-derived regulatory friction so this is academic unless BCP underperforms in a planned MSU macrophage assay. See [cannabinoids-terpenes.md](./cannabinoids-terpenes.md).
- **Is there an engineered microbial route to β-caryophyllene that scales past 10–50 mg/L?** Current titers are two orders of magnitude below the likely therapeutic dose (rat 100–400 mg/kg ≈ 1.1–4.5 g/day BSA-scaled). Titer improvement is required before "engineered koji produces BCP" enters the koji-track design. See [cannabinoids-terpenes.md](./cannabinoids-terpenes.md).

### Beta-caryophyllene

- **Does oral BCP at 50-200 mg/day (supplement range) reproduce the 100-400 mg/kg rat MSU effect?** PK scaling suggests possible 20-50× dose gap. Resolvable with desk work before wet-lab. See [cannabinoids-terpenes.md](./cannabinoids-terpenes.md).
- **Would THCV's 20× higher CB2 affinity (Ki 7.5 nM) translate to better MSU gout efficacy?** Untested; regulatory friction makes it academic unless BCP underperforms. See [cannabinoids-terpenes.md](./cannabinoids-terpenes.md).
- **Engineered microbial route to β-caryophyllene past 10-50 mg/L titer?** Two orders of magnitude below therapeutic dose. Titer improvement would unlock the "koji produces BCP" pathway. See [cannabinoids-terpenes.md](./cannabinoids-terpenes.md).

### Oridonin

- **Does oridonin's cellular-vs-kinetic IC50 split (5.18 μM human THP-1 per ChEMBL) matter for gout-specific efficacy?** No gout-specific studies exist for oridonin. Covalent Cys279 binding may be mechanistically preserved across species. See [oridonin.md](./oridonin.md).

### Other compounds (aggregated)

- **ChEMBL cross-check on remaining stack compounds** (BHB, KPV, ursolic acid, taurine, sulforaphane, berberine, resveratrol, curcumin, ergothioneine, ferulic acid, kojic acid): 2-5 more mechanistic reframings are expected when primary curated bioactivities are compared to the current wiki mechanism claims. See.

### Chaperone framework α-coefficient generalization — two-fold-class calibration vs. arbitrary novel-fold secreted disulfide-rich payloads

- **Does the [chaperone-orthogonal-stacking.md](./chaperone-orthogonal-stacking.md) framework's α-coefficient calibration generalize beyond the two fold classes covered by the §3.5.4 calibration set (lactoferrin transferrin-lobe + DAF SCR1-4 CCP/SCR)?** The framework derives α coefficients from non-koji in vitro folding kinetics and structural-rigidity arguments (Notari 2023; Schmidt 2010); §1.9 + §1.25 will validate the two specific fold classes empirically, but a successful calibration does NOT generalize the framework to future secreted disulfide-rich payloads with different fold architectures — e.g., C1-INH serpin (the parallel CP0 candidate flagged in comp-018 Phase 2), recombinant antibody-derived constructs, or other novel-fold secreted enzymes. cytosolic-payload novel folds (complestatin NRPS modules, cytosolic biosynthesis pathways) are NOT affected — the α framework only covers ER-pathway PDI-load competition, so cytosolic payloads sidestep the question entirely.
- **Two resolution paths:**
  1. **Calibration-set breadth expansion** — add a third / fourth fold class to the §3.5.4 calibration set (cost: ~$3–5K + 8 weeks wet-lab per additional fold class). Linear scaling; each new fold class validates its α independently.
  2. **Direct PDI-residence-time assay in *A. oryzae* microsomes** — multi-year tool-build that would generalize across fold classes simultaneously. No published *A. oryzae*-specific PDI kcat data exists for any fold class as of 2026-05-06. Tool-build cost not yet scoped.
- **Fires when:** OE wants to commit a new secreted disulfide-rich payload to a cassette design (e.g., C1-INH for the parallel CP0 track, an antibody-derived construct, or any future ER-routed cassette) and the framework's α prediction is the load-bearing decision input. Cytosolic payloads (cordycepin / carnS / panD / native ergothioneine biosynthesis) bypass this question entirely per the [koji-endgame-strain.md §3 third-cassette slot design rule](./koji-endgame-strain.md). Until then, dormant.
- **Cross-references:** [`chaperone-orthogonal-stacking.md` §8 item 6 "Generalization caveat"](./chaperone-orthogonal-stacking.md); [`chaperone-orthogonal-stacking.md` §3.5.4](./chaperone-orthogonal-stacking.md) (the two-fold-class calibration set definition); [`validation-experiments.md` §1.9](./validation-experiments.md) + §1.25 (the calibration arms themselves); [H05 — DAF SCR1-4 CP0 thesis](./hypotheses/H05-daf-scr14-cp0-thesis.md) (uses the framework as load-bearing).

### Quantification methodology — Tier 2 inter-operator reproducibility

- **Can the [quantification-ladder.md](./quantification-ladder.md) Tier 2 assays meet a product-specific tracking specification when run by trained operators at more than one controlled site after a shared Tier 3 calibration?** The framework is specified; no multi-operator reproducibility data exists. Applies to:
  - **Ergothioneine** ([SOP-6](./medicinal-mushroom-extract-sops.md) Ellman's reagent / DTNB) — well-anchored chemistry but multi-operator data lacking
  - **GLPP** ([SOP-6](./medicinal-mushroom-extract-sops.md) phenol-sulfuric) — same
  - **Cordycepin** ([SOP-6](./medicinal-mushroom-extract-sops.md) diazo-coupling, Speculative) — the *method validity* question is the upstream gate; tracked at [`validation-experiments.md` §1.28](./validation-experiments.md). The *inter-operator reproducibility* question fires only after §1.28 returns GREEN.
  - **Uricase activity** ([enzyme-quantification-protocol.md](./enzyme-quantification-protocol.md), 293 nm UV absorbance) — same multi-operator gap
- **Fires when:** a Tier 2 assay becomes a release or stability measurement at multiple sites. The prerequisite for [H09](./hypotheses/H09-community-fermentation-reliability.md) is to separate producer variation from assay-runner variation. Resolution work is a blinded round-robin using one calibrated reference batch; the site count, tolerance, and replication follow the assay and intended release decision rather than an inherited universal threshold.
- **Cross-references:** [H06](./hypotheses/H06-medicinal-mushroom-complement-track.md), [H09](./hypotheses/H09-community-fermentation-reliability.md), [`quantification-ladder.md`](./quantification-ladder.md), [`medicinal-mushroom-extract-sops.md`](./medicinal-mushroom-extract-sops.md) SOP-6, and [`enzyme-quantification-protocol.md`](./enzyme-quantification-protocol.md).

---

## Cross-cutting mechanisms and translation

Questions about shared biological assumptions, interaction risks, delivery constraints, regulatory classification, and the cheapest experiment that can change a verdict.

### Cross-route combination — repurposed drug × luminal urate intervention

The proposed arms target different chokepoints, but route separation does not establish additivity. The research question is whether each arm passes independently and whether the combination improves a prespecified outcome without a drug–microbe, exposure, or safety penalty.

- **Repurposed-drug candidate** — may target CP6a (5-LOX) or CP6b (GSDMD); see [`compounding-pharmacy-track.md`](./compounding-pharmacy-track.md) §"Combined / hybrid candidates."
- **Luminal UOX research configuration** — may target CP0 only after the configuration-specific activity and safety chain; see [`gut-lumen-sink.md`](./gut-lumen-sink.md).

Different mechanisms and routes make an interaction study conceivable, not additive by default. No co-administration evidence exists:

- Does the luminal configuration alter drug absorption, metabolism, microbiota, or exposure?
- What endpoints + biomarkers would actually let us measure layered effect vs. either track alone?
- What toxicology, PK, and interaction controls are required for the exact pair?

**Combination gate:** do not design an interaction study until both exact arms independently pass their biological, exposure, and safety gates. [comp-027](./computational-experiments.md) is a computational prior, not a prescription pathway.

**Cross-references:** [`compounding-pharmacy-track.md`](./compounding-pharmacy-track.md) §"Combined / hybrid candidates", [`koji-endgame-strain.md`](./koji-endgame-strain.md), [`comp-027`](./computational-experiments.md) (disulfiram dose modeling).

### Koji-track risk — can a qualified engineered-koji configuration be produced reproducibly at controlled sites?

[H09](./hypotheses/H09-community-fermentation-reliability.md) attacks one optional production model within the koji track. It starts only after a viable single-site configuration exists. The exact process must establish construct retention, activity, contamination detection, preservation, assay fitness, and release criteria before any multi-site comparison.

Industrial koji standardization is a process precedent, not evidence for distributed production of an engineered therapeutic configuration. A blinded comparison across trained operators or licensed facilities may be useful after single-site qualification; the number of sites and pass/fail limits must be justified by the actual product and assay. Failure redirects production to a more controlled model and does not invalidate the payload, gout weakness, or other tracks.

**Cross-references:** [H09](./hypotheses/H09-community-fermentation-reliability.md), [open-source-platform](./etc/open-source-platform.md), [engineered-koji-protocol](./engineered-koji-protocol.md), and [`operations/ward-1995-lab-access.md`](../operations/ward-1995-lab-access.md).

### Shared mechanism risk — does the gut-lumen uricase sink produce a clinically meaningful SUA reduction in typical (non-CKD) gout?

**Falsification card:** [H08 — Gut-Lumen Sink Mechanism](./hypotheses/H08-gut-lumen-sink-platform-thesis.md).

Several oral enzyme tracks depend on the gut-lumen sink producing a clinically meaningful SUA reduction in typical gout. The project as a whole does not. [COMP-019's unconditional flat-dose classification is not robust to COMP-044's tested substrate-occupancy and finite-window diagnostics](./gut-lumen-uricase-physiologic-regime-computational.md). COMP-044 supplies no replacement dose, serum effect, genotype ordering, physiological regime, efficacy model, topology or chassis selection, production-sufficiency, or safety conclusion. The biological and clinical-translation links are both open at the quantitative level:

- **ALLN-346 Study 201** ([NCT04987242](https://clinicaltrials.gov/study/NCT04987242)) completed with an actual registry enrollment of 16, but its Phase 2a abstract reports only the first 11 adults with hyperuricemia and normal renal function through stage 2 CKD. It reports a statistically significant mean serum-urate reduction versus placebo during seven days of treatment ([Terkeltaub et al. 2022](https://doi.org/10.1136/annrheumdis-2022-eular.1662)). **Study 202** ([NCT04987294](https://clinicaltrials.gov/study/NCT04987294)) enrolled 19 adults with hyperuricemia, gout, and stage 2 or 3 CKD, then terminated for company financing; ClinicalTrials.gov has no posted results. **Clinical Trial; conference-abstract and registry evidence.**
- The comp-019 search found no ABCG2 Q141K-stratified uricase clinical outcome in its searched sources as of 2026-05-08. This bounded result does not establish that the broader or later literature is empty.
- COMP-019's quantitative outputs are not decision-usable because its implementation omitted load-bearing physiological variables. COMP-044 is a regime audit, not a replacement efficacy model.

**If no tested configuration produces reproducible luminal urate disposal at the physiological substrate prior without redox injury**, the oral UOX mechanism track is killed before a human serum-effect threshold is assigned.

**Next evidence:**

- Search for later oral or gut-targeted UOX readouts and any genotype-stratified results.
- Determine whether ALLN-346 cohort-level genotype data can be accessed from public records or the sponsor.
- Complete §§1.33 and 1.36 with precommitted failure criteria before animal-dose design.
- If preclinical evidence supports translation, use an appropriately manufactured product and an ethics/regulatory-reviewed human study with serum urate, FEUA, safety, exposure, and attribution controls. No engineered-UOX n=1 self-experiment follows from the current evidence.

**Cross-references:** [cross-validation.md §Claim 1](./cross-validation.md) (feasibility 5.5/10), [gut-lumen-sink.md](./gut-lumen-sink.md), [uricase.md](./uricase.md), [comp-044](./gut-lumen-uricase-physiologic-regime-computational.md).

### Dietary-CP0 track risk — do dietary doses of rosmarinic acid, luteolin, Houttuynia, and Helicteres reach gut-luminal complement-suppressing concentrations?

The dietary-CP0 hypothesis requires an intact candidate to reach the relevant luminal compartment at sufficient free exposure and suppress complement without a countervailing effect. Existing rosmarinic-acid estimates are calculated rather than direct luminal measurements; plasma exposure does not substitute for the proposed luminal mechanism. Luteolin, *Houttuynia* polysaccharide, and *Helicteres* lignan exposure at the target compartment also remains unresolved.

**Discriminating evidence:**

- Measure segmental intestinal concentration and chemical identity after a controlled exposure in an appropriate animal model before any human translation.
- Pair concentration with ex-vivo complement activity and tissue-safety readouts; neither measurement alone establishes the mechanism.
- Keep the §1.30 Houttuynia macrophage screen separate: it can test a cell response but not dietary exposure, complement suppression, or product equivalence.
- Do not design a combination until each component has its own exposure, activity, and safety evidence and the interaction null is prespecified.

See [combined CP0 systems model](./combined-cp0-systems-model-computational.md), [CFH mechanism dissociation](./cfh-mechanism-dissociation-cp0-candidates-computational.md), [complement C5a in gout](./complement-c5a-gout.md), and [validation §1.30](./validation-experiments.md#130-houttuynia-cordata-polysaccharide-fraction-comparison-in-msu-stimulated-thp-1-macrophages--prioritization-screen).

### Matrix-specific assay gap for microbiome-derived metabolites

Microbiome-metabolite measurement is matrix- and analyte-specific. A method validated for bacterial culture supernatant does not automatically transfer to stool, plasma, intestinal tissue, or another metabolite. Analytical access also does not establish delivered dose, epithelial exposure, target-tissue concentration, target engagement, safety, or efficacy.

For butyrate, two research candidates have primary-source support:

- **Culture supernatant:** De Baere et al. validated underivatized HPLC-UV against bacterial culture supernatant over 0.5–50 mM, with a 0.5–1.0 mM LOQ ([PMID 23542733](https://doi.org/10.1016/j.jpba.2013.02.032)).
- **Stool:** Gu et al. reported an electrochemical/ANN platform compared with GC-MS in an independent fecal cohort; the method still requires local hardware qualification and independent external replication before Open Enzyme use ([PMID 42041444](https://doi.org/10.3390/bios16040223)).

These methods can support controlled research QC in their validated matrices. They do not verify a therapeutic exposure or a Q141K rescue. A butyrate experiment must separately measure exposure, ABCG2 surface trafficking, and functional urate flux. Secondary bile acids, microbial indoles, TMAO, and other metabolite classes each require their own validated method.

**Next gate:** run matrix-matched spike/recovery and a multi-operator comparison against the appropriate Tier 3 reference, using prespecified calibration, precision, and acceptance rules. See [`validation-experiments.md` §1.31](./validation-experiments.md), [`quantification-ladder.md`](./quantification-ladder.md), and [comp-038](./tier-2-butyrate-assay-audit-computational.md).

### Genotype stratification — Q141K and the gut-lumen-sink responder hypothesis

- **Does ABCG2 Q141K change substrate delivery or systemic response for an exact luminal-UOX configuration?** The direction and magnitude are unresolved. Comp-019 did not find genotype-stratified uricase clinical outcomes in its searched sources. COMP-019's unconditional flat-dose classification is not robust to COMP-044's tested substrate-occupancy and finite-window diagnostics; no demographic or responder claim follows.
  - **Path 1 — comp-019/044:** comp-019's 2026-05-08 search identified no genotype-stratified uricase clinical outcome in its searched sources. Its quantitative outputs are not decision-usable, and comp-044 supplies no replacement genotype-response model. Quantitative responder prediction remains open.
  - **Path 2 — §1.33 physiological factorial:** polarized intestinal transport with topology, urate, oxygen, peroxide, survival, and Q141K/WT stratification. This replaces the comp-019-gated single transwell concept.
  - **Path 3 — Overseen genotype-stratified human study, only after the preclinical gates.** A future protocol would require an appropriately manufactured product, regulatory and ethics review, prespecified genotype strata, safety monitoring, and adequate power. Self-administration of shio-koji or engineered koji is not an evidence path.
  - **Path 4 — Existing trial-data partnership.** Seek appropriately consented genotype-linked data from completed uricase studies if available. This is not load-bearing unless a data holder confirms the relevant exposure and outcome fields.
  - **Cross-references:** [comp-017 (intestinal ABCG2 sex-dimorphism)](./intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md), [comp-016 (T × intestinal ABCG2 evidence mining)](./t-abcg2-suppression-evidence-mining-computational.md), [cross-validation.md](./cross-validation.md) (gut-lumen uricase mechanism currently rated 6/10), [gut-lumen-sink.md](./gut-lumen-sink.md), [abcg2-modulators.md](./abcg2-modulators.md), and [personal-genome-protocol.md](./personal-genome-protocol.md).

### Platform selection and thesis

- **Is Open Enzyme's wiki-wide IC50 provenance practice rigorous enough?** Many IC50 values come from review papers, not primary ChEMBL-indexed assays. A written standard would prevent legacy-citation drift. See.
- **Does MCC950 / CRID3 / CP-456773 absence from ChEMBL name search reflect a curation gap or a synonym issue?** Worth a direct structure-based query. See.
- **Is there a "ChEMBL blind spot" for natural products?** ChEMBL's curation bias favors medicinal chemistry literature; natural products with strong functional but weak binding data (BCP, BHB, many terpenes) may be systematically underrepresented. See.

### Novel modalities (from modality-chokepoint-matrix.md)

The [Modality × Target Matrix](./modality-chokepoint-matrix.md) (2026-04-28) surfaces ten high-leverage exploration vectors not currently in the OE wiki. The highest-priority open questions per the matrix:

- **siRNA against URAT1 mRNA via kidney-tropic conjugate.** Sequence-specific renal-reabsorption knockdown; cleaner off-target profile than benzbromarone-class uricosurics. Adjacent to inclisiran-style GalNAc conjugate precedent. Zero clinical programs for gout. (Mechanistic Extrapolation; source: modality-chokepoint-matrix.md)
- **Engineered Faecalibacterium prausnitzii for local butyrate at the gut crypt.** Butyrate-mediated PPARγ induction of wild-type ABCG2 is the supported route. Direct Q141K trafficking rescue is proposed but unvalidated; durable colonization, titer, and epithelial exposure are also open. (Mechanistic Extrapolation; source: modality-chokepoint-matrix.md)
- **Myeloid-tropic LNP delivering NLRP3-silencing mRNA/siRNA to vessel-wall macrophages.** Myeloid LNP work in oncology supplies a delivery-class precedent; gout and vessel-wall translation remain untested. **Mechanistic Extrapolation**; source: modality-chokepoint-matrix.md.
- **Pharmacological chaperone for ABCG2 Q141K folding rescue.** CFTR correctors provide a protein-trafficking precedent within the ATP-binding-cassette superfamily, not evidence of transfer to ABCG2. Basseville 2012 (PMID 22472121) supports the rescue-pathway question; direct surface-expression and urate-flux assays remain required. **In Vitro**; source: modality-chokepoint-matrix.md, abcg2-modulators.md.
- **mRNA-IL-1RA pulse therapy for acute flare termination.** Transient expression matches flare window. Zero programs; mechanistically defensible; competes with canakinumab on cost. (Mechanistic Extrapolation; source: modality-chokepoint-matrix.md)
- **Wearable sweat-based or microneedle continuous UA monitoring.** Changes intervention-titration kinetics. UCSD/Stanford research-stage. (Mechanistic Extrapolation; source: modality-chokepoint-matrix.md)

### GSDMD pore self-delivery — does the PepT1 transporter actually show up on macrophages inside the joint?

The [GSDMD pore self-delivery paradox](./gsdmd-pore-delivery-paradox.md) proposes that membrane-impermeant payloads self-concentrate in pyroptotic synovial macrophages during a flare. comp-042 ([`kpv-gsdmd-pore-influx-computational.md`](./kpv-gsdmd-pore-influx-computational.md)) showed the mechanism's *selectivity* hinges on one uncharacterized datum: **do synovial-joint macrophages — resting and MSU-activated — express functional PepT1 (SLC15A1)?** For any PepT1-substrate payload (e.g. KPV), if the answer is yes, the payload enters healthy cells too via a concentrative electrogenic route that can make healthy cells accumulate *more* than pyroptotic ones — collapsing the pore's selectivity (and, if PepT1 is *absent*, reviving KPV as a viable selective payload). Functional PepT1 is demonstrated in immune cells generally ([Dalmasso 2008, PMID 18061177](https://doi.org/10.1053/j.gastro.2007.10.026)) and in inflamed-tissue macrophages ([Viennois 2016, PMID 27458604](https://doi.org/10.1016/j.jcmgh.2016.01.006)), but never quantified in synovial macrophages. Resolvable by immunostaining / qPCR / functional [³H]Gly-Sar uptake on synovial-macrophage samples. Gates the pore-delivery modality; note the [§1.32](./validation-experiments.md) selectivity probe sidesteps it by using a transporter-orphan tracer, so this datum is specifically what would decide whether a *PepT1-substrate* payload could ever be pore-selective. (Named gap; source: comp-042.)

### Engineered LBP chassis (independent gout-exploit track)

The [Engineered LBP Chassis](./engineered-lbp-chassis.md) treats engineered obligate anaerobes (*Faecalibacterium prausnitzii* primary, *Akkermansia muciniphila*, *Bacteroides*) as a peer track to the koji chassis. Six discrete in silico follow-ups are queued — none requires pharma-partner involvement to start:

- **P2-1 — Lit scan: *F. prausnitzii* engineering state-of-the-art.** Genetic-toolkit maturity, measured heterologous-payload activity, stability, containment, and safety gaps.
- **P2-2 — Lit scan: commercial / clinical engineered-LBP landscape.** Synlogic, Vedanta, NextBiotix, Seres, Pendulum — programs, partnership / licensing profile. (Queued, Opus subagent.)
- **P2-3 — Lit scan: FDA LBP regulatory path.** 2018 guidance, Vowst precedent, IND-enabling package, timeline + capital. (Queued, Opus subagent.)
- **P2-4 — comp-008: *F. prausnitzii* heterologous expression feasibility.** Tracked in [`computational-experiments.md` Planned Analyses](./computational-experiments.md). (Queued, Sonnet subagent.)
- **P2-5 — Falsification card H02.** Stub: [`hypotheses/H02-engineered-lbp-thesis.md`](./hypotheses/H02-engineered-lbp-thesis.md); full population queued.
- **P2-6 — Comparative chassis matrix for gout indication.** *F. prausnitzii* vs. *Akkermansia* vs. *Bacteroides* vs. engineered *E. coli* Nissle — payload tractability, niche fit, engineering complexity.

When the Phase 2 evidence lands, make a track decision: keep, narrow, or close the LBP route. The project mission is already modality-agnostic.

### Purine-Degrading Bacteria (PDB) — gut as independent urate disposal organ

See [purine-degrading bacteria](./purine-degrading-bacteria.md). The 2,8-dioxopurine pathway (Liu et al. 2023 Cell + 2025 Nat Microbiol) establishes ~15–25% of gut bacteria as a functionally distinct urate disposal system that evolved to compensate for hominid uricase loss. Engineered EcN with the full gene cluster (CBT2.0) achieved −63% plasma UA in hyperuricemic mice. Five priority follow-up threads:

**PDB-Q1 — Quantitative SUA reduction from PDB restoration in humans with intact renal function.** The FARMM study (n=30) had no statistical power to detect serum urate changes, and subjects had normal kidneys. What is the mg/dL effect in a typical gout patient? This number gates whether PDB restoration is "adjunctive to pharmacotherapy" or "potentially standalone." Required before designing any PDB clinical trial. No lit scan will resolve this — it requires a prospective study. Frame as a priority gap, not a computation. *(Human RCT or n-of-1 cohort; no current data)*

**PDB-Q2 — Does PDB-derived butyrate at physiological gut concentrations activate ABCG2 via PPARγ?** The butyrate → PPARγ → ABCG2 mechanism is established at pharmacological doses and for dietary fiber effects (DASH RCT, Li 2023 PMID 36948133). Whether native PDB flux generates enough luminal butyrate to meaningfully activate this axis is unresolved. This is a tractable Caco-2 experiment: measure ABCG2 expression in enterocyte monolayers at the butyrate concentrations achievable via gut PDB fermentation vs. pharmacological sodium butyrate doses. **Estimated cost: $2,000–5,000 if a wet-lab partner has Caco-2 capability.** *(In Vitro; immediately testable)*

**PDB-Q3 — Does selenium availability limit gut PDB activity in humans?** See the compact [Research Conjecture and paired abundance-versus-flux test](./purine-degrading-bacteria.md#research-conjecture-selenium-availability-may-gate-microbial-urate-disposal).

**PDB-Q4 — Can yanthine (2,8-dioxopurine) be measured reproducibly in a clinically accessible matrix?** The reported case-control difference makes yanthine a candidate pathway biomarker, not a validated measure of individual PDB function. Identify a validated assay, matrix, stability window, reference range, and relation to metagenomic pathway abundance before using it for stratification. **Human biomarker candidate.**

**PDB-Q5 — Which UOX/PDB topology, if any, earns testing?** CBT2.0 shows that EcN can carry a reductive urate-degradation cluster, while PULSE provides an EcN uricase precedent. That does not establish that the pathways are independent, additive, co-localizable, or SCFA-coupled. [comp-031](./dual-chassis-ecn-pdb-uricase-computational.md) is unusable for current decisions because it inherits an unsupported flat UOX regime, assigns unmeasured butyrate production to engineered EcN, and mixes compartments. COMP-044 establishes only that the legacy unconditional flat-dose classification is not robust to the tested substrate-occupancy and finite-window diagnostics. Compare one strain, separate strains, and temporal staging only after validation §§1.33, 1.34, and 1.37 resolve physiological UOX activity, CBT2.0 carbon fate, and spatial residual flux. *(Mechanistic Extrapolation + Animal Model precedents; topology open)*

See [engineered-lbp-chassis.md](./engineered-lbp-chassis.md) (LBP chassis peer track), [gut-lumen-sink.md](./gut-lumen-sink.md) (PULSE/uricase context), [abcg2-modulators.md](./abcg2-modulators.md) (butyrate/PPARγ + *A. indistinctus*/hippuric acid axes).

### TCM × Modern Rigor — discovery-engine output (fourth peer-track exploration vector)

The [TCM × Modern Rigor track](./tcm-modern-rigor-intersection.md) treats traditional Chinese medicine materia medica as a **discovery-engine output** — applying a six-rule methodology lens (chokepoint mapping, ChEMBL cross-check, bioavailability-honest framing, formula decomposition, standardized-extract specification, falsification-card discipline) to TCM compounds with documented gout/hyperuricemia indications. Sister to the [LBP chassis](./engineered-lbp-chassis.md) and [siRNA/URAT1](./sirna-urat1-modality.md) peer tracks. Six in silico Phase 2 follow-ups queued — none requires pharma-partner involvement to start:

- **P2-1 — Lit scan: classical TCM gout formulas + modern Chinese clinical evidence.** Si Miao San family, Bai Hu Jia Gui Zhi Tang, Smilax-enhanced variations. **Global multilingual sources by default** — ChiCTR registry, CNKI/WanFang (Chinese-language papers, read in original), J-STAGE (Japanese Kampo medicine literature), PubMed (English cross-check only). Output: evidence-tier-tagged summary of which formulas have credible clinical signal vs. tradition-only. (Queued, Opus subagent.)
- **P2-2 — comp-011: ChEMBL cross-check of the 8 candidate TCM gout compounds.** Same framework as comp-004 (supplement ABCG2 antagonism). Inputs: Smilax glabra, Rheum officinale, Plantago asiatica, Phellodendron amurense, Polygonum cuspidatum, Cinnamomum cassia, Atractylodes macrocephala, Astragalus membranaceus. Targets: NLRP3, ABCG2, URAT1, GLUT9, XO, NF-κB pathway. Output: per-compound mechanism + curated bioactivity + chokepoint hit map + IC50 vs. achievable gut-luminal concentration. (Queued, Sonnet subagent.)
- **P2-3 — Lit scan: Smilax glabra (Tu Fu Ling 土茯苓) deep-dive.** Highest-leverage single compound — explicit primary gout herb in classical TCM with substantial modern Chinese clinical literature. XO inhibition kinetics, uricosuric mechanism, standardization issues, drug interactions, adverse effects. (Queued, Opus subagent.)
- **P2-4 — Lit scan: Si Miao San multi-component coverage analysis.** Decompose the four-herb formula (Phellodendron, Atractylodes, Achyranthes, Coix) per "formula decomposition" discipline. Map each component to chokepoints. Identify designed-coverage vs. redundant vs. synergistic design. (Queued, Opus subagent.)
- **P2-5 — Falsification card H04: TCM × rigor methodology lens.** Stub: [`hypotheses/H04-tcm-rigor-intersection.md`](./hypotheses/H04-tcm-rigor-intersection.md); full population queued.
- **P2-6 — Bioavailability characterization for top 3 compounds advancing from P2-2.** Quantitative oral bioavailability + gut-vs-systemic distribution + first-pass metabolism + microbiome metabolism. Maps to the "embrace gut-luminal mechanisms" discipline (rule #3). (Queued, Opus subagent.)

Phase 3 reflection (content-triggered, not calendar-triggered): does the TCM-rigor track accumulate enough substance to elevate from "methodology lens" to "first-class discovery-engine output named in `open-enzyme-vision.md` §2.2 alongside the repurposing-surface candidates"? Trigger: after P2-1 through P2-6 land.

### Medicinal mushroom complement — Phase 7 peer track (cultivation, not engineering)

The [Medicinal Mushroom Complement Track](./medicinal-mushroom-complement-track.md) evaluates characterized native materials as an independent portfolio track. Cultivation does not establish composition, exposure, efficacy, safety, product equivalence, or regulatory status.

- **#1 Strain selection lit scan ✅** (multilingual, 2026-05-06; outputs: Ganoderma / Cordyceps / Pleurotus per-species scan files in comp-014 outputs dir)
- **#2 Cultivation × yield meta-analysis ✅** (2026-05-06)
- **#3 Extract characterization SOPs** — stub at [`medicinal-mushroom-extract-sops.md`](./medicinal-mushroom-extract-sops.md) (SOP-1 GLPP gated on Phase 5b CNKI dive; SOP-3 EGT lowest-friction)
- **#4 GLPP+cordycepin synergy wet-lab gate** — stub at [`validation-experiments.md` §2.6](./validation-experiments.md) (4-arm: whole-fermentate / cordycepin / cordycepin+GLPP / cordycepin+pentostatin)
- **#5 H06 hypothesis card ✅** (stub at [`hypotheses/H06-medicinal-mushroom-complement-track.md`](./hypotheses/H06-medicinal-mushroom-complement-track.md))
- **#6 Modality-chokepoint-matrix native-compound row ✅** (2026-05-06)
- **#7 Exposure grounding** — for each load-bearing compound, verify the material identity, measured exposure, route, and evidence tier in the primary study before using yield as a translational prior.

The medicinal-mushroom-complement track is already a first-class portfolio track. Its evidence and experiment results—not a future branding decision—determine whether it remains active.

### siRNA against URAT1 — discovery-engine output (peer-track exploration vector to LBP)

The [siRNA / URAT1 modality](./sirna-urat1-modality.md) treats kidney-tropic siRNA against URAT1 mRNA as a **discovery-engine output** — non-fermentable, non-microbial, positioned for partner / spinout development rather than in-house manufacture. Sister to the [LBP chassis](./engineered-lbp-chassis.md) under the broader chase-every-avenue framing. Six in silico Phase 2 follow-ups queued — none requires pharma-partner involvement to start:

- **P2-1 — Lit scan: kidney-tropic conjugate chemistry state-of-the-art.** Megalin-binding peptides, CDP nanoparticles, kidney-cortex-selective LNPs, aptamer-siRNA chimeras — design space, current best titers / pharmacokinetics, IP landscape. (Queued, Opus subagent.)
- **P2-2 — comp-009: URAT1 mRNA structural analysis for siRNA target site selection.** Tracked in [`computational-experiments.md` Planned Analyses](./computational-experiments.md). (Queued, Sonnet subagent.)
- **P2-3 — Lit scan: commercial / clinical landscape for kidney-tropic siRNA programs.** Alnylam, Arrowhead, Dicerna / Novo Nordisk, Sirnaomics — non-gout indications and what transfers; partnership / licensing profile. (Queued, Opus subagent.)
- **P2-4 — Comparative analysis: siRNA vs. small-molecule URAT1 inhibitors** (pozdeutinurad / AR882 efficacy, safety, cost, durability, hormone-axis-interaction). Honest competitive 5–10 year horizon assessment. (Queued.)
- **P2-5 — Falsification card H03.** Stub: [`hypotheses/H03-sirna-urat1-thesis.md`](./hypotheses/H03-sirna-urat1-thesis.md); full population queued.
- **P2-6 — Lit scan: FDA siRNA regulatory path.** Inclisiran / patisiran precedent, IND-enabling package, ballpark timeline + capital for a kidney-tropic siRNA BLA. (Queued, Opus subagent.)

The siRNA track is already evaluated as a first-class gout exploit track. It does not need to justify a future rebrand; it needs to survive its own falsification gates.

### Ward 1995 §1.9 — expression feasibility gate

Can independently qualified UOX-only and lactoferrin-only configurations retain active function when combined in solid-state *A. oryzae*? Build and characterize the exact single-payload configurations first, advance the UOX configuration through §1.33, then test the dual configuration against matched controls. Parent strain, sequence, topology, and host remain unranked until comparable data exist. See [H01](./hypotheses/H01-ward-dual-cassette.md) and [validation §1.9](./validation-experiments.md#19-ward-1995-dual-cassette-feasibility-test-koji-endgame-strain-gate).

### Distributed production and strain stability

- **Does the exact engineered configuration retain sequence, copy state, activity, and phenotype across its permitted propagation window?** Test this under controlled production; do not rely on a parent strain's food history or absence of an antibiotic marker as a safety argument.
- **Can trained operators or facilities meet the same justified release specification?** A blinded central assay can separate process variation from assay variation after single-site qualification.
- **What regulatory and containment model applies to the exact organism state and distribution path?** Resolve classification before distributing an engineered starter or product.

### Regulatory

- **How would the exact engineered-yeast configuration be regulated?** Classification depends on the construct, viable versus nonviable state, recovered payload, process, intended use, route, and claims. Parent-organism food-use history does not answer it. Resolve the scientific configuration first, then map the applicable food, LBP, biologic, containment, and release requirements. See [engineered yeast UOX plan](./engineered-yeast-uricase-proposal.md).
- **Can any lower-cost IL-1β-pathway intervention reproduce a clinically meaningful effect with acceptable exposure and safety?** Manufacturing route or parent-organism food history does not answer efficacy, regulatory status, or total cost.

### Microbiota and safety at scale

- **Does repeated exposure to an exact enzyme or NLRP3-intervention configuration select for specific commensals or cause dysbiosis?** Test composition, function, barrier effects, and persistence under a controlled preclinical protocol. See [cross-validation.md](./cross-validation.md).
- **Do any commensals express uricase natively?** If yes, does engineered uricase suppress or enhance them? See.
- **Which microbiome and barrier readouts should gate a living engineered-organism study?** Define configuration-specific preclinical stopping rules for community disruption, pathogen expansion, inflammation, barrier injury, persistence, shedding, and horizontal transfer before human translation.

### Combination therapy

- **Could any luminal UOX configuration add benefit on stable urate-lowering therapy?** Study 201's reported first 11 participants were not receiving concurrent urate-lowering therapy. A July 2022 sponsor release described a planned allopurinol-combination Cohort D for Study 202, contingent on data and financing, but Study 202 terminated for company financing and has no posted results ([NCT04987294](https://clinicaltrials.gov/study/NCT04987294)). Additivity, dose-sparing, and construct transfer remain untested. **Mechanistic Extrapolation.**

---

## Safety and experimental methodology

Questions about biomarker interpretation, stopping rules, microbiome impact, and the limits of n=1 inference.

### Biomarker design

- **Which biomarker panel distinguishes CP0, CP2, CP5b, and CP6a effects in a controlled study?** hs-CRP alone cannot attribute a result to a chokepoint. Prespecify mechanism-proximal readouts and controls for each tested node.
- **What's the optimal EPA:DHA ratio for gout-specific SPM production (RvD1/MaR1 vs. RvE1)?** Does it differ from the cardiovascular-optimized ratio? See [spm-resolution-pathway.md](./spm-resolution-pathway.md).

### Red-flag thresholds

- **What LFT elevation threshold triggers zileuton discontinuation?** Any future protocol must use current prescribing guidance and clinician oversight.
- **What biomarkers signal microbiome disruption vs. acceptable variation?** Alpha diversity drop threshold, specific pathobiont expansion (e.g., *Clostridium difficile*, *Enterococcus*), inflammatory markers (fecal calprotectin). See [cross-validation.md](./cross-validation.md).
- **Can BCP exposure in the rat MSU model be translated to a human-relevant concentration?** Simple dose scaling does not establish human exposure or safety. Resolve with PK modeling and measured target-tissue exposure before any human study. See [cannabinoids-terpenes.md](./cannabinoids-terpenes.md).

Every question must link to its evidence or experiment surface. Once resolved or falsified, update the linked evidence surface and remove the duplicate question; Git retains the history.
