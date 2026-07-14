---
type: comp-review
sweep_date: 2026-07-14
sweep_sha: 8ee4d25
comp: comp-015
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-015

Canonical review log: [`logs/comp-reviews/2026-07-14-comp-015-8ee4d25.md`](../../logs/comp-reviews/2026-07-14-comp-015-8ee4d25.md)

ACTION_REQUIRED: yes

# Independent comp review — comp-015

## Bottom-line verdict
**Action required.** The qualitative v2 direction—“cordycepin remains gout-favorable; tongkat/eurycomanone-family evidence reverses the v1 unfavorable extrapolation; H-AN-02 uniqueness is partially falsified”—is plausible from the artifact, but the implementation/summary contract is not clean. The artifact overstates several points: it substitutes *Eurycoma longifolia* extract / eurycomanol evidence for “eurycomanone” as a pure-compound verdict, uses precomputed concentration estimates rather than computing them from declared model inputs, cites a human SUA RCT without directly available primary provenance in the structured inputs, and has stale or incorrect wiki/README wording and reproduction/link paths.

## Implementation and constraint closure
I traced `inputs/*.json` through `analyze.py` into `outputs/results.json` and `outputs/summary.md`.

Key implementation findings:

- **Precomputed concentration estimates are read, not computed.** `analyze.py` loads `inputs/concentration_estimates.json` and uses `cmax_plasma_uM` / `gut_lumen_uM`. It does **not** compute those values from `compounds[].typical_supplement_dose_mg`, `bioavailability_fraction`, MW, or `model_parameters`. The README/summary describe “compute serum + gut-luminal concentration ranges based on dose × F × Vd,” but the executable contract is “trust precomputed estimates.”
- **Many “unused” input leaves are documentation-only or precomputed-source fields.** This is not automatically a bug, but the artifact should not imply the script dynamically derives those values.
- **No sensitivity analysis is implemented.** The summary discusses caveats and optimistic BA correction qualitatively, but `analyze.py` does not sweep BA, dose, Vd, lumen volume, HED scaling, active-compound content, or residence time. Dominant uncertainties are therefore not quantitatively covered.
- **ChEMBL lookup is not performed.** The artifact stores blocked/inferred ChEMBL statuses. The code only reads the committed `chembl_bioactivity.json`. This is reproducible, but it is not a live “curated ChEMBL bioactivity lookup.”
- **Eurycomanone verdict uses a hidden mixture/substitution.** The compound row is named “Eurycomanone,” but load-bearing urate evidence is from *Eurycoma longifolia* stem extract, a quassinoid mixture including eurycomanone/eurycomanol/eurycomalactone, and purified **eurycomanol** for PRPS/transporter modulation. The verdict is better stated as “standardized *Eurycoma* / tongkat-quassinoid preparations are gout-favorable at current evidence tier,” not pure eurycomanone-specific.
- **Eurycomanone human RCT support is not implemented as a structured input.** The 2021 Physta n=105 SUA ↓7–11% claim appears in summary/wiki prose and some `verdict_contribution` text, but not as a distinct structured `literature_claims.json` claim with primary PMID/DOI. Provenance says the primary publication is paywalled and the values come from a trial/product summary. This should not be presented as primary-source verified clinical proof without qualification.
- **ABCG2 concentration-site handling is misleading for expression evidence.** For `site_for_concentration = "gut lumen ... AND plasma"`, code prioritizes gut lumen. But eurycomanone ABCG2 evidence is kidney protein-expression modulation after systemic/extract dosing, not direct gut-luminal ABCG2 inhibition/induction. No IC50 ratio is computed, so this does not drive verdict arithmetic, but the per-target table’s “achievable conc” field is not biologically closed.
- **Animal-dose translatability is asserted but not implemented.** Cordycepin URAT1 and eurycomanone/extract transporter evidence are animal-model/expression data. The script treats any favorable transporter literature tier ≥2/3 as sufficient; it does not compute HED, exposure matching, active-compound exposure, tissue access, or duration equivalence.
- **Cordycepin XO quantitative ratio is internally coherent.** IC50 55.7 µM vs Cmax 0.057 µM gives ratio ≈0.001 and fractional inhibition ≈0.001. The artifact appropriately concludes the XO arm is in vitro-only / below systemic threshold.
- **XO compartment access is mostly handled correctly in prose.** `targets.json` forces XO concentration site to plasma and notes intracellular hepatic/intestinal mucosal access; high gut-luminal cordycepin is not treated as meaningful XO exposure.
- **Safety/off-target closure is incomplete.** The artifact mentions quassinoid/PK caveats, cordycepin ADA metabolism, and contamination/supplement caveats elsewhere, but the computation has no redox burden, off-target, coproduct, local-peak, liver/kidney access, or toxicity model. It should remain Phase 0 mechanistic triage, not clinical recommendation.
- **Reproducibility contract is not clean.**
  - README command says `cd experiments/comp-015-t-axis-adjuvant-urate-mapping`; actual path is `wiki/etc/experiments/comp-015-t-axis-adjuvant-urate-mapping`.
  - `analyze.py` source currently writes the interpretive-link line as `../../wiki/t-axis-adjuvant-urate-mapping-computational.md`, but committed `outputs/summary.md` contains `../../../t-axis-adjuvant-urate-mapping-computational.md`. At least one of code/output is stale. Running the script may not regenerate outputs identically.
  - Both relative links appear suspect from `outputs/summary.md`; from `wiki/etc/experiments/comp-015.../outputs/`, the correct path to `wiki/t-axis...` would require going up four levels, not three.

