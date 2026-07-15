---
type: comp-review
sweep_date: 2026-07-15
sweep_sha: eeab5b5
comp: comp-022
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-022

Canonical review log: [`logs/comp-reviews/2026-07-15-comp-022-eeab5b5.md`](../../logs/comp-reviews/2026-07-15-comp-022-eeab5b5.md)

ACTION_REQUIRED: yes

REVIEWED_SNAPSHOT: commit:eeab5b53054b93544c428a476dad06a8f8fe2621

# Independent comp review — comp-022

## Reviewed snapshot
Independent reviewer: OpenAI API reviewer. Reviewed daemon snapshot `commit:eeab5b53054b93544c428a476dad06a8f8fe2621`.

The inspected snapshot matched the supplied trigger diff and artifact bundle at the level visible to this review. I did not execute code. Repository search via `grep_repo` failed because `rg` was unavailable in the tool environment, so affected-surface discovery relied on the supplied explicit pages plus direct reads of omitted relevant pages (`koji-endgame-strain.md`, `chaperone-orthogonal-stacking.md`, `cassette-compatibility-computational.md`, `engineered-koji-protocol.md`) until the tool-result budget was exhausted.

## Bottom-line verdict
Action required.

The narrow 2026-07-14 correction in `wiki-archive.md` and `v2/provenance.md` is directionally right: the v2 strict N-of-5 = 5 tier is not the v1 top cluster, and only one strict-tier row is a v1-top-cluster member. However, the correction was not propagated to at least `wiki/koji-endgame-strain.md` and `wiki/validation-experiments.md`, which still state or imply that all four v1 top-cluster cassettes are strict N-of-5 = 5 and that PTS1-blocking is a v2-confirmed refinement. The committed v2 outputs contradict that.

The quantitative artifact is useful as a cassette-ranking heuristic, but its biological/model scope is narrower than some surrounding prose: it ranks sequence/cassette variants, mostly inside a prefiltered v1 koji-secreted shortlist, and does not establish physiological urate turnover, topology, oxygen sufficiency, peroxide handling, secretion localization, or clinical relevance.

## Implementation and constraint closure
I traced the main v1 and v2 paths:

- v1 `analyze.py`:
  - Enumerates 6 promoters × 12 SPs × 10 codon variants × 10 base scaffolds × 3 propeptide states × 2 N-glyc states = 43,200 candidates.
  - Computes CAI and v1 mRNA proxy per codon variant only.
  - Computes chaperone load per base scaffold plus propeptide/N-glyc deltas.
  - Computes promoter × SP prior from JSON promoter strengths and hard-coded `SP_BASE_EFFICIENCY`.
  - Gates on top-quintile membership for CAI, mRNA proxy, low chaperone load, and promoter-SP prior.
  - Collapses 2,421 candidate rows into 501 unique `(promoter, sp, codon, scaffold_base)` rows by selecting the best propeptide/N-glyc modifier.

- v2 `analyze_v2.py`:
  - Starts only from v1’s 501 unique-cassette shortlist, not the full 43,200 design space.
  - Joins v1 scores with committed ESM2-derived scores keyed by `(sp, scaffold_base, propeptide, nglyc)` and ViennaRNA scores keyed by `(codon, sp)`.
  - Drops v1 `mrna_5p` from the v2 concordance and replaces it with ViennaRNA MFE.
  - Adds ESM score as fifth axis.
  - Uses v1 full-cohort cutoffs for CAI/chaperone/prior and v2 shortlist-cohort cutoffs for MFE/ESM.
  - Produces 71 N-of-5 ≥ 4 rows and 4 strict N-of-5 = 5 rows.

Implementation issues / limitations that matter:

1. **The v2 “fold-quality” axis is not true ESMFold pLDDT and not true masked pseudo-likelihood.**  
   `run_esm2_pseudo_likelihood.py` performs a single unmasked forward pass and records true-token log probabilities. The artifact does disclose this in limitations, but many labels still say `esmfold_pLDDT.csv`, “pseudo-pLDDT,” and “ESM2 pseudo-likelihood.” This is acceptable only as a monotonic heuristic, not as a structural fold-confidence measurement.

2. **The v2 fold proxy models preprotein/cassette-context sequences, not mature uricase alone.**  
   `build_protein_shortlist.py` assembles signal peptide + generic propeptide + carrier head + KEX2 site + uricase + C-terminal tag. That may be a deliberate cassette-context proxy, but it is not “fold quality of the secreted mature enzyme.” Signal peptides and artificial propeptide placeholders can dominate the ESM ranking.

