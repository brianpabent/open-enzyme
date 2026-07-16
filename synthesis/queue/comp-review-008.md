---
type: comp-review
sweep_date: 2026-07-15
sweep_sha: eeab5b5
comp: comp-008
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-008


ACTION_REQUIRED: yes

REVIEWED_SNAPSHOT: commit:eeab5b53054b93544c428a476dad06a8f8fe2621

# Independent comp review — comp-008

## Reviewed snapshot
Independent reviewer: API review daemon. Reviewed daemon snapshot `commit:eeab5b53054b93544c428a476dad06a8f8fe2621`. The supplied artifact files were inspectable in full from the bundle. Repository tool search was unavailable because `rg` was missing, but omitted load-bearing wiki pages were inspected directly where needed (`engineered-lbp-chassis.md`, `abcg2-modulators.md`, `validation-experiments.md`, `modality-chokepoint-matrix.md`, partial `koji-endgame-strain.md`). No code execution was performed.

## Bottom-line verdict
Action required. The core qualitative conclusion is physically plausible—native BCoAT/butyrate boost is the most tractable *F. prausnitzii* payload; uricase is a poor fit for an obligate anaerobe because O₂ and H₂O₂ are load-bearing constraints. However, the artifact-corpus contract is not clean: `wiki-archive.md`, the interpretive comp page, `abcg2-modulators.md`, and some matrix/open-question language still overstate that engineered *F. prausnitzii* “solves” butyrate bioavailability or “hits” Q141K rescue, despite the corrected generated `outputs/summary.md` now properly saying this is unproven and requires colonization-density, titer, epithelial-exposure, and direct Q141K-rescue validation.

## Implementation and constraint closure
The executable model is a deterministic, stdlib-only scoring script with eight manually assigned factors per payload and geometric-mean aggregation. I traced:

- `chassis_profile.json` is read for host, genome GC, oxygen tolerance, and transformation-protocol status in `results.json` and `summary.md`.
- `payloads.json` is read but not actually used for scoring or output derivation. Payload lengths, disulfide counts, O₂-substrate flags, glycosylation fields, and UniProt IDs are duplicated manually in hard-coded `SCORES` rationales. This means the apparent JSON input provenance is documentation/provenance, not an executable data source.
- `SCORES` in `analyze.py` is the load-bearing model. The outputs are consistent with the hard-coded values and geometric means by inspection.
- Sensitivity ranges are low/high factor sweeps where all factors are set to their low or high values simultaneously. This is transparent but is not a probabilistic uncertainty model.

Constraint closure:

- **Uricase:** The model correctly identifies the key reaction constraint: uricase consumes molecular O₂ and produces H₂O₂. This is incompatible with an anoxic lumen and a strict anaerobe lacking robust peroxide handling. However, substrate import/export is only mentioned qualitatively, not modeled.
- **Butyrate/BCoAT:** Treated as a native cytoplasmic pathway boost. That supports engineering tractability, not physiologic therapeutic flux. No acetate/acetyl-CoA mass balance, colonization density, butyrate titer, luminal residence, epithelial exposure, or host/microbiome consumption model is implemented.
- **Lactoferrin and sCR1:** Correctly flagged as secretion/disulfide-folding gated in an anoxic organism. The scoring gives conditional-GREEN non-toolkit values for both, but this remains speculative; no secretion titer, Dsb machinery, or folded-active protein model is implemented.
- **Toolkit:** The shared 0.25 factor for no published *F. prausnitzii* transformation protocol is the dominant engineering constraint. The artifact treats adapting Lachnospiraceae conjugation as plausible but not demonstrated.

Main implementation concern: the experiment answers “expert-prior payload feasibility ranking,” not an experimentally grounded capacity or efficacy question. The README and limitations mostly acknowledge this, but input files should not be presented as if they drive the computation when the scoring is hard-coded.

## Summary-fidelity audit
Generated `outputs/results.json` and `outputs/summary.md` are internally consistent with `analyze.py` after the lactoferrin disulfide correction from 17 to 16 and the corrected comp-007 cross-link language.

Mismatches requiring action:

