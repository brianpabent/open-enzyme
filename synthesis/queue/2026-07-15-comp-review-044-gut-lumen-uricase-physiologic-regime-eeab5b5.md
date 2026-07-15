---
type: comp-review
sweep_date: 2026-07-15
sweep_sha: eeab5b5
comp: comp-044
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-044

Canonical review log: [`logs/comp-reviews/2026-07-15-comp-044-eeab5b5.md`](../../logs/comp-reviews/2026-07-15-comp-044-eeab5b5.md)

ACTION_REQUIRED: yes

REVIEWED_SNAPSHOT: commit:eeab5b53054b93544c428a476dad06a8f8fe2621

# Independent comp review — comp-044

## Reviewed snapshot
Independent reviewer: OpenAI API reviewer. Snapshot reviewed in daemon mode at commit `eeab5b53054b93544c428a476dad06a8f8fe2621`.

The comp-044 experiment directory files in the bundle were inspected completely: `README.md`, `analyze.py`, all three input files, and both generated outputs. I also inspected the supplied explicit wiki surfaces and, for load-bearing propagation checks, additionally inspected `wiki/gut-lumen-sink.md` and `wiki/uricase.md`. I did not execute code, consistent with daemon-mode review. The inspected artifact contents matched the trigger diff and bundle excerpts.

## Bottom-line verdict
Action required. The comp-044 arithmetic and deterministic output are materially reproducible by inspection, and the trigger edit correctly softens the summary from “regime reversed” to “unconditional saturated/flat-dose classification not robust.” However, corpus propagation is not fully clean: `gut-lumen-sink.md` still contains broad dose-feasibility / “low local uricase suffices” language that is stronger than comp-044 supports, even though the page has a top-level reset notice. Several omitted uricase/koji/yeast pages also need targeted audit for stale 20–50 mg/day, yield-solved, or flat-dose claims.

## Implementation and constraint closure
The implemented model is simple and traceable:

- `capacity_ratio()` computes enzyme capacity from dose, specific activity, pH/activity multiplier, minutes per active window, Michaelis–Menten substrate occupancy, oxygen/access/survival multipliers, urate molecular weight, and the legacy 233 mg/day intestinal-flux denominator.
- For `urate_uM = null`, the model sets substrate fraction to 1.0, reproducing a legacy 24-hour Vmax-style saturated-capacity comparison.
- For the central diagnostic, substrate fraction is `0.59 / (25 + 0.59) ≈ 0.0231`, which is the main correction relative to comp-019-style Vmax use.
- The 5 mg central diagnostic calculation checks out by hand:  
  `5 mg × 8.3 U/mg × 0.75 × 60 min/h × 3 h × 0.59/(25.59) = ~129 µmol urate`,  
  `~129 µmol × 168.11 µg/µmol = ~21.7 mg`,  
  `21.7 / 233 = 0.0932`.
- The 25 mg and 50 mg central values are linear multiples: `0.466` and `0.932`.
- The grid size is consistent: `5 urate × 3 Km × 4 hours × 3 oxygen × 3 access × 3 survival = 1620` cells per dose.

Stored-but-unused / duplication findings:

- `measured_or_regulatory_priors.*` are not consumed programmatically. Their values are duplicated into `named_scenarios` and `exhaustive_grid`, which are the actual values used by the code.
- `scenario_only_values_not_measured_human_baselines.*` are likewise documentation/source-of-truth fields whose values are duplicated into scenarios/grid.
- Current duplicate values are internally consistent, so this is not an output-invalidating bug, but it is a reproducibility hazard: future edits to the “priors” block would silently not affect results unless the scenarios/grid are also edited.
- `query-strategy.json` is documentation-only and not expected to be used by the code.

Constraint closure:

- Reaction substrate/product reality is only partially represented. The modeled reaction is effectively urate consumption capacity; oxygen is a dimensionless activity multiplier, not stoichiometric O₂ mass balance or Michaelis oxygen kinetics.
- H₂O₂ production, allantoin/product fate, local redox burden, epithelial effects, and antioxidant loss are not modeled. The artifact correctly defers these to topology/peroxide validation.
- Finite exposure time is represented as active hours, but local residence, mixing, diffusion, replenishment, depletion, reabsorption, and transport from epithelium into lumen are not dynamically modeled.
- Localization and physical access are represented only by scalar scenario multipliers. No topology-specific access or compartmental geometry is implemented.
- The daily 233 mg denominator and local jejunal concentration are different physical quantities. The artifact acknowledges this; the calculation is best interpreted as a regime-audit diagnostic, not a physiological flux closure.
- Sensitivity ranges cover some dominant uncertainties: urate concentration, Km, active window, oxygen, access, survival. They do not mechanistically cover oxygen kinetics, local volume/replenishment, topology-specific peroxide management, host transport capacity, enzyme decay kinetics, or covariance among scenario factors.

