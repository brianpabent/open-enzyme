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

Does comp-019's conclusion that 5–50 mg/day oral uricase is always in a substrate-limited, flat-dose regime survive when the omitted substrate-occupancy term and a finite active window are applied using the inherited corpus priors?

## Verdict

**Mechanistic Extrapolation (deterministic consistency audit; inherited inputs): LEGACY UNCONDITIONAL FLAT-DOSE CLASSIFICATION NOT ROBUST TO THE TESTED DIAGNOSTICS; biological gut-sink hypothesis remains OPEN.** The prior flat-dose and predicted-ΔSUA results should not guide dose or yield decisions. In the prespecified central diagnostic, applying 0.59 µM urate, Km 25 µM, and a three-hour window moves all three tested ratios below one before any oxygen, access, or survival penalty. This establishes only that comp-019's unconditional classification was not robust to the tested substrate-occupancy and finite-window diagnostics. It does not identify the true physiological regime, reverse the old conclusion, or establish a sufficient oral dose.

## Method summary

comp-044 converts UOX dose and specific activity into an upper-bound urate-degradation capacity, then explicitly applies:

- Michaelis–Menten substrate occupancy;
- finite active-window duration;
- nonmechanistic scenario multipliers for pH/activity, effective oxygen-dependent activity, substrate access, and enzyme survival;
- the legacy 233 mg/day intestinal-flux denominator, retained only to make the regime comparison legible.

Five named scenarios and a discrete 1,620-cell full-factorial grid per dose are evaluated. Grid occupancy is not treated as probability. No serum-urate change is computed.

The 8.3 U/mg specific activity, Km range, 2–4 hour active-window range, and 233 mg/day denominator are inherited or derived corpus priors. They were not newly primary-source verified for quantitative planning in comp-044. The 0.59 µM input is inherited from a grep-verified extraction of terminal-ileal fluid measurements in a balloon-enteroscopy cohort (Miyazaki et al. 2025, PMCID PMC11877951); it is not a healthy-population baseline. These inputs are adequate for the bounded internal-consistency test, not for selecting a dose.

## Key results

| Scenario | 5 mg | 25 mg | 50 mg |
|---|---:|---:|---:|
| Legacy 24-hour Vmax | 32.3377 | 161.6886 | 323.3773 |
| 0.59 µM, Km 25 µM, three hours; no additional penalty | 0.0932 | 0.4660 | 0.9320 |
| Same, with microoxic/access/survival scenario multipliers | 0.0035 | 0.0175 | 0.0349 |
| 50 µM sensitivity case with the same multipliers | 0.1011 | 0.5053 | 1.0106 |

Only the ratio-one boundary has direct mass-balance meaning. The other descriptive bins in the artifact are scanning aids. A ratio above one still does not prove complete luminal capture because local replenishment, depletion, diffusion, and reabsorption remain unmodeled.

## Terms omitted from the legacy calculation

1. **Substrate occupancy:** Under the inherited central inputs, 0.59 µM urate is below the 25 µM Km prior, so applying label Vmax directly overstates modeled capacity.
2. **Time exposure:** The prior calculation granted every delivered milligram 24 hours at full activity; comp-044 instead tests the inherited 2–4 hour active-window range.

Oxygen, topology, access, and survival add further uncertainty but were not needed to show that the unconditional flat-dose classification was not robust to the tested diagnostics.

## Limitations

- The fixed-concentration screen is not a dynamic compartmental gut model.
- The daily-flux denominator and local jejunal concentration are different kinds of quantities; their comparison is a bounded diagnostic, not physiological closure.
- The pH, oxygen, access, and survival multipliers are scenario variables and may be correlated.
- The 50 and 500 µM cases are sensitivity values, not measured human baselines.
- No renal compensation, intestinal reabsorption, microbial metabolism, genotype-specific supply, or serum-pool dynamics are modeled.
- The 8.3 U/mg activity, Km range, active-window range, and daily-flux denominator require direct primary-source verification before any quantitative planning use.

## Impact on experimental priorities

Oral-UOX dose response remains a **feasibility gate**. Yield optimization cannot be deprioritized on comp-019's basis, and no current production figure establishes dose sufficiency. Exact configurations must first be built and characterized in the relevant construct-supply work (validation §§1.1, 1.2, and 1.5) or supplied as an exact external configuration. §1.33 then measures local urate, oxygen, configuration-specific activity, peroxide, and persistence. A topology may be nominated only within a controlled host comparison; cross-host results remain configuration-specific. §1.36 safety precedes animal escalation.

## Cross-references

- [Reproducible artifact](./etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/)
- [Topology × oxygen × peroxide design](./uricase-topology-oxygen-peroxide-design-computational.md)
- [Validation experiments](./validation-experiments.md)
- [Comp-019 interpretation](./uricase-abcg2-genotype-stratification-computational.md)
