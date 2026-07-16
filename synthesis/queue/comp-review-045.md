---
type: comp-review
comp: comp-045
reviewed_snapshot: commit:eeab5b53054b93544c428a476dad06a8f8fe2621
action_required: true
propagation_eligibility: eligible_with_warning
synthesis_eligibility: eligible_with_warning
---

# Current COMP actions: comp-045

**Current lane status:** propagation = `eligible_with_warning` (corrective-only); synthesis = `eligible_with_warning`. The actions below remain open.

**Why action remains open:** Action required. The artifact is materially useful as a randomized decision-design generator, but the artifact-summary-wiki contract is not clean:

## Required actions

1. Update `wiki/uricase-topology-oxygen-peroxide-design-computational.md` to replace “indirect empirical support” language with the corrected “joint-module precedent; isolated KatG/VHb effects unresolved” wording. Verification criterion: no remaining claim that secreted/displayed isolated KatG-only or VHb-only arms have indirect empirical support as isolated modules.
2. Update `wiki/computational-experiments.md` comp-045 entry to remove “secreted/displayed forms have indirect empirical KatG+VHb support” or rephrase it as joint-module precedent with isolated effects unresolved. Verification criterion: comp-045 index wording matches `results.json`.
3. Update `inputs/provenance.md` evidence-state vocabulary to remove “indirect empirical support” and define `joint_module_precedent_isolated_unresolved`. Verification criterion: provenance vocabulary matches `design_factors.json`.
4. Resolve the intracellular isolated-module evidence-state ambiguity in `analyze.py`: either cite and document direct isolated empirical support for intracellular KatG-only and VHb-only arms, or downgrade those isolated intracellular module statuses to joint-module/isolated-unresolved while preserving direct support for the combined intracellular architecture. Verification criterion: `results.json`, `summary.md`, and provenance consistently distinguish combined-module precedent from isolated-module support.
5. Regenerate outputs after any `analyze.py` or input vocabulary change and re-check `outputs/results.json` plus `outputs/summary.md`.

The full review is available through Git history. This action remains open; lane eligibility and allowed scope are recorded in the current COMP receipt.
