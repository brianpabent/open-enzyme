---
type: comp-review
comp: comp-007
reviewed_snapshot: commit:eeab5b53054b93544c428a476dad06a8f8fe2621
action_required: true
propagation_eligibility: eligible_with_warning
synthesis_eligibility: eligible_with_warning
---

# Current COMP actions: comp-007

**Current lane status:** propagation = `eligible_with_warning` (corrective-only); synthesis = `eligible_with_warning`. The actions below remain open.

**Why action remains open:** Action required. The revised Basseville/butyrate attribution and censored HDAC6-selectivity wording are materially improved, but the artifact-summary-wiki contract is not clean: generated `outputs/summary.md` contains broken relative links; README/summary formula text misstates the implemented selectivity denominator; and the ranking model omits a load-bearing exposure-vs-IC50/operating-regime axis despite storing gut concentration estimates. The top butyrate conclusion is plausible, but the composite scores and “top 3 advance” decision are not fully supported as a physiological prioritization.

## Required actions

1. Fix `analyze.py::write_summary()` relative links and regenerate `outputs/summary.md`; verification criterion: links from the generated output resolve to `wiki/validation-experiments.md` and `wiki/food-grade-hdaci-screen-computational.md` from the `outputs/` directory.
2. Correct README and generated summary selectivity formula prose to match implementation: `ratio/(ratio+10)` or `HDAC6_IC50 / (HDAC6_IC50 + 10×mean_class_I_IC50)`.
3. Add an explicit exposure/operating-regime axis or sensitivity table comparing `typical_gut_concentration_uM` to class-I IC50 estimates and, where possible, HDAC6 IC50; rerun outputs and reconcile ranking/stage recommendations.
4. Add sensitivity analysis for the arbitrary unknown-HDAC6 penalty `0.30`, selectivity midpoint `10`, oral BA estimates, and effective IC50 estimates for SFN/PEITC/AM/DADS.
5. Fix `used_estimate=true` for DATA_UNAVAILABLE compounds with no estimate, or rename the field to avoid implying an estimate was used.
6. Replace or source the strong HDAC6-safety framing. If no primary support is added, soften to “HDAC6 is one off-target concern; broader class-I/systemic HDAC safety is unmodeled.”
7. Propagate any revised ranking or caveat to `wiki/computational-experiments.md`, `wiki/validation-experiments.md` §1.22, and the current interpretive page.

The full review is available through Git history. This action remains open; lane eligibility and allowed scope are recorded in the current COMP receipt.
