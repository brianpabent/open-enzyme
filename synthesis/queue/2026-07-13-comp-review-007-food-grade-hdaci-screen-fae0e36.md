---
type: comp-review
sweep_date: 2026-07-13
sweep_sha: fae0e36
comp: comp-007
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-007

Canonical review log: [`logs/comp-reviews/2026-07-13-comp-007-fae0e36.md`](../../logs/comp-reviews/2026-07-13-comp-007-fae0e36.md)

ACTION_REQUIRED: yes

# Independent comp review — comp-007

## Bottom-line verdict
Action required. The artifact is internally close on the ranking arithmetic, but the quantitative verdict is not fully clean: the code ranks nominal/estimated HDAC potency and an oral-bioavailability proxy, not demonstrated enterocyte Q141K rescue or exposure-adjusted HDAC occupancy. There are also reproducibility and fidelity problems: current `analyze.py` would not regenerate the committed `outputs/summary.md` links, censored HDAC6 data are treated as exact, “167×” and “222×” selectivity are mixed, and artifact text still contains stale Basseville/butyrate direct-rescue wording despite the trigger correction.

## Implementation and constraint closure
I traced the implemented score from `inputs/candidates.json` and `inputs/bioactivity_data.json` through `analyze.py` into `outputs/ranking.json` and `outputs/summary.md`.

What the code actually does:
- For HDAC1/2/3 potency:
  - Uses geometric mean of available HDAC1/2/3 IC50s.
  - If all three are absent, falls back to `effective_HDAC_class_I_IC50_estimate_nM`.
  - Normalizes raw `1/IC50` to the most potent candidate in the list.
- For HDAC6 selectivity:
  - Computes `ratio = HDAC6_IC50 / mean_class_i_ic50`.
  - Computes `selectivity_score = ratio / (ratio + 10)`.
  - Uses fixed `0.30` penalty for unknown HDAC6.
- For gut selectivity:
  - Uses `1 - oral_bioavailability_fraction`.
- For `DATA_UNAVAILABLE`, forces composite to zero.

Arithmetic spot-checks match the committed ranking:
- Butyrate: mean class-I ≈ 12,000 nM; selectivity ratio ≈ 2,000,000 / 12,000 = 166.7; selectivity score ≈ 166.7/(166.7+10)=0.9434; potency norm ≈ 5,000/12,000=0.4167; composite ≈ 0.4167×0.9434×0.95=0.3734.
- Sulforaphane: 5,000 nM estimate gives max potency score 1.0; unknown HDAC6 penalty 0.30; gut score 0.30; composite 0.0900.
- PEITC: potency 0.5; selectivity 0.30; gut score 0.40; composite 0.0600.

Implementation issues:
- `hdac_targets.json` is loaded but not used. The target metadata, localization, and cardiotoxicity rationale are documentation-only in the implementation.
- `typical_gut_concentration_uM` is copied to outputs but not used in scoring. This is load-bearing because exposure relative to IC50 is the physical operating regime.
- `gut_concentration_note`, `oral_bioavailability_note`, molecular weight, SMILES, common names, and role are unused; some are legitimately documentation-only, but concentration notes are not merely decorative for this question.
- Caffeic acid and ferulic acid receive `used_estimate: true` even though the fallback estimate is `null`. This is a code-state bug, though it does not change their zero scores.
- Censored butyrate HDAC6 data (`>2,000,000 nM`) are treated as exact `2,000,000 nM`. The implemented butyrate selectivity and composite are therefore lower-bound-like, but the output presents them as exact.
- The prose formula for selectivity is inconsistent with the code. Code implements `ratio/(ratio+10)`, equivalent to `HDAC6_IC50 / (HDAC6_IC50 + 10×mean_class_I_IC50)`. Several summaries phrase it as `HDAC6_IC50/(HDAC6_IC50 + mean_class_I_IC50), midpoint ratio=10`, which omits the factor of 10 and is mathematically misleading.
- Current `analyze.py` writes summary links as `../../wiki/validation-experiments.md` and `../../wiki/food-grade-hdaci-screen-computational.md`, but committed `outputs/summary.md` contains `../../../validation-experiments.md` and `../../../food-grade-hdaci-screen-computational.md`. The committed output is therefore not a byte-level regeneration from the shown script. Also, from `outputs/`, the committed `../../../validation-experiments.md` path appears likely still one directory short for reaching `wiki/validation-experiments.md`.

