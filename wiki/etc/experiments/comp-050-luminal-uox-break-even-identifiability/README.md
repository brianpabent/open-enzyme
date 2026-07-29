# comp-050 — Luminal UOX break-even and measurement-identifiability map

**Lifecycle rule:** Execute only when the current exact pre-run receipt says `PRE_RUN_GATE: GO`. Interpret or propagate outputs only when the current exact post-run receipt says `ACTION_REQUIRED: no`.

## Question

Can a conditional luminal-UOX capacity boundary and an exact structural-identifiability audit show which measurement combinations are sufficient to reconstruct local UOX removal, close a local urate ledger, or attribute UOX removal to systemic-origin urate—without substituting inherited scenario values for human physiological parameters?

## Decision this COMP may inform

This COMP may:

- derive a dimensionless boundary between initial active UOX capacity and mean total local urate influx under explicit fixed-occupancy and active-capacity assumptions;
- demonstrate whether the same luminal-urate concentration trajectory can conceal different UOX-removal fluxes;
- determine, from an explicit linear observation model, which targets are structurally identifiable under each declared ideal measurement combination;
- show how failure of the product-attribution prerequisites changes the structural result; and
- separate measurements that characterize local configuration performance from those needed for local ledger closure and systemic-source attribution.

It may not identify the human operating regime, select a dose, predict serum urate, rank a topology or chassis, establish production sufficiency, infer peroxide safety, or claim that oral UOX is effective or ineffective. It does not claim that any measurement combination is globally minimal.

## Amount and flux convention

All ledger variables are **amounts integrated over one declared window** of duration `T`, except the initial and terminal urate inventories:

```text
U_T - U_0 = I_systemic + I_other
            - R_UOX
            - R_reabsorption
            - R_outflow
            - R_unattributed
```

- `U_0` and `U_T` are initial and terminal luminal urate amounts. Concentration observations require measured compartment volume and correction for sampling or dilution before conversion to amount.
- `I_systemic` and `I_other` are window-integrated systemic-origin and other urate influxes.
- `R_UOX`, `R_reabsorption`, and `R_outflow` are window-integrated removal terms.
- `R_unattributed` is an explicit residual-loss term. A practical ledger is not considered closed merely because this algebraic residual can be calculated; its acceptance bound must be prespecified in the eventual experiment.
- `J_total_mean = (I_systemic + I_other) / T` is the mean **total local influx** used by the conditional capacity boundary.

The local UOX gross-removal fraction is:

```text
F_local_gross = R_UOX / (I_systemic + I_other)
```

This is not systemic-source capture. The systemic-origin UOX-removal fraction is:

```text
F_systemic_attributed = R_UOX,systemic / I_systemic
```

and is structurally available only when source-resolved tracer or equivalent fate measurements observe `R_UOX,systemic`. Neither fraction is a serum-effect prediction. Changes in inventory and competing losses remain explicit ledger terms.

## Conditional capacity boundary

For the response surface only, the analysis holds `C/Km` fixed over the window and defines:

```text
occupancy = (C/Km) / (1 + C/Km)
A_time = integral(Vmax_active(t) dt) / (Vmax_initial * T)
R_capacity = Vmax_initial * T * occupancy * A_time
```

The initial active-capacity multiple required for a declared gross-removal target `q` relative to mean total local influx is:

```text
Vmax_initial / J_total_mean = q / (occupancy * A_time)
```

`q = 1` is the conditional point at which integrated UOX capacity equals total local urate influx over the window. It is not a closed mass-balance result: actual removal can also depend on substrate depletion, competing fates, changing occupancy, volume, and initial/final inventory. Lower `q` rows are descriptive engineering slices, not clinical targets. Every grid level is dimensionless and is neither a biological distribution nor a probability.

Mapping `A_time` to data requires a calibrated reaction-site `Vmax_active(t)` time course for the exact configuration. Active-enzyme abundance or a dissolved-oxygen trace alone is insufficient. Oxygen, pH, access, and matrix effects must either be incorporated into the calibrated capacity measurement or represented in a later rate law.

## Product-equivalent observation contract

`P_eq` is a reconstructed cumulative UOX-attributed urate-consumption equivalent. The ideal observation used by the structural audit is:

```text
R_UOX = P_eq
R_UOX,systemic = P_eq,systemic

P_eq = (
    delta_product_inventory
    + recovered_product_outflow
    + recovered_product_sampling
    + quantified_product_degradation_or_scavenging
    - non_UOX_product_formation
) / (validated_stoichiometric_yield * validated_matrix_recovery)
```

`P_eq,systemic` applies the same corrected product-fate equation to a
source-resolved tracer or an equivalent observation that distinguishes product
formed from systemic-origin urate.

This equation is available only if the exact assay establishes all of the following:

1. analyte identity and UOX-product specificity;
2. stoichiometric conversion to urate-consumption equivalents;
3. initial/background product and non-UOX formation;
4. time-resolved matrix recovery;
5. product inventory, outflow, sampling, degradation, and scavenging fate;
6. no-UOX or inactive-UOX, no-urate, and matrix controls; and
7. prespecified recovery, mass-balance, and interference acceptance criteria;
   and
