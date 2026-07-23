COMP_VERDICT: clean_with_limitations
REVIEWED_SNAPSHOT: 5dede85c414fee37043b8486faab8ff3bd1ed6bff1843ccc38d93c85694b7a7e
PROPAGATION_ELIGIBILITY: eligible_with_warning
SYNTHESIS_ELIGIBILITY: eligible_with_warning
ACTION_REQUIRED: yes
PROPAGATION_ALLOWED_SCOPE: corrective-only propagation of comp-044’s bounded finding that comp-019 flat-dose regime is not robust to tested substrate-occupancy and finite-window diagnostics
SYNTHESIS_ALLOWED_SCOPE: bounded comp-044 synthesis as an internal-consistency audit and follow-up gate rationale only
FORBIDDEN_INFERENCES: no ΔSUA prediction; no oral UOX dose sufficiency; no genotype responder ordering; no topology/chassis winner; no production target; no peroxide or safety clearance; no probabilistic interpretation of grid occupancy; no physiological-regime reversal

# Independent comp review — comp-044

## Reviewed snapshot
Independent daemon consolidation reviewer; reviewed snapshot bound to supplied `push-review.manifest.json` SHA-256 `5dede85c414fee37043b8486faab8ff3bd1ed6bff1843ccc38d93c85694b7a7e` at source commit `50ecf5a9d8c3fcffbd0b2114e9fafd79ca907807`. Shard coverage reports complete inspection of all text spans supplied in the daemon manifest and no deterministic binary blocks. Targeted repository reads cross-checked `analyze.py`, `outputs/results.json`, the interpretive comp-044 page, `computational-experiments.md`, and relevant `validation-experiments.md` UOX sections. Fixed-string repository search was unavailable because `rg` was missing in the tool environment.

## Bottom-line verdict
Clean with limitations, with action required for non-blocking corpus maintenance. The implemented comp-044 arithmetic supports the narrow verdict: comp-019’s unconditional flat-dose classification is not robust once substrate occupancy and finite active window are applied under inherited priors. The result remains an internal consistency counterexample, not a replacement efficacy model. Corpus pages inspected are mostly faithful for comp-044, but unrelated and adjacent `validation-experiments.md` inconsistencies and a comp-019 invalidation-policy conflict still require correction.

## Implementation and constraint closure
The code computes capacity ratio as delivered UOX mass × specific activity × pH multiplier × minutes of activity × substrate fraction × oxygen/access/survival multipliers, converted from µmol urate to mg and divided by the legacy 233 mg/day intestinal-flux denominator. The `legacy_vmax_24h` control sets `urate_uM: null`, forcing substrate fraction to 1.0; this intentionally reproduces the old saturated-capacity framing and must not be read as physiological substrate access.

The central diagnostic uses 0.59 µM urate, Km 25 µM, and 3 hours. Output ratios 0.0932 / 0.4660 / 0.9320 for 5 / 25 / 50 mg match the implemented formula and all fall below 1, while saturated 24-hour control ratios are all ≥1. The decision rule is therefore implemented as declared.

Constraint closure is deliberately incomplete: uricase consumes urate and oxygen and produces oxidative intermediates/allantoin plus H₂O₂/CO₂ chemistry, but oxygen stoichiometry, depletion, peroxide generation/scavenging, tissue exposure, local depletion/replenishment, diffusion, reabsorption, microbiome metabolism, renal compensation, topology, and serum mapping are not modeled. Scenario multipliers for pH, oxygen, access, and survival are nonmechanistic. The 1,620-cell grids are sensitivity/occupancy scans, not probability distributions.

## Summary-fidelity audit
`outputs/results.json`, `outputs/summary.md`, README, the interpretive comp-044 page, `computational-experiments.md`, the delivery-route matrix, comp-031 invalidation page, comp-019 retirement surfaces, H08, open questions, and the UOX validation gates consistently preserve the bounded claim: comp-044 invalidates the old unconditional flat-dose regime but supplies no replacement dose, ΔSUA, genotype order, topology/chassis selection, yield target, or safety conclusion.

`validation-experiments.md` §1.33 is aligned with comp-044: exact configuration first, physiological product formation plus peroxide/viability readouts, no serum/dose/chassis inference. However, `validation-experiments.md` contains multiple dashboard/protocol inconsistencies elsewhere, including omitted registered sections, cost/timeline mismatches, matrix/lane ambiguities, and a likely `yanthine` typo in §1.34. These are not comp-044 verdict breakers but do impair corpus planning fidelity.

