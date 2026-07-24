ACTION_REQUIRED: no
REVIEWED_SNAPSHOT: ecd53fe3d969474bd4dd4adeba8c530f4eac75289115d014fff1e64b72978892

# Independent comp review — comp-007

## Reviewed snapshot

Reviewer `/root/comp007_retirement_post_review_v4`; authoring post-manifest canonical SHA-256 `ecd53fe3d969474bd4dd4adeba8c530f4eac75289115d014fff1e64b72978892`. All two design and eight proposed-update entries matched the manifest byte counts and SHA-256 values and were inspected completely. The manifest file’s byte hash is distinct from its embedded canonical digest, as expected. The deletion of `synthesis/queue/comp-review-007.md`, which is outside the manifest, was separately inspected from Git history.

## Bottom-line verdict

**Clean with limitations.** The retirement is internally complete and materially faithful. COMP-007 is now a non-runnable, hash-bound tombstone; every rank, composite score, confidence verdict, shortlist, advancement decision, causal HDAC1/2/3 assignment, HSF1–Hsp90 explanation, HDAC6-centered safety inference, exposure proxy, and genotype overreach is withdrawn.

The seven labels survive only as an unranked historical inventory. The independent butyrate-induction evidence and pharmacological Q141K-rescue precedent are separated into a properly bounded Research Conjecture. The direct validation path now controls material identity, measured exposure, genotype, trafficking, ABCG2-attributed urate flux, direct transporter inhibition, barrier integrity, viability, and broader safety.

The prior COMP-007 queue actions are all closed by retirement or explicit correction. The exact COMP-015 misattribution is operationally handed to its existing queue item and remains barred from decision use.

## Implementation and constraint closure

Inspection of the retired implementation at Git tree `35fd84865925592d42cbc89c84f45b1c8a81ad9f` independently confirms the invalidation rationale:

- `typical_gut_concentration_uM` was stored and emitted but never entered the scoring calculation.
- Potency combined direct recombinant IC50s, bulk nuclear-extract observations, cellular protein changes, and analogical estimates.
- Unknown HDAC6 activity received the arbitrary constant `0.30`; selectivity used the arbitrary midpoint `10`.
- Gut exposure was represented only as `1 − oral_bioavailability_fraction`, which does not establish free epithelial exposure.
- A censored HDAC6 value was converted into a numerical score.
- The implementation did not model Q141K trafficking, urate as substrate, polarized intestinal transport, intracellular exposure, concentration-time behavior, ABCG2 inhibition, tissue localization, barrier injury, or broad safety.
- The code assigned HDAC1/2/3 as causal rescue targets and HDAC6 avoidance as the main safety discriminator without implementing or establishing either conclusion.

The retirement ledger reproduces exactly: all eight historical file byte counts and SHA-256 values match the named Git tree. Its canonical digest independently recomputes to `6bba6541f53060b84ea20ad6a5d5e36a47f1ad3c8c31d1e737e474ff32ff4e8e`.

Pre/post design equality also passes: both manifests contain the same two design files with identical bytes and hashes. No code, input, parameter, decision-rule, model, or sensitivity change occurred between gates.

Constraint closure is transferred appropriately to validation §1.22:

- Basseville-pattern positive and contrast controls must reproduce before candidate interpretation.
- Material identity, purity, stability, conversion products, free concentration, intracellular exposure, and exposure time are required.
- WT-only, Q141K-only, and WT/Q141K co-expression arms prevent genotype overreach.
- Surface abundance must be paired with ABCG2-attributed basolateral-to-apical urate flux.
- A direct ABCG2-inhibition counterscreen prevents apparent trafficking rescue from masking transporter inhibition.
- PPARγ perturbation separates endogenous induction from possible Q141K trafficking rescue.
- Intestinal versus hepatocyte effects, compound-specific off-targets, barrier integrity, viability, and toxicity replace HDAC6-only safety logic.

## Summary-fidelity audit

The retirement verdict is consistent across all proposed surfaces:

