COMP_VERDICT: action_required
REVIEWED_SNAPSHOT: 5a9cc8f6f6a4145dae6906f32dc59cdac95b44c9906c5918ad9abd1001276b88
PROPAGATION_ELIGIBILITY: eligible_with_warning
SYNTHESIS_ELIGIBILITY: eligible_with_warning
ACTION_REQUIRED: yes
PROPAGATION_ALLOWED_SCOPE: corrective propagation that comp-019 flat-dose robustness is non-robust under comp-044's bounded diagnostics; no derived efficacy claims
SYNTHESIS_ALLOWED_SCOPE: bounded synthesis of comp-044 as a deterministic consistency audit with inherited priors and explicit open wet-lab gates
FORBIDDEN_INFERENCES: serum urate or ΔSUA prediction; oral dose or yield sufficiency; genotype ordering; topology or chassis winner; true physiological gut regime identified; grid fractions as probabilities; peroxide safety or redox closure; primary-source-verified quantitative planning values

# Independent comp review — comp-044

## Reviewed snapshot
Independent daemon reviewer; reviewed snapshot bound to supplied `push-review.manifest.json` SHA-256 `5a9cc8f6f6a4145dae6906f32dc59cdac95b44c9906c5918ad9abd1001276b88`. Shard coverage plus targeted repository reads matched the inspected text artifacts. No deterministic binary blocks were reported. Repository fixed-string search was unavailable in this environment because `rg` was missing; targeted cross-check reads were used instead.

## Bottom-line verdict
**Action required, but not blocked.** The core comp-044 artifact supports only the narrow verdict that comp-019’s unconditional flat-dose uricase regime is not robust to adding substrate occupancy and finite exposure-window diagnostics. The experiment does **not** establish physiological efficacy, dose sufficiency, topology, chassis, safety, or serum-urate effect. Corpus propagation is mostly faithful, but a provenance-label correction is needed in `wiki/etc/GRAPH.md`, and carryover non-comp-044 validation/wiki hygiene issues remain outside the safe synthesis lane.

## Implementation and constraint closure
The implemented model computes an upper-bound urate-degradation capacity ratio:

dose × UOX specific activity × pH/activity multiplier × minutes of exposure × Michaelis–Menten substrate fraction × oxygen/access/survival multipliers, converted to urate mass and divided by the legacy 233 mg/day intestinal-flux denominator.

The decision rule is closed and reproducible by inspection: the legacy saturated 24 h scenario must reproduce ratios ≥1 for all doses, and the central jejunal no-extra-penalty scenario falsifies legacy robustness if any tested dose is <1. In the committed output, all legacy ratios are far above 1, while central jejunal 5/25/50 mg ratios are 0.0932/0.4660/0.9320. That supports “legacy flat-dose regime not robust.”

Model-fit limits are material. The computation substitutes fixed-concentration upper-bound enzyme capacity against a daily flux denominator for a physiological gut reaction rate. It does not model substrate depletion/replenishment, local diffusion, residence-time distributions, epithelial reabsorption, renal compensation, microbiome metabolism, oxygen stoichiometry/depletion, hydrogen peroxide formation/scavenging, barrier injury, or serum urate. Oxygen, access, and survival are dimensionless scenario multipliers; they are evaluated in named scenarios and the grid but do not affect the predeclared verdict branch beyond summary context. The 1,620-cell grid is a design scan, not an uncertainty distribution.

## Summary-fidelity audit
The experiment README, `outputs/results.json`, and `outputs/summary.md` are materially aligned with the code and decision rule. They preserve the correct boundary: comp-044 invalidates only the prior unconditional flat-dose classification and supplies no replacement dose, ΔSUA, genotype order, physiological regime, topology/chassis selection, production sufficiency, or safety conclusion.

`wiki/computational-experiments.md`, `wiki/gut-lumen-uricase-physiologic-regime-computational.md`, `wiki/delivery-route-matrix.md`, `wiki/dual-chassis-ecn-pdb-uricase-computational.md`, `wiki/gout-action-guide.md`, `wiki/gout-multihop-research-program.md`, H08, and the comp-044-relevant `validation-experiments.md` sections largely preserve that boundary. The validation plan correctly routes UOX work through exact-configuration characterization, §1.33 physiological substrate/product/peroxide screening, §1.36 safety, and only then animal escalation.

One correction is required: `wiki/etc/GRAPH.md` labels the comp-044-to-§1.33 edge as “Mechanistic Extrapolation.” Because comp-044 is a deterministic computational audit and the experimental-routing inference is the extrapolative part, this label risks blurring evidence provenance.

