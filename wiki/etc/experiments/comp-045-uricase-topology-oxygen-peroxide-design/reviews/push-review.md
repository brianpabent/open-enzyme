COMP_VERDICT: action_required
REVIEWED_SNAPSHOT: 255fcd66cc5150ee38183d485c7e9cb8ed18146503383536793c8b75b33306f3
PROPAGATION_ELIGIBILITY: eligible_with_warning
SYNTHESIS_ELIGIBILITY: eligible_with_warning
ACTION_REQUIRED: yes
PROPAGATION_ALLOWED_SCOPE: design-only comp-045 layout/status corrections and wet-lab blocker propagation; no biological ranking or execution-ready protocol claims
SYNTHESIS_ALLOWED_SCOPE: narrow synthesis as blocked candidate layout/evidence-boundary artifact only
FORBIDDEN_INFERENCES: topology/chassis winner; biological efficacy or safety; wet-lab readiness; activity at 0.59 or 50 µM; oxygen sufficiency; isolated KatG-only or VHb-only effect; extracellular peroxide closure; direct A. oryzae UOX precedent; PULSE mixture as published positive control

# Independent comp review — comp-045

## Reviewed snapshot
Independent daemon review for comp-045, bound to push-review manifest SHA-256 `255fcd66cc5150ee38183d485c7e9cb8ed18146503383536793c8b75b33306f3` at source commit `00e535127beae0df3362f88654ddc323d269aba5`. Shard auditors reported complete inspection of the manifest text spans; targeted repository reads of the summary, README, computational index, and interpretive page matched the supplied audits. No deterministic binary blocks were reported. Repository fixed-string search tooling was unavailable due missing `rg`, so targeted cross-checks used direct file reads plus shard coverage.

## Bottom-line verdict
Action required, but not because the biological conclusion is overstated in the inspected comp-045 surfaces. The committed outputs and main wiki propagation correctly preserve the narrow result: `CANDIDATE_LAYOUT_GENERATED`, biological verdict `NOT_EVALUATED`, and wet-lab readiness blocked. Required actions remain for implementation/provenance hygiene: the gate is documented in the wrapper command rather than enforced by `analyze.py`, and load-bearing source facts are citation/narrative assertions rather than directly verifiable source excerpts or bibliographic records.

## Implementation and constraint closure
The computation fits only a design-validation question. It generates and validates an evidence vocabulary plus randomized candidate plate maps; it does not model UOX kinetics, oxygen consumption, peroxide dynamics, gut residence, mucus access, epithelial injury, expression burden, proteolysis, colonization, or clinical urate outcomes. This is an appropriate answer to “how should these configurations be compared,” not to “which topology works.”

Load-bearing design closure is mostly explicit:
- 18 unique configurations, 20 block assignments, 14 preregistered same-block contrasts, 12 full 96-well plates, 3 runs, 2 oxygen contexts, and full 96/0 used/empty well allocation are present in outputs and propagated summaries.
- Active-UOX rows have support-module-matched inactive-UOX controls at each concentration, but exact inactive mutation, expression equivalence, and localization equivalence are unresolved and explicitly block wet-lab execution.
- Oxygen labels are placeholders for measured regimes. PULSE sealed tubes and Zhao ~15%-normal dissolved oxygen are not interchangeable, and “oxic”/“microoxic” do not establish oxygen sufficiency.
- Reaction-site closure is correctly constrained: intracellular KatG is not at the extracellular/surface UOX reaction site for LamB/InaK-N rows; proposed co-secreted or co-displayed catalase requires expression, localization, activity, compatibility, and safety qualification.
- Substrate roles are appropriately separated: 0.59 µM is a terminal-ileal human-fluid prior not tested in the cited UOX configurations; 50 µM is sensitivity only; 250 µM is the lowest published PULSE topology-assay concentration.
- Sampling/readout closure remains unresolved: urate, pathway product, H₂O₂, dissolved oxygen, viability, and UOX localization may require aliquot/destructive-readout planning, and assay sensitivity at 0.59 µM is a blocker.

Implementation concern: the README says result-bearing execution is prohibited until `PRE_RUN_GATE: GO` and the documented reproduction command checks it, but `analyze.py` itself has no manifest/gate enforcement and can write outputs if run directly. The authoring gates are reported modern/valid, so this does not invalidate the pushed outputs, but the executable contract is weaker than the documentation implies.

## Summary-fidelity audit
The inspected `outputs/summary.md`, README, `wiki/uricase-topology-oxygen-peroxide-design-computational.md`, and `wiki/computational-experiments.md` are materially faithful: they state design-only disposition, biological `NOT_EVALUATED`, wet-lab blockers, exact/related precedent boundaries, no topology ranking, no wet-lab readiness, and no source-positive-control status for the PULSE mixture anchor.

