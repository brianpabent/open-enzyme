# comp-033: Inhaled mRNA-IL-1Ra pulse therapy — target validation, dose modeling, partner-ID

**Question:** Does dose modeling show pulmonary IL-1Ra expression can plausibly reach anakinra-equivalent therapeutic exposure at currently-feasible inhaled-mRNA doses (4–24 mg per administration), and which existing inhaled-mRNA programs / CDMOs are forkable partners?

**Verdict: RED** on the systemic-anakinra-equivalent gate. Median predicted plasma Cmax 0.025 µg/mL is 1/60th of anakinra (1.5 µg/mL); only the upper-decile prior space (p95 = 0.28 µg/mL) approaches the anakinra-trough exposure (0.05 µg/mL). Reverse-dose calculation predicts ~195 mg mRNA per administration would be needed to reach a 0.5 µg/mL median Cmax (minimum-effective threshold, 1/3 anakinra) and ~585 mg to reach the full anakinra benchmark — both 8–25× the highest currently-disclosed inhaled-mRNA clinical dose (24 mg, Translate Bio MRT5005). The dose-feasibility gap is the load-bearing finding.

**The verdict does NOT close the door on the modality.** Three honest paths forward:
1. **Repeat dosing within a single flare** — 2–4 nebulizer administrations per 24h could plausibly accumulate to therapeutic AUC without requiring single-dose breakthroughs.
2. **Local delivery (intra-articular mRNA-IL-1Ra)** — bypasses the systemic dilution that dominates the inhaled math; local concentration at the affected joint is what matters for flare-abort.
3. **Sub-anakinra systemic exposure may still be therapeutically meaningful** — anakinra's Cmin (trough) is 0.05 µg/mL and the drug retains efficacy; the upper-decile prior (Cmax 0.28 µg/mL, AUC ~5 µg·h/mL) reaches order-of-magnitude similar AUC to anakinra trough-band exposure sustained over 48h. The RED verdict is specifically against full anakinra-equivalent matching, NOT against any therapeutic effect.

**The partner landscape is intact.** 4 Tier A inhaled-mRNA clinical-stage programs identified (Arcturus, ReCode, Ethris, Sanofi/Translate Bio legacy), 7 Tier B CDMOs with relevant capability, 4 Tier C academic labs with published inhaled mRNA-LNP work. **15 total partner candidates.** Discovery-engine handoff package is shippable regardless of the dose-modeling verdict.

**The economic comparison holds independently of the dose-feasibility math.** Even at high-cost low-scale ($120 per dose × 10 flares = $1,200/yr), inhaled mRNA-IL-1Ra is 50–250× cheaper than canakinumab ($100K–300K/yr). At central economics ($18/dose, ~$180/yr) the ratio is 500–3000×.

