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
- **Could a joint-retained multi-node flare intervention outperform a matched single-node local arm?** See the route-specific premises and discriminating comparison in the [gout kill-chain delivery analysis](./gout-kill-chain-delivery-routes.md#research-conjecture--local-multi-node-control-without-systemic-overreach).
- **Could abaloparatide's controlled urate rise be a human readout of PTH1R-driven ABCG2 surface loss?** See the controlled-trial premises, unsupported mechanism bridge, and direct trafficking/flux test in [ABCG2 modulators](./abcg2-modulators.md#research-conjecture-abaloparatide-pth1r-abcg2).
- **Could bempedoic acid expose an OAT2-sensitive renal urate-secretion phenotype?** See the controlled human perturbation, substrate-specific in-vitro premise, and knockout/rescue test in [gout pathophysiology](./gout-pathophysiology.md#research-conjecture-bempedoic-acid-oat2-urate-secretion).
- **Could renal water handling expose a compartment-specific urate phenotype?** See the controlled tolvaptan perturbation, collecting-duct GLUT9b/ABCG2 mechanism, and paired-data test in [gout pathophysiology](./gout-pathophysiology.md#research-conjecture-renal-water-urate-coupling).
- **Could aromatase inhibition reveal a hormone-sensitive urate phenotype?** See the human hormone-perturbation premise, absent direct urate endpoint, and prospective measurement test in the [androgen–urate axis](./androgen-urate-axis.md#research-conjecture-aromatase-inhibition-may-reveal-a-hormone-sensitive-urate-phenotype).

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
- **Can the Ward 1995 *A. awamori* glucoamylase-fusion + KEX-2 architecture (>2 g/L submerged) transfer to solid-state rice koji fermentation?** The submerged-culture precedent is material-, host-, and process-specific (PMID 9634791). Solid-state mass transfer, redox, and proteolysis dynamics are different. This is the gating experiment for that exact lactoferrin configuration, not evidence for its gout function or co-expression. See [engineered-koji protocol](./engineered-koji-protocol.md) and [lactoferrin](./lactoferrin.md).

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

- **How much does complement C5a contribute relative to TLR4/LPS, TNFSF14, and other priming inputs in clinical gout flares?** Cumpelik 2016 (PMID 26245757), Khameneh 2017 (PMID 28167912), and An 2014 (PMID 25229885) establish a C5a route in animal and human-cell systems; they do not establish comparative dominance across human flares. See [complement-c5a-gout.md](./complement-c5a-gout.md), [nlrp3-exploit-map.md](./nlrp3-exploit-map.md).
- **Can an exact natural product directly antagonize C5aR1?** The recorded database and literature queries did not retrieve a wet-lab-validated direct antagonist, but that bounded non-retrieval does not close the class. Revisit only with a meaningfully different multilingual or source-space query, or when a named material gains receptor-specific functional evidence. See [complement-c5a-gout.md](./complement-c5a-gout.md) and [validation experiment §1.21](./validation-experiments.md#121-natural-product-c5ar1-antagonist-screening--historical-computational-pass).
- **Are there patient subgroups where non-complement priming (true LPS from SIBO) dominates?** Would change stack selection per patient. See [complement-c5a-gout.md §6 Q5](./complement-c5a-gout.md).
- **Is TNFSF14/LIGHT elevation a universal feature of gout flares or a patient subtype?** Would a TNFSF14 biomarker identify responders to EGCG or CERC-002 better than generic hs-CRP? See [tnfsf14-gout-target.md](./tnfsf14-gout-target.md).
- **Does an exact lactoferrin material alter any MSU-relevant complement, priming, or resolution readout?** No direct gout experiment currently assigns lactoferrin to CP0, CP1, CP5b, or a multi-chokepoint role. Test one qualified material in one compartment with mechanism-proximal controls before asking whether it interacts with another node. See [lactoferrin](./lactoferrin.md) and [complement C5a](./complement-c5a-gout.md).

### Chokepoint biology

- **Could an exact, qualified intervention configuration reduce flares during ULT initiation?** This is a future clinical question, not a food-use or home-production claim. An engineered configuration would first need product-specific identity, exposure, safety, containment, and preclinical efficacy gates; any later trial would use established-care prophylaxis as the controlled background. **Mechanistic Extrapolation.**
- **CP1a × CP2/CP3 interaction in vitro.** First establish each exact material's single-agent MSU response and mechanism; only then use a prespecified interaction model. Pathway labels alone do not establish synergy.
- **Do exact RvD1 and MaR1 effects reproduce in one matched MSU system?** The named mediators have distinct mouse evidence. Compare identity, stability, exposure, pathway engagement, and inflammatory/resolution readouts without assuming a class effect.
- **Can an EPA- or DHA-precursor configuration generate a measured gout-relevant RvD1, MaR1, or other exact mediator exposure?** Precursor administration is a separate conversion experiment, not a substitute for the mediator.
- **Can exact SPM identity and exposure be measured reproducibly in the selected matrix?** Qualify recovery, isomer discrimination, oxidation, calibration, and stability before using a mediator value as a biological endpoint.
- **Could exact RvD1 or MaR1 couple aggNET behavior to reduced complement amplification?** See the explicitly bounded [Research Conjecture and discriminating experiment](./spm-resolution-pathway.md).

### Independent chokepoint research leads

- **Does ADA warrant formal addition as a gout chokepoint?** The
  purine-flux and adenosine-resolution directions must be measured together
  for an exact, independently sourced material. See
  [gout pathophysiology §ADA](./gout-pathophysiology.md).
- **Does PINK1/mitophagy warrant formal addition as a gout-inflammation
  chokepoint?** Test whether an exact, independently sourced material changes
  mitophagy and MSU-triggered NLRP3 function under matched exposure. See
  [gout pathophysiology §PINK1](./gout-pathophysiology.md).

### Upstream-complement sub-questions

[The retired non-evidential COMP-018 record](./upstream-complement-modulator-sweep-computational.md) supplies no empty-class verdict, tier, or cross-material rank. The former COMP-020 is [quarantined legacy literature provenance](./etc/experiments/comp-020-upstream-complement-verification-rerun/quarantine.json) and supplies source-level leads only. Candidate-specific evidence lives on the focused rosmarinic-acid/complement, Houttuynia, C1-INH, and related pages. These independent questions remain useful:

- **Are there compounds that *upregulate the host-side complement regulators* (Factor H, DAF/CD55, CD59, clusterin, CR1), and would that create a distinct CP0 intervention route?** This remains unanswered. Anchor any focused scan to expression datasets plus complement-functional assays; gene upregulation alone would not prove C3/C5 convertase suppression.
  - **Anchor compound classes worth checking:** plant-derived Nrf2 activators (sulforaphane, curcumin, EGCG), butyrate and other HDAC-directed materials, retinoids, and dietary polyphenols. This is a search set, not a ranked or validated intervention list. HDAC activity does not by itself establish ABCG2 derepression or complement-regulator induction; each candidate requires direct expression plus complement-functional testing.
  - **Cross-references:** [complement-c5a-gout.md](./complement-c5a-gout.md) (Factor H, DAF/CD55, CD59, clusterin biology), [comp-018](./upstream-complement-modulator-sweep-computational.md), [hypotheses/H05-daf-scr14-cp0-thesis.md](./hypotheses/H05-daf-scr14-cp0-thesis.md) (engineering-side DAF thread — engineered koji that *secretes* the DAF protein is a distinct mechanism from compounds that *upregulate endogenous DAF expression*).

- **Should upstream complement remain inside CP0 or become a separately named chokepoint?** Defer the naming decision until it changes experiment routing or portfolio ownership.

- **What is the quantitative relationship between dietary rosmarinic-acid intake and active compound concentrations at the relevant gut and joint/MSU interfaces?** The legacy literature inventory preserves non-interchangeable assay records; it does not supply a combined potency range. Human exposure papers do not close the dietary source → segmental gut concentration → plasma exposure → joint/MSU activity chain. COMP-029's invalid toy-model outputs do not narrow this question. **Resolution path:** measure intestinal and systemic/joint exposure as separate compartment hypotheses, then pair each with a concentration-matched functional assay. See [`complement-c5a-gout.md` §9.5](./complement-c5a-gout.md) and the [legacy literature inventory](./upstream-complement-verification-rerun-computational.md).

- **Can a matrix-specific Tier 2 assay reproduce a Tier 3 reference result across operators and batches?** Validate analytical reproducibility on controlled research material before linking any assay to genotype, exposure, or an intervention study. Prespecify identity, matrix, calibration range, spike/recovery, operator count, batch count, and an acceptance rule. Cheap or portable measurement is useful for research QC only; it does not establish a delivered human dose, target-tissue exposure, safety, or efficacy. See the [genotype-informed intervention research workflow](./genotype-informed-supplement-workflow.md) and [H09 — Community Fermentation Reliability](./hypotheses/H09-community-fermentation-reliability.md).

### Cross-system translation

- **How much of a potency difference is caused by species versus cell system, stimulus, assay format, or exposure?** The existing dapansutrile records change several variables at once, so their numerical ratio cannot answer that question. Run matched mouse and human macrophage assays with the same stimulus, endpoint, timing, and free exposure. See [NLRP3 inhibitor screen](./nlrp3-inhibitor-screen.md).
- **What is the right evidence yardstick for an NLRP3 pathway modulator?** Use mechanism-matched human-cell readouts—such as priming, ASC assembly, caspase-1, mature IL-1β, GSDMD, and viability—rather than treating database non-retrieval as a biological result.

### Biomarker interpretation

- **Is hs-CRP alone sufficient to distinguish chokepoint-specific effects in a controlled study?** No — hs-CRP is a downstream output marker. Chokepoint attribution requires prespecified, mechanism-proximal readouts and appropriate controls; candidate measures include LTB4 (CP6a), C5a (CP0), and TNFSF14 (CP1a).

---

### Chronic tophaceous gout — the adaptive-immune axis (scoped 2026-07-13; no-go for a dedicated track)

A bounded scoping scan tested whether the Th17/IL-17 (RORγt) adaptive-immune axis had enough direct driver evidence to justify a dedicated Open Enzyme track. It did not establish that priority.

- **Current evidence does not establish Th17/IL-17 as the tophus driver.** Single-cell and spatial transcriptomics of tophus tissue (PMID 41107120) reported regulatory-skewed intra-tophus CD4 T cells and an SPP1/MMP9 macrophage population associated with matrix remodeling and bone erosion. The bounded registry scan did not retrieve an IL-17-blocker gout trial, but that search observation is not universal absence.
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

- **Does quercetin's 300 nM primary 5-LOX IC50 (PMID 2066989) translate to cellular neutrophil-chemotaxis block in a gout-relevant assay?** A zileuton head-to-head could resolve this if the question becomes decision-relevant.
- **Is quercetin + Boswellia (AKBA) redundant at 5-LOX, or complementary at IKKβ + 5-LOX?** Depends on AKBA's 5-LOX IC50 and whether the two compounds bind at the same site. ChEMBL query pending. See.

### BHB / Ketones

- **Can an exact BHB exposure reproduce the urate-crystal pathway result without an adverse urate-handling shift?** The cited study used BHB or a ketogenic context in mouse NLRP3-disease models, including urate-crystal peritonitis; it does not establish a human formulation or regimen (PMID 25686106). Measure exact exposure, inflammasome target engagement, and urate handling together. See [BHB](./bhb-ketones.md).
- **How does BHB activity transfer across species and systems?** Compare matched mouse and human macrophage assays; the existing dapansutrile records do not define a reusable numerical species penalty.
- **Does androgen status shift BHB's NLRP3 concentration-response?** BHB has reported activity at multiple NLRP3 nodes ([bhb-ketones.md](./bhb-ketones.md)); direct androgen effects on NLRP3 priming remain directionally ambiguous ([androgen-urate-axis.md](./androgen-urate-axis.md) §"Beyond transporters"). Test androgen × MSU × BHB in a concentration matrix with HCAR2 expression, inflammasome readouts, and viability rather than inferring a human dose. See [validation §1.23](./validation-experiments.md) and [nlrp3-exploit-map.md](./nlrp3-exploit-map.md).

### Lactoferrin

- **Can lactoferrin be expressed as an intact, active product in solid-state *A. oryzae*?** The *A. awamori* >2 g/L precedent is submerged and single-protein. Solid-state output, processing, activity, and batch variance remain unmeasured; a useful exposure target must be derived separately. See [engineered-koji protocol](./engineered-koji-protocol.md) and [lactoferrin](./lactoferrin.md).
- **Does *A. oryzae* KEX-2 process a glucoamylase-lactoferrin fusion identically to *A. awamori*?** Critical for transferring the Ward 1995 architecture. See [engineered-koji-protocol.md §16 Risks](./engineered-koji-protocol.md).
- **Has an exact oral lactoferrin material been tested in gout?** Run a source-pinned multilingual literature and registry refresh before treating the current corpus gap as absence. See [lactoferrin](./lactoferrin.md).
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

### Natural-product NLRP3 evidence qualification

- **Which exact materials have reproducible MSU-relevant activity?** Reverify species, preparation, exposure, assay, and primary source for sulforaphane, theaflavins, limonene, β-caryophyllene, curcumin derivatives, and other leads. Preserve direct animal observations without turning the mixed set into a tier or rank.
- **Which candidates reproduce in a matched human macrophage assay?** Measure free exposure, priming, inflammasome assembly, mature IL-1β, GSDMD, and viability. Database coverage and production titer do not answer this biological question.
- **When does an engineered source become useful?** Only after an exact material clears biological and exposure gates; then compare existing and engineered sourcing on identity, purity, stability, achievable exposure, and cost.

### Beta-caryophyllene

- **What free exposure reproduces the exact rat MSU result in a human-cell system?** Simple body-surface-area scaling and comparison with a supplement label cannot establish an effective human exposure. See [cannabinoids and terpenes](./cannabinoids-terpenes.md).
- **Does CB2 dependence explain the MSU-model effect?** Use an exact BCP material, receptor blockade or knockout, exposure measurement, and matched inflammatory readouts before comparing another cannabinoid.
- **Could an engineered route meet a validated material specification?** Production work opens only after biological exposure and identity requirements are known.

### Oridonin

- **How do oridonin's cellular and biochemical measurements transfer to an MSU system?** Reverify the exact primary assays, then compare exposure and NLRP3/NEK7 readouts in a gout-relevant human-cell model. The current corpus does not establish gout efficacy. See [oridonin.md](./oridonin.md).

### Do encoded folding-route features predict cassette interactions?

- **Question:** Do payload pairs with greater ER folding-route overlap show larger per-payload losses in matched combined configurations? Current fold-class labels are qualitative hypotheses, not calibrated demand measurements.
- **Required comparison:** §§1.9 and 1.25 provide single-payload configuration baselines. Matched dual- and triple-cassette configurations must measure each payload's abundance, native fold, secretion, activity, host stress, and growth before cassette interaction can be tested.
- **Boundary:** One lactoferrin/DAF comparison cannot validate transferrin-lobe or CCP/SCR fold classes or generalize to C1-INH, antibodies, or another secreted payload. Each new configuration remains empirical.
- **Longer-term path:** Direct folding-demand and PDI-network measurements in *A. oryzae* could determine whether any transferable predictor is justified.
- **Cross-references:** [chaperone-orthogonal stacking](./chaperone-orthogonal-stacking.md), [validation §1.9](./validation-experiments.md), [validation §1.25](./validation-experiments.md), and [H05](./hypotheses/H05-daf-scr14-cp0-thesis.md).

### Quantification methodology — Tier 2 inter-operator reproducibility

- **Can the [quantification-ladder.md](./quantification-ladder.md) Tier 2 assays meet a product-specific tracking specification when run by trained operators at more than one controlled site after a shared Tier 3 calibration?** The framework is specified; no multi-operator reproducibility data exists. Applies to:
  - **Ergothioneine** ([SOP-6](./medicinal-mushroom-extract-sops.md)) — a generic thiol/color readout is only a candidate until matrix specificity and agreement with the exact HILIC-LC/MS anchor are demonstrated
  - **GLPP** ([SOP-6](./medicinal-mushroom-extract-sops.md)) — a total-polysaccharide readout may track a batch only after correlation with the exact SEC-MALS/composition-defined fraction is demonstrated
  - **Cordycepin** ([SOP-6](./medicinal-mushroom-extract-sops.md) diazo-coupling, Speculative) — the *method validity* question is the upstream gate; tracked at [`validation-experiments.md` §1.28](./validation-experiments.md). The *inter-operator reproducibility* question fires only after §1.28 returns GREEN.
  - **Uricase activity** ([enzyme-quantification-protocol.md](./enzyme-quantification-protocol.md), 293 nm UV absorbance) — same multi-operator gap
- **Fires when:** a Tier 2 assay becomes a release or stability measurement at multiple sites. The prerequisite for [H09](./hypotheses/H09-community-fermentation-reliability.md) is to separate producer variation from assay-runner variation. Resolution work is a blinded round-robin using one calibrated reference batch; the site count, tolerance, and replication follow the assay and intended release decision rather than an inherited universal threshold.
- **Cross-references:** [medicinal-fungal exact-material conjecture](./medicinal-mushroom-complement-track.md#research-conjecture--a-reproducible-medicinal-fungal-material-may-expose-a-gout-weakness), [H09](./hypotheses/H09-community-fermentation-reliability.md), [`quantification-ladder.md`](./quantification-ladder.md), [`medicinal-mushroom-extract-sops.md`](./medicinal-mushroom-extract-sops.md) SOP-6, and [`enzyme-quantification-protocol.md`](./enzyme-quantification-protocol.md).

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

**Cross-references:** [cross-validation.md](./cross-validation.md), [gut-lumen-sink.md](./gut-lumen-sink.md), [uricase.md](./uricase.md), [comp-044](./gut-lumen-uricase-physiologic-regime-computational.md).

### Oral complement-candidate route split — intestinal activity versus joint/MSU activity

These are two different hypotheses. An orally delivered candidate could alter complement-related biology within the intestine, or absorbed parent compound/metabolites could reach a systemic or joint/MSU interface. Evidence for one compartment does not establish the other, and no causal gut-to-joint bridge has been demonstrated for these candidates.

**Discriminating evidence:**

- For the intestinal hypothesis, measure segmental concentration, chemical identity, local complement readouts, and tissue safety after a controlled exposure.
- For the systemic/joint hypothesis, measure plasma and joint-relevant exposure plus MSU-associated complement activity under matched conditions.
- To connect them, require a causal observation showing that a defined intestinal perturbation changes a downstream joint/MSU readout through the proposed route.
- Keep the two Houttuynia assays separate: [§1.30](./validation-experiments.md#130-houttuynia-cordata-polysaccharide-fraction-comparison-in-msu-stimulated-thp-1-macrophages--prioritization-screen) tests direct macrophage directionality, while [COMP-040](./computational-experiments.md) independently tests serum complement. Neither establishes dietary exposure or product equivalence, and neither gates the other.
- Do not design a combination until each component has its own exposure, activity, and safety evidence and the interaction null is prespecified.

See [Houttuynia](./houttuynia-cordata.md), [combined CP0 systems model](./combined-cp0-systems-model-computational.md), [CFH-dependence hypotheses](./cfh-mechanism-dissociation-cp0-candidates.md), and [complement C5a in gout](./complement-c5a-gout.md).

### Matrix-specific assay gap for microbiome-derived metabolites

Microbiome-metabolite measurement is matrix- and analyte-specific. A method validated for bacterial culture supernatant does not automatically transfer to stool, plasma, intestinal tissue, or another metabolite. Analytical access also does not establish delivered dose, epithelial exposure, target-tissue concentration, target engagement, safety, or efficacy.

For butyrate, two research candidates have primary-source support:

- **Culture supernatant:** The De Baere primary abstract reports HPLC-UV at 210 nm after ether back-extraction and acidification below pH 2, with matrix-matched calibration over 0.5–50 mM and an analyte-spanning 0.5–1.0 mM LOQ range. It does not explicitly state “underivatized” or assign an exact LOQ to butyrate in the accessible text ([PMID 23542733](https://doi.org/10.1016/j.jpba.2013.02.032)).
- **Stool:** Gu et al. reported a coupled VBS-100/G3-electrode, chemical-pretreatment, feature-extraction, and ANN platform compared with GC-MS in a within-study independent 30-sample fecal test cohort. The reported butyrate result is promising, but the full implementation still requires local reproduction and independent external transfer before Open Enzyme use ([PMID 42041444](https://pubmed.ncbi.nlm.nih.gov/42041444/)).

These methods support matrix-specific research directions in the source studies; neither is qualified for an OE workflow. They do not verify a therapeutic exposure or a Q141K rescue. A butyrate experiment must separately measure exposure, ABCG2 surface trafficking, and functional urate flux. Secondary bile acids, microbial indoles, TMAO, and other metabolite classes each require their own validated method.

**Next gates:** [§1.31](./validation-experiments.md#131-butyrate-culture-supernatant-hplc-uv-method-transfer-against-gc-ms) qualifies HPLC-UV for one exact culture-supernatant workflow. [§1.45](./validation-experiments.md#145-fecal-butyrate-electrochemicalann-reproducibility-and-transfer-gate) treats the stool platform as a complete hardware–chemistry–model transfer: obtain the author package, reproduce analytical performance, and then test a locked implementation in an independent cohort. Both require prespecified calibration, precision, and reference-agreement rules.

### Genotype stratification — Q141K and the gut-lumen-sink responder hypothesis

- **Does ABCG2 Q141K change substrate delivery or systemic response for an exact luminal-UOX configuration?** The direction and magnitude are unresolved. Comp-019 did not find genotype-stratified uricase clinical outcomes in its searched sources. COMP-019's unconditional flat-dose classification is not robust to COMP-044's tested substrate-occupancy and finite-window diagnostics; no demographic or responder claim follows.
  - **Path 1 — comp-019/044:** comp-019's 2026-05-08 search identified no genotype-stratified uricase clinical outcome in its searched sources. Its quantitative outputs are not decision-usable, and comp-044 supplies no replacement genotype-response model. Quantitative responder prediction remains open.
  - **Path 2 — §1.33 physiological factorial:** polarized intestinal transport with topology, urate, oxygen, peroxide, survival, and Q141K/WT stratification. This replaces the comp-019-gated single transwell concept.
  - **Path 3 — Overseen genotype-stratified human study, only after the preclinical gates.** A future protocol would require an appropriately manufactured product, regulatory and ethics review, prespecified genotype strata, safety monitoring, and adequate power. Self-administration of shio-koji or engineered koji is not an evidence path.
  - **Path 4 — Existing trial-data partnership.** Seek appropriately consented genotype-linked data from completed uricase studies if available. This is not load-bearing unless a data holder confirms the relevant exposure and outcome fields.
  - **Cross-references:** [COMP-017 intestinal ABCG2 evidence boundary](./intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md), [COMP-016 bounded evidence scan](./t-abcg2-suppression-evidence-mining-computational.md), [cross-validation.md](./cross-validation.md), [gut-lumen-sink.md](./gut-lumen-sink.md), [abcg2-modulators.md](./abcg2-modulators.md), and [personal-genome-protocol.md](./personal-genome-protocol.md).

### Platform selection and thesis

- **Is Open Enzyme's wiki-wide IC50 provenance practice rigorous enough?** Many IC50 values come from review papers, not primary ChEMBL-indexed assays. A written standard would prevent legacy-citation drift. See.
- **Can a source-pinned structure and synonym query recover the exact MCC950 primary assay record?** The current compact ChEMBL receipt cannot answer this; the primary paper remains the evidence source.
- **How should natural-product discovery combine databases and literature?** Use ChEMBL for bounded activity retrieval, then independently search primary multilingual literature by mechanism, material/species, traditional formula, and pathology framing. Non-retrieval in one source is not biological absence.

### Novel modalities (from modality-chokepoint-matrix.md)

The [Modality × Target Matrix](./modality-chokepoint-matrix.md) (2026-04-28) surfaces ten high-leverage exploration vectors not currently in the OE wiki. The highest-priority open questions per the matrix:

- **siRNA against URAT1 mRNA via kidney-targeted delivery.** An oligonucleotide would avoid benzbromarone's reactive-metabolite mechanism but introduces different sequence, immune, formulation, biodistribution, reversibility, and renal-hypouricemia risks. Liver-targeted siRNA supplies adjacent modality precedent; proximal-tubule delivery, a validated guide, gout efficacy, and comparative safety are unresolved. (**Mechanistic Extrapolation**; source: modality-chokepoint-matrix.md)
- **Engineered Faecalibacterium prausnitzii for local butyrate at the gut crypt.** Butyrate-mediated PPARγ induction of wild-type ABCG2 is the supported route. Direct Q141K trafficking rescue is proposed but unvalidated; durable colonization, titer, and epithelial exposure are also open. (Mechanistic Extrapolation; source: modality-chokepoint-matrix.md)
- **Myeloid-tropic LNP delivering NLRP3-silencing mRNA/siRNA to vessel-wall macrophages.** Myeloid LNP work in oncology supplies a delivery-class precedent; gout and vessel-wall translation remain untested. **Mechanistic Extrapolation**; source: modality-chokepoint-matrix.md.
- **Pharmacological chaperone for ABCG2 Q141K folding rescue.** CFTR correctors provide a protein-trafficking precedent within the ATP-binding-cassette superfamily, not evidence of transfer to ABCG2. Basseville 2012 (PMID 22472121) supports the rescue-pathway question; direct surface-expression and urate-flux assays remain required. **In Vitro**; source: modality-chokepoint-matrix.md, abcg2-modulators.md.
- **mRNA-IL-1RA pulse therapy for acute flare termination.** Transient expression could match a flare window, but pulmonary delivery, exposure, receptor occupancy, efficacy, repeat-dose safety, and competitive cost remain untested. A current source-pinned landscape scan is required before making a program-absence claim. (Mechanistic Extrapolation; source: modality-chokepoint-matrix.md)
- **Wearable sweat-based or microneedle continuous UA monitoring.** Changes intervention-titration kinetics. UCSD/Stanford research-stage. (Mechanistic Extrapolation; source: modality-chokepoint-matrix.md)

### GSDMD pore self-delivery — what survives a matched uptake test?

The [GSDMD pore self-delivery paradox](./gsdmd-pore-delivery-paradox.md) remains an open physical-delivery hypothesis. comp-042 ([`kpv-gsdmd-pore-influx-computational.md`](./kpv-gsdmd-pore-influx-computational.md)) is **YELLOW-A2-unresolved**: its A1 engineering states are intra-articular GREEN, subcutaneous YELLOW, and oral RED against an extracellular cell-assay effective-concentration proxy only. Its A2 pore-only heuristic contains favorable cases—absent and low PepT1 are at or above 3× in 9/9 tested concentration × Km cases for every route, while intra-articular reaches that threshold in 2/9 moderate and 1/9 high cases—but does not include concurrent PepT1 uptake in the pore-forming cell and is not total-cell selectivity.

Two empirical questions remain separate. First, do resting and MSU-activated synovial-joint macrophages have functional PepT1 (SLC15A1), and what is matched KPV accumulation with the pore on/off and PepT1 on/off? KPV transport through PepT1 is established in the epithelial and Jurkat-cell systems studied by Dalmasso et al. (**In Vitro**, [PMID 18061177](https://pubmed.ncbi.nlm.nih.gov/18061177/)); synovial-macrophage function is unmeasured. PepT1 absence or low activity would improve the modeled pore-to-healthy baseline but would not resolve KPV timing, because KPV acts upstream and GSDMD pores form downstream. Second, can an empirically prequalified transporter-orphan, membrane-impermeant tracer clear a prespecified pore-on versus pore-off uptake margin? [§1.32](./validation-experiments.md#132-gsdmd-pore-self-delivery--matched-uptake-and-selectivity-probe) tests the broader platform without making a KPV efficacy claim.

### Engineered LBP chassis (independent gout-exploit track)

The [Engineered LBP Chassis](./engineered-lbp-chassis.md) treats engineered obligate anaerobes including *Faecalibacterium prausnitzii*, *Akkermansia muciniphila*, and *Bacteroides* as a peer track to the koji chassis. Six discrete follow-ups are queued; P2-4 is an empirical genetic-entry gate, while the others are evidence scans, comparisons, or hypothesis work:

- **P2-1 — Lit scan: *F. prausnitzii* engineering state-of-the-art.** Genetic-toolkit maturity, measured heterologous-payload activity, stability, containment, and safety gaps.
- **P2-2 — Lit scan: commercial / clinical engineered-LBP landscape.** Synlogic, Vedanta, NextBiotix, Seres, Pendulum — programs, partnership / licensing profile. (Queued, Opus subagent.)
- **P2-3 — Lit scan: FDA LBP regulatory path.** 2018 guidance, Vowst precedent, IND-enabling package, timeline + capital. (Queued, Opus subagent.)
- **P2-4 — Exact-strain engineering entry gate.** COMP-008 is retired. For whichever organism LBP-1 and current evidence advance, transformation and reporter expression is the common empirical gate; native-pathway and heterologous-payload configurations remain separate, unranked questions with open colonization, product-flux, exposure, and function measurements.
- **P2-5 — Falsification card H02.** Stub: [`hypotheses/H02-engineered-lbp-thesis.md`](./hypotheses/H02-engineered-lbp-thesis.md); full population queued.
- **P2-6 — Comparative chassis matrix for gout indication.** *F. prausnitzii* vs. *Akkermansia* vs. *Bacteroides* vs. engineered *E. coli* Nissle — payload tractability, niche fit, engineering complexity.

When the Phase 2 evidence lands, make a track decision: keep, narrow, or close the LBP route. The project mission is already modality-agnostic.

### Purine-Degrading Bacteria (PDB) — gut as independent urate disposal organ

See [purine-degrading bacteria](./purine-degrading-bacteria.md). The 2,8-dioxopurine pathway (Liu et al. 2023 Cell + 2025 Nat Microbiol) establishes ~15–25% of gut bacteria as a functionally distinct urate disposal system that evolved to compensate for hominid uricase loss. Engineered EcN with the full gene cluster (CBT2.0) achieved −63% plasma UA in hyperuricemic mice. Five priority follow-up threads:

**PDB-Q1 — Quantitative SUA reduction from PDB restoration in humans with intact renal function.** The FARMM study (n=30) had no statistical power to detect serum urate changes, and subjects had normal kidneys. What is the mg/dL effect in a typical gout patient? This number gates whether PDB restoration is "adjunctive to pharmacotherapy" or "potentially standalone." Required before designing any PDB clinical trial. No lit scan will resolve this — it requires a prospective study. Frame as a priority gap, not a computation. *(Human RCT or n-of-1 cohort; no current data)*

**PDB-Q2 — Does PDB-derived butyrate at physiological gut concentrations activate ABCG2 via PPARγ?** The butyrate → PPARγ → ABCG2 mechanism is established at pharmacological doses and for dietary fiber effects (DASH RCT, Li 2023 PMID 36948133). Whether native PDB flux generates enough luminal butyrate to meaningfully activate this axis is unresolved. This is a tractable Caco-2 experiment: measure ABCG2 expression in enterocyte monolayers at the butyrate concentrations achievable via gut PDB fermentation vs. pharmacological sodium butyrate doses. **Estimated cost: $2,000–5,000 if a wet-lab partner has Caco-2 capability.** *(In Vitro; immediately testable)*

**PDB-Q3 — Does selenium availability limit gut PDB activity in humans?** See the compact [Research Conjecture and paired abundance-versus-flux test](./purine-degrading-bacteria.md#research-conjecture-selenium-availability-may-gate-microbial-urate-disposal).

**PDB-Q4 — Can yanthine (2,8-dioxopurine) be measured reproducibly in a clinically accessible matrix?** `Yanthine` is the name Li et al. use for 2,8-dioxopurine, the first reported reductive-pathway intermediate; it is distinct from xanthine (2,6-dioxopurine) ([Life Metabolism 2025, DOI 10.1093/lifemeta/loaf031](https://doi.org/10.1093/lifemeta/loaf031)). The reported case-control difference makes yanthine a candidate pathway biomarker, not a validated measure of individual PDB function. Identify a validated assay, matrix, stability window, reference range, and relation to metagenomic pathway abundance before using it for stratification. **Human Observational; biomarker candidate.**

**PDB-Q5 — Which UOX/PDB topology, if any, earns testing?** CBT2.0 shows that EcN can carry a reductive urate-degradation cluster, while PULSE provides an EcN uricase precedent. That does not establish that the pathways are independent, additive, co-localizable, or SCFA-coupled. [comp-031](./dual-chassis-ecn-pdb-uricase-computational.md) is unusable for current decisions because it inherits an unsupported flat UOX regime, assigns unmeasured butyrate production to engineered EcN, and mixes compartments. COMP-044 establishes only that the legacy unconditional flat-dose classification is not robust to the tested substrate-occupancy and finite-window diagnostics. Compare one strain, separate strains, and temporal staging only after validation §§1.33, 1.34, and 1.37 resolve physiological UOX activity, CBT2.0 carbon fate, and spatial residual flux. *(Mechanistic Extrapolation + Animal Model precedents; topology open)*

See [engineered-lbp-chassis.md](./engineered-lbp-chassis.md) (LBP chassis peer track), [gut-lumen-sink.md](./gut-lumen-sink.md) (PULSE/uricase context), [abcg2-modulators.md](./abcg2-modulators.md) (butyrate/PPARγ + *A. indistinctus*/hippuric acid axes).

### TCM-derived urate-axis leads

[TCM-derived gout leads](./tcm-modern-rigor-intersection.md) treats traditional-use and formula records as a hypothesis-discovery surface across urate production, renal and intestinal transport, and inflammation. No compound rank, formula priority, or chassis follows from the current evidence.

- **Mixed-source evidence qualification:** [COMP-049](./etc/experiments/comp-049-tcm-urate-axis-primary-evidence-qualification/) is the pre-run replacement for invalidated COMP-013. It must distinguish primary from secondary sources, preserve tested material separately from traditional occurrence, expose simultaneous attribution/exposure/function gaps, and route without ranking.
- **Formula interaction:** Does a composition-verified formula outperform its components and declared combinations under a prespecified additivity model? See the [formula Research Conjecture](./tcm-modern-rigor-intersection.md#formula-decomposition-without-inventing-synergy).
- **Exposure and attribution:** For each lead, which material and compartment produce the measured effect, and does the named target cause it?
- **Multilingual discovery:** Continue mechanism, species/original-language, traditional-formula, and traditional-pathology query frames; database absence is not biological evidence.
- **H04:** Test whether this method produces new falsifiable connections rather than a larger catalog. See [H04](./hypotheses/H04-tcm-rigor-intersection.md).

### Medicinal-fungal exact-material research thread

The [medicinal-mushroom research page](./medicinal-mushroom-complement-track.md) evaluates exact native materials. Cultivation does not establish composition, exposure, efficacy, safety, product equivalence, or portfolio priority.

- **Search boundary:** retired COMP-014 supplies no strain, cultivation, or
  candidate evidence. New leads must come from primary-source-qualified,
  multilingual searches that preserve exact material identity and tested
  context.
- **Method qualification:** [`medicinal-mushroom-extract-sops.md`](./medicinal-mushroom-extract-sops.md) contains draft analytical candidates whose tolerances remain unset until each method is validated.
- **Matched interaction study:** [`validation-experiments.md` §2.6](./validation-experiments.md) defines a pilot-driven exact-material design; it assumes neither synergy nor a fixed arm count.
- **Exact-material conjecture:** the [medicinal-mushroom research page](./medicinal-mushroom-complement-track.md#research-conjecture--a-reproducible-medicinal-fungal-material-may-expose-a-gout-weakness) asks whether one composition-defined material can produce a reproducible gout-relevant functional signal. It remains a conjecture until one exact material, endpoint, exposure regime, analytical tolerance, and advance/kill threshold are chosen.
- **Exposure grounding:** verify material identity, measured exposure, route, and evidence tier in the primary study before using yield as a translational prior.

The evidence decides whether an exact material and mechanism advance; an inherited rank or track label does not.

### siRNA against URAT1 — discovery-engine output (peer-track exploration vector to LBP)

The [siRNA / URAT1 modality](./sirna-urat1-modality.md) treats kidney-tropic siRNA against URAT1 mRNA as a **discovery-engine output** — non-fermentable, non-microbial, positioned for partner / spinout development rather than in-house manufacture. Sister to the [LBP chassis](./engineered-lbp-chassis.md) under the broader chase-every-avenue framing. Current research questions are:

- **P2-1 — Lit scan: kidney-tropic conjugate chemistry state-of-the-art.** Megalin-binding peptides, CDP nanoparticles, kidney-cortex-selective LNPs, aptamer-siRNA chimeras — design space, current best titers / pharmacokinetics, IP landscape. (Queued, Opus subagent.)
- **P2-2 — COMP-048: human proximal-tubule delivery-handle screen.** Ask whether any internalizing surface receptor co-localizes with SLC22A12-positive cells strongly and selectively enough to justify receptor-targeted delivery work. Keep co-expression, segment enrichment, kidney off-target expression, systemic expression, protein/spatial corroboration, and internalization evidence separate rather than collapsing them into a composite winner.
- **P2-2b — guide design only after delivery survives.** [COMP-009 is invalidated](./urat1-sirna-target-site-selection-computational.md). A new guide-design COMP must cover relevant SLC22A12 transcripts and human variation, perform transcriptome-wide off-target analysis, use a validated current method, and hand candidates to empirical URAT1 knockdown.
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
- **Which exact precursor-to-mediator conversion, if any, is reproducible in a gout-relevant compartment?** Measure EPA, DHA, and each named mediator under one controlled exposure before comparing precursor configurations. No optimal gout ratio is established. See [SPM resolution pathway](./spm-resolution-pathway.md).

### Red-flag thresholds

- **What LFT elevation threshold triggers zileuton discontinuation?** Any future protocol must use current prescribing guidance and clinician oversight.
- **What biomarkers signal microbiome disruption vs. acceptable variation?** Alpha diversity drop threshold, specific pathobiont expansion (e.g., *Clostridium difficile*, *Enterococcus*), inflammatory markers (fecal calprotectin). See [cross-validation.md](./cross-validation.md).
- **Can BCP exposure in the rat MSU model be translated to a human-relevant concentration?** Simple dose scaling does not establish human exposure or safety. Resolve with PK modeling and measured target-tissue exposure before any human study. See [cannabinoids-terpenes.md](./cannabinoids-terpenes.md).

Every question must link to its evidence or experiment surface. Once resolved or falsified, update the linked evidence surface and remove the duplicate question; Git retains the history.
