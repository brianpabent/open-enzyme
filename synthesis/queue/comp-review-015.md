---
type: comp-review
sweep_date: 2026-07-15
sweep_sha: eeab5b5
comp: comp-015
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-015


ACTION_REQUIRED: yes

REVIEWED_SNAPSHOT: commit:eeab5b53054b93544c428a476dad06a8f8fe2621

# Independent comp review — comp-015

## Reviewed snapshot
Independent API reviewer; daemon-mode review of commit `eeab5b53054b93544c428a476dad06a8f8fe2621`. I inspected the supplied complete comp-015 artifact bundle, all supplied generated outputs (`outputs/results.json`, `outputs/summary.md`, `wiki-archive.md`), the committed README update, and the top-level wiki pages supplied in the bundle. Repository search tooling failed because `rg` was unavailable in the tool environment; I used direct file reads for several omitted/high-risk pages (`prps-purine-biosynthesis-chokepoint.md`, `gout-action-guide.md`, `genotype-informed-supplement-workflow.md`, `validation-experiments.md`, `medicinal-mushroom-complement-track.md`). I did not execute `analyze.py`.

## Bottom-line verdict
**Action required.** The broad qualitative reframe is plausible but not materially clean: the artifact conflates *eurycomanone*, *eurycomanol*, and whole *Eurycoma longifolia*/Physta extract; the code/output reproducibility contract appears broken for at least one generated link; several summary/wiki surfaces overstate or inconsistently count evidence cells; the interpretive stub still states a four-target question despite v2 being five-target; and at least one affected hypothesis page still repeats the corrected-away “eurycomanone via XO” mechanism.

