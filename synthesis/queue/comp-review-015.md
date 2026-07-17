---
type: comp-review
comp: comp-015
reviewed_snapshot: commit:eeab5b53054b93544c428a476dad06a8f8fe2621
action_required: true
propagation_eligibility: eligible_with_warning
synthesis_eligibility: eligible_with_warning
---

# Current COMP actions: comp-015

**Current lane status:** propagation = `eligible_with_warning` (corrective-only); synthesis = `eligible_with_warning`. The actions below remain open.

**Why action remains open:** **Action required.** The broad qualitative reframe is plausible but not materially clean: the artifact conflates *eurycomanone*, *eurycomanol*, and whole *Eurycoma longifolia*/Physta extract; the code/output reproducibility contract appears broken for at least one generated link; several summary/wiki surfaces overstate or inconsistently count evidence cells; and the interpretive stub still states a four-target question despite v2 being five-target.

## Required actions

1. **Fix reproducibility contract.** Update `analyze.py` or regenerate `outputs/summary.md` so the committed output is byte-identical to a rerun; correct the README `cd` path to `wiki/etc/experiments/comp-015-t-axis-adjuvant-urate-mapping`; verify with a local rerun.
2. **Correct stale target-count text.** Update README file description and `wiki/t-axis-adjuvant-urate-mapping-computational.md` question text from four-target to five-target v2 wording including XO.
4. **Fix code labeling for uncertain/negative evidence.** Do not mark `"UNKNOWN — POSSIBLY INDUCER"` as a favorable checkmark; preserve “Negative Screen” as an evidence class rather than converting it to `No-Data`.
5. **Resolve the eurycomanone/extract/eurycomanol substitution.** Rename the verdict surface or add explicit fields distinguishing pure eurycomanone, eurycomanol, quassinoid mixture, *Eurycoma longifolia* extract, and Physta. State which entity each PMID actually tested.
7. **Caveat or primary-verify the Physta SUA RCT.** Either obtain and cite the primary publication for the n=105 SUA −7–11% values or mark those values as secondary/product-summary-derived wherever they are promoted, especially in `gout-action-guide.md`.
9. **Confirm validation propagation.** Ensure the cordyceps vs tongkat/Physta head-to-head trial is either registered in `validation-experiments.md` with lead-generation wording and endpoints, or explicitly deferred.

The full review is available through Git history. This action remains open; lane eligibility and allowed scope are recorded in the current COMP receipt.
