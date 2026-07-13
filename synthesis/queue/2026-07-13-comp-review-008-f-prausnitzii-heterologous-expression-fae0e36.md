---
type: comp-review
sweep_date: 2026-07-13
sweep_sha: fae0e36
comp: comp-008
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-008

Canonical review log: [`logs/comp-reviews/2026-07-13-comp-008-fae0e36.md`](../../logs/comp-reviews/2026-07-13-comp-008-fae0e36.md)

ACTION_REQUIRED: yes

# Independent comp review — comp-008

## Bottom-line verdict
Action required — the artifact is plausibly deterministic and the headline qualitative direction is mostly defensible, but the artifact-summary-corpus contract is not clean. The main issues are: hardcoded expert scores are presented as if they derive from JSON payload metadata; lactoferrin disulfide correction is incompletely propagated; `payloads.json` still stores `disulfide_bonds: 17`; output summaries still contain stale “17 disulfides” text for sCR1 comparisons; `computational-experiments.md`, `engineered-lbp-chassis.md`, `open-questions.md`, and H02 still carry queued/planned or stale framing; and the butyrate “winner” substitutes native-enzyme feasibility for demonstrated butyrate-flux increase without mass-balance or rate-control closure.

## Implementation and constraint closure

**What was traced.** `analyze.py` loads `inputs/payloads.json` and `inputs/chassis_profile.json`, but only the chassis object is actually used for a few output fields. The payload metadata is loaded and then not used in scoring. All payload factor values, rationales, sensitivity ranges, verdicts, and rankings come from the hardcoded `SCORES` dictionary. The computation itself is simple and deterministic: geometric mean of eight factor values, low and high geometric means from all-low/all-high factor ranges, threshold labels at GREEN ≥0.60, YELLOW 0.30–0.59, RED <0.30.

**Stored-but-unused / implementation closure findings.**
- `payloads.json` is not a source of implemented scoring. Lengths, GC%, disulfide counts, glycosylation flags, O₂ substrate flags, secretion requirements, and source organisms are documentation-only unless manually duplicated in `SCORES`.
- This matters because the corrected lactoferrin disulfide count is implemented in code rationales as 16, but `payloads.json` still stores `"disulfide_bonds": 17`. The verification note says 16, creating an internal contradiction.
- The payload input `_note` says CAI is “computed analytically,” but the code computes no CAI/RSCU/codon table. GC/codon scores are expert estimates.
- `chassis_profile.json` contains many detailed fields that are not programmatically used in the score, e.g., RM systems, growth medium, MAM secretion baseline, and engineering complexity factors.
- The low/high ranges are not a true one-at-a-time sensitivity analysis; they are all-low and all-high scenario geometric means.
- The geometric mean clamps zeros to 0.01, but no factor is zero, so this has no current effect.
- Output generation contains wrong/stale relative links: `outputs/summary.md` writes `../../wiki/engineered-lbp-chassis.md`, which is not a valid path from `wiki/etc/experiments/comp-008-f-prausnitzii-heterologous-expression/outputs/`. README reproduction path also says `cd experiments/...` rather than the tracked `wiki/etc/experiments/...` path.

**Reaction / operating-regime closure.**
- **Uricase:** The core constraint is correctly identified: uricase requires urate + O₂ + H₂O and produces H₂O₂. That is a real chemistry-host mismatch for a strict anaerobe in an anoxic colonic lumen. However, the model does not quantify O₂ availability, urate transport into the cell, allantoin export, H₂O₂ detox capacity, residence time, or local peroxide peaks. The artifact’s qualitative “do not put uricase in Fp” conclusion is stronger than the numeric YELLOW label but mechanistically plausible.
- **Lactoferrin:** The artifact recognizes secretion, iron-binding, glycosylation, and 16-disulfide folding as constraints. It does not close bicarbonate/iron loading, luminal Fe availability, proteolysis after secretion, secretion titer, or whether an anoxic exterior/periplasm-equivalent space can form the correct transferrin fold. The correction from 17 to 16 disulfides is incomplete.
- **sCR1 SCR1-4:** The artifact recognizes secretion and 8 disulfides. It does not model complement substrates, C3b/C4b/MSU access, luminal complement concentration, functional decay-acceleration, residence time, or correct disulfide pairing. The code and outputs still compare sCR1 to “lactoferrin’s 17 disulfides” in some places.
- **BCoAT / butyrate pathway boost:** The winner is a native cytoplasmic enzyme and thus the lowest expression/folding risk. But the model does **not** establish that BCoAT is rate-limiting, that overexpression increases net butyrate output, that acetate/acetyl-CoA/butyryl-CoA pools are sufficient, that flux is not feedback-limited, or that local colonic butyrate reaches ABCG2/HDAC-relevant exposure. The payload verification note gives the reverse reaction direction (`butanoate + acetyl-CoA -> butanoyl-CoA + acetate`), while the engineering claim depends on butyrate production direction. Directionality and thermodynamic/flux context need correction or explicit bidirectional framing.

