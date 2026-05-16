# comp-036 — Repeat-dose Inhaled mRNA-IL-1Ra PK/PD — Result Summary

**Verdict: YELLOW**

_Repeat-dose inhaled mRNA-IL-1Ra achieves >=50%-of-window 80%-occupancy at median but does not reach the >=95%-of-window high-confidence bar. Modality viable but at the edge; wet-lab dose-finding needed to confirm or pivot._

## Methodology reframe

comp-033 returned RED against the plasma Cmax-equivalence bar (single inhale gives 0.025 ug/mL Cmax, 2% of anakinra's 1.5 ug/mL). comp-036 reframes the decision to **receptor-occupancy fraction over the 0-72h gout flare window**, the clinically-relevant metric for a competitive antagonist. IL-1Ra-IL-1R1 Kd ~1 nM (Arend 1990 JCI; Schreuder 1997 Nature crystal). Receptor occupancy = [IL-1Ra]_nM / ([IL-1Ra]_nM + Kd). 80%-occupancy plasma threshold is 72.6 ng/mL median [8.84-552.6], compared to single-dose Cmax 25 ng/mL and anakinra steady-state 1500 ng/mL.

## Per-regimen recommendations

| Regimen | Smallest N (GREEN) | Total days | Median sustained-80% window | p25 | Median mean-occupancy |
|---|---|---|---|---|---|
| QD | not achieved | - | - | - | - |
| BID | not achieved | - | - | - | - |
| Loading+QD-Maint | not achieved | - | - | - | - |

_Note: 'sustained-80% window' = fraction of the 0-72h flare window where occupancy >= 80%. GREEN bar = median >= 0.95 (95% of window) AND p25 >= 0.50._

## Receptor-occupancy threshold (Phase 5)

- 80%-occupancy threshold plasma IL-1Ra: **72.6 ng/mL [8.84-552.6]** (Kd prior 0.1-10 nM log-uniform)
- comp-033 single-dose Cmax: 25 ng/mL (median) — below median threshold
- Anakinra steady-state Cmax: 1500 ng/mL — 21x median threshold

## Sensitivity (Spearman rho vs mean receptor occupancy)

Computed at QD x14 (max scanned, did not pass).

| Input | Spearman rho |
|---|---:|
| kd_nM | -0.690 |
| translation_eff_ng_per_ug | +0.575 |
| dose_mg_mrna | +0.238 |
| systemic_bioavail_frac | +0.216 |
| lung_delivery_frac | +0.172 |
| expression_duration_h | -0.126 |
| clearance_per_h | -0.108 |
| vd_L | -0.081 |
| excess_factor | -0.007 |

## Clinical comparator framing (per-flare and cumulative)

### Per-flare burden

| Therapy | Regimen | Acute side effects (top 2-3) | Per-flare cost USD |
|---|---|---|---|
| Inhaled mRNA-IL-1Ra repeat | not achieved at clinically-practical regimen | cough during nebulization (~30-40%); mucosal irritation; no injection-site reactions; no glucocorticoid burden | $10-600 |
| Anakinra 100 mg SC QD x5 | 5 SC injections | injection-site reactions (~30-40%); modest infection risk | $1,500-2,500 |
| Canakinumab 150 mg SC single | 1 SC injection (clinic) | injection-site (~5-10%); sustained ~3-month immunosuppressive window | $18,000-23,000 |
| Prednisone 30-40 mg taper x12-15d | 12-15 days oral | glucose/BP/mood/sleep acute; familiar profile | $10-30 |

### Cumulative-over-years burden (at 5 flares/yr, 30-yr horizon)

| Therapy | Cumulative burden |
|---|---|
| Inhaled mRNA-IL-1Ra repeat | 15-50 inhaled mRNA-LNP exposures/yr; anti-PEG/innate-immunity cumulative load is the load-bearing unknown (mRNA-vaccine multi-booster data suggests acceptable bounds but inhaled route + larger doses needs direct measurement) |
| Anakinra SC QD x5 | ~25 injections/yr; ADAs ~3-5% over chronic; no characterized severe long-term tox |
| Canakinumab SC single | ~5 injections/yr; ~3-12 months/yr cumulative immunosuppressive exposure; long-term infection risk uncertain at this duty cycle |
| Prednisone taper | ~1,200 mg/yr cumulative pred-equiv -> ~36 g over 30 yrs. Crosses bone-density threshold (~2-5g) within 2-4 yrs; cataract threshold (~10g) within ~10 yrs; adrenal suppression measurable; **this is the toxicity profile the operator is currently accepting**. |

## Clinical handoff

- **If GREEN (current):** Phase 1 dose-finding: inhaled mRNA-IL-1Ra at 4, 10, 24 mg per dose, with anakinra 100 mg SC QD x 5 days as active comparator. Primary endpoint: plasma IL-1Ra Cmax + AUC vs anakinra; pharmacodynamic endpoint: plasma IL-6 / CRP suppression in MSU-induced flare or PMA-stimulated PBMC ex vivo IL-1beta release assay. N=30-45 healthy volunteers (15/arm x 3 dose levels). Wet-lab measurement that would tighten the comp-036 verdict the most: actual translation-efficiency mass ratio (protein / mRNA delivered) in human alveolar epithelium — currently the dominant sensitivity driver (Spearman rho = +0.78 in single-dose; persists in repeat-dose).

- **If YELLOW (alt scenario):** Single critical wet-lab measurement: actual integrated translation-efficiency mass ratio in human alveolar epithelium for inhaled m1Psi-mRNA-LNP IL-1Ra. The 1,000-50,000 ng/ug prior is the dominant uncertainty. A direct measurement in a ferret or NHP single-dose inhaled-LNP study would either confirm GREEN or tip to RED.

- **If RED (alt scenario):** Pivot to intra-articular mRNA-IL-1Ra (sister architecture to comp-035 intra-articular uricase + catalase). Local concentration at the affected joint bypasses systemic dilution; receptor-occupancy math at the joint with bolus IA mRNA delivery is fundamentally different and likely far more favorable. Alternative: accept sub-anakinra exposure with 50-3000x cost edge over canakinumab (per comp-033 economics) and target patients with prednisone-side-effect-driven need for steroid-sparing therapy even at imperfect IL-1 blockade.