## Summary-fidelity audit
Artifact-level fidelity is mostly good after the trigger edit:

- `outputs/results.json` matches the code structure and numerical values by inspection.
- `outputs/summary.md` now avoids the earlier overclaim that the physiological regime is definitively “reversed.” It says the unconditional flat-dose / saturated-capacity classification is invalidated and notes that the 50 mg central no-extra-penalty ratio is close to one. This is the right interpretation.
- `README.md` is broadly faithful: it states that comp-044 does not predict serum urate and that the fixed-concentration / whole-day-denominator comparison is a limitation.
- `wiki/gut-lumen-uricase-physiologic-regime-computational.md` is consistent with the corrected interpretation: RED for legacy quantitative claim, biological hypothesis open, no ΔSUA computed.
- `wiki/computational-experiments.md` is consistent: it gives the correct central ratios, preserves “grid occupancy is not probability,” and states no serum-urate mapping.
- `wiki/validation-experiments.md` sections supplied in the bundle are materially consistent: §1.33 is moved to Gate 0; §1.9 no longer freezes UOX topology before §1.33; historical saturating-activity thresholds are explicitly downgraded to expression benchmarks.
- `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` is consistent: the numeric ΔSUA prior is retracted, H08 is reopened, and future interpretation is tied to physiological topology/oxygen/peroxide tests.
- `wiki/dual-chassis-ecn-pdb-uricase-computational.md` is consistent: comp-031 is invalidated because it inherited the failed UOX regime.
- `wiki/uricase-abcg2-genotype-stratification-computational.md` is consistent: comp-019 is superseded and frozen for provenance.
- `wiki/ginkgo-cloud-lab-evaluation.md` is consistent: it no longer treats a cheap cell-free fold check as relevant to the physiological-regime failure.
- `wiki/gout-multihop-research-program.md` is consistent and properly frames comp-044/045/046 as corrections to the program architecture.

Mismatch / propagation issue:

