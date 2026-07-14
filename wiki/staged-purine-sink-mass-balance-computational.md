---
title: "Staged Purine Sink Conserved Ledgers — Computational Analysis (comp-046)"
date: 2026-07-13
tags: [gout, purine, nucleoside, GR-5, uricase, PDB, gut, computational, comp-046]
related:
  - computational-experiments.md
  - validation-experiments.md
  - purine-degrading-bacteria.md
  - purine-load-koji-vs-yeast.md
  - gut-lumen-sink.md
sources:
  - "Ji et al. 2025 — DOI 10.1038/s41538-025-00556-y; PMCID PMC12375036"
  - "Wilson and Wilson — PMID 8254512"
  - "Bronk and Hastewell — PMID 6716178"
  - "Liu et al. 2023 — PMCID PMC10421625"
---

# Staged Purine Sink Conserved Ledgers — Computational Analysis (comp-046)

## Question

When are proximal nucleoside interception, microoxic UOX, and distal anaerobic purine degradation genuinely complementary rather than redundant or counterproductive?

## Verdict

**YELLOW — two conditional hypotheses, not one additive efficacy claim.** Whole-cell GR-5 helps the dietary precursor ledger only when nucleoside cleavage is coupled to microbial salvage/retention or reduced absorption of the liberated base. Spatial UOX→PDB staging helps the endogenous luminal-urate ledger only when residual transfer is efficient enough relative to overlap in the urate pool accessible to both arms.

The two ledgers cannot be summed into a serum-urate prediction.

## Why this matters

UOX acts on urate, not on adenine, guanine, or their nucleosides. The current chassis-purine discussion implicitly assumes carried UOX can neutralize co-ingested biomass purines, while comp-031 treats UOX and PDB as well-mixed competitors. GR-5 adds a plausible upstream interception stage, but its DeoD enzyme cleaves nucleosides to free bases rather than destroying the purine ring. That distinction determines whether the intervention reduces or merely changes the absorbable species.

## Method summary

comp-046 uses two independent structures — but **only the dietary one is a conserved 100-unit ledger** (corrected 2026-07-14 per comp-review). The dietary precursor side is a conserved 100-unit fate ledger; the endogenous side is a **capture-fraction architecture comparison, not a conserved 100-unit ledger** — its `endogenous_luminal_urate_units` input is stored but unused by the code, which computes only well-mixed-vs-staged capture fractions. The two structures are:

1. **Dietary precursor ledger:** unintercepted absorbed nucleoside, unintercepted unabsorbed nucleoside, whole-cell microbial salvage/retention, liberated absorbed base, and liberated unabsorbed base. Every grid cell sums to 100.
2. **Endogenous luminal-urate ledger:** UOX and PDB capture under an overlap-adjusted well-mixed equation or a staged equation with explicit residual-transfer efficiency.

A deterministic 6,561-cell full-factorial scans low/mid/high levels. Occupancy of grid cells is a design-space description, not probability.

## Key results

At the central dietary scenario, the conserved 100-unit ledger is:

| Fate | Units |
|---|---:|
| Unintercepted nucleoside absorbed | 36.250 |
| Unintercepted nucleoside unabsorbed | 13.750 |
| Microbial salvage/retention | 22.500 |
| Liberated base absorbed | 18.941 |
| Liberated base unabsorbed | 8.559 |

Across the selected grid, whole-cell GR-5 produces a median 0.181 reduction relative to the matched untreated absorbed precursor, but increases absorbed precursor in 0.111 of grid cells. These are not biological incidence estimates. The dominant unknowns are salvage/retention, interception, and relative base absorption.

For the separate endogenous urate ledger, staging is greater than the overlap-adjusted well-mixed equation in 4,617 of 6,561 grid cells and worse in 1,944. The median difference is only 0.010. The result therefore supplies a boundary, not evidence that staging is superior:

`uox + (1-uox) × residual_transfer × pdb` must exceed the overlap-adjusted same-pool capture.

## Independent mechanism axes

1. **Upstream precursor retention:** disappearance of nucleoside is insufficient; the purine atoms must enter microbial biomass, remain unabsorbed, or be converted into a demonstrably less absorbable fate.
2. **Downstream spatial complementarity:** PDB adds coverage only if residual urate reaches the anaerobic stage while the PDB remains active. Poor transfer or high same-pool access can erase the advantage.

## Limitations

- The GR-5 stage represents the whole organism's cleavage-plus-salvage system, not isolated DeoD causality; the primary mouse study did not provide a DeoD knockout test.
- Parameter levels are design scenarios, not fitted human values.
- Dietary precursor and endogenous luminal urate are separate ledgers and are not added.
- Architecture equations require measured kinetics, residence time, overlap, transfer loss, and PDB viability.
- Microbial turnover/re-release, cross-feeding, renal compensation, inflammation, colonization, and serum dynamics are outside the model.
- Independent peer review rejected the first architecture equation because it guaranteed staging would win. The corrected artifact conserves mass, separates endogenous and dietary pools, and allows either architecture to win.

## Impact on experimental priorities

The staged-platform idea remains plausible, but both links become **feasibility gates**:

- isotope-resolved dietary flux must establish retention rather than nucleoside disappearance;
- a sequential microoxic→anoxic reactor must establish residual transfer, complete product fate, and PDB viability.

## Cross-references

- [Reproducible artifact](./etc/experiments/comp-046-staged-purine-sink-mass-balance/)
- [Purine-degrading bacteria](./purine-degrading-bacteria.md)
- [Purine load: koji versus yeast](./purine-load-koji-vs-yeast.md)
- [Validation experiments](./validation-experiments.md)

