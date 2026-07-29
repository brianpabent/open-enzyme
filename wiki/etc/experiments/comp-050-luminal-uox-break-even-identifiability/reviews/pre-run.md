PRE_RUN_GATE: GO
REVIEWED_SNAPSHOT: b6c92c4f9aec463fe5d79dea18bc3142e7d2c9c335e1a2bcb49c8116fa0701ca

# Adversarial pre-run review — comp-050

## Reviewed snapshot

Reviewer: `/root/comp050_gate1_r7_20260728`, a fresh context-isolated Gate-1 subagent. Reviewed the canonical `pre-run.manifest.json` payload SHA-256 `b6c92c4f9aec463fe5d79dea18bc3142e7d2c9c335e1a2bcb49c8116fa0701ca`, comprising five design files and five prior-output baseline files. I inspected all five design files completely and recorded the independent design findings before reading any historical output or prior receipt. Every manifest-bound design and baseline path, byte length, and file SHA-256 matched the file inspected, and an independent canonical JSON calculation reproduced the recorded manifest payload digest. The manifest matched the files inspected.

## Bottom-line verdict

This exact snapshot may run. The only manifest-bound design delta from the preceding Gate-1 snapshot is a README interface clarification that names the already-emitted product-failure status `STRUCTURALLY_IDENTIFIABLE_WITHOUT_PRODUCT_OBSERVATION` for non-product targets and states that it does not rescue local or systemic-origin UOX attribution. Version-control inspection showed no change to `analyze.py`, `model_contract.json`, provenance, query strategy, model equations, coefficient vectors, parameter grid, decision checks, output schema, or result mapping. The companion `A_time` definition added to the focused interpretive page is outside the pre-run manifest.

The README change brings the declared vocabulary into fidelity with the unchanged executable branch. It is documentation hardening, not a model, decision-rule, sensitivity-plan, implementation, or planned-output change. The bounded experiment remains safe to execute as a conditional dimensionless capacity map and exact structural-identifiability audit. It cannot identify a human operating regime, validate an assay, select a dose, predict serum urate, establish production sufficiency or peroxide safety, rank a topology or chassis, prove global measurement minimality, establish oral-UOX efficacy or inefficacy, or close H08.

## Question and model fit

The capacity question is answered by a conditional identity, not a hidden physiological proxy. With fixed `C/Km`, `occupancy = (C/Km)/(1 + C/Km)` and `A_time = integral(Vmax_active(t) dt)/(Vmax_initial × T)`, so `R_capacity = Vmax_initial × T × occupancy × A_time`. Setting this equal to `q × J_total_mean × T` yields `Vmax_initial/J_total_mean = q/(occupancy × A_time)`. The grid is explicitly dimensionless and scenario-defined; it neither fits nor inherits human parameters.

The denominator remains mean **total local** influx, `J_total_mean = (I_systemic + I_other)/T`. Systemic-source attribution is separately defined as `R_UOX,systemic/I_systemic` and requires source-resolved product fate. No total-local result is substituted for systemic-origin capture.

The exact steady-state counterexamples and the linear observation model answer distinct identifiability questions. The counterexamples show that one constant concentration trajectory can coexist with different UOX-removal fluxes under the declared rate law. The row-space audit asks whether each scalar target, or each named component of grouped local-ledger closure, is determined by the governing and ideal observation equations. Positive structural identifiability is not presented as practical identifiability, assay qualification, measurement precision, biological feasibility, or clinical effect.

## Constraint and implementation audit

The amount ledger is dimensionally coherent: influx and removal variables are integrated over the declared window, while `U_0` and `U_T` are endpoint inventories. The README requires measured volume and sampling/dilution correction before concentration is converted to amount. Contract and code use the same sign convention:

`U_T - U_0 = I_systemic + I_other - R_UOX - R_reabsorption - R_outflow - R_unattributed`.

