ACTION_REQUIRED: no
REVIEWED_SNAPSHOT: f20c3c46bb91abfe2d6b7135a17cb3c222b43655937af77911b8949bdd442c1b

# Independent comp review — comp-044

## Reviewed snapshot

Reviewer: `/root/comp044_gate2` (context-isolated authoring-time Gate 2 reviewer).

The post-run manifest check passed and returned `f20c3c46bb91abfe2d6b7135a17cb3c222b43655937af77911b8949bdd442c1b`. Every bound file matched its manifest entry and was inspected completely.

Gate 1 is bound to approved pre-run manifest `248abfa19e377c97848a3f5d185df0f92e56b6dd395cffce410fe5c9f63bb7b9`. All five current design hashes exactly match that manifest:

- README: `07a8035a…`
- `analyze.py`: `c6a018c3…`
- model parameters: `2f1edff6…`
- provenance: `2fca6e29…`
- query strategy: `d6778942…`

The pre-run receipt contains `PRE_RUN_GATE: GO` and the exact reviewed snapshot. A current pre-run check reports only that the two bound historical prior-output baselines have changed, which is the expected consequence of the authorized regeneration; the design snapshot itself remains unchanged.

The regenerated output hashes match both the post manifest and the operator’s two-run report: `results.json` `1d1b55f9…` and `summary.md` `921226d2…`.

## Bottom-line verdict

Clean.

The result faithfully applies the preregistered decision rule: the saturated 24-hour legacy control is reproduced above ratio one at every dose, while all three terminal-ileal clinical-cohort diagnostic doses are below ratio one. Therefore COMP-019’s unconditional flat-dose classification is not robust to the tested substrate-occupancy and finite-window diagnostic.

The artifact does not claim a replacement dose, physiological regime, serum effect, efficacy, genotype ordering, topology/chassis choice, production sufficiency, or safety conclusion.

Static comparison with the previous artifact confirms that regeneration changed only the corrected terminal-ileal clinical-cohort provenance/scenario labels, query framing, supporting provenance text, and the explicit machine-readable provenance field. Numerical inputs, equations, grid membership, ratios, regime bins, verdict mapping, and decision semantics did not change.

## Implementation and constraint closure

The implemented ratio is:

`dose × 8.3 U/mg × 0.75 × 60 min/h × hours × urate/(Km+urate) × oxygen × access × survival × 168.11/1000 ÷ 233 mg/day`

Units, multiplier polarity, time base, molecular-weight conversion, and denominator placement are internally consistent for the declared bounded diagnostic.

Independent arithmetic audit found:

- Legacy 5/25/50 mg ratios: `32.337726 / 161.688631 / 323.377262`.
- Terminal-ileal diagnostic applies `(3/24) × 0.59/(25+0.59)`, yielding `0.093196847 / 0.465984233 / 0.931968467`.
- Its microoxic/access/survival case applies an additional `0.15 × 0.5 × 0.5 = 0.0375`, yielding `0.003494882 / 0.017474409 / 0.034948817`.
- The 50 µM case applies `(3/24) × 50/75 × 0.0375`, yielding `0.101055394 / 0.505276972 / 1.010553943`.
- The 500 µM case applies `500/525 × 0.01 × 0.25 × 0.25`, yielding `0.019248647 / 0.096243233 / 0.192486465`.

Every reported regime label agrees with the declared `<0.25`, `<1`, `<4`, and `≥4` bins. The grid contains `5 × 3 × 4 × 3 × 3 × 3 = 1,620` cells per dose. Each regime-count row sums to 1,620; each fraction below one equals the two below-one counts divided by 1,620; and the reported extrema occur at the expected extreme-factor corners.

Oxygen stoichiometry and depletion, H₂O₂ production and safety, dynamic urate replenishment/depletion, reabsorption, spatial access, renal compensation, microbiome metabolism, topology, and formulation remain outside the model and are explicitly bounded as limitations. This is therefore an internal-consistency counterexample, not physiological closure.

## Summary-fidelity audit

`results.json`, `summary.md`, the README, and the proposed canonical page agree on all named ratios, grid summaries, verdict, and limitations.

The canonical update correctly calls the result a **Mechanistic Extrapolation** from a deterministic audit with inherited inputs. It says all three diagnostic ratios move below one, but explicitly rejects a true-regime reversal or sufficient-dose inference.

The active corpus already uses the same narrow interpretation. Targeted searches found no active non-review surface that positively describes the 0.59 µM input as jejunal or as a healthy-population baseline. Matches outside the maintenance queue are correct negative boundaries such as “not a jejunal measurement or healthy-population baseline,” or unrelated uses of “healthy baseline.”

The maintenance queue item is fully resolved by this Gate 1 → deterministic regeneration → Gate 2 lifecycle. It may be deleted after this receipt is bound, as the queue file itself requires.

## Reader-facing ownership audit

