# comp-033 — Inhaled mRNA-IL-1Ra Pulse Therapy — Result Summary
**Verdict: RED**
_median Cmax (0.025 ug/mL) < 0.1 ug/mL minimum-effective threshold at currently-feasible inhaled mRNA doses (4-24 mg/administration). Only the upper-decile prior space (p95 = 0.28 ug/mL) reaches anakinra-trough exposure. Dose modeling predicts 195 mg mRNA needed to reach 0.5 ug/mL median Cmax and 585 mg to reach anakinra Cmax — both outside currently-feasible single-administration inhaled doses. Partner landscape (4 Tier A) is intact; the dose-feasibility gap is the load-bearing finding for the OE handoff._

## Dose-AUC prediction
- Monte Carlo n = 20000, RNG seed 33
- Predicted plasma Cmax: median **0.03 µg/mL** [0.002–0.28] (5th–95th percentile)
- Predicted plasma AUC (24h): median **0.5 µg·h/mL** [0.04–5.0]
- Anakinra benchmark Cmax 1.5 µg/mL → median ratio **0.02× anakinra Cmax** (2%)
- Anakinra benchmark AUC 12.0 µg·h/mL → median ratio **0.04× anakinra AUC** (4%)

## Decision gates

| Gate | Threshold | Observed | Pass |
|---|---|---|:-:|
| Median Cmax | ≥ 0.5 µg/mL | 0.025 | ❌ |
| 5th-pct Cmax | ≥ 0.1 µg/mL | 0.002 | ❌ |
| Tier A partners | ≥ 2 | 4 | ✅ |

## Sensitivity (Spearman ρ vs predicted Cmax)

| Input | Spearman ρ |
|---|---:|
| translation_eff_ng_per_ug | +0.781 |
| dose_mg_mrna | +0.333 |
| systemic_bioavail_frac | +0.277 |
| lung_delivery_frac | +0.257 |
| expression_duration_h | -0.250 |
| clearance_per_h | -0.163 |
| vd_L | -0.133 |

## Economic comparison

- Inhaled mRNA-IL-1Ra cost per flare at scale: $2 (low) — $18 (central) — $120 (high)
- Annual cost at 5–10 flares/yr (central economics): ~$90–180 USD/yr
- Canakinumab benchmark: $105,000–300,000/yr
- **Cost ratio (median inhaled : canakinumab): ~500–3000×** in favor of inhaled mRNA approach.

## Partner shortlist (recommended first contacts)

- Arcturus Therapeutics (highest-stage clinical inhaled mRNA-LNP)
- ReCode Therapeutics (SORT-LNP lung tropism)
- Siegwart Lab UTSW (academic origin of lung-tropic LNP class — could provide a precompetitive scientific collaboration)
- Mitchell Lab UPenn (academic; multiple inhaled mRNA-LNP papers)

Full Tier-A / Tier-B / Tier-C breakdown in `inputs/partner_landscape.json`. Total partner candidates surfaced: 15

## V1 simplifications owned

- Single-compartment PK for systemic IL-1Ra. Anakinra PK is well-described by single-compartment SC model; pulmonary->systemic input is modeled as zero-order infusion over the expression-duration window. Validated by anakinra precedent.
- Lung-expressed protein assumed to reach plasma at the systemic-bioavailability fraction. The alveolar interstitium kinetics are not separately modeled.
- No mRNA degradation kinetics within the LNP -> alveolar epithelium pathway; the 'translation efficiency' parameter folds in all losses upstream of protein synthesis.
- No saturation of cellular translation machinery at high mRNA doses. Reasonable at the 4-24 mg dose range; would need to be revisited if doses scaled to >100 mg.
- No accounting for first-pass alveolar macrophage uptake (which would reduce delivery to alveolar epithelium). Conservative: this is part of the lung-delivery-efficiency fraction's lower bound.
- Single administration per flare. Repeat dosing within a 72h flare window not modeled; the central dose-AUC predicts whether single-dose suffices.
