---
type: comp-review
sweep_date: 2026-07-14
sweep_sha: 8ee4d25
comp: comp-036
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-036

Canonical review log: [`logs/comp-reviews/2026-07-14-comp-036-8ee4d25.md`](../../logs/comp-reviews/2026-07-14-comp-036-8ee4d25.md)

ACTION_REQUIRED: yes

# Independent comp review — comp-036

## Bottom-line verdict

**Action required.** The raw code plausibly implements a deterministic Monte Carlo **plasma IL-1Ra concentration → IL-1R1 occupancy** screen and supports a weak YELLOW-style conclusion that repeat dosing improves on comp-033 but does not clear the high-confidence bar. However, the artifact-summary contract is materially broken: output fields contradict the overall verdict, the “current” clinical handoff is stale/incorrect, the recommended BID regimen is misreported in multiple places, several input claims are stored but unused, and the clinical-efficacy / prednisone-displacement interpretation is stronger than the implemented model can establish.

The quantitative output should be treated as a **Phase 0 plasma-occupancy prior**, not as a validated clinical-efficacy, joint-synovium, or side-effect-tradeoff model.

## Implementation and constraint closure

I traced the main load-bearing path through `analyze.py`:

- Inherited comp-033 priors are sampled: mRNA dose, translation efficiency, lung delivery fraction, systemic bioavailability, expression duration, IL-1Ra clearance, and Vd.
- A zero-order protein-input / first-order elimination single-dose model generates plasma IL-1Ra.
- Multi-dose profiles are linear superpositions of single-dose profiles.
- Plasma IL-1Ra is converted to nM using MW 17.3 kDa and mapped to receptor occupancy as `C / (C + Kd)`.
- Sustained occupancy is counted on a 0.5 h grid over the inclusive 0–72 h flare window.
- GREEN is implemented as median sustained-80%-window fraction ≥0.95 and p25 sustained-window fraction ≥0.50.
- YELLOW is implemented as median sustained-80%-window fraction ≥0.50.

Key closure findings:

1. **The code does not use the competitive-antagonism excess factor.**  
   `competitive_antagonism_excess_factor_prior` is sampled and included in sensitivity tracking, but never affects occupancy, biological inhibition, verdict, or any supplementary output. This contradicts `model_parameters.json`, `il1ra_receptor_binding.json`, and `provenance.md`, which say the 10–100× excess factor is used or is the operative clinical-efficacy constraint.

2. **The code computes raw IL-1Ra receptor occupancy, not functional IL-1β signaling inhibition.**  
   No IL-1β concentration, IL-1α concentration, agonist occupancy, receptor reserve, IL-1RAcP recruitment, local synovial cytokine burden, or competitive displacement dynamics are modeled. Therefore “clinically meaningful” and “prednisone-displacing” claims are extrapolations from a receptor-occupancy proxy, not outputs of the implementation.

3. **Plasma concentration is silently substituted for target-site concentration.**  
   The model assumes plasma free IL-1Ra equilibrates to the relevant IL-1R1-bearing cells and inflamed synovium. There is no synovial-fluid partitioning, vascular leak, inflamed-joint residence time, receptor turnover, macrophage/synoviocyte compartment, or local cytokine concentration model.

4. **The dominant safety and handling constraints are qualitative only.**  
   LNP innate immune activation, anti-PEG accumulation, pulmonary irritation, repeated nebulization tolerance, mucosal peaks, and long-term repeated exposure are not modeled. They are discussed in text and comparator tables but not implemented as constraints or penalties.

5. **Dose-count scans include many post-window doses that cannot affect the 0–72 h endpoint.**  
   QD doses after 72 h and BID doses after 72 h are irrelevant to the primary window. This is not fatal, but it makes “QD ×14” / “BID ×28” language misleading for a 0–72 h endpoint.

6. **Smallest YELLOW regimen is not reported consistently.**  
   The committed JSON says `BID_smallest_N_YELLOW = 6 doses = 3 days`. BID ×4 has median sustained-window fraction 0.49655 and `passes_YELLOW_gate: false`. README and interpretive pages repeatedly describe “BID 4+ doses” as reaching the YELLOW bar, apparently by rounding 0.49655 to ~0.50.