Constraint closure:

- **Reaction/target substrates and products:** XO biology is included conceptually (hypoxanthine/xanthine → urate), but coproduct peroxide/redox burden is not modeled because the experiment is target mapping rather than UOX/XO flux. PRPS is discussed off-panel, not modeled.
- **Operating constants:** Only cordycepin×XO has an IC50 and ratio. URAT1/ABCG2/OAT1 verdicts lack Km/Ki/IC50 values and rely on direction-of-effect literature.
- **Physiological concentration vs operating constant:** Closed only for cordycepin×XO. Not closed for eurycomanone/quassinoid transporter effects.
- **Finite mass balance / residence time:** Not modeled. Gut-luminal concentrations are peak dose-density estimates, not residence-time exposure.
- **Localization/transport/access:** Partially discussed; not implemented quantitatively. Major open issue for expression-level mechanisms and for pure-compound vs extract exposure.
- **Coproducts/local peaks/off-targets/safety:** Mostly prose caveats, no computational closure.
- **Sensitivity ranges:** Not implemented; dominant uncertainties are active-compound content, BA, animal-to-human exposure, tissue concentration, extract-vs-pure substitution, and primary-source access.

## Summary-fidelity audit
Several summary surfaces are materially stronger or stale relative to the artifact.

- **README**
  - Question says five targets, but Files section still says `inputs/targets.json` contains “4 targets.”
  - Reproduction path is wrong for repo root.
  - Method says ChEMBL lookup and achievable-concentration computation; artifact actually reads blocked/inferred ChEMBL records and precomputed concentration estimates.
- **`outputs/summary.md`**
  - Mostly matches `results.json`, but includes stronger narrative claims than code derives: e.g., human Physta RCT support, “head-to-head wet-lab gate,” and eurycomanone clinical confirmation.
  - Verdict matrix shows eurycomanone SHBG as “✓ Clin,” but direct SHBG binding is not verified; the clinical evidence is T-elevation meta-analysis, not a direct SHBG target assay.
  - Icariin XO appears as `? ? (PMID 17666819)` due to the negative-screen evidence tier being downgraded to “No-Data” label by `evidence_tier()`. That display is ambiguous.
- **`wiki-archive.md` / interpretive page**
  - The archived full page’s “Question” still says “four dominant ... targets (URAT1, ABCG2, OAT1, SHBG)” despite v2 adding XO.
  - The live interpretive stub repeats the four-target question, while the title/status says v2 and tags XO. This is a stale topology statement.
- **`wiki/computational-experiments.md`**
  - The comp-015 entry broadly reflects v2, but it imports the strongest claims: 2021 RCT SUA −7–11%, PRPS suppression, and “eurycomanone better-characterized than cordycepin.” These need the extract/eurycomanol and provenance qualifiers.
- **`wiki/androgen-natural-modulation.md`**
  - §1.7/§1.9 are partly reconciled and correctly identify the XO claim as citation-laundering.
  - However §5.3 still says cordyceps is “the most gout-favorable T-axis adjuvant in this scan,” and §10 H-AN-02 still frames “Cordyceps as uniquely gout-favorable.” That conflicts with comp-015 v2.
