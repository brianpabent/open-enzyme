---
title: "EcN Folding Capacity for DAF and Lactoferrin (comp-043)"
date: 2026-07-13
tags: [complement, DAF, CD55, lactoferrin, disulfide, DsbA, DsbC, EcN, LBP, folding-feasibility, computational]
related:
  - chaperone-orthogonal-stacking.md
  - engineered-lbp-chassis.md
  - complement-c5a-gout.md
  - computational-experiments.md
  - validation-experiments.md
sources:
  - "UniProt P08174 (DAF / CD55)"
  - "UniProt P02788 (human lactoferrin / LTF)"
  - "Ward PP et al. Nat Biotechnol 1992;10:784-789 (PMID 1368268)"
  - "Sun XL et al. Acta Crystallogr D 1999;55:403-407 (PMID 10089347)"
status: retired-invalid-model
---

# EcN Folding Capacity for DAF and Lactoferrin (comp-043)

Can an exact DAF or lactoferrin construct reach its native, functional state through an EcN expression and secretion route?

COMP-043 does not answer that question. Its disulfide-capacity bands, connectivity weights, protease scores, glycan assumptions, and composite outputs were uncalibrated. The numerical ordering, viability crossover, chassis comparison, and experiment priority are invalid. The [COMP-043 tombstone](./etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/) is non-runnable; Git retains the retired implementation and outputs.

## Evidence boundary

DAF and lactoferrin are disulfide-containing proteins with distinct native folds (**In Vitro** structural and annotation records; UniProt P08174 and P02788). That makes native-fold attainment a necessary measurement for each exact EcN construct. This page does not reproduce historical feature counts; reverify any count against the current primary record before using it as a design input.

The prior scan did not identify a calibrated DsbA/DsbC capacity rule that converts disulfide architecture into expression success for these exact secreted configurations (**Mechanistic Extrapolation**). Cytoplasmic oxidizing-strain precedents do not establish the capacity of the proposed periplasmic route.

> **Research conjecture — folding-system capacity may become a configuration-specific bottleneck**{ .research-conjecture-label }
>
> **Grounded premises:** DAF and lactoferrin require specific disulfide-connected native folds (**In Vitro**; [UniProt P08174](https://www.uniprot.org/uniprotkb/P08174/entry), [UniProt P02788](https://www.uniprot.org/uniprotkb/P02788/entry), and PMID 10089347). EcN route-specific expression, native-fold attainment, secretion, stability, and retained function have not been measured for the proposed constructs.
>
> **Novel leap:** One or more exact EcN payload configurations may exceed the useful capacity of the baseline folding route, and DsbC co-expression may rescue some—not necessarily all—of that failure. No direct evidence establishes this for the proposed constructs.
>
> **Why it matters:** A configuration-level result can redirect construct, secretion route, folding support, or chassis without declaring the payload class viable or infeasible.
>
> **Discriminating observation:** Compare baseline and DsbC-co-expression arms for each exact construct. Measure expression, secretion, native disulfide connectivity or validated native-fold proxy, aggregation, route-relevant stability, and retained function. Advance only the configuration that meets prespecified functional and quality gates.

The result does not choose EcN or koji. A negative result kills only the tested construct × route × folding-support configuration.

Related: [validation §1.25](./validation-experiments.md#125-daf-lbp-route-gate) · [engineered LBP chassis](./engineered-lbp-chassis.md) · [complement portfolio](./complement-c5a-gout.md)