- `wiki/gut-lumen-sink.md` has top-of-page correction notices, but later retained prose still says or strongly implies that dosing is feasible in the 20–50 mg/day range, that “even low local uricase concentrations suffice,” and that lumen-based delivery is already the right initial proof-of-concept. Those statements are stronger than comp-044 permits unless explicitly labeled as historical/uncertain and gated on §1.33 plus a dynamic model.
- `wiki/uricase.md` is mostly corrected in its “Gut-Lumen Insight” section, but its “Oral Dosing Estimates” section still preserves 20–50 mg-style feasibility logic without enough local-regime caveat. It should be cross-linked directly to comp-044 limitations or reframed as historical, non-decisive dosing context.
- Because repository search was not available through the review environment, the omitted pages listed in the bundle—especially `engineered-yeast-uricase-proposal.md`, `engineered-koji-protocol.md`, `koji-endgame-strain.md`, `uricase-variant-selection.md`, `gout-action-guide.md`, and `gi-survival-prediction.md`—still require a targeted stale-claim sweep for “20–50 mg/day,” “yield solved,” “flat above 5 mg/day,” “low local uricase suffices,” and related comp-019-derived conclusions.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/outputs/results.json` | generated output | Yes | Numerically matches code by inspection. Verdict text is acceptable but still terse; no ΔSUA is inferred. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/outputs/summary.md` | generated output / trigger-updated summary | Yes | Corrected wording is materially faithful: invalidates unconditional flat-dose/saturated-capacity classification without claiming definitive reversal. |
| `wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/analyze.py` | committed code / summary generator changed in trigger | Yes | Code writes the corrected summary. Core computation is deterministic and stdlib-only. |
| `wiki/computational-experiments.md` | committed wiki surface supplied in daemon bundle | Reviewed supplied comp-044 section | Consistent with output and limitations. |
| `wiki/validation-experiments.md` | committed wiki surface supplied in daemon bundle | Reviewed supplied relevant sections; full file was bundle-truncated | Relevant UOX/koji sections are consistent with comp-044. |
| `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` | committed wiki surface supplied in daemon bundle | Yes | Consistent; H08 reopened and numeric ΔSUA prior retracted. |
| `wiki/dual-chassis-ecn-pdb-uricase-computational.md` | committed wiki surface supplied in daemon bundle | Yes | Consistent; comp-031 invalidation properly cites comp-044. |
| `wiki/gut-lumen-uricase-physiologic-regime-computational.md` | committed interpretive page supplied in daemon bundle | Yes | Consistent with artifact and corrected summary. |
| `wiki/uricase-abcg2-genotype-stratification-computational.md` | committed wiki surface supplied in daemon bundle | Yes | Consistent; comp-019 quantitative outputs retired. |
| `wiki/ginkgo-cloud-lab-evaluation.md` | committed wiki surface supplied in daemon bundle | Yes | Consistent; correctly says cell-free cannot resolve physiological-regime failure. |
| `wiki/gout-multihop-research-program.md` | committed wiki surface supplied in daemon bundle | Yes | Consistent; uses comp-044 as a program correction. |
| `wiki/gut-lumen-sink.md` | additional affected page inspected by reviewer | Yes | Change required: later retained prose still overstates dose feasibility / low-local-uricase sufficiency relative to comp-044. |
| `wiki/uricase.md` | additional affected page inspected by reviewer | Yes | Mostly reconciled, but oral dosing section needs clearer comp-044 caveat or historical labeling. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Uricase specific activity `8.3 U/mg` | `inputs/model_parameters.json`; `inputs/provenance.md` | Direct multiplier in capacity calculation | Inherited regulatory/literature prior from comp-019; primary source not directly verified in this review | Usable as a scenario prior, not primary-source verified. |
| pH/activity multiplier `0.75` | `inputs/model_parameters.json`; provenance labels as inherited scenario multiplier | Direct multiplier for all scenarios including legacy Vmax | Scenario value, not a measured regulatory constant | Acceptable because labeled nonmechanistic, but it affects all headline ratios. |
| Molecular weight urate `168.11 g/mol` | `inputs/model_parameters.json` | Converts µmol urate to mg urate | Standard chemical value; not independently source-checked here | Arithmetic use is correct. |
| Legacy intestinal urate flux `233 mg/day` | `inputs/model_parameters.json`; provenance | Denominator for all ratios | Corpus prior: 700 mg/day turnover × 0.33 intestinal share; primary basis not verified here | Appropriate only as diagnostic denominator; not patient-specific flux. |
| Human jejunal urate central `0.59 µM`, range `0.06–1.16 µM` | `inputs/model_parameters.json`; provenance | Used via duplicated `named_scenarios` and grid values | Inherited from comp-019 extraction of Miyazaki 2025; conversion `99.5 pg/µL → 0.592 µM` is arithmetically sound; primary source not re-read here | Load-bearing and plausible, but source verification remains inherited. |
| Uricase Km central `25 µM`, range `5–100 µM` | `inputs/model_parameters.json`; provenance | Used via duplicated scenario/grid values | Inherited prior; exact enzyme/formulation specificity unresolved | Correctly treated as uncertainty, not universal constant. |
| Active window central `3 h`, range `2–4 h` | `inputs/model_parameters.json`; provenance | Direct multiplier via scenarios/grid | Physiological prior inherited from `gi-survival-prediction.md`; primary source not checked here | Important; plausible but not directly verified. |
| Oxygen factors `0.01, 0.15, 1.0` | `inputs/model_parameters.json`; provenance | Direct scalar activity multiplier | Scenario-only; Zhao/PULSE support oxygen as uncertainty, not these numeric factors | Correctly labeled nonmechanistic; not evidence-derived kinetics. |
| Access factors `0.25, 0.5, 1.0` | `inputs/model_parameters.json` | Direct scalar activity multiplier | Scenario-only, not measured | Acceptable for sensitivity only. |
| Survival factors `0.25, 0.5, 1.0` | `inputs/model_parameters.json` | Direct scalar activity multiplier | Scenario-only, not measured | Acceptable for sensitivity only. |
| Postprandial/inflamed `50 µM` and distal high `500 µM` urate | `inputs/model_parameters.json`; provenance | Used in named scenarios and grid | Explicitly scenario-only, not human baseline | Properly labeled; should not be promoted to measured physiology. |
| Central diagnostic ratios `0.093 / 0.466 / 0.932` | `outputs/results.json`; `outputs/summary.md`; README | Generated by code and asserted in script | Recomputed by inspection | Valid for the stated fixed-concentration diagnostic. |
| Grid fractions below one `0.906 / 0.777 / 0.709` | `outputs/results.json`; `outputs/summary.md` | Generated from full-factorial grid counts | Not independently enumerated cell-by-cell, but grid size/count logic is consistent | Valid as design-space occupancy only; not probability. |
| “No ΔSUA predicted” | README, outputs, provenance, interpretive pages | Implemented by omission; no serum mapping exists | Directly supported by code inspection | Correct and important. |

