---
type: comp-review
comp: comp-019
reviewed_snapshot: commit:eeab5b53054b93544c428a476dad06a8f8fe2621
action_required: true
propagation_eligibility: eligible_with_warning
synthesis_eligibility: eligible_with_warning
---

# Current COMP actions: comp-019

**Current lane status:** propagation = `eligible_with_warning` (corrective-only); synthesis = `eligible_with_warning`. The actions below remain open.

**Why action remains open:** Action required. The current corpus-level interpretation correctly supersedes comp-019 with comp-044 and retires the ΔSUA, genotype-ranking, flat-dose, and yield-deprioritization conclusions. However, the invalidation propagation is incomplete inside the actual artifact: `outputs/phase_a_table.md` still contains an active “model predicts the mechanism works MORE in non-Q141K patients” statement with no invalidation banner, and `outputs/flux_model_results.json` remains a machine-readable invalid result file with no invalidation metadata. The model’s quantitative verdict is invalid.

## Required actions

1. Add an invalidation/supersession banner to `outputs/phase_a_table.md`, or edit its closing Phase B statement to say the model prediction is retired and only the “no Q141K-stratified uricase trial found” result survives. Verification criterion: no unbannered generated Markdown output states that non-Q141K patients respond more or that comp-019 predicts genotype ordering.
2. Add machine-readable invalidation metadata to `outputs/flux_model_results.json` (for example `_metadata.status: "invalidated/superseded"`, `superseded_by: "comp-044"`, and `do_not_use_for: [...]`), or provide a clearly named sidecar consumed by downstream tooling. Verification criterion: any programmatic reader of the JSON can detect that ΔSUA, capacity ratios, genotype ranking, flat dose-response, and yield recommendations are retired.
3. Update `README.md` status/verdict lines, or add an immediately adjacent note after them, so they do not appear to be the current verdict beneath the banner. Verification criterion: a skim reader sees `Status: Invalidated/Superseded` before encountering the historical retired verdict.
4. Optional but recommended: state explicitly in the artifact README that `phase_a_table.md` preserves a valid literature-gap table but its Phase B extrapolation is retired. Verification criterion: Phase A surviving result and Phase B invalid result are separable.

The full review is available through Git history. This action remains open; lane eligibility and allowed scope are recorded in the current COMP receipt.
