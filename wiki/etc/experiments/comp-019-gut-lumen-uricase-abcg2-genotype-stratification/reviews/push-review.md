COMP_VERDICT: action_required
REVIEWED_SNAPSHOT: 1ec63b843755383c76e32ab847f05145a2255ab88b8978e8ff7959aa5e38b34a
PROPAGATION_ELIGIBILITY: eligible_with_warning
SYNTHESIS_ELIGIBILITY: eligible_with_warning
ACTION_REQUIRED: yes
PROPAGATION_ALLOWED_SCOPE: corrective propagation of comp-019 invalidation and bounded search observation only
SYNTHESIS_ALLOWED_SCOPE: cite only as invalidated tombstone/audit lesson and as bounded no-Q141K-stratified-outcome search result
FORBIDDEN_INFERENCES: comp-019 ΔSUA estimates; dose or yield conclusions; genotype responder ordering; flat-dose adequacy; topology or chassis selection; efficacy or safety claims; trial-design implications; treating bounded search as universal absence

# Independent comp review — comp-019

## Reviewed snapshot
Daemon independent review for comp-019 at supplied push-review manifest SHA-256 `1ec63b843755383c76e32ab847f05145a2255ab88b8978e8ff7959aa5e38b34a`, source commit `6efddd88c579c3827c6fe4a8664e342da976df7c`. Authoring gates were reported modern and valid. Shard auditors reported complete inspection of all supplied text spans; targeted reads of the comp-019 tombstone, invalidation record, interpretive page, and computational index matched the invalidated-tombstone state. Local `push-review.manifest.json` was not readable as a repo file, and repository grep was unavailable due missing `rg`; this limits independent corpus discovery beyond supplied shard coverage and targeted reads.

## Bottom-line verdict
Action required, but the bounded current result is usable with warnings. The live comp-019 artifact correctly retires the old model: Phase B did not use physiological substrate occupancy/Km and assumed saturated 24 h activity, so the quantitative verdict is invalidated. Current pages mostly enforce that no comp-019 ΔSUA, dose, genotype order, efficacy, safety, or topology claim survives. Required actions are corpus-maintenance issues: add comp-045 to the comp-019 README current evidence-owner/replacement list, and close existing UOX-related validation/provenance inconsistencies before any wider synthesis.

## Implementation and constraint closure
The current implementation is not a runnable model; it is a hash-bound tombstone. `invalidation.json` records retired commit, retired file hashes, non-runnable status, invalidated scopes, and surviving scope. This is appropriate because the old executable artifact answered the wrong physical question: nominal uricase capacity was treated as if substrate-saturated for a whole day, while stored luminal urate concentration, UOX Km, finite active window, oxygen/access/survival, replenishment, and transit constraints were not closed.

Constraint closure is therefore negative rather than affirmative. Reaction substrates and products for UOX, oxygen demand, peroxide production, local urate access, compartment exposure, genotype-dependent supply, and serum mapping remain unmodeled by comp-019. COMP-044 gives only an internal-consistency counterexample to the unconditional flat-dose classification; it does not establish the true physiological regime. Validation §1.33 and §1.36 now own empirical topology/oxygen/peroxide and antioxidant-loss/H₂O₂ safety gates. The current tombstone correctly prevents resurrection of retired numerical outputs.

## Summary-fidelity audit
The comp-019 README, `invalidation.json`, interpretive page, and computational-experiments index agree on the main decision: comp-019 is non-runnable and not decision-usable. They preserve only the bounded Phase A search observation: sources searched as of 2026-05-08 contained no Q141K-stratified uricase clinical outcome, not proof of universal absence.

Material fidelity is good across reviewed surfaces: gout action, genetic variants, multihop program, comp-044 interpretive page, and open questions preserve “no replacement ΔSUA/dose/genotype order/topology/safety” wording. The minor mismatch is that the computational index lists comp-045 as a replacement/gate for topology/peroxide evidence, while the comp-019 README current evidence-owner list names comp-044, validation §1.33, and §1.36 but omits comp-045. Existing comp-044 review actions also remain relevant: validation dashboard/protocol inconsistencies, §1.34 “yanthine” analyte issue, and an invalidation-policy conflict should be resolved.

