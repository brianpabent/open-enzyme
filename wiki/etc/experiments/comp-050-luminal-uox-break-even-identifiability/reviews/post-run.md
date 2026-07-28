ACTION_REQUIRED: no
REVIEWED_SNAPSHOT: 1d44192f5181aa8c701b02248676a8d39d20a5db7994a2b714026aa080eaf08d

# Independent comp review — comp-050

## Reviewed snapshot

Reviewer: `/root/comp050_gate2_r4_20260728`, a fresh context-isolated authoring-time Gate-2 reviewer. The canonical payload digest computed from `post-run.manifest.json` is `1d44192f5181aa8c701b02248676a8d39d20a5db7994a2b714026aa080eaf08d`, matching its recorded digest and the supplied snapshot. All 22 entries matched their recorded paths, byte counts, and SHA-256 values and were inspected completely. Independent artifact, output, proposed-surface, and mechanism-search findings were recorded before earlier authoring reviews, the push receipt, or its queue action were read.

## Bottom-line verdict

**Clean with limitations.** The exact artifact is deterministic, internally valid, and correctly bounded to a conditional-capacity identity and structural-identifiability map. The hardened executable guard now requires the exact eight declared product-prerequisite names, including source-resolved product fate for systemic attribution. A disposable seven-item contract failed before any output mutation, while the committed eight-item contract ran twice and reproduced the unchanged five output hashes. This closes the exact push-review action without changing the model, outputs, scientific interpretation, or propagation. No material correction remains.

## Implementation and constraint closure

The capacity identity follows exactly from `R_capacity = Vmax_initial × T × occupancy × A_time`, `J_total_mean = (I_systemic + I_other)/T`, and `R_capacity = q × J_total_mean × T`, giving `Vmax_initial/J_total_mean = q/(occupancy × A_time)`. The response-surface denominator is mean **total local** urate influx. It remains separate from the systemic-source attribution denominator in `R_UOX,systemic/I_systemic`.

An independent exact-rational implementation reproduced all 120 surface rows, their fractions, and the declared-grid extrema `101/400` and `1010`. Those are grid-only extrema, not biological or global extrema. The three constant-volume counterexamples independently evaluate to `dC/dt = 0` with UOX-attributed fluxes `1/10`, `1/2`, and `9/10`; starting at the shared equilibrium therefore gives the same concentration trajectory with different UOX removal within the declared rate law.

Independent row reduction reproduced every coefficient matrix, all 48 target rows, every augmented-rank vector, ideal-product ranks `2/4/5/10`, and failed-product ranks `2/3/4/8`. In the final ideal combination, the mass-balance row plus observed inventories, source influxes, reabsorption, outflow, calibrated capacity, and qualified total/source-resolved product observations make `R_unattributed` algebraically reconstructible; it is not directly observed. Practical closure remains conditional on the reconstructed residual passing a prespecified mass-balance tolerance. Removing product observations after prerequisite failure leaves local UOX removal confounded with the residual and systemic-origin UOX removal unconstrained, correctly blocking local attribution, systemic attribution, and grouped ledger closure.

The guard first requires unique non-empty strings, then compares their set with the exact eight expected names. In a disposable copy, removing only `source_resolved_product_fate_for_systemic_attribution` produced exit code 1 with that name reported as missing; hashes, nanosecond mtimes, and sizes for all five pre-existing outputs remained unchanged. The committed eight-item contract ran twice with `METHOD_MAP_DERIVED`; both runs matched each other and the committed baselines:

- `break-even-surface.csv` — `9a6dd92ac07fb26e094c19f42ac782ecb7109f67840ea070efc0b05bd37b63ff`
- `measurement-identifiability.csv` — `712efdea7f5cc5c68ecf7597764c1184ee715a0c64f8e47adf500fd8fa26c2bf`
- `results.json` — `e23671522b4d4294c5bd09bdd7f76b0aaca4c5070e7f3b792583acf3a39ac6e2`
- `same-concentration-counterexamples.csv` — `8bbe8328515ccce51b2793a9dc836a7409a17a1e0b1a18520ffb03ca541530ef`
- `summary.md` — `4b130e45f5f0b862c905834e25fb0bd7bfa1a14f1b5409ae3e04c1adbe343fd5`

The product-equivalent branch remains conditional on analyte identity and specificity, validated stoichiometry, background and non-UOX formation, time-resolved recovery, complete product fate, matched controls, interference criteria, and source-resolved product fate. These are ideal assumptions, not assay validation. Dynamic substrate depletion, changing occupancy, oxygen/pH/access/matrix effects, transport, residence, practical precision, residual-tolerance acceptance, peroxide safety, systemic compensation, and a human operating regime remain outside the model. `biological_regime` remains `NOT_EVALUATED`.

