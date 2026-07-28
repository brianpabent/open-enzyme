---
title: "Testosterone × Intestinal ABCG2 Suppression — Bounded Evidence Scan (comp-016)"
date: 2026-05-07
tags:
  - androgens
  - testosterone
  - abcg2
  - intestinal-urate-secretion
  - evidence-mining
related:
  - intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md
  - androgen-urate-axis.md
  - abcg2-modulators.md
  - computational-experiments.md
sources:
  - "Hoque KM et al. Nature Communications (2020) PMID 32488095"
  - "Sakamoto et al. PLOS One (2018) PMID 30557349"
  - "Liu L et al. Nutrition & Metabolism (2021) PMID 34144706"
  - "Slepnev AA et al. Biochemistry (Moscow) (2023) DOI 10.1134/S1990747823050100"
  - "Jeong et al. Biochim Biophys Acta (2015) PMID 25615818"
  - "MacLean et al. Drug Metabolism and Disposition (2008) PMID 18378562"
status: historical-bounded-scan
---

# Testosterone × intestinal ABCG2 suppression — bounded evidence scan

COMP-016 asked whether primary literature supported direct androgen-driven suppression of intestinal ABCG2 at a magnitude large enough to impose a male-specific constraint on intestinal urate export.

**Surviving result:** the bounded scan did not identify a primary in-vivo study that directly demonstrated testosterone or androgen-receptor suppression of intestinal ABCG2. That supports keeping the proposed mechanism unconfirmed; it does not establish the opposite mechanism, a healthy-human null, or a population-wide response rule.

## Corrected evidence boundary

- Hoque et al. provide **Animal Model** evidence from Q140K mice. The primary-verified like-for-like Western comparison is a 78% jejunal reduction versus a 44% renal reduction. The older 53%/88% values are not supported by the primary article or publisher source-data workbook.
- Liu et al. tested estradiol benzoate in Caco-2 cells. The retained condition was nominal 100 µM at 48 hours, with no dose-dependent response (**In Vitro**). This does not quantify physiological intestinal regulation.
- Slepnev et al.—not Klyushova et al.—reported increased Caco-2 ABCG2 after nominal 1, 10, and 100 µM testosterone, estradiol, or progesterone (**In Vitro**, official English abstract tier). PXR/FXR inhibitor results do not directly exclude androgen-receptor involvement, and no serum-exposure multiplier is justified.
- MacLean et al. reported no sex-specific difference across a healthy-rat intestinal transporter scan (**Animal Model**). This is not a healthy-human effect-size estimate.

The current evidence therefore supports a narrower statement: **direct androgen repression of intestinal ABCG2 was not demonstrated in the sources reviewed.** Healthy-human intestinal sex stratification remains unresolved.

[COMP-017](./intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md) is the current evidence home for attribution, quantitative corrections, context separation, and the next discriminating experiment. COMP-016 remains available as the historical bounded scan; its artifact is not deleted or relabeled as a completed direct-human analysis.

**Reproducible artifact:** [COMP-016 inputs, script, and outputs](./etc/experiments/comp-016-t-abcg2-suppression-evidence-mining/)