- The tombstone, focused COMP page, computational index, and dashboard all withdraw rank, score, shortlist, causal-isoform, HDAC6-safety, and advancement authority.
- The focused page presents the seven materials in an explicitly unranked table with compound-specific evidence modalities and missing decision evidence.
- The LBP page no longer treats butyrate as computationally prioritized or genotype-agnostic; it separates preclinical endogenous-ABCG2 induction from untested Q141K rescue.
- `open-questions.md` retains the route as an unresolved, functionally gated question without importing the old ranking.
- Validation §1.22 carries all seven labels unranked and requires the complete control pattern and direct functional readouts.
- Validation §1.14 separately direction-finds butyrate in WT and Q141K systems while explicitly stating that Basseville did not test butyrate. It does not turn the conjecture into a positive prior.
- Mechanism/stale-phrase searches covered COMP-007, the historical numerical scores, “rank 1,” “top three,” Stage 2 advancement, HSF1/Hsp90, class-I causal assignment, HDAC6 safety, direct butyrate rescue, and genotype-agnostic language. Remaining hits are explicit retirement statements, historical/log material, independently invalidated COMP artifacts, or properly labeled untested hypotheses.

The deleted COMP-007 queue item required seven actions. All are closed:

1. Broken generated-output links are moot because the generated outputs are retired from the live tree.
2. Misstated formula prose is removed with the invalid model.
3. The absent exposure/operating-regime axis is named as an invalidation reason; no revised rank is retained.
4. Arbitrary-parameter sensitivity is no longer needed because the quantitative model has no surviving decision use.
5. The misleading `used_estimate` output is removed.
6. HDAC6-only safety framing is explicitly invalidated and replaced by broad compound-specific safety testing.
7. All named reader-facing surfaces are reconciled.

The COMP-015 handoff is exact and operational: its queue item names `analyze.py`, README, `inputs/provenance.md`, `outputs/results.json`, and `outputs/summary.md`; requires removal of the false achievable-concentration/IC50 attribution; routes code/output changes through COMP-015’s authoring lifecycle; and requires regenerated outputs to contain no COMP-007 decision-rule attribution.

## Reader-facing ownership audit

Ownership is clean:

- `wiki/food-grade-hdaci-screen-computational.md` owns the invalidated COMP verdict, unranked evidence inventory, sourcing/delivery constraints, and direct falsification gate.
- `wiki/abcg2-modulators.md` owns the surviving dual-route Research Conjecture.
- `wiki/validation-experiments.md` owns the detailed experimental controls and decision rules.
- `wiki/computational-experiments.md` and `index.md` provide compact tracking/discovery summaries.
- `wiki/engineered-lbp-chassis.md` keeps the delivery implication local to the LBP track without presenting a chassis winner.
- `synthesis/queue/comp-review-015.md` owns the unresolved cross-COMP operational correction.

No proposed reader-facing surface contains editorial history, personalized treatment instructions, a cross-track ranking, a narrative foil, or duplicated long-form conjecture exposition.

## Conjecture preservation audit

The correction separates factual support from idea value correctly.

The surviving block in `wiki/abcg2-modulators.md` has the required shape:

- **Grounded premises:** Xie’s non-Q141K-specific, non-urate rat, primary mouse-enterocyte, and Caco-2 findings are tagged **In Vitro + Animal Model**; PPARγ antagonist/silencing support is limited to Caco-2. Basseville’s selected pharmacological-HDAC-inhibitor rescue is tagged **In Vitro**.
- **Novel leap:** one measured butyrate exposure might combine PPARγ-mediated endogenous induction with some Q141K trafficking rescue; direct evidence is explicitly absent.
- **Why it matters:** possible restoration of more intestinal urate-export capacity.
- **Discriminating observation:** polarized isogenic genotype arms, concentration-time series, PPARγ blockade, matched positive/negative controls, surface trafficking, ABCG2-attributed urate flux, exposure, barrier, viability, and inhibition measurements.

The negative retirement kills only COMP-007’s old model, quantitative ordering, causal assignments, and decisions. It does not erase the pharmacological rescue class, compound-specific testing, or the independent endogenous-ABCG2 induction route.

## Generated-output and proposed-update inventory

| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-007-food-grade-hdaci-screen/README.md` | design | Yes | Clean non-runnable tombstone; exact invalidated/surviving scopes and dependency owners |
| `wiki/etc/experiments/comp-007-food-grade-hdaci-screen/invalidation.json` | design | Yes | Ledger, canonical digest, invalidation boundary, and surviving scope reproduce |
| `index.md` | proposed_update | Yes | Compact invalidated-ranking summary; no stale priority |
| `synthesis/queue/comp-review-015.md` | proposed_update | Yes | Exact five-file attribution correction, lifecycle routing, and verification criterion |
| `wiki/abcg2-modulators.md` | proposed_update | Yes | Source modalities preserved; conjecture correctly shaped and bounded |
| `wiki/computational-experiments.md` | proposed_update | Yes | No rank, score, shortlist, causal isoform, safety, or advancement survives |
| `wiki/engineered-lbp-chassis.md` | proposed_update | Yes | No butyrate priority or genotype-agnostic claim; delivery and exposure gates explicit |
| `wiki/food-grade-hdaci-screen-computational.md` | proposed_update | Yes | Correct evidence owner; unranked inventory, sourcing, delivery, and direct test |
| `wiki/open-questions.md` | proposed_update | Yes | Surviving questions remain unresolved and functionally gated |
| `wiki/validation-experiments.md` | proposed_update | Yes | Control-pattern reproduction, genotype arms, flux attribution, exposure, and safety logic complete |

There are no `generated_output` entries in this retirement manifest.

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Retirement is non-runnable | Tombstone README; `invalidation.json` | Prevents use of invalid model | Explicit state; executable artifacts removed from live tree | Pass |
| Historical artifact identity | `retired_tree_commit`, `retired_files` | Auditability | All eight blobs reproduced from Git with exact bytes/hashes | Pass |
| Retirement canonical digest | `invalidation.json` | Detects scope mutation | Independently recomputed exactly | Pass |
| Pre/post design equality | pre/post manifests | Authoring lifecycle integrity | Same two design entries, bytes, and hashes | Pass |
| Old ranks/scores/shortlist invalid | All summary surfaces | Removes decision use | Old code/output inspected; invalidation covers formula and verdicts | Pass |
| Stored concentrations were unused | Old `analyze.py` and candidate inputs | Supports model invalidation | Values emitted only; not referenced by score | Pass |
| HDAC1/2/3 causality withdrawn | Tombstone, focused page, validation | Prevents causal overclaim | Basseville precedent retained without isoform assignment | Pass |
| HDAC6-only safety withdrawn | Same | Prevents false safety inference | Replaced by compound-specific off-target/toxicity testing | Pass |
| Xie modality boundary | Tombstone, focused page, conjecture | Grounds induction premise | Systems, genotype, substrate, and Caco-2 PPARγ limits explicit | Pass |
| Basseville modality boundary | Focused page, conjecture, §1.22 | Grounds rescue precedent/control logic | Selected pharmacological HDIs; **In Vitro**; no butyrate or urate claim | Pass |
| Seven candidates unranked | Tombstone, focused page, validation | Preserves inventory without priority | Explicitly no predictive or decision use | Pass |
| COMP-015 handoff | Tombstone README; queue item | Prevents false method inheritance | Exact files, lifecycle, and output verification named | Pass |
| COMP-007 queue deletion | Deleted queue via Git show | Closes prior action ledger | Every action closed by retirement/correction; deletion condition satisfied | Pass |

## Affected wiki pages

- `wiki/food-grade-hdaci-screen-computational.md` — already consistent — owns invalidation, inventory, exposure, and direct test.
- `wiki/abcg2-modulators.md` — already consistent — owns the bounded dual-route conjecture.
- `wiki/validation-experiments.md` — already consistent — implements the required controls and functional gates.
- `wiki/computational-experiments.md` — already consistent — tracks the retired verdict without surviving quantitative claims.
- `wiki/engineered-lbp-chassis.md` — already consistent — removes butyrate priority and genotype overreach.
- `wiki/open-questions.md` — already consistent — retains only unresolved, testable questions.
- `index.md` — already consistent — discovery summary matches the retirement.
- `synthesis/queue/comp-review-015.md` — already consistent — operational cross-COMP correction remains open under COMP-015.
- `synthesis/queue/comp-review-007.md` — deletion justified — all prior actions and the handoff condition are satisfied.

## New connections or implications

None found beyond the already preserved Research Conjecture. The artifact supports no additional cross-corpus inference.

## Required actions

1. None.

## Review limits

Static read-only review. The retired analysis was not executed. Historical code, inputs, outputs, and queue state were inspected through Git; current manifest files were hash-checked. Primary-paper full texts were not independently re-read, so this review verifies the corpus’s source modality, causality, and scope handling rather than re-adjudicating every primary experiment.
