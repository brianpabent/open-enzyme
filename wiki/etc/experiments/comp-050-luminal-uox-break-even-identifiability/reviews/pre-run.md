PRE_RUN_GATE: GO
REVIEWED_SNAPSHOT: 05f0e0776644113abe8c70fc174b50d5b4253d43ae197cad5b76ca5dcc0a52d5

# Adversarial pre-run review — comp-050

## Reviewed snapshot

Reviewer: `/root/comp050_gate1_r5_20260728`, a fresh context-isolated Gate-1 subagent. Reviewed `pre-run.manifest.json` payload SHA-256 `05f0e0776644113abe8c70fc174b50d5b4253d43ae197cad5b76ca5dcc0a52d5`, comprising five design files and five prior-output baseline files. The manifest payload digest validated, and every recorded path, byte length, and file SHA-256 matched the files inspected. I completed the independent design inspection before reading the superseded receipts or inspecting the historical outputs for compatibility.

## Bottom-line verdict

This exact snapshot may run. The sole design change from the last accepted Gate-1 snapshot is that `write_csv()` now passes `lineterminator="\n"` to `csv.DictWriter`. The code diff changes only CSV record serialization from the module default CRLF to LF. It does not change field names or order, row construction, values, equations, exact arithmetic, ranks, checks, method statuses, or decision mappings.

The unchanged bounded design remains internally consistent. It derives a conditional capacity identity, supplies an exact concentration-only counterexample, and audits declared ideal observation combinations with exact rational row-space tests. Analytic success cannot establish a biological regime, assay validity, human dose, serum effect, topology, chassis, production sufficiency, safety, a globally minimal measurement set, or closure of H08.

## Question and model fit

The response surface follows from `R_capacity = Vmax_initial × T × occupancy × A_time` and `q × J_total_mean × T`, yielding `Vmax_initial / J_total_mean = q / (occupancy × A_time)` under fixed `C/Km` and the declared active-capacity time-area assumption. `J_total_mean` is explicitly `(I_systemic + I_other)/T`; it is not replaced by systemic-origin influx. The distinct systemic-attribution denominator remains `I_systemic` in `R_UOX,systemic/I_systemic`.

The exact steady-state constructions show that the same constant concentration trajectory can coexist with different UOX-attributed product-equivalent fluxes under the declared rate law. The separate linear audit asks whether scalar targets or every component of a grouped ledger target lie in the row space of the governing and observation equations. Direct labels are ideal observations, not proxies for assay validity, practical identifiability, or a physiological regime.

## Constraint and implementation audit

All load-bearing grid values enter through `Fraction(str(value))`. Occupancy, required capacity, counterexample fluxes and derivatives, extrema, Gaussian elimination, and augmented-rank tests use exact rational arithmetic; 12-significant-digit decimal fields are presentation only. Static substitution gives exact zero derivatives for all three counterexamples and distinct UOX-attributed fluxes.

The exact rational elimination operates on the declared ten-variable amount ledger. Static retracing gives cumulative ideal-product ranks `2`, `4`, `5`, and `10` and failed-product ranks `2`, `3`, `4`, and `8`. Grouped ledger closure requires each named ledger variable to be individually identifiable. In the complete ideal combination, the governing equation reconstructs `R_unattributed`; it is not directly observed. A future practical closure claim must additionally require that residual to satisfy a prespecified mass-balance tolerance.

The qualified product-equivalent observations are available only under the enumerated specificity, stoichiometry, background, recovery, fate, control, interference, and source-resolution prerequisites. The preregistered failure branch removes those observation rows, leaving total UOX removal confounded with the residual and systemic-origin UOX removal unconstrained. That branch must block local attribution, systemic attribution, and grouped ledger closure.

The design explicitly excludes dynamic substrate depletion, changing occupancy, uncalibrated oxygen/pH/access/matrix effects, practical assay error, residual-tolerance acceptance, peroxide safety, and human operating-regime inference. `biological_regime` is hard-coded to `NOT_EVALUATED`. These are visible boundaries of the formal question rather than hidden substitutions.