7. **Sensitivity is mislabeled as “recommended regimen.”**  
   `sensitivity_at_recommended_regimen` is actually computed at QD ×14 because no QD regimen passes, even though a BID YELLOW regimen exists. This is disclosed in the label but contradicts the JSON key and the clinical emphasis on BID as the load-bearing regimen.

8. **Monte Carlo dose-count comparisons are unpaired.**  
   Each dose-count cell samples an independent Monte Carlo population. Around a sharp 0.50 YELLOW threshold, this produces non-monotonic behavior and makes the exact “smallest N” fragile. A rerun using common random numbers across dose counts within each regimen would make the regimen escalation boundary more reliable.

9. **Reproduction command path is wrong relative to the provided repository layout.**  
   README says:
   ```bash
   cd experiments/comp-036-repeat-dose-inhaled-mrna-il1ra-pkpd
   python3 analyze.py
   ```
   The tracked path is:
   ```bash
   cd wiki/etc/experiments/comp-036-repeat-dose-inhaled-mrna-il1ra-pkpd
   python3 analyze.py
   ```

Constraint closure by category:

- **Substrates/products:** mRNA dose and translated IL-1Ra mass are modeled. Cellular translation resources, LNP payload release, protein secretion, IL-1β/IL-1α agonist competition, and receptor accessory protein effects are not modeled.
- **Operating constants:** Kd is modeled as log-uniform 0.1–10 nM. The claimed 10–100× excess factor is not used. IL-1β concentrations and receptor density are not used.
- **Finite mass balance/time:** mRNA dose, delivery, systemic bioavailability, expression duration, clearance, and Vd are represented. Repeated-dose LNP tolerance or expression attenuation is not represented.
- **Localization/access:** pulmonary delivery → systemic plasma is represented via a scalar bioavailability prior. Joint/synovial access is assumed, not modeled.
- **Coproducts/off-targets/safety:** LNP route effects, pulmonary irritation, anti-PEG, innate immunity, and infection-risk comparisons are qualitative only.
- **Sensitivity:** Kd and translation efficiency dominate, but sensitivity is reported at QD ×14 rather than the BID YELLOW regimen that drives the conclusion.

## Summary-fidelity audit

Major mismatches:

- `outputs/dose_pkpd_prediction.json` overall verdict is **YELLOW**, but `side_effect_comparator_table.per_flare_burden.inhaled_mrna_repeat_dose_recommended.regimen` says **“RED — no practical regimen identified”**. This is an implementation bug caused by checking only `qd_green`, not the overall verdict or BID YELLOW result.

- `outputs/summary.md` says the per-flare inhaled mRNA regimen is **“not achieved at clinically-practical regimen”**, while the verdict text says **YELLOW because ≥50%-of-window 80%-occupancy is achieved at median**. The committed JSON identifies BID ×6 as the smallest YELLOW regimen.

- `outputs/summary.md` clinical handoff says **“If GREEN (current)”** even though the verdict is YELLOW. This stale branch appears in the generated summary and appended wiki archive.

- The YELLOW clinical handoff says translation efficiency is “the dominant uncertainty,” but the actual sensitivity table and README identify **Kd_nM as #1** and translation efficiency as #2.

- README and interpretive wiki page say **BID 4+ doses** reach ~50% / YELLOW. The JSON says BID ×4 median is 0.49655 and `passes_YELLOW_gate: false`; BID ×6 is the smallest YELLOW regimen.

- The interpretive and index pages state receptor occupancy is “the clinically-relevant metric.” That is directionally plausible for an IL-1R1 antagonist, but the implementation does not model agonist concentration, synovial exposure, or functional inhibition. Wording should be softened to “a more mechanistically relevant proxy than Cmax-equivalence.”

- Provenance language overstates direct verification. The artifact contains citation strings and claims of PubMed metadata/abstract retrieval; it does not include primary full-text extracts or direct numerical Kd verification. The 0.1–10 nM prior is plausible but not directly primary-source-verified within the artifact.

