ACTION_REQUIRED: no
REVIEWED_SNAPSHOT: bef2dca5044a7e5a49a6f8d8ac08c3d919e291aa5b0877973e30b09a8207ff10

# Independent comp review — comp-050

## Reviewed snapshot

Reviewer: `/root/comp050_gate2_r5_20260728`, a fresh context-isolated authoring-time Gate-2 reviewer. I reviewed the post-run manifest payload digest `bef2dca5044a7e5a49a6f8d8ac08c3d919e291aa5b0877973e30b09a8207ff10`. All 22 manifest entries matched their declared byte lengths and file SHA-256 values and were inspected completely. I recorded the independent artifact, output, proposed-surface, and mechanism-search findings before opening the earlier authoring receipts or push-review receipt. The manifest matched the files inspected.

## Bottom-line verdict

**Clean with limitations.** The exact artifact correctly derives a conditional dimensionless capacity identity, supplies a valid same-concentration counterexample, and performs the declared exact structural-identifiability audit. It does not substitute those formal results for a human operating regime, practical identifiability, assay validation, efficacy, dose, production, topology, chassis, or safety evidence.

The two documentation/interface actions from the fully covered push review are closed. The focused page now defines `A_time = ∫Vmax_active(t)dt / (Vmax_initial × T)` locally as a dimensionless retained active-capacity time area and explicitly says it is not an enzyme-abundance or oxygen proxy. The README now declares `STRUCTURALLY_IDENTIFIABLE_WITHOUT_PRODUCT_OBSERVATION` for targets that remain identifiable in the failed-product branch and explicitly says that this status does not rescue local or systemic-origin UOX attribution. No new ambiguity or required action remains.

## Implementation and constraint closure

The capacity identity follows from `R_capacity = Vmax_initial × T × occupancy × A_time`, fixed `occupancy = (C/Km)/(1 + C/Km)`, and `R_capacity = q × J_total_mean × T`, yielding `Vmax_initial/J_total_mean = q/(occupancy × A_time)`. The denominator is mean **total local** influx, `(I_systemic + I_other)/T`, not systemic-origin influx. Systemic attribution remains the separate target `R_UOX,systemic/I_systemic` and requires source-resolved product fate.

The contract-to-code trace is complete. Every surface value enters exact `Fraction` arithmetic. An independent exact-rational reconstruction reproduced all 120 surface rows, the exact fractions, monotonic directions, and grid extrema `101/400` and `1010`. Those extrema are declared-grid boundaries only. The three constructed counterexamples independently balance to `dC/dt = 0` with UOX fluxes `1/10`, `1/2`, and `9/10`; starting at the shared equilibrium therefore gives the same concentration trajectory with different UOX removal under the declared constant-volume rate law.

The ten unknowns, governing mass-balance signs, four cumulative measurement combinations, six targets, direct observations, conditional observations, coefficient matrices, base ranks, augmented ranks, and grouped-ledger rule agree across contract, code, CSV, and JSON. A separate elimination implementation reproduced all 48 per-target rows and statuses. The exact eight-name prerequisite guard uses uniqueness plus set equality: the committed contract and a reordered equivalent passed, while missing, extra, and duplicate-name mutation tests failed before output generation.

The failed-product branch removes both product-derived observation rows. Inventory change, measured active capacity, and—at the final combination—total local influx can remain structurally identifiable and are accurately labeled `STRUCTURALLY_IDENTIFIABLE_WITHOUT_PRODUCT_OBSERVATION`. Local UOX removal remains confounded with the unattributed residual in every combination, systemic-origin UOX removal remains unconstrained, and grouped ledger closure fails. The new vocabulary therefore cannot be read as salvaging UOX attribution.

In the complete ideal combination, qualified total UOX removal plus the other direct ledger observations makes `R_unattributed` algebraically reconstructible. This is not practical closure: README, results, summary, focused page, and dependents consistently require a future prespecified residual mass-balance tolerance. No numeric tolerance is invented by this formal COMP.

Reaction-site substrate, oxygen, localization, access, matrix effects, time-varying occupancy, finite replenishment, residence, recovery precision, oxidative coproduct and H2O2 fate, scavenging, epithelial exposure, and systemic compensation are not silently represented by `Vmax_initial`, `A_time`, or the identifiability matrices. They are explicitly excluded or assigned to later exact-configuration and safety work. The qualified product-equivalent equation covers identity, stoichiometry, background/non-UOX formation, recovery, inventory/outflow/sampling/degradation/scavenging fate, controls, acceptance criteria, and source-resolved product fate as ideal prerequisites; it does not claim that an assay has passed them.

The documented root command ran twice under the authorized review. Both runs returned `METHOD_MAP_DERIVED`; all five output SHA-256 hashes were unchanged before run 1, after run 1, and after run 2.

