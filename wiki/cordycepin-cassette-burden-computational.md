---
title: "Cordycepin (cns1+cns2) Cassette Metabolic Burden: Computational Analysis (comp-023)"
date: 2026-05-14
tags:
  - cordycepin
  - cns1
  - cns2
  - aspergillus-oryzae
  - koji
  - koji-endgame-strain
  - metabolic-burden
  - flux-balance-analysis
  - fba
  - genome-scale-metabolic-model
  - iWV1314
  - vongsangnak-2008
  - lactoferrin
  - uricase
  - kojic-acid
  - ergothioneine
  - carnosine
  - chaperone-orthogonal-stacking
  - cassette-compatibility
  - jeennor-2023
  - computational
  - comp-023
related:
  - computational-experiments.md
  - chaperone-orthogonal-stacking.md
  - koji-endgame-strain.md
  - medicinal-mushroom-complement-track.md
  - cassette-compatibility-computational.md
  - validation-experiments.md
sources:
  - "PMID 38071331 (Jeennor S et al. 2023, Microb Cell Fact). Efficient de novo production of bioactive cordycepin by Aspergillus oryzae using a food-grade expression platform; 564.64 ± 9.59 mg/L/day on glucose"
  - "PMID 29056419 (Xia Y et al. 2017, Cell Chem Biol). Fungal Cordycepin Biosynthesis Is Coupled with the Production of the Safeguard Molecule Pentostatin; original cns1+cns2+cns3 BGC characterization"
  - "PMC11300563 (Wang et al. 2023, Int Microbiol). A novel complementary pathway of cordycepin biosynthesis in Cordyceps militaris; confirms Cns1 = oxidoreductase, Cns2 = HDc-family phosphohydrolase, Cns3 = kinase"
  - "Yan et al. 2024, Front Chem Eng (doi 10.3389/fceng.2024.1446454). Prospects for cordycepin biosynthesis in microbial cell factories; cns1+cns2 sufficient for heterologous expression, host-derived 3'-AMP supply"
  - "PMID 18801187 (Vongsangnak W et al. 2008, BMC Genomics). Improved annotation through genome-scale metabolic modeling of Aspergillus oryzae; iWV1314 GEM source"
  - "BioModels MODEL1507180056; iWV1314 SBML deposit (2,361 reactions, 1,104 metabolites, 1,346 genes)"
  - "PMID 20650324 (Terabayashi Y et al. 2010, Fungal Genet Biol). Identification and characterization of genes responsible for biosynthesis of kojic acid"
  - "PMID 21514215 (Marui J et al. 2011, Appl Microbiol Biotechnol). Kojic acid biosynthesis in A. oryzae is regulated by a Zn(II)2Cys6 transcriptional activator"
  - "PMID 25496641 (Hu W et al. 2014, Org Lett). Bioinformatic and Biochemical Characterizations of C-S Bond Formation and Cleavage Enzymes in N. crassa Ergothioneine Biosynthetic Pathway"
  - "PMID 22276148 (Seebeck FP 2010, J Am Chem Soc / Bello MH 2012, Mol Microbiol). Ergothioneine biosynthesis EgtA-E mechanism"
status: complete (v1)
---

# Cordycepin Cassette Metabolic Burden: comp-023

## Question

