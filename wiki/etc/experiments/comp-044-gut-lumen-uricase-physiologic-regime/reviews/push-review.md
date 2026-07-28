COMP_VERDICT: clean_with_limitations
REVIEWED_SNAPSHOT: b5c71487a4b95b7aa253f0265943d412103e4edeaf130e425ea28ba0c2768838
PROPAGATION_ELIGIBILITY: eligible_with_warning
SYNTHESIS_ELIGIBILITY: eligible_with_warning
ACTION_REQUIRED: no
PROPAGATION_ALLOWED_SCOPE: use COMP-044 only as a bounded internal-consistency audit showing that COMP-019's unconditional flat-dose classification is not robust to the tested substrate-occupancy and finite-window diagnostics
SYNTHESIS_ALLOWED_SCOPE: use only the same negative boundary; preserve the biological gut-sink, possible UOX operating regimes, and UOX/PDB complementarity as unresolved
FORBIDDEN_INFERENCES: true physiological UOX regime identified; oral UOX dose or production sufficiency; serum-urate or efficacy prediction; genotype ordering; topology or chassis selection; UOX/PDB additivity; peroxide, redox, or general safety; animal or human escalation readiness; clinical advice

# Independent comp review — comp-044

## Reviewed snapshot

Reviewer: `/root/comp044_exact_reviewer_20260728`, a fresh context-isolated reviewer. The exact push-manifest payload SHA-256 is `b5c71487a4b95b7aa253f0265943d412103e4edeaf130e425ea28ba0c2768838`. Every manifest entry matched the inspected file. Receipt files under `reviews/` are excluded by design.

The current uncommitted correction to the COMP-031 tombstone README is outside the COMP-044 push manifest but was separately inspected because it closes a prior in-scope action.

## Bottom-line verdict

Clean with limitations. COMP-044 is a deterministic bounded internal-consistency audit. It supports only that COMP-019's unconditional flat-dose classification is not robust to the tested substrate-occupancy and finite-window diagnostics. It does not identify a true physiological regime or establish dose, efficacy, serum effect, genotype order, topology, chassis, production sufficiency, UOX/PDB additivity, or safety.

No current corrective action remains. The stale feasibility-score duplication has been removed from active `open-questions.md`, and the COMP-031 README correction now narrows COMP-044's role to invalidating reliance on COMP-019's unconditional flat-dose/saturated-capacity classification while preserving possible UOX regimes and UOX/PDB complementarity. That README points to validation §§1.33, 1.34, and 1.37.

## Implementation and constraint closure

`capacity_ratio()` implements:

`dose × 8.3 U/mg × 0.75 × 60 min/h × hours × S/(Km+S) × oxygen × access × survival × 168.11/1000 ÷ 233 mg/day`.

The multiplier polarity, time conversion, molecular-weight conversion, denominator, scenario construction, grid construction, and three-way verdict rule are internally consistent. Configuration assertions prevent duplicated named-scenario and grid inputs from drifting. The decision-rule self-check exercises all three possible verdicts.

The saturated 24-hour control remains above ratio one at 5, 25, and 50 mg. The terminal-ileal clinical-cohort diagnostic applies 0.59 µM urate, Km 25 µM, and three hours, placing all three ratios below one (`0.093196847`, `0.465984233`, and `0.931968467`). That is sufficient for the preregistered non-robustness verdict but is not a physiological reaction-rate or efficacy model.

The full-factorial grid has 1,620 cells per dose. Grid occupancy is explicitly descriptive, not probabilistic. Only ratio one has a direct mass-balance interpretation; the 0.25 and 4 bins are descriptive.

The model does not close finite local mass balance, urate replenishment or depletion, reabsorption, diffusion, oxygen stoichiometry or depletion, topology-specific localization, enzyme decay, peroxide/redox safety, renal compensation, microbiome metabolism, or whole-body serum mapping. Those omissions are stated in code-generated outputs and reader-facing summaries.

