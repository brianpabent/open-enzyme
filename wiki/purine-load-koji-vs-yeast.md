---
title: "Purine Load: Koji vs. Yeast Chassis"
date: 2026-06-30
updated: 2026-07-13
tags:
  - purine
  - koji
  - yeast
  - chassis-selection
  - gout
related:
  - uricase
  - saccharomyces-cerevisiae
  - aspergillus-oryzae
  - staged-purine-sink-mass-balance-computational
sources:
  - "Kaneko et al. 2014, doi:10.1248/bpb.b13-00967"
  - "USDA/NIH ODS Purine Database Release 2.0 (2025)"
---

# Purine Load: Koji vs. Yeast Chassis

**Status:** Open product-measurement question. Earlier chassis-ranking conclusion retracted
2026-07-13.

> **Correction.** The previous version inferred an engineered-yeast product from broad
> “dried yeast” ranges and inferred engineered rice koji from rice and miso. It then reported
> a 15–120-fold chassis difference without measuring either product. Those substitutions do
> not support a product-level comparison. The reference-food values below are retained only
> as assay-planning bounds.

## Verdict

Ingested microbial biomass can add purines, but **the actual Open Enzyme yeast and koji
products have not been measured**. Chassis selection therefore cannot yet use purine load as
a settled advantage for either host.

There is a second mechanistic correction: uricase oxidizes **urate**, not the adenine,
guanine, hypoxanthine, nucleosides, or nucleotides contained in biomass. Co-delivered
uricase cannot be assumed to neutralize biomass purines directly. Those substrates must
first reach urate through host or microbial metabolism. The compartment and timing matter.

## Verified reference values—not product measurements

| Reference material | Total purines (mg/100 g) | Ten-gram equivalent | What the number establishes |
|---|---:|---:|---|
| “Yeast, dried,” USDA/ODS Release 2.0 merged entry | 847.1 | 84.7 mg | One reference bound for dried yeast material |
| “Beer yeast,” one product in Kaneko et al. 2014 | 2,995.7 | 299.6 mg | Product-to-product variation can be large |
| Unpolished rice, Kaneko et al. 2014 | 37.4 | 3.74 mg | A substrate reference, **not** a rice-koji measurement |
| Engineered Open Enzyme yeast product | unknown | unknown | Requires direct assay |
| Engineered Open Enzyme rice-koji product | unknown | unknown | Requires direct assay |

**Evidence level: analytical food-composition measurements.** The USDA value is the sum of
adenine 409.3, guanine 422.7, and hypoxanthine 15.1 mg/100 g in the merged “Yeast, dried”
entry. The Kaneko beer-yeast and rice values are measurements of the named samples, not
universal species constants.

The rice value cannot be carried forward as the value for koji. Fungal biomass density,
growth phase, residual rice fraction, drying, autolysis, and downstream processing can all
change total purines and their chemical forms. The same caution applies across yeast
products.

## Why species-resolved fate matters

Dietary purines do not arrive as one interchangeable “purine load.” Adenine and guanine can
be salvaged into nucleotides, degraded through hypoxanthine/xanthine to urate, or metabolized
by gut microbes. A downstream luminal uricase arm acts only after urate exists; an upstream
whole-cell purine-degrading bacterium can alter earlier branch points. [comp-046](./staged-purine-sink-mass-balance-computational.md)
therefore uses a conserved dietary-precursor fate ledger and a separate endogenous
luminal-urate capture-fraction comparison. It treats staging as an empirical question rather
than subtracting “uricase capacity” from total biomass purines.

## Decisive experiment

Measure the two final formulations—not proxy foods—with a species-resolved assay for
adenine, guanine, hypoxanthine, xanthine, urate, nucleosides, and nucleotides. Then run the
isotope-resolved sequential-flux experiment in
[validation experiment 1.34](./validation-experiments.md#134-isotope-resolved-dietary-precursor--uox--pdb-sequential-flux).
The decision variable is recovered purine fate and urate appearance after the complete
formulation, not total-purine concentration alone.

## Sources

- Kaneko K, Aoyagi Y, Fukuuchi T, Inazawa K, Yamaoka N. Total purine and purine base
  content of common foodstuffs for facilitating nutritional therapy for gout and
  hyperuricemia. *Biol Pharm Bull.* 2014;37:709–721.
  [doi:10.1248/bpb.b13-00967](https://doi.org/10.1248/bpb.b13-00967).
- USDA Agricultural Research Service and NIH Office of Dietary Supplements. Purine Content
  of Foods, Release 2.0 (2025): [landing page](https://www.ars.usda.gov/northeast-area/beltsville-md-bhnrc/beltsville-human-nutrition-research-center/methods-and-application-of-food-composition-laboratory/mafcl-site-pages/purine-content-of-foods/)
  and [workbook](https://www.ars.usda.gov/ARSUserFiles/80400535/Data/Purine/PURINEDATABASEANDDATASOURCES2025.xlsx).
