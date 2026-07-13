---
title: "Gout Multihop Research Program"
date: 2026-07-13
tags:
  - gout
  - research-program
  - multihop
  - uricase
  - abcg2
  - nlrp3
  - microbiome
related:
  - gut-lumen-sink
  - uricase-topology-oxygen-peroxide-design-computational
  - staged-purine-sink-mass-balance-computational
  - validation-experiments
sources:
  - "Corpus-wide connection audit, 2026-07-13"
---

# Gout Multihop Research Program

**Status:** Phase 0 research map. These are testable threads, not treatment recommendations.

The corpus-wide audit found that the highest-value gaps are not additional single-target
inhibitors. They are **interfaces between compartments**: precursor versus urate, epithelial
transport versus inflammation, oxygen versus peroxide, microbial carbon fate versus host
signaling, and preventive urate lowering versus flare resolution.

## Three immediate corrections

1. **The old oral-UOX dose regime is invalid.** [comp-019](./uricase-abcg2-genotype-stratification-computational.md)
   converted flat enzyme mass into catalytic capacity without physiological substrate,
   oxygen, access, survival, or transit constraints. [comp-044](./gut-lumen-uricase-physiologic-regime-computational.md)
   retires its ΔSUA, genotype-ranking, flat-dose, and “yield is solved” conclusions.
2. **UOX topology and peroxide handling cannot be separated.** Intracellular catalase directly
   co-localizes only with intracellular UOX. PULSE supports three topologies plus joint
   KatG+VHb, but does not identify the human-optimal architecture. [comp-045](./uricase-topology-oxygen-peroxide-design-computational.md)
   defines the factorial.
3. **Dietary precursor and endogenous luminal urate are different ledgers.** A whole-cell
   nucleoside-salvage stage and UOX/PDB urate stages cannot be added as independent ΔSUA
   effects. [comp-046](./staged-purine-sink-mass-balance-computational.md) conserves both pools
   and shows that staging can help or hurt across the design grid.

## Research threads

| Thread | Multihop connection | Evidence boundary | Decisive next test |
|---|---|---|---|
| Physiologic UOX regime | human jejunal urate → oxygen/transit/access → topology → peroxide | Direct human substrate measurement + rodent/in-vitro engineering precedents; human efficacy unknown | [1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial) |
| Staged precursor sink | dietary nucleosides → whole-cell salvage → urate appearance → UOX/PDB | Each stage has precedent; ordering and net host flux are untested | [1.34](./validation-experiments.md#134-isotope-resolved-dietary-precursor--uox--pdb-sequential-flux) |
| Enterocyte tissue paradox | NLRP3 inhibition → PDZK1/ABCG2 trafficking → intestinal urate export | Direct intestinal-cell link exists; candidate-specific direction unknown | [1.35](./validation-experiments.md#135-enterocyte-nlrp3pdzk1abcg2-tissue-paradox-assay) |
| Redox double edge | remove luminal urate antioxidant → generate UOX H2O2 → epithelial redox injury | Biochemical mechanism established; therapeutic window unmeasured | [1.36](./validation-experiments.md#136-luminal-urate-antioxidant-loss--uox-h2o2-safety-assay) |
| PDB self-niche | reductive urate carbon fate → butyrate or other products → colonocyte O2 consumption → anaerobe persistence | Full-pathway anaerobe supports carbon fate; CBT2.0 output unresolved | [1.37](./validation-experiments.md#137-cbt20-carbon-fate-and-pdb-self-niche-test) |
| OMV gut-to-blood bridge | T0SS cargo loading → OMV epithelial transfer → active systemic UOX | Mouse/ex-vivo transport precedent; UOX cargo, safety, and activity untested | [1.38](./validation-experiments.md#138-t0ss-uox-omv-gut-to-systemic-bridge-assay) |
| Fructose feed-forward loop | KHK/ATP depletion → urate/ROS → intestinal ABCG2 suppression → less gut excretion | Rat ileum/cell evidence plus canonical hepatic fructolysis; human causal chain open | [1.39](./validation-experiments.md#139-fructose--khk--nox--abcg2-human-enteroid-test) |
| Purinergic resolution | extracellular ATP → CD39/CD73 → adenosine → inflammasome resolution; ADA changes both precursor and signal | Acute-gout mechanistic precedent; timing and urate tradeoff unknown | [1.40](./validation-experiments.md#140-cd39cd73adenosine-gout-resolution-time-course) |
| Bile-acid bridge | FXR → ABCG2 and TGR5 → NLRP3, conditioned by microbial bile acids | Separate arms supported; joint human-gout phenotype untested | [1.41](./validation-experiments.md#141-parallel-fxrabcg2-and-tgr5nlrp3-bile-acid-screen) |
| Succinate bifurcation | hepatocyte succinate → AMPD2/urate while immune succinate → SUCNR1/NLRP3 | Human gout metabolomics + animal/cell mechanism; compartment dominance unknown | [1.42](./validation-experiments.md#142-succinate-compartment-dissociation-hepatic-ampd2-vs-immune-sucnr1) |
| Drug–microbe compatibility | PDB enzymes/salvage × allopurinol/oxypurinol/febuxostat → altered microbial efficacy or metabolite exposure | No direct compatibility dataset identified | [1.43](./validation-experiments.md#143-pdb--allopurinoloxypurinolfebuxostat-interaction-assay) |

## Program order

Run 1.33 and 1.34 first: they decide whether the core sink architecture and staging logic
survive realistic chemistry. Run 1.35 and 1.36 before combining anti-inflammatory or redox
modules with UOX. Run 1.37 before attributing butyrate-mediated host effects to CBT2.0. The
remaining screens are parallel discovery branches whose positive results can change product
architecture rather than merely add another ingredient.

Negative results are useful. They can eliminate a topology, separate prevention from flare
resolution, or show that a seemingly additive stack closes the intestinal urate gate it
depends on.