All load-bearing numerical strings are converted to `Fraction`. Occupancy, capacity multiples, counterexample fluxes and derivatives, Gaussian elimination, and augmented-rank comparisons therefore use exact rational arithmetic; decimal fields are rendering only. Static substitution gives UOX fluxes `1/10`, `1/2`, and `9/10`, paired with non-UOX losses `9/10`, `1/2`, and `1/10`, so all three declared derivatives are exactly zero while UOX-attributed flux differs.

The exact ten-variable model contains initial and terminal inventory, two influxes, total UOX removal, reabsorption, outflow, unattributed residual loss, systemic-origin UOX removal, and integrated active capacity. Scalar targets are tested by target-vector row-space membership. The grouped `local_ledger_closed` target passes only when all eight named ledger components are individually identifiable.

The product-observation contract declares eight prerequisite names. `require_unique_strings()` rejects empty, non-string, empty-string, and duplicate entries; exact set equality against `EXPECTED_PRODUCT_PREREQUISITES` then rejects a missing prerequisite, substitution or misspelling, and any extra prerequisite. The guarded names cover analyte identity/specificity, stoichiometry, background/non-UOX formation, time-resolved recovery, product inventory/outflow/sampling/degradation/scavenging fate, controls, acceptance criteria, and source-resolved product fate for systemic attribution. This validates contract vocabulary only; it does not claim any assay has satisfied those prerequisites.

The product-failure branch removes both conditional product-observation rows and recomputes every rank. Non-product targets that remain identifiable are faithfully labeled `STRUCTURALLY_IDENTIFIABLE_WITHOUT_PRODUCT_OBSERVATION`. Local UOX removal remains confounded with the unattributed residual in every combination, systemic-origin UOX removal remains unconstrained, and grouped ledger closure fails. Dedicated checks require all three attribution/closure failures before `METHOD_MAP_DERIVED` is possible. The clarified status therefore cannot rescue UOX attribution.

In the final ideal combination, direct observations plus qualified total UOX removal make `R_unattributed` algebraically reconstructible through the mass-balance row; it is not directly observed. Practical closure remains separately contingent on a prespecified residual mass-balance tolerance. Dynamic substrate depletion, changing occupancy, oxygen, pH, matrix access, transport, residence, practical error, product recovery, residual acceptance, peroxide fate and tissue exposure, systemic compensation, and the human operating regime remain outside the computation.

## Load-bearing pre-run table

| Planned claim or parameter | Artifact location | Intended implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Conditional capacity identity | `README.md`; `break_even_rows()`; result equations | Derives the fixed-occupancy dimensionless capacity boundary | Exact symbolic identity under declared assumptions; no biological value imported | Pass |
| Mean total-local influx denominator | README amount convention; `response_surface.denominator`; result definitions | Normalizes initial capacity by `(I_systemic + I_other)/T` | Formal amount/flux convention, explicitly distinct from source attribution | Pass |
| Systemic-origin attribution target | README fraction definitions; target vector; result definitions | Tests only `R_UOX,systemic` under source-resolved fate observation | Formal target; no source-resolved assay is claimed | Pass |
| Response-surface grid and arithmetic | `model_contract.json`; `q()`; `break_even_rows()`; exact monotonicity checks | Emits the declared 120-row conditional surface | Constructed dimensionless scenarios and exact rational arithmetic | Pass |
| Same-concentration counterexamples | Contract scenarios; `counterexample_rows()` | Demonstrates concentration-only non-identifiability | Exact constructed examples, not biological measurements | Pass |
| Scalar and grouped target tests | Governing/observation rows; `matrix_rank()`; `target_test()` | Tests exact row-space membership and componentwise ledger closure | Exact rational linear algebra | Pass |
| Unattributed residual and tolerance boundary | Mass-balance equation; grouped closure target; README limitations | Allows algebraic residual reconstruction only in the complete ideal combination | Formal structural implication; practical acceptance requires a future prespecified tolerance | Pass |
| Qualified product observations | Product equations; conditional observation rows | Conditions total and systemic-origin UOX attribution | Ideal-assumption-only and explicitly not empirically evaluated | Pass |
| Exact eight-name prerequisite guard | `EXPECTED_PRODUCT_PREREQUISITES`; `load_contract()` | Rejects incomplete, substituted, duplicated, or expanded contracts | Executable schema guard; current contract exactly matches | Pass |
| Product-prerequisite failure branch | second `structural_audit()`; `identifiability_checks()` | Removes product observations and requires attribution/closure failure | Preregistered structural sensitivity, not an assay-failure probability model | Pass |
| Failure-branch status vocabulary | `structural_audit()`; README status list; baseline CSV/JSON schema | Distinguishes surviving non-product identifiability without rescuing UOX targets | README now exactly documents unchanged emitted status | Pass |
| Biological and translational boundary | README exclusions; provenance; method statuses; limitations | Prevents analytic success from becoming a biological verdict | `biological_regime` is always `NOT_EVALUATED`; forbidden inferences are explicit | Pass |