Independent reproduction was authorized and completed twice with the documented standard-library command. Before, after run 1, and after run 2, `results.json` was byte-identical at `1d1b55f922f88d456df32cb2a174aee236c0ff294ffbfea93e9ef461bf66af4e`; `summary.md` was byte-identical at `921226d21e7cfeee10ce4ee4c57a76f9666e7386202d77620ac51a497e00bdd4`. No output worktree diff resulted. The modern authoring lifecycle validator passes: the pre-run design equals the post-run design and the current artifact equals the post-run snapshot. The pre-run manifest's historical output baselines differ only because the authorized post-run regeneration replaced them.

## Summary-fidelity audit

The README, `results.json`, `summary.md`, canonical COMP-044 page, computational index, graph, gout action guide, multihop program, H08 card, open-questions index, and validation plan agree on the narrow verdict and its limits. All numeric COMP-044 results remain audit-only. The 8.3 U/mg activity, Km range, 0.75 pH/activity multiplier, 2–4-hour window, and 233 mg/day denominator are explicitly inherited or derived and non-planning-grade.

No active non-receipt COMP-044/cross-validation surface retains the former 5.5/10 or 6/10 feasibility scores. No reviewed surface converts COMP-044 into dose, efficacy, serum-urate, topology, chassis, production, or safety evidence.

The current COMP-031 README correction is faithful: COMP-044 invalidates only COMP-031's reliance on COMP-019's unconditional flat-dose/saturated-capacity classification. It explicitly preserves other possible UOX operating regimes and the separate conjecture that UOX and PDB could be complementary, and it routes replacement evidence to §§1.33, 1.34, and 1.37.

## Reader-facing ownership audit

The focused COMP-044 page owns the audit evidence, inherited-input boundary, exposure limitations, and next falsification gates. Cross-host/topology conclusions remain prohibited; validation §1.33 permits topology nomination only within a controlled host comparison. No editorial-history narrative, personalized protocol, or duplicated cross-track ranking remains in the inspected reader-facing surfaces.

## Conjecture preservation audit

The audit kills only the robustness of the inherited unconditional flat-dose classification under the tested finite-substrate and finite-window diagnostics. H08, oral luminal UOX, other possible UOX operating regimes, prospective genotype stratification, and UOX/PDB spatial or temporal complementarity remain open. COMP-031's quantitative ΔSUA, butyrate, Q141K-rescue, competition, and topology recommendations remain invalid for independent reasons; the current correction does not use COMP-044 to erase adjacent possibilities.

## Generated-output and proposed-update inventory

| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/README.md` | design | yes | Bounded question, conditional propagation, and reproduction contract are faithful. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/analyze.py` | design | yes | Declared formula, grid, branch logic, limitations, and deterministic outputs are implemented. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/inputs/model_parameters.json` | design | yes | Priors and scenario-only factors are separated and internally consistent. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/inputs/provenance.md` | design | yes | Terminal-ileal cohort boundary and inherited/non-planning-grade priors are explicit. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/inputs/query-strategy.json` | design | yes | Query scope is bounded; no result is encoded. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/outputs/results.json` | generated_output | yes | Exact verdict, ratios, grid summaries, provenance status, and limitations are faithful. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/outputs/summary.md` | generated_output | yes | Rounded human summary matches machine output and prohibits stronger inference. |
| `wiki/computational-experiments.md` | proposed_update | yes | Reports the bounded counterexample and non-planning-grade inputs. |
| `wiki/dual-chassis-ecn-pdb-uricase-computational.md` | proposed_update | yes | Preserves UOX/PDB possibilities while invalidating COMP-031's quantitative prior. |
| `wiki/etc/GRAPH.md` | proposed_update | yes | Routes exact configurations through §1.33 and §1.36 without selecting a chassis. |
| `wiki/gout-action-guide.md` | proposed_update | yes | Research-roadmap boundary; no treatment or fixed-dose inference. |
| `wiki/gout-multihop-research-program.md` | proposed_update | yes | Construct supply precedes physiological screening; no abstract topology winner. |
| `wiki/gut-lumen-uricase-physiologic-regime-computational.md` | proposed_update | yes | Canonical audit page states the exact invalidation boundary and limitations. |
| `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` | proposed_update | yes | H08 remains open and has no numeric ΔSUA claim. |
| `wiki/open-questions.md` | proposed_update | yes | No stale 5.5/10 or 6/10 feasibility score; genotype and UOX/PDB questions remain open. |
| `wiki/validation-experiments.md` | proposed_update | yes | §§1.33, 1.34, 1.36, and 1.37 preserve configuration, compartment, mass-balance, and safety gates. |

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| 0.59 µM terminal-ileal clinical-cohort urate | parameters/provenance/scenarios | Central `S/(Km+S)` diagnostic | Grep-verified inherited extraction and arithmetic; not a healthy baseline | Adequate for bounded audit. |
| 8.3 U/mg specific activity | parameters/code | Capacity numerator | Inherited; not newly primary-source verified | Audit-only; planning prohibited. |
| Km 5–100 µM, central 25 µM | parameters/code/grid | Occupancy denominator/sensitivity | Inherited and enzyme-context dependent | Audit-only; planning prohibited. |
| 0.75 pH/activity multiplier | parameters/code | Scenario capacity factor | Inherited scenario value | Not a measured physiological constant. |
| 2–4 h active window, central 3 h | parameters/code/grid | Finite-time diagnostic | Inherited physiology range | Audit-only; not a patient parameter. |
| 233 mg/day denominator | parameters/code/results | Legacy comparison denominator | Derived corpus prior | Not local or patient-specific mass balance. |
| Oxygen/access/survival factors | parameters/code/grid | Nonmechanistic sensitivity penalties | Scenario-only | No mechanistic or probability interpretation. |
| Ratio-one verdict rule | code/results | Robustness branch | Predeclared and self-tested | Correctly applied. |
| Reported output hashes | generated outputs | Reproduction authority | Independently reproduced twice | Byte-identical; no worktree drift. |

## Affected wiki pages

- `wiki/gut-lumen-uricase-physiologic-regime-computational.md` — already consistent — canonical bounded evidence home.
- `wiki/computational-experiments.md` — already consistent — audit-only numbers and inherited-input limitations are explicit.
- `wiki/dual-chassis-ecn-pdb-uricase-computational.md` — already consistent — UOX/PDB complementarity remains open.
- `wiki/etc/GRAPH.md` — already consistent — no topology/chassis selection.
- `wiki/gout-action-guide.md` — already consistent — no dose, efficacy, or treatment inference.
- `wiki/gout-multihop-research-program.md` — already consistent — correct construct-supply and empirical-gate sequence.
- `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` — already consistent — biological hypothesis remains open.
- `wiki/open-questions.md` — already consistent — stale feasibility-score duplication is gone.
- `wiki/validation-experiments.md` — already consistent — §§1.33/1.34/1.37 close distinct UOX, staging, and PDB questions.
- `wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/README.md` — already consistent in the inspected uncommitted correction — exact blast radius and §§1.33/1.34/1.37 links are present.

## New connections or implications

No new propagation is required. The already-routed implication is sound: a future quantitative UOX/PDB model must first obtain configuration-level physiological UOX measurements (§1.33), spatial residual-flux measurements (§1.34), and isotope-resolved CBT2.0 carbon fate (§1.37). This is an experiment-ordering implication, not evidence for complementarity or additivity.

## Required actions

1. None.

## Review limits

The inherited specific-activity, Km, pH/activity, transit-window, and daily-flux priors were not independently promoted to primary-source-verified planning inputs in this review. That is not a current action because every active surface confines them to the bounded internal-consistency audit and explicitly prohibits quantitative planning. Primary-source verification becomes required if a future surface uses them for dose, production, efficacy, or other quantitative planning.