## Reader-facing ownership audit
Current focused pages mostly satisfy the reader contract. The comp-019 page owns its invalidation and surviving search boundary without giving medical instructions or portfolio rankings. UOX advancement is routed to configuration-specific validation gates, not to comp-019. Cross-track comparisons remain in computational-experiment and validation surfaces. No personalized treatment instructions or narrative foils were found in inspected comp-019-related pages. The README evidence-owner list should include comp-045 so readers can find topology/peroxide design ownership without relying on the portfolio index.

## Conjecture preservation audit
The unsupported factual assertions from the old model are appropriately killed only in their tested scope: saturated, flat-dose, genotype-order, serum-urate, dose/yield, trial-design, safety, and topology conclusions. Adjacent conjectures survive with boundaries: Q141K remains a prospective stratification variable; gut-lumen uricase remains an open track; UOX topology, oxygen, substrate access, peroxide burden, and finite exposure can be tested in §1.33/§1.36 and comp-045-style designs. The negative comp-019 result should not be used to delete all gut-lumen uricase concepts, only to prevent use of the invalidated numerical regime.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---|---|
| `wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/README.md` | push text | Yes | Correct non-runnable tombstone; omits comp-045 from current evidence owners. |
| `wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/invalidation.json` | push text | Yes | Hash-bound retirement record; invalidated/surviving scopes clear. |
| `wiki/computational-experiments.md` | push text | Yes | Comp-019 index aligned; includes comp-044/045/validation replacement gates. |
| `wiki/uricase-abcg2-genotype-stratification-computational.md` | push text | Yes | Correct invalidated-tombstone interpretation and forbidden uses. |
| `wiki/gut-lumen-uricase-physiologic-regime-computational.md` | push text | Yes | Correctly bounds comp-044 as counterexample, not replacement efficacy model. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/README.md` | push text | Yes | Bounded corrective branch; output-dependent authority noted. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/inputs/provenance.md` | push text | Yes | Priors inherited/non-planning-grade; no serum mapping. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/reviews/push-review.md` | review text | Yes | Clean-with-limitations; open maintenance actions remain. |
| `wiki/dual-chassis-ecn-pdb-uricase-computational.md` | push text | Yes | Correctly prevents comp-031 rehabilitation from comp-019 regime. |
| `wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/README.md` | push text | Yes | Requires new COMP for renewed dual-chassis analysis. |
| `wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/inputs/provenance.md` | push text | Yes | Rejects comp-019-derived quantitative priors. |
| `wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/reviews/post-run.md` | review text | Yes | Confirms inherited unsupported UOX anchor. |
| `wiki/etc/autonomous-screening-methodology.md` | push text | Yes | Labels comp-019 Monte Carlo outputs non-decision-grade. |
| `wiki/gout-action-guide.md` | push text | Yes | Medical boundary and no UOX dose/effect claim preserved. |
| `wiki/gout-genetic-variants.md` | push text | Yes | Q141K/UOX open question correctly bounded. |
| `wiki/gout-multihop-research-program.md` | push text | Yes | UOX sequencing through construct and validation gates preserved. |
| `wiki/open-questions.md` | push text | Yes | No comp-019 overreach; contains separate “yanthine” issue requiring action. |
| `wiki/validation-experiments.md` | push text, two spans covering file | Yes per shards | UOX §1.33/§1.36 boundaries correct; many unrelated validation caveats found. |
| `wiki/etc/experiments/comp-020-upstream-complement-verification-rerun/inputs/provenance.md` | push text | Yes | Independent of comp-019; no UOX support. |
| `wiki/etc/experiments/comp-020-upstream-complement-verification-rerun/inputs/query-strategy.md` | push text | Yes | Independent upstream-complement scope only. |
| `wiki/etc/experiments/comp-020-upstream-complement-verification-rerun/outputs/per-node-findings.md` | generated output | Yes | No comp-019 claim supported or leaked. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Comp-019 Phase B omitted physiological substrate occupancy and finite exposure | README; invalidation record; interpretive page | Basis for tombstone/non-runnable status | Verified by current artifact and corroborating comp-031/044 reviews; retired code not re-executed | Supports invalidation |
| Old ΔSUA/capacity/genotype/dose/topology claims invalid | `invalidation.json`; README | Defines forbidden scopes | Hash-bound retired file list available; current live tree does not retain executable outputs | Correct |
| Surviving no Q141K-stratified uricase clinical outcome search | README; interpretive page; `invalidation.json` | Only surviving comp-019 observation | Search sources not independently re-run; bounded as of 2026-05-08 | Usable only as bounded search observation |
| 0.59 µM jejunal urate prior | comp-044 provenance | Used by comp-044 diagnostic, not comp-019 live artifact | Inherited from comp-019 extraction; arithmetic checked, primary not newly verified | Non-planning-grade prior |
| Km 5–100 µM, central 25 µM; 8.3 U/mg activity | comp-044 provenance/review | Diagnostic sensitivity only | Inherited literature/regulatory priors; not newly primary-verified | Cannot support dose planning |
| 2–4 h active window; 233 mg/day denominator | comp-044 README/review | Diagnostic ratio denominator/window | Derived/inherited; finite-window correction demonstrates non-robustness only | Correctly bounded |
| UOX topology/peroxide safety | comp-045 index; validation §1.33/§1.36 | Future empirical gates | Design/validation surfaces inspected; not measured by comp-019 | Open, not inferred |

## Affected wiki pages
- `wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/README.md` — change required — add comp-045 as a current evidence owner/replacement topology-peroxide design surface.
- `wiki/computational-experiments.md` — already consistent — comp-019 entry blocks quantitative use and lists comp-044/045/validation replacement gates.
- `wiki/uricase-abcg2-genotype-stratification-computational.md` — already consistent — invalidated tombstone and bounded search wording.
- `wiki/gut-lumen-uricase-physiologic-regime-computational.md` — already consistent — comp-044 not overextended into efficacy/dose.
- `wiki/validation-experiments.md` — change required — close previously noted UOX dashboard/protocol inconsistencies and §1.34 analyte naming issue; §1.33/§1.36 boundaries themselves are appropriate.
- `wiki/gout-action-guide.md` — already consistent — no reader-facing UOX medical advice.
- `wiki/gout-genetic-variants.md` — already consistent — Q141K remains prospective/open.
- `wiki/gout-multihop-research-program.md` — already consistent — proper UOX gate sequencing.
- `wiki/dual-chassis-ecn-pdb-uricase-computational.md` — already consistent — does not rehabilitate comp-019-derived quantitative claims.
- `wiki/etc/autonomous-screening-methodology.md` — already consistent — identifies comp-019 outputs as non-decision-grade.

## New connections or implications
Comp-019’s failure is a reusable audit pattern: enzyme mass or nominal activity cannot substitute for physiologic reaction rate when substrate is far below Km, exposure is finite, oxygen/access are uncertain, and serum mapping is absent. This same boundary should govern comp-031-style additive UOX models and any future UOX topology comparison. Research Conjecture boundary: Q141K may still matter as a stratification variable if genotype changes intestinal urate supply into a validated luminal sink, but comp-019 provides no responder ordering or adequate-dose evidence; the discriminating observation is configuration-specific urate flux under human-baseline substrate with genotype-relevant supply modeling or matched clinical stratification.

## Required actions
1. Update `wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/README.md` current evidence owners to include comp-045 / `uricase-topology-oxygen-peroxide-design-computational.md`; verify the README and computational index list the same live UOX evidence surfaces.
2. Resolve the open comp-044 maintenance actions touching UOX propagation: validation dashboard/protocol inconsistencies, validation §1.34 “yanthine” analyte naming/justification, and the comp-019 invalidation-policy conflict; verify by re-reading affected validation and interpretive pages.
3. Do not propagate any comp-019-derived quantitative numbers, genotype ordering, dose, topology, or safety conclusions into synthesis; automated propagation may only carry the tombstone and bounded search observation.

## Review limits
No code was executed, and retired comp-019 code/outputs were not independently recovered from Git; the live artifact is intentionally non-runnable. Primary sources behind the Phase A search, urate concentration, Km, activity, and window priors were not independently verified. Repository fixed-string search failed because `rg` is unavailable, so affected-surface discovery relied on supplied complete shard audits plus targeted file reads. Local `push-review.manifest.json` was not readable as a repo file; this review is bound to the daemon-supplied manifest SHA and shard coverage.