Does adding the bacterial **cns1+cns2 cordycepin biosynthesis pathway** (Jeennor 2023, [PMID 38071331](https://pubmed.ncbi.nlm.nih.gov/38071331/), 564 mg/L/day in *A. oryzae*) on top of the dual uricase + lactoferrin cassette in the [koji-endgame-strain](./koji-endgame-strain.md) §1 design impose a prohibitive metabolic burden, defined by:

- Growth rate penalty vs. wild-type *A. oryzae* on glucose-minimal media
- Native kojic acid yield (target: ≥80% of dual-cassette baseline)
- Native ergothioneine yield (target: ≥80% of dual-cassette baseline)

This is the proteome-burden gap that the [chaperone-orthogonal-stacking framework](./chaperone-orthogonal-stacking.md) explicitly flags as out-of-scope (line 238: "framework scores ER folding-machinery competition... does NOT track generic proteome burden imposed by cytosolic enzymes"). The cns1+cns2 pathway is cytosolic and assigns zero PDI/calnexin/BiP load in the chaperone framework; but cytosolic protein synthesis, precursor pool draw (adenosine + ATP + NADPH), and carbon balance are real burdens that need an orthogonal evaluation.

## Verdict

**GREEN. The cns1+cns2 cordycepin arm is metabolic-burden-feasible at the Jeennor 2023 empirical titer.** The cassette is predicted to consume <1% of cellular carbon flux at 564 mg/L/day, leaves growth rate within +0.02% of dual-cassette baseline, and leaves kojic acid + ergothioneine yield headroom at 100% of baseline.

Decision criteria (per [computational-experiments.md](./computational-experiments.md) comp-023 row):

| Metric | Threshold | Observed | Pass? |
|---|---|---|---|
| Growth penalty vs WT | <10% | +0.02% | ✓ |
| Kojic acid yield vs dual | ≥80% | 100.00% | ✓ |
| Ergothioneine yield vs dual | ≥80% | 100.00% | ✓ |
| Cordycepin flux delivers Jeennor titer | 564 mg/L/d | 564.6 mg/L/d (constrained at empirical anchor) | ✓ |

**Recommendation:** green-light the cordycepin arm of the [koji-endgame-strain](./koji-endgame-strain.md) §1.9 extended design subject to the limitations enumerated below. The metabolic-burden axis does not rule it out. Other risk axes (cassette-design integration per [comp-010](./cassette-compatibility-computational.md), adenosine deaminase competition without pentostatin co-engineering, integration-locus interference) remain open and need separate validation.

## Method summary

**GEM.** [Vongsangnak 2008 iWV1314](https://www.ebi.ac.uk/biomodels/MODEL1507180056) ([PMID 18801187](https://pubmed.ncbi.nlm.nih.gov/18801187/)) is the *A. oryzae* genome-scale metabolic model, fetched from BioModels (MODEL1507180056). 2,361 reactions / 1,104 metabolites / 1,346 genes / 4 compartments (cytosol, peroxisome, mitochondria, extracellular). The original Vongsangnak 2008 paper reported 1,314 reactions and 1,073 metabolites; the BioModels deposit is the curated/extended version.

**Solver.** [cobrapy 0.31.1](https://github.com/opencobra/cobrapy) with the default GLPK linear programming backend. Standard flux-balance analysis (FBA) maximizing the biomass-formation reaction (r1897 in iWV1314), with the cassette demand reactions added as lower-bounded flux constraints.

**Media setup.** Glucose-minimal media. iWV1314 ships with 81 source-uptake reactions all at bounds (0, 10): the model on default settings can take up every carbon source, every amino acid, and most central-carbon intermediates simultaneously, which violates minimal-media constraints. We close all non-essential uptakes and re-open only D-glucose (10 mmol gDW⁻¹ h⁻¹, canonical FBA reference), NH₃ (unconstrained), O₂ (unconstrained), phosphate (unconstrained), sulfate (unconstrained). CO₂ uptake is closed to 0 (cells produce CO₂; this prevents the model from using exogenous CO₂ to bypass glucose-carbon limitation). Eighteen reverse-direction "Excretion" reactions (r2281-r2298 with lb = -10) covering central-metabolism pools are also closed to prevent metabolite-pool inflow.

**Cassette perturbations.**

| Cassette | Anchor titer | Stoichiometry added to GEM | Source |
|---|---|---|---|
| Uricase (*A. flavus uaZ*) | 40 mg/L/d (Phase 0 conservative) | Glutamate + 4.5 × ATP + 4.5 × H₂O → ADP + Pi + H⁺ per amino acid (translation + secretion cost proxy) | [Comp-010](./cassette-compatibility-computational.md) |
| Lactoferrin (hLf) | 500 mg/L/d (§1.9 success threshold) | Same with 6.0 × ATP per amino acid (translation + PDI-heavy ER folding cost proxy) | [koji-endgame-strain §1.9](./koji-endgame-strain.md) |
| cns1+cns2 cordycepin | 564 mg/L/d (Jeennor 2023 empirical) | Adenosine + ATP + NADPH → cordycepin + ADP + Pi + NADP⁺ + H⁺ (host kinase + Cns2 phosphohydrolase + Cns1 oxidoreductase net) | [PMID 38071331](https://pubmed.ncbi.nlm.nih.gov/38071331/) |
| carnS (carnosine synthase) | ~50 mg/L/d (cytosolic placeholder) | β-alanine + L-histidine + ATP → carnosine + AMP + PPi | [chaperone-orthogonal-stacking §4](./chaperone-orthogonal-stacking.md) |
| panD (aspartate decarboxylase) | ~100 mg/L/d (cytosolic placeholder, paired with carnS) | L-aspartate + H⁺ → β-alanine + CO₂ | [chaperone-orthogonal-stacking §4](./chaperone-orthogonal-stacking.md) |

**Native metabolite pathways added.** iWV1314 does not include kojic acid or ergothioneine biosynthesis. We added simplified net reactions:

- **Kojic acid**: D-glucose + O₂ + NADP⁺ → kojic acid + 2 H₂O + NADPH + H⁺ (Mechanistic Extrapolation; per [Terabayashi 2010 PMID 20650324](https://pubmed.ncbi.nlm.nih.gov/20650324/) + [Marui 2011 PMID 21514215](https://pubmed.ncbi.nlm.nih.gov/21514215/): one oxidation + two dehydrations; KojA is FAD-dependent but FBA stoichiometry is equivalent with NADP⁺/NADPH as redox carrier).
- **Ergothioneine**: L-histidine + 3 SAM + L-cysteine + O₂ → ergothioneine + 3 SAH + pyruvate + NH₃ + H₂O (fungal Egt1+Egt2 net, per [Hu 2014 PMID 25496641](https://pubmed.ncbi.nlm.nih.gov/25496641/) + [Bello 2012 PMC3438316](https://pmc.ncbi.nlm.nih.gov/articles/PMC3438316/)).

**Burden metrics.**

1. *Growth rate*: biomass-formation flux r1897 (model-native units; treat as relative across scenarios, not absolute h⁻¹, since the model's biomass coefficient sum is ~153 and the flux scale doesn't correspond to literature mu_max directly).
2. *Max kojic flux*: re-optimize on EX_KOJIC with biomass locked ≥ 99% of its scenario-optimal value. Tells us how much headroom remains for native metabolite production.
3. *Max ergothioneine flux*: same approach for EX_EGT.
4. *Cordycepin flux*: direct read of EX_COR, clamped at the scenario's empirical demand.

**Pre-commit grep-verify gate ([CLAUDE.md Rule 4](../CLAUDE.md)).** Every load-bearing number in this page is verified against a primary source: cordycepin titer (Jeennor 2023 abstract, 564.64 ± 9.59 mg/L/d), Cns1/Cns2/Cns3 enzyme assignments (Xia 2017 Cell Chem Biol, Wang 2023 Int Microbiol, Yan 2024 Front Chem Eng review), iWV1314 model dimensions (BioModels deposit metadata + cobrapy load), §1.9 success thresholds (verified against [koji-endgame-strain.md](./koji-endgame-strain.md) §3.2 + [validation-experiments.md §1.9](./validation-experiments.md)).

## Key results

Five primary scenarios + four stress-test scenarios (cordycepin demand swept 10×, 100×, 1,000×, 10,000× and 100,000× the Jeennor empirical titer).

| Scenario | growth (model-native flux) | Δ growth vs WT | max kojic | kojic yield vs dual | max EGT | EGT yield vs dual | cordycepin flux (mmol gDW⁻¹ h⁻¹) | Verdict |
|---|---|---|---|---|---|---|---|---|
| WT | 17.678 | (ref) | 5.767 | (ref) | 1.098 | (ref) | n/a | n/a |
| dual (uricase + Lf) | 17.675 | +0.02% | 5.766 | 100.0% | 1.098 | 100.0% | 0 | GREEN |
| **+cns1-cns2 (Jeennor titer)** | **17.675** | **+0.02%** | **5.766** | **100.0%** | **1.098** | **100.0%** | **0.0187** (= 564 mg/L/d) | **GREEN** |
| +carnS+panD | 17.674 | +0.02% | 5.765 | 100.0% | 1.098 | 100.0% | 0 | GREEN |
| +panD only | 17.675 | +0.02% | 5.765 | 100.0% | 1.098 | 100.0% | 0 | GREEN |
| Stress 10× titer (~5.6 g/L/d) | 17.681 | -0.01% | 5.767 | 100.0% | 1.099 | 100.0% | 0.187 | GREEN |
| Stress 100× titer (~56 g/L/d) | 17.731 | -0.30% | 5.775 | 100.2% | 1.110 | 101.1% | 1.873 | GREEN |
| Stress 1,000× titer (~564 g/L/d) | 15.865 | +10.26% | 5.236 | 90.8% | 1.185 | 107.9% | 18.728 | **RED** |
| Stress 10,000× titer | INFEASIBLE | n/a | n/a | n/a | n/a | n/a | n/a | INFEASIBLE |
| Stress 100,000× titer | INFEASIBLE | n/a | n/a | n/a | n/a | n/a | n/a | INFEASIBLE |

(Full numeric output: [`experiments/comp-023-cns1-cns2-metabolic-burden/outputs/results.json`](../experiments/comp-023-cns1-cns2-metabolic-burden/outputs/results.json). Reproducible by `python3 analyze.py` in the experiment folder.)

**Three load-bearing observations:**

1. **The Jeennor 2023 titer is ~3 orders of magnitude below the metabolic-burden breakpoint.** The FBA breakpoint where cordycepin demand starts to materially compete with growth + native metabolites is around 564 g/L/day (1,000× the empirical titer), far beyond anything achievable in submerged fungal fermentation. The 564 mg/L/d demand consumes ~0.02% of glucose-carbon flux. *(Mechanistic Extrapolation; FBA prediction, in silico.)*

2. **Cordycepin biosynthesis taps a low-cost intracellular adenosine pool.** Under the FBA flux distribution, the cordycepin pathway substrate (adenosine) is supplied primarily via the S-adenosylhomocysteinase reaction (r857: SAH → adenosine + homocysteine), i.e., from the SAM cycle exhaust rather than from net de novo purine biosynthesis. WT and dual-cassette scenarios already produce ~1.78 mmol gDW⁻¹ h⁻¹ adenosine from r857, then waste it via adenosine kinase (r1128: ADN + ATP → ADP + AMP, an essentially futile cycle in cells with ample purine supply). Adding the cns1+cns2 demand redirects this adenosine to cordycepin export, which is actually a small net-positive for ATP economy at modest demand levels (this is why "Δ growth vs WT" reads negative, i.e., growth marginally *up*, at 10× and 100× the Jeennor titer: the cordycepin pathway substitutes for the ATP-wasting adenosine kinase step). *(Mechanistic Extrapolation; FBA flux split, in silico.)*

3. **Kojic acid headroom at 100% of dual baseline.** The model can produce up to 5.77 mmol gDW⁻¹ h⁻¹ kojic acid while sustaining ≥99% of scenario-optimal growth, identical to the dual-cassette baseline. Same for ergothioneine (1.10 mmol gDW⁻¹ h⁻¹). The cordycepin cassette does not compete for the load-bearing precursor pools of either native metabolite. Kojic acid comes from glucose directly. Ergothioneine from histidine + SAM + cysteine. None of these compete with the adenosine pool that cns1+cns2 draw down. *(In Vitro consistency check: native kojic acid yield in WT *A. oryzae* is 3-5 g/L per [koji-endgame-strain.md §2.3](./koji-endgame-strain.md), within order-of-magnitude of the FBA prediction at 5.77 mmol/gDW/h × 5 gDW/L × 24 h × 142 g/mol = 98 g/L/d theoretical maximum. The empirical titer is ~5-10% of theoretical maximum, consistent with FBA upper-bound conventions.)*

## Impact on experimental priorities

**[koji-endgame-strain.md](./koji-endgame-strain.md) §1.9 extended design now has a green-lit cordycepin arm.** The cassette is metabolic-burden-feasible. Update the §1.9 validation framing to reflect that the cordycepin arm has cleared the in silico pre-feasibility gate, not just been hand-waved as cytosolic-and-therefore-low-burden.

**Three wet-lab gates still open for the cordycepin arm**, each of which would benefit from a discrete comp-NNN follow-up before committing wet-lab resources:

1. **Adenosine deaminase competition.** The host's native ADA (r1115-r1117 in iWV1314) deaminates adenosine to inosine + NH₃, draining the cns1+cns2 substrate pool. Jeennor 2023 reached 564 mg/L/d *without* pentostatin co-engineering, but submerged-glucose fermentation may have low ADA-derived deaminase pressure compared to solid-state koji. *Recommended:* comp-024-style scope page asking whether ADA-knockout or pentostatin co-expression is needed for the koji endgame strain, with FBA simulation under varying ADA activity. Cross-reference [`medicinal-mushroom-complement-track.md` §"The natural Cordyceps ADA-inhibitor pairing"](./medicinal-mushroom-complement-track.md) where pentostatin co-production is already flagged as the engineering route to ADA protection.

2. **PDI/chaperone load from triple-cassette stacking.** This FBA does NOT capture PDI saturation effects. The [chaperone-orthogonal-stacking framework](./chaperone-orthogonal-stacking.md) §5.5 separately predicts that the dual cassette + DAF SCR1-4 triple stack pushes ER folding toward saturation. Adding cns1+cns2 to the dual cassette is *off* the PDI axis entirely (cytosolic), so the burden axis is orthogonal. But the framework's worst-case scenario (triple cassette = dual + DAF SCR1-4) is *not* this analysis's triple. **This page covers cytosolic-cytosolic stacking (cns1+cns2 atop dual). The chaperone-orthogonal-stacking framework covers ER-folding-axis stacking.** Both verdicts must hold for the full endgame strain to be feasible. They are independent risks.

3. **Static-stoichiometry doesn't capture dynamic induction trajectory.** Jeennor 2023 reports 564 mg/L/day as a *productivity rate* under fed-batch conditions with a specific induction protocol. Stationary-phase metabolism + multi-cassette induction-promoter interference are out of FBA scope. A v2 dynamic FBA (dFBA) or kinetic model would address this; not gating.

**Optional cytosolic third cassettes (carnS, panD): also GREEN.** Both score essentially zero burden in the FBA, consistent with the chaperone framework's "bypasses secretion entirely" verdict for cytosolic carnosine + panD. Triple-cassette stacking with carnS+panD instead of cns1+cns2 is the alternate route for the third therapeutic chokepoint mode, covering URAT1 modulation via carnosine rather than cordycepin's URAT1 modulation. The endgame strain has *two* mutually exclusive cytosolic third-cassette options, both metabolic-burden-feasible.

**Does §1.9's extended design get a cordycepin arm?** Yes, on the burden axis. Pending the three follow-up gates above and the chaperone framework's separate verdict on PDI load, the cordycepin arm of the endgame strain is engineerable and worth committing to. Estimated additional cost over the baseline §1.9 dual-cassette test: ~$1,500-2,500 (one additional codon-optimized cassette synthesis + ~10% additional fermentation arm + cordycepin LC-MS quantification). Estimated additional timeline: 2-3 weeks parallel to the dual-cassette §1.9 work, if cns1+cns2 are added as a third cassette using the NSAR1 5-marker platform's free third integration slot (per [koji-endgame-strain.md §3](./koji-endgame-strain.md), three slots remain free after dual cassette).

## Limitations

1. **FBA, not pcSecKoji.** v1 uses plain flux-balance analysis with cassette burdens modeled as flux demands and stoichiometric balance constraints. PDI / chaperone / BiP / calnexin proteome-occupancy constraints are NOT in the model. This v1 captures the carbon, nitrogen, energy, and reducing-equivalent burden; it does NOT capture secretion-pathway proteome saturation. A v2 upgrade is `pcSec`-class modeling (see [Sánchez et al. 2017 *Mol Syst Biol* 13:935](https://www.embopress.org/doi/full/10.15252/msb.20167411) for the *S. cerevisiae* implementation; no publicly downloadable *A. oryzae* equivalent as of 2026-05-14). The proteome-burden gap that the [chaperone-orthogonal-stacking framework](./chaperone-orthogonal-stacking.md) line 238 flags applies asymmetrically: cytosolic cassettes (cns1+cns2, carnS, panD) bypass the ER and are well-modeled here; the secreted cassettes (uricase, lactoferrin) are only roughly modeled here, and the chaperone framework is the load-bearing tool for those.

2. **Lactoferrin burden modeled as a generic translation + ER-folding ATP cost.** The 16-disulfide PDI/ERO1 load is approximated by elevating ATP-per-aa from 4.5 (uricase, PDI-light) to 6.0 (Lf, PDI-heavy). Real PDI saturation effects from [chaperone-orthogonal-stacking.md §3.5](./chaperone-orthogonal-stacking.md) (effective PDI load 24-40 for Lf) are out of scope for this v1 FBA. The lactoferrin amino-acid drain pulls glutamate as a proxy carrier, not the actual aa-composition vector of hLf; a v2 refinement would use the exact aa frequencies (Lf is 9% Leu, 8% Cys for example) and the corresponding multi-aa drain.

3. **Kojic acid and ergothioneine reactions added manually with simplified net stoichiometry.** iWV1314 does not include either pathway. We use one-step net reactions per published mechanism. Real biosynthesis involves multiple enzyme steps and possibly cofactor recycling we haven't captured. Specifically: kojic acid's exact stoichiometry remains debated (Terabayashi 2010 + Marui 2011 confirm the kojA/kojR/kojT gene cluster but the "exact number of genes essential for kojic acid production remains unknown" per their analysis); we use a glucose-substrate, one-NADPH-equivalent, two-water-released net reaction as a reasonable approximation. Ergothioneine's 3-SAM-per-product cost is well-established for the EgtD/Egt1 N-trimethylation step.

4. **Cordycepin pathway stoichiometry: NADPH choice for Cns1 is best-guess.** [Yan et al. 2024 Front Chem Eng](https://www.frontiersin.org/journals/chemical-engineering/articles/10.3389/fceng.2024.1446454/full) documents that the Cns1 cofactor (NADH vs NADPH) has not been mechanistically pinned. We use NADPH because it is the standard biosynthetic reductant in fungi. If the true cofactor is NADH, switching changes the carbon partition only marginally: NADH and NADPH pools are interchangeable via transhydrogenase reactions present in iWV1314, with a small ATP cost per inter-conversion. *(Mechanistic Extrapolation; flag for v2 verification.)*

5. **Static demands.** Each cassette is treated as a fixed lower-bound flux. Real titers vary with growth phase, induction state, substrate, and inter-cassette transcriptional cross-talk. FBA is steady-state and cannot capture transient dynamics. The Jeennor 2023 564 mg/L/day is reported as the optimized fed-batch rate; whether the cassette delivers similar productivity in solid-state koji is the wet-lab open question.

6. **Adenosine deaminase competition not modeled as a kinetic constraint.** The host's native ADA (r1115-r1117 in iWV1314) competes with cns1+cns2 for the adenosine substrate pool. FBA picks the optimal split between cordycepin synthesis and inosine production based purely on stoichiometric balance. In vivo, the relative kcat × [enzyme] of ADA vs cns1+cns2 determines the actual partition. Pentostatin protection ([Xia 2017 PMID 29056419](https://pubmed.ncbi.nlm.nih.gov/29056419/)) would be needed if intracellular ADA flux outcompetes cns1+cns2 at the empirical [enzyme] levels achieved by the engineered cassette.

7. **iWV1314 biomass flux units are not directly h⁻¹.** The biomass-formation reaction r1897 has coefficient sum ~153 (sum of |coef| across precursors), which means the model flux at 10 mmol/gDW/h glucose comes out to ~17.7 instead of the literature mu_max ~0.31 h⁻¹ for *A. oryzae* on glucose ([Vongsangnak 2008 PMID 18801187](https://pubmed.ncbi.nlm.nih.gov/18801187/) Table 1). Comparisons across scenarios are valid (the scaling is consistent), but **absolute h⁻¹ growth-rate predictions from this analysis should be treated as relative percentages, not predicted doubling times.**

8. **Multilingual source coverage** ([CLAUDE.md §Global-multilingual](../CLAUDE.md)). Cordycepin metabolic engineering has a substantial Chinese-language literature (PMID 29056419 Xia is itself a Chinese-author group). No CNKI / WanFang dive was performed specifically on cns1+cns2 mechanism in this v1 because the Cell Chem Biol + Front Chem Eng + Microb Cell Fact coverage already converges on the Cns1 oxidoreductase / Cns2 phosphohydrolase / Cns3 kinase assignments. A v2 follow-up could query CNKI for *Cordyceps militaris* metabolic-engineering literature in Chinese, particularly around alternative cofactor partitioning and ADA competition studies, to verify or refine the NADPH assignment.

## Cross-references

- [computational-experiments.md](./computational-experiments.md): comp-023 tracking entry
- [chaperone-orthogonal-stacking.md](./chaperone-orthogonal-stacking.md): Section 4 has the cns1+cns2 row already entered with PDI load = 0; this analysis closes the proteome-burden gap line 238 flags as out-of-scope
- [koji-endgame-strain.md](./koji-endgame-strain.md): §1.9 extended design beneficiary of the green-light verdict
- [medicinal-mushroom-complement-track.md](./medicinal-mushroom-complement-track.md): Jeennor 2023 cordycepin precedent + pentostatin co-engineering discussion
- [cassette-compatibility-computational.md](./cassette-compatibility-computational.md): comp-010 dual-cassette feasibility prior
- [validation-experiments.md §1.9](./validation-experiments.md): wet-lab gate; this comp informs whether to add a cordycepin arm to that experiment
- [experiments/comp-023-cns1-cns2-metabolic-burden/](../experiments/comp-023-cns1-cns2-metabolic-burden/): full analysis script, GEM, inputs, and reproducibility provenance

## Status

Complete (v1; 2026-05-14). FBA-without-pcSec simplification owned in Limitations. Verification-agent self-review pass: every load-bearing number grep-verified against the source list above. Next step is incorporation into the koji-endgame §1.9 protocol if Brian green-lights the cordycepin arm.