Constraint closure:
- The biological target is not HDAC activity in isolation; it is restoration of functional Q141K-ABCG2 apical surface trafficking and urate efflux in enterocyte-relevant cells. The computation substitutes HDAC1/2/3 potency, HDAC6 avoidance, and a gut-enrichment proxy for that outcome.
- Reaction/access closure is incomplete. HDAC inhibition occurs in enterocyte nuclei for HDAC1/2/3; the code does not model intracellular concentration, metabolism, residence time, nuclear access, or whether the active species is the parent compound or metabolite.
- Operating-regime closure is incomplete:
  - Butyrate: typical gut concentration 1,000 µM versus class-I IC50 ≈12 µM supports plausible occupancy, but exposure is microbiome/fiber-dependent and not modeled.
  - Sulforaphane: typical gut concentration 5–20 µM versus estimated class-I IC50 5 µM is only margin-level and relies on indirect/cellular evidence.
  - PEITC: typical gut concentration 3–10 µM versus estimated class-I IC50 10 µM may be sub-IC50; ranking does not penalize this.
  - Allyl mercaptan: typical 200 µM versus estimated 50 µM could be exposure-plausible, but volatility, intracellular generation, and HDAC6 risk are unresolved.
  - DADS: typical 200 µM versus estimated 1,000 µM is likely below its own direct IC50; its relevant mechanism is AM prodrug conversion, not modeled.
- Mass balance/replenishment/residence time are not modeled. `1 - oral_bioavailability_fraction` is a convenience proxy, not a finite enterocyte exposure model.
- Safety closure is partial. HDAC6 is considered, but other off-targets and systemic exposures for sulforaphane/PEITC/AM/DADS are not quantitatively assessed.
- Sensitivity analysis is absent. Dominant uncertainties—estimated IC50s, HDAC6 penalty, bioavailability proxy, actual gut/intracellular concentration, residence time, and censored butyrate HDAC6 IC50—are not swept.

## Summary-fidelity audit
The main top-line ranking is consistent across README, committed outputs, `wiki-archive.md`, and `wiki/computational-experiments.md`: Butyrate rank 1, Sulforaphane rank 2, PEITC rank 3, with caffeic/ferulic acid at zero. However, several fidelity issues require correction:

- Direct Q141K rescue attribution is inconsistent:
  - The trigger diff correctly changes provenance to say direct Q141K trafficking rescue by any food-grade candidate, including butyrate, was not established by Basseville 2012.
  - But `inputs/provenance.md` still says “Butyrate at 1 mM rescues Q141K surface expression ~30–50%.”
  - `inputs/bioactivity_data.json` Butyrate notes say “butyrate at 1 mM rescues Q141K trafficking ~30–50%.”
  - `wiki-archive.md` says the pathway gives “partial membrane-trafficking rescue (~30–50% surface expression restoration at 1 mM butyrate),” then later says Basseville used a pharmacological tool compound and no food-grade candidate has direct Q141K rescue data. This is internally contradictory.
- Selectivity wording is inconsistent:
  - Code/output ratio for butyrate is 167× using HDAC6 over class-I geometric mean.
  - Provenance says 222× using HDAC6 over HDAC3.
  - Outputs limitations mention “confirmed 222x selectivity” even while ranking table says 167×.
  - The wiki archive formula text also mentions “confirmed 222× → 0.957,” but the code’s score for the output table is 0.943 from 167×.