The current `write_csv()` change is serialization-only. The previous baselines contain CRLF-delimited CSV records; the proposed run will emit LF-delimited records. The unchanged row dictionaries and `fieldnames=list(rows[0])` preserve schema, ordering, values, and row counts. JSON and Markdown writers are untouched.

## Load-bearing pre-run table

| Planned claim or parameter | Artifact location | Intended implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Conditional capacity identity | `README.md`; `break_even_rows()` | Generates the dimensionless boundary | Exact algebra under fixed occupancy and `A_time`; no biological value imported | Pass |
| Total-local influx denominator | `README.md`; `response_surface.denominator`; results definitions | Normalizes the conditional capacity surface | Symbolic amount/flux convention; kept separate from systemic-source attribution | Pass |
| Exact surface arithmetic | `q()`; `break_even_rows()` | Computes occupancy and required capacity | Exact `Fraction` operations from fixed decimal strings | Pass |
| Constant-volume counterexample | `counterexample_rows()` | Demonstrates concentration-only non-identifiability | Constructed exact scenarios; derivative and diversity checks use fractions | Pass |
| Exact scalar and grouped rank tests | `matrix_rank()`; `target_test()` | Tests row-space membership and componentwise ledger closure | Exact rational Gaussian elimination | Pass |
| Algebraic residual reconstruction | mass-balance row; fourth ideal combination | Identifies `R_unattributed` structurally from the other terms | Exact formal implication; practical tolerance remains required | Pass |
| Qualified product-equivalent observations | product contract; conditional observation rows | Conditions total and systemic-source attribution | Ideal assumption only; prerequisites explicitly enumerated | Pass |
| Product-prerequisite failure branch | second `structural_audit()`; `identifiability_checks()` | Requires contrary non-attribution and non-closure results | Preregistered removal of conditional observation rows | Pass |
| CSV line terminator | `write_csv()` | Emits LF-only CSV files accepted by repository whitespace checks | Explicit standard-library serialization option; no computational path change | Pass |
| Biological and interpretive boundary | `method_statuses`; README; limitations | Prevents method success from becoming a biological or translational verdict | Always `NOT_EVALUATED`; prohibited inferences explicit | Pass |

## Falsification, sensitivity, and output contract

Contrary results can win. Any failed surface direction, absent `q = 1` boundary, nonzero counterexample derivative, identical counterexample UOX flux, unexpected target status, false ledger closure, or retained local/systemic attribution or ledger closure after product-observation removal prevents the success verdict.

The planned outputs retain exact and decimal surface values, exact counterexample fluxes and derivatives, unknown ordering, every coefficient matrix, base and augmented ranks, target statuses, failure-mode results, method checks, definitions, and limitations. The historical outputs match the current planned headers and top-level schema, but they are prior-run baselines only and do not authorize any outcome for this snapshot. The cumulative combinations are declared scenarios, not a global-minimality proof.

## Downstream authoring contract

`wiki/luminal-uox-break-even-identifiability-computational.md` is the planned canonical evidence home. After a clean Gate 2, the registry, H08, and validation §1.33 may receive only bounded links or local decision deltas supported by the conditional identity, exact counterexample, structural rank results, and ideal-observation limitations.

No outcome may identify a human regime, select a dose, predict serum urate, validate an assay, establish production sufficiency, rank a topology or chassis, infer peroxide safety, close H08, establish oral-UOX efficacy, or claim global measurement minimality. No cross-track comparison is planned. A negative result may narrow only the exact conditional-capacity or identifiability claim tested; adjacent delivery, sink, chassis, production, and safety conjectures remain outside this run. Reader-facing updates must not add editorial history, corpus-placement narration, personalized treatment instructions, or duplicated exposition.

## Required actions before execution

None.

## Review limits

This was static inspection only. I did not execute or import `analyze.py`, create outputs, or test runtime serialization. All five design files and five historical baseline files were available and matched the manifest. I inspected prior output headers, row counts, record terminators, and JSON/Markdown schema only for compatibility after completing the independent design assessment; prior values and receipts did not authorize the verdict. Assay validity, practical identifiability, biological operating conditions, deterministic double-run hashes for the repaired serializer, and downstream interpretations remain for authorized execution and a fresh Gate 2.
