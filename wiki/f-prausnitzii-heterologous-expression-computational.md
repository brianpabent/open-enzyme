---
title: "*Faecalibacterium* Engineering Questions (comp-008)"
date: 2026-05-16
tags: [computational-experiment, engineered-lbp-chassis, faecalibacterium, heterologous-expression, butyrate]
related:
  - engineered-lbp-chassis.md
  - hypotheses/H02-engineered-lbp-thesis.md
  - uricase.md
  - lactoferrin.md
  - complement-c5a-gout.md
sources:
  - "Sheridan 2023 Microbiome Research Reports doi:10.20517/mrr.2022.13"
  - "Martín 2023 FEMS Microbiol Rev doi:10.1093/femsre/fuad039"
  - "Quévrain 2016 Gut doi:10.1136/gutjnl-2014-307649"
  - "Breyner 2017 Front Microbiol doi:10.3389/fmicb.2017.00114"
  - "Sakamoto 2022 IJSEM doi:10.1099/ijsem.0.005379"
status: retired-invalid-model
---

# *Faecalibacterium* Engineering Questions (comp-008)

COMP-008 does not rank payloads or establish *Faecalibacterium* as a tractable chassis. Its hard-coded scores, ranges, category thresholds, roadmap, and host-safety rationales were uncalibrated. The [COMP-008 tombstone](./etc/experiments/comp-008-f-prausnitzii-heterologous-expression/) is non-runnable; Git retains the retired artifact.

The artifact did correctly separate CR1 P17927 from DAF/CD55 P08174. It did not validate a specific CR1 fragment, lactoferrin construct, uricase topology, transformation method, secretion route, or native-pathway intervention.

> **Research conjecture — native-pathway intervention as one configuration question**{ .research-conjecture-label }
>
> **Grounded premises:** *Faecalibacterium* is a butyrate-producing gut commensal candidate, while the cited MAM studies used engineered *Lactococcus lactis* as a delivery workaround rather than demonstrating the proposed *Faecalibacterium* engineering route (**In Vitro / Animal Model** precedent; DOI 10.1136/gutjnl-2014-307649 and DOI 10.3389/fmicb.2017.00114). The exact transformation, expression, product-flux, colonization, and exposure performance of the proposed strain configuration is unmeasured.
>
> **Novel leap:** If a reproducible genetic entry point exists, a bounded native-pathway intervention might change local butyrate exposure without requiring a secreted heterologous protein. No direct evidence establishes that engineered configuration, and this does not make it preferable to other payload or chassis questions.
>
> **Why it matters:** A native-pathway result would test one mechanistically distinct use of the chassis without declaring it the project or assigning it priority.
>
> **Discriminating observation:** In one exact strain, demonstrate stable transformation and reporter expression, then compare a prespecified native-pathway intervention with an isogenic control for product flux, growth, stability, colonization-relevant fitness, and epithelial exposure. This test is independent of the separate uricase, lactoferrin, and CR1 configuration questions.

Uricase, lactoferrin, and CR1 remain separate configuration-level questions. Oxygen access, native folding, secretion, retained function, colonization density, and delivered exposure must be measured for the exact construct and compartment; COMP-008 supplies no ordering among them.

Related: [engineered LBP chassis](./engineered-lbp-chassis.md) · [H02](./hypotheses/H02-engineered-lbp-thesis.md) · [validation §1.14](./validation-experiments.md#114-butyrate-abcg2-rescue-in-q141k-epithelial-cells)
