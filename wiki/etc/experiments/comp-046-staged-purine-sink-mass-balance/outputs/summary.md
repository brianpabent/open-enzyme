# comp-046 summary — dietary fate ledger + endogenous capture comparison

**Verdict: TWO CONDITIONAL HYPOTHESES, NOT ONE ADDITIVE EFFICACY CLAIM.** Whole-cell GR-5 helps the conserved dietary fate ledger only if cleavage is coupled to enough microbial salvage/retention or reduced base absorption. Spatial UOX→PDB staging changes the separate endogenous capture fraction only under favorable residual transfer. The two structures are not summed into ΔSUA.

The analysis contains two independent discrete full-factorials: **81 dietary cases** and **81 endogenous architecture cases**. Occupancy is not biological probability.

## Dietary purine-precursor ledger

Central ledger (100 normalized dietary purine units):

| Fate | Units |
|---|---:|
| unintercepted_nucleoside_absorbed | 36.250 |
| unintercepted_nucleoside_unabsorbed | 13.750 |
| microbial_salvage_or_retention | 22.500 |
| liberated_base_absorbed | 18.941 |
| liberated_base_unabsorbed | 8.559 |

Across the selected grid, whole-cell GR-5 changes absorbed precursor by a median reduction of **0.181 relative to the matched untreated absorbed precursor** (5th–95th percentile -0.042–0.724). In 0.111 of grid cells it increases absorbed precursor. These are design-space occupancies, not incidence estimates.

## Endogenous luminal-urate capture-fraction comparison

| Architecture | Median captured fraction | 5th–95th percentile |
|---|---:|---:|
| Well-mixed/overlapping | 0.800 | 0.062–0.843 |
| Spatially staged | 0.584 | 0.081–0.904 |

Staging is greater in 57/81 grid cells, well-mixed access is greater in 24/81, and they are equal in 0/81. Median staged-minus-well-mixed capture is 0.010; it is not assumed positive.

**Boundary:** staging wins only when `uox + (1-uox) × transfer × pdb` exceeds the overlap-adjusted well-mixed capture equation documented in the artifact.

## Experimental consequence

Use isotope-resolved dietary flux to measure nucleosides, free bases, microbial biomass incorporation, and transepithelial transfer. Separately, use a sequential microoxic→anoxic urate reactor to measure UOX capture, residual transfer, PDB capture, every pathway product, and viability. Do not infer joint three-stage complementarity or additivity by combining the two structures.

## Limitations

- Grid occupancy is not probability; levels are deliberately broad design cases.
- The GR-5 stage represents whole-cell cleavage plus salvage/retention, not DeoD causality alone.
- Dietary precursor and endogenous luminal urate are separate accounting structures and are not summed (dietary = conserved 100-unit fate ledger; endogenous = capture-fraction architecture comparison, NOT a conserved ledger -- endogenous_luminal_urate_units is stored but unused).
- Architecture equations are hypotheses requiring measured kinetics, overlap, transfer loss, residence time, and PDB viability.
- The model omits microbial turnover and re-release, cross-feeding, renal compensation, inflammation, colonization, and serum-urate dynamics.