**Constraint coverage gaps.**
- No finite mass balance for substrates, cofactors, coproducts, or products.
- No residence-time / exposure-time model for any payload.
- No transport/access model for urate into Fp, allantoin out, secreted lactoferrin/sCR1 diffusion, or butyrate efflux.
- No secretion titer model; Sec/Tat presence is treated as availability, not capacity.
- No safety model for local iron sequestration, H₂O₂, butyrate local peaks, host fitness burden, or engineered LBP containment.
- Sensitivity ranges mostly cover scoring uncertainty, not dominant biological uncertainties such as BCoAT flux control, transformation efficiency, secretion titer, Dsb capacity, O₂ microgradients, or colonization density.

## Summary-fidelity audit

**README vs code/outputs.**
- README headline scores match `results.json` and `summary.md`.
- README claims payload metadata records are “UniProt-verified,” but primary UniProt records are not stored and not programmatically checked; the artifact contains citation strings and verification notes only.
- README “How to reproduce” path is wrong/incomplete relative to the tracked repository path.
- README says the computational tracking row was promoted from Planned to Analyses, but the provided `wiki/computational-experiments.md` still lists comp-008 under Planned Analyses.

**`outputs/summary.md` / `wiki-archive.md` vs code.**
- Numeric scores and rankings match the code.
- Stale lactoferrin disulfide text remains:
  - sCR1 `secretion_pathway_availability` rationale says “less than lactoferrin’s 17”.
  - Key finding #4 says “8 vs 17”.
- `outputs/summary.md` generated link to `engineered-lbp-chassis.md` is wrong after the trigger diff.
- The summary calls lactoferrin and sCR1 “conditional GREEN” in the toolkit-conditional context. Numerically this is true only after removing the toolkit factor and only barely for lactoferrin (0.603), while disulfide folding remains unresolved. This should remain explicitly “conditional/provisional,” not a wet-lab priority upgrade.

**Interpretive page.**
- `wiki/f-prausnitzii-heterologous-expression-computational.md` is mostly aligned with the intended conclusions and uses 16 disulfides for lactoferrin.
- It does not expose that the JSON payload metadata is not used in the computation.
- It correctly frames uricase as wrong for Fp, but this is stronger than the formal composite verdict label YELLOW; the page should clarify that the RED conclusion is a host-physiology sub-verdict, not the composite label.