- Censored HDAC6 value is not faithfully represented. `>2 mM` should propagate as `≥167×` or `>167×` and a lower-bound score, not an exact 167×/0.3734 if the source relation is respected.
- Reproducibility contract is broken or at least stale: current code would generate different summary links than the committed summary.
- README reproduction command says `cd experiments/comp-007-food-grade-hdaci-screen`, but the tracked directory is `wiki/etc/experiments/comp-007-food-grade-hdaci-screen`. The command is not repo-root accurate.
- The Stage 2 advancement recommendation is stronger than the model can support unless clearly framed as “screen these first because they are the top deterministic surrogate-ranking candidates.” Because actual concentration-vs-IC50 and intracellular access are not scored, PEITC vs. AM is not robustly resolved by the implemented model.
- `outputs/summary.md` says zero-score compounds “are not ranked” while the table assigns ranks 6 and 7. Minor, but should be reconciled.
- `wiki/validation-experiments.md` §1.22 is mostly reconciled with the corrected Basseville framing and properly treats butyrate as unvalidated for direct rescue. It still repeats the exact comp-007 score/selectivity wording and should be updated if the artifact is corrected.

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Butyrate HDAC1/2/3 IC50 = 16,000 / 12,000 / 9,000 nM | `inputs/bioactivity_data.json`; `inputs/provenance.md` | Directly used to compute class-I geomean and potency score | ChEMBL activity IDs cited; primary ChEMBL not independently queried in this review | Plausibly implemented; source not primary-verified here |
| Butyrate HDAC6 IC50 `>2,000,000 nM` | `inputs/bioactivity_data.json`; `inputs/provenance.md` | Used as exact 2,000,000 nM | ChEMBL activity ID cited; relation is censored | Action required: propagate as censored/lower-bound |
| Butyrate selectivity 167× | `outputs/ranking.json`; README; summary | Computed as 2,000,000 / geomean(HDAC1/2/3) | Derived from implemented values | Numerically matches code but should be `≥`/`>` because HDAC6 is censored |
| Butyrate selectivity 222× | `inputs/provenance.md`; `outputs/ranking.json` limitations; `wiki-archive.md` formula note | Not the code’s ranking denominator; uses HDAC3 denominator | Derived from same censored HDAC6 but different denominator | Action required: choose one denominator and label consistently |
| Selectivity score formula | `analyze.py`; README; output summaries | Code uses `ratio/(ratio+10)` | Internal formula, no external source | Action required: prose formula omits effective `10×mean_class_I` denominator |
| Sulforaphane class-I IC50 estimate = 5,000 nM | `inputs/bioactivity_data.json`; provenance | Directly used; gives max potency score | Literature citations are qualitative/cellular; no isoform IC50 | Low-confidence estimate; acceptable only as exploratory surrogate |
| PEITC class-I IC50 estimate = 10,000 nM | `inputs/bioactivity_data.json`; provenance | Directly used | Analogical extrapolation from SFN and cell-growth/protein-level data | Very low load-bearing support; ranking fragile |
| Allyl mercaptan estimate = 50,000 nM | `inputs/bioactivity_data.json`; provenance | Directly used | Derived from 92% inhibition at 200 µM in bulk nuclear extract | Approximate; no isoform closure; concentration may be relevant but not scored |
| DADS estimate = 1,000,000 nM | `inputs/bioactivity_data.json`; provenance | Directly used | Derived from 29% inhibition at 200 µM; prodrug context | Approximate; direct-inhibitor scoring may answer wrong mechanism |
| Oral bioavailability fractions | `inputs/candidates.json` | Directly used as `1 - BA` gut score | Mostly literature-estimate strings; not primary-verified; some no direct human PK | Major hidden substitution: low BA ≠ enterocyte nuclear exposure |
| Typical gut concentration | `inputs/candidates.json`; output JSON | Stored/copied only | Estimate strings only | Action required: currently unused despite being dominant operating-regime parameter |
| HDAC6 unknown penalty = 0.30 | `analyze.py`; outputs | Directly controls all non-butyrate ranked candidates | Arbitrary model constant | Needs sensitivity analysis; ranking depends on it |
| Caffeic/ferulic no IC50 | `bioactivity_data.json`; provenance | Forces composite zero via `DATA_UNAVAILABLE` | ChEMBL/PubMed absence asserted, not independently verified | Conservative scoring is defensible; `used_estimate: true` bug remains |
| Basseville direct butyrate Q141K rescue | `inputs/provenance.md`; `bioactivity_data.json`; `wiki-archive.md` | Not used in code but supports biological interpretation | Trigger diff says not established; validation page agrees not established | Action required: stale artifact text must be corrected |
| Stage 2 top 3 advance | README; `outputs/summary.md`; validation §1.22 | Derived from composite rank | Based on surrogate ranking only | Conditional recommendation; should not be treated as validated wet-lab priority without exposure/sensitivity caveat |

## Affected wiki pages
- `wiki/etc/experiments/comp-007-food-grade-hdaci-screen/inputs/provenance.md` — change required — trigger correction is partly applied, but earlier text still attributes direct 1 mM butyrate Q141K rescue to Basseville.
- `wiki/etc/experiments/comp-007-food-grade-hdaci-screen/inputs/bioactivity_data.json` — change required — Butyrate notes still claim direct butyrate Q141K rescue; HDAC6 censored relation is not propagated into score semantics.
- `wiki/etc/experiments/comp-007-food-grade-hdaci-screen/wiki-archive.md` — change required — internally contradictory Basseville/butyrate rescue wording; selectivity formula/167×/222× inconsistency.
- `wiki/etc/experiments/comp-007-food-grade-hdaci-screen/outputs/summary.md` — change required — code/output mismatch, selectivity wording, exact treatment of censored HDAC6, 222× limitation wording, and “not ranked” vs ranks 6–7.
- `wiki/etc/experiments/comp-007-food-grade-hdaci-screen/README.md` — change required — reproduction path is repo-root inaccurate; formula/selectivity/censored-value wording should be corrected.
- `wiki/food-grade-hdaci-screen-computational.md` — already mostly consistent as a stub, but change required if archive/output links or corrected verdict wording are propagated.
- `wiki/computational-experiments.md` — change required — comp-007 entry should avoid exact composite/selectivity overclaim if censored HDAC6 is handled; should note surrogate-ranking limitations and direct-rescue caveat.
- `wiki/validation-experiments.md` §1.22 — mostly already consistent on Basseville not proving butyrate rescue; change required after artifact correction to keep Stage 1 score/selectivity wording and Stage 2 advancement strength aligned.
- `wiki/abcg2-modulators.md` — already consistent on the key caveat: Basseville did not directly show butyrate rescue; no immediate change required unless comp-007 is reworded.
- `wiki/gut-lumen-sink.md` — already consistent on the corrected direct-butyrate caveat; no immediate change required.
- `wiki/engineered-lbp-chassis.md` — change required — butyrate “dual action” wording should distinguish established WT PPARγ induction from proposed/unvalidated Q141K HDAC-mediated rescue by butyrate.
- `wiki/hypotheses/H02-engineered-lbp-thesis.md` — change required — claim text still says butyrate’s class-I HDAC activity rescues Q141K; assumption stack later caveats this, but the headline claim should be softened.
- `wiki/f-prausnitzii-heterologous-expression-computational.md` — already mostly consistent if read as “comp-007 supports butyrate’s HDAC profile,” but should inherit the direct-Q141K-rescue caveat if H02/LBP wording is revised.
- `wiki/tcm-gout-compound-triage-computational.md` — already consistent as a cross-reference to the comp-007 scoring framework; no direct number change found.

