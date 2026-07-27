---
title: "Medicinal Mushroom Compound × Gout Chokepoint Mapping (comp-014)"
date: 2026-05-06
tags:
  - medicinal-mushrooms
  - fungi
  - natural-products
  - chokepoint-mapping
  - computational
related:
  - computational-experiments.md
  - modality-chokepoint-matrix.md
  - tcm-modern-rigor-intersection.md
  - nlrp3-exploit-map.md
  - abcg2-modulators.md
  - validation-experiments.md
status: partial-lead-inventory
---

# Medicinal mushroom compound × gout chokepoint mapping

Fungal natural products may expose gout weaknesses across urate production, renal or intestinal transport, inflammasome signaling, and adjacent inflammatory pathways. COMP-014 attempted a broad compound-to-target map so those leads could be found before selecting a delivery or production route.

## Verdict

The retained artifact is a partial lead inventory, not a comprehensive fungal natural-product map and not a candidate ranking.

It combines manually seeded source-species records with partial LOTUS, NPAtlas, KNApSAcK, and ChEMBL coverage. Species provenance is uneven, assay types are heterogeneous, target-effect polarity is not consistently adjudicated, and absence from the queried databases is not evidence of biological inactivity.

The former Phase 6 occupancy and feasibility triage is retired. Its script and outputs have been removed from the live tree. No `PURSUE`, `DROP`, viability, dose, clinical-exposure, production-route, synergy, or chassis decision survives from that phase.

## What survives

The source/compound/target rows remain search leads that can be re-read against their primary records. The historical candidate set includes fungal-source or fungal-associated records at:

- urate production and renal or intestinal transport;
- NLRP3, caspase-1, IL-1β, and TNF-related inflammatory nodes;
- ADA and other purine-catabolism nodes;
- PPARγ, Nrf2/KEAP1, and adjacent barrier or stress-response nodes.

These categories do not establish favorable direction, physiological exposure, target attribution, or useful function. Plant-origin compounds found in mushroom-associated records must not be relabeled as products of fungal biosynthesis without direct source evidence.

## Evidence needed for any named lead

Before a compound, extract, or species can be prioritized, preserve:

- exact chemical or material identity;
- source species and whether the compound is synthesized, accumulated from substrate, or merely query-associated;
- primary source and verified location;
- target, substrate, assay system, effect polarity, and evidence level;
- direct function rather than binding or expression alone;
- free parent and metabolite exposure in the relevant compartment;
- off-target, toxicity, barrier-integrity, and viability data;
- reproducible production or extraction yield only after the biological gate passes.

For ABCG2, a drug-substrate interaction or expression change is not an intestinal urate-flux result. For a formula or whole extract, the whole-material phenotype does not establish which component caused it.

## Sourcing and delivery

Delivery is lead-specific:

- a defined small molecule may favor synthesis, purification, or formulation;
- a native fungal metabolite may favor controlled cultivation and extraction;
- a polysaccharide or whole extract requires composition and batch-release assays;
- heterologous expression becomes relevant only when it solves a demonstrated yield, stability, or localization constraint.

The fact that a lead is fungal-associated does not make a mushroom, koji, or engineered chassis the default route.

## Discriminating workflow

1. Rehydrate a lead from the primary source and verify material, source attribution, polarity, assay, and evidence level.
2. Measure or justify free exposure in the compartment where the mechanism is proposed.
3. Run the mechanism-matched functional assay with attribution and safety controls.
4. Compare sourcing and delivery routes only for leads that survive the biological gate.
5. Treat a negative result as local to the tested material, exposure, endpoint, and route.

## Artifact

- [COMP-014 directory](./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/)
- [Phase 2 unified table](./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/phase-2-unified-fungal-compounds.json)
- [Phase 3 target mapping](./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/phase-3-compound-x-target.json)
- [Phase 4 intersection](./etc/experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/phase-4-chokepoint-intersection-v2.json)

The artifact may nominate a record for primary review. It cannot establish efficacy, safety, dose, ranking, or delivery.