## Reader-facing ownership audit
Focused pages generally own their own evidence and gates. The comp-044 interpretive page explains the model, inherited-source limits, allowed conclusion, and falsification/next-step requirements without converting it into advice or a route ranking. Cross-route and cross-chassis comparisons are mostly kept on portfolio surfaces. No personalized treatment instruction was found in the inspected comp-044 propagation.

The delivery-route matrix appropriately avoids assigning oral-UOX economic or per-dose advantage from comp-044 and leaves rectal/oral/other UOX routes behind route-specific substrate, peroxide, and safety gates.

## Conjecture preservation audit
The negative result kills only the exact prior claim that 5–50 mg/day oral UOX can be treated as unconditionally flat-dose/substrate-limited under the legacy saturated 24 h simplification. It does not kill the gut-lumen sink hypothesis, oral UOX, PULSE-like constructs, EcN/PDB/koji chassis concepts, or topology questions. Those survive as gated conjectures requiring measured local substrate, oxygen, product formation, persistence, and peroxide/barrier safety.

Useful conjectures are preserved with appropriate boundaries: topology/catalase/VHb support remains configuration-specific and not a comp-044 outcome; Q141K/genotype stratification remains prospective; UOX–mushroom or cross-route combinations remain downstream and unsupported until independent arms pass their own gates.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/README.md` | experiment narrative | Yes | Faithful narrow non-robustness claim; forbids efficacy/dose/topology inferences. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/analyze.py` | implementation | Yes + targeted read | Code matches bounded capacity-ratio audit; verdict ignores grid except named diagnostic branch. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/inputs/model_parameters.json` | input | Yes | Parameters trace into code; many are inherited/scenario priors. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/inputs/provenance.md` | provenance | Yes | Explicitly not newly primary-source verified for planning-grade use. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/inputs/query-strategy.json` | provenance/search | Yes | No independent primary-source verification established by this review. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/outputs/results.json` | generated output | Yes + targeted read | Internally consistent with code and verdict. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/outputs/summary.md` | generated output | Yes | Faithful limitations and ratios. |
| `wiki/computational-experiments.md` | proposed/affected wiki update | Yes | Comp-044, comp-019, and comp-031 propagation materially aligned. |
| `wiki/delivery-route-matrix.md` | proposed/affected wiki update | Yes | Correctly avoids UOX route sufficiency/economic overclaim. |
| `wiki/dual-chassis-ecn-pdb-uricase-computational.md` | proposed/affected wiki update | Yes | Correctly treats comp-031 as invalidated and comp-044 as narrow audit. |
| `wiki/etc/GRAPH.md` | proposed/affected wiki update | Yes | Change required: edge label blurs computational audit versus extrapolative routing. |
| `wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/reviews/push-review.md` | prior review receipt | Yes | Prior action items remain context; receipt-only status does not invalidate comp-044. |
| `wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/README.md` | affected retired artifact | Yes | Correctly invalidated; no quantitative rescue. |
| `wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/inputs/provenance.md` | affected retired provenance | Yes | Correctly rejects reuse of old quantitative priors. |
| `wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/outputs/summary.md` | affected retired output summary | Yes | Invalidation record, not live generated evidence. |
| `wiki/etc/experiments/comp-045-uricase-topology-oxygen-peroxide-design/inputs/provenance.md` | affected downstream provenance | Yes | Preserves topology evidence limits; no numerical ranking closure. |
| `wiki/gout-action-guide.md` | proposed/affected wiki update | Yes | Preserves non-clinical boundary and no UOX intervention basis. |
| `wiki/gout-multihop-research-program.md` | proposed/affected wiki update | Yes | Correctly sequences construct characterization, §1.33, §1.36. |
| `wiki/gut-lumen-uricase-physiologic-regime-computational.md` | proposed/affected wiki update | Yes + targeted read | Faithful interpretive page; no overclaim found. |
| `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` | affected hypothesis | Yes | Hypothesis remains open with correct gates. |
| `wiki/open-questions.md` | affected wiki update | Yes | UOX/genotype/ALLN-346 boundaries mostly correct; separate analyte-name issue persists. |
| `wiki/validation-experiments.md` | affected wiki update | Yes, across two segments | Comp-044 UOX gates consistent; unrelated validation-page hygiene issues remain outside comp-044 result. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| 8.3 U/mg UOX specific activity | `model_parameters.json`, provenance, code regression | Multiplies dose into µmol/min capacity | Inherited prior, not newly primary-source verified | Adequate only for bounded audit. |
| pH/activity factor 0.75 | inputs/code | Global capacity multiplier | Scenario/derived prior | Not physiological closure. |
| 0.59 µM central jejunal urate | inputs, interpretive page | Michaelis–Menten substrate fraction | Reported inherited extraction from Miyazaki 2025; not independently primary-verified here | Supports diagnostic sensitivity, not dose planning. |
| Km 5–100 µM, central 25 µM | inputs/code | Michaelis–Menten denominator | Inherited enzyme-context-dependent range | Major uncertainty; not planning-grade. |
| 2–4 h active window, central 3 h | inputs/code | Exposure duration | Inherited physiology range | Valid for falsifying 24 h simplification only. |
| 233 mg/day intestinal urate flux | inputs/code | Ratio denominator | Derived corpus prior, not local measured compartment | Useful comparator, not physiological mass balance. |
| Oxygen/access/survival multipliers | inputs/code | Scenario and grid multipliers | Nonmechanistic scenario values | Cannot decide topology, safety, or true regime. |
| Ratio-one boundary | code/results/summary | Decision threshold | Direct mass-balance comparator within simplified model | Interpretable; ratio ≥1 still not efficacy. |
| Grid fractions below one | outputs/summary | Sensitivity scan descriptor | Equal-weighted design grid | Not probabilities. |
| Peroxide/safety conclusion | limitations/validation gates | Not modeled | Requires §1.33/§1.36 measurement | No safety inference allowed. |

## Affected wiki pages
- `wiki/computational-experiments.md` — already consistent — narrow comp-044 and comp-019/031 correction preserved.
- `wiki/gut-lumen-uricase-physiologic-regime-computational.md` — already consistent — explains inherited priors, diagnostic ratios, and forbidden dose/efficacy conclusions.
- `wiki/validation-experiments.md` — already consistent for comp-044 UOX gates — §1.33/§1.36/animal escalation sequencing matches artifact limits; unrelated validation-page issues should be handled separately.
- `wiki/etc/GRAPH.md` — change required — edge label should distinguish deterministic comp audit from downstream mechanistic/extrapolative experimental routing.
- `wiki/delivery-route-matrix.md` — already consistent — no route sufficiency or economic advantage assigned from comp-044.
- `wiki/dual-chassis-ecn-pdb-uricase-computational.md` — already consistent — comp-031 invalidation and no topology/chassis claim preserved.
- `wiki/gout-action-guide.md` — already consistent — no clinical or intervention upgrade from UOX computations.
- `wiki/gout-multihop-research-program.md` — already consistent — preserves exact-configuration and safety gates.
- `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` — already consistent — hypothesis remains open, not quantitatively promoted.
- `wiki/open-questions.md` — mostly consistent for comp-044 — separate “yanthine” biomarker wording requires correction/justification outside comp-044’s quantitative verdict.

## New connections or implications
Comp-044 turns oral UOX from a nominal production/yield question into a local-exposure and product-formation gate: exact constructs must be tested at human-baseline substrate with oxygen and peroxide readouts before yield optimization or animal dosing can be prioritized. This also means topology claims from comp-045/PULSE-style precedents cannot be synthesized as winners unless exact configurations pass §1.33 and §1.36.

Research Conjecture boundary: rectal or localized UOX depots may improve exposure/control versus oral transit, but comp-044 supplies only the reason to measure local substrate/product/peroxide; it does not establish feasibility for rectal, oral, or other routes.

## Required actions
1. In `wiki/etc/GRAPH.md`, relabel the comp-044-to-§1.33 relationship to separate “deterministic computational audit” from the downstream “experimental-routing inference.” Verification: graph text no longer implies comp-044 itself is mechanistic biological validation.
2. Keep propagation receipts/summaries scoped to: “legacy flat-dose robustness not supported under comp-044 diagnostics.” Verification: no page uses comp-044 for ΔSUA, dose sufficiency, genotype order, topology/chassis winner, production target, or safety conclusion.
3. Track non-comp-044 carryover wiki hygiene issues separately, especially the `open-questions.md` “yanthine” biomarker wording and unrelated `validation-experiments.md` methodological/budget inconsistencies. Verification: corrected or explicitly justified in their owning reviews; not synthesized as comp-044 evidence.

## Review limits
No code was executed. Primary sources were not independently verified; provenance status is based on committed artifact text and targeted reads. Repository-wide grep failed because the local `rg` executable was unavailable, so corpus discovery relied on shard coverage and targeted file reads. The review did not treat receipt-only review files as independent evidence for the comp result. Unrelated validation-page defects were not fully adjudicated as comp-044 scientific failures, but they remain outside the allowed synthesis scope unless separately resolved.