**Informs:** [`wiki/chassis-pending-interventions.md` §4](../../../chassis-pending-interventions.md) (the originating chassis-pending entry); [`wiki/etc/open-enzyme-vision.md` §10](../../../etc/open-enzyme-vision.md) (the temporal-stack platform-positioning frame); [`wiki/modality-chokepoint-matrix.md` §"Open exploration questions" #5](../../../modality-chokepoint-matrix.md); [`wiki/delivery-route-matrix.md`](../../../delivery-route-matrix.md).

**Interpretive wiki page:** [`wiki/inhaled-mrna-il1ra-pulse-computational.md`](../../../inhaled-mrna-il1ra-pulse-computational.md)

**Related experiments:** [comp-035 (intra-articular uricase + catalase reaction-diffusion)](../comp-035-ia-uricase-h2o2-reaction-diffusion/) — different intervention, same intra-articular-as-acute-flare-route thesis; the intra-articular pivot path-3 above is the comp-033 → comp-035 sister relationship.

---

## How to reproduce

```bash
cd experiments/comp-033-inhaled-mrna-il1ra-pulse-therapy
python3 analyze.py
```

Stdlib-only Python 3 (no external packages). All inputs are committed in `inputs/`. Outputs are deterministic given the RNG seed (33).

---

## File index

```
comp-033-inhaled-mrna-il1ra-pulse-therapy/
  analyze.py                              ← analysis script (run this)
  README.md                               ← this file
  inputs/
    il1ra_target_properties.json          ← IL-1Ra (UniProt P18510) target validation + alternative-payload comparison + route selection
    anakinra_benchmark_pk.json            ← anakinra PK reference + canakinumab cost benchmark
    inhaled_mrna_precedents.json          ← published inhaled mRNA-LNP programs (Translate Bio, Arcturus, ReCode, Ethris, Moderna) + lung-expression anchors
    construct_design_priors.json          ← codon / UTR / chemistry / polyA / signal peptide / LNP-device recommendations
    mrna_lnp_economics.json               ← COGS at COVID-vaccine-class scale + specialty-inhaled scale; cost-per-flare scenarios
    partner_landscape.json                ← Tier A clinical-stage programs / Tier B CDMOs / Tier C academic labs; recommended first contacts
    model_parameters.json                 ← Monte Carlo + decision-rule parameters
    provenance.md                         ← Per CLAUDE.md Rule 4: source + verification status for every input
  outputs/
    dose_auc_prediction.json              ← MC plasma Cmax + AUC distribution; sensitivity; reverse-dose calculation
    economic_comparison.json              ← cost-per-flare at scale vs canakinumab benchmark
    summary.md                            ← human-readable result summary (auto-generated by analyze.py)
```

---

## Methodology — Monte Carlo dose-AUC model + partner-landscape scan

Per the comp-033 brief and BioDesignBench evaluation-depth discipline ([`etc/autonomous-screening-methodology.md`](../../../etc/autonomous-screening-methodology.md) §"BioDesignBench evaluation-depth audit"), the analysis combines:

### 1. Target validation

IL-1Ra (UniProt P18510 mature aa 26–177, 17.3 kDa, non-glycosylated, single disulfide C91–C141) selected over alternative IL-1-axis payloads:
- **Soluble IL-1R2 decoy** — higher IL-1β affinity but blocks only IL-1β, not IL-1α; gout flares release both.
- **IL-1β-binding nanobody** — 12–15 kDa, cheaper mRNA but again blocks only IL-1β; canakinumab clinical precedent shows this is *sufficient* for gout but doesn't change the modality math.
- **IL-1Ra is the right payload** for inhaled mRNA: dual blockade matches anakinra precedent (gives a direct PK benchmark), 17 kDa is well within mRNA-LNP burden range, and non-glycosylated production simplifies alveolar epithelium expression.

Route selection: pulmonary inhaled chosen over SC, IV, intra-articular because (a) ~70 m² alveolar surface is the largest absorptive interface, (b) self-administration via nebulizer matches the home-flare-management use case better than SC injection at flare onset, (c) inhaled mRNA-LNP has the deepest current clinical/CDMO infrastructure (CF, RSV programs).

### 2. Dose-AUC modeling (Monte Carlo, n=20,000, seed 33)

Single-administration mRNA dose → systemic IL-1Ra plasma exposure, computed as:

```
mRNA delivered to alveolus    = dose_mg × lung_delivery_fraction
protein synthesized in lung   = mRNA_alveolus × translation_efficiency_mass_ratio
protein reaching systemic     = protein_synthesized × alveolar_to_systemic_bioavail
plasma kinetics               = zero-order infusion over expression_duration
                                with first-order clearance (anakinra-class)
Cmax                          = (k_in / (Vd × k_el)) × (1 - exp(-k_el × t_expr))
AUC_24h                       = integral over input + decline phases
```

Prior distributions:
- Dose: log-uniform [4, 24] mg per administration (anchored on Translate Bio MRT5005 + Arcturus ARCT-032 disclosed clinical doses)
- Translation efficiency (mass ratio): log-uniform [1,000, 50,000] ng protein per µg mRNA (1–50× mass ratio, anchored on BNT162b2 IM spike-detection plus inhaled-LNP preclinical reports)
- Lung delivery: uniform [0.10, 0.40] (vibrating-mesh nebulizer lower-airway fraction)
- Alveolar→systemic bioavailability: uniform [0.10, 0.50] (17 kDa non-glycosylated, Patton & Byron precedents)
- Expression duration: uniform [24, 96] hours (m1Psi + transient UTRs)
- IL-1Ra clearance: uniform [0.10, 0.25] /hour (anakinra t½ = 4h)
- Vd: uniform [12, 25] L

Anakinra benchmark: 100 mg SC QD → plasma Cmax 1.5 µg/mL, 24h AUC ≈ 12 µg·h/mL.

### 3. Decision rule

- **GREEN:** median Cmax ≥ 0.5 µg/mL AND p05 Cmax ≥ 0.1 µg/mL AND ≥2 Tier A partners
- **YELLOW:** median Cmax 0.1–0.5 µg/mL (sub-anakinra but plausibly therapeutic)
- **RED:** median Cmax < 0.1 µg/mL at currently-feasible inhaled doses

### 4. Reverse-dose calculation

Linear-scaling extrapolation: at median dose of ~10 mg, the model predicts median Cmax 0.025 µg/mL. To reach 0.5 µg/mL median, dose must scale by 20× → ~195 mg. To reach anakinra Cmax 1.5 µg/mL, dose must scale by 60× → ~585 mg. Both far above the currently-disclosed single-administration inhaled mRNA dose of 24 mg.

### 5. Economic comparison

Cost per flare at COVID-vaccine-class manufacturing economics ($0.1–5 per mg mRNA-LNP at scale) × 4–24 mg per dose × 5–10 flares per year. Scenarios:
- Low (high scale, small dose): ~$2/dose, ~$10–20/yr
- Central: ~$18/dose, ~$90–180/yr
- High (low scale, large dose): ~$120/dose, ~$600–1,200/yr

Canakinumab benchmark: $21,000/dose × 5–14 doses/yr = $105K–300K/yr. **Cost ratio 50–3,000× in favor of inhaled mRNA-IL-1Ra approach**, dominated by mRNA-LNP scale economics, independent of dose-feasibility verdict.

### 6. Partner identification

Three tiers:
- **Tier A** (active inhaled-mRNA clinical/preclinical programs): Arcturus ARCT-032, ReCode RCT2100, Ethris SNIM-RNA / AstraZeneca, Sanofi (legacy MRT5005 platform)
- **Tier B** (CDMOs with relevant mRNA-LNP or inhaled-device capability): CordenPharma, Aldevron/Danaher, Lonza, Recipharm (inhalation device), Acuitas (LNP IP), Precision NanoSystems, TriLink/Maravai (modified-nucleoside mRNA)
- **Tier C** (academic labs with published inhaled mRNA-LNP work): Mitchell (UPenn), Sahay (OSU), Anderson (MIT), Siegwart (UTSW, SORT-LNP origin)

**Recommended first contacts:** Arcturus, ReCode, Siegwart Lab UTSW, Mitchell Lab UPenn.

---

## Hard constraints honored

1. **CLAUDE.md Rule 4 pre-commit grep-verify gate** — UniProt P18510 verified directly via `rest.uniprot.org/uniprotkb/P18510.txt` on 2026-05-16 (precursor 177 aa, signal 1–25, mature chain 26–177, disulfide C91–C141, INN=Anakinra). Anakinra PK (100 mg SC, Cmax 1.5 µg/mL, t½ 4h) verified at FDA-label + Yang 2003 peer-reviewed-PK tier. Translate Bio MRT5005 dose range verified at Rowe 2023 J Cyst Fibros + NCT03375047. Translation-efficiency prior corrected mid-analysis (initial 50–500 ng/µg was an underestimate conflating plasma-detection with total-protein-synthesized; corrected to 1,000–50,000 ng/µg integrated mass ratio, with the correction explicitly logged in `inputs/provenance.md`). Six order-of-magnitude estimates with wide priors and explicit anchors.
2. **Explicit confidence bounds throughout** — every output is a distribution (Monte Carlo n=20,000), not a point estimate. Sensitivity analysis reports Spearman rank correlations of all 7 inputs vs predicted Cmax. Top driver: translation efficiency (ρ = +0.78); dose itself is only the 2nd-largest driver (ρ = +0.33), because the dose range explored is narrow log-uniform.
3. **BioDesignBench discipline** — explicit decision rule, multi-axis evaluation (target validation + dose feasibility + economics + partner landscape), reverse-dose calculation to surface the gap, multiple paths forward enumerated honestly.
4. **No further subagents spawned** per brief.
5. **Multilingual default honored** — CNKI and J-STAGE checked for inhaled-mRNA-IL-1Ra or inhaled-biologics-for-gout work. Chinese anakinra-in-gout meta-analyses corroborate Western off-label use; no inhaled-mRNA-IL-1Ra-specific programs in Chinese or Japanese pipelines as of 2026-05-16. Documented in `inputs/provenance.md`.
6. **OE positioning honored** — analysis treats OE as discovery-engine output (target validation + construct-design priors + dose math + economic argument + partner-ID), NOT as manufacturing or clinical-development. The handoff package is what's deliverable.
7. **File restrictions honored** — only `experiments/comp-033-inhaled-mrna-il1ra-pulse-therapy/*` and `wiki/inhaled-mrna-il1ra-pulse-computational.md` created.

---

## V1 simplifications (owned)

1. **Single-compartment PK** for systemic IL-1Ra. Anakinra PK is well-described by single-compartment SC model; pulmonary→systemic input is modeled as zero-order infusion over the expression-duration window. Two-compartment refinement would marginally change AUC distribution but not the verdict.
2. **Lung-expressed protein assumed to reach plasma at the systemic-bioavailability fraction.** Alveolar interstitium and lymphatic transit kinetics are not separately modeled. Folded into the wide [0.10, 0.50] bioavailability prior.
3. **No mRNA degradation kinetics** within the LNP → alveolar epithelium pathway; the translation-efficiency parameter folds in all losses upstream of protein synthesis (LNP uncoating, mRNA escape from endosome, ribosome engagement, template degradation over 24–48h).
4. **No saturation of cellular translation machinery** at high mRNA doses. Reasonable at the 4–24 mg dose range; the reverse-dose extrapolation to 195–585 mg would need re-validation if doses ever reach that scale (likely sub-linear scaling, making the dose-feasibility gap worse, not better).
5. **No accounting for first-pass alveolar macrophage uptake** (which would reduce delivery to alveolar epithelium); conservative — part of the lung-delivery-efficiency lower bound.
6. **Single administration per flare.** Repeat-dosing kinetics (2–4 administrations per 24h within the 72h flare window) is enumerated as a forward path but not modeled quantitatively here. A follow-up comp-NNN could model repeat-dose AUC accumulation.
7. **Linear scaling assumed in reverse-dose calc.** At >100 mg doses, expression-machinery saturation, LNP-toxicity, and per-cell mRNA-burden ceilings likely break linearity — the 195 mg / 585 mg reverse-dose numbers are upper-bound favorable; the true required dose is likely larger.

---

## Disagreement protocol

If you reproduce the outputs and disagree with the methods or numbers, file a GitHub issue referencing this folder (`comp-033-inhaled-mrna-il1ra-pulse-therapy`). Primary candidates for revision:

1. **Translation efficiency mass-ratio prior** (1,000–50,000 ng/µg) — the single largest sensitivity driver (ρ = +0.78). Anchored on BNT162b2 plasma-detection + inhaled-LNP preclinical reports, but the integrated mass-ratio is rarely directly reported in the literature. A peer-reviewed inhaled mRNA-LNP study with quantified total protein in lung tissue per mg mRNA delivered would tighten this prior considerably and likely shift the median Cmax substantially.
2. **Alveolar→systemic bioavailability range** (0.10–0.50) — based on Patton & Byron 2007 protein-class data; IL-1Ra specifically has not been delivered via pulmonary route in any clinical program. The closest analog is Afrezza inhaled insulin (5.8 kDa, ~10–15% bioavailability).
3. **Lung delivery efficiency** (0.10–0.40) — vibrating-mesh nebulizer fraction; could be higher with optimized device geometry or dry-powder inhaler.
4. **Reverse-dose linear-scaling assumption** — translation machinery and LNP toxicity likely break linearity above ~50–100 mg single-administration dose.
5. **Dose-per-flare assumption** — the brief and the wiki frame this as single-administration; repeat-dosing within the 72h flare window could change the verdict materially. A separate comp-NNN repeat-dose AUC accumulation model is warranted.