## Reader-facing ownership audit
The focused comp-044 page owns its evidence tier, limitations, and falsification boundary without turning into a route-ranking or treatment page. Portfolio-level comparisons remain in portfolio surfaces. The inspected gout action guide avoids personalized medical advice and correctly states that engineered gut-lumen UOX has no validated serum-effect, genotype-ordering, or dose model. No comp-044 page improperly promotes oral UOX, EcN, koji, rectal, IA, or systemic formats.

## Conjecture preservation audit
The exact comp-019 flat-dose/saturation claim is killed for decision use under the tested inputs and decision rule. Adjacent ideas survive: a gut-lumen urate sink remains open; Q141K remains a prospective stratification variable; topology, oxygen, peroxide, and access hypotheses remain testable; and dynamic compartmental modeling remains justified after measured §1.33 inputs. These should remain framed as hypotheses or Research Conjectures, not as rescued efficacy claims.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/README.md` | comp artifact | yes | Faithful bounded authoring contract; corrective propagation only. |
| `.../analyze.py` | comp code | yes | Implements declared ratio audit; legacy saturated control intentionally bypasses Km. |
| `.../inputs/model_parameters.json` | comp input | yes | Inherited/scenario priors; not planning-grade. |
| `.../inputs/provenance.md` | comp input | yes | Provenance limitations explicit. |
| `.../inputs/query-strategy.json` | comp input | yes | No independent literature completeness claim. |
| `.../outputs/results.json` | generated output | yes | Ratios and limitations support bounded verdict. |
| `.../outputs/summary.md` | generated output | yes | Faithful; no replacement efficacy claim. |
| `wiki/gut-lumen-uricase-physiologic-regime-computational.md` | proposed/affected wiki | yes | Faithful interpretive page. |
| `wiki/computational-experiments.md` | proposed/affected wiki | yes | Faithful comp-044 registry entry. |
| `wiki/delivery-route-matrix.md` | affected wiki | yes | Does not over-promote routes. |
| `wiki/dual-chassis-ecn-pdb-uricase-computational.md` | affected wiki | yes | Uses comp-044 only to reopen UOX regime. |
| `wiki/etc/GRAPH.md` | affected index | yes | Correct sequencing and forbidden inferences. |
| `wiki/etc/experiments/comp-019.../README.md` | affected artifact | yes | Supersession boundaries correct. |
| `wiki/etc/experiments/comp-019.../inputs/query_strategy.md` | affected artifact | yes | Historical search only. |
| `wiki/etc/experiments/comp-019.../outputs/flux_model_summary.md` | affected output | yes | Clearly invalidated for quantitative use. |
| `wiki/etc/experiments/comp-019.../outputs/phase_a_table.md` | affected output | yes | Preserves only dated no-identified-stratified-outcome claim. |
| `wiki/etc/experiments/comp-019.../reviews/pre-run.md` | prior review | yes | Confirms archival/retirement scope. |
| `wiki/etc/experiments/comp-019.../reviews/post-run.md` | prior review | yes | Static-inspection limit preserved. |
| `wiki/etc/experiments/comp-019.../reviews/push-review.md` | prior review | yes | Required policy-conflict action appears still relevant. |
| `wiki/etc/experiments/comp-031.../README.md` | affected artifact | yes | Invalidated; no recommendation survives. |
| `wiki/etc/experiments/comp-031.../inputs/provenance.md` | affected artifact | yes | Rejected inputs not reused. |
| `wiki/etc/experiments/comp-031.../outputs/summary.md` | affected output | yes | Invalidation consistent. |
| `wiki/etc/experiments/comp-045.../inputs/provenance.md` | affected artifact | yes | No topology rank; physiological substrate boundary retained. |
| `wiki/gout-action-guide.md` | affected reader page | yes | No medical/dose upgrade from comp-044. |
| `wiki/gout-multihop-research-program.md` | affected program page | yes | Correct staged UOX sequencing. |
| `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` | affected hypothesis | yes | Remains open with measured-input gates. |
| `wiki/open-questions.md` | affected wiki | yes | Follow-ups and safety/ethics boundaries preserved. |
| `wiki/validation-experiments.md` | affected wiki | yes | §1.33/1.36 aligned with comp-044; other dashboard/protocol inconsistencies require action. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| 8.3 U/mg UOX activity | parameters/provenance/results | Linear capacity multiplier | Inherited prior, not newly primary-source verified | OK for audit; not planning-grade |
| Km 25 µM central | parameters/analyze/results | Substrate fraction `urate/(Km+urate)` | Inherited enzyme-context range | OK for sensitivity; not dose selection |
| 0.59 µM jejunal urate | parameters/interpretive page | Central diagnostic substrate | Inherited extraction from Miyazaki; reviewer did not primary-source verify | Usable only as bounded prior |
| 2–4 h active window; 3 h central | parameters/analyze/results | Reaction time | Inherited physiology range | Dominant uncertainty; not patient-measured |
| 233 mg/day denominator | parameters/analyze/results | Capacity-ratio denominator | Derived corpus prior; not local-compartment measurement | Valid comparator only for internal audit |
| pH factor 0.75 | parameters/analyze | Linear multiplier | Scenario/inherited | Nonmechanistic |
| Oxygen/access/survival multipliers | parameters/analyze/grid | Linear penalties/sensitivities | Scenario-only | Descriptive only |
| Ratio = 1 boundary | analyze/results/summary | Decision threshold | Mass-balance boundary within diagnostic | Valid narrow boundary |
| Grid fractions below 1 | results/summary | Sensitivity occupancy | Full-factorial selected levels, no probability weights | Must not be interpreted as likelihood |
| Peroxide/safety | limitations/validation §1.36 | Not modeled | Requires wet-lab gate | No safety inference |

## Affected wiki pages
- `wiki/gut-lumen-uricase-physiologic-regime-computational.md` — already consistent — bounded audit and no dose/ΔSUA claim.
- `wiki/computational-experiments.md` — already consistent for comp-044 — registry preserves limitations and forbidden inferences.
- `wiki/validation-experiments.md` — change required — §1.33/1.36 are comp-044-consistent, but dashboard/protocol inconsistencies and §1.34 analyte typo impair planning.
- `wiki/delivery-route-matrix.md` — already consistent — no route promotion from comp-044.
- `wiki/gout-action-guide.md` — already consistent — no clinical advice or engineered-UOX dose model.
- `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` — already consistent — hypothesis remains open with measured-input gates.
- `wiki/open-questions.md` — already consistent — Q141K and oral/gut UOX follow-ups remain unresolved.
- `wiki/dual-chassis-ecn-pdb-uricase-computational.md` — already consistent — comp-031 remains invalidated.
- `wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/` — change required only for process policy — numerical outputs are correctly marked invalidated, but prior push review identified a live-tree executable-artifact vs invalidated-COMP policy conflict.
- `wiki/etc/GRAPH.md` — already consistent — dependency sequencing and forbidden inference list are correct.

## New connections or implications
Comp-044 makes §1.33 not just a topology experiment but the first place where substrate, oxygen, active UOX at reaction site, peroxide, and viability must be measured together. A high-substrate benchmark-positive UOX configuration should not pass the physiological gate unless it also forms product at the human-baseline substrate prior without peroxide/viability penalties.  

Research Conjecture boundary: low jejunal urate relative to Km may make local access/replenishment, not nominal enzyme mass, the dominant engineering problem. This is grounded in comp-044’s occupancy calculation but remains unproven until a dynamic local gut model and §1.33 measurements exist.

## Required actions
1. Correct `wiki/validation-experiments.md` dashboard/protocol inconsistencies: reconcile §1.10 cost, §1.10 lane count/numbering, dashboard omissions for §§1.26–1.32, §1.22 cost/weeks, §1.20 matrix dimensions, §1.25 host-strain wording, and other shard-noted planning mismatches. Verification: dashboard and detailed sections agree.
2. Fix or justify `wiki/validation-experiments.md` §1.34 “yanthine” analyte. Verification: product/analyte panel uses correct chemical names.
3. Resolve the comp-019 invalidation-policy conflict noted in its prior push review: either align live-tree artifacts with the invalidated-COMP convention or document the exception. Verification: `computational-experiments.md` convention and comp-019 folder contents no longer conflict.
4. Preserve comp-044 forbidden inferences in any future propagation: no ΔSUA, dose sufficiency, topology/chassis winner, production target, safety, or probability claim from this artifact.

## Review limits
No experiment code was executed in daemon mode. Primary sources were not independently opened or verified; provenance was assessed from committed artifact text and shard audits. Repository fixed-string search failed because `rg` was unavailable, so cross-corpus discovery relied on supplied hash-bound shard coverage plus targeted file reads. Binary artifacts were not present in the deterministic-block list.