1. **`wiki-archive.md` is stale on the comp-007 cross-link.** It still says: “Continuous gut-luminal butyrate from an engineered *F. prausnitzii* strain solves the bioavailability problem…” and uses “167×” rather than the corrected “>=167x censored lower bound” framing. This contradicts `analyze.py` and `outputs/summary.md`.
2. **Interpretive page `wiki/f-prausnitzii-heterologous-expression-computational.md` is stale.** Its final comp-007 cross-reference still says engineered Fp butyrate “solves oral bioavailability.” This is stronger than the artifact supports and conflicts with the corrected wording in `engineered-lbp-chassis.md`.
3. **`wiki/abcg2-modulators.md` retains an overstrong LBP statement:** “An engineered colonically-resident butyrate producer solves the bioavailability problem at the dose-frequency level.” The same page elsewhere has strong caveats about direct Q141K butyrate rescue being untested; this sentence should be harmonized.
4. **Open-question/matrix language remains too strong in places.** `open-questions.md` and `modality-chokepoint-matrix.md` still use shorthand such as engineered *Faecalibacterium* “hits both WT ABCG2 and Q141K” or “local butyrate … Q141K rescue” without the direct-rescue and exposure caveats. These should be softened to “proposed / gated on §1.14 and exposure measurements.”
5. **README path hygiene:** the “How to reproduce” command was fixed, but the README “Files” tree still begins with `experiments/comp-008.../` rather than the actual `wiki/etc/experiments/.../`. This is minor but should be corrected for reproducibility documentation.
6. **Generated summary relative links are suspect.** In `outputs/summary.md`, the link to `engineered-lbp-chassis.md` is `../../wiki/engineered-lbp-chassis.md`, which does not resolve correctly from `wiki/etc/experiments/comp-008.../outputs/`. The archive uses different relative paths. Broken generated links should be fixed or made plain text.

Pages already substantially reconciled:

