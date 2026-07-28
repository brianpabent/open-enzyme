PRE_RUN_GATE: GO
REVIEWED_SNAPSHOT: b4170647352adbc8b289a4d858485021ff8344cf8709c1b9098797abc3356808

# Adversarial pre-run review — comp-050

## Reviewed snapshot

Reviewer: `/root/comp050_gate1_r6_20260728`, a fresh context-isolated Gate-1 subagent. Reviewed `pre-run.manifest.json` payload SHA-256 `b4170647352adbc8b289a4d858485021ff8344cf8709c1b9098797abc3356808`, comprising five design files and five prior-output baseline files. Every manifest-bound design path, byte length, and file SHA-256 matched the files inspected. I inspected all five design files completely and recorded the independent design findings before reading the historical outputs or prior receipts; those prior artifacts were used only for schema compatibility and closure of the previously reported guard action. The manifest matched the files inspected.

## Bottom-line verdict

This exact snapshot may run. The only design delta from source commit `2a32fddd3520c0278aa83a8a064854040ef9ddb5` replaces the permissive `len(prerequisites) < 7` check with exact set equality against the eight declared prerequisite names, including `source_resolved_product_fate_for_systemic_attribution`.

`require_unique_strings()` first rejects an empty list, non-string or empty entries, and duplicates. The subsequent set-equality check then rejects every seven-item subset, any same-length substitution or misspelling, and any extra name, reporting sorted missing and unexpected names. The committed eight-name contract equals the expected set. Therefore the hardening closes the prior implementation defect without changing the current contract, model, surface grid, arithmetic, coefficient matrices, target definitions, ranks, method checks, result schema, or decision mapping. It validates only the executable contract vocabulary; it neither tests nor implies that a product assay has satisfied any prerequisite.

The unchanged bounded experiment remains decision-useful as a conditional-capacity and exact structural-identifiability map. It cannot identify a biological operating regime, validate an assay, select a dose, predict serum urate, establish production or peroxide safety, rank a topology or chassis, prove a globally minimal measurement set, establish oral-UOX efficacy, or close H08.

## Question and model fit

The response-surface question is answered by the declared conditional identity. With fixed `C/Km`, `occupancy = (C/Km)/(1 + C/Km)` and `A_time = integral(Vmax_active(t) dt)/(Vmax_initial × T)`, so `R_capacity = Vmax_initial × T × occupancy × A_time`. Equating that capacity to `q × J_total_mean × T` yields `Vmax_initial/J_total_mean = q/(occupancy × A_time)`. This is a dimensionless capacity boundary, not a solved dynamic mass balance or biological parameter estimate.

The denominator is consistently mean **total local** urate influx, `J_total_mean = (I_systemic + I_other)/T`. The distinct systemic-source attribution target remains `R_UOX,systemic/I_systemic`; neither the code nor planned summaries substitute total-local capture for systemic-origin capture.

The concentration counterexample and the linear observation audit answer separate identifiability questions. The former constructs identical constant concentration trajectories with different UOX-attributed fluxes under one declared rate law. The latter asks whether each scalar target, or every component of the grouped ledger target, lies in the exact row space of the governing and ideal observation equations. Direct-observation labels, qualified product equivalents, and calibrated capacity are explicitly ideal observations rather than proxies for practical precision, assay qualification, or human physiology.

## Constraint and implementation audit

The ledger uses window-integrated amounts for influxes and removals and initial/terminal amounts for inventory. The README requires measured volume plus sampling/dilution correction before concentrations are converted to amounts. The mass-balance signs in the contract and coefficient vector agree with `U_T - U_0 = I_systemic + I_other - R_UOX - R_reabsorption - R_outflow - R_unattributed`.

All load-bearing numeric strings pass through `Fraction`, and occupancy, capacity multiples, counterexample fluxes and derivatives, Gaussian elimination, and augmented-rank tests use exact rational arithmetic. Decimal fields are presentation-only. Static substitution in the three counterexamples gives UOX fluxes `1/10`, `1/2`, and `9/10`; their corresponding non-UOX losses are `9/10`, `1/2`, and `1/10`, so every derivative is exactly zero while UOX-attributed flux differs.

The rank implementation performs exact Gauss-Jordan elimination over the ten declared unknowns. The cumulative ideal combinations have the previously exposed ranks `2`, `4`, `5`, and `10`; the aggregate product-failure combinations have ranks `2`, `3`, `4`, and `8`. In the final ideal combination, inventories, both source influxes, reabsorption, outflow, qualified total UOX removal, source-resolved UOX removal, and calibrated active capacity are observed. The governing equation then makes `R_unattributed` algebraically reconstructible. It is not directly measured, and practical closure still requires the eventual experiment to prespecify and satisfy a mass-balance tolerance.

The qualified product equations remain conditional on specificity, stoichiometry, background/non-UOX formation, time-resolved recovery, product inventory/outflow/sampling/degradation/scavenging fate, controls, interference acceptance, and source-resolved product fate for systemic attribution. The declared aggregate failure sensitivity removes both conditional product-observation rows. Local UOX removal then remains confounded with the unattributed residual, systemic-origin UOX removal remains unconstrained, and grouped ledger closure fails. This is a conservative structural failure case, not a per-prerequisite assay simulation.