## Summary-fidelity audit

README, contract, code, all five outputs, and all twelve proposed updates agree on the conditional identity, denominator separation, concentration counterexample, exact rank results, product-prerequisite failure branch, algebraic residual reconstruction, and limitations.

Residual wording remains closed across `wiki/computational-experiments.md`, `wiki/etc/GRAPH.md`, `wiki/gout-action-guide.md`, `wiki/gut-lumen-sink.md`, `wiki/luminal-uox-break-even-identifiability-computational.md`, `wiki/uricase.md`, and `wiki/validation-experiments.md`: each distinguishes algebraic reconstruction from direct measurement and requires a prespecified tolerance for practical closure. H08 and `wiki/open-questions.md` retain the unresolved residual-bound and data requirements.

Mechanism searches beyond explicit COMP references found no stale active claim. No artifact or reader-facing surface maps the grid to a biological regime, assay validity, human dose, serum-urate effect, topology or chassis winner, production sufficiency, peroxide or clinical safety, a globally minimal measurement set, oral-UOX efficacy, or H08 closure.

## Reader-facing ownership audit

The focused interpretive page owns the formal result, intestinal-disposal relevance, exposure constraints, limitations, and next discriminating measurements. Registry, graph, action-guide, multihop, hypothesis, and validation surfaces carry compact local routing deltas. Cross-track rankings remain outside the focused page. I found no narrative foil, editorial or sweep history, page-placement narration, personalized treatment instruction, or duplicated long-form exposition.

## Conjecture preservation audit

COMP-050 invalidates concentration-only attribution within the declared model and identifies which ideal observations make its formal targets structurally identifiable. It does not invalidate UOX catalysis, the gut-lumen sink, any topology, chassis, delivery route, production path, safety hypothesis, or a later systemic consequence. H08 remains open and measurement-blocked. No grounded adjacent conjecture was erased, and no conjecture was upgraded to a factual biological claim.

## Generated-output and proposed-update inventory

| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-050-luminal-uox-break-even-identifiability/README.md` | design | Yes | Formal question, residual rule, outputs, and exclusions agree. |
| `wiki/etc/experiments/comp-050-luminal-uox-break-even-identifiability/analyze.py` | design | Yes | Exact algebra/ranks pass; exact eight-name guard closes push action. |
| `wiki/etc/experiments/comp-050-luminal-uox-break-even-identifiability/inputs/model_contract.json` | design | Yes | Ten-variable ledger, observations, targets, and eight prerequisites match code. |
| `wiki/etc/experiments/comp-050-luminal-uox-break-even-identifiability/inputs/provenance.md` | design | Yes | Constructed scenarios are not represented as biological evidence. |
| `wiki/etc/experiments/comp-050-luminal-uox-break-even-identifiability/inputs/query-strategy.json` | design | Yes | Correctly records a formal run requiring no external search. |
| `wiki/etc/experiments/comp-050-luminal-uox-break-even-identifiability/outputs/break-even-surface.csv` | generated_output | Yes | 120 exact rows; hashes unchanged; extrema are grid-only. |
| `wiki/etc/experiments/comp-050-luminal-uox-break-even-identifiability/outputs/measurement-identifiability.csv` | generated_output | Yes | 48 rows; every base and augmented rank independently reproduced. |
| `wiki/etc/experiments/comp-050-luminal-uox-break-even-identifiability/outputs/results.json` | generated_output | Yes | Definitions, matrices, checks, statuses, and limits agree. |
| `wiki/etc/experiments/comp-050-luminal-uox-break-even-identifiability/outputs/same-concentration-counterexamples.csv` | generated_output | Yes | Three exact zero-derivative cases with distinct UOX fluxes. |
| `wiki/etc/experiments/comp-050-luminal-uox-break-even-identifiability/outputs/summary.md` | generated_output | Yes | Faithful method result with `NOT_EVALUATED` biology. |
| `index.md` | proposed_update | Yes | Compact discovery pointer; no quantitative or biological upgrade. |
| `wiki/computational-experiments.md` | proposed_update | Yes | Reconstructible residual and practical tolerance remain distinct. |
| `wiki/cross-validation.md` | proposed_update | Yes | Appropriate unranked threat-model routing. |
| `wiki/etc/GRAPH.md` | proposed_update | Yes | Algebraic residual reconstruction and tolerance are explicit. |
| `wiki/gout-action-guide.md` | proposed_update | Yes | Non-clinical measurement boundary; no dose or response prediction. |
| `wiki/gout-multihop-research-program.md` | proposed_update | Yes | Routes measurements without biological or ledger overclaim. |
| `wiki/gut-lumen-sink.md` | proposed_update | Yes | Measured terms, reconstructed residual, and tolerance are separated. |
| `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` | proposed_update | Yes | H08 remains open and the dynamic model remains data-blocked. |
| `wiki/luminal-uox-break-even-identifiability-computational.md` | proposed_update | Yes | Complete faithful result with grid-only extrema and exclusions. |
| `wiki/open-questions.md` | proposed_update | Yes | Residual-bound and later-model requirements remain unresolved. |
| `wiki/uricase.md` | proposed_update | Yes | Method map is not assay, biological, production, or safety evidence. |
| `wiki/validation-experiments.md` | proposed_update | Yes | §1.33 characterizes local performance; it does not close systemic attribution. |

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Exact eight-name prerequisite guard | `EXPECTED_PRODUCT_PREREQUISITES`; `load_contract()` | Rejects incomplete, substituted, duplicated, or extra contracts | Executable schema hardening; seven-item negative control failed before writes | Pass |
| `Vmax_initial/J_total_mean = q/(occupancy × A_time)` | README; code; surface CSV | Generates conditional surface | Exact symbolic algebra; no biological estimate | Pass |
| Total-local versus systemic-origin denominators | README; contract; results | Separates local capacity from source attribution | Explicit amount/flux definitions | Pass |
| 120 rows; extrema `101/400`, `1010` | Contract; CSV; results; focused page | Summarizes declared grid | Exact constructed grid only; no global or biological claim | Pass |
| Counterexample fluxes `1/10`, `1/2`, `9/10` | Contract; code; CSV | Demonstrates concentration-only non-identifiability | Exact constructed examples | Pass |
| Ideal ranks `2/4/5/10`; failed ranks `2/3/4/8` | Code; CSV; results | Determines target status | Independently reproduced exact rational ranks | Pass |
| `R_unattributed` reconstruction | Balance; final ideal matrix; surfaces | Completes structural target | Algebraic implication; practical tolerance remains required | Pass |
| Qualified product observations | Product contract; ideal/failed branches | Conditions attribution | Ideal assumption only; not empirically validated | Pass |
| Biological regime | Results; summary; proposed surfaces | Prevents method-to-biology promotion | Always `NOT_EVALUATED` | Pass |

## Affected wiki pages

- `index.md` — already consistent — discoverability only.
- `wiki/computational-experiments.md` — already consistent — structural and practical closure remain distinct.
- `wiki/cross-validation.md` — already consistent — no rank or biological verdict.
- `wiki/etc/GRAPH.md` — already consistent — residual is algebraically calculated.
- `wiki/gout-action-guide.md` — already consistent — no clinical, dose, or unqualified closure inference.
- `wiki/gout-multihop-research-program.md` — already consistent — routes the correct measurement classes.
- `wiki/gut-lumen-sink.md` — already consistent — measured terms, reconstructed residual, and tolerance are separated.
- `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` — already consistent — open and blocked on data.
- `wiki/luminal-uox-break-even-identifiability-computational.md` — already consistent — full result and boundaries are faithful.
- `wiki/open-questions.md` — already consistent — residual bound and later model remain open.
- `wiki/uricase.md` — already consistent — no assay, biology, production, or safety upgrade.
- `wiki/validation-experiments.md` — already consistent — §1.33 is local characterization, not systemic or practical closure.
- Mechanism-matched non-manifest pages — already consistent — no stale concentration-only attribution, direct-residual-measurement, or closure claim found.

## New connections or implications

None beyond the represented boundary. Product-qualification failure destroys attribution under this observation model but does not falsify UOX catalysis or the luminal-sink mechanism.

## Required actions

1. None.

## Review limits

No manifest entry was missing, unreadable, truncated, or uninspected. I executed the hardened analysis twice in a disposable copy as explicitly authorized, ran the seven-prerequisite negative control without output mutation, and independently reproduced the exact algebra and ranks. I did not validate a wet-lab assay, practical precision, biological operating regime, peroxide safety, systemic effect, or clinical efficacy. No load-bearing biological parameter is introduced, so no new primary biological-source verification is claimed. Earlier reviews and the push receipt were read only after independent artifact, output, surface, and mechanism-search findings were recorded; their sole required guard action is satisfied by the exact-name check and disposable tests.