- **`wiki/validation-experiments.md`**
  - The comp artifact proposes a 4-arm cordyceps/tongkat/placebo/combo head-to-head, but I did not see a corresponding dashboard entry in the inspected portion. If the corpus is going to claim wet-lab reprioritization from confirmation to head-to-head, the validation registry needs an explicit proposed experiment or an explicit decision not to register it.
- **`wiki/personal-genome-protocol.md`**
  - The genotype-stratified table is useful but stronger than comp-015 supports. It says eurycomanone’s ABCG2-up arm “directly addresses Q141K,” but comp-015 did not test Q141K rescue, transporter function in variant carriers, or human genotype-stratified response.
- **`wiki/genotype-informed-supplement-workflow.md`**
  - It derives URAT1 genotype supplement preferences “per comp-015 v2,” but comp-015 did not implement genotype stratification. This should be labeled as mechanistic extrapolation layered on top of comp-015, not a direct comp-015 result.
- **`wiki/gout-action-guide.md`**
  - The androgen-elevated path makes user-facing supplement recommendations based on comp-015. This is an application surface and should carry stronger Phase 0 / primary-source-unverified / extract-vs-pure qualifiers, especially for tongkat/eurycomanone and cordycepin dosing.
- **`wiki/prps-purine-biosynthesis-chokepoint.md`**
  - It states eurycomanol has “direct binding inhibition of PRPS catalytic activity.” The comp-015 artifact more consistently describes decreased PRPS expression / purine-synthesis suppression. Unless the primary paper truly shows direct PRPS binding/catalytic inhibition, the PRPS page overstates the mechanism.

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| 4 compounds × 5 targets = 20 pairs | `targets.json`, `compounds.json`, `results.json` | Fully iterated in `main()` | Directly inspectable in artifact | Clean |
| ChEMBL coverage is blocked/empty; only 1 published IC50 | `chembl_bioactivity.json`, `provenance.md` | Code reads committed JSON only; no API call | Artifact documents API 403; not independently re-fetched | Reproducible as stored, not a real lookup |
| Cordycepin×XO IC50 = 0.014 mg/mL = 55.7 µM | `chembl_bioactivity.json`, `literature_claims.json`, `results.json` | Used as `ic50_nM=55700`; ratio computed | Primary PMID string supplied; primary source not available in artifact; unit conversion arithmetically plausible | Internally coherent; primary verification unresolved |
| Cordycepin Cmax = 0.057 µM at 50 mg, F=2% | `concentration_estimates.json` | Used directly; not computed from dose/F/MW | BA source cited; precomputed value inspectable | Usable bound; not dynamically derived |
| Cordycepin XO ratio ≈0.001 | `results.json`, `summary.md` | Computed from Cmax/IC50 | Depends on two above | Clean internally; supports “not systemic-active” |
| Cordycepin×URAT1 animal SUA 337→203 µmol/L | `literature_claims.json`, `provenance.md` | Favorable transporter hit; drives cordycepin verdict | PMID and numbers cited; primary not included | Plausible but primary-source verification unresolved |
| Cordycepin URAT1 mechanism is expression-level, not direct binding | `literature_claims.json`, `summary.md` | Achievability class “lit-evidence-only-no-IC50” | Artifact states no IC50 | Clean limitation |
| Eurycomanone×URAT1 favorable | `literature_claims.json` v2 reopened row | Favorable transporter hit tier 2; drives eurycomanone verdict | Evidence is *Eurycoma* extract/quassinoids, not pure eurycomanone; specific IC50 behind paywall | Direction plausible; compound identity/magnitude not closed |
| Eurycomanone×ABCG2 favorable | `literature_claims.json` | Favorable transporter hit tier 3; drives eurycomanone verdict | Animal kidney protein expression from extract; fold changes behind paywall | Direction plausible; renal/gut/Q141K extrapolation unresolved |
| Eurycomanone×OAT1 favorable-ish | `literature_claims.json`, `results.json` | Tier 1, not counted as favorable hit; matrix displays ✓ Mech | Direction explicitly extrapolated | Not load-bearing; display should be softened |
| Eurycomanol/PRPS suppression | `literature_claims.json`, `wiki-archive.md`, PRPS page | Not modeled in `analyze.py`; used in prose rationale | PMID cited; primary details not in artifact | Important new connection; mechanism wording needs verification |
| 2021 Physta RCT SUA ↓7–11%, n=105 | `wiki-archive.md`, `summary.md`, `androgen-natural-modulation.md` | Not a structured claim used by code | Product/trial summary cited; primary publication paywalled/unavailable; no PMID/DOI in artifact | Action required: do not present as primary-verified clinical evidence |
| Icariin×XO negative screen | `literature_claims.json`, `chembl_bioactivity.json` | Classifier identifies `xo-negative-screen`; display ambiguous | PMID cited; primary not included | Qualitatively OK; evidence label/display bug |
| Icariin/echninacoside mechanism unclear | `results.json` | Verdict from no transporter data + XO no-data/negative-screen | English-only search; CNKI/WanFang not accessed | Clean with stated limits |
| `model_parameters` Vd/BW/lumen volume | `concentration_estimates.json` | Not used by code | Documentation only | Action required if README says computation derives concentrations |
| H-AN-02 “partially falsified” | `results.json`, `summary.md` | Computed by `is_favorable()` over verdict strings | Depends on eurycomanone-family favorable verdict | Qualitative conclusion plausible; uniqueness claim should be propagated |
| `outputs/summary.md` regenerates identically | README, `analyze.py`, committed output | Contract claim | Source/output link path mismatch observed | Action required: rerun/reconcile |
| Reproduction command | README | User instruction | Path wrong from repo root | Action required |