`wiki/validation-experiments.md` §1.33 preserves the comp-045 boundary: schema-2 layout is candidate-only, biological verdict is not evaluated, execution is blocked pending controls/sampling, and cross-host ranking is forbidden. `wiki/gout-multihop-research-program.md`, `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md`, and `wiki/etc/GRAPH.md` appropriately route comp-045 into later validation without upgrading it to biological evidence.

No inspected surface was found claiming a topology winner, efficacy, dose, genotype order, ΔSUA effect, safety conclusion, or execution-ready protocol from comp-045.

## Reader-facing ownership audit
The interpretive comp page owns the evidence boundary, construct/topology distinctions, substrate/oxygen constraints, wet-lab blockers, and falsification boundary. Cross-track and program-order claims remain on portfolio/program surfaces rather than being duplicated as long narrative foils on the focused page. No personalized treatment instructions were found. `wiki/aspergillus-oryzae.md` properly treats food-use/native secretion as experiment motivation only and keeps engineered-strain safety, active UOX, peroxide, exposure, and release gates open.

## Conjecture preservation audit
Unsupported factual upgrades are already avoided: KatG-only/VHb-only effects, extracellular peroxide closure, surface accessibility, and koji-secreted active UOX are not stated as established. The main surviving useful conjecture is explicitly labeled: joint-module benefit outside the cell may reflect VHb oxygen/cell-fitness support, intracellular ROS handling, or both rather than extracellular peroxide closure. The discriminating observation—matched no-module/KatG-only/VHb-only/joint/reaction-site-catalase comparisons with product, DO, H₂O₂, viability, localization, and exposure readouts—is grounded and should be preserved as conjecture, not claim.

