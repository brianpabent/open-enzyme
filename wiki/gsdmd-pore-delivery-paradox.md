---
title: GSDMD Pore Self-Delivery Hypothesis
tags:
  - gsdmd
  - gasdermin
  - pyroptosis
  - drug-delivery
  - nlrp3
  - cp6b
related:
  - nlrp3-exploit-map.md
  - gout-kill-chain-delivery-routes.md
  - kpv-peptide.md
  - kpv-gsdmd-pore-influx-computational.md
  - validation-experiments.md
sources:
  - "Sborgi L et al. EMBO J 2016;35(16):1766-1778 (PMID 27418190; DOI 10.15252/embj.201694696)"
  - "Xia S et al. Nature 2021;593:607-611 (PMID 33883744; DOI 10.1038/s41586-021-03478-3)"
  - "bioRxiv 2025; DOI 10.1101/2025.02.11.637513"
---

# GSDMD Pore Self-Delivery Hypothesis

Gasdermin D (GSDMD) pores breach the plasma membrane of a pyroptotic cell. The engineering opportunity is to test whether that transient breach can become a state-dependent entry route for an extracellular, otherwise membrane-impermeant payload with a still-actionable intracellular target.

This is a physical-delivery hypothesis, not a qualified therapeutic route.

## Observed basis

Activated inflammatory caspases cleave GSDMD, and its N-terminal fragments assemble into membrane pores. Sborgi et al. measured rings with a mean inner diameter of 21.2 ± 5.6 nm by AFM (n=164; **In Vitro / structural**, [PMID 27418190](https://pubmed.ncbi.nlm.nih.gov/27418190/)). Xia et al. resolved a 33-subunit pore with an inner diameter of approximately 21.5 nm and reported a predominantly negatively charged conduit with charge-dependent cargo behavior (**In Vitro / structural**, [PMID 33883744](https://pubmed.ncbi.nlm.nih.gov/33883744/)).

A 2025 preprint reports increased entry of the membrane-impermeant caspase-inhibitor configurations it studied in GSDMD-pore-expressing cells relative to intact-membrane controls (**In Vitro — preprint**, [DOI 10.1101/2025.02.11.637513](https://doi.org/10.1101/2025.02.11.637513)). Its exact compounds, cell systems, exposures, pore states, and time windows bound that observation.

Pore diameter alone does not establish passage. Charge, conformation, binding, hydrodynamic behavior, pore abundance, pore lifetime, and the extracellular boundary concentration can all change transport. KPV and larger Open Enzyme payloads are therefore candidates for exact-payload testing, not members of a validated deliverable class.

## Why gout makes the question interesting

In a gout-relevant inflammasome sequence, caspase-1 activation precedes GSDMD cleavage and pore formation. A pore could therefore create access to an intracellular target only after the inflammatory program has begun. Whether enough actionable biology remains at that point depends on payload influx, target activity, IL-1β release, membrane repair or lysis, and extracellular exposure in the same cell and time window. No current result establishes that ordering as therapeutically sufficient.

The cleanest first probe is not a known transporter substrate. A membrane-impermeant payload with no competing uptake route and a downstream target would separate pore-dependent entry from ordinary cellular uptake. KPV is useful as a confounded comparator because its PepT1 route can be manipulated, but it cannot by itself qualify the platform.

## COMP-042: KPV transport prior

[COMP-042](./kpv-gsdmd-pore-influx-computational.md) is **YELLOW — A2 unresolved**.

- **A1:** against a 10 nM extracellular cell-assay proxy, the modeled passive pore contribution is GREEN for the intra-articular design space, YELLOW for subcutaneous, and RED for oral. These are engineering states, not target-engagement or efficacy results.
- **Pore timing:** the central modeled time constant is 2.17 seconds, but the grid is not uniformly at equilibrium. At 10 pores over 60 seconds, the retained fraction is 0.749. Lifetime is low-sensitivity in much of the tested space, not universally irrelevant.
- **A2:** the route concentration × Km grid retains favorable heuristic corners. Intra-articular crosses the ≥3× line in 2/9 moderate-PepT1 and 1/9 high-PepT1 cases; absent and low scenarios cross in all nine cases for every route.
- **Empirical gap:** the healthy-cell equation and PepT1 scenarios are unvalidated, synovial-macrophage PepT1 function is unmeasured, and concurrent PepT1 transport in the pore-forming cell is excluded. KPV-specific selectivity is unresolved, not falsified.
- **Timing boundary:** KPV is framed upstream of GSDMD pore formation. The model cannot determine whether enough relevant activity remains after pore opening.

> **Research conjecture — transporter-orphan downstream payload**{ .research-conjecture-label }
>
> **Grounded premises:** GSDMD pores admit the otherwise membrane-impermeant inhibitor configurations studied in a cell model (**In Vitro — preprint**; [DOI 10.1101/2025.02.11.637513](https://doi.org/10.1101/2025.02.11.637513)). [COMP-042](./kpv-gsdmd-pore-influx-computational.md) supports substantial passive entry for a KPV-sized solute in much of its declared model space (**Mechanistic Extrapolation**) but cannot resolve KPV/PepT1 selectivity.
>
> **Novel leap:** A membrane-impermeant payload with no competing transporter and a target still actionable after pore formation could create a useful pore-specific exposure difference. No direct evidence tests this exact design in gout.
>
> **Why it matters:** The pore could become a state-dependent delivery gate rather than only an inflammatory exit route.
>
> **Discriminating observation:** In matched pore-on/off cells, a prequalified transporter-orphan tracer must clear a prespecified intracellular-uptake margin, track verified pore state, and lose the differential under a pore-blocking control.

## Empirical gate

[Validation §1.32](./validation-experiments.md#132-gsdmd-pore-self-delivery--matched-uptake-and-selectivity-probe) separates two experiments:

1. A prequalified transporter-orphan, membrane-impermeant tracer tests the pore-on versus pore-off physical-delivery difference.
2. KPV in a pore-on/off × PepT1-on/off design estimates the competing transporter contribution without making an efficacy claim.

GREEN or RED is bounded to the exact tracer, concentration, cell model, pore induction, and time window. A successful tracer result would nominate exact downstream payloads for their own transit, retention, target-engagement, and safety tests. A failed configuration would not refute every payload or every GSDMD-pore state.

## Open measurements

- Simultaneous payload influx, target activity, and IL-1β efflux after verified pore formation
- Exact-payload permeability as a function of size, charge, conformation, and extracellular concentration
- Pore abundance and open lifetime in primary human synovial macrophages
- Functional PepT1 and matched KPV accumulation in resting and MSU-activated synovial macrophages
- Intracellular payload stability and retained activity after transit

Until those measurements exist, GSDMD pore self-delivery remains a testable engineering conjecture rather than a gout intervention.
