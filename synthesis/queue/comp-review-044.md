---
type: comp-review
comp: comp-044
reviewed_snapshot: commit:eeab5b53054b93544c428a476dad06a8f8fe2621
action_required: true
---

# Current COMP actions: comp-044

**Why blocked:** Action required. The comp-044 arithmetic and deterministic output are materially reproducible by inspection, and the trigger edit correctly softens the summary from “regime reversed” to “unconditional saturated/flat-dose classification not robust.” However, corpus propagation is not fully clean: `gut-lumen-sink.md` still contains broad dose-feasibility / “low local uricase suffices” language that is stronger than comp-044 supports, even though the page has a top-level reset notice. Several omitted uricase/koji/yeast pages also need targeted audit for stale 20–50 mg/day, yield-solved, or flat-dose claims.

## Required actions

1. Update `wiki/gut-lumen-sink.md` to soften or historical-label later claims that 20–50 mg/day is feasible, low local uricase suffices, or lumen-based delivery is ready as the initial proof-of-concept. Verification criterion: every dose/yield/sufficiency statement either cites comp-044 limitations and §1.33 gating or is explicitly marked historical/non-decisive.
2. Update `wiki/uricase.md` “Oral Dosing Estimates” to state that 20–50 mg/day-style estimates are not validated physiological-regime predictions after comp-044. Verification criterion: no reader can infer that 20–50 mg/day or current production yields are sufficient without §1.33/dynamic-model data.
3. Run a targeted stale-claim sweep across omitted uricase/koji/yeast pages for: `20–50 mg`, `25 mg/day`, `flat dose`, `flat-dose`, `yield is solved`, `yield optimization`, `low local uricase`, `suffice`, `substrate-limited`, and `ΔSUA`. Owner surface: corpus wiki propagation. Verification criterion: all remaining hits are either current, historical, or explicitly superseded by comp-044.
4. Harden `inputs/model_parameters.json` or `analyze.py` against duplicate-prior drift. Verification criterion: either the code derives named scenarios/grid from `measured_or_regulatory_priors` / `scenario_only_values_not_measured_human_baselines`, or it asserts that duplicated values match.
5. If comp-044 is later used for quantitative planning, verify primary sources for the 8.3 U/mg specific activity, Km range, active-window prior, and 233 mg/day intestinal flux denominator. Verification criterion: claim-level provenance cites directly inspected primary sources or clearly remains inherited/unverified.

The full review is available through Git history. A new exact-artifact review must pass before propagation or synthesis eligibility is restored.
