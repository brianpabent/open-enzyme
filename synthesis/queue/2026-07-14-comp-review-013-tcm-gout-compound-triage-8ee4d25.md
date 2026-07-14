---
type: comp-review
sweep_date: 2026-07-14
sweep_sha: 8ee4d25
comp: comp-013
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-013

Canonical review log: [`logs/comp-reviews/2026-07-14-comp-013-8ee4d25.md`](../../logs/comp-reviews/2026-07-14-comp-013-8ee4d25.md)

ACTION_REQUIRED: yes

# Independent comp review — comp-013

## Bottom-line verdict

**Quantitative verdict invalid; action required.** The artifact is useful as a curated evidence inventory, but the implemented triage does **not** validly support the stated “4 GUT-LUMINAL VIABLE + 1 MODERATE” verdict. Two code-level logic errors are load-bearing:

1. **Rhein’s “MODERATE / VIABLE-WITH-DOSE-CAVEAT” verdict is derived from off-target plasma occupancy**, not gout-target occupancy. The code treats moderate AChE/FTO off-target occupancy as if it supported systemic gout viability.
2. **Luteolin’s gut ABCG2 occupancy is treated as favorable “gut-luminal viability” despite ABCG2 inhibition being bad for gout physiology** in the target definition itself. The artifact discusses this paradox narratively, but the code lacks target polarity and cannot adjudicate net effect.

The committed outputs are also not fully reproducible from the committed script: `scripts/analyze.py` would write a different interpretive-link path than the committed `outputs/summary.md`.

## Implementation and constraint closure

I traced the load-bearing path from JSON inputs → `scripts/analyze.py` → `outputs/triage.json`, `outputs/summary.md`, and CSV.

**Implemented model:**
- Gut concentration = `dose_mg × (1 − BA) / 0.25 L`, capped by `intestinal_solubility_mg_L`.
- Plasma Cmax = `dose_mg × BA / (Vd_L_kg × body_weight_kg)`, with Vd = 1 L/kg and BW = 70 kg.
- Occupancy = `conc / IC50`, Hill n=1.
- ABCG2 is assigned gut concentration; all other targets use plasma Cmax.
- Composite score = normalized potency × selectivity × gut-enrichment.

**Major implementation problems:**
- `assign_verdict(..., on_target_data)` receives `on_target_data` but does not use it.
- `relevant_occ` is computed but unused.
- `has_high_gut`, `has_high_plasma`, and `has_moderate_plasma` include **off-targets** and do not filter for gout-relevant targets or target polarity.
- For rhein, `has_moderate_plasma` is true because AChE and FTO off-target occupancies are moderate. This drives the “MODERATE / VIABLE-WITH-DOSE-CAVEAT” verdict despite no implemented URAT1/XO/ABCG2/NLRP3 potency.
- For luteolin, high gut ABCG2 inhibition is treated as favorable, although `targets.json` explicitly says ABCG2 inhibition raises serum urate and is bad for gout.
- `confidence` is inflated by any biochemical ChEMBL hit, including off-target hits. Thus emodin and berberine receive HIGH confidence from off-target biochemical data plus animal evidence, despite lacking direct biochemical gout-target IC50.
- Ranking after luteolin is essentially arbitrary: all remaining compounds have composite score 0.0000, so ranks 2–9 are stable-sort/input-order artifacts, not quantitative separation.
- The selectivity ratio is inconsistently described. Code computes `off_target_ic50 / on_target_ic50`, which is sensible; parts of README/summary label or define it as “on/off,” which is inverted.
- `plasma_volume_L`, `small_intestine_pH`, and location notes are stored but not used. These appear documentation-only, not necessarily bugs, but `plasma_volume_L` creates confusion because the text sometimes reports plasma Cmax values inconsistent with the Vd model.

