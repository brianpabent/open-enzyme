# Input provenance — comp-044

Fetched/rechecked 2026-07-13.

## Direct or inherited evidence priors

- Human jejunal urate concentration: central 0.59 µM, range 0.06–1.16 µM, inherited from comp-019's grep-verified extraction of Miyazaki et al. 2025 (PMCID PMC11877951). The conversion is independently arithmetic-checked: 99.5 pg/µL = 99.5 µg/L; divided by urate MW 168.11 g/mol = 0.592 µmol/L.
- Uricase Km range 5–100 µM, central 25 µM, and specific activity 8.3 U/mg: inherited regulatory/literature prior from comp-019; not newly checked against the primary regulatory or enzyme source for quantitative planning. The model treats the Km range as uncertainty, not a universal enzyme constant. The separate 0.75 pH/activity term is an inherited scenario multiplier, not a regulatory measurement.
- Small-bowel active window 2–4 h: inherited physiology prior already used in `wiki/gi-survival-prediction.md`; not newly verified against a primary source or treated as a measured patient value.
- Legacy daily intestinal urate flux 233 mg/day: corpus prior derived from 700 mg/day total turnover × 0.33 intestinal share. It remains uncertain and is used only as the denominator for regime classification, not as a predicted patient-specific flux.

## Direct engineered-system precedents

- Zhao R et al. *Gut Microbes* 2022. PMID 35491895; PMCID PMC9067508. PucL/PucM + YgfU + KatG + Vitreoscilla hemoglobin improved urate degradation under restricted dissolved oxygen. This supports including oxygen as an explicit uncertainty; it does not justify treating the relative-oxygen factor as linear enzyme kinetics.
- Gao et al. *Cell Reports Medicine* 2025. PMID 41038159; PMCID PMC12629798. PULSE tested intracellular, LamB-secreted, and InakN-displayed smUOX and added KatG + VHb. This supports separating physiological regime classification from topology selection.

## Scenario parameters — not evidence claims

The 50 and 500 µM urate cases, pH/activity multiplier, effective oxygen-dependent activity multipliers, substrate-access factors, and enzyme-survival factors are deliberately broad design scenarios. They are not labeled human baselines. Exact *A. flavus* UOX oxygen kinetics in the relevant gut formulation are not available; oxygen is therefore a nonmechanistic dimensionless activity multiplier, not a linear oxygen-kinetics claim. Access and survival may be correlated; the full-factorial grid does not model that covariance.

## Excluded claim

No serum-urate change is computed. The previous comp-019 mapping from enzyme capacity to ΔSUA is not retained because it requires dynamic whole-body transport, renal compensation, absorption/reabsorption, and patient-specific ABCG2 supply that this bounded analysis does not establish.
