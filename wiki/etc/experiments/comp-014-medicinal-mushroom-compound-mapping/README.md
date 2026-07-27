# comp-014 — Medicinal mushroom compound × chokepoint mapping

**Status:** Partial lead inventory. The former candidate rankings and Phase 6 occupancy/feasibility triage are invalid for decision use.

## Current question

Which compound/source/target records in this bounded fungal-natural-product artifact are worth rehydrating from primary sources for a polarity-, exposure-, and function-aware experiment?

The artifact does not represent all fungal natural products or the global literature. It cannot identify the best compound, species, producer, production route, delivery route, or chassis.

## What survives

- Raw and joined compound/source/target rows survive as search leads.
- Primary-source identifiers attached to a row survive as retrieval pointers, not as verification that the row's interpretation is correct.
- ADA, PINK1/mitophagy, urate transport, urate production, inflammasome, redox, and barrier-associated rows remain open nodes for source rehydration.
- Database absence survives only as a record of what the bounded query did not return.

Plant-origin compounds found in mushroom-associated queries are not fungal biosynthesis products unless a primary source establishes that provenance. Binding, expression, target prediction, and whole-animal phenotype are not interchangeable with direct mechanism-matched function.

## What does not survive

- Any candidate, potency, species, or production ranking.
- `PURSUE`, `DROP`, tier, readiness, highest-priority, highest-leverage, or viability labels.
- Nominal exposure, occupancy, dose-feasibility, clinical-risk, synergy, production, delivery, or chassis conclusions.
- Universal claims that a target is empty, a fungal antagonist does not exist, or a whole material cannot act.
- Component or target causality inferred from a formula, extract, expression result, database association, or phenotype alone.

The former Phase 6 script and outputs are removed from the live tree. Other legacy derived files remain evidence-retrieval aids only where they expose a source identifier or row; their ranks and narrative verdicts have no current authority. Git preserves the retired logic.

## Retained reproducible check

From this directory:

```bash
python3 scripts/scope_validate.py
```

The standard-library validator checks the current Phase 1 input structure and regenerates `outputs/scope-summary.md`. It does not reproduce the database pulls, later joins, rankings, or retired Phase 6.

`scripts/scope_validate.py` is the only runnable script retained in this directory. The old LOTUS pull/aggregation and target-mapping scripts are removed because their derived narratives are quarantined and their execution contract is not current.

## Retained artifact map

- `inputs/` records the bounded historical source, species, toxicity, and target scope.
- `outputs/scope-summary.md` is the only currently regenerated output.
- Other top-level `outputs/phase-*` files are historical snapshots and lead inventories.
- Raw source captures remain unchanged in `outputs/_chembl_raw/`, `outputs/_lotus_raw/`, `outputs/_npatlas_raw/`, and `outputs/_knapsack_raw/`.
- Historical lookup caches/intermediates remain unchanged in `outputs/_chembl_molecule_inchikey_cache.json`, `outputs/_knapsack_inchikey_cache.json`, and `outputs/_chokepoint_chembl_targets.json`.

The unchanged raw captures preserve the retrieved source payloads. They are not evidence that any derived fungal provenance, target mapping, rank, or verdict is correct.

## Lead-rehydration gate

Before any row can support a current claim or experiment:

1. verify exact material identity and producer/source provenance;
2. inspect the primary record and preserve target or endpoint, effect polarity, substrate, assay, species, and compartment;
3. distinguish direct function from binding, expression, prediction, or phenotype;
4. measure or justify free parent and metabolite exposure in the proposed compartment;
5. run mechanism-matched function with attribution, off-target, toxicity, barrier, and viability controls;
6. compare sourcing and delivery only after the biological gate passes.

A negative result kills only the tested material, exposure, endpoint, and route. It does not erase the source record or neighboring untested mechanisms.

## Current evidence home

[Medicinal mushroom compound mapping](../../../medicinal-mushroom-compound-mapping-computational.md) states the current evidence and decision boundary.