8. for systemic-source attribution, source-resolved product fate rather than
   source-resolved influx alone.

COMP-050 assumes these conditions only for an **ideal structural-identifiability scenario**; it does not claim that an assay has passed them. The code reruns the audit with the product observation removed. In that failure scenario, local UOX removal must report `NOT_IDENTIFIABLE`.

## Structural counterexample

The design includes three exact steady-state parameterizations of:

```text
dC/dt = J_total - Vmax * C/(Km + C) - k_non_UOX * C
```

All use constant volume and the same `C`, `Km`, and `J_total`, and all produce `dC/dt = 0`, but their UOX-attributed product-equivalent fluxes differ. Starting at equilibrium therefore gives the same concentration trajectory with different UOX removal. This is a mathematical counterexample, not a patient or assay model.

## Implemented structural-identifiability audit

`inputs/model_contract.json` defines:

- the unknown integrated inventories and fluxes;
- the mass-balance equation;
- each measurement combination as direct ideal observations;
- product-equivalent observations that depend on the assay prerequisites; and
- target coefficient vectors.

The code constructs an exact rational coefficient matrix for each measurement combination. A scalar target is structurally identifiable only when its coefficient vector lies in the row space of the governing and observation equations. A grouped target such as local-ledger closure passes only when every named ledger component is individually identifiable.

The cumulative combinations are:

1. **Terminal urate amount only:** observes `U_T`; local UOX removal is not identifiable.
2. **Initial/terminal urate plus qualified UOX-product equivalent:** conditionally identifies `R_UOX` under the product observation contract, but not total influx, ledger closure, or systemic-source attribution.
3. **Add calibrated reaction-site capacity:** also identifies the integrated active-capacity term used to connect the exact configuration to the conditional boundary; it still does not close the urate ledger.
4. **Add source and boundary-fate measurements:** observes both influxes, reabsorption, and outflow, while qualified source-resolved product fate conditionally observes systemic-origin UOX removal. Under the ideal observation assumptions, the remaining unattributed residual is structurally reconstructible and the declared ledger terms are identifiable. A future practical closure rule must additionally require that residual to fall within a prespecified mass-balance tolerance.

These are declared cumulative combinations, not a proof of global minimality. Outputs expose every equation, matrix rank, target-rank test, and unresolved target. A product-control failure scenario removes the conditional product observation before recomputing the ranks.

## Inputs and result branches

The response-surface values and algebraic counterexamples are dimensionless design scenarios. No biological parameter distribution is fitted. Derived surface values are emitted as exact reduced fractions plus 12-significant-digit decimal renderings; monotonicity checks use the exact fractions.

The output reports separate statuses:

- `conditional_capacity_algebra`: derived or method failure;
- `concentration_only_nonidentifiability`: demonstrated or method failure;
- `measurement_structural_audit`: completed or method failure;
- per measurement combination and target: `STRUCTURALLY_IDENTIFIABLE_UNDER_IDEAL_OBSERVATION` or `NOT_IDENTIFIABLE`;
- in the product-prerequisite-failure branch, a target that remains identifiable without any product-derived observation: `STRUCTURALLY_IDENTIFIABLE_WITHOUT_PRODUCT_OBSERVATION`; this status does not rescue local or systemic-origin UOX attribution;
- product-prerequisite failure sensitivity: must make local UOX removal `NOT_IDENTIFIABLE`; and
- `biological_regime`: always `NOT_EVALUATED`.

The overall method verdict is `METHOD_MAP_DERIVED` only if schema, algebra, counterexample, rank, and failure-sensitivity checks pass. Any failed method check yields `METHOD_FAILURE` and permits no scientific interpretation. Analytic success never certifies an assay, a biological operating regime, or systemic effect.

## Planned outputs

- `outputs/results.json` — contract digest, definitions, equations, separate method statuses, rank diagnostics, prerequisite sensitivity, and limitations.
- `outputs/break-even-surface.csv` — complete conditional dimensionless capacity surface.
- `outputs/same-concentration-counterexamples.csv` — exact parameterizations with the same concentration trajectory and different UOX-attributed flux.
- `outputs/measurement-identifiability.csv` — per-combination, per-target rank result.
- `outputs/summary.md` — concise human-readable result.

## Reproduce after Gate 1

Requires CPython 3.11 or newer. From the repository root:

```bash
python3 wiki/etc/experiments/comp-050-luminal-uox-break-even-identifiability/analyze.py
```

The implementation uses only the Python standard library, writes UTF-8 with stable ordering, and contains no randomness or external calls. Run it twice and compare every output hash before Gate 2.

## Planned downstream authoring

If Gate 2 passes:

- `wiki/luminal-uox-break-even-identifiability-computational.md` will own the complete result and limitations;
- `wiki/computational-experiments.md` will receive a compact registry entry;
- `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` will distinguish this pre-data structural map from the still-blocked measured dynamic model; and
- `wiki/validation-experiments.md` §1.33 will receive only the local-versus-systemic measurement boundary.

No result can close H08, select a chassis, establish a dose, or replace the measured dynamic model. No open-question entry is planned unless Gate 2 identifies a distinct unresolved routing action.