The current result is best treated as a **lead-generation reframe**: cordycepin remains gout-favorable by animal URAT1 expression evidence; tongkat/*Eurycoma* extract/eurycomanol-family evidence is directionally gout-favorable but not cleanly attributable to pure eurycomanone at human supplement exposure; icariin/echinacoside remain mechanism-unclear on the urate-production/transport panel.

## Implementation and constraint closure
I traced the pipeline from `inputs/*.json` through `analyze.py` to `outputs/results.json` and `outputs/summary.md`.

Key implementation findings:

- **Code/output mismatch likely breaks deterministic reproduction.** In the supplied `analyze.py`, the generated summary link appears as `../../wiki/t-axis-adjuvant-urate-mapping-computational.md`, while the committed `outputs/summary.md` contains `../../../t-axis-adjuvant-urate-mapping-computational.md`. If the supplied code is current, rerunning would not regenerate the committed output identically. This violates the stated reproduction contract.
- **README reproduction path is wrong.** It says `cd experiments/comp-015-t-axis-adjuvant-urate-mapping`, but the tracked path is `wiki/etc/experiments/comp-015-t-axis-adjuvant-urate-mapping`.
- **README file list is stale.** It describes `inputs/targets.json` as “4 targets” even though v2 has five.
- **Eurycomanone literature rows are stored twice in `literature_claims.json`.** The original v1 no-data rows and later v2 reopened rows coexist. The code silently resolves this by overwriting earlier rows in `lit_by_pair`, which is acceptable if intentional, but fragile and not explicitly documented in the implementation.
- **Direction-alignment logic over-promotes uncertain OAT1 wording.** `analyze_pair()` marks direction favorable if the target’s canonical favorable word appears anywhere in the literature direction. The eurycomanone OAT1 direction is `"UNKNOWN — POSSIBLY INDUCER..."`, so it is marked `direction_alignment: favorable`, and the summary matrix shows a checkmark for a mechanistic-extrapolation/unknown-direction cell. This is not load-bearing for the final verdict because tier 1 is not counted as a favorable transporter hit, but it is a summary-fidelity problem.
- **Negative-screen evidence is internally mishandled.** Icariin × XO is semantically a negative-screen evidence row, but `evidence_tier()` reduces it to `"No-Data"` tier 0; downstream special-case logic recovers the negative-screen class via the direction string. The output therefore says “Negative-screen evidence … No-Data,” which is confusing and should be fixed.
- **The model does not truly answer “which compound is most gout-favorable.”** It classifies compounds by qualitative verdict but does not implement a ranking metric. The output narrative then makes comparative claims (“eurycomanone better-characterized,” “head-to-head,” “comparable”) that are not derived from a quantitative ranking.
- **Hidden substitution: pure compound vs extract vs related metabolite.** The experiment is titled and keyed as “Eurycomanone,” but the load-bearing evidence includes:
  - *Eurycoma longifolia* stem extract at 100/200/400 mg/kg in animal models;
  - isolated quassinoids including eurycomanone/eurycomanol/eurycomalactone for hURAT1 uptake inhibition;
  - eurycomanol in PMID 34785103 for PRPS/transporter modulation;
  - Physta human trial summary values at 100/200 mg/day extract.
  
  The code’s concentration model uses ~2 mg pure eurycomanone per 200 mg Physta extract, but the direction-of-effect evidence is not cleanly anchored to that pure-compound exposure. The README caveat’s “tongkat/eurycomanone-family” wording is more accurate than much of the artifact’s “Eurycomanone” labeling.
- **Concentration closure is partial.** Cordycepin × XO is correctly bounded: 0.057 µM modeled Cmax vs 55.7 µM IC50 → ratio ~0.001, below systemic threshold. For cordycepin × URAT1 and the *Eurycoma* transporter effects, the artifact relies on animal expression/transport evidence without IC50/Ki and without a clean human-achievable tissue-exposure bridge. The artifact usually discloses this but the verdict surfaces sometimes read stronger than the implementation supports.
- **Compartment closure is mixed.** XO site is correctly forced to plasma/systemic exposure rather than gut lumen. ABCG2 uses gut-lumen concentration even when the cited *Eurycoma* ABCG2 effect is kidney protein upregulation, not direct intestinal luminal inhibition/induction. This is not fatal for direction tagging but weakens any exposure/potency inference.
- **Mass balance/replenishment/time are not modeled.** This is a qualitative evidence map, not a kinetic urate model. The artifact should avoid implying quantitative SUA prediction beyond cited animal/human observations.
- **Safety/off-target closure is limited.** The artifact flags Chinese-language gaps, ChEMBL/API gaps, rat-derived BA, cordycepin ADA metabolism, and eurycomanone magnitude gaps. It does not fully resolve quassinoid off-targets, extract composition variability, or human exposure of the active quassinoids.

## Summary-fidelity audit
The README, outputs, wiki archive, interpretive stub, computational index, and affected pages are not fully reconciled.

Material mismatches and overstatements:

- **`outputs/summary.md` appears not to be regenerated by the supplied `analyze.py`** because of the link-path mismatch noted above.
- **Interpretive stub `wiki/t-axis-adjuvant-urate-mapping-computational.md` still asks the v1 four-target question.** It says the analysis asks about “the four dominant urate-handling + T-axis targets (URAT1, ABCG2, OAT1, SHBG)” even though the page title/frontmatter and v2 artifact are five-target with XO. This is a direct stale-summary issue.
- **Evidence-cell counts are inconsistent.**
  - `results.json` says 7/20 pairs with primary-literature evidence.
  - `wiki-archive.md` says “FIVE cells have direct evidence,” then lists cordycepin × URAT1, cordycepin × XO, eurycomanone × URAT1, eurycomanone × ABCG2, eurycomanone × SHBG, plus the icariin × XO negative-screen — effectively six named cells if SHBG is counted, or five direct urate-axis cells only if SHBG/negative-screen are excluded. The wording needs one explicit denominator and inclusion rule.
  - `literature_claims.json` summary says 5 direct-evidence cells and 2 indirect, but includes eurycomanone × OAT1 as a reopened mechanistic-extrapolation row. The narrative should separate “direct urate-axis evidence,” “negative evidence,” “T-axis SHBG evidence,” and “off-panel PRPS evidence.”
- **Eurycomanone/Eurycoma attribution is too strong in several surfaces.** The computational index, action guide, personal-genome table, and archive often say “Eurycomanone = GOUT-FAVORABLE,” while the clean conclusion is “standardized *Eurycoma*/Physta or eurycomanone-family quassinoid evidence is gout-favorable at lead-generation tier; pure eurycomanone magnitude is unanchored.”
- **`hypotheses/H07-clomid-intestinal-er-antagonism.md` still contains stale XO wording.** It says direct urate-axis modulators include “eurycomanone via XO + multi-target transporter modulation.” That contradicts comp-015 v2’s central correction that the XO mechanism was citation laundering.
- **`androgen-natural-modulation.md` is partially reconciled.** The supplied section 1.7/1.9 correctly states transporter + PRPS and says the XO claim was citation-laundering. However, other parts of the corpus still repeat older or stronger wording.
- **`gout-action-guide.md` promotes tongkat/Physta as an actionable androgen-elevated-path supplement with RCT SUA −7–11%.** That page is an application surface and is clearer than the experiment about mechanism, but the underlying human RCT values are described in the artifact as paywalled/product-summary-derived rather than primary-source-verified. Promotion to an action guide should either be softened or include a direct provenance caveat.
- **`personal-genome-protocol.md` genotype table is explicitly speculative, but it overstates Q141K rescue logic.** “Eurycomanone’s ABCG2-up arm directly addresses Q141K” is mechanistically plausible only if expression/upregulation meaningfully rescues a misfolded/LoF transporter; no genotype-stratified evidence is present. The page does label the whole section speculative, which mitigates but does not fully close the claim.
- **`prps-purine-biosynthesis-chokepoint.md` is broadly consistent** with comp-015’s PRPS finding and accurately labels the human-RCT-to-PRPS connection as mechanistic extrapolation.
- **`medicinal-mushroom-complement-track.md` is broadly consistent** on cordycepin’s product-dose gap and animal URAT1 evidence, and it adds later CNKI/whole-extract evidence not used by comp-015. This does not independently validate comp-015 but is a relevant cross-corpus connection.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---|---|
| `wiki/etc/experiments/comp-015-t-axis-adjuvant-urate-mapping/outputs/results.json` | generated_output | Yes, supplied content inspected | Internally structured and largely traceable to code/inputs, but inherits pure-compound/extract/metabolite conflation; eurycomanone OAT1 marked favorable despite unknown/possible direction; negative-screen handling emits “No-Data” label. |
| `wiki/etc/experiments/comp-015-t-axis-adjuvant-urate-mapping/outputs/summary.md` | generated_output | Yes, supplied content inspected | Not fully reproducible from supplied code due apparent link-path mismatch; summary matrix overmarks eurycomanone OAT1 as ✓ Mech and icariin XO as “? ?”; evidence counts need clearer category definitions. |
| `wiki/etc/experiments/comp-015-t-axis-adjuvant-urate-mapping/wiki-archive.md` | generated_output / archived interpretive summary | Yes, supplied content inspected | Rich but overlong; contains inconsistent evidence-cell counts, pure-compound/extract conflation, and application-like supplement wording that should remain Phase 0/caveated. |
| `wiki/etc/experiments/comp-015-t-axis-adjuvant-urate-mapping/README.md` | proposed_update / committed trigger update | Yes, supplied content inspected | New caveat is directionally appropriate, but README still has stale “4 targets” file description and wrong reproduction `cd` path; v2 conclusion remains stronger than artifact’s quantitative closure unless framed as lead-generation only. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Four compounds × five targets = 20 pairs | `targets.json`, `results.json`, `summary.md` | Loops over `targets_input["targets"]` and all compounds | Directly present in inputs | Verified in implementation. README/stub text has stale four-target wording. |
| XO added as fifth target | `targets.json`, README, archive, output summaries | Adds `Xanthine Oxidase` pair per compound; `classify_xo_contribution()` | Target IDs cited as reused from comp-013; not independently fetched here | Panel addition is justified; provenance partly inherited. |
| Cordycepin × XO IC50 0.014 mg/mL = 55.7 µM | `chembl_bioactivity.json`, `literature_claims.json`, `results.json` | Only numeric IC50; used for achievable/IC50 ratio | Citation string PMID 38141695; primary not directly available in artifact beyond citation/claimed WebSearch | Arithmetic conversion is correct: 0.014 mg/mL / 251.24 g/mol ≈ 55.7 µM. Primary-source verification not independently performed here. |
| Cordycepin Cmax 0.057 µM at 50 mg, F=2%, Vd=70 L | `concentration_estimates.json`, `results.json` | Used for XO ratio and plasma-site rows | BA bound from PMC6823370/PMIDs; no primary text in artifact | Formula checks: 50 mg × 0.02 / 70 L = 0.0143 mg/L; /251.24 = 0.057 µM. Caveated appropriately. |
| Cordycepin × XO ratio ~0.001 below systemic threshold | `results.json`, `summary.md`, archive | Drives “in vitro only” XO classification | Derived from above | Verified arithmetic and conclusion; do not cite as systemic XO mechanism. |
| Cordycepin × URAT1 animal SUA 337→216/210/203 µmol/L | `literature_claims.json`, `results.json`, archive | Main driver of cordycepin `GOUT-FAVORABLE` | Citation PMID 29422889; primary not directly included | Plausible and consistently reported; not independently primary-verified here. Expression-level, not binding IC50. |
| Eurycomanone/tongkat URAT1/ABCG2 favorable mechanism | `literature_claims.json`, `results.json`, archive | Main driver of eurycomanone `GOUT-FAVORABLE` | PMIDs 31920654/34785103 cited; specific IC50/fold-changes behind paywall | Directional lead supported at literature-claim tier, but pure eurycomanone vs extract/eurycomanol attribution unresolved. |
| Eurycomanone × XO no direct evidence / citation-laundering correction | `chembl_bioactivity.json`, `literature_claims.json`, archive, androgen-natural-modulation | Used to avoid XO contribution for eurycomanone | Based on artifact’s primary-source reread; not independently reverified here | Important correction and likely valid. Needs propagation to H07 and any remaining XO phrasing. |
| Eurycomanone human RCT SUA ↓7–11%, n=105 | archive, summary, androgen-natural-modulation, gout-action-guide | Supports human direction and action-guide promotion | Artifact says primary publication paywalled/product summary corroborates; not directly verified | Should be cited as secondary/product-summary-derived unless primary paper is directly obtained. Too strong for action-guide without caveat. |
| Eurycomanone Cmax 0.0073 µM from 2 mg pure dose | `concentration_estimates.json`, `results.json` | Used as plasma concentration for eurycomanone rows | Rat BA source; pure dose inferred from Physta content | Arithmetic plausible, but mismatched to extract/eurycomanol evidence; not a clean exposure bridge. |
| Icariin × XO negative screen | `chembl_bioactivity.json`, `literature_claims.json`, `results.json` | Drives `xo-negative-screen`, mechanism-unclear verdict | PMID 17666819 cited; primary not directly included | Directional negative-screen claim plausible; code labels evidence as “No-Data,” needing cleanup. |
| Icariin/echinacoside mechanism-unclear on urate axis | `results.json`, `summary.md`, archive | Final verdict | Based on absence of English-language evidence and no ChEMBL | Correct only within stated scan limits; multilingual gap remains. |
| ChEMBL API blocked | `provenance.md`, `chembl_bioactivity.json`, summary | Explains lack of curated records and route to literature claims | Stated environment status; not independently tested | Accept as artifact limitation; rerun with API access remains future action if quantitative potency is needed. |
| Reproduction command regenerates outputs identically | README, `analyze.py`, outputs | Reproducibility contract | Inspection only; code not executed | Not established; apparent code/output mismatch and wrong README path require correction. |

