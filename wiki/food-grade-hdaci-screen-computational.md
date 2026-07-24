---
title: "Food-Associated HDAC-Directed Candidates for Q141K ABCG2"
date: 2026-07-24
tags: [abcg2, q141k, hdac, hdac-inhibitor, gout, hyperuricemia, butyrate, sulforaphane, computational]
related:
  - abcg2-modulators.md
  - validation-experiments.md
  - computational-experiments.md
sources:
  - "Basseville A et al. Cancer Res. 2012;72:3642-3651. PMID 22472121"
  - "Xie QS et al. Acta Pharmacol Sin. 2021;42:470-481. PMID 32555444"
  - "Druesne N et al. Carcinogenesis. 2004;25:1227-1236. PMID 14976134"
  - "Su ZY et al. Cancer Prev Res. 2014;7:319-329. PMID 24441674"
  - "Gupta R et al. Toxicol Appl Pharmacol. 2019;377:114631. PMID 31228495"
  - "Saenglee S et al. Pharmacol Rep. 2016;68:1102-1110. PMID 27588384"
---

# Food-Associated HDAC-Directed Candidates for Q141K ABCG2

Q141K ABCG2 is a gout-relevant trafficking weakness: less transporter reaches the cell surface, potentially constraining intestinal urate export. Basseville et al. showed that selected pharmacological HDAC inhibitors restored Q141K surface localization and ABCG2-specific drug-substrate efflux in Flp-In-293 cells (**In Vitro**; [PMID 22472121](https://pubmed.ncbi.nlm.nih.gov/22472121/)). The study did not test urate, butyrate, human intestinal epithelium, or a chronic intervention.

The exploitable question is therefore direct: can a defined, compartment-relevant material restore apical Q141K ABCG2 and ABCG2-attributed urate flux without inhibiting the transporter, injuring the epithelial barrier, or creating unacceptable off-target activity?

## COMP-007 verdict

**Invalidated and retired.** COMP-007 combined heterogeneous biochemical, nuclear-extract, cellular, and analogical potency evidence with arbitrary selectivity constants and `1 − oral bioavailability` as a gut-exposure surrogate. Its stored concentration estimates did not enter the score.

No candidate rank, composite score, confidence-ranked verdict, causal HDAC1/2/3 assignment, HDAC6-centered safety conclusion, top-three shortlist, or Stage 2 advancement survives. The [non-runnable tombstone](./etc/experiments/comp-007-food-grade-hdaci-screen/) binds the retired artifact to its exact Git snapshot.

## Unranked evidence inventory

The inventory nominates materials for direct testing; it does not compare them.

| Candidate | Evidence boundary | Missing decision evidence |
|---|---|---|
| **Butyrate** | Assay-specific recombinant HDAC records exist. Xie et al. found increased endogenous intestinal BCRP/ABCG2 expression and drug-substrate function in non-Q141K-specific rat, primary mouse-enterocyte, and Caco-2 systems; PPARγ antagonist and silencing supported dependence in Caco-2 (**In Vitro + Animal Model**; [PMID 32555444](https://pubmed.ncbi.nlm.nih.gov/32555444/)). | Direct Q141K rescue, urate flux, epithelial free exposure, and safety at the active exposure. |
| **Sulforaphane** | Cellular HDAC-activity or HDAC-protein signals exist; they are not isoform-resolved Q141K-rescue data (**In Vitro**; PMID 24441674 and cited cellular studies). | Comparable potency, Q141K trafficking, urate flux, compartment exposure, and safety. |
| **Allyl mercaptan** | Bulk HDAC activity was measured in Caco-2 nuclear extracts (**In Vitro**; [PMID 14976134](https://pubmed.ncbi.nlm.nih.gov/14976134/)). | Isoform causality, Q141K trafficking, urate flux, achieved intracellular exposure, and safety. |
| **Diallyl disulfide** | Bulk HDAC activity and histone-acetylation effects were reported in cellular systems (**In Vitro**; PMID 14976134). | Active material identity after metabolism, isoform causality, Q141K trafficking, urate flux, exposure, and safety. |
| **Phenethyl isothiocyanate** | HDAC1-protein changes were reported in colorectal-cell and rat-tumor models; this is not a biochemical HDAC IC50 or a transporter-rescue result (**In Vitro + Animal Model**; [PMID 31228495](https://pubmed.ncbi.nlm.nih.gov/31228495/)). | Direct target activity, Q141K trafficking, urate flux, epithelial exposure, and safety. |
| **Caffeic acid** | COMP-007 did not verify candidate-specific quantitative HDAC evidence adequate for this question. | The complete target, trafficking, flux, exposure, and safety chain. |
| **Ferulic acid** | Cellular histone-H3 hyperacetylation is consistent with altered acetylation biology but does not identify a causal HDAC isoform or Q141K effect (**In Vitro**; [PMID 27588384](https://pubmed.ncbi.nlm.nih.gov/27588384/)). | Direct target activity, Q141K trafficking, urate flux, exposure, and safety. |

## Sourcing and delivery

The relevant compartment is the intestinal epithelial cell, not merely the gut lumen. A defined compound, food-derived precursor, microbial metabolite, or engineered producer is useful only if the route delivers a characterized active material to the intracellular machinery for long enough to change surface ABCG2. Luminal abundance, low systemic bioavailability, and food occurrence do not establish that exposure.

For each route, measure material identity, free concentration, conversion products, epithelial uptake, exposure time, intestinal segment, barrier integrity, and systemic spillover. Chassis selection is downstream of those measurements; the hypothesis does not require yeast, koji, or any other production host.

## Discriminating experiment

First reproduce the Basseville control pattern with selected positive HDAC-inhibitor conditions and the reported non-rescuing valproate/HDAC6-selective contrasts. Then test the seven materials without a computational rank in a polarized intestinal model containing WT-only, Q141K-only, and WT/Q141K co-expression arms.

Measure total and apical-surface ABCG2, ABCG2-attributed basolateral-to-apical urate flux, intracellular exposure, viability, barrier integrity, and direct ABCG2 inhibition. Use PPARγ blockade to separate endogenous-ABCG2 induction from any Q141K-trafficking effect. A material advances only if the direct trafficking-plus-urate-flux result survives the inhibition and safety counterscreens. See [validation experiment §1.22](./validation-experiments.md#122-gut-compartment-hdac-directed-candidate-screen-for-q141k-abcg2-trafficking-rescue).
