---
title: "Gut-Lumen Uricase Physiological Regime — Computational Audit (comp-044)"
date: 2026-07-13
tags: [uricase, gout, gut-lumen, kinetics, oxygen, computational, comp-044]
related:
  - computational-experiments.md
  - validation-experiments.md
  - uricase-abcg2-genotype-stratification-computational.md
  - gut-lumen-sink.md
  - hypotheses/H08-gut-lumen-sink-platform-thesis.md
sources:
  - "Miyazaki et al. 2025 — PMCID PMC11877951"
  - "Gao et al. 2025 — PMID 41038159"
  - "Zhao et al. 2022 — PMID 35491895"
---

# Gut-Lumen Uricase Physiological Regime — Computational Audit (comp-044)

## Question

Does comp-019's conclusion that 5–50 mg/day oral uricase is always in a substrate-limited, flat-dose regime survive when the model's own luminal-urate concentration and Km are applied together with a finite active window?

## Verdict

**RED for the legacy quantitative claim; biological gut-sink hypothesis remains OPEN.** The prior flat-dose and predicted-ΔSUA results should not guide dose or yield decisions. Applying 0.59 µM urate, Km 25 µM, and a three-hour window moves all three central diagnostic dose ratios below one before any oxygen, access, or survival penalty. This does not establish the true in-vivo regime; it establishes that comp-019's regime classification was not robust.

## Why this matters

The flat-dose verdict propagated into H08, engineered-strain yield priorities, single-dose validation design, and comp-031's claim that UOX and PDB must compete for a fully depleted luminal pool. Those downstream choices depend on a calculation that did not use the substrate concentration or Km stored in its own input file.

## Method summary

comp-044 converts UOX dose and specific activity into an upper-bound urate-degradation capacity, then explicitly applies:

- Michaelis–Menten substrate occupancy;
- finite active-window duration;
- nonmechanistic scenario multipliers for pH/activity, effective oxygen-dependent activity, substrate access, and enzyme survival;
- the legacy 233 mg/day intestinal-flux denominator, retained only to make the regime comparison legible.

Five named scenarios and a discrete 1,620-cell full-factorial grid per dose are evaluated. Grid occupancy is not treated as probability. No serum-urate change is computed.

## Key results

| Scenario | 5 mg | 25 mg | 50 mg |
|---|---:|---:|---:|
| Legacy 24-hour Vmax | 32.3377 | 161.6886 | 323.3773 |
| 0.59 µM, Km 25 µM, three hours; no additional penalty | 0.0932 | 0.4660 | 0.9320 |
| Same, with microoxic/access/survival scenario multipliers | 0.0035 | 0.0175 | 0.0349 |
| 50 µM sensitivity case with the same multipliers | 0.1011 | 0.5053 | 1.0106 |

Only the ratio-one boundary has direct mass-balance meaning. The other descriptive bins in the artifact are scanning aids. A ratio above one still does not prove complete luminal capture because local replenishment, depletion, diffusion, and reabsorption remain unmodeled.

## Two independent reasons the legacy verdict fails

1. **Substrate occupancy:** 0.59 µM urate is far below the central 25 µM Km prior, so label Vmax cannot be applied directly.
2. **Time exposure:** the prior calculation granted every delivered milligram 24 hours at full activity even though its own primary small-bowel window was 2–4 hours.

Oxygen, topology, access, and survival add further uncertainty but are not needed to invalidate the unconditional flat-dose claim.

## Limitations

- The fixed-concentration screen is not a dynamic compartmental gut model.
- The daily-flux denominator and local jejunal concentration are different kinds of quantities; their comparison is a bounded diagnostic, not physiological closure.
- The pH, oxygen, access, and survival multipliers are scenario variables and may be correlated.
- The 50 and 500 µM cases are sensitivity values, not measured human baselines.
- No renal compensation, intestinal reabsorption, microbial metabolism, genotype-specific supply, or serum-pool dynamics are modeled.
- Independent peer review confirmed the arithmetic and verdict but required the grid to be described as design-space occupancy rather than probability; that correction is incorporated.

## Impact on experimental priorities

This turns oral-UOX dose response from “settled computationally” back into a **feasibility gate**. Yield optimization cannot be deprioritized on comp-019's basis. The next experiment must jointly measure local urate, oxygen, topology-specific activity, peroxide, and enzyme persistence; comp-045 supplies that design.

## Cross-references

- [Reproducible artifact](./etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/)
- [Topology × oxygen × peroxide design](./uricase-topology-oxygen-peroxide-design-computational.md)
- [Validation experiments](./validation-experiments.md)
- [Superseded comp-019 interpretation](./uricase-abcg2-genotype-stratification-computational.md)