## Affected wiki pages
- `wiki/computational-experiments.md` — already consistent — comp-044 section states the corrected ratios, no serum mapping, and proper limitation language.
- `wiki/validation-experiments.md` — already consistent in supplied relevant sections — §1.33 is Gate 0, §1.9 is staged, and saturating activity thresholds are not treated as physiological sufficiency.
- `wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md` — already consistent — quantitative prior retracted and hypothesis reopened.
- `wiki/dual-chassis-ecn-pdb-uricase-computational.md` — already consistent — comp-031 invalidation properly depends on comp-044.
- `wiki/gut-lumen-uricase-physiologic-regime-computational.md` — already consistent — interpretive page matches artifact and avoids ΔSUA inference.
- `wiki/uricase-abcg2-genotype-stratification-computational.md` — already consistent — comp-019 is superseded and frozen.
- `wiki/ginkgo-cloud-lab-evaluation.md` — already consistent — cell-free fold testing is not treated as a substitute for physiological-regime validation.
- `wiki/gout-multihop-research-program.md` — already consistent — program order reflects comp-044/045/046 corrections.
- `wiki/gut-lumen-sink.md` — change required — despite top reset notices, later sections retain stronger claims about dose feasibility, low local uricase sufficiency, and lumen-route readiness than comp-044 supports.
- `wiki/uricase.md` — change required — the “Oral Dosing Estimates” section should be explicitly labeled historical/non-decisive or caveated with comp-044’s substrate/time/topology limitations.
- `wiki/engineered-yeast-uricase-proposal.md` — change required / unresolved — omitted from bundle; likely surface for stale 20–50 mg/day or oral-dose feasibility language and should be searched.
- `wiki/engineered-koji-protocol.md` — change required / unresolved — omitted full page; should be searched for yield-solved, 20–50 mg/day, or direct-secretion sufficiency language.
- `wiki/koji-endgame-strain.md` — change required / unresolved — omitted full page; should be searched for UOX topology/dose assumptions derived from comp-019.
- `wiki/uricase-variant-selection.md` — change required / unresolved — omitted full page; should be searched for oral-track dose or yield-priority claims.
- `wiki/gi-survival-prediction.md` — unresolved — active-window prior source not checked; stale interpretation may remain.
- `wiki/gout-action-guide.md` — unresolved — omitted patient-facing/action-oriented page should be checked to ensure no comp-019 dosing or efficacy claims remain.

## New connections or implications
- The most important remaining unknown is not just enzyme mass; it is local urate delivery/replenishment at the reaction site. A 50 mg dose is only ~0.93× the legacy daily denominator under the optimistic central no-extra-penalty diagnostic, so any real oxygen/access/survival/topology penalty can dominate.
- Because the 50 mg central ratio is close to one, comp-045-style topology and peroxide measurements are not downstream refinements; they can decide the sign of the regime classification.
- The duplicate prior/scenario structure in `model_parameters.json` creates a general maintenance risk for future comps: human-readable prior blocks should either be code-linked or checked by assertions against scenario values.
- Claims that oral UOX “works because low local concentrations suffice” are now materially suspect unless they specify rodent/PULSE context, substrate concentration, topology, and oxygen/peroxide handling.

## Required actions
1. Update `wiki/gut-lumen-sink.md` to soften or historical-label later claims that 20–50 mg/day is feasible, low local uricase suffices, or lumen-based delivery is ready as the initial proof-of-concept. Verification criterion: every dose/yield/sufficiency statement either cites comp-044 limitations and §1.33 gating or is explicitly marked historical/non-decisive.
2. Update `wiki/uricase.md` “Oral Dosing Estimates” to state that 20–50 mg/day-style estimates are not validated physiological-regime predictions after comp-044. Verification criterion: no reader can infer that 20–50 mg/day or current production yields are sufficient without §1.33/dynamic-model data.
3. Run a targeted stale-claim sweep across omitted uricase/koji/yeast pages for: `20–50 mg`, `25 mg/day`, `flat dose`, `flat-dose`, `yield is solved`, `yield optimization`, `low local uricase`, `suffice`, `substrate-limited`, and `ΔSUA`. Owner surface: corpus wiki propagation. Verification criterion: all remaining hits are either current, historical, or explicitly superseded by comp-044.
4. Harden `inputs/model_parameters.json` or `analyze.py` against duplicate-prior drift. Verification criterion: either the code derives named scenarios/grid from `measured_or_regulatory_priors` / `scenario_only_values_not_measured_human_baselines`, or it asserts that duplicated values match.
5. If comp-044 is later used for quantitative planning, verify primary sources for the 8.3 U/mg specific activity, Km range, active-window prior, and 233 mg/day intestinal flux denominator. Verification criterion: claim-level provenance cites directly inspected primary sources or clearly remains inherited/unverified.

## Review limits
I did not execute `analyze.py`; daemon-mode review was by inspection only. Primary literature sources were not opened or independently verified; provenance status above distinguishes inherited citation strings from direct verification. Repository fixed-string search was not available in this review environment, so affected-surface discovery relied on the bundle, directory listing, and targeted file reads rather than full-corpus grep. The full `validation-experiments.md` file was bundle-truncated, although the supplied relevant UOX/koji sections were reviewed. I did not inspect prior `reviews/` logs because none were supplied in the bundle and no further repository access was available during finalization.
