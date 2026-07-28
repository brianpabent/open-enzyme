---
title: Gout Kill Chain — Target-First Delivery Analysis
date: 2026-07-27
tags:
  - gout
  - delivery
  - compartments
  - urate
  - nlrp3
  - resolution
related:
  - gout-pathophysiology.md
  - nlrp3-exploit-map.md
  - delivery-route-matrix.md
  - modality-chokepoint-matrix.md
  - uricase.md
  - complement-c5a-gout.md
status: comparison-surface
---

# Gout Kill Chain — Target-First Delivery Analysis

## The routing question

A gout mechanism is actionable only if an exact product can reach the compartment where that mechanism operates, on the required time scale, at an active exposure. This page starts with the target. [Delivery Route × Product Class](./delivery-route-matrix.md) provides the orthogonal product-first view.

Route, formulation, material, target, and disease phase must be qualified together. A successful route for one product does not validate another payload, and a failed configuration does not kill the target.

## Target–compartment map

| Kill-chain node | Primary compartment | Evidence anchor | Delivery problem that remains |
|---|---|---|---|
| Purine input and degradation | Gut lumen, liver, systemic circulation | Diet and host metabolism contribute purine substrate; exact contribution is context-dependent | Distinguish reduced input, altered absorption, and active degradation with mass balance |
| Xanthine oxidoreductase | Liver and other expressing tissues | Approved small-molecule inhibitors establish the node clinically | Exact exposure, metabolites, selectivity, and safety remain product-specific |
| Renal urate reabsorption/secretion | Proximal tubule | Clinical transporter drugs establish that renal urate handling is actionable | Reach the correct membrane/cell while avoiding off-target transport effects |
| Intestinal urate secretion and degradation | Intestinal epithelium and lumen | ABCG2 physiology establishes intestinal urate export; [ALLN-346 Study 201](https://clinicaltrials.gov/study/NCT04987242) reached human testing, but it does not by itself validate this project’s compartmental mechanism or configuration (**Clinical Trial registry**) | Place active material where secreted urate is accessible; quantify substrate flux and competing loss |
| Circulating urate degradation | Blood | Systemic uricase products establish the node | Control immunogenicity, infusion reactions, persistence, and peroxide for the exact product |
| Crystal burden | Synovial fluid, cartilage, tophus | MSU crystals are the inflammatory substrate | Achieve sufficient local urate/crystal effect without tissue injury; local enzyme delivery remains experimental |
| Complement-associated priming | Plasma, synovial fluid, recruited leukocytes | Defined in-vitro, animal, and clinical-sample evidence links complement/C5a to gout-relevant inflammation | Establish when and where complement is causal rather than a correlated amplifier |
| NLRP3 activation | Macrophages and other responsive cells | Multiple preclinical and selected clinical inhibitor precedents | Demonstrate cell exposure and exact target engagement, not cytokine suppression alone |
| Pyroptotic execution | Inflammasome-active cells and local tissue | GSDMD/caspase biology supplies a mechanistic node | Avoid confusing delivery through damaged membranes with safe selectivity |
| Neutrophil recruitment and resolution | Synovium and inflammatory exudate | Gout resolution involves neutrophil behavior, mediator clearance, and aggNET-associated processes | Preserve host defense while accelerating termination of sterile inflammation |
| Pain signaling | Peripheral nociceptors and neuroimmune interface | RvD1 mouse work supplies an exact preclinical neuroimmune lead | Separate analgesia, inflammatory target engagement, and structural recovery |

## Route gates by disease phase

### Intercritical urate control

The exposure may need to be sustained, but chronic tolerability and adherence become dominant. Gut-lumen uricase, transporter modulation, systemic uricase, and production-limiting strategies are separate tracks. Compare them by measured urate mass balance and product-specific safety, not by chassis preference.

### Acute crystal inflammation

Onset and synovial or immune-cell exposure matter. A preclinical
anti-inflammatory mechanism is not an acute-flare route. The [KPV](./kpv-peptide.md)
and [BPC-157](./bpc-157.md) evidence homes do not establish a gout-qualified
route; route selection remains an experiment rather than a conclusion from
adjacent models.

### Resolution and repair

SPMs, neutrophil-resolution mechanisms, and repair leads act on different stages. Exact RvD1 and MaR1 have direct MSU animal evidence; EPA and DHA are precursors and require measured conversion. BPC-157 is an adjacent repair lead, not a validated resolution or gout intervention.

## Measurements that travel across tracks

Every route experiment should report:

1. Exact product identity, purity, stability, and biological activity.
2. Concentration–time in the intended compartment, including free rather than nominal exposure where relevant.
3. Target engagement upstream of the final disease marker.
4. A matched safety panel for the route and compartment.
5. A negative-control route or formulation when feasible.
6. Advance, redirect, and kill thresholds fixed before result interpretation.

> **Research conjecture — Local multi-node control without systemic overreach**{ .research-conjecture-label }
>
> **Grounded premises:** MSU crystals, complement-associated priming, macrophage inflammasome activity, neutrophil recruitment, and nociceptor signaling can coexist in the inflamed joint (**Clinical sample + In Vitro + Animal Model**; [gout pathway map](./gout-pathophysiology.md), [complement evidence](./complement-c5a-gout.md), and [RvD1 evidence](./spm-resolution-pathway.md)). Local delivery can alter concentration and residence relative to systemic exposure (**Mechanistic Extrapolation**).
>
> **Novel leap:** No direct evidence establishes that one exact local formulation can safely alter two or more of these nodes with a better therapeutic window than matched systemic exposure.
>
> **Why it matters:** A local product could exploit the spatial concentration of the gout kill chain while reducing unnecessary whole-body exposure.
>
> **Discriminating observation:** In a joint-relevant system, compare matched local and systemic concentration–time profiles while measuring crystal or urate change, complement, macrophage target engagement, neutrophil behavior, pain-proxy signaling, tissue injury, and systemic escape.

## Decision rule

Advance the smallest defensible claim: exact material × exact route × exact compartment × exact model. Redirect when the target is sound but exposure fails. Kill only the configuration or causal premise the experiment actually tested.

This is Phase 0 research, not treatment or delivery guidance.