A later negative wet-lab result would kill only the exact construct × concentration × oxygen × control regime tested. It would not kill gut-lumen UOX, other topologies, other chassis, or reaction-site peroxide-control concepts unless their required premise was directly tested and failed.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-045-uricase-topology-oxygen-peroxide-design/README.md` | experiment documentation | Yes | Design-only contract faithful; gate documented via wrapper, not enforced in `analyze.py`. |
| `wiki/etc/experiments/comp-045-uricase-topology-oxygen-peroxide-design/analyze.py` | experiment code | Yes | Generates layout/outputs; no internal pre-run manifest gate. |
| `wiki/etc/experiments/comp-045-uricase-topology-oxygen-peroxide-design/inputs/design_factors.json` | input | Yes | Encodes evidence/configuration regimes; no summary drift reported. |
| `wiki/etc/experiments/comp-045-uricase-topology-oxygen-peroxide-design/inputs/provenance.md` | input/provenance | Yes | Source claims are narrative/citation assertions; primary-source verification unresolved. |
| `wiki/etc/experiments/comp-045-uricase-topology-oxygen-peroxide-design/inputs/query-strategy.json` | input/provenance | Yes | Query framing inspected; not primary-source evidence. |
| `wiki/etc/experiments/comp-045-uricase-topology-oxygen-peroxide-design/outputs/results.json` | generated output | Yes | Design disposition `CANDIDATE_LAYOUT_GENERATED`, biological `NOT_EVALUATED`, wet-lab blocked; no biological outcomes. |
| `wiki/etc/experiments/comp-045-uricase-topology-oxygen-peroxide-design/outputs/summary.md` | generated output | Yes | Faithful compact boundary; no topology/effect upgrade. |
| `wiki/uricase-topology-oxygen-peroxide-design-computational.md` | interpretive wiki update | Yes | Faithful design-only page with appropriate Research Conjecture. |
| `wiki/computational-experiments.md` | index/summary update | Yes | Correctly lists comp-045 as design only / not evaluated. |
| `wiki/validation-experiments.md` | validation update | Yes | §1.33 preserves blockers and forbids cross-host rankings; unrelated page issues not used for comp-045 verdict. |
| `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` | hypothesis update | Yes | Keeps topology advance tied to exact measured configurations. |
| `wiki/gout-multihop-research-program.md` | program update | Yes | Correctly places exact UOX build/characterization before escalation. |
| `wiki/aspergillus-oryzae.md` | affected chassis page | Yes | Consistent: food-use/native secretion do not establish engineered UOX safety/efficacy. |
| `wiki/etc/GRAPH.md` | graph/index update | Yes | Link/routing only; no biological validation upgrade. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Biological verdict is `NOT_EVALUATED` | `outputs/results.json`, `outputs/summary.md`, wiki pages | Output/status field and propagation boundary | Directly present in artifact | Supported. |
| 18 unique configurations / 20 block assignments / 14 same-block contrasts / 12 plates | Results, summary, computational index | Layout-generation and summary claims | Directly present in generated outputs; code not executed in daemon review | Plausible by inspection; deterministic reproduction not independently run. |
| 96 used / 0 empty wells per plate | `outputs/results.json`, summary | Plate-map allocation | Directly present in output records | Supported as generated layout claim. |
| Active-UOX matched inactive-UOX controls | Results, README, summary | Control design | Exact inactive mutation/equivalence unresolved | Supported as planned control class; not executable. |
| 0.59 µM terminal-ileal prior | Inputs/provenance, summary, interpretive page | Urate regime label | Citation/narrative only; primary source not directly verified here | Usable only as labeled prior; source verification unresolved. |
| 50 µM sensitivity scenario | Inputs/outputs/summary | Design concentration | Internal label; not evidence-backed | Supported as sensitivity-only. |
| 250 µM PULSE assay concentration | Provenance/summary | Published-comparator concentration | Citation/narrative only | Bounded; primary verification unresolved. |
| PULSE exact EcN topology precedents | Inputs/provenance/interpretive page | Evidence vocabulary | Citation/narrative only | Bounded to whole configurations; not independently source-verified. |
| KatG-only and VHb-only not source-isolated | Summary/interpretive page/results | Evidence-boundary rule | Derived from narrative source scope | Correctly preserved; source verification unresolved. |
| Intracellular KatG not reaction-site peroxide closure for LamB/InaK-N | Results/summary/wiki | Constraint labeling | Mechanistic localization inference from topology definitions | Supported as caution; needs wet-lab H₂O₂/localization readouts. |
| Koji-secreted UOX has no direct cited precedent | Summary/wiki/A. oryzae page | Evidence label | Citation audit not independently verified | Correctly treated as proposed configuration. |
| Oxygen contexts require predeclared/measured DO | Results/summary/wiki | Wet-lab blocker | Internal design constraint; source regimes narrative | Supported; no oxygen sufficiency inference allowed. |
| PULSE-KV mixture is cross-plate anchor, not positive control | Results/summary | Anchor interpretation | Internal design label | Supported; must not be upgraded. |

## Affected wiki pages
- `wiki/uricase-topology-oxygen-peroxide-design-computational.md` — already consistent — owns comp-045 design-only interpretation and wet-lab blockers.
- `wiki/computational-experiments.md` — already consistent — index preserves `DESIGN ONLY / NOT EVALUATED` and layout numbers.
- `wiki/validation-experiments.md` — already consistent for comp-045 §1.33 — candidate layout is blocked and non-decision-grade; cross-host ranking forbidden.
- `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` — already consistent — topology advance requires exact measured configuration contrasts.
- `wiki/gout-multihop-research-program.md` — already consistent — exact configuration build/characterization precedes §1.33 and downstream escalation.
- `wiki/aspergillus-oryzae.md` — already consistent — engineered A. oryzae UOX remains gated by direct active-UOX, peroxide, safety, and exposure evidence.
- `wiki/etc/GRAPH.md` — already consistent — routing edge only; not biological validation.
- `wiki/etc/experiments/comp-045-uricase-topology-oxygen-peroxide-design/README.md` — change required — clarify or enforce that the gate is external wrapper enforcement unless `analyze.py` is modified to check manifests itself.

## New connections or implications
Comp-045 sharpens an important cross-corpus separation: reaction-site peroxide control is not equivalent to host-cell ROS handling. For extracellular or displayed UOX, intracellular KatG can remain useful as a viability/ROS-support module, but it cannot be synthesized as proven peroxide detoxification at the extracellular urate reaction site. This supports preserving reaction-site catalase as a distinct Research Conjecture rather than treating KatG+VHb success as closure.

It also constrains A. oryzae extrapolation: native secretion and food-use history justify construct testing, but not active secreted UOX, peroxide control, safety, serving size, or superiority. Validation §1.33 and the A. oryzae chassis page are aligned on that boundary.

## Required actions
1. Update the comp-045 README or implementation contract: either add manifest/gate enforcement to `analyze.py`, or state plainly that gate enforcement is external to the documented wrapper command and direct `analyze.py` execution is not gate-safe. Verification: direct execution behavior and README wording no longer conflict.
2. Add directly inspectable provenance support for load-bearing source facts, or downgrade wording to “citation asserted/not independently verified in artifact.” This applies to PULSE/Gao topology scope and 250 µM concentration, Zhao oxygen scope, Li related-precedent scope, and the 0.59 µM terminal-ileal concentration conversion. Verification: source excerpts/bibliographic metadata or explicit unverified-provenance labels are present.
3. Before any wet-lab execution from this layout, bind exact active/inactive UOX identities, inactive mutation, expression/localization equivalence criteria, constructs, stocks, cell normalization, dissolved-oxygen targets, sampling/aliquot/destructive-readout plan, and assay quantification at 0.59 µM. Verification: a new reviewed lifecycle or protocol addendum resolves all blockers and regenerates the layout if the qualified set changes.

## Review limits
Code was not executed in daemon mode; deterministic reproduction was assessed by inspection and authoring-gate receipt only. Primary sources were not independently opened or verified; provenance status is therefore citation/narrative unless the artifact itself supplied inspectable support. Repository fixed-string search failed because the search backend was unavailable, so affected-surface discovery relied on shard coverage and targeted direct reads rather than a fresh repository-wide grep. Unrelated issues reported by shard auditors in broader `validation-experiments.md` sections were not used to change the comp-045 verdict unless they affected comp-045 propagation.
