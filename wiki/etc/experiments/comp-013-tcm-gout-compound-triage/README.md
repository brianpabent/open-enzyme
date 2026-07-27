> **INVALIDATED TOMBSTONE — NOT RUNNABLE.** No rank, viability verdict, exposure estimate, risk tier, or advancement decision survives. Git preserves the retired artifact; the live tree does not.

# comp-013 — TCM gout compound triage

**Status:** Invalidated for biological and decision use.

## What survives

- The nine named compounds and their source materials remain an unranked historical lead inventory for primary-source re-review.
- Si Miao San and other traditional-formula connections remain research leads. Formula-level evidence does not identify which component caused an effect.
- Sparse database coverage remains a search limitation, not evidence that an unrepresented compound is inactive.

## What is invalidated

The former rank order, composite scores, confidence tiers, `GUT-LUMINAL VIABLE`, `MODERATE`, and `MECHANISM UNCLEAR` verdicts are withdrawn. The same applies to nominal gut-lumen and plasma concentrations, occupancy ratios, Hill-equation percent inhibition, risk labels, dose feasibility, formulation direction, and clinical or safety implications.

The model reused COMP-004's invalid nominal-concentration/drug-substrate-IC50 shortcut, adapted COMP-007's invalid composite score, failed to preserve whether a target effect was favorable or adverse, and mixed direct assays, expression changes, animal phenotypes, and off-target signals as if they were comparable evidence.

## Hash-bound retirement record

[`invalidation.json`](./invalidation.json) binds every retired non-review file to Git commit `e0419bb0125fe57e1e20200c411cb03825555ea8` by byte count and SHA-256. It records the exact invalidated and surviving scopes.

Any renewed triage must be a new COMP built from primary evidence records that preserve material, source, target or endpoint, effect polarity, assay system, evidence level, measured free exposure, and mechanism-matched function. It must not infer viability from nominal concentration divided by IC50.

## Current evidence home

- [TCM gout leads — invalidated prior and mixed-source evidence rebuild](../../../tcm-gout-compound-triage-computational.md)