**Constraint closure gaps:**
- **Reaction/transport polarity:** Target direction is not modeled. XO inhibition is favorable, URAT1 inhibition/downregulation may be favorable, ABCG2 inhibition is unfavorable, but the code treats all high occupancy as similarly meaningful.
- **Substrates/cosubstrates/products:** XO substrate competition, xanthine concentration, oxygen, and H₂O₂ coproducts are not modeled. URAT1 exchange physiology and ABCG2 urate flux capacity are not modeled.
- **Physiological operating regime:** IC50 comparisons do not include free fraction, protein binding, metabolite identity, active conjugates, transporter expression, substrate-specific IC50, or assay-format differences.
- **Mass balance/time:** No urate-production or urate-excretion mass balance, no gut residence time, no repeat dosing, no degradation/metabolism kinetics, no replenishment.
- **Localization/access:** Gut vs plasma split is coarse. Renal proximal tubule exposure is approximated by plasma Cmax, but filtrate/tubular concentrations are not modeled. Intestinal epithelial ABCG2 access is approximated by bulk luminal concentration.
- **Safety/off-targets:** Some ChEMBL off-targets are listed, but the off-target panel is non-systematic. The model can even convert off-target occupancy into positive viability.
- **Sensitivity:** No sensitivity analysis over dominant uncertainties: BA, solubility, dose, Vd, intestinal segment volume, free luminal fraction, metabolism, animal-to-human translation, or unresolved IC50s.

## Summary-fidelity audit

**README / wiki archive / output summary mismatch:**
- The top-line count is consistent across README, summary, and index, but the count is not supported by the implementation logic.
- README and wiki archive contain stale or conflicting luteolin plasma numbers:
  - Output: luteolin plasma Cmax = **0.25 µM / 249.5 nM**, XO ratio = **0.45×**.
  - README/wiki archive also state ~**24 nM** and ratio **0.04×** in one place.
  - Wiki archive additionally claims **8.9 µM plasma Cmax “per outputs/triage.json”**, which is not in `triage.json`.
- ChEMBL coverage is misstated:
  - Inputs show **4 compounds with no ChEMBL ID**: astilbin, aucubin, cylindrin, atractylenolide I.
  - The wiki archive and index say **5 of 9 have no ChEMBL data**, while simultaneously listing five compounds with ChEMBL data: rhein, emodin, berberine, chlorogenic acid, luteolin.
  - The correct summary should distinguish “4 no ChEMBL entry” from “only 1 compound has a curated biochemical gout-relevant IC50.”
- The summary’s rank table implies a meaningful rank ordering, but ranks 2–9 are all composite 0 and should be treated as unordered evidence categories.
- The output summary says “Best on-target IC50: N/A (ChEMBL gap)” for rhein while still assigning a positive “MODERATE” verdict. That is internally inconsistent.
- The output summary method note defines selectivity as “best gout-relevant on-target IC50 / best non-gout off-target IC50,” but code uses the inverse.
- The committed `outputs/summary.md` link differs from the link that current `scripts/analyze.py` would write, so committed outputs are not a faithful product of the current script.

