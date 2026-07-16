---
type: comp-review
comp: comp-043
reviewed_snapshot: commit:eeab5b53054b93544c428a476dad06a8f8fe2621
action_required: true
propagation_eligibility: eligible_with_warning
synthesis_eligibility: eligible_with_warning
---

# Current COMP actions: comp-043

**Current lane status:** propagation = `eligible_with_warning` (corrective-only); synthesis = `eligible_with_warning`. The actions below remain open.

**Why action remains open:** **Action required.** The computational artifact is internally coherent for a Phase 0 mechanistic-prior analysis, and the code/output contract is plausible by inspection. However, propagation is not clean: `wiki/computational-experiments.md` still cites `chaperone-orthogonal-stacking.md §8 item 6` for the DsbA/DsbC capacity gap, while the experiment, interpretive page, provenance, and output summary now cite **§8 item 8**. Several downstream wet-lab/hypothesis surfaces still describe EcN/LBP as a DAF fallback without carrying comp-043’s new “EcN DAF is only provisional/capacity-gated” caveat.

## Required actions

1. Update `wiki/computational-experiments.md` comp-043 key finding from `chaperone-orthogonal-stacking.md §8 item 6` to **§8 item 8**. Verification criterion: no comp-043-related DsbA/DsbC capacity-gap reference points to item 6.
2. Update `wiki/validation-experiments.md` §1.25 cross-reference/routing language so any EcN/LBP DAF route is explicitly **PROVISIONAL / DsbA-DsbC-capacity-gated**, not an unqualified fallback. Verification criterion: §1.25 references comp-043 or repeats its bounded caveat.
3. Update `wiki/hypotheses/H05-daf-scr14-cp0-thesis.md` to cite comp-043 in the LBP peer-track discussion and state that EcN DAF SCR1-4 is provisional secondary, while koji remains primary. Verification criterion: H05 no longer implies EcN/LBP is an automatically viable DAF route.
4. Review `wiki/complement-c5a-gout.md` for older DAF-to-LBP fallback language and add the same comp-043 caveat where needed. Verification criterion: CP0 architecture text says the two-chassis architecture stands, but EcN does not dominate koji and DAF-on-EcN is capacity-gated.
5. If primary-source verification is intended to be auditable from the artifact, commit or quote the relevant UniProt `FT DISULFID` and `FT CARBOHYD` lines used for the disulfide/glycan counts, or soften provenance wording from “verified” to “reported verified by author.” Verification criterion: an independent reviewer can reproduce the primary annotation check from committed text without external fetch.

The full review is available through Git history. This action remains open; lane eligibility and allowed scope are recorded in the current COMP receipt.