Dynamic substrate depletion, changing occupancy, finite-volume dynamics beyond the amount ledger, uncalibrated oxygen/pH/access/matrix effects, transport and residence constraints, practical assay error, residual-tolerance acceptance, peroxide generation/scavenging and tissue exposure, systemic compensation, and a human operating regime remain outside the computation. The outputs hard-code `biological_regime` as `NOT_EVALUATED` and retain these exclusions.

## Load-bearing pre-run table

| Planned claim or parameter | Artifact location | Intended implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Conditional capacity identity | `README.md`; `break_even_rows()`; result equations | Generates the dimensionless capacity boundary | Exact symbolic algebra under fixed occupancy and `A_time`; no biological parameter imported | Pass |
| Total-local influx denominator | README amount convention; `response_surface.denominator`; result definitions | Normalizes initial capacity by `(I_systemic + I_other)/T` | Declared formal amount/flux convention; separate from systemic attribution | Pass |
| Systemic-source denominator | README fraction definitions; result definitions | Bounds `R_UOX,systemic/I_systemic` to source-resolved fate | Formal target requiring source-resolved product fate | Pass |
| Exact response-surface arithmetic | `q()`; `break_even_rows()`; monotonicity checks | Computes occupancy and required-capacity rows | Exact `Fraction` operations on fixed dimensionless design levels | Pass |
| Same-concentration counterexamples | Contract scenarios; `counterexample_rows()` | Demonstrates concentration-only non-identifiability | Constructed exact scenarios, not biological measurements | Pass |
| Scalar and grouped identifiability tests | Governing/observation rows; `matrix_rank()`; `target_test()` | Tests row-space membership and componentwise ledger closure | Exact rational linear algebra | Pass |
| Unattributed residual | Mass-balance row; final ideal combination; grouped target | Algebraically reconstructs the remaining ledger term | Formal implication only; direct measurement is not claimed and practical tolerance remains required | Pass |
| Qualified product observations | Product equations and eight prerequisite names; conditional rows | Conditions total and systemic-origin UOX attribution | Ideal-assumption-only; no empirical assay validation | Pass |
| Exact prerequisite-name guard | `EXPECTED_PRODUCT_PREREQUISITES`; `load_contract()` | Rejects incomplete, substituted, duplicated, or extra prerequisite contracts | Internal executable schema hardening; current eight-name contract matches exactly | Pass |
| Aggregate product-failure branch | second `structural_audit()`; `identifiability_checks()` | Requires non-attribution and non-closure when product observations are removed | Preregistered structural sensitivity; not a wet-lab failure-rate model | Pass |
| Biological and translational boundary | README exclusions; method statuses; limitations | Prevents analytic success from becoming a biological verdict | `biological_regime` always `NOT_EVALUATED`; forbidden inferences explicit | Pass |

## Falsification, sensitivity, and output contract

Contrary method results can win. A failed surface monotonicity check, missing `q = 1` boundary, nonzero counterexample derivative, identical counterexample UOX fluxes, failed preregistered rank-status check, retained local/systemic attribution after product-observation removal, or retained grouped ledger closure in that branch prevents `METHOD_MAP_DERIVED`.

The planned outputs expose all 120 surface rows with exact and decimal values, every counterexample parameter and exact derivative, the complete unknown ordering and coefficient matrices, base and augmented ranks for all targets, ideal and product-failure statuses, separate method statuses, definitions, checks, limitations, and `NOT_EVALUATED` biological status. The five existing outputs retain the planned schema and are historical baselines only; they do not authorize a result for this snapshot.

The dominant biological uncertainties—actual occupancy dynamics, calibrated active-capacity decay, local influxes and boundary fates, product recovery and fate, oxygen/access/residence constraints, practical error, residual acceptance, and systemic compensation—are intentionally not assigned inherited values. Consequently this run can derive only the formal boundary and structural observation map. The cumulative measurement combinations are declared scenarios, not a global-minimality search.

## Downstream authoring contract

`wiki/luminal-uox-break-even-identifiability-computational.md` is the planned canonical evidence home. Only after a clean Gate 2 may `wiki/computational-experiments.md`, H08, and validation §1.33 receive compact local decision deltas supported by the conditional identity, counterexample, exact rank results, product-prerequisite sensitivity, and explicit limitations.

No downstream surface may map the design grid to a human regime, select a dose, predict serum urate, validate a product assay, establish production sufficiency, infer peroxide safety, rank a topology or chassis, claim global measurement minimality, establish oral-UOX efficacy or inefficacy, or close H08. No cross-track comparison is planned. A negative result can narrow only the exact conditional-capacity or structural-identifiability claim tested; adjacent UOX catalysis, delivery, chassis, gut-sink, production, safety, and systemic-effect conjectures remain outside the run. Reader-facing updates must not add editorial history, corpus-placement narration, personalized treatment instructions, or duplicated long-form exposition.

## Required actions before execution

None.

## Review limits

This was static inspection only. I did not execute or import `analyze.py`, mutate the input contract, or generate outputs. Exact guard behavior was established from the unique-string validation and set-equality control flow; runtime rejection messages remain to ordinary authorized execution. All five design files and five historical output baselines were available. Assay qualification, practical identifiability, biological operating conditions, residual acceptance, peroxide safety, systemic effect, deterministic double-run output hashes for this hardened snapshot, and all proposed interpretations remain for authorized execution and a fresh Gate 2.