Pages already broadly consistent:

- `wiki/computational-experiments.md` correctly marks comp-036 YELLOW and does not claim GREEN.
- `wiki/validation-experiments.md` does not duplicate a comp-036-specific wet-lab protocol and is broadly consistent with chassis-pending validation being tracked elsewhere.
- `wiki/nlrp3-exploit-map.md` only lists inhaled mRNA-IL-1RA as engineering-pending at CP5a; that remains consistent.

Pages requiring changes are listed below.

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| mRNA dose 4–24 mg per administration | `inputs/single_dose_pk_inherited.json`; README | Sampled log-uniform and directly drives IL-1Ra production | Inherited from comp-033; named anchors only | Plausible inherited prior; not independently verified here |
| Translation efficiency 1,000–50,000 ng protein/µg mRNA | `inputs/single_dose_pk_inherited.json`; README | Sampled log-uniform; #2 sensitivity driver in output | Inherited; source strings only | Load-bearing and unresolved; direct inhaled human/NHP measurement needed |
| Lung delivery fraction 0.10–0.40 | `inputs/single_dose_pk_inherited.json` | Sampled uniform | Inherited; source strings only | Plausible broad prior; not directly verified here |
| Alveolar→systemic bioavailability 0.10–0.50 | `inputs/single_dose_pk_inherited.json` | Sampled uniform | Inherited; source strings only | Major hidden substitution for pulmonary-to-plasma access; unresolved |
| Expression duration 24–96 h | `inputs/single_dose_pk_inherited.json` | Sampled uniform | Inherited; broad modified-mRNA prior | Used; direct payload/route-specific verification absent |
| IL-1Ra clearance 0.10–0.25 /h | `inputs/single_dose_pk_inherited.json` | Sampled uniform | Inherited from anakinra PK | Used; reasonable for plasma IL-1Ra but not independently rechecked |
| Vd 12–25 L | `inputs/single_dose_pk_inherited.json` | Sampled uniform | Inherited from anakinra PK | Used; reasonable but inherited |
| IL-1Ra MW 17.3 kDa | `inputs/il1ra_receptor_binding.json`; `receptor_occupancy()` default | Used for ng/mL→nM conversion | Inherited from UniProt comp-033 | Arithmetic in code is correct |
| Kd 0.1–10 nM, central 1 nM | `inputs/model_parameters.json`; `inputs/il1ra_receptor_binding.json`; README | Sampled log-uniform; #1 sensitivity driver | Citation strings and qualitative “nM regime” support; direct numerical primary verification not present | Load-bearing and unresolved; needs primary/full-text or new SPR verification |
| 80% occupancy threshold = 4×Kd ≈ 72.6 ng/mL median | `outputs/dose_pkpd_prediction.json`; README | Derived in Phase 5 | Derived correctly from Kd prior and MW | Arithmetic correct; clinical threshold not independently validated |
| Competitive-antagonism excess factor 10–100× | `inputs/model_parameters.json`; `inputs/il1ra_receptor_binding.json`; provenance | Sampled and tracked only; no effect on outputs | Arend quote claimed; artifact does not include primary text beyond provenance | Stored-but-unused; output claims about functional inhibition are unsupported |
| Receptor density 50–5000 per cell | `inputs/il1ra_receptor_binding.json` | Not used | Context only | Correctly unused for simple occupancy, but cannot support functional inhibition claims |
| Flare window 0–72 h | `inputs/model_parameters.json`; `dosing_regimens.json` | Used as assessment window | Anchored to gout-flare clinical framing/Saag endpoint | Used; reasonable but not a full clinical outcome model |
| GREEN gate median ≥0.95 window above 80% and p25 ≥0.50 | README; implemented in `passes_GREEN_gate` | Direct verdict criterion | Internal decision rule | Implemented, but differs from some input comments saying p25 occupancy ≥60% |
| YELLOW gate median ≥0.50 window above 80% | README; `passes_YELLOW_gate` | Direct verdict criterion | Internal decision rule | Implemented; exact smallest N fragile due unpaired MC and rounding |
| BID smallest YELLOW = 6 doses / 3 days | `outputs/dose_pkpd_prediction.json` | Derived from scan | Internal computation | Supported by committed JSON; README/wiki saying 4+ doses need correction |
| Anakinra Cmax 1500 ng/mL, Cmin 50 ng/mL | `inputs/il1ra_receptor_binding.json`; comparator trajectory | Used in threshold comparison and trajectory only | Inherited from comp-033/Kineret sources | Used as simplified comparator; no full PK model |
| Anakinra mean occupancy ~85–90% | README; interpretive page; `il1ra_receptor_binding.json` | Not calculated in verdict; used for framing | Derived from simplified Cmax/Cmin and Kd=1 nM | Directionally plausible; not a clinical efficacy derivation |
| Side-effect and cost comparator table | `inputs/clinical_comparators.json`; output summary | Copied into outputs; not part of PK/PD model | Citation strings and qualitative summaries | Not model-derived; some corpus conflicts with gout-action-guide injection-site framing |
| “Modality viable / prednisone displacement plausibly yes” | README; interpretive page; chassis-pending; open vision; gout-action-guide | Not implemented | Mechanistic extrapolation only | Overstated relative to artifact |

