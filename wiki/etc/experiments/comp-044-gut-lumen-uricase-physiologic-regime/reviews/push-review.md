COMP_VERDICT: clean_with_limitations
REVIEWED_SNAPSHOT: df65073c0b1065ba8553cddb0b3fabe99925d5ffb8f0b2ec23cc0fdbb756c181
PROPAGATION_ELIGIBILITY: eligible_with_warning
SYNTHESIS_ELIGIBILITY: eligible_with_warning
ACTION_REQUIRED: yes
PROPAGATION_ALLOWED_SCOPE: bounded corrective propagation only: comp-019 unconditional flat-dose robustness fails the comp-044 diagnostic
SYNTHESIS_ALLOWED_SCOPE: bounded mechanistic audit synthesis with inherited-input and no-serum/no-dose/no-topology limitations
FORBIDDEN_INFERENCES: serum-urate effect; dose recommendation; genotype ordering; true physiological regime; topology or chassis winner; production-sufficiency target; safety conclusion; probability from grid occupancy; clinical or self-experiment guidance

# Independent comp review — comp-044

## Reviewed snapshot
Independent daemon consolidation for comp-044, bound to supplied `push-review.manifest.json` SHA-256 `df65073c0b1065ba8553cddb0b3fabe99925d5ffb8f0b2ec23cc0fdbb756c181`. The supplied shard coverage reports complete text inspection of the comp artifact, generated outputs, and affected/proposed wiki surfaces. Targeted repository reads of the comp code, inputs, outputs, interpretive page, and computational index agreed with the shard findings. The manifest file itself was not readable via the repository tool, but the daemon brief supplied a valid modern authoring-gate status and no deterministic blocks.

## Bottom-line verdict
Clean with limitations for the comp-044 scientific result: the code and summaries support the narrow conclusion that comp-019’s unconditional saturated, 24-hour flat-dose classification is not robust once substrate occupancy and a finite active window are applied under inherited priors. Action is still required because the broad `validation-experiments.md` surface contains unrelated material QA issues found during full-page audit; those do not block bounded comp-044 propagation.

## Implementation and constraint closure
I traced the load-bearing path from `inputs/model_parameters.json` through `analyze.py` to `outputs/results.json` and `outputs/summary.md`.

The capacity calculation uses dose × 8.3 U/mg × 0.75 pH/activity factor × 60 min/h × active hours × substrate occupancy × oxygen × access × survival, converts µmol urate to mg using 168.11 g/mol, then divides by the inherited 233 mg/day intestinal-flux denominator. The unit conversion is internally plausible for a diagnostic ratio.

Important implementation boundary: the verdict rule depends only on two named scenarios: reproduction of the legacy saturated 24-hour control and whether all central jejunal no-extra-penalty ratios are ≥1. Oxygen, access, survival, postprandial/distal scenarios, and grid occupancy are evaluated but do not determine the verdict. This is acceptable only because the central diagnostic alone is a predeclared counterexample to unconditional robustness; it must not be represented as a full physiological-regime model.

Constraint closure remains intentionally incomplete and documented. Substrate occupancy is included via urate/(Km+urate), but local replenishment, depletion, diffusion, reabsorption, renal compensation, microbiome metabolism, genotype-specific urate supply, oxygen stoichiometry, peroxide production/scavenging, barrier exposure, and topology-specific localization are not modeled. The pH, oxygen, access, and survival factors are nonmechanistic scenario multipliers, not measured human parameters. The 1,620-cell grid is design-space occupancy over selected levels, not probability.

## Summary-fidelity audit
The comp README, `outputs/results.json`, and `outputs/summary.md` faithfully report the generated verdict and central ratios: 0.093 / 0.466 / 0.932 for 5 / 25 / 50 mg in the 0.59 µM, Km 25 µM, 3-hour central diagnostic, versus 32.3 / 161.7 / 323.4 in the legacy saturated 24-hour control. The summary correctly forbids replacement ΔSUA, dose, genotype-ordering, physiological-regime, efficacy, topology/chassis, production, and safety claims.

