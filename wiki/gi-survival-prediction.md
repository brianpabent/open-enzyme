---
title: GI Tract Survival Profile of A. flavus Uricase for Oral Delivery
date: 2026-04-21
tags: ['uricase', 'A. flavus', 'gastrointestinal', 'pH stability', 'proteolysis', 'enzyme engineering', 'oral delivery']
status: analysis
related: ['engineered-yeast-uricase-proposal.md', 'blood-barrier-exploits.md', 'gout-deep-dive.md', 'nlrp3-exploit-map.md', 'protein-engineering-strategy.md', 'uricase-variant-selection.md', 'codon-optimization-expression-cassette.md', 'uricase.md']
sources: ['ALLN-346 trials', 'pancreatic enzyme literature', 'rasburicase pharmacology', 'ABCG2 transporter data', 'disulfide bond engineering 2025', 'bile salt proteolysis', 'yeast cell wall protection']
---

# GI Tract Survival Profile of A. flavus Uricase for Oral Delivery

## Executive Summary

This page scopes the variables that determine whether active *Aspergillus flavus* uricase reaches an intestinal reaction site. No validated survival fraction or oral dose is currently available. Acid exposure, proteolysis, refolding, formulation, topology, oxygen, substrate access, peroxide handling, and transit must be measured together rather than collapsed into a fixed survival percentage.

**Current implications:**
- Gastric acid, pepsin, intestinal proteases, and product processing are candidate activity-loss mechanisms.
- Enteric coating, protein engineering, and whole-cell delivery are competing protection hypotheses, not established survival multipliers.
- COMP-019's unconditional flat-dose classification is not robust to [COMP-044's](./gut-lumen-uricase-physiologic-regime-computational.md) tested substrate-occupancy and finite-window diagnostics.
- Jointly measure delivered active enzyme, local urate, oxygen, peroxide, access, topology, and persistence in [validation experiment 1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial).

---

## Evidence boundary

The current evidence supports a list of plausible loss mechanisms and protection strategies, not a numerical end-to-end survival estimate.

- **In Vitro:** purified-protein and simulated-fluid studies can measure loss under specified pH, protease, bile, temperature, and time conditions.
- **Animal Model:** oral uricase precedents establish that a gut-lumen approach can be tested in vivo, but their engineered proteins, formulations, activity levels, and host physiology do not supply a survival multiplier for *A. flavus* UOX in yeast or koji.
- **Mechanistic Extrapolation:** enteric protection, whole-cell encapsulation, secretion, intracellular retention, disulfide engineering, and other protein changes are competing hypotheses until compared under matched conditions.
- **Clinical Trial:** ALLN-346 provides bounded human evidence for a different engineered uricase product. It does not validate this enzyme, topology, chassis, formulation, or dose.

## Loss and access map

| Stage | Failure modes to measure | Required readout |
|---|---|---|
| Production and processing | low active expression, aggregation, oligomer disruption, heat or drying loss | total, soluble, and active UOX; oligomeric state; batch variance |
| Gastric exposure | acid inactivation, pepsin cleavage, formulation release | active UOX before and after the prespecified gastric challenge |
| Intestinal exposure | proteolysis, bile effects, incomplete release, time-dependent decay | active UOX time course in the intended topology and matrix |
| Reaction site | inadequate urate, oxygen, access, or persistence; peroxide accumulation | substrate removal, oxygen, H₂O₂, catalase/scavenger capacity, localization, viability |
| Translation | reabsorption and whole-body clearance can decouple local reaction from serum effect | separately reviewed in-vivo design; no serum mapping from this page |

## Matched experimental matrix

At minimum, compare wild-type UOX and each engineered candidate in:

1. purified or cell-free form;
2. intracellular whole-cell form;
3. secreted or extracellular form when technically available;
4. the intended processed formulation;
5. controls without UOX and controls without the proposed protection feature.

Predeclare the challenge sequence, pH, protease and bile composition, temperature, exposure time, sampling points, activity assay, normalization basis, replicates, and decision rule. Report retained active IU after each stage. Do not multiply separately estimated survival fractions across compartments.