## Affected wiki pages

- `wiki/repeat-dose-inhaled-mrna-il1ra-pkpd-computational.md` — **change required** — Correct BID ×4 vs ×6, soften “clinically-relevant metric” to “mechanistically relevant proxy,” and distinguish raw receptor occupancy from functional IL-1β inhibition.

- `wiki/computational-experiments.md` — **change required** — Entry is broadly consistent but should avoid “modality viable” without caveat; if listing key findings, it should note BID smallest YELLOW is 6 doses in committed output and that functional inhibition was not modeled.

- `wiki/chassis-pending-interventions.md` — **change required** — The comp-036 handoff repeats BID ×4–28 as YELLOW and contains strong prednisone-displacement / partner-conversation claims. These should be downgraded to Phase 0 extrapolation unless a clinical-response model or wet-lab PD data is added.

- `wiki/gout-action-guide.md` — **change required** — The future inhaled mRNA row is an application surface and uses comp-036 numbers in a patient-facing comparator table. It should not imply clinical meaningfulness from raw receptor occupancy, and the BID regimen should be corrected to the committed output or deferred until rerun.

- `wiki/etc/open-enzyme-vision.md` — **change required** — The temporal-stack section imports the operator-relevant prednisone-displacement framing. It should state that comp-036 supports only a plasma-occupancy prior, not clinical shortening/dampening.

- `wiki/inhaled-mrna-il1ra-pulse-computational.md` — **already mostly consistent / minor change recommended** — It says comp-033 does not close repeat dosing and links forward. Optional update could summarize comp-036 as a YELLOW raw-occupancy follow-up with unresolved clinical translation.

- `wiki/delivery-route-matrix.md` — **already consistent** — It treats pulmonary mRNA as an exploration vector and is comparatively cautious.

- `wiki/validation-experiments.md` — **already consistent** — It explicitly says chassis-pending interventions have separate validation paths and does not over-propagate comp-036.

- `wiki/nlrp3-exploit-map.md` — **already consistent** — It lists inhaled mRNA-IL-1RA as engineering-pending at CP5a without relying on comp-036’s specific regimen numbers.

- `wiki/gout-clinical-pipeline.md` — **already consistent for comp-036 purposes** — It frames anakinra/canakinumab clinical context but does not rely on the comp-036 artifact’s dose-scan details.

## New connections or implications

- The biggest mechanistic gap is not just translation efficiency; it is the **bridge from plasma IL-1Ra occupancy to inflamed-joint functional IL-1β blockade**. This links comp-036 to the intra-articular mRNA-IL-1Ra route mentioned in comp-033/036 and `delivery-route-matrix.md`: local joint delivery would eliminate the plasma→synovium substitution and should be evaluated with a separate local concentration/residence model.