- `wiki/engineered-lbp-chassis.md` has a corrected caveat: engineered Fp butyrate is proposed to address dose-frequency bioavailability but remains unproven and requires colonization, titer, epithelial exposure, and Q141K validation.
- `wiki/hypotheses/H02-engineered-lbp-thesis.md` correctly says Q141K butyrate rescue is proposed/unvalidated and gated on validation §1.14.
- `wiki/validation-experiments.md` §1.14 includes the direct butyrate/Q141K rescue test, consistent with the corrected artifact.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---|---|
| `wiki/etc/experiments/comp-008-f-prausnitzii-heterologous-expression/README.md` | tracked artifact / proposed update | Yes | Top-line and limitations mostly faithful; reproduce command fixed. File tree still uses old `experiments/...` path. |
| `wiki/etc/experiments/comp-008-f-prausnitzii-heterologous-expression/analyze.py` | tracked artifact / proposed update | Yes | Deterministic hard-coded scoring; lactoferrin disulfide correction propagated in code; payload JSON read but not used for scoring. |
| `wiki/etc/experiments/comp-008-f-prausnitzii-heterologous-expression/inputs/chassis_profile.json` | tracked input | Yes | Used partly for output chassis fields; many detailed fields are provenance/documentation only. |
| `wiki/etc/experiments/comp-008-f-prausnitzii-heterologous-expression/inputs/payloads.json` | tracked input / proposed update | Yes | Lactoferrin disulfides corrected to 16. Most payload metadata is not consumed by code; must be documented as provenance/manual-scoring support, not executable input. |
| `wiki/etc/experiments/comp-008-f-prausnitzii-heterologous-expression/inputs/provenance.md` | tracked input/provenance | Yes | Provides named sources and verification notes but primary-source verification was not independently redone here. |
| `wiki/etc/experiments/comp-008-f-prausnitzii-heterologous-expression/outputs/results.json` | generated output / proposed update | Yes | Consistent with `analyze.py`; corrected 16-disulfide rationale present. |
| `wiki/etc/experiments/comp-008-f-prausnitzii-heterologous-expression/outputs/summary.md` | generated output / proposed update | Yes | Internally faithful and corrected on butyrate/Q141K caveat; likely broken relative links. |
| `wiki/etc/experiments/comp-008-f-prausnitzii-heterologous-expression/wiki-archive.md` | archive/proposed update | Yes | Stale comp-007 cross-link remains: overstates engineered Fp butyrate as solving bioavailability. Needs correction. |
| `wiki/f-prausnitzii-heterologous-expression-computational.md` | explicit top-level wiki surface | Yes | Headline ranking consistent, but comp-007 cross-link overstates bioavailability solution. Needs correction. |
| `wiki/computational-experiments.md` | explicit top-level wiki surface | Yes, relevant sections | comp-008 row broadly consistent; no major mismatch beyond less precise comp-007 phrasing elsewhere. |
| `wiki/hypotheses/H02-engineered-lbp-thesis.md` | explicit top-level wiki surface | Yes | Correctly caveats direct butyrate Q141K rescue as unvalidated and §1.14-gated. |
| `wiki/engineered-lbp-chassis.md` | omitted but load-bearing affected page | Yes | Already harmonized with corrected caveat; still has P2-4 marked queued in follow-up table despite comp-008 completed in an added section. |
| `wiki/abcg2-modulators.md` | omitted but load-bearing affected page | Yes | Contains overstrong “solves the bioavailability problem” statement in LBP engineering implications. Needs correction. |
| `wiki/validation-experiments.md` | omitted but load-bearing affected page | Partially; relevant §1.14 and dashboard inspected | Correctly includes direct butyrate/Q141K attribution test and exposure caveats. |
| `wiki/modality-chokepoint-matrix.md` | omitted but affected page | Yes | Some shorthand still implies engineered Fp butyrate covers Q141K; should add proposed/gated caveat. |
| `wiki/open-questions.md` | explicit top-level wiki surface in bundle | Relevant sections inspected | Contains both corrected caveats and some older shorthand; harmonization required. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Fp A2-165 / *F. duncaniae* genome GC 56.6% | `chassis_profile.json`, `provenance.md`, outputs | Read from JSON into outputs; supports GC/codon rationale | Named Fraccascia 2022; not independently primary-verified in this review | Accept as artifact-level sourced; primary verification unresolved |
| No published Fp transformation protocol as of 2026-05 | `chassis_profile.json`, `provenance.md`, `SCORES` toolkit factor 0.25 | Hard-coded score/rationale; JSON boolean exported | Named Sheridan/Martín/Quévrain/Breyner sources; not independently primary-verified | Plausible and central; should remain caveated as literature-status claim |
| Uricase requires molecular O₂ and produces H₂O₂ | `payloads.json`, `provenance.md`, uricase `SCORES` | Hard-coded host-physiology 0.10 and toxicity 0.20 | UniProt Q00511 named; not independently fetched | Physically load-bearing and correctly used |
| Fp is strict obligate anaerobe / anoxic colonic lumen | `chassis_profile.json`, outputs | Hard-coded host-physiology rationale; chassis output | Literature named; not independently primary-verified | Supports uricase rejection; plausible |
| Lactoferrin mature protein has 16 disulfides | `payloads.json`, `provenance.md`, `analyze.py`, outputs | Hard-coded folding/secretion scores; corrected from 17 to 16 | UniProt/Notari named; not independently primary-verified | Correction propagated to code/results/summary, but not all wiki surfaces |
| CR1 SCR1-4 has 8 disulfides | `payloads.json`, `analyze.py`, outputs | Hard-coded folding/secretion scores | UniProt P17927 named; not independently primary-verified | Used consistently |
| BCoAT native 448 aa cytoplasmic enzyme | `payloads.json`, `provenance.md`, `analyze.py` | Hard-coded tractability/folding/secretion scores | UniProt C7H5K4 named; not independently fetched | Supports tractability ranking; therapeutic flux not established |
| Composite scores 0.748 / 0.565 / 0.540 / 0.393 | `analyze.py`, `results.json`, `summary.md`, README | Derived from hard-coded geometric means | Reproducible by inspection; code not executed | Internally plausible |
| Toolkit-conditional scores 0.875 / 0.635 / 0.603 / 0.419 | `analyze.py`, `results.json`, `summary.md` | Derived by excluding toolkit factor | Reproducible by inspection; code not executed | Useful but should not be read as empirical “conditional GREEN” without folding/titer data |
| Butyrate comp-007 selectivity `>=167x` and bioavailability caveat | `analyze.py`, `outputs/summary.md` | Summary-only claim, not part of scoring | Refers to comp-007; not independently reviewed here | Corrected in generated summary, stale in archive/wiki pages |
| Engineered Fp butyrate solves bioavailability | `wiki-archive.md`, interpretive page, `abcg2-modulators.md` | Summary/wiki claim, not implemented | Unsupported by comp-008 | Invalid wording; must be changed to proposed/gated |