## Affected wiki pages
- `wiki/t-axis-adjuvant-urate-mapping-computational.md` — **change required** — stub still frames the question as four targets and omits XO in the question text, despite v2 being five-target.
- `wiki/computational-experiments.md` — **already mostly consistent / minor change recommended** — comp-015 entry captures the v2 verdict and citation-laundering correction, but should avoid implying pure eurycomanone-specific certainty where evidence is extract/eurycomanol-family.
- `wiki/androgen-natural-modulation.md` — **already mostly consistent** in the supplied tongkat section — correctly states transporter + PRPS and rejects XO; retain caveat that the 2021 RCT values are not directly primary-verified in the artifact.
- `wiki/hypotheses/H07-clomid-intestinal-er-antagonism.md` — **change required** — still says “eurycomanone via XO + multi-target transporter modulation,” contradicting comp-015’s core correction.
- `wiki/personal-genome-protocol.md` — **change required / soften** — genotype-stratified table is marked speculative, but “Eurycomanone’s ABCG2-up arm directly addresses Q141K” should be softened because Q141K is a folding/LoF variant and no genotype-stratified eurycomanone evidence exists.
- `wiki/gout-action-guide.md` — **change required / caveat** — androgen-elevated path promotes tongkat ali/Physta with human SUA −7–11% values; this should explicitly say the human values are not primary-source-verified in comp-015 unless the primary RCT is obtained.
- `wiki/prps-purine-biosynthesis-chokepoint.md` — **already consistent** — accurately treats PRPS as a new stub-level chokepoint and labels the human-RCT-to-PRPS bridge as mechanistic extrapolation.
- `wiki/medicinal-mushroom-complement-track.md` — **already consistent with limitations** — cordycepin product-dose gap and animal URAT1 evidence are appropriately caveated; later whole-extract evidence is outside comp-015 and should not be treated as independent confirmation of the comp-015 purified-cordycepin model.
- `wiki/validation-experiments.md` — **change may be required** — comp-015 archive proposes a cordyceps vs tongkat/Physta head-to-head trial, but I could not confirm a dedicated registered validation section before tool budget exhaustion. If absent, add or deliberately defer with rationale; if present later in the file, ensure it is framed as lead-generation/head-to-head, not confirmation of a validated quantitative result.
- `wiki/genotype-informed-supplement-workflow.md` — **already mostly consistent** — references comp-015 genotype-informed selection in a speculative workflow; no direct action beyond avoiding overclaiming in linked `personal-genome-protocol.md`.