3. **The glucoamylase carrier is truncated to a 60-aa head in v2.**  
   This is disclosed, but it means v2 cannot fairly represent full glucoamylase-KEX2 fusion fold/secretion burden. v1 chaperone load penalizes fusions, while v2 ESM assesses only a truncated fusion proxy.

4. **v2 is a gate on v1 survivors, not a re-enumeration.**  
   This is disclosed in v2 provenance and `wiki-archive.md`, but any statement that v2 “names the true top four cassettes” for the whole 43,200 design space is too strong. It names the strict tier among v1-shortlisted rows under the v2 axes.

5. **Unused/stored JSON fields are mostly documentation/provenance, not executable parameters.**  
   The heuristic flagged fields such as `evidence`, `expected_cai_in_oryzae`, `expected_gc`, `literature_use_count_proxy`, `pro_region_available`, and `_meta.*`. Inspection shows these are not intended to drive scoring except where separately hard-coded:
   - Promoter `relative_strength` is used.
   - SP efficiencies are hard-coded, not read from `signal_peptides[].evidence` or `pro_region_available`.
   - `rare_codons_list` is used; `freq_threshold` and `rscu_threshold` are provenance for how the list was derived, not live thresholds.
   - `expected_cai_in_oryzae` / `expected_gc` are not used; actual codon sequences are generated by code.

6. **Reaction/physiology constraints are not closed by comp-022.**  
   The computation does not model:
   - urate concentration relative to uricase Km;
   - oxygen availability;
   - H₂O₂ generation and scavenging at the actual reaction site;
   - intestinal residence time or substrate access;
   - secretion vs intracellular/displayed topology performance;
   - product formation at human-baseline urate;
   - mass balance to serum urate.
   
   The surrounding corpus now correctly routes these questions to comp-044/045 and validation §1.33/§1.36, but some older prose in the artifact and related pages still reads as if cassette ranking itself confirms gene-synthesis decisions.

## Summary-fidelity audit
The internal v2 outputs support the corrected strict-tier statement:

- `v2_shortlist.csv` first four strict rows:
  1. `PamyB SPamyB_pro 5p_softened direct_3xAla_pts1blk`
  2. `PamyB SPamyB_pro 5p_softened direct_natag_pts1ok`
  3. `PglaA SPamyB_pro 5p_softened direct_3xAla_pts1blk`
  4. `PglaA SPamyB_pro 5p_softened direct_natag_pts1ok`

Only row 1 matches the v1 top-cluster definition requiring `PamyB`, `SPamyB` or `SPamyB_pro`, `5p_softened`, `direct_3xAla_pts1blk` or `direct_his6_pts1ok`, and `nglyc_ablated`.

Consistency checks:

- `v2_summary.json`: consistent with the correction: 501 v1 shortlist, 45 v1 strict unique cassettes, 71 v2 shortlist, 4 v2 strict, v1 top cluster 4/4 survives into N-of-5 ≥ 4.
- `v2_top25.md`: mostly consistent, but the phrase “v1-top-cluster … survival in v2: 4/4” should explicitly say “into the N-of-5 ≥ 4 shortlist,” not “strict tier,” to avoid the exact confusion being corrected.
- `v2/provenance.md`: corrected properly.
- `wiki-archive.md`: corrected properly in §9.2, §9.3, §9.6, and §9.9.
- `computational-experiments.md`: supplied page is already consistent and explicitly notes that PTS1-blocking is not a v2 strict-tier requirement.
- `README.md`: the newly added reproduction warning about `analyze_v2.py` being canonical is useful. However, the README’s top-level verdict remains v1-heavy and still foregrounds “PTS1-blocked C-terminal tag” as part of the headline cluster without the v2 correction. That is not necessarily false for v1, but it is stale if the README is read as the current v1+v2 summary.
- `validation-experiments.md`: supplied page still says comp-022 v2 “confirmed” all three refinements and that “all 4 v1 top-cluster members are in the v2 N-of-5 = 5 tier.” This is contradicted by `v2_shortlist.csv`.
- `koji-endgame-strain.md`: direct read found the same stale statement: “all 4 v1 top-cluster members are in the v2 N-of-5 = 5 tier” and lists PTS1-blocking as a confirmed refinement. This must be corrected.
- `chaperone-orthogonal-stacking.md`: no direct comp-022 strict-tier propagation issue found in the inspected sections; it mainly uses comp-022 for the N191Q / secreted-cassette framing.
- `engineered-koji-protocol.md`: older design sections still contain pre-comp-044/045 and pre-v2 framing around PTS1 removal/secretion. Some of this may be historical protocol text rather than a comp-022 summary, but it should not be allowed to override §1.33 topology gating.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/outputs/codon_variant_scores.md` | generated output | Yes | Matches code-level Tier 1 codon scores; supports v1 5p_softened claim. |
| `wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/outputs/full_ranking_top1000.csv` | generated output | No | Large file inspected in supplied excerpt and partial tail attempt; not fully line-by-line audited. Top rows support v1 ranking. Incomplete inspection itself requires action under the review contract. |
| `wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/outputs/report.json` | generated output | Yes for supplied content | v1 headline numbers are internally consistent: 43,200 total, 2,421 N≥3 candidates, 501 unique cassettes, 195 candidate rows at N=4. |
| `wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/outputs/scaffold_chaperone_loads.md` | generated output | Yes | Matches `chaperone_load()` base-scaffold outputs. |
| `wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/outputs/top25.md` | generated output | Yes | Matches v1 top cluster and v1-only PTS1-blocked ranking. |
| `wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/outputs/unique_cassette_shortlist.csv` | generated output | No | Large file inspected in supplied excerpt; not fully line-by-line audited. Supports first 501 shortlist structure but full file not independently exhaustively checked. |
| `wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/v2/outputs/esmfold_pLDDT.csv` | generated output | Yes | 106 rows, pseudo-pLDDT scaled 50–90. Label overstates true structural pLDDT; values are single-pass ESM log-prob rescaling. |
| `wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/v2/outputs/v2_shortlist.csv` | generated output | Yes | Decisively supports correction: strict tier is four rows; only one is v1-top-cluster. |
| `wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/v2/outputs/v2_summary.json` | generated output | Yes | Internally consistent with v2 shortlist: 71 N≥4, 4 strict, 4/4 v1 top cluster survives N≥4. |
| `wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/v2/outputs/v2_top25.md` | generated output | Yes | Numerically consistent; should clarify that “v1-top-cluster survival in v2” means N-of-5 ≥ 4, not strict tier. |
| `wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/v2/outputs/viennarna_mfe.csv` | generated output | Yes | 52 codon×SP pairs; supports MFE cutoff and weak v1 proxy correlation. |
| `wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/README.md` | proposed update | Yes | Canonical v2 reproduction note is good; current verdict remains v1-heavy and should mention v2 strict-tier correction / PTS1 nuance. |
| `wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/v2/provenance.md` | proposed update | Yes | Corrects prior strict-tier error accurately. |
| `wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/v2/rerank_v2.py` | proposed update | Yes | Deprecation header is necessary and accurate; prevents schema-clobbering reproduction error. |
| `wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/wiki-archive.md` | proposed update | Yes | Corrects the central strict-tier/top-cluster mistake accurately. |
| `wiki/computational-experiments.md` | affected summary page | Yes for supplied comp-022 section | Already consistent with corrected v2 interpretation. |
| `wiki/validation-experiments.md` | affected summary/protocol page | Partial supplied excerpt plus relevant §1.9 content | Change required: still says all four v1 top-cluster rows are strict N-of-5 = 5 and PTS1-blocking is confirmed by v2. |
| `wiki/koji-endgame-strain.md` | affected mechanism/design page | Partial direct read until tool budget exhaustion | Change required: stale comp-022 v2 paragraph repeats the false strict-tier claim and overstates PTS1-blocking as v2-confirmed. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Design space = 43,200 | `README.md`, `parts_list.json`, `analyze.py`, `report.json` | Explicit enumeration and assertion | Artifact-internal; arithmetic verified | Supported. |
| v1 N-of-4 ≥ 3 = 2,421 candidates; 501 unique cassettes | `report.json`, `top25.md`, `README.md` | Computed in v1 | Artifact-internal, not rerun | Supported by outputs. |
| v1 N-of-4 = 4 = 195 candidates | `report.json`, `README.md` | Computed in v1 across full 43,200 candidate rows | Artifact-internal, not rerun | Supported; distinct from 45 strict unique cassettes used in v2 summary. |
| v1 strict unique cassettes = 45 | `v2_summary.json` | Computed from `unique_cassette_shortlist.csv` rows with `concordance_n == 4` | Artifact-internal | Plausible and not inconsistent with 195 candidate-row count. |
| v2 N-of-5 ≥ 4 = 71 | `v2_shortlist.csv`, `v2_summary.json`, `v2_top25.md` | v2 gate result | Artifact-internal | Supported. |
| v2 N-of-5 = 5 = 4 | `v2_shortlist.csv`, `v2_summary.json` | v2 strict tier | Artifact-internal | Supported. |
| v1 top cluster survives v2 N-of-5 ≥ 4 at 4/4 | `v2_summary.json`, `v2_shortlist.csv` | `is_v1_top_cluster()` in `analyze_v2.py` | Artifact-internal | Supported. |
| All 4 v1 top-cluster cassettes are strict N-of-5 = 5 | stale `validation-experiments.md`, stale `koji-endgame-strain.md` | Not supported by current v2 output | Contradicted by `v2_shortlist.csv` | False; must be corrected. |
| Only 1 of 4 v2 strict-tier rows is v1 top cluster | `v2_shortlist.csv`, corrected `wiki-archive.md`, corrected `v2/provenance.md` | Direct row comparison | Artifact-internal | Supported. |
| PTS1-blocking is v2 strict-tier requirement | stale prose in affected pages | Not implemented as a required v2 condition | Contradicted by strict rows containing `direct_natag_pts1ok` | False; PTS1-blocking remains biologically motivated but not v2-strict-confirmed. |
| 5p_softened remains supported | v1 outputs, v2 strict rows | Codon score and v2 rows | Artifact-internal; biological literature citation only by string | Supported within model; not physiological evidence. |
| N191Q / `nglyc_ablated` remains supported | v1/v2 shortlists | Selected modifier in unique rows and v2 scoring | Heuristic load assumption; no primary-source glycosylation occupancy verified here | Supported as model preference, not experimental occupancy claim. |
| ESM2 pseudo-pLDDT cutoff 87.53 | `v2_summary.json`, `esmfold_pLDDT.csv` | v2 top20 ESM axis | Artifact-internal; scale is presentational | Supported as a ranking cutoff, not true pLDDT. |
| ViennaRNA MFE cutoff −16.4 kcal/mol | `v2_summary.json`, `viennarna_mfe.csv` | v2 top20 MFE axis | Artifact-internal; ViennaRNA primary source cited, not verified in this review | Supported by outputs. |
| MFE vs v1 proxy Spearman rho = 0.241 | `v2_summary.json`, `analyze_v2.py` | Summary statistic | Artifact-internal; not recomputed independently | Plausible; supports “v1 proxy weak” conclusion. |
| Physiological UOX topology / product formation | Corpus prose around §1.33 and §1.9 | Not implemented in comp-022 | Not part of artifact | Not established by comp-022. |
| Primary literature verification for promoter/SP/KEX2 coefficients | `inputs/provenance.md`, `provenance.md` | Some values used as hard-coded priors | Mostly citation strings / secondary corpus cross-checks in artifact; not independently primary-source verified here | Treat as bounded priors, not verified measurements. |

## Affected wiki pages
- `wiki/computational-experiments.md` — already consistent — supplied comp-022 entry correctly says PTS1-blocking is not a v2 strict-tier requirement and strict tier is not the v1 top cluster.
- `wiki/uricase-cassette-ranking-computational.md` — already mostly consistent — stub correctly frames comp-022 as cassette ranking only and defers topology to §1.33. It points readers to the archive.
- `wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/wiki-archive.md` — already consistent after proposed diff — central correction is accurate.
- `wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/v2/provenance.md` — already consistent after proposed diff — central correction is accurate.
- `wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/README.md` — change required — reproduction note is good, but the headline/current verdict remains v1-heavy and should warn that v2 strict tier is distinct and PTS1-blocking is not v2-strict-confirmed.
- `wiki/validation-experiments.md` — change required — §1.9 comp-022 prior still states that all four v1 top-cluster members are in the v2 N-of-5 = 5 tier and lists PTS1-blocking as v2-confirmed. Must be reconciled to the corrected v2 outputs.
- `wiki/koji-endgame-strain.md` — change required — direct read found the stale false statement that all four v1 top-cluster members are strict N-of-5 = 5, and overstatement of PTS1-blocking as a confirmed v2 refinement.
- `wiki/chaperone-orthogonal-stacking.md` — already broadly consistent in inspected sections — comp-022 mainly informs N191Q / chaperone-load framing; no strict-tier claim found in the read portion.
- `wiki/cassette-compatibility-computational.md` — already consistent as a frozen comp-010 stub — no comp-022 strict-tier propagation issue found.
- `wiki/engineered-koji-protocol.md` — possible change required — older protocol prose still contains direct-secretion / PTS1-removal framing. It should be checked beyond the inspected excerpt to ensure it does not cite comp-022 as proving topology or v2-confirming PTS1-blocking.

## New connections or implications
1. The v2 strict tier weakens the “PTS1-blocking as rank-confirmed winner” story but does not weaken the biological routing concern. The right formulation is: PTS1-blocking is a risk-mitigation design choice from comp-010, not a v2 rank requirement.
2. The strict tier introduces `PglaA` and non-PTS1-blocked direct scaffolds, which should keep promoter and C-terminal-tag choices open in §1.33/§1.9B rather than prematurely freezing PamyB + PTS1-blocked only.
3. The weak v1 proxy vs ViennaRNA correlation supports a general caution for future ClockBase-style cassette screens: GC-clamp heuristics can be useful for first pass but should not be treated as rank-stable where real MFE is cheap enough to run.
4. The v2 fold proxy’s dependence on signal peptide / propeptide / truncated carrier sequences means its “fold-quality” signal may be more of a cassette-context naturalness score than a mature-enzyme fold score. This is relevant to future comp-030-style cassette rankings and should be described consistently.

## Required actions
1. Update `wiki/validation-experiments.md` §1.9 comp-022 prior: replace “all 4 v1 top-cluster members are in the v2 N-of-5 = 5 tier” with “all 4 survive the N-of-5 ≥ 4 shortlist; only 1/4 is in the strict N-of-5 = 5 tier,” and soften PTS1-blocking to “biologically motivated, not v2-strict-confirmed.” Verification criterion: the section matches `v2_shortlist.csv` and `v2_summary.json`.
2. Update `wiki/koji-endgame-strain.md` §3.4 comp-022 paragraph with the same correction. Verification criterion: no occurrence remains implying the strict tier is identical to the v1 top cluster.
3. Update `README.md` current verdict or add a v2 note near the headline so readers do not stop at the v1 PTS1-blocked top-cluster summary. Verification criterion: README distinguishes v1 top cluster, v2 ≥4 survival, and v2 strict tier.
4. Search the full corpus for the stale claims once search tooling is available: phrases to check include “all 4 v1 top-cluster,” “strictest tier IS the v1 top cluster,” “three gene-synthesis-time refinements are confirmed,” “PTS1-blocking … confirmed,” and “N-of-5 = 5 tier names exactly.” Verification criterion: no top-level page outside the archive repeats the false strict-tier/PTS1 requirement claim.
5. Clarify `v2_top25.md` wording: “v1-top-cluster survival in v2” should explicitly say “survival into N-of-5 ≥ 4 shortlist,” not strict tier. Verification criterion: ambiguity removed.
6. Optionally rename or annotate `v2/outputs/esmfold_pLDDT.csv` and related prose to avoid implying true ESMFold pLDDT. Verification criterion: summaries consistently say “single-pass ESM2 log-probability proxy, rescaled for display.”
7. Complete an exhaustive line-by-line audit of `full_ranking_top1000.csv` and `unique_cassette_shortlist.csv` if the review contract requires every generated row to be independently inspected; this review could not complete that due tool-result budget limits.

## Review limits
- Code was not executed; reproducibility was assessed by static inspection only.
- Repository fixed-string search failed because `rg` was unavailable, so corpus-wide stale-claim discovery is incomplete.
- Tool-result budget was exhausted while reading large/omitted files. I could not fully inspect all rows of `full_ranking_top1000.csv` or `unique_cassette_shortlist.csv`.
- Primary sources were not independently retrieved; provenance status is based on artifact citation strings and corpus cross-references only.
- `validation-experiments.md`, `koji-endgame-strain.md`, `chaperone-orthogonal-stacking.md`, and `engineered-koji-protocol.md` were only partially read where relevant excerpts were available before budget exhaustion.
- The review did not validate numerical Spearman correlations or re-run v1/v2 scripts independently.
