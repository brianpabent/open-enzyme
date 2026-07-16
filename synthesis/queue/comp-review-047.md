---
type: comp-review
comp: comp-047
reviewed_snapshot: commit:eeab5b53054b93544c428a476dad06a8f8fe2621
action_required: true
---

# Current COMP actions: comp-047

**Why blocked:** **Action required.** The high-level scientific conclusion “rigid docking does not establish a Q141K chaperone candidate” is directionally plausible, but the artifact-summary-wiki contract is not clean. The most serious issues are:

## Required actions

1. **Integrate Axis 2b into executable results generation.**  
   Update `build_results.py` to read `outputs/drugbank_substrate_axis.json` and/or honor `substrate_disqualified` in `chembl_axis2.json`. Verification criterion: rerun merge produces `results.json` with rosuvastatin `final_known_abcg2: true` or equivalent and `wetlab_candidate: "no"`.

2. **Regenerate `outputs/results.json`, `outputs/controls.md`, and `outputs/summary.md`.**  
   Verification criterion: `summary.md` candidate shortlist matches the interpretive page: rosuvastatin removed; vorinostat is the sole marginal/uncertain survivor, or the interpretive page is changed to match executable output.

3. **Update `wiki/computational-experiments.md`.**  
   Verification criterion: comp-047 entry no longer says sensitivity did not run or Axis 2 is only thin/3-molecule; it should reflect `sensitivity.json`, DrugBank Axis 2b, rosuvastatin disqualification, and the remaining null/inconclusive conclusion.

4. **Update README reproducibility instructions and scripts.**  
   Verification criterion: the command works from the stated directory or scripts use `Path(__file__).parent`; remove hardcoded private temp paths or document required environment variables; define `$VBIN`; create `logs/` and `work/docking/` as needed; list `drugbank_substrate_axis.json` in outputs.

5. **Clarify validation follow-up registration.**  
   Verification criterion: `validation-experiments.md` either has a dedicated Q141K trafficking-rescue + urate-flux + ABCG2-inhibition counterscreen entry, or the comp-047 interpretive page links to a specific existing section and states how candidate compounds would enter it.

6. **Either fully inspect/verify generated receptor intermediates or mark them explicitly as unverified.**  
   Verification criterion: Q141K clean PDB/PDBQT and WT PDB/PDBQT are either reviewed/validated with hashes and basic residue/atom checks, or the review/provenance states that the receptor intermediates are assumed from script output and not independently inspected.

The full review is available through Git history. A new exact-artifact review must pass before propagation or synthesis eligibility is restored.
