---
title: "Uricase Thermal/pH Stability in Shio-Koji — Computational Analysis (comp-002)"
date: 2026-05-16
tags: [uricase, shio-koji, thermal-stability, tetramer, computational]
related:
  - computational-experiments.md
  - validation-experiments.md
  - uricase.md
  - uricase-variant-selection.md
  - uricase-protease-stability-computational.md
  - engineered-koji-protocol.md
sources:
  - "Imani & Shahmohamadnejad 2017, 3 Biotech 7:201, DOI:10.1007/s13205-017-0841-3, PMID:28667645 — WT *A. flavus* uricase Tm = 27°C, t½ = 38 min at 40°C"
  - "Rezaeian Marjani et al. 2020, Iran J Biotechnol 18:e2662, DOI:10.30498/IJB.2020.2662, PMID:33850949 — disulfide-engineered optimum-activity-temperature and 40°C half-life comparison"
  - "Retailleau et al. 2004, Acta Cryst D60:453, PDB 1R56 — tetramer interface footprint"
  - "UniProt Q00511 — homotetramer (ECO:0000269|PubMed:16478683); zero native DISULFID features"
status: retired-invalid-model
---

# Uricase Thermal/pH Stability in Shio-Koji — Computational Analysis (comp-002)

The engineering weakness is loss of assembled, active *A. flavus* uricase during a multi-day shio-koji process. COMP-002 does not determine whether that happens.

## Current evidence boundary

- Wild-type *A. flavus* uricase had a reported melting temperature of 27°C and an approximately 38-minute half-life at 40°C in the Imani 2017 study (**In Vitro**). Those measurements establish thermal sensitivity under their assay conditions; they do not predict retention during a 7–14-day ferment.
- UniProt and structural records identify Q00511 as a homotetramer (**In Vitro** structural/biochemical record). Whether the exact produced material remains assembled and active through the intended process is unmeasured.
- Rezaeian Marjani 2020 reported engineered variants with a higher optimum-activity temperature and longer half-life under thermal stress (**In Vitro**). The study does not establish the size of a melting-temperature shift or performance in shio-koji.
- COMP-001 supplies only a fixed-filter and pLDDT-context inventory. Protease survival remains a separate empirical question.

The retired COMP-002 model used an unswept refolding exponent, hard-coded interface weights, arbitrary category boundaries, and pLDDT as a physical interface/integrity proxy. Every quantitative result, failure-mode ranking, and engineering recommendation is invalid. The [COMP-002 tombstone](./etc/experiments/comp-002-uricase-shio-koji-thermal-stability/) is non-runnable; Git retains the retired implementation.

> **Research conjecture — sub-Tm process attrition may still limit Q00511**{ .research-conjecture-label }
>
> **Grounded premises:** Wild-type *A. flavus* uricase shows thermal sensitivity in purified assays (**In Vitro**; Imani 2017, PMID 28667645). The [§1.10 process specification](./validation-experiments.md#110-heterologous-uricase--lactoferrin-stability-in-shio-koji-salt-protease-ferment) defines retention of assembly and activity through the multi-day matrix as a project requirement (**Mechanistic Extrapolation**). The current corpus contains no direct joint measurement of salt, pH, matrix, proteolysis, and repeated exposure for the exact construct.
>
> **Novel leap:** Even when the process temperature is below the reported melting temperature, cumulative process exposure might reduce intact tetramer and specific activity enough to become a practical bottleneck. No direct study has tested that multi-factor, multi-day failure mode.
>
> **Why it matters:** A confirmed thermal/assembly bottleneck would justify variant or process engineering; a negative result would keep attention on other delivery constraints.
>
> **Discriminating observation:** Under the exact process matrix, measure total protein, intact monomer, tetrameric assembly, and specific activity at day 0, 7, and 14 across the prespecified temperature and pH range.

## Experiment that advances or redirects the track

Run [validation §1.10](./validation-experiments.md#110-heterologous-uricase--lactoferrin-stability-in-shio-koji-salt-protease-ferment) on the exact construct and process. Native-PAGE or another validated assembly readout can distinguish loss of tetramer from loss of abundance; specific activity separates intact protein from functional enzyme. Measure ferment temperature and pH rather than importing a single nominal condition.

If wild type loses assembly or activity reproducibly, compare the exact variant and process arms under the same readouts. A favorable result advances only that configuration. Failure redirects the variant, process, formulation, or delivery track without rejecting uricase or the wider project.

## Cross-references

- **Wet-lab gate:** [`validation-experiments.md` §1.10](./validation-experiments.md) (uricase + lactoferrin shio-koji stability); [§1.16](./validation-experiments.md) (candidate disulfide variant only if the measured failure mode justifies it).
- **Sister analysis (protease):** [`uricase-protease-stability-computational.md`](./uricase-protease-stability-computational.md) (comp-001, proxy only). The two computations do not identify a dominant failure mode: both protease survival and retained activity under the complete ferment conditions require direct measurement.
- **Tracking index:** [`computational-experiments.md`](./computational-experiments.md)
- **Platform context:** [`uricase.md`](./uricase.md), [`uricase-variant-selection.md`](./uricase-variant-selection.md), [`engineered-koji-protocol.md`](./engineered-koji-protocol.md)