## New connections or implications
- The comp-015 v2 finding is less “eurycomanone beats cordycepin” than “the prior binary was under-recalled.” The strongest methodological implication is search-recall sensitivity: v1’s uniqueness claim failed because an existing *Eurycoma* hyperuricemia literature strand was missed.
- PRPS is a legitimate new corpus chokepoint, but comp-015 does not establish that Physta’s human SUA effect is mediated by PRPS. The PRPS page correctly keeps that as mechanistic extrapolation.
- The cordycepin track has an internal tension: comp-015 uses a 50 mg cordycepin midpoint and shows systemic XO is inactive, while the medicinal-mushroom track later emphasizes that ordinary fruiting-body products may deliver only a few mg cordycepin per serving. Any consumer-facing “cordyceps URAT1” claim must be dose-form specific.
- Genotype-stratified T-axis adjuvant selection is a reasonable future hypothesis, but the current evidence does not resolve Q141K-specific response, URAT1 genotype response, or eurycomanone-vs-cordycepin ranking.

## Required actions
1. **Fix reproducibility contract.** Update `analyze.py` or regenerate `outputs/summary.md` so the committed output is byte-identical to a rerun; correct the README `cd` path to `wiki/etc/experiments/comp-015-t-axis-adjuvant-urate-mapping`; verify with a local rerun.
2. **Correct stale target-count text.** Update README file description and `wiki/t-axis-adjuvant-urate-mapping-computational.md` question text from four-target to five-target v2 wording including XO.
3. **Separate evidence categories and counts.** Revise `wiki-archive.md`, `outputs/summary.md`, and any index text to distinguish: direct urate-axis evidence, negative-screen evidence, SHBG/T-axis evidence, mechanistic extrapolation, off-panel PRPS evidence, and human SUA outcome evidence.
4. **Fix code labeling for uncertain/negative evidence.** Do not mark `"UNKNOWN — POSSIBLY INDUCER"` as a favorable checkmark; preserve “Negative Screen” as an evidence class rather than converting it to `No-Data`.
5. **Resolve the eurycomanone/extract/eurycomanol substitution.** Rename the verdict surface or add explicit fields distinguishing pure eurycomanone, eurycomanol, quassinoid mixture, *Eurycoma longifolia* extract, and Physta. State which entity each PMID actually tested.
6. **Propagate the XO correction.** Remove stale “eurycomanone via XO” wording from `hypotheses/H07-clomid-intestinal-er-antagonism.md` and any other pages found by a full repo search once tooling is available.
7. **Caveat or primary-verify the Physta SUA RCT.** Either obtain and cite the primary publication for the n=105 SUA −7–11% values or mark those values as secondary/product-summary-derived wherever they are promoted, especially in `gout-action-guide.md`.
8. **Soften genotype-specific claims.** In `personal-genome-protocol.md`, rewrite Q141K preference language as a hypothesis requiring genotype-stratified testing, not a direct rescue claim.
9. **Confirm validation propagation.** Ensure the cordyceps vs tongkat/Physta head-to-head trial is either registered in `validation-experiments.md` with lead-generation wording and endpoints, or explicitly deferred.

## Review limits
- I did not execute `analyze.py`; reproducibility findings are by inspection.
- Repository fixed-string search failed because `rg` was unavailable, so affected-page discovery is incomplete. I compensated by reading supplied pages and several omitted high-risk pages directly, but a later full search for “eurycomanone,” “XO,” “PRPS,” “Physta,” “H-AN-02,” and “cordycepin” is still required.
- I did not independently access PubMed/ChEMBL/PubChem or primary full texts; provenance is assessed from artifact citations and internal consistency, not primary-source verification.
- Tool-result budget was exhausted before I could inspect all of `validation-experiments.md` and `supplements-stack.md`; conclusions about those pages are therefore bounded.
- Prior `reviews/` logs were not supplied and were not inspected.