## Decision rule

A protection or engineering strategy advances only if it reproducibly improves retained active UOX through the complete intended challenge sequence without unacceptable losses in baseline activity, expression, release, viability, or peroxide control.

A positive survival result does not establish:

- a sufficient human dose or product serving;
- oral bioavailability;
- a serum-urate effect;
- superiority of yeast, koji, free enzyme, or another chassis;
- safety at the reaction site.

COMP-019's unconditional flat-dose classification is not robust to [COMP-044's](./gut-lumen-uricase-physiologic-regime-computational.md) tested substrate-occupancy and finite-window diagnostics. COMP-044 supplies no replacement ΔSUA, dose, genotype order, physiological regime, efficacy model, topology/chassis selection, production-sufficiency target, or safety conclusion. [Validation experiment 1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial) owns the configuration-level substrate × oxygen × peroxide test.
## References

[[1]](#ref1) RCSB PDB 1WS2. Urate oxidase from *Aspergillus flavus* complexed with 5,6-diaminouracil. UniProtKB Q00511. *In Vitro.*

[[2]](#ref2) Structural dissection of alkaline-denatured pepsin. *PMC*, PMC2323848. Pepsin activity as a function of pH and digestion time on caseins and egg white proteins. *Food & Function*, 2021. *In Vitro.*

[[3]](#ref3) Stability and functional consequences of disulfide bond engineering in *Aspergillus flavus* uricase. *Scientific Reports*, 2025. PMC12106716. *In Vitro.*

[[4]](#ref4) Ontogeny of human gastric lipase and pepsin activities. *Gastroenterology*, 1995. Pancreatic lipase is susceptible to proteolysis by pepsin. *PMC*, PMC5205606. *In Vitro.*

[[5]](#ref5) The bile salt content of human bile impacts on simulated intestinal proteolysis of β-lactoglobulin. *Scientific Reports*, 2021. Bile salts enhance the susceptibility of peach allergenic protein to gastrointestinal proteolysis. *Scientific Reports*, 2023. Bile salts act as effective protein-unfolding agents. *PNAS*, 2014. *In Vitro.*

[[6]](#ref6) First verification of human small intestinal uric acid secretion and effect of ABCG2 polymorphisms. *Journal of Translational Medicine*, 2025. Baseline uric acid concentrations: 105.3 pg/µL (100% functional ABCG2), 70.1 pg/µL (50% functional). *Clinical Trial.*

[[7]](#ref7) Extra-renal elimination of uric acid via intestinal efflux transporter BCRP/ABCG2. *PLOS One*, 2011. Two-thirds renal excretion, one-third intestinal (ABCG2-mediated). *Established.*

[[8]](#ref8) Oral treatment with an engineered uricase, ALLN-346, reduces hyperuricemia and uricosuria in urate oxidase-deficient mice. *Frontiers in Medicine*, 2020. *Animal Model.* ALLN-346 Study 201 (NCT04987242) was completed with actual enrollment 16; the published abstract reports the first 11 participants and no concurrent urate-lowering therapy. Study 202 (NCT04987294) enrolled 19, was terminated for company financing, and has no posted results. *Clinical Trial records; the two studies do not supply one combined outcome.*

[[9]](#ref9) Cell wall component of *Saccharomyces cerevisiae* as a novel wall material for encapsulation of probiotics. *ScienceDirect*, 2017. Probiotic bacteria encapsulated with S. cerevisiae cell wall components showed higher survival in simulated GIT. *In Vitro.*

[[10]](#ref10) Effect of yeast cell wall supplementation on intestinal integrity, digestive enzyme activity and immune traits of broilers. *PubMed*, 2021. Modulation of intestinal inflammation by yeasts and cell wall extracts. *PubMed*, 2012. *Animal Model / In Vitro.*

[[11]](#ref11) Functional inclusion bodies produced in the yeast *Pichia pastoris*. *Microbial Cell Factories*, 2016. Inclusion bodies retain biological activity, resist proteolysis, and penetrate mammalian cells. *In Vitro.*

---
