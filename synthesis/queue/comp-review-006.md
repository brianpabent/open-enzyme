---
type: comp-review
comp: comp-006
reviewed_snapshot: commit:eeab5b53054b93544c428a476dad06a8f8fe2621
action_required: true
propagation_eligibility: eligible_with_warning
synthesis_eligibility: eligible_with_warning
---

# Current COMP actions: comp-006

**Current lane status:** propagation = `eligible_with_warning` (corrective-only); synthesis = `eligible_with_warning`. The actions below remain open.

**Why action remains open:** Action required. The computational artifact is plausibly deterministic and internally reproducible as a sequence-rule + pLDDT-proxy risk scan, but the updated interpretation still contains material fidelity problems:

## Required actions

1. Correct the NPr sensitivity interpretation in `README.md`, `outputs/summary.md`, and any generated-summary template in `analyze.py`: under NPr pH factor 0.3–0.5, the ectodomain no longer reaches HIGH from NPr, but the artifact’s acid-protease score (~0.195) and ALP score (~0.188 if unchanged) keep the overall model in **MODERATE**, not LOW. Verification criterion: regenerated summary and README no longer say `MODERATE/LOW` unless a new full scenario table changes all protease pH factors.
3. Add executable or tabulated sensitivity output if realistic pH factors are treated as load-bearing. Verification criterion: `cleavage_sites.json` or a companion output includes at least the primary conservative scenario plus NPr pH 0.5 and 0.3 scenarios, with overall worst protease and verdict recalculated across all proteases.
4. Propagate pLDDT-proxy caveats to affected CP0/H05 surfaces that still say “buried,” “verified protease stability,” or “in silico validated” without qualification. Verification criterion: `complement-c5a-gout.md` CP0 status and H05 explicitly say pLDDT-confidence proxy, no SASA, no degradation/survival model.
5. Fix stale repo paths in the generated summary if the current repo convention is `wiki/etc/experiments/...`. Verification criterion: `outputs/summary.md` script/library paths match the actual reproduction path or explicitly explain the alias.
6. Document primary-source verification status for the disulfide correction if it remains load-bearing. Verification criterion: include directly verified UniProt feature lines in provenance or state that UniProt was cited but not bundled.

The full review is available through Git history. This action remains open; lane eligibility and allowed scope are recorded in the current COMP receipt.