**Tracking/index and hypothesis surfaces.**
- `wiki/computational-experiments.md` is stale: comp-008 remains in Planned Analyses rather than Analyses despite README and interpretive page claiming completion.
- `wiki/engineered-lbp-chassis.md` has a good comp-008 section, but its Open Follow-Ups table still lists P2-4 as queued, and “Other plausible payloads” still includes heterologous uricase without the comp-008 contraindication.
- `wiki/open-questions.md` still lists comp-008 / P2-4 as queued.
- `wiki/hypotheses/H02-engineered-lbp-thesis.md` still says the assumption stack will be populated after comp-008 and still contains an anticipated assumption that Fp engineering tools are “research-grade tools published 2018–present,” which conflicts with comp-008’s “no published Fp transformation protocol” finding.

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Fp / A2-165 reclassified as *F. duncaniae*; A2-165 = DSM 17677 / JCM 31915 | `chassis_profile.json`, `provenance.md`, summaries | Used only in output text | Citation string to Sakamoto 2022; no primary text stored | Plausible but not independently verified in artifact |
| Genome GC 56.6%, size 2.78–3.23 Mbp, ~2795 genes | `chassis_profile.json`, `provenance.md` | GC used in output chassis; GC rationale hardcoded in scores | Provenance claims pre-commit grep from Fraccascia; primary text not stored | Plausible; source not directly verifiable here |
| Strict obligate anaerobe / anoxic colonic lumen | `chassis_profile.json`, code rationales | Drives uricase low host-physiology score | Citation context present but not primary-verified in artifact | Mechanistically central; needs primary-source verification if used for hard exclusion |
| No published Fp transformation protocol as of 2026-05 | `chassis_profile.json`, `provenance.md`, code | Hardcoded toolkit score 0.25 for all payloads | Based on Sheridan/Martín review and multilingual scan notes; no source snapshots | Load-bearing and plausible; unresolved primary verification |
| Engineering-toolkit-maturity = 0.25, range 0.15–0.35 | `analyze.py` `SCORES` | Direct factor in all composite scores; limiting factor for three payloads and BCoAT | Expert estimate, not derived from data | Reproducible but subjective |
| Uricase Q00511, 302 aa, O₂ substrate, H₂O₂ product | `payloads.json`, `provenance.md`, code | Hardcoded uricase host-physiology 0.10 and toxicity 0.20 | UniProt citation string only; reaction is standard | Mechanistically sound; primary source not stored |
| Uricase substrate/product transport in Fp | Mentioned in rationale | Not modeled | No source or calculation | Unclosed design decision |
| Lactoferrin P02788 length 710, mature 691 | `payloads.json`, `provenance.md`, code rationale | Hardcoded cluster-size score | UniProt citation string only | Plausible; not directly verified |
| Lactoferrin mature disulfide count = 16 | Code, provenance, verification note | Hardcoded in lactoferrin folding/secretion rationales | Notari 2023 citation; no primary verification | Partially corrected; **inconsistent with `payloads.json` field still saying 17** |
| sCR1 SCR1-4 = 280 aa, 8 disulfides | `payloads.json`, `provenance.md`, code | Hardcoded sCR1 scores | UniProt citation string and derived count | Plausible; source not stored |
| BCoAT C7H5K4 = 448 aa, native cytoplasmic enzyme | `payloads.json`, `provenance.md`, code | Hardcoded BCoAT high scores | UniProt citation string only | Plausible; source not stored |
| BCoAT overexpression increases butyrate output | `payloads.json` `oe_relevance`, code rationales, summaries | Central reason BCoAT wins | No flux model; no rate-control evidence; reaction direction text is ambiguous/reversed | **Unclosed; action required before treating as flux verdict** |
| Human payload GC ~58% vs Fp 56.6%; CAI/codon compatibility | `payloads.json`, code rationales, provenance | Hardcoded GC/codon scores | Framework estimate; no RSCU/CAI computation | Accept as qualitative prior only; summary should not imply computed CAI |
| Sec/Tat pathways present; MAM secretion documented | `chassis_profile.json`, code rationales | Hardcoded secretion scores | Citation strings to Quévrain/Breyner; no genome annotation evidence stored | Plausible but not sufficient for heterologous secretion capacity |
| Composite scores: BCoAT 0.748, sCR1 0.565, lactoferrin 0.540, uricase 0.393 | `results.json`, `summary.md`, code | Direct output | Deterministic from hardcoded scores | Reproducible by inspection |
| Toolkit-conditional scores: 0.875, 0.635, 0.603, 0.419 | `results.json`, `summary.md`, code | Direct output excluding one factor | Deterministic from hardcoded scores | Reproducible by inspection; should not be overread as solved biology |
| “Uricase should be removed from Fp payload menu” | README, summary, interpretive page | Summary conclusion, not a separate computed verdict | Mechanistic inference from O₂ requirement | Reasonable qualitative conclusion; label conflict with composite YELLOW should be clarified |
| “Continuous Fp butyrate solves bioavailability” | `summary.md`, interpretive page, `engineered-lbp-chassis.md` | Strategic implication | No colonization, titer, exposure, or ABCG2/Q141K rescue model in comp-008 | Overstrong as written; needs caveat/action |

## Affected wiki pages
- `wiki/f-prausnitzii-heterologous-expression-computational.md` — change required — mostly consistent, but should disclose that scores are hardcoded expert estimates rather than derived from `payloads.json`, and clarify that uricase is composite-YELLOW but host-physiology-RED/contraindicated.
- `wiki/computational-experiments.md` — change required — comp-008 remains in Planned Analyses despite being complete and explicitly referenced as completed elsewhere.
- `wiki/engineered-lbp-chassis.md` — change required — comp-008 section is largely reconciled, but Open Follow-Ups still says P2-4 queued, and “Other plausible payloads” still lists heterologous uricase for the chassis without the comp-008 contraindication.
- `wiki/open-questions.md` — change required — engineered LBP P2-4 / comp-008 remains queued; should be marked complete with the new open questions shifted to toolkit development, BCoAT flux validation, and chassis matrix P2-6.
- `wiki/hypotheses/H02-engineered-lbp-thesis.md` — change required — still pre-comp-008 stub language; assumption stack should replace “research-grade tools published” with the comp-008 finding that no Fp-specific transformation protocol is published as of 2026-05.
- `wiki/daf-lactoferrin-ecn-folding-feasibility-computational.md` — already consistent — uses lactoferrin 16 disulfides and appropriately treats high-disulfide LBP folding as capacity-gated.
- `wiki/lactoferrin.md` — already consistent on the 16-disulfide correction and fungal/koji production context; no comp-008-specific change required from this artifact alone.
- `wiki/abcg2-modulators.md` — already consistent on butyrate’s Q141K caveat and the need for direct validation; no comp-008-specific correction required, but it supports adding a BCoAT/butyrate exposure validation gate.
- `wiki/validation-experiments.md` — change required if comp-008 is used to reprioritize wet lab — add or cross-link an Fp-specific toolkit + BCoAT flux validation gate, with butyrate output measured by an appropriate assay, rather than treating the BCoAT score as a wet-lab-ready efficacy result.