**Wiki/index propagation:**
- `wiki/computational-experiments.md` repeats the “4 viable + 1 caveat” and “5 of 9 no ChEMBL data” claims. Both require correction or caveating.
- `wiki/tcm-gout-compound-triage-computational.md` includes a later addendum that correctly identifies seed-list/query-framing failures, but it does not explicitly invalidate the original comp-013 quantitative verdict logic.
- `wiki/tcm-modern-rigor-intersection.md` P2-2 repeats the same over-strong verdict and ChEMBL-count error.
- `wiki/hypotheses/H04-tcm-rigor-intersection.md` partly diagnoses query-framing problems, but still relies on the stale “5/9 no ChEMBL data” comp-013 framing.

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| 9 compounds evaluated | `inputs/compounds.json`; outputs | Iterated directly | Directly visible in artifact | Clean |
| Gut volume = 0.25 L | `inputs/gut_model.json` | Used in gut concentration | Named as comp-004 assumption; primary physiological basis not included | Usable assumption, not independently verified |
| Vd = 1 L/kg; BW = 70 kg | `inputs/gut_model.json` | Used for plasma Cmax | Generic assumption; no primary source in artifact | Major uncertainty; no sensitivity |
| `plasma_volume_L = 3.0` | `inputs/gut_model.json` | Not used | Documentation-only or stale | Needs clarification because text has conflicting plasma numbers |
| Doses, BA, solubility | `inputs/compounds.json` | Directly used | Many marked `[UNVERIFIED]`; sources mostly citation strings | Load-bearing unresolved inputs |
| Luteolin XO IC50 = 550 nM | `bioactivity_data.json`; outputs | Best on-target IC50; composite driver | Artifact asserts ChEMBL activity verification; primary ChEMBL not available in bundle | Accept as artifact-provenance claim, not independently verified |
| Luteolin ABCG2 IC50 = 8,900 nM | `bioactivity_data.json`; outputs | Gut occupancy = VERY_HIGH | Artifact asserts ChEMBL verification | Computed correctly, but polarity mishandled |
| ABCG2 inhibition is bad for gout | `inputs/targets.json`; luteolin notes | Not encoded in verdict logic | Mechanistically stated in artifact | Implementation violates this constraint |
| Luteolin plasma Cmax | `triage.json`, `summary.md`, README/wiki archive | Used for occupancy | Computed as 249.5 nM from code | README/wiki archive contain stale/incorrect numbers |
| Rhein no gout-target IC50 | `bioactivity_data.json`; output summary | `best_on_target_ic50_nM = null` | Artifact asserts ChEMBL gap; Yu URAT1 IC50 not extracted | Should prevent positive quantitative verdict |
| Rhein moderate verdict | `triage.json`; `summary.md` | Derived by code | Based on off-target AChE/FTO occupancy | Invalid |
| Emodin animal FEUA effect, XO excluded | `bioactivity_data.json`; summary | Animal-evidence override | Artifact asserts Paperclip verification; primary unavailable | Evidence inventory useful; quantitative viability not implemented |
| Berberine TDO 30 nM off-target | `bioactivity_data.json`; outputs | Off-target occupancy; confidence inflation | Artifact asserts ChEMBL verification | Useful safety/off-target flag; should not raise gout confidence |
| Astilbin animal URAT1 evidence | `bioactivity_data.json` | Animal-evidence override | Artifact asserts review-line verification; primary unavailable | Candidate evidence, not quantitative occupancy |
| Si Miao San meta-analysis SUA −90.62 µmol/L | `bioactivity_data.json`; outputs | Formula-level evidence only | Artifact asserts Paperclip line verification; primary unavailable | Should remain formula-level; no single-component attribution |
| Composite ranking | `analyze.py`; outputs | Sorts by composite | Deterministic code | Misleading after rank 1 because all others tie at 0 |
| Reproduction command | README | User command | Path omits `wiki/etc/` | Needs correction |
| Output generation fidelity | `scripts/analyze.py` vs `outputs/summary.md` | Claimed generated outputs | Link text differs | Re-run/recommit needed |

## Affected wiki pages

- `wiki/tcm-gout-compound-triage-computational.md` — **change required** — needs explicit correction that the original quantitative verdict/ranking is invalid as implemented; addendum fixes seed-list misses but not the code logic.
- `wiki/computational-experiments.md` — **change required** — current comp-013 index repeats “4 viable + 1 caveat” and “5 of 9 no ChEMBL data”; both need correction/caveating.
- `wiki/tcm-modern-rigor-intersection.md` — **change required** — P2-2 status repeats the over-strong comp-013 verdict and ChEMBL-count error; should say comp-013 produced a useful evidence inventory but needs rerun with polarity/on-target filtering.
- `wiki/hypotheses/H04-tcm-rigor-intersection.md` — **change required** — partially updated for query-framing, but still repeats stale comp-013 coverage framing; should distinguish seed-list failure from database coverage and correct the 4-vs-5 count.
- `wiki/abcg2-modulators.md` — **partly consistent / possible change required** — already treats ABCG2 inhibition as a risk. Any luteolin or TCM-compound entry should not inherit comp-013’s “gut-luminal viable” label without the ABCG2-inhibition caveat.
- `wiki/androgen-urate-axis.md` — **mostly consistent with caveat** — its cross-track URAT1 redundancy note cites astilbin as animal-model URAT1 expression evidence. That remains usable only as animal evidence, not as quantified human-relevant viability.
- `wiki/medicinal-mushroom-compound-mapping-computational.md` — **change required if using comp-013 as database-gap precedent** — the page generalizes the “ChEMBL coverage gap” pattern; should reference the later query-framing correction and avoid the erroneous “5/9 no ChEMBL” number.
- `wiki/validation-experiments.md` — **no direct comp-013 mismatch found in inspected portion** — however, if any TCM-compound wet-lab prioritization uses comp-013 rank/order, it should be reviewed.