The interpretive page, computational index, delivery route matrix, dual-chassis page, GRAPH, action guide, multihop program, H08 hypothesis, open questions, and validation §1.33 preserve the same boundary. I found no comp-044-specific summary drift, stale winner, unsupported wet-lab reprioritization, or evidence-tier upgrade.

## Reader-facing ownership audit
The focused comp-044 interpretive page owns the evidence, sourcing boundary, delivery/exposure limitations, and falsification gate. Cross-track route and topology comparisons remain in portfolio surfaces and validation designs rather than being promoted on the focused page. The reviewed comp-044 surfaces avoid personalized treatment instructions and do not turn engineered UOX into clinical guidance.

The larger `validation-experiments.md` page contains unrelated reader-contract and technical QA issues in sections outside comp-044, including at least the 16S/fungal-dominance mismatch and several threshold/provenance ambiguities. These should be handled as page QA, not as comp-044 synthesis.

## Conjecture preservation audit
Comp-044 kills only the exact old claim that 5–50 mg/day oral UOX can be treated as unconditionally flat-dose/substrate-limited under the inherited saturated-capacity regime. It does not kill the biological gut-lumen sink hypothesis, oral UOX feasibility, topology testing, or genotype-response conjectures. Those survive only as open conjectures requiring exact-configuration characterization, physiological substrate/product measurements, peroxide/barrier safety, and later dynamic mass-balance/serum modeling.