## New connections or implications
- comp-008’s BCoAT winner connects directly to the Tier-2 butyrate assay gap: a native BCoAT overexpression campaign is not validated by expression alone; it requires measured butyrate flux in culture supernatant and eventually epithelial exposure. The comp-038 HPLC-UV / GC-MS butyrate assay path is therefore not ancillary; it is a necessary validation layer for this winner.
- The uricase/Fp exclusion aligns with later corpus direction from physiological UOX topology work: O₂ access, peroxide handling, and topology must be evaluated together. Fp should not be treated as a generic “gut-resident uricase chassis.”
- The lactoferrin/sCR1 Fp path should be read alongside the EcN disulfide-scaling result: high-disulfide payloads are not made safe by simply moving to an LBP chassis. Fp is even less characterized than EcN for oxidative folding, so “conditional GREEN” should stay highly provisional.
- The BCoAT reaction-direction ambiguity suggests a broader design rule: “native enzyme” does not imply “native flux boost.” A native-payload feasibility score must be separated from a metabolic-control coefficient or product-titer claim.

## Required actions
1. Update `inputs/payloads.json` so lactoferrin’s stored `disulfide_bonds` field is 16, or explicitly rename it if it represents a legacy/unverified value. Verification criterion: no artifact file contains an internal 16-vs-17 contradiction for lactoferrin.
2. Regenerate `outputs/results.json`, `outputs/summary.md`, and `wiki-archive.md` after fixing all stale “lactoferrin’s 17 disulfides” text in `analyze.py`, especially sCR1 secretion rationale and Key finding #4. Verification criterion: fixed-string search for `17 disulfides` and `lactoferrin's 17` in the comp-008 folder returns no live stale lactoferrin references.
3. Correct `outputs/summary.md` link generation for `engineered-lbp-chassis.md`, and fix README reproduction path to the tracked `wiki/etc/experiments/...` directory. Verification criterion: every relative link resolves from its actual file location.
4. Update `wiki/computational-experiments.md`: move comp-008 from Planned to Analyses or mark the planned row completed/redirected. Verification criterion: no current row implies comp-008 is still queued.
5. Update `wiki/engineered-lbp-chassis.md`: mark P2-4 complete, caveat/remove heterologous uricase from the Fp “plausible payloads” list, and keep BCoAT as the first Fp campaign only as an expression/flux-validation hypothesis.
6. Update `wiki/open-questions.md` and `wiki/hypotheses/H02-engineered-lbp-thesis.md` to incorporate comp-008’s actual findings: no Fp-specific published transformation protocol, BCoAT/native-butyrate boost as the leading payload, uricase contraindicated for Fp, and disulfide payloads gated on secretion/folding evidence.
7. Add or cross-link a validation gate for Fp BCoAT overexpression that measures actual butyrate output, acetate/acetyl-CoA/butyryl-CoA flux context, host fitness, and stability. Verification criterion: the validation surface distinguishes “BCoAT expression succeeds” from “butyrate flux increases to biologically relevant exposure.”
8. Soften or qualify corpus wording that says “continuous gut-luminal butyrate from engineered Fp solves bioavailability” until colonization density, product titer, epithelial exposure, and Q141K rescue are directly measured.
9. Primary-source verification should be repeated or archived for load-bearing claims if they remain decision-driving: Fp transformation absence, Sec/Tat/MAM secretion capacity, lactoferrin 16-disulfide count, BCoAT localization/reaction direction, and Fp oxygen/H₂O₂ detox capacity.

## Review limits
I did not execute `analyze.py`; reproducibility was assessed by code inspection only. Repository search via `grep_repo` failed because `rg` is unavailable, so affected-page discovery relied on bundled explicit pages and targeted `read_file` calls before the tool-result budget was exhausted. Primary sources such as UniProt records, Fraccascia 2022, Sheridan reviews, Notari 2023, and Quévrain/Breyner papers were not directly fetched or verified; the review treats artifact provenance notes as citation strings unless the cited text was included in the bundle. Some relevant pages (`koji-endgame-strain.md`, `modality-chokepoint-matrix.md`, `complement-c5a-gout.md`, H05) could not be inspected due to tool-result budget exhaustion.
