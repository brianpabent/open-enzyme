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
  - self-experiment-protocol.md
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

---

## Uricase / Enzyme Engineering

Questions about uricase variant selection, GI survival, protease resistance, yeast-vs-koji choice, and expression strategy.

### Variant selection and properties

- **Is *Candida utilis* uricase substantially more amenable to oral delivery than *A. flavus* uricase?** Three programs (Allena/ALLN-346 and two others per industry-revealed preference) picked *C. utilis* over *A. flavus*. Driver could be: (a) higher specific activity, (b) better protease resistance, (c) fewer anti-drug-antibody concerns, (d) IP/freedom-to-operate. See [uricase-variant-selection.md](./uricase-variant-selection.md).
- **No human trial data exists for *A. flavus* uricase delivered orally.** ALLN-346 (*C. utilis*) showed no systemic immune response, but fungal-vs-bacterial immunogenicity differences in the gut lumen are uncharacterized. See [uricase-variant-selection.md §7](./uricase-variant-selection.md).
- **Vibrio vulnificus uricase expression in *S. cerevisiae*: codon optimization and titer remain unknown.** Likely feasible from sequence analysis; no peer-reviewed titer in eukaryotic hosts. See [uricase-variant-selection.md](./uricase-variant-selection.md).
- **Rasburicase's anti-drug-antibody profile in ~60% of patients on IV delivery: does oral mucosal delivery invert this via oral tolerance?** Open — oral tolerance literature suggests yes, but uricase-specific data is absent. See [engineered-yeast-uricase-proposal.md §6 Q5](./engineered-yeast-uricase-proposal.md).

### GI survival and stability

- **Refolding kinetics of acid-unfolded uricase are unknown.** The enzyme's tetramer dissociates at low pH; whether it refolds after duodenal pH normalization determines real-world efficacy beyond simple in vitro survival measurements. See [gi-survival-prediction.md §§refolding](./gi-survival-prediction.md).
- **Does rice bran substrate improve or degrade uricase GI survival?** Rice bran contains phytic acid, phenolics, and fiber — could stabilize the tetramer (polyphenol-tetramer binding) or destabilize it (altered transit time). See [engineered-koji-protocol.md](./engineered-koji-protocol.md).
- **Secretion vs. intracellular expression in yeast — which gives better effective dose?** Intracellular accumulation gives cell-wall acid protection (~10-15% survival advantage) but limits total enzyme output. Secreted is efficient but acid-vulnerable. See [engineered-yeast-uricase-proposal.md](./engineered-yeast-uricase-proposal.md).

### Wild-type koji baseline and EPI applications

- **What is the quantitative enzyme activity of shio-koji (units/g) vs. commercial PERT (Creon, Zenpep units per pill)?** Lab-measurable via amylase / protease / lipase assays of finished shio-koji, but not yet done. This is the key comparison that determines whether wild-type koji is a meaningful PERT-reducer or merely a condiment. **Methodology now specified in [enzyme-quantification-protocol.md](./enzyme-quantification-protocol.md)** — Tier 3 bench first-run (~$200–400 reagents, single-day session at a community-college lab) is the load-bearing experiment. See also [koji-home-fermentation.md](./koji-home-fermentation.md). (source: koji-home-fermentation.md, enzyme-quantification-protocol.md)
- **Is shio-koji-marinated protein a meaningful PERT-reducer in mild-to-moderate EPI?** N=1 / household trials with PERT-dose-per-meal tracking would generate informative observational data. No formal evidence exists. See [koji-home-fermentation.md](./koji-home-fermentation.md). (source: koji-home-fermentation.md)
- **What is the gastric survival of shio-koji-derived enzymes?** Hypothesis: poor without enteric coating; useful only for pre-digestion in marinade phase, not in-gut activity post-ingestion. Testable via simulated gastric fluid (SGF pH 2, pepsin, 2h). See [koji-home-fermentation.md](./koji-home-fermentation.md). (source: koji-home-fermentation.md)
- **Is lipase the limiting digestive-enzyme axis for fat malabsorption EPI when using wild-type *A. oryzae* shio-koji?** Lipase activity of *A. oryzae* shio-koji is low compared to *A. niger* or engineered strains. Quantitative comparison needed. Methodology in [enzyme-quantification-protocol.md §3.1](./enzyme-quantification-protocol.md) (p-NPP lipase assay vs. Creon-cap-equivalent reference standard). See also [koji-home-fermentation.md](./koji-home-fermentation.md), [aspergillus-oryzae.md](./aspergillus-oryzae.md). (source: koji-home-fermentation.md, enzyme-quantification-protocol.md)
- **Are there any human studies of koji-fermented diets in EPI specifically?** None identified. Would be high-value evidence. See [koji-home-fermentation.md](./koji-home-fermentation.md). (source: koji-home-fermentation.md)

### Yeast vs. koji host choice within enzyme-production tracks

- **At what expression and recovery levels does a yeast route become operationally competitive?** Existing mass-burden estimates are track-specific assumptions, not a reason to appoint a different chassis as the project default. See [engineered-yeast-uricase-proposal.md §5](./engineered-yeast-uricase-proposal.md).
- **Can the Ward 1995 *A. awamori* glucoamylase-fusion + KEX-2 architecture (>2 g/L submerged) transfer to solid-state rice koji fermentation?** The submerged-culture precedent is solid (PMID 9634791). Solid-state mass transfer, redox, and proteolysis dynamics are different. This is the specific gating experiment for the lactoferrin co-expression module. See [engineered-koji-protocol.md §16](./engineered-koji-protocol.md), [spm-resolution-pathway.md §5](./spm-resolution-pathway.md).

### Protein engineering

- **Do the OPT-1 disulfide-engineered mutations (A6C + R290C + S119C + C220C + K234E + K236E) fold correctly in *A. oryzae*'s redox environment?** Mutations designed for *S. cerevisiae* expression; *A. oryzae* cytoplasmic redox is different. See, [protein-engineering-strategy.md](./protein-engineering-strategy.md).
- **What is the minimal viable protease-resistant mutation set** that preserves activity while surviving 30-60 min duodenal transit? ALLN-346 achieved ~20× protease resistance; mechanism is covered by a now-expired patent. Literature audit needed. See.

### Genotype stratification of the gut-lumen sink response

- **REOPENED 2026-07-13:** [comp-044](./gut-lumen-uricase-physiologic-regime-computational.md) invalidated comp-019's ΔSUA, genotype ordering, substrate-limited designation, and 25 mg dose recommendation. Phase A's negative finding remains useful: no Q141K-stratified uricase trial was identified. The question is now whether any genotype interaction survives physiological substrate, oxygen, access, survival, and transit constraints. See [validation experiment 1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial).

### Co-engineered substrate-supply mechanisms

Strategic question across the engineering pipeline: should the chassis produce both substrate degradation (uricase) and substrate-supply enhancement (ABCG2 induction or relief of suppression)? The architecture remains plausible, but neither additivity nor genotype-independence is established. Directly measure transporter flux and UOX consumption together; do not inherit comp-019's serum-response mapping.

Three candidate routes are currently defined, each with a different chassis-level implication:

- **Butyrate co-production or co-formulation with a butyrogenic strain.** Butyrate can induce wild-type ABCG2 through PPARγ in relevant models. Whether it directly rescues Q141K surface trafficking and functional urate flux is unproven; Basseville 2012 supplies a rescue-pathway precedent, not a butyrate result. Co-formulation is therefore gated on validation §1.14 and strain-specific carbon fate.