## New connections or implications
- The most important lost implication is that `typical_gut_concentration_uM` may invert or at least weaken some rank confidence. PEITC’s estimated gut concentration can be below its estimated IC50, while allyl mercaptan’s local concentration may exceed its rough IC50 despite lower nominal potency. A concentration/occupancy-aware sensitivity pass could change Stage 2 inclusion confidence.
- comp-007 is more useful as a biochemical-prior generator for validation §1.22 than as a wet-lab prioritization engine. The decisive experiment is still paired Caco-2/hepatocyte HDAC activity plus Q141K surface trafficking/urate flux.
- The LBP/butyrate pages should use comp-007 narrowly: it supports butyrate’s class-I-over-HDAC6 biochemical profile, not direct proof that LBP-derived or fiber-derived butyrate rescues Q141K in human enterocytes.
- The “food-grade” label does not close safety. For chronic Q141K-directed use, HDAC6 is only one off-target axis; systemic sulforaphane/PEITC exposure and electrophile biology remain unmodeled.

## Required actions
1. Correct stale Basseville/butyrate rescue wording in `inputs/provenance.md`, `inputs/bioactivity_data.json`, and `wiki-archive.md`. Verification criterion: no artifact text claims Basseville established direct Q141K trafficking rescue by butyrate; butyrate is described as a proposed food-grade HDAC-directed candidate pending §1.14/§1.22 validation.
2. Fix selectivity reporting. Verification criterion: code, README, output summary, ranking JSON limitations, provenance, wiki archive, computational index, and validation §1.22 use one denominator convention; if using class-I geomean, report butyrate as `>167×` or `≥167×`, not exact, and remove stray 222× unless explicitly labeled as HDAC3-only.
3. Fix the selectivity formula prose. Verification criterion: summaries state `ratio/(ratio+10)` or equivalently `HDAC6_IC50 / (HDAC6_IC50 + 10×mean_class_I_IC50)`.
4. Reconcile `analyze.py` and committed outputs. Verification criterion: running the stated command from the correct repo-relative directory regenerates `outputs/ranking.json` and `outputs/summary.md` with matching links and content.
5. Correct the README reproduction command to the tracked path, or explain intended working directory. Verification criterion: a fresh clone user can follow the command without guessing whether `wiki/etc/` is omitted.
6. Add exposure/occupancy sensitivity or explicitly downgrade Stage 2 ranking confidence. Verification criterion: either incorporate `typical_gut_concentration_uM` versus IC50/estimated IC50 and residence/intracellular-access assumptions into a sensitivity table, or state that the top-3 advancement is a surrogate-prior only and not robust against exposure uncertainty.
7. Fix `used_estimate` handling for `DATA_UNAVAILABLE` compounds. Verification criterion: caffeic acid and ferulic acid do not appear as `used_estimate: true` when no estimate exists.
8. Propagate corrected wording to `wiki/computational-experiments.md`, `wiki/validation-experiments.md` §1.22, `wiki/engineered-lbp-chassis.md`, and `wiki/hypotheses/H02-engineered-lbp-thesis.md`. Verification criterion: no downstream page upgrades comp-007 into direct Q141K rescue evidence or exact clinical/wet-lab efficacy evidence.

## Review limits
I did not execute `analyze.py` or independently query ChEMBL/PubMed; source verification is limited to committed citation strings and internal consistency. The repository `grep_repo` tool failed because `rg` was unavailable, so affected-page discovery used the bundle plus targeted `read_file` inspection of key pages (`abcg2-modulators.md`, `gut-lumen-sink.md`, `validation-experiments.md`, `engineered-lbp-chassis.md`, and hypothesis cards). Primary literature claims, ChEMBL activity IDs, oral bioavailability estimates, and gut concentration estimates remain unverified against primary sources in this review.
