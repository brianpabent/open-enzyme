---
title: Delivery Route × Product Class Matrix
date: 2026-07-27
tags:
  - delivery
  - formulation
  - compartment
  - pharmacokinetics
  - portfolio
related:
  - gout-kill-chain-delivery-routes.md
  - modality-chokepoint-matrix.md
  - uricase.md
  - peptide-gout-addendum.md
  - engineered-lbp-chassis.md
status: comparison-surface
---

# Delivery Route × Product Class Matrix

## Decision rule

Route is a property of an exact product, not a compound name or a production chassis. A route is qualified only when the exact material reaches the intended compartment at an active exposure with acceptable local and systemic safety.

This page compares delivery questions. It does not rank tracks, certify availability, or transfer evidence between products.

| Product class | Evidence anchor | Open delivery question | Required measurement before qualification |
|---|---|---|---|
| Small molecule | Multiple oral and systemic precedents exist, but each molecule has its own absorption, distribution, metabolism, and elimination | Can a formulation reach renal transporter, circulating immune, or synovial targets on the required time scale? | Exact-product PK, free target-site exposure, target engagement, metabolites, safety |
| Short peptide | KPV has PepT1-related uptake evidence in named intestinal-cell systems; other peptides have separate adjacent evidence | Is the intended action luminal/epithelial, systemic, or local to a joint? | Identity, proteolytic stability, route-specific PK, target-compartment exposure, activity |
| Recombinant protein or enzyme | Systemic uricase products and an oral gut-lumen uricase trial provide product-specific precedents | Can an enzyme reach urate in the selected compartment while controlling peroxide, immunogenicity, and loss of activity? | Active enzyme concentration, urate flux, oxygen, peroxide, catalase capacity, immune and tissue safety |
| Live engineered organism | Oral delivery is a plausible access route for gut-local action; chassis survival and containment remain product-specific | Can the organism or released payload act at the relevant intestinal site without requiring systemic exposure? | Viability and containment, spatial residence, substrate access, payload release/activity, microbiome and safety readouts |
| Nanoparticle or depot | Formulations can alter distribution and residence, but a carrier precedent does not transfer to a new payload | Does the carrier improve target-site exposure rather than only total exposure? | Payload integrity, release kinetics, biodistribution, cell uptake, target engagement, carrier toxicity |
| RNA or gene-regulation product | Delivery determines which cell type is perturbed | Can the construct reach the relevant renal, hepatic, immune, or synovial cell without off-target expression? | Cell-type biodistribution, knockdown/expression, duration, innate-immune activation, reversibility and safety |

## Route-specific questions

### Enteral

Enteral delivery is relevant when the intended action is luminal, epithelial, or achievable after measured absorption. Gastric survival, intestinal location, food matrix, microbiome metabolism, epithelial transport, and first-pass metabolism must be measured for the exact product.

- KPV: the current evidence supports a PepT1-related intestinal-cell lead. It does not qualify oral systemic, buccal, intranasal, subcutaneous, or intra-articular delivery.
- BPC-157: no route is qualified for gout by the reviewed source packet.
- Oral uricase: ALLN-346 is an exact-product clinical precedent for gut-lumen exposure; it does not qualify an engineered organism or another purified enzyme.
- Live organisms: ingestion is only the start of the route. Activity requires survival or release, correct intestinal location, substrate contact, and containment.

### Systemic

Intravenous, subcutaneous, intramuscular, and absorbed enteral products cannot be grouped together. Each produces a different concentration–time and immune-exposure profile.

- Systemic uricase precedents qualify only their exact products and protocols.
- No reviewed evidence qualifies systemic KPV or BPC-157 for gout.
- A nanoparticle or conjugate must demonstrate target-cell delivery for its exact payload; platform success elsewhere is not enough.

### Local or regional

Intra-articular, transdermal, microneedle, and other local routes may reduce total exposure while increasing local concentration, but they introduce separate tissue-safety, retention, clearance, sterility, and procedure questions. A local route is not automatically safer and does not reach renal or gut targets.

> **Research conjecture — Local uricase with reaction-site peroxide control**{ .research-conjecture-label }
>
> **Grounded premises:** Uricase converts urate while generating hydrogen peroxide (**Biochemical evidence**; [uricase](./uricase.md)). Local delivery can change residence and tissue exposure relative to a systemic product (**Mechanistic Extrapolation**; exact-product qualification still required).
>
> **Novel leap:** No direct evidence establishes that a locally retained exact uricase–catalase configuration can dissolve or deplete joint urate while keeping peroxide and immune injury below a useful boundary.
>
> **Why it matters:** A successful configuration could attack the crystal compartment without requiring chronic systemic enzyme exposure.
>
> **Discriminating observation:** In a joint-relevant ex-vivo system, measure active uricase and catalase, urate and crystal change, oxygen, peroxide, tissue injury, residence, and immune activation for matched single and combined arms.

## Portfolio routing gates

1. Name the exact material and intended compartment.
2. Define the exposure and target-engagement threshold before selecting a route.
3. Measure route-specific failure modes rather than importing generic bioavailability.
4. Compare routes only under matched biological endpoints.
5. Advance, redirect, or kill the exact material–route pair; do not kill the whole modality from one failed configuration.

See [Gout kill-chain delivery routes](./gout-kill-chain-delivery-routes.md) for the target-first view.