The proposed canonical page stands on its own: it states the question, evidence boundary, source and compartment, method, numerical results, exposure constraints, limitations, and next discriminating experiment.

It contains no personalized treatment instruction, home-production recommendation, editorial-history narration, chassis narrative foil, cross-track ranking, or unsupported clinical implication. Comparative chassis decisions remain outside COMP-044 and configuration-specific topology testing remains assigned to validation §1.33, with safety assigned separately.

## Conjecture preservation audit

The unsupported legacy factual conclusion is narrowed without deleting the biological gut-lumen sink idea.

H08 and related gut-sink work remain open as falsifiable hypotheses. The negative result kills only COMP-019’s unconditional flat-dose classification under COMP-044’s declared diagnostic inputs and ratio-one rule. It does not kill oral luminal UOX generally, select or reject a chassis/topology, establish production insufficiency, or infer clinical inefficacy.

## Generated-output and proposed-update inventory

| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/README.md` | design | Yes | Conditional contract and narrow scope are coherent |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/analyze.py` | design | Yes | Inputs, calculation, bins, verdict branches, and output derivations close |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/inputs/model_parameters.json` | design | Yes | Correct labels; numerical design unchanged |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/inputs/provenance.md` | design | Yes | Source, cohort, compartment, conversion, and inherited-prior limits stated |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/inputs/query-strategy.json` | design | Yes | Search framing now matches terminal-ileal clinical-cohort scope |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/outputs/results.json` | generated output | Yes | Ratios, regimes, grid summaries, provenance field, and verdict agree |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/outputs/summary.md` | generated output | Yes | Faithful human-readable rendering |
| `wiki/gut-lumen-uricase-physiologic-regime-computational.md` | proposed update | Yes | Correct owner, evidence boundary, interpretation, and falsification path |

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| PMID 40033341 / PMCID PMC11877951 / DOI 10.1186/s12967-025-06145-7 | Provenance | Identifies Miyazaki source | Verified against PubMed and publisher record | Pass |
| Terminal-ileal sampling | Provenance; labels | Compartment boundary for diagnostic prior | Source Figure 1/sampling materials identify distal terminal-ileal balloon-enteroscopy sampling | Pass |
| Clinical cohort: 30 Crohn’s, 2 simple ulcers, 2 OGIB | Provenance | Prevents healthy-baseline generalization | Verified in primary full text; total n=34 | Pass |
| Lesion-free sampled segments | Provenance | Narrows local sampling condition without making cohort healthy | Verified in primary full text | Pass |
| 99.5 [10.1–194.0] pg/µL | Provenance | Basis for 0.59 [0.06–1.16] µM input | Verified in primary full text | Pass |
| 99.5 pg/µL → 0.591874 µM | Provenance; parameters | Central substrate input | Conversion independently checked using 168.11 g/mol | Pass |
| 8.3 U/mg and 0.75 factor | Parameters; ratio | Nominal activity capacity | Inherited/scenario values, explicitly non-planning-grade | Pass for bounded audit |
| Km 5–100 µM, central 25 µM | Parameters; occupancy | Michaelis–Menten sensitivity | Inherited and enzyme-context dependent | Pass for bounded audit |
| 2–4 h active window | Parameters; time multiplier | Finite exposure diagnostic | Inherited, not a cohort measurement | Pass for bounded audit |
| 233 mg/day denominator | Parameters; ratio | Legacy classification comparison | Derived corpus prior, not local or patient-specific flux | Pass for bounded audit |
| Ratio-one verdict boundary | Code; outputs | Robustness decision | Predeclared and applied correctly | Pass |

## Affected wiki pages

- `wiki/gut-lumen-uricase-physiologic-regime-computational.md` — already consistent — proposed update correctly binds the diagnostic to terminal-ileal clinical-cohort provenance.
- `wiki/computational-experiments.md` — already consistent — reports the narrow non-robustness verdict and forbidden inferences.
- `wiki/uricase-topology-oxygen-peroxide-design-computational.md` — already consistent — explicitly says the prior is not jejunal or a healthy-population baseline.
- `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` — already consistent — preserves the platform hypothesis and correct cohort boundary.
- `wiki/validation-experiments.md` — already consistent — routes the prior to configuration-level empirical testing without dose or chassis inference.
- `synthesis/queue/zz-maintenance-comp044-terminal-ileum-label.md` — resolved — may be deleted after this receipt is bound.

## New connections or implications

None beyond the already routed implication: COMP-044 removes the legacy justification for treating yield optimization or dose sufficiency as settled, while leaving the biological sink hypothesis open for configuration-level substrate × oxygen × peroxide testing.

## Required actions

None.

## Review limits

This was a static, read-only review. I did not execute `analyze.py` or any result-bearing experiment logic. Determinism is supported by the operator’s two identical runs and the matching output hashes, not by independent execution during this review.

The inherited activity, Km, active-window, and 233 mg/day priors were not upgraded to quantitative-planning evidence; the artifact explicitly preserves that limitation.