## New connections or implications

- **Target polarity must become a reusable field.** This is not just a comp-013 bug. Any future ChEMBL/occupancy screen involving transporters needs explicit `desired_direction` or `effect_polarity`: inhibition favorable, inhibition harmful, activation favorable, expression up/down, unknown.
- **Animal-evidence overrides need a separate evidence tier from quantitative IC50 occupancy.** Astilbin, emodin, and berberine may be reasonable “animal-evidence candidates,” but the artifact should not present them as occupying the same quantitative framework as luteolin’s XO IC50.
- **Off-target occupancy should demote, not promote, viability.** The rhein bug shows why off-targets must be excluded from positive target-occupancy checks and used in safety/selectivity only.
- **The later 2026-05-19 addendum partly supersedes the original seed list.** The strongest TCM mechanism candidates may not be the original 9 compounds; mangiferin, Coix seed oil mechanisms, Plantago marker correction, acacetin, and kaempferol materially change the candidate landscape. That supports a comp-013 v2 rather than patching the old ranking.
- **“ChEMBL gap” was over-attributed.** The corpus later recognizes that formula/marker seed-list construction, not just ChEMBL coverage, caused misses. The artifact should be aligned with that newer methodological diagnosis.

## Required actions

1. **Fix `assign_verdict` logic in `scripts/analyze.py`.** Verification criterion: positive viability checks filter for gout-relevant targets only, exclude off-target occupancy, and require target polarity to be favorable.
2. **Add target-effect polarity to `targets.json` / bioactivity records.** Verification criterion: ABCG2 inhibition is scored as gout-unfavorable; XO inhibition and URAT1 inhibition/downregulation are scored separately and explicitly.
3. **Recompute outputs and recommit `triage.json`, `summary.md`, and CSV.** Verification criterion: committed outputs are byte-consistent with the current script after rerun, except for expected timestamp-free deterministic formatting.
4. **Correct stale numeric/text claims.** Verification criterion: README, wiki archive, output summary, and index agree on luteolin plasma Cmax/ratios and on ChEMBL coverage counts.
5. **Reframe rhein.** Verification criterion: until a verified URAT1/XO/ABCG2/NLRP3 IC50 or robust gout-specific in vivo dose-response is extracted, rhein is not labeled “viable-with-dose-caveat” based on off-target occupancy.
6. **Reframe ranks 2–9 as unordered zero-composite candidates.** Verification criterion: no page implies that astilbin rank 2 vs berberine rank 6 is a quantitative outcome of the composite score.
7. **Correct reproducibility paths.** Verification criterion: README command uses `wiki/etc/experiments/comp-013-tcm-gout-compound-triage`; output summary interpretive links resolve correctly from `outputs/summary.md`.
8. **Propagate corrections to affected wiki pages.** Verification criterion: `computational-experiments.md`, `tcm-modern-rigor-intersection.md`, `tcm-gout-compound-triage-computational.md`, and H04 no longer carry the invalid quantitative verdict or the wrong ChEMBL-count wording.
9. **Primary-source verification remains needed for all artifact-only citation claims.** Verification criterion: either include line-anchored source excerpts/metadata in the artifact or explicitly label claims as “artifact asserts verification; primary not bundled.”

## Review limits

- I did not execute the code.
- The repository fixed-string search tool failed because `rg` was unavailable, so affected-page discovery was limited to provided pages plus targeted file reads.
- I read `wiki/tcm-modern-rigor-intersection.md` and the beginning of `wiki/validation-experiments.md`; I did not fully inspect every omitted page such as `koji-endgame-strain.md`, `complement-c5a-gout.md`, or `cfh-mechanism-dissociation-cp0-candidates-computational.md`.
- I could not independently verify ChEMBL, PubMed, Paperclip, or primary-literature line claims; I treated them as artifact provenance assertions, not primary-source verification.
- The artifact’s qualitative evidence inventory may still be valuable after correction; this review invalidates the quantitative verdict/ranking and summary contract as currently implemented.
