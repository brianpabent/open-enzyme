COMP_VERDICT: clean_with_limitations
REVIEWED_SNAPSHOT: 95076ab1c4e287024aa1e178f463a025d55131c99f2d07dfd0a28239ffc0e3da
PROPAGATION_ELIGIBILITY: eligible_with_warning
SYNTHESIS_ELIGIBILITY: eligible_with_warning
ACTION_REQUIRED: no
PROPAGATION_ALLOWED_SCOPE: bounded corrective propagation that comp-019's unconditional flat-dose oral-UOX classification is not robust to comp-044's tested substrate-occupancy and finite-window diagnostics
SYNTHESIS_ALLOWED_SCOPE: cite only as a deterministic consistency audit preserving the oral gut-sink hypothesis as open and requiring configuration-level measurement before dose, topology, or safety conclusions
FORBIDDEN_INFERENCES: replacement physiological regime; serum-urate or ΔSUA prediction; clinical advice; genotype ordering; sufficient oral dose or production/yield target; topology or chassis winner; safety or peroxide closure; probabilistic interpretation of grid fractions; primary-source-verified quantitative planning inputs

# Independent comp review — comp-044

## Reviewed snapshot
Independent daemon reviewer; trigger snapshot `95076ab1c4e287024aa1e178f463a025d55131c99f2d07dfd0a28239ffc0e3da` at source commit `8c8be0642f5839afc2925b361c8746d2eaa252b6`. Authoring gates were reported modern and valid. No deterministic blocks were reported. Hash-bound shard coverage plus targeted repository reads matched the inspected comp-044 artifact and principal affected pages.

## Bottom-line verdict
Clean with limitations. The artifact supports its narrow verdict: comp-019’s unconditional flat-dose classification is not robust when the tested Michaelis–Menten occupancy term and finite active window are applied. The result is not a physiological gut model and does not establish dose sufficiency, serum effect, topology/chassis priority, or safety.

## Implementation and constraint closure
I traced the load-bearing computation from `model_parameters.json` through `analyze.py` to `outputs/results.json` and `outputs/summary.md`. The formula is fixed-concentration capacity: dose × specific activity × pH factor × 60 × hours × urate/(Km+urate) × oxygen × access × survival, converted from µmol urate to mg and divided by the legacy 233 mg/day intestinal-flux denominator. The named-scenario results and grid summaries are arithmetically consistent by inspection.

The implementation closes the stated binary decision rule: legacy 24 h saturated Vmax ratios all exceed one, while the central jejunal diagnostic ratios are 0.093 / 0.466 / 0.932 for 5 / 25 / 50 mg, all below one. The decision rule does not depend on grid occupancy. Grid size is internally consistent: 5 urate × 3 Km × 4 hours × 3 oxygen × 3 access × 3 survival = 1,620 cells per dose.

Constraints are explicitly not closed physiologically. Oxygen is only a dimensionless activity multiplier; stoichiometric O₂ demand, depletion, transport, spatial gradients, and kinetic coupling are not modeled. Hydrogen peroxide production, scavenging, local epithelial exposure, redox burden, and safety handling are outside comp-044. Urate depletion, replenishment, reabsorption, microbiome metabolism, renal compensation, genotype-specific supply, and serum-pool dynamics are also absent. This is acceptable because the artifact labels itself as a bounded regime audit, not an efficacy model.

Potential implementation fragility: duplicated grid/scenario consistency checks use Python `assert`, so `python -O` would disable them. The declared reproduction command uses normal `python3`, so this is not a current block.

## Summary-fidelity audit
`outputs/summary.md`, `results.json`, the README, `wiki/gut-lumen-uricase-physiologic-regime-computational.md`, `wiki/computational-experiments.md`, `wiki/delivery-route-matrix.md`, `wiki/dual-chassis-ecn-pdb-uricase-computational.md`, `wiki/gout-action-guide.md`, `wiki/gout-multihop-research-program.md`, `wiki/open-questions.md`, H08, and the inspected validation sections preserve the central boundary: comp-044 invalidates only the unconditional flat-dose robustness claim and supplies no replacement ΔSUA, dose, genotype ranking, topology/chassis winner, production sufficiency, or safety conclusion.

