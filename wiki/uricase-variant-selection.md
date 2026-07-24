---
title: "Uricase Variant Selection for Oral Delivery"
date: 2026-04-21
tags: [uricase, enzyme-selection, oral-delivery, protein-engineering, gout]
related: [uricase.md, engineered-yeast-uricase-proposal.md, protein-engineering-strategy.md, validation-experiments.md]
---

# Uricase Variant Selection for Oral Delivery

No uricase sequence is currently the default oral therapeutic. Parent-enzyme choice depends on the topology and reaction-site conditions that pass [validation experiment §1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial). Sequence, host, formulation, and delivery route must therefore be compared as interacting variables rather than collapsed into a universal rank.

## Evidence boundary

The corpus supports several reasons to keep multiple candidates in the screen:

| Candidate | Directly supported prior | What the prior does not establish |
|---|---|---|
| *Aspergillus flavus* UOX (Q00511) | Recombinant manufacturing and clinical systemic-use precedent through rasburicase; extensive biochemical and engineering literature. **Clinical use + In Vitro.** | Oral retained activity, reaction-site access, peroxide control, immunogenicity in the proposed format, or superiority in yeast/koji. |
| *Candida utilis* UOX (P78609) | Parent-enzyme precedent in ALLN-346 and other uricase programs; disclosed engineered sequence candidates can be tested. **Clinical Trial + In Vitro.** | Transfer of an ALLN-346 result to a different construct, host, topology, or formulation; wild-type GI performance. |
| *Vibrio vulnificus* UOX | Engineered-*S. boulardii* expression and animal-model precedent reported by Gao et al. 2025. **In Vitro + Animal Model.** | Human exposure, superiority outside that construct, or performance in koji. |
| Other bacterial, fungal, yeast, or plant UOX sequences | Potential diversity in activity, pH response, folding, and stability. **Mechanistic Extrapolation until measured.** | Any categorical GI-stability, expression, immunogenicity, or delivery advantage. |

Clinical-program parent choice is useful prior information, not a head-to-head enzyme comparison. Systemic manufacturing success likewise does not predict oral reaction-site performance.

## Selection contract

### Gate 1 — sequence and provenance

- Confirm the exact sequence, accession, length, construct boundaries, and disclosed mutations.
- Distinguish wild type from engineered derivatives in every assay and result.
- Record the evidence behind each mutation; a computational suggestion is not a validated stability change.

### Gate 2 — matched purified-enzyme characterization

Measure candidates under the same assay conditions across the pH, substrate, oxygen, and temperature ranges relevant to the intended compartment. Report activity units, Km or an appropriate substrate-response curve, tetramer/oligomer state, aggregation, and peroxide generation. Favorable-assay specific activity is not an oral-dose calculation.

### Gate 3 — matched topology screen

Use [§1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial) to compare intracellular/release, surface-displayed, secreted, and cell-free configurations as applicable. Measure active UOX at the reaction site, substrate removal over time, oxygen dependence, peroxide, access, and persistence. Do not choose a topology from signal-peptide heuristics, expression analogies, or a static urate budget.

### Gate 4 — processing and GI retention

For configurations that pass Gate 3, measure retained activity after the actual production, drying, storage, gastric, intestinal, and formulation steps. Report failure modes rather than converting a survival percentage into a human dose.

### Gate 5 — advance the smallest supported claim

A candidate advances only within the topology and conditions in which it was measured. Animal escalation follows [§1.36](./validation-experiments.md#136-luminal-urate-antioxidant-loss--uox-h2o2-safety-assay); it is not the first validator of a sequence ranking. Human-dose, serum-urate, and product-format conclusions require later evidence.

## Current candidate set

Retain *A. flavus* and *C. utilis* as well-documented initial comparators. Add the *V. vulnificus* construct when its sequence and assay context can be reproduced. Other candidates enter only when they add a defined property or diversity axis that can be tested under the same protocol.

[comp-010](./etc/experiments/comp-010-cassette-compatibility/) and [comp-011](./etc/experiments/comp-011-c-utilis-uricase-cassette-compatibility/) are invalidated, non-runnable tombstones. Their codon, cysteine-risk, processing, secretion-burden, and overall-risk conclusions do not survive. Wild-type Q00511, wild-type P78609, and any patent-mutation proxy remain distinct sequence objects that require exact CDS definition and matched expression, localization, assembly, activity, and safety measurements.

## Decision table

| Result | Action |
|---|---|
| One sequence retains more active UOX under a matched, relevant topology without worsening peroxide or safety gates | Advance that sequence for that topology; retain a control sequence until reproduced. |
| Rankings change by topology or compartment | Keep topology-specific candidates; do not force a global winner. |
| Expression differs but delivered active UOX does not | Treat expression yield as non-limiting within that comparison; do not infer dose sufficiency. |
| No candidate clears the reaction-site and safety gates | Stop optimizing the current UOX configuration and test another delivery architecture or urate-disposal mechanism. |

## Falsification boundary

The variant-selection hypothesis fails if sequence-level optimization cannot produce reproducible retained activity at the intended reaction site, or if peroxide, access, persistence, or safety constraints dominate across candidates. That outcome retires or redirects the affected UOX configuration; it does not hold up the Open Enzyme portfolio.

## Related

- [Uricase](./uricase.md)
- [Gut-lumen sink](./gut-lumen-sink.md)
- [Protein-engineering strategy](./protein-engineering-strategy.md)
- [Engineered yeast UOX proposal](./engineered-yeast-uricase-proposal.md)
- [Validation experiments](./validation-experiments.md)
