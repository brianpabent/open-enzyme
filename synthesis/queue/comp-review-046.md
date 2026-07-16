---
type: comp-review
comp: comp-046
reviewed_snapshot: commit:eeab5b53054b93544c428a476dad06a8f8fe2621
action_required: true
propagation_eligibility: eligible_with_warning
synthesis_eligibility: eligible_with_warning
---

# Current COMP actions: comp-046

**Current lane status:** propagation = `eligible_with_warning` (corrective-only); synthesis = `eligible_with_warning`. The actions below remain open.

**Why action remains open:** **Action required.** The executable model and committed output are internally plausible as a deterministic algebraic design-space comparison, and the recent diff correctly acknowledges that `endogenous_luminal_urate_units` is stored but unused. However, several artifact/corpus surfaces still overstate the endogenous side as a “100-unit ledger” or say comp-046 “conserves both pools.” The code conserves only the dietary precursor ledger; the endogenous side is a capture-fraction architecture comparison. That mismatch is material because it changes the interpretation of the result.

## Required actions

1. Correct `README.md` and `inputs/provenance.md` so they no longer say there are “two 100-unit ledgers” or that endogenous luminal urate is a conserved ledger. Verification criterion: no artifact text implies conservation of the endogenous 100 units unless the code is changed to implement that conservation.
2. Correct `wiki/computational-experiments.md`, `wiki/gout-multihop-research-program.md`, and residual wording in `wiki/staged-purine-sink-mass-balance-computational.md` to say: dietary side = conserved 100-unit fate ledger; endogenous side = capture-fraction architecture comparison with `endogenous_luminal_urate_units` unused. Verification criterion: grep/search for “100-unit endogenous,” “conserves both pools,” and “separate conserved ledgers” returns no stale comp-046 claims.
3. Consider renaming `endogenous_luminal_urate_ledger` in `results.json` / `summary.md` generation to `endogenous_luminal_urate_architecture_comparison`, or add an adjacent machine-readable `ledger_type: "capture_fraction_not_conserved"` field. If changed, rerun `python3 analyze.py` and recommit outputs.
4. If provenance statements are used for prioritization beyond this algebraic model, primary-source verification should be recorded explicitly for the Ji/GR-5, UOX/PULSE, and PDB pathway anchors. Verification criterion: each load-bearing biological statement cites a checked primary source, not only a citation string.

The full review is available through Git history. This action remains open; lane eligibility and allowed scope are recorded in the current COMP receipt.