The pages inspected by shards also correctly keep comp-031 invalidated and prevent recovery of its additive serum-urate or topology recommendation. Comp-045 provenance is consistent with comp-044’s boundary: no numerical topology ranking exists because the relevant topology × oxygen × catalase combinations at human jejunal urate concentrations were not jointly tested in primary evidence.

## Reader-facing ownership audit
The canonical comp-044 page owns the evidence, provenance caveats, omitted physiology, and follow-up gate. Portfolio comparison surfaces limit themselves to cross-route or cross-track context and do not convert comp-044 into a chassis ranking. The action guide maintains the non-clinical research-roadmap contract and does not give personalized engineered-UOX use instructions. No inspected page used comp-044 as a narrative foil for home treatment, food-safety transfer, or editorial phase history.

## Conjecture preservation audit
The negative result kills only the exact old claim: the comp-019 unconditional flat-dose/substrate-limited robustness classification under omitted occupancy and 24 h full-activity assumptions. It does not kill the gut-lumen sink hypothesis. Surviving conjecture: oral luminal UOX may remain useful if exact configurations show adequate local urate disposal at physiological substrate, oxygen, residence, access, and survival without peroxide/barrier injury. This is correctly preserved as a Research Conjecture-style platform hypothesis in H08 and routed to configuration-level validation rather than being stated as established efficacy.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/README.md` | comp artifact / proposed contract | yes | Branch contract and limits are aligned with generated verdict. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/analyze.py` | comp source | yes | Implements stated deterministic ratio audit; no hidden serum model. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/inputs/model_parameters.json` | comp input | yes | Scenario values and inherited priors clearly separated. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/inputs/provenance.md` | comp input/provenance | yes | Correctly labels non-planning-grade inherited priors. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/inputs/query-strategy.json` | comp input/provenance | yes | Framing-only; not misused as quantitative support. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/outputs/results.json` | generated output | yes | Numerically and semantically consistent with code and inputs. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/outputs/summary.md` | generated output | yes | Faithful; preserves forbidden inferences. |
| `wiki/computational-experiments.md` | proposed/affected wiki update | yes | Correct bounded index entry. |
| `wiki/delivery-route-matrix.md` | proposed/affected wiki update | yes | No oral production sufficiency or route ranking from comp-044. |
| `wiki/dual-chassis-ecn-pdb-uricase-computational.md` | affected wiki update | yes | Uses comp-044 only to reopen regime uncertainty. |
| `wiki/etc/GRAPH.md` | affected corpus graph | yes | Dependency boundaries preserved. |
| `wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/reviews/push-review.md` | prior review check | yes | Prior limitations not over-propagated. |
| `wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/README.md` | affected invalidated comp | yes | Correctly retracts obsolete comp-031 claims. |
| `wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/inputs/provenance.md` | affected invalidated comp | yes | Rejected inputs remain rejected. |
| `wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/outputs/summary.md` | affected invalidation record | yes | Not treated as reproducible model output. |
| `wiki/etc/experiments/comp-045-uricase-topology-oxygen-peroxide-design/inputs/provenance.md` | affected comp provenance | yes | Correctly prevents topology ranking overreach. |
| `wiki/gout-action-guide.md` | affected reader page | yes | Non-clinical boundary maintained. |
| `wiki/gout-multihop-research-program.md` | affected program page | yes | Correct sequencing: construct characterization before §1.33 and safety before animals. |
| `wiki/gut-lumen-uricase-physiologic-regime-computational.md` | canonical proposed update | yes | Faithful interpretive page. |
| `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` | affected hypothesis | yes | Preserves open hypothesis without numeric ΔSUA. |
| `wiki/open-questions.md` | affected planning page | yes | Correctly blocks comp-019/031-derived dose, genotype, and additivity claims. |
| `wiki/validation-experiments.md` | affected validation page | yes | UOX ordering consistent; unrelated planning-number cautions noted as review limits, not comp-044 blockers. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| 0.59 µM central human jejunal urate | `model_parameters.json`; `provenance.md` | Occupancy numerator in central diagnostic | Inherited Miyazaki extraction; arithmetic conversion stated; primary not reverified here | Adequate for bounded audit, not planning. |
| Urate range 0.06–1.16 µM | inputs | Grid/sensitivity levels | Inherited extraction | Adequate as selected design grid. |
| Km 25 µM central; 5–100 µM range | inputs | Occupancy denominator | Inherited enzyme/regulatory prior; enzyme-context dependent | Adequate only as uncertainty range. |
| Specific activity 8.3 U/mg | inputs/code | Converts dose to µmol/min capacity | Inherited prior, not primary-source verified | Non-planning-grade; correctly labeled. |
| pH/activity factor 0.75 | inputs/code | Scenario multiplier | Inherited scenario multiplier, not direct measurement | Acceptable as labeled scenario value. |
| Active window 2–4 h; central 3 h | inputs/code | Capacity time multiplier | Inherited physiology prior | Acceptable for robustness counterexample only. |
| Legacy intestinal urate flux 233 mg/day | inputs/code | Capacity-ratio denominator | Derived corpus prior, not local/patient measurement | Usable only for diagnostic comparison. |
| Oxygen/access/survival factors | inputs/code | Multiplicative scenario penalties | Scenario-only, nonmechanistic | Not evidence of physiology; correctly bounded. |
| Ratio-one boundary | code/results | Decision threshold | Direct mass-balance interpretation within diagnostic denominator | Valid for narrow decision rule. |
| Grid fractions below one | results/summary | Design-space summaries | Equal-weight discrete grid, not probability | Correctly labeled non-probabilistic. |

## Affected wiki pages
- `wiki/gut-lumen-uricase-physiologic-regime-computational.md` — already consistent — canonical page states bounded counterexample and no dose/serum/topology/safety conclusion.
- `wiki/computational-experiments.md` — already consistent — index reports central ratios and inherited-input limits.
- `wiki/delivery-route-matrix.md` — already consistent — route-specific gates retained without oral sufficiency ranking.
- `wiki/dual-chassis-ecn-pdb-uricase-computational.md` — already consistent — comp-031 remains invalidated; comp-044 only reopens UOX regime.
- `wiki/etc/GRAPH.md` — already consistent — dependencies preserve conjecture boundaries.
- `wiki/gout-action-guide.md` — already consistent — no clinical or personalized engineered-UOX advice.
- `wiki/gout-multihop-research-program.md` — already consistent — correct order of construct supply, physiological screen, and safety.
- `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` — already consistent — platform hypothesis remains open without numeric effect.
- `wiki/open-questions.md` — already consistent — genotype, topology, and additivity remain controlled questions.
- `wiki/validation-experiments.md` — already consistent for comp-044 UOX sequencing — unrelated design-threshold cautions should be handled in their own reviews if material to those experiments.

## New connections or implications
Comp-044 strengthens the need to treat “label UOX units” and “delivered physiological reaction rate” as separate quantities across the oral-UOX corpus. Research Conjecture boundary: if exact constructs preserve activity at sub-Km jejunal urate while managing oxygen and peroxide locally, the gut-lumen sink remains plausible; if §1.33 cannot show reproducible disposal at physiological substrate without redox injury, the oral-UOX mechanism should be killed before assigning any human serum-effect threshold.

## Required actions
1. None for comp-044 propagation or synthesis at this snapshot.

## Review limits
Arbitrary experiment code was not executed in daemon mode. Primary sources behind inherited priors were not independently opened or verified; the artifact appropriately labels those values as inherited/non-planning-grade. Repository fixed-string search failed because `rg` was unavailable in the tool environment, so affected-surface assessment relies on the hash-bound shard coverage plus targeted file reads rather than a fresh repo-wide grep. Unrelated issues observed in `validation-experiments.md` are not adjudicated as comp-044 blockers.