- The unused competitive-antagonism excess factor is not harmless documentation drift. The corpus repeatedly says IL-1Ra may require high molar excess for biological inhibition; comp-036’s code does not implement that mechanism. A follow-up could explicitly model IL-1β concentration ranges and compute fractional IL-1β signaling suppression, not just IL-1Ra receptor occupancy.

- Exact regimen selection is threshold-sensitive. Because BID ×4 sits just below the YELLOW threshold in committed output, a paired-common-random-number rerun may materially change the “smallest practical regimen” even if the overall YELLOW verdict remains.

- The clinical comparator surfaces need a tier separation: **anakinra efficacy is clinical evidence; inhaled mRNA-IL-1Ra is Phase 0 exposure modeling**. Repeating them in one table without evidence-tier markers risks turning a computational prior into apparent clinical parity.

## Required actions

1. **Fix generated output-summary logic in `analyze.py`.**  
   Owner surface: comp-036 artifact.  
   Verification criterion: rerun produces `summary.md` and `dose_pkpd_prediction.json` with no “If GREEN (current)” text under a YELLOW verdict, no “RED — no practical regimen” for a YELLOW BID result, and a clear YELLOW regimen table.

2. **Correct BID regimen reporting across README, output summary, wiki archive, interpretive page, index, chassis-pending, open-vision, and gout-action-guide.**  
   Owner surface: comp-036 summary + affected wiki pages.  
   Verification criterion: all surfaces either state the committed output’s smallest YELLOW regimen as BID ×6 / 3 days or explicitly mark the exact threshold as pending paired rerun.

3. **Rerun or revise the regimen scan using paired common random numbers across dose counts.**  
   Owner surface: `analyze.py`.  
   Verification criterion: each regimen’s dose-count escalation is evaluated on the same sampled parameter set, yielding monotonic or explainably non-monotonic behavior and a stable smallest-N YELLOW boundary.

4. **Either implement or remove the competitive-antagonism excess-factor claims.**  
   Owner surface: `analyze.py`, `model_parameters.json`, `il1ra_receptor_binding.json`, provenance, README.  
   Verification criterion: either a functional inhibition calculation uses IL-1β/IL-1α and the 10–100× factor, or all text says the current model is raw IL-1Ra occupancy only and the excess factor is not used.

5. **Downgrade clinical-efficacy and prednisone-displacement wording.**  
   Owner surface: interpretive page, `chassis-pending-interventions.md`, `gout-action-guide.md`, `etc/open-enzyme-vision.md`.  
   Verification criterion: wording clearly states “plasma receptor-occupancy proxy; clinical benefit vs prednisone not established.”

6. **Repair provenance language.**  
   Owner surface: `inputs/provenance.md`, README.  
   Verification criterion: distinguish “citation/metadata/abstract checked” from “primary full-text numerical verification,” and mark the Kd prior as unresolved unless direct source excerpts or a new SPR measurement support it.

7. **Fix reproduction command path.**  
   Owner surface: README.  
   Verification criterion: command uses `wiki/etc/experiments/comp-036-repeat-dose-inhaled-mrna-il1ra-pkpd` or otherwise matches the actual tracked tree.

## Review limits

I did not execute `analyze.py`; this review is by inspection of committed code, inputs, outputs, and wiki surfaces. The repository `grep_repo` tool failed because `rg` was unavailable, so affected-page discovery relied on the supplied explicit pages plus manual reads of relevant omitted pages (`validation-experiments.md`, `inhaled-mrna-il1ra-pulse-computational.md`, `etc/open-enzyme-vision.md`, `nlrp3-exploit-map.md`, `gout-clinical-pipeline.md`). Primary papers were not independently retrieved; provenance verification is limited to citation strings and artifact claims.

---
## ✓ Actioned 2026-07-14
**Disposition: caveat/downgrade** (relabel/hygiene tier). Added a ⚠️ caveat banner to the interpretive page (or artifact README for comp-015) capturing the audit's headline finding — the qualitative direction holds, but the quantitative/verdict framing overstated what the model resolves. Deeper artifact fixes (reproducibility defects, provenance-tier labeling, code/summary mismatches, any recompute) remain in the Required-actions above as residuals for a focused follow-up.
