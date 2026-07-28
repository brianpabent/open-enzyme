---
title: "Intestinal ABCG2 Sex Differences — Evidence Boundary"
date: 2026-05-07
tags:
  - abcg2
  - intestinal-urate-secretion
  - sex-differences
  - q141k
  - q140k
  - hormone-signaling
related:
  - t-abcg2-suppression-evidence-mining-computational.md
  - androgen-urate-axis.md
  - abcg2-modulators.md
  - gut-lumen-sink.md
  - computational-experiments.md
sources:
  - "Hoque KM, Halperin Kuhns VL et al. (2020) Nature Communications 11:2767, PMID 32488095, doi:10.1038/s41467-020-16525-w"
  - "Liu L, Zhao T, Shan L et al. (2021) Nutrition & Metabolism 18:63, PMID 34144706, doi:10.1186/s12986-021-00583-y"
  - "Slepnev AA, Abalenikhina YV, Popova NM et al. (2023) Biochemistry (Moscow), Supplement Series A, doi:10.1134/S1990747823050100"
  - "MacLean C, Moenning U, Reichel A, Fricker G (2008) Drug Metabolism and Disposition 36:1249-1254, PMID 18378562, doi:10.1124/dmd.108.020859"
status: active
---

# Intestinal ABCG2 sex differences — evidence boundary

Intestinal ABCG2 is a gout-relevant urate-export chokepoint: changing its abundance, surface localization, or transport activity could change how much urate reaches the lumen. The decision-relevant question is whether healthy-human intestinal ABCG2 differs by sex enough to alter that supply.

**Current verdict: unresolved.** COMP-017 extracted no sex-stratified GTEx intestinal distributions and no sex-stratified Human Protein Atlas intestinal protein values. It therefore did not test its prespecified 1.5-fold population threshold. Animal, disease-state, and cell-culture findings cannot substitute for that missing human comparison.

## What the available evidence establishes

| Context | Result | Evidence boundary |
|---|---|---|
| Healthy-human intestinal baseline | No direct sex-stratified values were extracted. | **Unresolved**; no quantitative null or difference is established. |
| Healthy rat intestine | MacLean et al. reported no sex-specific transporter-expression difference across the intestinal scan. | **Animal Model**; qualitative null without a human effect-size estimate. |
| Q140K mouse disease state | Hoque et al. reported 78% lower jejunal ABCG2 by Western blot in Q140K+/+ versus WT mice (WT n=8; Q140K+/+ n=6; p=0.0046), compared with a 44% renal reduction. Modeled ABCG2-mediated jejunal urate flux fell 84.2% (WT n=17; Q140K+/+ n=10; p<0.0001). | **Animal Model**; genotype-stressed mouse physiology, not healthy-human baseline. |
| Estradiol-benzoate exposure in Caco-2 cells | Liu et al. found that nominal 100 µM estradiol benzoate increased ABCG2 mRNA at 48 hours without a dose-dependent response; 50 µM LY294002 partially blocked the effect. | **In Vitro**; pharmacological culture exposure, not physiological regulation magnitude. |
| Sex-hormone exposure in Caco-2 cells | Slepnev et al. reported increased ABCG2 after progesterone, estradiol, or testosterone at nominal 1, 10, and 100 µM for 24 hours. PXR/FXR inhibitor conditions reduced the testosterone-associated increase, which remained above control. | **In Vitro**, official English abstract tier; fold changes and free-tissue exposure were not established, and androgen-receptor involvement was not directly excluded. |

For Hoque et al., use the primary-verified **78% jejunal versus 44% renal Western-blot comparison**. The article reports a separate statistically significant reduction in jejunal immunofluorescence signal but no combined 53% or 88% intestinal reduction. The underlying source-data workbook reproduces the published ~78% homozygote result.

## What this does not establish

- A healthy-human intestinal ABCG2 sex difference or null.
- Direct androgen-receptor repression of intestinal ABCG2.
- A physiological effect size from nominal high-concentration Caco-2 exposures.
- A clomiphene mechanism, a pan-male response rule, or a genotype-conditioned response to luminal uricase.
- That transcript abundance alone predicts apical protein, urate flux, or intervention response.

> **Research conjecture — Intestinal ABCG2 response may be context-stratified rather than sex-binary**{ .research-conjecture-label }
>
> **Grounded premises:** Q140K mice show a large intestinal ABCG2 abundance and urate-flux defect in a gout-relevant disease state (**Animal Model**; Hoque et al. 2020, PMID 32488095). Healthy rats showed no baseline intestinal sex difference (**Animal Model**; MacLean et al. 2008, PMID 18378562). Caco-2 ABCG2 responds to sex hormones under nominal pharmacological exposures (**In Vitro**; Liu et al. 2021, PMID 34144706; Slepnev et al. 2023, DOI 10.1134/S1990747823050100).
>
> **Novel leap:** No direct evidence establishes this connection, but human intestinal urate-export capacity may separate most strongly by genotype × hormone state × inflammatory context rather than by sex alone.
>
> **Why it matters:** A context-stratified model could identify a real supply constraint or rescue opportunity without imposing a blanket male ceiling.
>
> **Discriminating observation:** Measure total and apical ABCG2 plus polarized urate flux in donor-derived intestinal models stratified by rs2231142, with prespecified hormone and inflammatory conditions.

## Next discriminating work

1. Fix a versioned direct-human dataset, intestinal tissue definitions, donor inclusion rules, sex-variable provenance, normalization, uncertainty model, and the population-level threshold before rerunning the baseline question.
2. Treat RNA, total protein, apical localization, and urate flux as separate measurements.
3. If direct-human baseline differences are small, test whether rs2231142, hormone state, or inflammation exposes a larger conditional effect rather than declaring the entire track dead.
4. Advance an intervention claim only when matched conditions show a reproducible change in functional urate flux.

The reproducible inputs, validator, outputs, and exact-snapshot reviews are in [COMP-017](./etc/experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/). [COMP-016](./t-abcg2-suppression-evidence-mining-computational.md) remains the historical bounded scan; this page supersedes only its ABCG2 attribution, magnitude, and healthy-baseline interpretations.
