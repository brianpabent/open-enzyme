---
title: "Cordycepin cns1+cns2 Route: Evidence and Experimental Gate"
date: 2026-05-14
tags:
  - cordycepin
  - cns1
  - cns2
  - aspergillus-oryzae
  - metabolic-burden
  - research-conjecture
  - comp-023
related:
  - computational-experiments.md
  - chaperone-orthogonal-stacking.md
  - validation-experiments.md
sources:
  - "Jeennor S et al. Microb Cell Fact. 2023. PMID 38071331; DOI 10.1186/s12934-023-02261-5."
status: deprioritized; COMP-023 invalidated
---

# Cordycepin *cns1+cns2* Route

Jeennor et al. directly demonstrated heterologous cordycepin production from *cns1+cns2* expression in *Aspergillus oryzae* under their tested fermentation configuration (**In Vitro**, [PMID 38071331](https://pubmed.ncbi.nlm.nih.gov/38071331/)). This makes the route technically relevant if engineered cordycepin production becomes a portfolio priority.

COMP-023 supplies no burden, flux, yield, breakpoint, feasibility, product, or multi-cassette result. Its comparator and units were not fit for the decision: it converted source-reported batch-average productivity into a fixed continuous mmol/gDW/h demand using an assumed biomass density without time-resolved, condition-matched calibration. It also used unverified reaction assumptions and an artificial export bound, mishandled scenario boundaries, and reported separately optimized capacity maxima as yields. The executable artifact is retired.

> **Research conjecture — cytosolic cordycepin synthesis may be ER-orthogonal**{ .research-conjecture-label }
>
> **Grounded premises:** Jeennor et al. demonstrated *cns1+cns2*-enabled cordycepin production in *A. oryzae* (**In Vitro**; source: PMID 38071331). Secreted-protein payloads depend on ER folding and trafficking (**Mechanistic Extrapolation**; source: [chaperone-stacking evidence](./chaperone-orthogonal-stacking.md)).
>
> **Novel leap:** If the functional *cns1+cns2* route and its relevant intermediates remain outside the ER in the intended strain, the cassette might add cordycepin production without directly competing for ER folding capacity. No direct evidence establishes that orthogonality.
>
> **Why it matters:** A clean result would preserve a small-molecule route that could coexist with a secreted-protein payload if the track later becomes decision-relevant.
>
> **Discriminating observation:** Compare four otherwise-isogenic *A. oryzae* strains—matched empty-vector control, *cns1+cns2* alone, one exact secreted-protein cassette alone, and both cassettes—using matched integration copy number and one fermentation protocol. Measure cordycepin identity and production, secreted-payload abundance and retained function, biomass/growth, and a prespecified ER-stress/cell-state panel. Advance the orthogonality conjecture only if the dual strain produces both products while the secreted-payload and ER-stress readouts remain within preregistered noninferiority limits relative to the secreted-payload-only strain.

The engineered-cordycepin track is currently deprioritized. Reopen it only if portfolio value justifies the isogenic experiment; do not substitute another unconstrained FBA.

The [COMP-023 tombstone](./etc/experiments/comp-023-cns1-cns2-metabolic-burden/) preserves the exact invalidation boundary.