## Affected wiki pages
- `wiki/f-prausnitzii-heterologous-expression-computational.md` — change required — stale cross-link says engineered Fp butyrate “solves oral bioavailability”; should match corrected `outputs/summary.md`.
- `wiki/etc/experiments/comp-008-f-prausnitzii-heterologous-expression/wiki-archive.md` — change required — stale generated/archive summary still has overstrong comp-007 cross-link and old uncensored `167×` framing.
- `wiki/abcg2-modulators.md` — change required — LBP engineering section says engineered colonically resident butyrate producer “solves” bioavailability; should be “is proposed to address dose-frequency bioavailability, pending colonization/titer/exposure/Q141K validation.”
- `wiki/open-questions.md` — change required — some engineered-Fp / local-butyrate shorthand still implies Q141K rescue as an achieved mechanism; add direct validation and exposure caveat.
- `wiki/modality-chokepoint-matrix.md` — change required — engineered Fp local butyrate row/open question should say proposed Q141K rescue, not established coverage.
- `wiki/engineered-lbp-chassis.md` — already mostly consistent — corrected caveat is present; follow-up table still labels comp-008/P2-4 “Queued,” which is stale relative to the added comp-008 section and should be updated for queue hygiene.
- `wiki/hypotheses/H02-engineered-lbp-thesis.md` — already consistent — explicitly says direct butyrate Q141K rescue is unvalidated and §1.14-gated.
- `wiki/validation-experiments.md` — already consistent in relevant sections — §1.14 contains the direct butyrate/Q141K rescue arm.
- `wiki/computational-experiments.md` — already broadly consistent — comp-008 planned table marks completed and links interpretive page; no urgent numerical mismatch found.

## New connections or implications
Comp-008’s most useful cross-corpus implication is not merely “BCoAT wins”; it distinguishes **engineering tractability** from **therapeutic flux sufficiency**. That distinction should govern every downstream butyrate/LBP statement. Fp is attractive because native BCoAT overexpression is the lowest-friction engineering campaign, but the therapeutic mechanism still needs a separate exposure chain: engineered strain viability → colonization density → acetate/BCoAT flux → butyrate titer near epithelium → ABCG2 induction and/or direct Q141K trafficking rescue.

A second grounded implication is that strict-anaerobe chassis selection should treat O₂-dependent enzymes as a chemistry-level exclusion, not a toolkit problem. This aligns comp-008 with later UOX regime work: uricase belongs in a facultative/microoxic or aerobic/transit topology, not in Fp.

## Required actions
1. Correct `wiki-archive.md` comp-007 cross-link to match `outputs/summary.md`: `>=167x` censored lower bound; engineered Fp butyrate is proposed/gated, not proven to solve bioavailability.
2. Correct `wiki/f-prausnitzii-heterologous-expression-computational.md` final comp-007 cross-link with the same caveat.
3. Harmonize `wiki/abcg2-modulators.md`, `wiki/open-questions.md`, and `wiki/modality-chokepoint-matrix.md` wherever engineered Fp/local butyrate is described as “solving” bioavailability or “hitting” Q141K rescue; wording should explicitly require colonization density, butyrate titer, epithelial exposure, and validation §1.14.
4. Update `wiki/engineered-lbp-chassis.md` Open Follow-Ups table so P2-4/comp-008 is no longer marked queued.
5. Document in README or provenance that `payloads.json` is a provenance/manual-scoring support file and is not executable input to the scoring model; alternatively refactor `analyze.py` to derive displayed load-bearing metadata from the JSON.
6. Fix minor reproducibility/link hygiene: README file tree path and generated `outputs/summary.md` relative wiki links.

## Review limits
I did not execute `python3 analyze.py`; reproducibility was assessed by code and output inspection only. Primary sources (UniProt, Fraccascia, Sheridan, Martín, Quévrain, Notari, etc.) were not independently fetched or verified. Repository fixed-string search failed because `rg` was unavailable, so affected-page discovery relied on the supplied explicit pages plus direct reads of omitted high-risk pages. `validation-experiments.md` and `koji-endgame-strain.md` were only inspected in relevant sections due to size/tool budget. No prior review logs were inspected.