## Summary-fidelity audit

README, all five generated outputs, the focused page, registry, dashboard, H08, validation §1.33, gut-lumen mechanism page, uricase page, open questions, action guide, multihop program, cross-validation, and graph agree on the narrow result. They distinguish total-local removal from systemic-origin capture; retain `biological_regime: NOT_EVALUATED`; keep H08 open; require qualified product fate and calibrated reaction-site capacity for local configuration characterization; require source/boundary fates and residual tolerance for later ledger closure; and preserve peroxide/safety gates.

No surface upgrades the formal grid into a biological distribution, treats grid extrema as planning values, claims global measurement minimality, infers serum effect, selects a dose or production target, ranks a topology/chassis, validates a product assay, or turns structural into practical identifiability. Repository searches found no parser or consumer that restricts the failed-product branch to the prior two-value vocabulary.

## Reader-facing ownership audit

The focused computational page owns the full result, units, measurement table, product-qualification boundary, limitations, falsification direction, and reproducible links. Mechanism and hypothesis pages carry compact local consequences. The dashboard and computational registry remain routing surfaces rather than duplicating the result. Validation §1.33 uses COMP-050 only to harden the local measurement contract and explicitly defers complete ledger and systemic attribution.

No cross-track ranking, narrative foil, editorial or phase-history residue, personalized treatment instruction, production recommendation, or duplicated long exposition was introduced.

## Conjecture preservation audit

COMP-050 invalidates only inference from concentration alone and the named unqualified observation routes within its declared formal model. It does not kill H08, oral luminal UOX generally, any exact sequence/host/topology, ABCG2 stratification as a prospective question, UOX/PDB staging, other UOX delivery routes, or the possibility that a future qualified assay can resolve source fate. Those ideas remain bounded by exact-configuration activity, product qualification, source/boundary-fate, practical precision, residual-tolerance, redox, and translation gates. No grounded adjacent conjecture was erased or upgraded to fact.

## Generated-output and proposed-update inventory

| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-050-luminal-uox-break-even-identifiability/README.md` | design | Yes | Complete formal contract; both interface actions closed. |
| `wiki/etc/experiments/comp-050-luminal-uox-break-even-identifiability/analyze.py` | design | Yes | Exact arithmetic, rank logic, guard, failure branch, and output mapping pass. |
| `wiki/etc/experiments/comp-050-luminal-uox-break-even-identifiability/inputs/model_contract.json` | design | Yes | Grid, ledger, observations, targets, and exact eight-name prerequisite set are coherent. |
| `wiki/etc/experiments/comp-050-luminal-uox-break-even-identifiability/inputs/provenance.md` | design | Yes | Correctly limits inputs to formal scenarios and repository decision context. |
| `wiki/etc/experiments/comp-050-luminal-uox-break-even-identifiability/inputs/query-strategy.json` | design | Yes | External search is appropriately unnecessary for the result-bearing formal derivation. |
| `wiki/etc/experiments/comp-050-luminal-uox-break-even-identifiability/outputs/break-even-surface.csv` | generated_output | Yes | All 120 exact rows independently reproduced. |
| `wiki/etc/experiments/comp-050-luminal-uox-break-even-identifiability/outputs/measurement-identifiability.csv` | generated_output | Yes | All 48 ranks, augmented ranks, and statuses independently reproduced. |
| `wiki/etc/experiments/comp-050-luminal-uox-break-even-identifiability/outputs/results.json` | generated_output | Yes | Complete matrices, checks, definitions, statuses, and limitations match code and CSVs. |
| `wiki/etc/experiments/comp-050-luminal-uox-break-even-identifiability/outputs/same-concentration-counterexamples.csv` | generated_output | Yes | All three exact steady-state balances independently reproduced. |
| `wiki/etc/experiments/comp-050-luminal-uox-break-even-identifiability/outputs/summary.md` | generated_output | Yes | Faithful and appropriately bounded. |
| `index.md` | proposed_update | Yes | Compact discoverability entry; no overclaim. |
| `wiki/computational-experiments.md` | proposed_update | Yes | Registry matches the formal result and residual boundary. |
| `wiki/cross-validation.md` | proposed_update | Yes | Treats qualified attribution and operating regime as live risks. |
| `wiki/etc/GRAPH.md` | proposed_update | Yes | Dependency edge preserves empirical closure and safety sequencing. |
| `wiki/gout-action-guide.md` | proposed_update | Yes | Research-only routing; no dose, treatment, or efficacy claim. |
| `wiki/gout-multihop-research-program.md` | proposed_update | Yes | Uses COMP-050 as a measurement boundary, not biological evidence. |
| `wiki/gut-lumen-sink.md` | proposed_update | Yes | Mechanism evidence, delivery limits, and falsification gates remain local and bounded. |
| `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` | proposed_update | Yes | H08 remains open and the dynamic model remains blocked on data. |
| `wiki/luminal-uox-break-even-identifiability-computational.md` | proposed_update | Yes | Full result owner; `A_time` is now locally and unambiguously defined. |
| `wiki/open-questions.md` | proposed_update | Yes | Requires the measurement set before dynamic or serum-effect modeling. |
| `wiki/uricase.md` | proposed_update | Yes | Correctly separates product attribution, capacity, ledger, and safety. |
| `wiki/validation-experiments.md` | proposed_update | Yes | §1.33 characterizes local configuration performance only; later ledger closure remains separate. |

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Integrated amount-ledger signs | README; contract; code; results | Governing coefficient row | Formal, directly inspectable | Pass |
| `J_total_mean = (I_systemic + I_other)/T` | README; results | Capacity denominator | Formal definition, not a biological estimate | Pass |
| `A_time = ∫Vmax_active(t)dt/(Vmax_initial×T)` | README; code; results; focused page | Dimensionless retained active-capacity time area | Formal definition; locally documented and explicitly not an abundance/O2 proxy | Pass |
| Conditional capacity boundary | Code; surface CSV; results; summary | Generates 120-row grid | Exact identity under fixed occupancy | Pass |
| Surface extrema `101/400` and `1010` | CSV; results; focused page | Declared-grid summary | Independently reproduced; not physiological/global | Pass |
| Same-concentration fluxes `1/10`, `1/2`, `9/10` | Contract; code; CSV; focused page | Non-identifiability counterexample | Exact constructed values | Pass |
| Ten-variable ranks and grouped ledger rule | Contract; code; CSV; JSON | Structural-identifiability verdicts | Independently reproduced exact linear algebra | Pass |
| Exact eight-name prerequisite set | Contract; `EXPECTED_PRODUCT_PREREQUISITES`; loader | Guards conditional observation vocabulary | Base/reorder accepted; missing/extra/duplicate rejected | Pass |
| Failed-product status vocabulary | Code; CSV; JSON; README | Distinguishes surviving non-product targets | Documented without rescuing either UOX-attribution target | Pass |
| Residual tolerance boundary | README; summary; focused/dependent pages | Separates algebraic reconstruction from practical closure | Future prespecified criterion; no value invented | Pass |
| Biological regime | Results; summary; all reader surfaces | Prevents formal-to-biological upgrade | Always `NOT_EVALUATED` | Pass |

## Affected wiki pages

- `wiki/luminal-uox-break-even-identifiability-computational.md` — already consistent — defines `A_time` locally and owns the full bounded result.
- `wiki/computational-experiments.md`, `index.md` — already consistent — compact registry/dashboard routing only.
- `wiki/validation-experiments.md` — already consistent — §1.33 keeps local characterization separate from later ledger/systemic closure.
- `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` — already consistent — hypothesis remains open and data-blocked.
- `wiki/gut-lumen-sink.md`, `wiki/uricase.md` — already consistent — mechanism, product qualification, exposure, and safety boundaries are intact.
- `wiki/open-questions.md`, `wiki/gout-action-guide.md`, `wiki/gout-multihop-research-program.md`, `wiki/cross-validation.md`, `wiki/etc/GRAPH.md` — already consistent — no stale concentration-only, dose, efficacy, or topology inference.
- Mechanism-search dependents including `wiki/gout-pathophysiology.md`, `wiki/supplements-stack.md`, `wiki/genotype-informed-supplement-workflow.md`, `wiki/modality-chokepoint-matrix.md`, and `wiki/etc/ai-bio-tools-playbook.md` — already consistent — none requires a COMP-050 correction.

## New connections or implications

No new action-worthy connection was found. The cross-corpus implication already captured is methodological: future luminal-UOX models must treat qualified product fate, calibrated reaction-site capacity, source/boundary fates, and residual tolerance as measured inputs rather than infer them from concentration, abundance, or oxygen alone. This does not imply that the measurements will be feasible or precise in a biological system.

## Required actions

1. None.

## Review limits

All 22 manifest entries were available, text-inspectable, hash-matched, and inspected; there were no binary artifacts. The analysis was executed twice under explicit authorization, and independent exact-rational checks covered the complete surface, counterexamples, and rank/status table. This review did not re-verify inherited biological literature claims because COMP-050 introduces no result-bearing biological parameter; the terminal-ileal, animal, clinical, and safety evidence remains owned by its cited primary-source pages and future experiments. Assay performance, practical identifiability, biological operating conditions, residual acceptance, peroxide safety, and systemic effect remain outside this formal result.
