---
type: comp-review
comp: comp-011
reviewed_snapshot: commit:eeab5b53054b93544c428a476dad06a8f8fe2621
action_required: true
propagation_eligibility: eligible_with_warning
synthesis_eligibility: eligible_with_warning
---

# Current COMP actions: comp-011

**Current lane status:** propagation = `eligible_with_warning` (corrective-only); synthesis = `eligible_with_warning`. The actions below remain open.

**Why action remains open:** **Action required.** The new ALLN-346 mutant implementation is directionally plausible and the key I132R result is internally consistent, but the artifact-summary-wiki contract is not clean:

## Required actions

1. Reconcile the current interpretive page with `outputs/summary.md`. Verification criterion: no unqualified “both 130 and 138 HIGH / mutate both” language remains for the recommended P78609+ALLN-346 construct.

2. **Update `README.md` to mention the added ALLN-346 mutant analysis.**  
   Verification criterion: README key results distinguish WT P78609 KEX2 scoring from P78609+ALLN-346 scoring and point readers to the mutant JSON/summary section.

3. **Reconcile `outputs/summary.md` internal wording.**  
   Verification criterion: earlier KEX2 recommendation section says WT requires attention at 130+138, while ALLN-346 reduces position 130 to MODERATE but does not abolish it; position 138 remains HIGH. Avoid implying I132R fully solves position 130 under a fusion topology.

4. **Clarify JSON summary fields or add labels separating WT comparison from mutant comparison.**  
   Verification criterion: primary `combined_burden`/`comparison` fields are clearly labeled as WT P78609, or corresponding mutant-adjusted comparison fields are added for the recommended P78609+ALLN-346 construct.

5. **Update `wiki/computational-experiments.md` comp-011 entry.**  
   Verification criterion: entry states that I132R is the P1′ residue of the position-130 KR site and reduces the KEX2 classification from HIGH to MODERATE; it should not only say “adjacent.”

6. **Run a corpus-wide propagation audit using a working search tool.**  
   Verification criterion: pages containing `ALLN-346`, `P78609`, `C. utilis`, `130 + 138`, `both HIGH`, `double KR`, or `KRI` are checked and reconciled, especially omitted pages such as `chaperone-orthogonal-stacking.md` and `koji-endgame-strain.md`.

7. **Preserve the primary-source verification boundary.**  
   Verification criterion: summaries continue to say that US10815461B2 discloses the mutation set but exact ALLN-346 parent sequence is not available; avoid wording that implies the exact clinical ALLN-346 full sequence was primary-verified.

The full review is available through Git history. This action remains open; lane eligibility and allowed scope are recorded in the current COMP receipt.
