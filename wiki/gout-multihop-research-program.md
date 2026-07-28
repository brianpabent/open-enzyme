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
---

# Gout Multihop Research Program

**Status:** Phase 0 research map. These are testable threads, not treatment recommendations.

The highest-value open questions include **interfaces between compartments**: precursor versus urate, epithelial
transport versus inflammation, oxygen versus peroxide, microbial carbon fate versus host
signaling, and preventive urate lowering versus flare resolution.

## Three immediate evidence boundaries

1. **The old oral-UOX flat-dose classification is not robust.** [comp-019](./uricase-abcg2-genotype-stratification-computational.md)
   converted flat enzyme mass into catalytic capacity without physiological substrate,
   oxygen, access, survival, or transit constraints. [comp-044](./gut-lumen-uricase-physiologic-regime-computational.md)
   found that the unconditional classification did not survive its tested substrate-occupancy
   and finite-window diagnostics. It did not identify the true physiological regime or reverse
   the old conclusion, so comp-019's ΔSUA, genotype ranking, dose, and yield claims cannot guide decisions.
   [comp-050](./luminal-uox-break-even-identifiability-computational.md) then shows why urate
   concentration alone cannot identify UOX removal and separates qualified product fate,
   calibrated reaction-site capacity, source influx, and boundary-fate measurements.
2. **UOX topology and peroxide handling cannot be separated.** Intracellular catalase directly
   co-localizes only with intracellular UOX. PULSE supports three topologies plus joint
   KatG+VHb, but does not identify the human-optimal architecture. [comp-045](./uricase-topology-oxygen-peroxide-design-computational.md)
   generates a blocked candidate layout and contains no biological topology verdict.
3. **Dietary precursor and endogenous luminal urate require different accounting structures.** A whole-cell
   nucleoside-salvage stage and UOX/PDB urate stages cannot be added as independent ΔSUA
   effects. [comp-046](./staged-purine-sink-mass-balance-computational.md) conserves the dietary
   precursor ledger and separately compares endogenous capture architectures; staging can help
   or hurt across the design grid.

## Research threads

| Thread | Multihop connection | Evidence boundary | Decisive next test |
|---|---|---|---|
| Physiologic UOX regime | exact configuration → qualified product fate + calibrated reaction-site capacity → source/boundary-fate ledger → oxygen/transit/access → peroxide | Direct human substrate measurement + rodent/in-vitro engineering precedents; human efficacy unknown | Build and characterize exact configurations in the relevant construct-supply work (§§1.1, 1.2, and 1.5) or use an exact external configuration, then run [1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial) and collect the [comp-050](./luminal-uox-break-even-identifiability-computational.md) ledger inputs before dynamic modeling |
| Staged precursor sink | dietary nucleosides → whole-cell salvage → urate appearance → UOX/PDB | Each stage has precedent; ordering and net host flux are untested | [1.34](./validation-experiments.md#134-isotope-resolved-dietary-precursor--uox--pdb-sequential-flux) |
| Enterocyte tissue paradox | NLRP3 inhibition → PDZK1/ABCG2 trafficking → intestinal urate export | Direct intestinal-cell link exists; candidate-specific direction unknown | [1.35](./validation-experiments.md#135-enterocyte-nlrp3pdzk1abcg2-tissue-paradox-assay) |
| Redox double edge | remove luminal urate antioxidant → generate UOX H2O2 → epithelial redox injury | Biochemical mechanism established; therapeutic window unmeasured | [1.36](./validation-experiments.md#136-luminal-urate-antioxidant-loss--uox-h2o2-safety-assay) before animal escalation |
| PDB self-niche | reductive urate carbon fate → butyrate or other products → colonocyte O2 consumption → anaerobe persistence | Full-pathway anaerobe supports carbon fate; CBT2.0 output unresolved | [1.37](./validation-experiments.md#137-cbt20-carbon-fate-and-pdb-self-niche-test) |
| OMV gut-to-blood bridge | T0SS cargo loading → OMV epithelial transfer → active systemic UOX | Mouse/ex-vivo transport precedent; UOX cargo, safety, and activity untested | [1.38](./validation-experiments.md#138-t0ss-uox-omv-gut-to-systemic-bridge-assay) |
| Fructose feed-forward loop | KHK/ATP depletion → urate/ROS → intestinal ABCG2 suppression → less gut excretion | Rat ileum/cell evidence plus canonical hepatic fructolysis; human causal chain open | [1.39](./validation-experiments.md#139-fructose--khk--nox--abcg2-human-enteroid-test) |
| Purinergic resolution | extracellular ATP → CD39/CD73 → adenosine → inflammasome resolution; ADA changes both precursor and signal | Acute-gout mechanistic precedent; timing and urate tradeoff unknown | [1.40](./validation-experiments.md#140-cd39cd73adenosine-gout-resolution-time-course) |
| Bile-acid bridge | FXR → ABCG2 and TGR5 → NLRP3, conditioned by microbial bile acids | Separate arms supported; joint human-gout phenotype untested | [1.41](./validation-experiments.md#141-parallel-fxrabcg2-and-tgr5nlrp3-bile-acid-screen) |
| Succinate bifurcation | hepatocyte succinate → AMPD2/urate while immune succinate → SUCNR1/NLRP3 | Human gout metabolomics + animal/cell mechanism; compartment dominance unknown | [1.42](./validation-experiments.md#142-succinate-compartment-dissociation-hepatic-ampd2-vs-immune-sucnr1) |
| Drug–microbe compatibility | PDB enzymes/salvage × allopurinol/oxypurinol/febuxostat → altered microbial efficacy or metabolite exposure | No direct compatibility dataset identified | [1.43](./validation-experiments.md#143-pdb--allopurinoloxypurinolfebuxostat-interaction-assay) |

## Program order

Build and characterize the exact UOX configurations in the relevant construct-supply work
(§§1.1, 1.2, and 1.5) or use an exact external configuration before §1.33. Within a controlled host, §1.33 may nominate a topology;
cross-host results remain configuration-specific. Run §1.36 before animal escalation. Run 1.34
to test the staging logic, 1.35 before combining anti-inflammatory modules with UOX, and 1.37
before attributing butyrate-mediated host effects to CBT2.0. The
remaining screens are parallel discovery branches whose positive results can change product
architecture rather than merely add another ingredient.

Within the koji track, §1.9A lactoferrin-only may run opportunistically in parallel with the
§1.5 build and §1.33 screen when NSlD-ΔP10 access is available. Freeze §1.9B UOX-only only
after §1.33 advances an exact §1.5-built koji configuration, and enter §1.9C dual-cassette only after both single-cassette arms
pass. This preserves lab-access momentum without spending the full dual-cassette budget on an
unselected UOX architecture.

Negative results are useful. They can eliminate a topology, separate prevention from flare
resolution, or show that a seemingly additive stack closes the intestinal urate gate it
depends on.