- **Glucoraphanin co-production (Nrf2 → ABCG2 induction).** Already flagged at [abcg2-modulators.md §Engineering implications #1](./abcg2-modulators.md). Sulforaphane precursor produced in the chassis, converted to active sulforaphane by gut myrosinase from cruciferous-resident bacteria. **Mechanistic Extrapolation; *A. oryzae* glucoraphanin biosynthetic pathway feasibility not yet assessed** — multi-enzyme plant pathway, fungal-host expression unknown.

- **Lactoferrin co-expression (relief of TNFα-driven ABCG2 suppression).** Already in flight as [engineered-koji-protocol.md §16](./engineered-koji-protocol.md) for its primary CP1a/CP5b roles. Beyond those: sustained lactoferrin secretion in the lumen would suppress local TNFα → relieve the parallel ABCG2 suppression mechanism (Ferrer-Picón 2020, PMID 31211831). **The lactoferrin module may be doing more for the gut-sink than its current positioning suggests** — secondary effect not yet quantified.

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

- **Does engineered-koji prophylaxis reduce flare frequency on ULT initiation?** This is the clinical question that justifies the platform's "adjunct" positioning. Colchicine is the current standard for ULT-initiation prophylaxis (ACR 2020: 0.5–0.6 mg/day × 3–6 months). A food-based CP1a-targeted koji adjunct could plausibly reduce the frequency of colchicine-rescue or prednisone-rescue events during the dissolution-flare window. Flare-rate endpoint, measurable in any ULT-initiation cohort with adequate follow-up. (Mechanistic Extrapolation; source: colchicine.md §8)
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

- **Can the genotype-informed supplement quantification workflow be validated in a small multi-user pilot (N=5–10) before the larger H09 community-fermentation trial?** The [genotype-informed supplement workflow](./genotype-informed-supplement-workflow.md) defines the five-step closed-loop pipeline (genotype → variant-informed selection → produce/source → Tier 2 batch QC → calibrated dose → biomarker tracking) and is currently instantiated at n=1. [H09 — Community Fermentation Reliability](./hypotheses/H09-community-fermentation-reliability.md) explicitly depends on **multi-user batch consistency**, not single-user feasibility — so an N=5–10 pilot of the workflow itself, before any community-fermentation infrastructure is committed, would test operational failure modes (user error in Tier 2 assays, batch CV exceeding the ±20% Tier 2 tolerance, genotype misclassification from consumer panels). Cost: ~$2,000–5,000 (genotyping + reagents + coordination). **Practical constraints:** real human-subjects work → IRB consideration (low-risk self-experimentation pilots may qualify for exemption, but multi-user data collection probably needs IRB review); recruitment (5–10 motivated participants willing to clinical-grade-genotype + run a stack + report biomarker data); coordination overhead. This pilot is the natural next-step gate before H09.

### Species-gap and translation

- **Does the 1,000× dapansutrile mouse-vs-human cellular IC50 gap apply to every mouse-derived NLRP3 potency claim in the wiki?** Oridonin, BHB, ursolic acid, β-caryophyllene, carnosine — all have murine efficacy as primary evidence. Translation risk is now the dominant uncertainty. See [nlrp3-inhibitor-screen.md ChEMBL appendix](./nlrp3-inhibitor-screen.md).
- **For "pathway modulator" class (quercetin, ursolic acid, BHB, KPV, carnosine, taurine), what's the correct primary-evidence yardstick?** ChEMBL IC50 doesn't exist by definition for these compounds. Is it functional IL-1β suppression in MSU-stimulated human macrophages? See.

### Biomarker interpretation

- **Is hs-CRP alone sufficient to distinguish chokepoint-specific effects in the self-experiment?** No — hs-CRP is a downstream output marker; urinary LTB4 (CP6a), serum C5a (CP0), TNFSF14 (CP1a) are all needed for mechanism. See [self-experiment-protocol.md](./self-experiment-protocol.md).

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
- **Hepatotoxicity mechanism.** Proteasome-driven, redox-driven, mitochondrial, or immune-mediated? Literature divided; practical dose cap (600 mg/day) is conservative enough to cover all. Mechanism informs formulation choice. See [egcg.md Open questions #3](./egcg.md).
- **Does EGCG suppress TNFSF14 at the HVEM-receptor level specifically, or only through general NF-κB blockade?** Replication needed in human macrophages. See [egcg.md Open questions #4](./egcg.md), [validation-experiments.md §1.8](./validation-experiments.md).
- **Can DHA + EGCG achieve combined TNFSF14 suppression?** Orthogonal mechanisms; both already in stack. See [egcg.md Open questions #5](./egcg.md).
- **Does stacking theaflavins + EGCG amplify EGCG's documented hepatotoxicity ceiling?** Theaflavins and EGCG are mechanism-orthogonal and additive at the pathway level (CP1a + CP2/CP3 + URAT1; see [theaflavins.md](./theaflavins.md)), which motivates a combined stack. EGCG carries a documented hepatotoxicity ceiling (EFSA 800 mg/day); theaflavins' own liver profile at supplement doses is **uncharacterized** — *not* an established signal (an earlier synthesis "documented ALT/AST" claim for theaflavins was a fabrication, caught before it propagated; see [theaflavins.md §Contraindications](./theaflavins.md)). Open question: does co-dosing two concentrated tea-polyphenol extracts additively load the hepatic-stress axis, or is theaflavins hepatically neutral at supplement doses? Cheapest discriminator: n=1 with monthly ALT/AST on a theaflavin + matcha regimen. See [egcg.md Open questions #3](./egcg.md).

### Quercetin

- **Does quercetin's 300 nM ChEMBL 5-LOX IC50 translate to cellular neutrophil-chemotaxis block in a gout-relevant assay?** A zileuton head-to-head could resolve this if the question becomes decision-relevant.
- **Is quercetin + Boswellia (AKBA) redundant at 5-LOX, or complementary at IKKβ + 5-LOX?** Depends on AKBA's 5-LOX IC50 and whether the two compounds bind at the same site. ChEMBL query pending. See.

### BHB / Ketones

- **Does the ketogenic-diet-gout rat result translate to a human oral BHB dosing regimen?** The rat study used intrinsic ketogenesis (diet); exogenous BHB dosing has different PK. See [bhb-ketones.md](./bhb-ketones.md), [nlrp3-exploit-map.md](./nlrp3-exploit-map.md).
- **Does BHB's mouse-vs-human species gap follow the dapansutrile pattern?** Mouse ketogenic data may overstate BHB's required human dose. See.
- **How does androgen status interact with BHB's NLRP3-inhibiting effect?** BHB is a multi-target NLRP3 inhibitor ([bhb-ketones.md](./bhb-ketones.md)); androgens have directionally-ambiguous *direct* effects on NLRP3 priming ([androgen-urate-axis.md](./androgen-urate-axis.md) §"Beyond transporters"). The three-way interaction (androgen × MSU × BHB) is untested and matters for the platform's male-skewed demographic — does a high-testosterone or TRT patient need a *higher* BHB dose for the same NLRP3 suppression? **Sub-question:** BHB acts partly via HCAR2/GPR109A, and androgen signaling can cross-modulate GPCR expression, so whether macrophage HCAR2 is itself androgen-sensitive is a mechanistic anchor. Path to resolution: the BHB interaction arm now added to [validation-experiments.md §1.23](./validation-experiments.md) (androgen × MSU × NLRP3). See also [nlrp3-exploit-map.md](./nlrp3-exploit-map.md).

### Lactoferrin

- **Can lactoferrin be expressed in *A. oryzae* at therapeutically relevant titers in solid-state rice fermentation?** *P. pastoris* 3.5 g/L and *A. awamori* >2 g/L are both submerged culture. **Solid-state koji is the missing data point.** The remaining question is specifically the submerged→solid-state transfer. See [engineered-koji-protocol.md §16](./engineered-koji-protocol.md), [spm-resolution-pathway.md §6 Q6](./spm-resolution-pathway.md).
- **Does *A. oryzae* KEX-2 process a glucoamylase-lactoferrin fusion identically to *A. awamori*?** Critical for transferring the Ward 1995 architecture. See [engineered-koji-protocol.md §16 Risks](./engineered-koji-protocol.md).
- **Is there a dedicated gout trial of oral lactoferrin anywhere?** None identified. See [spm-resolution-pathway.md §6 Q5](./spm-resolution-pathway.md).
- **Bovine vs. human lactoferrin — which is the right GRAS-pathway variant?** Bovine has infant-formula history; human has the Aspergillus expression precedent. See [engineered-koji-protocol.md §16](./engineered-koji-protocol.md).

### Carnosine

- **Human gout RCT evidence is absent.** Hyperuricemia rat dual-phenotype data is promising; translation to human serum uric acid / flare reduction is unknown. See [carnosine.md Open questions](./carnosine.md).
- **Engineered yeast carnosine titer (~150 mg/L baseline) needs primary-source confirmation.** Carried from internal analysis without cited peer-reviewed titer. See [carnosine.md Open questions](./carnosine.md), [engineered-koji-protocol.md §15](./engineered-koji-protocol.md).
- **Koji carnosine co-expression feasibility.** No published carnosine-in-koji data; target is mechanistic extrapolation. See [engineered-koji-protocol.md §15](./engineered-koji-protocol.md), [validation-experiments.md §1.24](./validation-experiments.md).
- **Serum carnosinase (CN1) half-life limits.** Whether rapid cleavage caps peak systemic exposure below effective NLRP3-suppression concentration in humans is unresolved. Carnosinase-resistant analogs (D-carnosine, N-acetyl-carnosine) not yet gout-tested. See [carnosine.md Open questions](./carnosine.md).
- **Carnosine + uricase co-delivery: additive, synergistic, or flat?** Complementary mechanisms (renal URAT1/GLUT9 vs. luminal urate degradation). See [carnosine.md Open questions](./carnosine.md).
- **Androgen + carnosine combined experiment not yet run.** The "precision countermeasure" framing in [koji-endgame-strain.md §2.5](./koji-endgame-strain.md) composes two Animal Model links (androgen → URAT1↑ in one set of experiments; carnosine → URAT1↓ in a different set). A combined experiment — hyperuricemia rat on androgen supplementation + carnosine co-treatment vs. androgen alone — would directly confirm or falsify the precision-countermeasure claim. (Mechanistic Extrapolation; source: koji-endgame-strain.md §2.5)

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

- **Can the [quantification-ladder.md](./quantification-ladder.md) Tier 2 assays stay within their pre-registered tracking tolerance (±20% per the ladder's calibrate-once-at-Tier-3 / track-batches-cheap operational pattern) when run by multiple independent home / community-biolab operators after a shared Tier 3 calibration?** The framework is specified; no multi-operator reproducibility data exists. Applies to:
  - **Ergothioneine** ([SOP-6](./medicinal-mushroom-extract-sops.md) Ellman's reagent / DTNB) — well-anchored chemistry but multi-operator data lacking
  - **GLPP** ([SOP-6](./medicinal-mushroom-extract-sops.md) phenol-sulfuric) — same
  - **Cordycepin** ([SOP-6](./medicinal-mushroom-extract-sops.md) diazo-coupling, Speculative) — the *method validity* question is the upstream gate; tracked at [`validation-experiments.md` §1.28](./validation-experiments.md). The *inter-operator reproducibility* question fires only after §1.28 returns GREEN.
  - **Uricase activity** ([enzyme-quantification-protocol.md](./enzyme-quantification-protocol.md), 293 nm UV absorbance) — same multi-operator gap
- **Fires when:** Tier 2 assays start being used in practice by ≥3 independent operators (home + community-biolab adopters); structural prerequisite for the [H09 — Community Fermentation Reliability](./hypotheses/H09-community-fermentation-reliability.md) batch-CV claim (CV < 30% cross-user requires both producer + assay-runner reproducibility). Until then, dormant. Resolution work: design a small multi-operator round-robin (single calibrated reference batch sent to N=3–5 operators, each runs the Tier 2 assay independently, compare results) — estimated $500–1,000 + 4–6 weeks once operator network exists.
- **Cross-references:** [H06](./hypotheses/H06-medicinal-mushroom-complement-track.md), [H09](./hypotheses/H09-community-fermentation-reliability.md), [`quantification-ladder.md`](./quantification-ladder.md), [`medicinal-mushroom-extract-sops.md`](./medicinal-mushroom-extract-sops.md) SOP-6, [`enzyme-quantification-protocol.md`](./enzyme-quantification-protocol.md), [`self-experiment-protocol.md`](./self-experiment-protocol.md) §12 (the workflow that depends on this).

---

## Cross-cutting mechanisms and translation

Questions about shared biological assumptions, interaction risks, delivery constraints, regulatory classification, and the cheapest experiment that can change a verdict.

### Cross-route combination — repurposed drug × luminal urate intervention

The proposed arms target different chokepoints, but route separation does not establish additivity. The research question is whether each arm passes independently and whether the combination improves a prespecified outcome without a drug–microbe, exposure, or safety penalty.

- **Compounded pill** (Rx, daily) — hits CP6a (5-LOX, via zileuton) or CP6b (GSDMD, via disulfiram) — see [`compounding-pharmacy-track.md`](./compounding-pharmacy-track.md) §"Combined / hybrid candidates"
- **Engineered-koji daily food** (shio-koji / amazake / miso) — hits CP0 (luminal uricase) and upstream priming (CP1–CP5) — see [`koji-endgame-strain.md`](./koji-endgame-strain.md)

The combination is mechanistically clean (different mechanisms, different routes), but **no co-administration protocol or patient-experience model exists**:

- What's the timing relationship between the pill and the food? Does enzyme activity in the gut lumen affect drug absorption? Do gut-microbiota changes from daily fermented food alter drug PK?
- What does the daily patient experience look like (pill + condiment + food prep + monitoring)? Adherence-friendly or burdensome?
- What endpoints + biomarkers would actually let us measure layered effect vs. either track alone?
- Off-target interactions: any reasonable drug-food interaction concerns at therapeutic doses?

**Combination gate:** do not design a co-administration protocol until both arms pass their biological, exposure, and safety gates. [comp-027](./computational-experiments.md) is a dose hypothesis, not a prescription pathway.

**Cross-references:** [`compounding-pharmacy-track.md`](./compounding-pharmacy-track.md) §"Combined / hybrid candidates", [`koji-endgame-strain.md`](./koji-endgame-strain.md), [`comp-027`](./computational-experiments.md) (disulfiram dose modeling).

### Koji-track risk — can engineered koji be reliably home- and community-fermented at therapeutic doses?

**Falsification card:** [H09 — Community Fermentation Reliability](./hypotheses/H09-community-fermentation-reliability.md) (stub, 2026-05-15). Full killshot menu, pre-committed thresholds, and assumption stack queued as Phase 2 on the H09 card.

H09 is a production-model risk within the koji track, while [H08](./hypotheses/H08-gut-lumen-sink-platform-thesis.md) tests a mechanism shared by several oral luminal urate-degradation approaches. If H09 fails, community production is revised or killed; centralized koji manufacture and unrelated tracks remain available.

The corpus offers mitigation sketches (chromosomal integration, first-batch QC, never-backslop-past-N rule), but **zero direct empirical evidence for an engineered multi-cassette *A. oryzae* strain in the community-fermentation context.** Community production is therefore a proposal to test, not a claim Brian has made. Ward 1995 §1.9 is the first wet-lab gate, and it validates only lab expression—not community-fermentation reliability.

**Provisional alive/killed thresholds:** CV < 30% cross-user enzyme activity, strain retention ≥ 95% at generation 5, contamination < 5% per batch under hygiene protocol. Killed if a properly-powered multi-user pilot materially misses any of these.

**Phase 2 follow-ups (queued on H09 card, see full table there):**
- P2-1 Lit scan: industrial koji batch-CV baseline (Japanese miso/sake reproducibility data)
- P2-2 Multi-user community-fermentation pilot trial (N=5–10, central QC at community biolab)
- P2-3 Passaging-based strain stability protocol (50 generations, qPCR/activity readout)
- P2-4 Drying activity-retention comparison (lyophilization vs. oven-dry vs. trehalose-lyoprotected)
- P2-5 Contamination-spike test (wild-strain spike, 5-generation tracking)
- P2-6 Smartphone-camera colorimetric uric-acid assay validation
- P2-11 Regulatory framework scoping pass (engineered-spore distribution path) — user-action-required (external consultant engagement)

**Cross-references:** [cross-validation.md](./cross-validation.md), [open-source-platform.md §"Open Questions — Reliability of Community Fermentation"](./etc/open-source-platform.md), [engineered-koji-protocol.md](./engineered-koji-protocol.md), [koji-endgame-strain.md](./koji-endgame-strain.md), [self-experiment-protocol.md](./self-experiment-protocol.md), [`operations/ward-1995-lab-access.md`](../operations/ward-1995-lab-access.md).

### Shared mechanism risk — does the gut-lumen uricase sink produce a clinically meaningful SUA reduction in typical (non-CKD) gout?

**Falsification card:** [H08 — Gut-Lumen Sink Mechanism](./hypotheses/H08-gut-lumen-sink-platform-thesis.md).

Several oral enzyme tracks depend on the gut-lumen sink producing a clinically meaningful SUA reduction in typical gout. The project as a whole does not. No valid numerical band currently exists: [comp-044](./gut-lumen-uricase-physiologic-regime-computational.md) showed that comp-019's mapping omitted physiological substrate occupancy and residence time. The biological and clinical-translation links are both open at the quantitative level:

- **ALLN-346 Phase 2a Study 201** showed signal in CKD patients; Study 202 (broader cohort) showed 0–5% reduction, no significance vs. placebo, and the program terminated with 19/200 enrolled.
- **Zero** uricase trials (ALLN-346, PRX-115, rasburicase, pegloticase) have stratified by ABCG2 Q141K genotype — the Q141K × allopurinol response literature is rich, the Q141K × uricase response literature is empty.
- The comp-019 quantitative model is superseded; comp-044 is a regime audit, not a replacement efficacy model.

**If no topology produces measurable transepithelial urate capture at physiological substrate without redox injury**, the oral UOX mechanism track is killed before a human serum-effect threshold is assigned.

**Phase 2 follow-ups (queued on H08 card):**
- P2-1 — Lit scan for any post-ALLN-346 oral or gut-targeted uricase Phase 2 typical-gout readout (Opus subagent).
- P2-2 — Re-analysis attempt of ALLN-346 Study 202 cohort-level genotype data accessibility (FOIA / sponsor request / supplementary data grep). Highest information-per-dollar killshot if data obtainable.
- P2-3 through P2-6 — Populate assumption stack, killshot menu, pre-committed thresholds, failure-mode coverage map per H01 template.
- P2-7 — Integrate n=1 self-experiment design with the FEUA protocol on [self-experiment-protocol.md](./self-experiment-protocol.md).

**Cross-references:** [cross-validation.md §Claim 1](./cross-validation.md) (feasibility 5.5/10), [gut-lumen-sink.md](./gut-lumen-sink.md), [uricase.md](./uricase.md), [comp-044](./gut-lumen-uricase-physiologic-regime-computational.md).

### Dietary-CP0 track risk — do dietary doses of rosmarinic acid, luteolin, Houttuynia, and Helicteres reach gut-luminal complement-suppressing concentrations?

The dietary-CP0 strategy (four candidates evaluated in comp-018 / comp-020 / comp-039: rosmarinic acid, luteolin, *Houttuynia cordata* polysaccharide, *Helicteres angustifolia* benzofuran lignans) rests on the **assumption** that dietary doses produce gut-luminal concentrations sufficient to suppress complement activation at the C3 convertase / C4 / C5 nodes—and that this local suppression reduces systemic C5a-driven NLRP3 priming at MSU crystal surfaces. The **dietary-PK side is almost entirely unanchored**. The only corpus estimate—252–1,100 µM luminal rosmarinic acid after a 200 mg dose—is calculated from dose and assumed intestinal volume, not measured. Luteolin luminal PK after food intake is uncharacterized; *Houttuynia* polysaccharide residence is unstudied. None has a direct in-vivo measurement of luminal complement suppression after dietary intake.

**Where this is anchored in the corpus:**
- [comp-029 (combined-cp0-systems-model)](./combined-cp0-systems-model-computational.md) returned YELLOW with the substantive reframe that rosmarinic acid's CP0 effect is **gut-luminal-transient, not systemic** — at free plasma Cmax (~20 nM, Baba 2004), the systemic regime returned ~0% inhibition (RA is ~1,700× below the central IC50). RA's CP0 leverage comes from the gut-luminal post-meal window, not from systemic exposure. This **sharpens** the riskiest-assumption claim: it's not "do these compounds work systemically" (settled — they don't, at dietary doses), it's "does the gut-luminal transient window deliver enough exposure at the relevant complement compartment to be mechanistically meaningful."
- [comp-039 (cfh-mechanism-dissociation-cp0-candidates-computational.md) §6](./cfh-mechanism-dissociation-cp0-candidates-computational.md) names bioavailability as a limitation for all four candidates but treats it as a secondary caveat to the CFH-independence classification, not as the primary load-bearing unknown.
- [`complement-c5a-gout.md` §9.7](./complement-c5a-gout.md) preserves the rosmarinic-acid 44× IC50 assay-format spread AND the dietary bioavailability + tissue occupancy as explicitly unresolved.

**If the actual gut-luminal concentrations fall below the IC50 threshold for any of these candidates**, the dietary CP0 strategy collapses from "mechanism-grounded dietary intervention" to "interesting pharmacology that doesn't translate at the dinner table." The CFH-independence classification (comp-039) remains computationally rigorous; the missing variable is whether the candidates ever reach their target at dietary doses.

> **✓ Rosmarinic-acid PK scan 2026-06-01 (multilingual; English + Chinese 迷迭香酸 + Japanese ロスマリン酸).** Did the work on the lead candidate's PK; it leaves the assumption unanchored and **mildly weakens the distal-gut version** of the thesis:
> - **No direct gut-luminal RA measurement exists field-wide** — not just absent from our corpus. The 252–1,100 µM figure is a *calculation* (oral dose ÷ estimated intestinal volume); the scan located it stated verbatim as a calculation in Sasaki et al. ([PMC7828042](https://pmc.ncbi.nlm.nih.gov/articles/PMC7828042/)), which cites an earlier paper for the derivation. *(Attribution note: this entry currently credits "Kang 2021" — reconcile the Kang-2021-vs-Sasaki lineage; both present it as calculated, not measured, so the load-bearing point stands regardless.)*
> - **Plasma route confirmed out** (corroborates comp-029): oral bioavailability ~1–2%; free plasma RA peaks ~0.02–0.16 µM (human, 200–500 mg) to ~0.6–2 µM (rat, high mg/kg) — order-of-magnitude below the complement IC50.
> - **NEW — proximal vs. distal gut.** RA survives the *proximal* small intestine largely intact but is degraded by **colonic microbiota** to caffeic acid + phenylpropionics before the distal gut (shown directly in antibiotic-treated animals — degradation is microbiota-mediated, J Sci Food Agric 2025 [10.1002/jsfa.70000](https://doi.org/10.1002/jsfa.70000)). Since comp-020 verified C3b modification by *intact RA*, the dietary-CP0 mechanism is most defensible as a **proximal small-intestinal** effect (high calculated RA, pre-microbial, intact); the colonic/distal framing is the **weakest** version (active species there is RA's metabolites, whose complement activity is separate and unverified).
> - **Cheapest de-risking experiment (the single highest-value PK datum the project lacks):** a direct segmental intestinal-content RA assay (rat, oral dose, proximal→distal luminal sampling by LC-MS/MS) — converts the load-bearing number from calculation to measurement.
> - PK detail: Cmax human total RA ~162 nmol/L (500 mg Melissa, PLoS One 2015 [pone.0126422](https://doi.org/10.1371/journal.pone.0126422)); rat absolute BA 0.91–1.69% (RSC Adv 2017 [10.1039/C6RA28237G](https://doi.org/10.1039/C6RA28237G)). Evidence level: Animal + Human PK (measured plasma); gut-luminal still calculation-only.

**Provisional alive/killed thresholds:**
- **Alive:** at least one dietary candidate produces a measured gut-luminal concentration ≥ the IC50 (lower bound of the assay-format spread for that candidate) in a fed-state human study, AND the CFH-independence prediction holds in the UKB ↔ AoU cross-tab.
- **Killed:** none of the four candidates produce measured gut-luminal concentrations within an order of magnitude of the IC50 lower bound AND the biobank cross-tab returns null or AMD-paradox direction for the candidates that have dietary-intake quantification (rosmarinic acid via Phenol-Explorer, luteolin via Apiaceae intake — Houttuynia and Helicteres lack UKB exposure quantification).

**Phase 2 follow-ups:**
- **P2-1 — Direct gut-luminal PK measurement (n=1 stable-isotope tracer feasibility scan).** Cheapest first-pass: literature scan for any published gut-luminal PK measurement of the four candidates (deuterated rosmarinic acid, ¹³C-luteolin, fluorescein-tagged Houttuynia polysaccharide). If a tracer study has been done for any of the four, that immediately closes a single instance of this assumption. If none exists, the next step is feasibility-scoping for an n=1 study (intestinal aspirate + LC-MS/MS) — operationally non-trivial but quantifiable.
- **P2-2 — Gut-luminal complement-activity readout as a functional proxy.** Rather than measuring concentration, measure activity: collect stool / colonic effluent from a dietary-RA-loaded subject vs baseline, assay for C3 convertase activity ex vivo with MSU-trigger. If activity drops measurably, that's an integrated readout that covers PK + activity + tissue compartment in one assay. Cheaper than direct PK if a validated complement-activity assay exists for gut-effluent samples (literature scan required).
- **P2-3 — Gate further dietary CP0 candidate expansion on at least one PK anchor.** Until at least one of the four candidates has a measured gut-luminal concentration or a gut-effluent complement-activity reduction, do NOT add a fifth dietary CP0 candidate to the stack. The discipline: when future discovery identifies another candidate, document it as "candidate identified" rather than "candidate added to dietary CP0 stack" until the PK gate closes for at least one existing candidate.
- **P2-4 — Re-anchor §9.9 dormant composition gate.** The dormant C1-INH + rosmarinic acid composition at [`complement-c5a-gout.md` §9.9](./complement-c5a-gout.md) is already gated on rosmarinic acid PK as one of two reactivation conditions. The promotion of this assumption to RA #3 strengthens that gate — the dormant composition reactivates if RA #3 closes positively (RA PK anchor measured) OR if C1-INH RCL kinetic-competition assay returns positive. RA #3 closure is now the cheaper of the two reactivation paths.

**Portfolio relationship:**

| RA | Subject | Load-bearing for |
|---|---|---|
| #1 | Gut-lumen uricase sink produces clinically meaningful ΔSUA in typical (non-CKD) gout | Koji track + engineered LBP track |
| #2 | Engineered koji can be home / community-fermented at therapeutic doses | Koji track distinctive accessibility thesis |
| #3 (new) | Dietary doses of RA / luteolin / Houttuynia / Helicteres reach gut-luminal complement-suppressing concentrations | Dietary-CP0 stack across four candidates; gates the multi-track architecture's dietary arm; informs whether the dietary + engineered LBP composition (per `gout-pathophysiology.md` 2026-05-22 addition) is real or aspirational on the dietary side |

The three are not redundant. #1 gates the upstream uricase mechanism; #2 gates one production and delivery model; #3 gates the dietary arm. Each can be killed independently. A negative result removes or narrows the affected track without changing the project mission.

**Fires when:** any of the dietary candidates is being elevated to a wet-lab or clinical-decision context. Currently fires immediately because Houttuynia is at §1.30 wet-lab prioritization screen status (per [`validation-experiments.md` §1.30](./validation-experiments.md)) — the THP-1 macrophage assay's IL-1β readout is *necessary but not sufficient* to validate the dietary-CP0 thesis; it doesn't measure whether *dietary intake* of Houttuynia produces equivalent gut-luminal concentrations. The Houttuynia §1.30 screen partially derisks Houttuynia's mechanism; the dietary-PK question remains open even if §1.30 returns positive.

**Cross-references:** [`combined-cp0-systems-model-computational.md`](./combined-cp0-systems-model-computational.md) (comp-029 YELLOW — gut-luminal-transient framing), [`cfh-mechanism-dissociation-cp0-candidates-computational.md` §6](./cfh-mechanism-dissociation-cp0-candidates-computational.md) (bioavailability as named limitation across all four candidates), [`complement-c5a-gout.md` §9.7](./complement-c5a-gout.md) (rosmarinic-acid 44× IC50 spread + PK uncertainty), [`complement-c5a-gout.md` §9.9](./complement-c5a-gout.md) (dormant composition gated on this PK question), [`upstream-complement-verification-rerun-computational.md`](./upstream-complement-verification-rerun-computational.md) (comp-020 IC50 verification).

### Class-level Tier 2 assay gap for microbiome-derived metabolites

The [`quantification-ladder.md`](./quantification-ladder.md) framework specifies "calibrate once at Tier 3, track batches at Tier 2" as the operational pattern for verifying dose at home / community-biolab scale. For most compound classes on the platform — cordycepin (diazo-coupling), EGT (Ellman's reagent), GLPP (phenol-sulfuric), engineered-strain uricase (293 nm UV), enzyme assays per [`enzyme-quantification-protocol.md`](./enzyme-quantification-protocol.md) — a Tier 2 home-runnable assay exists and is reasonably calibrated against a Tier 3 anchor. **For microbiome-derived metabolites, no Tier 2 assay exists that is calibrated against a Tier 3 anchor at the relevant biological concentration.** [comp-038](./tier-2-butyrate-assay-audit-computational.md) (2026-05-20) confirmed this for butyrate (YELLOW: no ready-to-adopt home colorimetric / breath / electrochemical assay was identified); by extension, the same gap applies to every metabolite class produced or modified by the gut microbiota.

**Why this is a platform-level open question, not a butyrate-specific inconvenience.** Multiple Open Enzyme intervention tracks depend on microbiome-derived metabolites reaching target tissues at therapeutic concentrations, and **none** has a validated Tier 2 proxy for verifying that the metabolite actually arrived at its target:

- **Purine-degrading bacteria (PDB) → strain-specific carbon fate** → possible PPARγ/ABCG2 signaling only if butyrate production and epithelial exposure are demonstrated; Q141K rescue remains a direct-test question
- **Houttuynia cordata polysaccharide** → gut-microbiota modulation + gut-mucosal TLR4 (per [`complement-c5a-gout.md` §9.7](./complement-c5a-gout.md) Tier 1d dietary CP0+CP1 candidate)
- **Prebiotic fiber → colonic SCFA** → candidate wild-type ABCG2 induction route; direct Q141K rescue remains unvalidated
- **Future microbiome-metabolite tracks** — secondary bile acids (FXR/TGR5), microbial indoles (AHR), TMAO, microbiome-conditioned polyphenol metabolites, *Alistipes* / hippuric acid axis

For each of these, the active metabolite's concentration at the target tissue is currently **assumed**, not measured. The dose remains an unverified variable — indistinguishable from mechanism-failure noise. This is the "silent underdosing" failure mode: the workflow controls it for non-microbiome-mediated compound classes but not for microbiome-mediated ones. Until even ONE metabolite class has a validated Tier 2 proxy, every gut-microbiome-mediated intervention operates under the same invisible dose-verification ceiling.

**Operational consequence for the proposed Q141K experiment.** Exposure verification is necessary but not sufficient. The design also needs direct surface-trafficking and functional urate-flux evidence before butyrate can be treated as a Q141K rescue, much less a personalized intervention.

**Cheapest path to closing the assay gap (per comp-038):** validate HPLC-UV for engineered-strain culture supernatant and electrochemical fecal SCFA profiling for stool against GC-MS spike/recovery. This would verify exposure for the butyrate experiment; it would not establish Q141K rescue. Other metabolite classes still require separate assay development.

> **✓ Butyrate corner partially de-risked — De Baere 2013 primary-source-verified 2026-07-14.** The load-bearing Tier-2 candidate, **HPLC-UV (De Baere et al. 2013, *J Pharm Biomed Anal* 80:107–115, PMID 23542733, [DOI](https://doi.org/10.1016/j.jpba.2013.02.032)), is now verified against the primary source** (not just via comp-038, whose committed artifact remains abstract-level): matrix-matched calibration on **bacterial culture supernatant**, linear **0.5–50 mM** (r 0.9951–0.9993), LOQ 0.5–1.0 mM, **underivatized** (direct UV at 210 nm after liquid-liquid diethyl-ether extraction + acidification to pH<2) — all three load-bearing specifics confirmed. It SURVIVES as the culture-supernatant Tier-2 candidate (community-biolab tier). **Full-text-verified 2026-07-14 (correcting the earlier rejection).** The earlier "electrochemical+ANN FAILS — do not re-surface" claim was **wrong** and contradicted the comp-038 artifact. Full text of PMID 42041444 (Gu et al. 2026, *Biosensors* 16(4):223, [DOI](https://doi.org/10.3390/bios16040223)) shows the electrochemical-ANN fecal SCFA platform was **validated against GC-MS in an independent fecal cohort (n=30), butyric-acid MAE/RMSE 0.029/0.034 mM** — mM-range, butyrate-specific, no pg/mL mismatch. It is a **genuine stool-specific Tier-2 candidate** (matching comp-038's own "most promising stool-specific direction"), pending OE hardware access + independent external validation — **not** a failed candidate; the stool track is a natural §1.31 sibling if stool butyrate becomes load-bearing. The **SCFA ELISA kits remain RED-provisional** (no PubMed/GC-MS validation surfaced; butyrate-specific specificity + spike-recovery required first), per the comp-038 artifact. The candidate-selection question is closed; only the empirical spike/recovery remains, now a tracked wet-lab gate at [`validation-experiments.md` §1.31](./validation-experiments.md) (GREEN/YELLOW/RED criteria), awaiting partner-CRO / community-biolab HPLC-UV + GC-MS access (OE is Phase 0). The methodology pattern is thus established for the SCFA corner; **secondary bile acids / microbial indoles / TMAO remain unaddressed** (P2-3 below queues the bile-acid panel next) and are correctly deferred — none gates a live OE intervention yet, so their full-text verification fires when one does.

**Phase 2 follow-ups:**
- P2-1: comp-038 next-step — focused HPLC-UV protocol-verification scan against GC-MS for butyrate (engineering-strain supernatants first, stool second). Subagent-executable.
- P2-2: If P2-1 produces a workable Tier 2 candidate, design a multi-operator round-robin to validate inter-operator CV at the relevant biological concentration (combines with the [Tier 2 inter-operator reproducibility open question](#quantification-methodology--tier-2-inter-operator-reproducibility) above).
- P2-3: Extend the closed methodology pattern to a second microbiome-derived metabolite class — secondary bile acid panel is the obvious next candidate (LC-MS Tier 3 well-characterized; Tier 2 surface unknown).

**Fires when:** any of the dependent intervention tracks (PDB, Houttuynia gut-microbiota arm, prebiotic-fiber-specific stack) reaches a clinical-decision point where dose verification matters more than directional signal. Until then, the gap is documented and not actionable beyond P2-1's protocol-verification scan.

**Cross-references:** [`quantification-ladder.md`](./quantification-ladder.md), [`tier-2-butyrate-assay-audit-computational.md`](./tier-2-butyrate-assay-audit-computational.md), the proposed Q141K experiment in [`genotype-informed-supplement-workflow.md`](./genotype-informed-supplement-workflow.md), [`purine-degrading-bacteria.md`](./purine-degrading-bacteria.md), and [`abcg2-modulators.md`](./abcg2-modulators.md).

### Genotype stratification — Q141K and the gut-lumen-sink responder hypothesis

- **Can the gut-lumen uricase sink produce meaningful SUA reduction in non-Q141K males, or does the mechanism rely on Q141K-positive disease-state ABCG2 vulnerability to show benefit?** This is the single most important unanswered question for Open Enzyme's primary demographic positioning. If the mechanism only works in Q141K-positive readers (~25-30% of European-descent men, ~50%+ of East Asian men), the platform's addressable population shrinks dramatically — from "all gout patients" to "Q141K-positive gout patients." That's a strategic question that should change trial design, demographic targeting, and possibly commercial framing. (Source: comp-017 + cross-validation.md prior-art context.)
  - **Path 1 — comp-019/044:** comp-019 found no genotype-stratified uricase trial but its efficacy model failed the physiological-regime audit in comp-044. Quantitative responder prediction remains open.
  - **Path 2 — §1.33 physiological factorial:** polarized intestinal transport with topology, urate, oxygen, peroxide, survival, and Q141K/WT stratification. This replaces the comp-019-gated single transwell concept.
  - **Path 3 — n=1 stratified self-experiment (parallel, low-friction).** Brian + contributors with known genotype (via [personal-genome-protocol](./personal-genome-protocol.md) MinION or 23andMe import) take shio-koji or future engineered koji + monitor SUA. Stratify post-hoc by Q141K status. Weak power per individual, but if the platform builds a contributor cohort with genotype data, it's the lowest-cost path to real human evidence. Lives in [self-experiment-protocol.md](./self-experiment-protocol.md) once cohort exists.
  - **Path 4 — Consumer genomics partnership / natural-experiment data (long shot).** 23andMe, AncestryDNA, or other consumer-genomics platforms could potentially surface a small cohort of gout patients with self-reported uricase exposure (allopurinol-failed patients trialing rasburicase IV, plus any existing oral-uricase trial participants who released their data). Long-shot partnership move; not load-bearing unless someone offers it.
  - **Cross-references:** [comp-017 (intestinal ABCG2 sex-dimorphism)](./intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md), [comp-016 (T × intestinal ABCG2 evidence mining)](./t-abcg2-suppression-evidence-mining-computational.md), [cross-validation.md](./cross-validation.md) (gut-lumen uricase mechanism currently rated 6/10), [gut-lumen-sink.md](./gut-lumen-sink.md), [abcg2-modulators.md](./abcg2-modulators.md), and [personal-genome-protocol.md](./personal-genome-protocol.md).

### Platform selection and thesis

- **Is Open Enzyme's wiki-wide IC50 provenance practice rigorous enough?** Many IC50 values come from review papers, not primary ChEMBL-indexed assays. A written standard would prevent legacy-citation drift. See.
- **Does MCC950 / CRID3 / CP-456773 absence from ChEMBL name search reflect a curation gap or a synonym issue?** Worth a direct structure-based query. See.
- **Is there a "ChEMBL blind spot" for natural products?** ChEMBL's curation bias favors medicinal chemistry literature; natural products with strong functional but weak binding data (BCP, BHB, many terpenes) may be systematically underrepresented. See.

### Novel modalities (from modality-chokepoint-matrix.md)

The [Modality × Target Matrix](./modality-chokepoint-matrix.md) (2026-04-28) surfaces ten high-leverage exploration vectors not currently in the OE wiki. The highest-priority open questions per the matrix:

- **siRNA against URAT1 mRNA via kidney-tropic conjugate.** Sequence-specific renal-reabsorption knockdown; cleaner off-target profile than benzbromarone-class uricosurics. Adjacent to inclisiran-style GalNAc conjugate precedent. Zero clinical programs for gout. (Mechanistic Extrapolation; source: modality-chokepoint-matrix.md)
- **Engineered Faecalibacterium prausnitzii for local butyrate at the gut crypt.** Butyrate-mediated PPARγ induction of wild-type ABCG2 is the supported route. Direct Q141K trafficking rescue is proposed but unvalidated; durable colonization, titer, and epithelial exposure are also open. (Mechanistic Extrapolation; source: modality-chokepoint-matrix.md)
- **Myeloid-tropic LNP delivering NLRP3-silencing mRNA/siRNA to vessel-wall macrophages.** Brian-pattern Lp-PLA2 persistence is the n=1 case study. Acuitas/Moderna myeloid LNPs exist for oncology; gout repurposing is novel. (Mechanistic Extrapolation; source: modality-chokepoint-matrix.md)
- **Pharmacological chaperone for ABCG2 Q141K folding rescue.** CFTR-corrector class precedent (~$10B annual market for ΔF508 correction). Same ATP-binding cassette superfamily. Academic mechanism literature exists (Basseville 2012 PMID 22472121); no clinical programs. (In Vitro; source: modality-chokepoint-matrix.md, abcg2-modulators.md)
- **mRNA-IL-1RA pulse therapy for acute flare termination.** Transient expression matches flare window. Zero programs; mechanistically defensible; competes with canakinumab on cost. (Mechanistic Extrapolation; source: modality-chokepoint-matrix.md)
- **Wearable sweat-based or microneedle continuous UA monitoring.** Changes intervention-titration kinetics. UCSD/Stanford research-stage. (Mechanistic Extrapolation; source: modality-chokepoint-matrix.md)

### GSDMD pore self-delivery — does the PepT1 transporter actually show up on macrophages inside the joint?

The [GSDMD pore self-delivery paradox](./gsdmd-pore-delivery-paradox.md) proposes that membrane-impermeant payloads self-concentrate in pyroptotic synovial macrophages during a flare. comp-042 ([`kpv-gsdmd-pore-influx-computational.md`](./kpv-gsdmd-pore-influx-computational.md)) showed the mechanism's *selectivity* hinges on one uncharacterized datum: **do synovial-joint macrophages — resting and MSU-activated — express functional PepT1 (SLC15A1)?** For any PepT1-substrate payload (e.g. KPV), if the answer is yes, the payload enters healthy cells too via a concentrative electrogenic route that can make healthy cells accumulate *more* than pyroptotic ones — collapsing the pore's selectivity (and, if PepT1 is *absent*, reviving KPV as a viable selective payload). Functional PepT1 is demonstrated in immune cells generally ([Dalmasso 2008, PMID 18061177](https://doi.org/10.1053/j.gastro.2007.10.026)) and in inflamed-tissue macrophages ([Viennois 2016, PMID 27458604](https://doi.org/10.1016/j.jcmgh.2016.01.006)), but never quantified in synovial macrophages. Resolvable by immunostaining / qPCR / functional [³H]Gly-Sar uptake on synovial-macrophage samples. Gates the pore-delivery modality; note the [§1.32](./validation-experiments.md) selectivity probe sidesteps it by using a transporter-orphan tracer, so this datum is specifically what would decide whether a *PepT1-substrate* payload could ever be pore-selective. (Named gap; source: comp-042.)

### Engineered LBP chassis (independent gout-exploit track)

The [Engineered LBP Chassis](./engineered-lbp-chassis.md) treats engineered obligate anaerobes (*Faecalibacterium prausnitzii* primary, *Akkermansia muciniphila*, *Bacteroides*) as a peer track to the koji chassis. Six discrete in silico follow-ups are queued — none requires pharma-partner involvement to start:

- **P2-1 — Lit scan: *F. prausnitzii* engineering state-of-the-art.** Genetic toolkit maturity, heterologous payload titers achieved, gap to therapeutic-grade. (Queued, Opus subagent.)
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

**PDB-Q3 — Selenium status and gut PDB function in humans.** DOPDH (the key PDB enzyme) requires selenium and runs 27x faster with selenium than the sulfur-dependent variant. Liu et al. 2025 cites correlations between lower urinary molybdenum and higher serum urate / gout incidence; the selenium arm of this is implied but uncharacterized. **Immediate personal action: add serum selenium to next blood panel.** If Brian's selenium is low-normal, supplementation (55–200 µg/day, safe range, $0.10/day) could activate latent PDB capacity without any bacterial intervention. A lit scan for "serum selenium × serum urate × gut metagenomics" in existing biobank cohorts could be run as a subagent task in a few minutes. *(Mechanistic Extrapolation; trivial personal test)*

**PDB-Q4 — Is yanthine (2,8-dioxopurine) measurable on any commercial panel?** Yanthine is elevated in gout patients vs. healthy controls (Life Metabolism 2025, n=68) — it is the first PDB pathway intermediate, and elevated serum yanthine = PDB insufficiency. If there is a commercial metabolomics panel or specialty lab offering yanthine measurement, adding it to Brian's next self-experiment draw would answer whether *his* gut PDB are functionally depleted. This is a $200–400 metabolomics panel question, not a $10K research study. Lit scan to identify: does Metabolon Precision Metabolomics, Genova NutrEval, or similar measure yanthine / 2,8-dioxopurine? *(Human biomarker; immediate triage task)*

**PDB-Q5 — Which UOX/PDB topology, if any, earns testing?** CBT2.0 shows that EcN can carry a reductive urate-degradation cluster, while PULSE provides an EcN uricase precedent. That does not establish that the pathways are independent, additive, co-localizable, or SCFA-coupled. [comp-031](./dual-chassis-ecn-pdb-uricase-computational.md) is invalidated and validates neither a combined strain nor separate strains. Compare one strain, separate strains, and temporal staging only after comp-044/045/046 and validation §§1.33/1.34/1.37 resolve physiologic UOX activity, CBT2.0 carbon fate, and spatial residual flux. *(Mechanistic Extrapolation + Animal Model precedents; topology open)*

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

The [Medicinal Mushroom Complement Track](./medicinal-mushroom-complement-track.md) treats native-compound medicinal mushrooms (*Ganoderma lucidum* GLPP, *Cordyceps militaris* cordycepin+pentostatin, *Pleurotus citrinopileatus* ergothioneine, *Lentinula edodes* eritadenine, *Hericium erinaceus* erinacines, *Trametes versicolor* PSK, *Inonotus obliquus* inotodiol) as a peer track to engineered koji / engineered LBPs / siRNA discovery. Different engineering discipline (cultivation + extraction, NO genetic engineering); different consumption UX (decoction / tincture / dried fruiting body vs koji condiments); regulatory simplicity (GRAS food / supplement-grade, no GMO burden). Seven Phase 7 follow-ups are tracked in [§6](./medicinal-mushroom-complement-track.md):

- **#1 Strain selection lit scan ✅** (multilingual, 2026-05-06; outputs: Ganoderma / Cordyceps / Pleurotus per-species scan files in comp-014 outputs dir)
- **#2 Cultivation × yield meta-analysis ✅** (2026-05-06)
- **#3 Extract characterization SOPs** — stub at [`medicinal-mushroom-extract-sops.md`](./medicinal-mushroom-extract-sops.md) (SOP-1 GLPP gated on Phase 5b CNKI dive; SOP-3 EGT lowest-friction)
- **#4 GLPP+cordycepin synergy wet-lab gate** — stub at [`validation-experiments.md` §2.6](./validation-experiments.md) (4-arm: whole-fermentate / cordycepin / cordycepin+GLPP / cordycepin+pentostatin)
- **#5 H06 hypothesis card ✅** (stub at [`hypotheses/H06-medicinal-mushroom-complement-track.md`](./hypotheses/H06-medicinal-mushroom-complement-track.md))
- **#6 Modality-chokepoint-matrix native-compound row ✅** (2026-05-06)
- **#7 Therapeutic dose grounding pass** — for each load-bearing compound (cordycepin, GLPP, ergothioneine, eritadenine, erinacines, PSK, inotodiol, astilbin), grep-verify the human therapeutic dose range from primary clinical / supplement-trial literature under the [pre-commit grep-verify gate](../CLAUDE.md). The track currently discusses production yields without a dose-context anchor — without that anchor, "GYS60 hits 7,883 mg/L" is meaningless to a supplement-stack decision and to the wet-lab-gated Phase 2 follow-ups. Cross-applies to the [TCM compound triage](./tcm-gout-compound-triage-computational.md) compounds. Output: per-compound dose-grounding table (typical supplement / clinical-trial / mechanism-derived ranges, with confidence tier). **Sub-task:** while in primary literature, also note validated colorimetric-assay precedents at ~Tier 2 sensitivity per [`medicinal-mushroom-extract-sops.md` SOP-6](./medicinal-mushroom-extract-sops.md) — specifically whether a diazo-coupling cordycepin assay exists (current SOP-6 flags this as Speculative); Ellman's-for-EGT and phenol-sulfuric-for-total-polysaccharide are already well-anchored.

**CTO-actionable TODOs** are tracked operationally — see [`operations/todos.md`](../operations/todos.md) §"Phase 7 medicinal-mushroom-complement track" (TODO surface; this index points to it for completeness per the umbrella aggregation pattern).

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

The [Ward 1995 §1.9 lab-access landscape](../operations/ward-1995-lab-access.md) maps parallel options for executing [validation §1.9](./validation-experiments.md#19-ward-1995-dual-cassette-feasibility-test-koji-endgame-strain-gate) across Japan, China, and Europe. Key findings:

- **NSlD-ΔP10 (the ten-protease-deletion chassis required for H01 Killshot #1) is not deposited in any public culture collection.** The Maruyama lab at the University of Tokyo is the only verified source. (source: ward-1995-lab-access-global.md)
- **Single most actionable lead:** Jun-ichi Maruyama (amarujun@mail.ecc.u-tokyo.ac.jp), University of Tokyo, origin lab for NSlD-ΔP10. A draft email is available in the operations document.
- **Parallel paths if Tokyo doesn't engage:** Jingwen Zhou / Guoqiang Zhang group at Jiangnan University (C19 chassis, multi-locus integration); Mortensen group at DTU (CRISPR-Cas9/Mad7 toolkit, strongest in Europe).
- **Order-of-operations:** Week 0 email Maruyama + Jiangnan in parallel; Week 2 email DTU if no response; Week 4 query JCM/CGMCC for substitute strains; Week 6 reframe as paid CRO request.

Lab-access and outreach logistics live in the [operations document](../operations/ward-1995-lab-access.md). The scientific question here is whether the construct expresses, remains active, and survives the relevant processing conditions.

### Community fermentation and strain stability

- **Does engineered koji drift across generations of home propagation?** Food-grade strains carry no antibiotic selection marker (correct for GRAS compliance), which removes the pressure that keeps the construct in the population. Chromosomal integration + redundant copies mitigate but don't eliminate. See [open-source-platform.md §Open Questions](./etc/open-source-platform.md).
- **Do 100 home fermenters of the same koji strain get consistent enzyme titers and NLRP3 activity?** Home conditions ≠ lab conditions. Protocol robustness is the gating question for the decentralized vision. See [open-source-platform.md §Open Questions](./etc/open-source-platform.md).
- **Is distribution of engineered spores "drug manufacturing" (requires IND) or "research strain" (flexible)?** Regulatory question with large downstream implications. See [open-source-platform.md §Open Questions](./etc/open-source-platform.md).

### Regulatory

- **Is an engineered-yeast food product a food (GRAS self-determination), a dietary supplement (DSHEA), or a Biologic License Application?** FDA's evolving live-biotherapeutic-products (LBP) framework may apply. See [engineered-yeast-uricase-proposal.md §6 Q4](./engineered-yeast-uricase-proposal.md).
- **Does the canakinumab approval (Aug 2023) create demand for a cheaper IL-1β blocker reachable via food-grade engineering?** Canakinumab at $300K/year is the price ceiling; anything food-grade clears cost bar. Question is whether food-grade compounds can produce clinically meaningful IL-1β suppression. See.

### Microbiota and safety at scale

- **Does daily high-enzyme + NLRP3-inhibitor load select for specific commensals or cause dysbiosis?** Repeated-dose koji is effectively a selection-pressure experiment on gut flora. See [cross-validation.md](./cross-validation.md).
- **Do any commensals express uricase natively?** If yes, does engineered uricase suppress or enhance them? See.
- **For Brian's n=1 self-experiment specifically — what microbiome red flags would matter?** Scope clarification (2026-04-27): the platform is not chasing regulatory approval; the question is what to monitor in Brian's self-experiment to detect dysbiosis early enough to course-correct. Candidate panel: stool 16S at baseline + week 4/8/12, watch for alpha-diversity drop >20%, *C. difficile* / *Enterococcus* expansion, fecal calprotectin elevation, persistent stool-form change. A full safety cohort (n=8) is out of scope for a self-experiment; the n=1 monitoring panel is the right resolution. Tracked separately in [`self-experiment-protocol.md`](./self-experiment-protocol.md). See.

### Combination therapy

- **Could engineered koji become standard adjunct to allopurinol?** ALLN-346 trial demonstrated enzyme-adjunct efficacy on stable allopurinol. Complementary mechanisms (XO upstream, luminal-degradation downstream). See.

---

## Safety and experimental methodology

Questions about biomarker interpretation, stopping rules, microbiome impact, and the limits of n=1 inference.

### Biomarker design

- **Does the self-experiment protocol need CP0 and CP5b biomarkers to be mechanistically interpretable?** hs-CRP alone cannot distinguish quercetin (CP6a) effects from BHB (CP2) effects. See [self-experiment-protocol.md](./self-experiment-protocol.md).
- **What's the optimal EPA:DHA ratio for gout-specific SPM production (RvD1/MaR1 vs. RvE1)?** Does it differ from the cardiovascular-optimized ratio? See [spm-resolution-pathway.md](./spm-resolution-pathway.md).

### Red-flag thresholds

- **What LFT elevation threshold triggers zileuton discontinuation?** Any future protocol must use current prescribing guidance and clinician oversight.
- **What biomarkers signal microbiome disruption vs. acceptable variation?** Alpha diversity drop threshold, specific pathobiont expansion (e.g., *Clostridium difficile*, *Enterococcus*), inflammatory markers (fecal calprotectin). See [cross-validation.md](./cross-validation.md).
- **Is BCP dose-scaling from 100-400 mg/kg rat MSU to 50-200 mg/day supplement safe to extrapolate upward?** If supplement is 20-50× under-dosed, bumping the dose has unknown off-target profile in humans. See [cannabinoids-terpenes.md](./cannabinoids-terpenes.md).

Every question must link to its evidence or experiment surface. Once resolved or falsified, update the linked evidence surface and remove the duplicate question; Git retains the history.