## Falsification, sensitivity, and output contract

Contrary method results can win. A schema or exact-prerequisite mismatch, failed surface monotonicity, missing `q = 1` boundary, nonzero counterexample derivative, identical counterexample UOX fluxes, failed preregistered ideal rank result, local or systemic attribution surviving product-observation removal, or grouped ledger closure surviving that failure branch forces `METHOD_FAILURE` or an explicit failed sensitivity status and prohibits scientific interpretation.

The planned outputs expose all surface inputs and exact/decimal results, all counterexample parameters and exact derivatives, unknown ordering, governing and observation equations, complete coefficient matrices, base and augmented ranks, per-target statuses in both product modes, separate method statuses, definitions, checks, limitations, and biological status `NOT_EVALUATED`. The README now declares all three per-target status values used by the unchanged implementation. The five existing outputs matched the manifest and were inspected only as historical schema/interface baselines; they do not authorize interpretation for this snapshot.

The dominant unknowns—time-varying occupancy, calibrated active-capacity behavior in an exact configuration, influxes and boundary fates, product recovery and fate, oxygen/access/residence limits, practical measurement error, residual tolerance, safety, and systemic compensation—remain unparameterized. Consequently the run can derive only the formal capacity boundary and structural observation map. The cumulative combinations are declared scenarios, not a global-minimality search.

## Downstream authoring contract

`wiki/luminal-uox-break-even-identifiability-computational.md` remains the planned canonical evidence home. It is outside the Gate-1 manifest; its new local `A_time` definition is a reader-facing documentation correction and does not alter the executable design. Only after a clean Gate 2 may `wiki/computational-experiments.md`, H08, and validation §1.33 carry compact local decision deltas supported by the exact artifact.

No downstream surface may map the grid to a human regime, select a dose, predict serum urate, validate an assay, establish production sufficiency, infer peroxide safety, rank a topology or chassis, claim global measurement minimality, establish oral-UOX efficacy or inefficacy, close H08, or treat algebraic residual reconstruction as practical closure without a prespecified tolerance. A negative result may narrow only the exact conditional-capacity or structural-identifiability claim tested. Adjacent catalysis, delivery, chassis, gut-sink, production, safety, and systemic-effect conjectures remain outside the run. No cross-track comparison is planned, and reader-facing updates must not add editorial history, corpus-placement narration, personalized treatment instructions, or duplicated long-form exposition.

## Required actions before execution

None.

## Review limits

This was static inspection only. I did not execute or import `analyze.py`, modify the model contract, or generate outputs. The exact guard behavior, status mapping, failure branch, rank method, and decision checks were established from source control flow and exact algebra; runtime behavior and deterministic double-run hashes remain for an authorized execution. All five design files and five historical output baselines were available. The focused interpretive page was inspected only to verify closure of the external documentation action and is not part of the pre-run manifest. Assay qualification, practical identifiability, biological operating conditions, residual acceptance, peroxide safety, systemic effect, execution reproducibility, and every proposed interpretation remain outside this Gate-1 verdict.