Unsupported factual upgrades were not found on comp-044 surfaces. Adjacent ideas are preserved in the correct form: Research Conjecture / open hypothesis, not validated intervention.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/README.md` | comp artifact | yes | Matches bounded not-robust result and limitations. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/analyze.py` | implementation | yes | Deterministic stdlib calculation; verdict ignores grid except central diagnostic, a documented boundary. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/inputs/model_parameters.json` | input | yes | Inputs trace to code; several are inherited/non-planning-grade. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/inputs/provenance.md` | input provenance | yes | Clearly marks inherited priors and scenario-only multipliers. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/inputs/query-strategy.json` | input support | yes | No material comp-044 defect reported. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/outputs/results.json` | generated_output | yes | Supports verdict; 50 mg central ratio is near boundary at 0.932. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/outputs/summary.md` | generated_output | yes | Faithful and appropriately bounded. |
| `wiki/computational-experiments.md` | proposed_update | yes | Comp-044 entry faithful; no over-propagation. |
| `wiki/delivery-route-matrix.md` | proposed_update | yes | Does not use comp-044 to select route. |
| `wiki/dual-chassis-ecn-pdb-uricase-computational.md` | proposed_update | yes | Correctly narrows comp-044 and comp-031 invalidation. |
| `wiki/etc/GRAPH.md` | proposed_update | yes | Routes comp-044 as unresolved audit, not validation. |
| `wiki/gout-action-guide.md` | proposed_update | yes | Research-only framing preserved. |
| `wiki/gout-multihop-research-program.md` | proposed_update | yes | Gate sequencing and comp-044 limits preserved. |
| `wiki/gut-lumen-uricase-physiologic-regime-computational.md` | proposed_update | yes | Interpretive page faithful to outputs and provenance. |
| `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` | proposed_update | yes | Hypothesis remains Open; no numeric ΔSUA claim. |
| `wiki/open-questions.md` | proposed_update | yes | Genotype/dose/topology boundaries preserved. |
| `wiki/validation-experiments.md` | proposed_update / affected page | yes | §1.33 comp-044 integration is consistent; unrelated sections have material QA issues requiring separate action. |
| `wiki/etc/experiments/comp-019.../reviews/push-review.md` | context | yes | Prior limits support avoiding comp-019 resurrection. |
| `wiki/etc/experiments/comp-031...` files | context | yes | Invalidation preserved; no topology claim recoverable. |
| `wiki/etc/experiments/comp-045.../inputs/provenance.md` | context | yes | Supports topology-design boundaries only, not ranking. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| 8.3 U/mg uricase activity | `model_parameters.json`, provenance | Linear capacity numerator | Inherited, not newly primary-source verified | Usable only for bounded audit. |
| pH/activity factor 0.75 | inputs/provenance | Linear multiplier | Inherited scenario multiplier | Not a measured in vivo constant. |
| Jejunal urate 0.59 µM | inputs/provenance, interpretive page | Central substrate occupancy | Inherited grep-verified extraction with arithmetic conversion shown | Strongest input, still not patient/local dynamic closure. |
| Km 25 µM, range 5–100 µM | inputs/provenance | Substrate occupancy denominator | Inherited enzyme-context prior | Not planning-grade. |
| Active window 2–4 h, central 3 h | inputs/provenance | Time multiplier | Inherited physiology prior | Diagnostic only. |
| 233 mg/day intestinal flux | inputs/provenance | Ratio denominator | Derived corpus prior, not local compartment measurement | Adequate for legacy comparison, not physiological mass balance. |
| Oxygen/access/survival multipliers | inputs/provenance | Scenario/grid multipliers | Deliberately nonmechanistic | Cannot infer oxygen kinetics, localization, or safety. |
| Verdict: flat-dose regime not robust | `analyze.py`, outputs | Legacy control plus central diagnostic rule | Reproducible by inspection; code not executed in daemon | Valid within exact diagnostic scope. |
| Grid fractions | outputs | Sensitivity summary | Full-factorial selected levels | Not probabilities or uncertainty estimates. |

## Affected wiki pages
- `wiki/computational-experiments.md` — already consistent — bounded comp-044 entry and forbidden inferences present.
- `wiki/gut-lumen-uricase-physiologic-regime-computational.md` — already consistent — focused page owns limitations and gates.
- `wiki/validation-experiments.md` — change required outside comp-044 — §1.33 is consistent, but unrelated sections contain material technical/provenance QA issues.
- `wiki/delivery-route-matrix.md` — already consistent — no route promotion from comp-044.
- `wiki/dual-chassis-ecn-pdb-uricase-computational.md` — already consistent — no recovery of invalid comp-031 topology claims.
- `wiki/gout-action-guide.md` — already consistent — research-only, no clinical guidance.
- `wiki/gout-multihop-research-program.md` — already consistent — preserves exact-configuration and safety gates.
- `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` — already consistent — hypothesis remains open with survival_count 0.
- `wiki/open-questions.md` — already consistent for comp-044 — no replacement genotype/dose model.
- `wiki/etc/GRAPH.md` — already consistent — comp-044 routed as audit, not validation.

## New connections or implications
Comp-044 strengthens the rationale for validation §1.33’s low-substrate physiological arm: high-substrate or saturated positives cannot rescue the old flat-dose claim without product formation at the human-baseline substrate prior and without peroxide/viability penalties.

Research Conjecture boundary: if exact UOX configurations later show activity at low jejunal urate while controlling peroxide and maintaining persistence, the gut-sink hypothesis remains testable; comp-044 itself provides only the counterexample to the old saturated-regime shortcut.

## Required actions
1. Triage `wiki/validation-experiments.md` non-comp-044 QA issues found during full-page audit, especially the 16S-versus-fungal-dominance error and threshold/provenance ambiguities. Verification criterion: affected sections either corrected, explicitly marked provisional, or moved to a separate QA issue without relying on them as binding gates.
2. When propagating comp-044, include the forbidden-inference boundary verbatim or equivalently: no serum effect, dose, genotype order, true physiological regime, topology/chassis selection, production sufficiency, safety, or probabilistic grid interpretation.

## Review limits
I did not execute `analyze.py`, consistent with daemon-mode rules. Primary sources behind inherited activity, Km, active-window, and flux priors were not independently verified. Repository fixed-string search failed because the search backend was unavailable; affected-surface assurance therefore relies on the supplied hash-bound shard coverage plus targeted file reads. The supplied manifest hash could not be reopened as a text file via tool, but the daemon brief reported modern valid authoring gates and no deterministic blocks.
