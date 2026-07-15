---
type: comp-review
sweep_date: 2026-07-15
sweep_sha: eeab5b5
comp: comp-045
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-045

Canonical review log: [`logs/comp-reviews/2026-07-15-comp-045-eeab5b5.md`](../../logs/comp-reviews/2026-07-15-comp-045-eeab5b5.md)

ACTION_REQUIRED: yes

REVIEWED_SNAPSHOT: commit:eeab5b53054b93544c428a476dad06a8f8fe2621

# Independent comp review — comp-045

## Reviewed snapshot

Independent reviewer: API audit reviewer. Reviewed daemon snapshot `eeab5b53054b93544c428a476dad06a8f8fe2621`.

The tracked comp-045 files supplied in the bundle were inspected. I also used repository reads to inspect the full `outputs/results.json` in two chunks because the bundle excerpt was truncated. The inspected artifact content matched the trigger diff’s intended correction from `indirect_empirical_support` to `joint_module_precedent_isolated_unresolved` in generated JSON for the affected secreted/displayed EcN isolated KatG/VHb arms.

## Bottom-line verdict

Action required. The artifact is materially useful as a randomized decision-design generator, but the artifact-summary-wiki contract is not clean:

1. Several wiki surfaces still say “indirect empirical support” for secreted/displayed KatG+VHb, despite the commit’s core correction that isolated KatG-only/VHb-only arms inherit only joint-module precedent.
2. `inputs/provenance.md` still defines the evidence-state vocabulary using “indirect empirical support,” which is stale relative to `design_factors.json`, `analyze.py`, and `results.json`.
3. The implementation may still overstate **isolated intracellular KatG-only** and **isolated intracellular VHb-only** evidence as `direct_empirical_support`, despite the provenance and summary stating that KatG and VHb were introduced jointly in key precedents and that independent effects require the proposed separate arms.

## Implementation and constraint closure

I traced `inputs/design_factors.json` into `analyze.py` and then into both generated outputs:

- `topologies`, `peroxide_strategies`, `oxygen_support`, and `oxygen_contexts` are dynamically iterated.
- `supports_vhb` is implemented: `koji_free_secretion` correctly excludes VHb arms.
- The duplicate intracellular `compartment_matched_catalase` physical construct is excluded in code.
- `urate_concentrations_uM`, `biological_runs`, `random_seed`, and `shared_controls_per_plate` drive plate-map construction.
- `primary_readouts` are propagated to `results.json` and `summary.md`.
- Some heuristic “unused” leaves are documentation/provenance-only rather than code bugs: `purpose`, `scope`, `natural_product_scope`, `framings`, `urate_concentration_roles`, and `evidence_states` are not computationally required for plate generation.

Arithmetic/design closure by inspection:

- Base factorial conditions: 19.
- Per plate: `19 × 3 = 57` factorial wells.
- Controls per plate: four inactive-UOX controls × 3 = 12; EcN no-UOX × 3 = 3; koji no-UOX × 3 = 3; EcN no-urate = 1; koji no-urate = 1; PULSE mixture × 3 = 3; medium blank = 1; total controls = 24.
- Total per plate: 57 + 24 = 81, matching `results.json` and `summary.md`.
- Six plates = three biological runs × two oxygen contexts.
- Plate maps assign wells A1–G9 only, leaving unused wells; no >96-well overflow.

Important implementation caveat:

- `graded_conditions` repeats the same 19 condition IDs for each run/context without including `biological_run`. This is not a fatal design error because plate maps carry run IDs, but the `graded_conditions` array contains duplicate records indistinguishable by run except for oxygen context. If downstream parsers treat `condition_id + oxygen_context` as unique, they will see repeated duplicates. The summary’s “19 valid conditions” remains correct for base conditions.

Constraint closure:

- Reaction chemistry is treated qualitatively, not kinetically: UOX consumes urate and O₂ and produces allantoin/pathway product plus H₂O₂; the design requires urate/product, H₂O₂, dissolved O₂, viability, and localization readouts. It does not compute reaction rates, O₂ demand, Km effects, residence time, diffusion, replenishment, or epithelial exposure.
- The design does not model finite mass balance or physiological turnover. That is acceptable only because the stated question is experimental design, not efficacy prediction.
- Compartment logic is mostly explicit: intracellular KatG is directly co-localized only with intracellular UOX; extracellular/surface catalase is a proposed construct; intracellular KatG may reduce cell-associated ROS after diffusion without closing extracellular epithelial exposure.
- The dominant unresolved biology remains: substrate at 0.59 µM relative to UOX Km, oxygen availability in microoxic gut-like contexts, localization, H₂O₂ peaks, viability, and whether measured product formation at the human-baseline arm exists at all.