## Affected wiki pages
- `wiki/t-axis-adjuvant-urate-mapping-computational.md` — **change required** — live stub still asks about four targets despite v2 adding XO; archive link/path framing should be checked.
- `wiki/etc/experiments/comp-015-t-axis-adjuvant-urate-mapping/wiki-archive.md` — **change required** — archived “Question” still says four targets; several clinical/action claims need extract-vs-pure and primary-source qualifiers.
- `wiki/computational-experiments.md` — **change required** — broadly consistent but should qualify 2021 RCT provenance and eurycomanone-vs-extract/eurycomanol substitution.
- `wiki/androgen-natural-modulation.md` — **change required** — §1.7/§1.9 largely reconciled, but §5.3 and §10 H-AN-02 still preserve “cordyceps uniquely/most gout-favorable” framing inconsistent with comp-015 v2.
- `wiki/validation-experiments.md` — **change required** — if comp-015’s head-to-head wet-lab reprioritization is accepted, register the proposed cordyceps vs tongkat vs combo vs placebo experiment or explicitly decline it.
- `wiki/personal-genome-protocol.md` — **change required** — genotype-stratified adjuvant table should be labeled as mechanistic extrapolation; Q141K/eurycomanone “directly addresses” language exceeds comp-015.
- `wiki/genotype-informed-supplement-workflow.md` — **change required** — URAT1/compound preference should not be attributed as a direct comp-015 result; comp-015 did not perform genotype stratification.
- `wiki/gout-action-guide.md` — **change required** — application-surface supplement recommendations based on comp-015 need Phase 0 qualifiers and the unresolved primary-source / extract-vs-pure caveats.
- `wiki/prps-purine-biosynthesis-chokepoint.md` — **change required** — direct PRPS binding/catalytic inhibition wording appears stronger than comp-015’s “decreased PRPS expression / purine-synthesis suppression” support.
- `wiki/medicinal-mushroom-complement-track.md` — **not inspected; likely check required** — cited as cordycepin prior; inspect for “unique/most gout-favorable” claims after H-AN-02 partial falsification.
- `wiki/supplements-stack.md` — **not inspected; likely check required** — user-facing tongkat/cordyceps entries may need the same provenance and Phase 0 qualifiers.

## New connections or implications
- **PRPS is a genuine off-panel chokepoint candidate, but the mechanism needs careful wording.** The useful new connection is not “eurycomanone is an XO inhibitor”; it is “some *Eurycoma* quassinoid evidence points upstream of XO to purine synthesis / PRPS.” This is distinct from XO and transporter handling, and it should be promoted only with primary-source-accurate wording.
- **The artifact exposes a search-recall lesson.** v1’s “cordycepin uniqueness” appears partly due to missed *Eurycoma* hyperuricemia literature. Future “unique” claims need explicit recall-quality controls: multiple query formulations, species/extract names, active metabolite names, and multilingual search where relevant.
- **The most decision-relevant follow-up is not more static target mapping; it is exposure-anchored head-to-head testing.** Cordycepin URAT1 expression evidence and *Eurycoma* multi-target evidence are mechanistically different and not potency-matched. A head-to-head with SUA, FEUA, transporter markers, and active-compound quantification would resolve more than another in silico verdict pass.
- **Genotype stratification is promising but currently extrapolative.** The Q141K/URAT1/SLC2A9 tables in downstream pages are a reasonable hypothesis surface, not a result of comp-015.

