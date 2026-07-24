---
type: comp-review
comp: comp-022
reviewed_snapshot: commit:eeab5b53054b93544c428a476dad06a8f8fe2621
action_required: true
propagation_eligibility: eligible_with_warning
synthesis_eligibility: eligible_with_warning
---

# Current COMP actions: comp-022

**Current lane status:** propagation = `eligible_with_warning` (corrective-only); synthesis = `eligible_with_warning`. The actions below remain open.

**Why action remains open:** Action required.

## Required actions

1. Update `wiki/validation-experiments.md` §1.9 comp-022 prior: replace “all 4 v1 top-cluster members are in the v2 N-of-5 = 5 tier” with “all 4 survive the N-of-5 ≥ 4 shortlist; only 1/4 is in the strict N-of-5 = 5 tier,” and soften PTS1-blocking to “biologically motivated, not v2-strict-confirmed.” Verification criterion: the section matches `v2_shortlist.csv` and `v2_summary.json`.
2. Update `wiki/koji-endgame-strain.md` §3.4 comp-022 paragraph with the same correction. Verification criterion: no occurrence remains implying the strict tier is identical to the v1 top cluster.
3. Update `README.md` current verdict or add a v2 note near the headline so readers do not stop at the v1 PTS1-blocked top-cluster summary. Verification criterion: README distinguishes v1 top cluster, v2 ≥4 survival, and v2 strict tier.
4. Search the full corpus for stale claims: “all 4 v1 top-cluster,” “strictest tier IS the v1 top cluster,” “three gene-synthesis-time refinements are confirmed,” “PTS1-blocking … confirmed,” and “N-of-5 = 5 tier names exactly.” Verification criterion: no current page repeats the false strict-tier/PTS1 requirement claim.
5. Clarify `v2_top25.md` wording: “v1-top-cluster survival in v2” should explicitly say “survival into N-of-5 ≥ 4 shortlist,” not strict tier. Verification criterion: ambiguity removed.
6. Optionally rename or annotate `v2/outputs/esmfold_pLDDT.csv` and related prose to avoid implying true ESMFold pLDDT. Verification criterion: summaries consistently say “single-pass ESM2 log-probability proxy, rescaled for display.”
7. Complete an exhaustive line-by-line audit of `full_ranking_top1000.csv` and `unique_cassette_shortlist.csv` if the review contract requires every generated row to be independently inspected; this review could not complete that due tool-result budget limits.
8. Remove or replace the uncalibrated “chaperone-load” ranking axis. Its disulfide/glycosylation/KEX2 coefficients were inherited from the now-retired folding-score framework and are not measured predictors of expression, folding, secretion, or function. Recompute every shortlist and concordance claim that depends on that axis under a fresh pre-run design, or retire the affected ranking scope. Verification criterion: no active page calls the current shortlist, direct-secretion cluster, “winner,” or gene-synthesis refinement decision-eligible before a new independently reviewed artifact establishes which axes are calibrated to which named outcomes.

The full review is available through Git history. This action remains open; lane eligibility and allowed scope are recorded in the current COMP receipt.
