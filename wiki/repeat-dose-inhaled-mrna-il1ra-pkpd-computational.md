---
title: "Repeat-dose inhaled mRNA-IL-1Ra PK/PD with receptor-occupancy framing (comp-036)"
date: 2026-05-16
tags:
  - chassis-pending
  - mrna-lnp
  - acute-flare-abort
  - il1ra
  - receptor-occupancy
  - repeat-dose
  - pkpd
  - computational
related:
  - chassis-pending-interventions.md
  - inhaled-mrna-il1ra-pulse-computational.md
  - etc/open-enzyme-vision.md
  - nlrp3-inflammasome.md
  - gout-action-guide.md
sources:
  - "etc/experiments/comp-036-repeat-dose-inhaled-mrna-il1ra-pkpd/ — Monte Carlo PK/PD, n=10,000/regimen, seed 36"
  - "Arend 1990 JCI (PMID 2139669, DOI 10.1172/JCI114622); Schreuder 1997 Nature (PMID 9062194); Vigers 1997 Nature (PMID 9062193); Saag 2021 Arthritis Rheumatol (PMID 33605029, DOI 10.1002/art.41699)"
status: published
---

# Repeat-dose inhaled mRNA-IL-1Ra PK/PD — computational analysis (comp-036)

**Verdict: YELLOW.** Repeat dosing partially salvages comp-033's RED single-dose Cmax verdict, but the high-confidence GREEN bar (median 95% of the 0-72h flare window above 80% receptor occupancy AND p25 >= 50%) is NOT reached by any of three dosing regimens. The modality is viable but at the edge — wet-lab dose-finding is needed to confirm or pivot.

## Methodology reframe (load-bearing)

comp-033 used plasma Cmax-vs-anakinra-1.5-µg/mL as the decision gate (single inhale gives 0.025 µg/mL = 2% of anakinra → RED). comp-036 reframes to **receptor-occupancy fraction over the 0-72h gout flare window** — the clinically-relevant metric for a competitive antagonist. IL-1Ra-IL-1R1 Kd ~1 nM (range 0.1-10 nM log-uniform; Arend 1990 JCI [DOI 10.1172/JCI114622](https://doi.org/10.1172/JCI114622); Schreuder 1997 Nature crystal at 2.7 Å). Receptor occupancy = [IL-1Ra]_nM / ([IL-1Ra]_nM + Kd). 80%-occupancy plasma threshold: **median 73 ng/mL** [p05-p95: 9-553]. Single-dose Cmax 25 ng/mL is below median threshold; anakinra steady-state 1500 ng/mL is 21× above (operates at ~85-90% mean occupancy).

## Regimen scan (smallest N achieving sustained occupancy bar)

| Regimen | Best median sustained-80%-window | p25 | Median mean-occ | GREEN? |
|---|---|---|---|---|
| QD x1-14 days | 0.00 | 0.00 | 0.66 | NO — trough drops <80% every interval |
| BID x4-28 doses (2-14d) | 0.50-0.56 | 0.00 | 0.73-0.74 | NO — median 50%, p25=0 |
| Loading 2x + QD x14 | 0.32 | 0.00 | 0.75 | NO |

**BID is qualitatively superior.** BID 4+ doses (2+ days every-12h) reaches ~50% of flare window above 80% occupancy at mean occupancy ~73-74%. QD never sustains 80% (24h troughs too low). Anakinra steady-state (~85-90% mean occupancy) remains unmatched. **p25 stays at 0% across all regimens** — driven by Kd-prior uncertainty (ρ = -0.69) and translation-efficiency uncertainty (ρ = +0.58).

## Sensitivity drivers

Top 3 drivers of mean window occupancy: **Kd_nM (ρ = -0.69)**, translation_eff_ng_per_µg (ρ = +0.58), dose_mg_mrna (ρ = +0.24). Kd is now the #1 driver — comp-036's introduction of receptor-occupancy framing surfaces this previously-implicit uncertainty.

## Clinical handoff (YELLOW path)

**Single critical wet-lab measurement**: integrated translation-efficiency mass ratio in human alveolar epithelium for inhaled m1Psi-mRNA-LNP. The 1,000-50,000 ng/µg prior is the #2 dominant uncertainty; ferret or NHP single-dose inhaled-LNP study with BAL protein quantification would resolve. **Second priority**: modern SPR IL-1Ra-IL-1R1 Kd measurement at physiological conditions to tighten 0.1-10 nM prior to <2× span.

## Clinical reframe

Repeat-dose inhaled mRNA-IL-1Ra is NOT a like-for-like anakinra replacement at the receptor-occupancy level. It IS a meaningfully-better-than-nothing option that could displace prednisone for gout patients tolerating sub-anakinra occupancy in exchange for no SC injections, no glucocorticoid burden (acute glucose/BP/mood/sleep; chronic bone/cataract/adrenal), and substantial cost edge vs canakinumab. Decision reframes from "match anakinra?" (no) to "partial-suppression × side-effect-advantage worth it vs prednisone?" (plausibly yes — needs wet-lab data).

## Frozen analysis archived to ./etc/experiments/comp-036-repeat-dose-inhaled-mrna-il1ra-pkpd/wiki-archive.md

## Cross-references

[comp-036 reproducible analysis](./etc/experiments/comp-036-repeat-dose-inhaled-mrna-il1ra-pkpd/) | [comp-033 single-dose precursor](./etc/experiments/comp-033-inhaled-mrna-il1ra-pulse-therapy/) → [`inhaled-mrna-il1ra-pulse-computational.md`](./inhaled-mrna-il1ra-pulse-computational.md) | [`chassis-pending-interventions.md` §4](./chassis-pending-interventions.md) | [`gout-action-guide.md`](./gout-action-guide.md) | [`nlrp3-inflammasome.md`](./nlrp3-inflammasome.md)