Implementation concern requiring action:

- The trigger corrected isolated KatG/VHb support for **secreted/displayed EcN** arms to `joint_module_precedent_isolated_unresolved`.
- However, the same provenance statement says “KatG and VHb were combined in the principal PULSE/Zhao comparisons; their independent contributions were not fully isolated.” The code still assigns:
  - intracellular + VHb + no peroxide module, microoxic: `oxygen_status = direct_empirical_support`;
  - intracellular + KatG/native catalase + no VHb: `peroxide_status = direct_empirical_support`.
- If the evidence state is meant to describe isolated module support, those intracellular isolated arms are likely overstated. If the intended meaning is “direct support for the combined intracellular closed-loop architecture,” then the code should reserve direct support for the combined intracellular KatG+VHb arm or rename/clarify the status fields.

## Summary-fidelity audit

Inspected summaries and wiki surfaces show partial but incomplete propagation.

Consistent surfaces:

- `README.md` correctly frames comp-045 as deterministic design, not efficacy ranking.
- `outputs/summary.md` matches generated counts: 19 conditions, 3 urate concentrations, 3 biological runs × 2 oxygen contexts, 6 plates, 81 wells/plate.
- `outputs/summary.md` correctly states that KatG and VHb were introduced jointly and that their independent effects require separate arms.
- `validation-experiments.md` §1.33 correctly describes the six-plate design, readouts, no serum-urate inference, and topology promotion rule.
- `gut-lumen-sink.md`, H08, and the multihop program page are directionally consistent that topology/peroxide/oxygen remain empirical gates and no clinical/serum-urate inference is allowed.

Mismatches requiring action:

- `wiki/uricase-topology-oxygen-peroxide-design-computational.md` still says evidence is graded as “direct support, **indirect empirical support**, proposed direct test...” even though `design_factors.json` removed `indirect_empirical_support`.
- The same interpretive page says “PULSE provides **indirect empirical support** for KatG+VHb benefit in secreted and displayed forms.” After this commit, the more precise statement should be “joint-module precedent; isolated KatG-only and VHb-only effects unresolved.”
- `wiki/computational-experiments.md` comp-045 verdict still says secreted/displayed forms have “**indirect empirical KatG+VHb support**,” which is the stale phrase this trigger was intended to correct.
- `inputs/provenance.md` still says the design uses graded states including “**indirect empirical support**,” while `design_factors.json` and `results.json` use `joint_module_precedent_isolated_unresolved`.
- `wiki/uricase-topology-oxygen-peroxide-design-computational.md` says “Independent peer review rejected...” which is historical/review-log content but does not reflect this trigger’s new correction. It should not imply that the current isolated-module evidence-state issue is fully closed.

## Generated-output and proposed-update inventory

| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-045-uricase-topology-oxygen-peroxide-design/README.md` | tracked artifact / summary | Yes | Counts and high-level design mostly faithful; does not expose the lingering intracellular isolated-module evidence-state ambiguity. |
| `wiki/etc/experiments/comp-045-uricase-topology-oxygen-peroxide-design/analyze.py` | tracked artifact / executable | Yes | Deterministic standard-library script; corrected secreted/displayed isolated KatG/VHb states; possible remaining overstatement for isolated intracellular KatG-only and VHb-only states. |
| `wiki/etc/experiments/comp-045-uricase-topology-oxygen-peroxide-design/inputs/design_factors.json` | tracked artifact / input | Yes | Inputs close to code; `evidence_states` updated to include `joint_module_precedent_isolated_unresolved`; documentation-only leaves not all used computationally. |
| `wiki/etc/experiments/comp-045-uricase-topology-oxygen-peroxide-design/inputs/provenance.md` | tracked artifact / provenance | Yes | Stale vocabulary: still lists “indirect empirical support.” Provides citation anchors but primary sources were not independently verified in this review. |
| `wiki/etc/experiments/comp-045-uricase-topology-oxygen-peroxide-design/inputs/query-strategy.json` | tracked artifact / input | Yes | Documentation/literature-framing only; no implementation dependency expected. |
| `wiki/etc/experiments/comp-045-uricase-topology-oxygen-peroxide-design/outputs/results.json` | generated output | Yes | Fully read via repository chunked read; counts/plate maps internally coherent; contains new `joint_module_precedent_isolated_unresolved` status for secreted/displayed isolated-module precedent. |
| `wiki/etc/experiments/comp-045-uricase-topology-oxygen-peroxide-design/outputs/summary.md` | generated output | Yes | Counts match code; limitation language correctly states joint KatG/VHb precedent; does not surface possible intracellular isolated-module overstatement. |
| `wiki/uricase-topology-oxygen-peroxide-design-computational.md` | proposed/affected wiki surface | Yes | Change required: stale “indirect empirical support” language remains. |
| `wiki/computational-experiments.md` | proposed/affected wiki surface | Partially, comp-045 section read | Change required: comp-045 entry still says secreted/displayed have “indirect empirical KatG+VHb support.” |
| `wiki/validation-experiments.md` | affected wiki surface | Relevant §1.33 read | Already mostly consistent with design and no-efficacy boundary. |
| `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` | affected wiki surface | Yes from bundle | Already consistent with no topology eliminated and no numeric ΔSUA prior. |
| `wiki/gut-lumen-sink.md` | affected wiki surface | Relevant comp/PULSE sections read | Already mostly consistent: describes PULSE as topology-diverse and points to comp-044/045 gates. |
| `wiki/gout-multihop-research-program.md` | affected wiki surface | Yes from bundle | Already consistent at program level. |

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| 0.59 µM human jejunal urate baseline | `inputs/design_factors.json`, `inputs/provenance.md`, `summary.md` | Used as one of three urate arms in every factorial/control condition | Citation string to Miyazaki 2025 and conversion note via comp-044; primary source not independently checked here | Accept as artifact-supported, not primary-verified |
| 50 µM sensitivity arm | `design_factors.json`, `summary.md` | Used as middle urate arm | Labeled sensitivity; no primary physiological claim | OK |
| 250 µM PULSE benchmark arm | `design_factors.json`, `provenance.md`, `summary.md` | Used as benchmark urate arm | Citation to Gao/PULSE; primary not independently checked | Accept as artifact-supported, not primary-verified |
| Four topologies: intracellular+YgfU, LamB-secreted, InakN-displayed, koji free secretion | `design_factors.json`, `provenance.md` | Drives factorial conditions and substrate evidence state | Gao/PULSE and other citations for EcN; koji is proposed/testable | Mostly OK; koji remains proposed |
| `supports_vhb = false` for koji | `design_factors.json` | Excludes koji VHb arms | Design choice; no direct source needed | OK |
| 19 base factorial conditions | `analyze.py`, `results.json`, `summary.md` | Derived by Cartesian product minus invalid/duplicate arms | Directly reproducible by inspection | OK |
| 81 wells/plate | `analyze.py`, `results.json`, `summary.md` | Derived from 57 factorial + 24 controls | Directly reproducible by inspection | OK |
| No topology eliminated | `README.md`, `results.json`, `summary.md`, wiki pages | Verdict only; no ranking implemented | Supported by design-only model, not efficacy data | OK with limitation |
| Secreted/displayed isolated KatG-only or VHb-only support is not isolated empirical support | `analyze.py`, `design_factors.json`, `results.json` | Implemented as `joint_module_precedent_isolated_unresolved` | Supported by provenance statement that PULSE used joint KatG+VHb | Corrected in outputs; wiki propagation incomplete |
| Intracellular isolated KatG-only and VHb-only direct support | `analyze.py`, `results.json` | Implemented as `direct_empirical_support` for intracellular isolated arms | Provenance says KatG and VHb were combined in key precedents and independent contributions not fully isolated | Needs clarification/correction |
| Compartment-matched extracellular/surface catalase is proposed, not published | `design_factors.json`, `provenance.md`, `summary.md` | Implemented as `proposed_direct_test` except intracellular duplicate excluded | Supported by artifact provenance; primary not checked | OK |
| Required readouts: urate, product, H₂O₂, dissolved O₂, viability, localization | `design_factors.json`, `results.json`, `summary.md` | Propagated into outputs | Mechanistically appropriate | OK |
| Deterministic reproduction with `python3 analyze.py` | `README.md`, `analyze.py` | Standard library, fixed seed | Not executed in daemon mode | Plausible by inspection |

## Affected wiki pages

- `wiki/uricase-topology-oxygen-peroxide-design-computational.md` — change required — still uses “indirect empirical support” in the evidence vocabulary and mechanism-axis text; should use the corrected joint-module/isolated-unresolved framing.
- `wiki/computational-experiments.md` — change required — comp-045 entry still says secreted/displayed forms have “indirect empirical KatG+VHb support,” which is materially stronger/less precise than the corrected artifact state for isolated module arms.
- `wiki/validation-experiments.md` — already consistent — §1.33 describes the factorial design, readouts, and no-serum-urate boundary; no obvious stale indirect-support wording found in the inspected section.
- `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` — already consistent — no topology winner and no numeric ΔSUA prior; points to comp-045 as design gate.
- `wiki/gut-lumen-sink.md` — already mostly consistent — describes PULSE as topology-diverse and says topology/oxygen/peroxide remain gates; no immediate action from this trigger.
- `wiki/gout-multihop-research-program.md` — already consistent — correctly states UOX topology and peroxide handling cannot be separated and points to §1.33.
- `wiki/etc/experiments/comp-045-uricase-topology-oxygen-peroxide-design/inputs/provenance.md` — change required — not a top-level wiki page, but part of the artifact; its evidence-state vocabulary is stale and contradicts `design_factors.json`.

## New connections or implications

The correction from “indirect empirical support” to “joint-module precedent; isolated unresolved” has a broader implication than the trigger diff applied: if KatG and VHb were jointly introduced in the key intracellular precedents too, the factorial’s isolated intracellular KatG-only and VHb-only arms should not be labeled as having isolated direct empirical support unless the authors can cite a source that separated those modules. The strongest evidence is for the **closed-loop intracellular combined module**, not necessarily for each isolated module.

This matters for §1.33 interpretation: a positive intracellular KatG+VHb combined arm would be precedent-concordant, but a KatG-only or VHb-only result should still be treated as an empirical isolation test rather than a confirmation of a directly supported isolated module.

## Required actions

1. Update `wiki/uricase-topology-oxygen-peroxide-design-computational.md` to replace “indirect empirical support” language with the corrected “joint-module precedent; isolated KatG/VHb effects unresolved” wording. Verification criterion: no remaining claim that secreted/displayed isolated KatG-only or VHb-only arms have indirect empirical support as isolated modules.
2. Update `wiki/computational-experiments.md` comp-045 entry to remove “secreted/displayed forms have indirect empirical KatG+VHb support” or rephrase it as joint-module precedent with isolated effects unresolved. Verification criterion: comp-045 index wording matches `results.json`.
3. Update `inputs/provenance.md` evidence-state vocabulary to remove “indirect empirical support” and define `joint_module_precedent_isolated_unresolved`. Verification criterion: provenance vocabulary matches `design_factors.json`.
4. Resolve the intracellular isolated-module evidence-state ambiguity in `analyze.py`: either cite and document direct isolated empirical support for intracellular KatG-only and VHb-only arms, or downgrade those isolated intracellular module statuses to joint-module/isolated-unresolved while preserving direct support for the combined intracellular architecture. Verification criterion: `results.json`, `summary.md`, and provenance consistently distinguish combined-module precedent from isolated-module support.
5. Regenerate outputs after any `analyze.py` or input vocabulary change and re-check `outputs/results.json` plus `outputs/summary.md`.

## Review limits

- I did not execute `python3 analyze.py`; daemon-mode review was by inspection only.
- Primary papers named in provenance were not independently opened or verified; I treated citation strings and artifact provenance as unverified source anchors.
- Repository `grep_repo` failed because the underlying `rg` executable was unavailable, so affected-page search relied on the supplied explicit pages and direct repository reads rather than full fixed-string search.
- Bundle omitted some potentially affected pages such as `engineered-koji-protocol.md`, `delivery-route-matrix.md`, `gout-kill-chain-delivery-routes.md`, and `uricase.md`; I did not inspect them after the search-tool failure.