## Required actions
1. **Reconcile reproducibility artifacts.** Owner: comp-015 artifact maintainer. Verification: `python3 analyze.py` from the correct repo path regenerates `outputs/results.json` and `outputs/summary.md` byte-identically, including corrected relative links; README reproduction command points to `wiki/etc/experiments/...`.
2. **Fix stale target-count wording.** Owner: comp-015 page maintainer. Verification: README, live interpretive stub, and archive all consistently say five targets / 4×5 matrix and do not retain the old four-target question.
3. **Separate pure eurycomanone from tongkat extract/quassinoid-family evidence.** Owner: comp-015 maintainer plus downstream page owners. Verification: verdict labels and tables state whether evidence is for pure eurycomanone, eurycomanol, isolated quassinoids, or standardized *Eurycoma* extract.
4. **Add or downgrade the 2021 Physta SUA RCT claim.** Owner: androgen/tongkat evidence maintainer. Verification: add structured source with PMID/DOI/full citation and primary-access status, or downgrade wording to “secondary/product-summary reported” and remove it as clinical load-bearing proof.
5. **Clarify concentration-model implementation.** Owner: comp-015 code maintainer. Verification: either implement concentration calculations from dose/F/MW/Vd/lumen parameters with sensitivity ranges, or state explicitly that `concentration_estimates.json` contains precomputed estimates and the script only consumes them.
6. **Add translatability/sensitivity closure for animal/extract evidence.** Owner: comp-015 maintainer. Verification: include HED/exposure comparison, active-compound content bounds, and separate systemic vs gut/kidney exposure assumptions for cordycepin and *Eurycoma* rows.
7. **Correct PRPS mechanism wording.** Owner: `prps-purine-biosynthesis-chokepoint.md` maintainer. Verification: primary paper wording checked; page distinguishes decreased PRPS expression, purine-synthesis suppression, enzyme activity inhibition, and direct binding if each is actually supported.
8. **Propagate H-AN-02 partial falsification cleanly.** Owner: androgen-natural-modulation maintainer. Verification: §5.3 and §10 no longer call cordyceps uniquely/most gout-favorable without noting eurycomanone/tongkat-family reversal.
9. **Register or explicitly reject the proposed head-to-head validation experiment.** Owner: validation-experiments maintainer. Verification: `validation-experiments.md` contains a proposed cordyceps/tongkat/combo/placebo protocol with Phase 0 caveats, or a note explaining why it is not being queued.
10. **Qualify downstream application/genotype surfaces.** Owner: `gout-action-guide.md`, `personal-genome-protocol.md`, and `genotype-informed-supplement-workflow.md` maintainers. Verification: all genotype- or user-action claims derived from comp-015 are labeled mechanistic extrapolation / Phase 0 and not clinical advice.

## Review limits
- I did not execute `analyze.py`; review is by inspection only.
- Primary papers were not independently retrieved. PMIDs and trial claims are assessed as artifact-provided provenance, not primary-source verification.
- Repository fixed-string search failed because `rg` is unavailable in the tool environment. I used the supplied explicit pages plus manual directory/file inspection for omitted high-impact pages.
- `validation-experiments.md` was only inspected in the initial large chunk/dashboard; a deeper full-file search was not possible with the broken grep tool.
- `medicinal-mushroom-complement-track.md` and `supplements-stack.md` were not inspected; they remain likely propagation surfaces requiring manual follow-up.
- ChEMBL/PubChem API access was not tested independently.

---
## ✓ Actioned 2026-07-14
**Disposition: caveat/downgrade** (relabel/hygiene tier). Added a ⚠️ caveat banner to the interpretive page (or artifact README for comp-015) capturing the audit's headline finding — the qualitative direction holds, but the quantitative/verdict framing overstated what the model resolves. Deeper artifact fixes (reproducibility defects, provenance-tier labeling, code/summary mismatches, any recompute) remain in the Required-actions above as residuals for a focused follow-up.
