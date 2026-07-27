---
title: "Gout Weakness × Intervention Route Matrix"
date: 2026-05-05
tags:
  - intervention-routes
  - chokepoints
  - portfolio
  - falsification
related:
  - nlrp3-exploit-map.md
  - gout-pathophysiology.md
  - delivery-route-matrix.md
  - chassis-pending-interventions.md
  - purine-degrading-bacteria.md
  - validation-experiments.md
sources:
  - "Evidence dossiers linked in each row"
status: published
---

# Gout Weakness × Intervention Route Matrix

## Scope

This matrix starts with exploitable weaknesses in urate production, disposal, crystallization, and inflammation, then asks which intervention routes can test each weakness. A route is not a project identity, product recommendation, or priority by itself.

Cells summarize evidence and the next falsification gate. They do not establish dose, access, clinical sufficiency, additivity, regulatory status, market fit, or a winning chassis.

## Evidence key

| State | Meaning |
|---|---|
| **Clinical** | Human intervention evidence for the stated mechanism and scope |
| **Animal** | In-vivo evidence; human translation unresolved |
| **In Vitro** | Cell, biochemical, tissue, or construct evidence |
| **Mechanistic Extrapolation** | Composed or adjacent mechanism requiring direct validation |
| **Open** | A testable route with no decision-grade evidence yet |

## Matrix

| Intervention route | Primary gout weakness it can test | Current boundary | Next discriminating gate |
|---|---|---|---|
| Established small molecules or biologics | XO, URAT1, IL-1, microtubule/ASC, 5-LOX, complement, systemic UOX | Clinical evidence is compound- and indication-specific; approval elsewhere does not establish gout use for a repurposing candidate | Verify gout-specific exposure, target engagement, safety, and outcome in an appropriate controlled study |
| Natural compounds or characterized native materials | XO, transporter expression, NLRP3 priming/assembly, resolution pathways | Mostly In Vitro or Animal; material identity and achievable exposure often limit translation | Test exact material, free exposure, target-proximal readout, safety, and gout-relevant endpoint |
| Peptides and recombinant proteins | Barrier, complement, IL-1, local anti-inflammatory nodes | Proteolysis, tissue access, immunogenicity, and active conformation are configuration-specific | Measure identity, active function, compartment exposure, stability, and safety before choosing delivery |
| Engineered yeast | Luminal UOX or another locally acting payload | Mechanistic Extrapolation; parent-organism history does not transfer to an engineered configuration | Build and characterize exact configurations, then §1.33 → route-specific retention → §1.36 before animals |
| Engineered *A. oryzae* | Luminal UOX or independently validated payloads | Mechanistic Extrapolation; no multi-payload architecture is established | Build and characterize exact single-payload configurations, advance UOX through §1.33, test coexistence only after single arms pass, then §1.36 before animals |
| Engineered EcN | Luminal UOX, reductive PDB pathway, biosensor-controlled local activity | PULSE and CBT2.0 are separate precedents; they do not establish a combined strain, additivity, carbon fate, or human effect | Reconstruct the exact configuration; measure pathway completion, carbon fate, target engagement, persistence, and safety |
| Obligate-anaerobe LBP | PDB restoration, butyrate-associated signaling, barrier or community functions | Host, payload, carbon fate, colonization, epithelial exposure, and manufacturing stability remain configuration-specific | Matched host/configuration screen with direct flux, exposure, persistence, community, and containment readouts |
| Phage, consortium, or FMT | Microbiome subtraction or community restoration | Community effects and target specificity are unresolved for gout | Define the target community state, then measure urate flux, off-target ecological change, persistence, and safety |
| RNA or oligonucleotide delivery | URAT1, NLRP3, IL-1, or other expressed targets | Sequence specificity does not solve tissue delivery, durability, or off-target exposure | Demonstrate target-cell uptake, knockdown/expression, functional effect, biodistribution, and safety |
| Gene or cell editing | Durable transporter or UOX restoration hypotheses | Delivery, off-target effects, tissue renewal, and long-term safety remain open | Establish editing specificity, target-cell coverage, function, durability, and safety in a justified model |
| Local depot or intra-articular delivery | Tophi, synovial NLRP3, local UOX–catalase | Local delivery does not eliminate peroxide, tissue, sterility, retention, or immune risks | Compare exact formulations under matched activity, diffusion, retention, tissue-safety, and immunogenicity conditions |
| Sensors and biomarker systems | Urate dynamics or mechanism-proximal monitoring | A measurement tool does not validate an intervention or chokepoint | Validate analytical accuracy, matrix, calibration, temporal resolution, and relation to the biological endpoint |

## Route-specific boundaries

### Engineered UOX configurations

The decision order is fixed:

1. Build and characterize exact configurations in §§1.1, 1.2, and 1.5, or acquire and verify an exact external configuration.
2. Run [§1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial) on those extant configurations. A within-host matched comparison may nominate a localization strategy; cross-host observations remain configuration-specific.
3. Run route-specific process-retention experiments only for an advanced configuration.
4. Clear [§1.36](./validation-experiments.md#136-luminal-urate-antioxidant-loss--uox-h2o2-safety-assay) before animal escalation.

COMP-044 establishes only that the legacy unconditional flat-dose classification is not robust to the tested substrate-occupancy and finite-window diagnostics. It does not identify the true physiological regime, sufficient dose, serum effect, sequence, topology, host, or product architecture.

See [engineered yeast](./engineered-yeast-uricase-proposal.md), [engineered koji](./engineered-koji-protocol.md), [gut-lumen sink](./gut-lumen-sink.md), and [validation experiments](./validation-experiments.md).

### PDB and microbiome routes

The reductive PDB pathway is distinct from oxidative UOX. CBT2.0 does not establish that engineered EcN produces butyrate, that butyrate reaches epithelium, or that PDB and UOX are additive. Compare one strain, separate strains, and temporal staging only after carbon fate and residual flux are measured. [Comp-031](./dual-chassis-ecn-pdb-uricase-computational.md) is unusable for current decisions because it inherits an unsupported flat UOX regime, assigns unmeasured butyrate production to engineered EcN, and mixes compartments.

See [purine-degrading bacteria](./purine-degrading-bacteria.md), [engineered LBP chassis](./engineered-lbp-chassis.md), and validation [§§1.34 and 1.37](./validation-experiments.md#134-isotope-resolved-dietary-precursor--uox--pdb-sequential-flux).

### Native materials and compound combinations

Cultivation, dietary occurrence, or commercial availability does not establish composition, free exposure, efficacy, safety, or regulatory status. Characterize the exact material and test individual mechanisms before a combination. A combination study must prespecify the interaction null and measure exposure, target engagement, efficacy, and new safety liabilities for the exact pair.

See [medicinal mushroom track](./medicinal-mushroom-complement-track.md), [TCM rigor track](./tcm-modern-rigor-intersection.md), [supplements evidence catalog](./supplements-stack.md), and [validation §2.6](./validation-experiments.md#26-glpp--cordycepin-interaction-in-hyperuricemia--matched-wet-lab-gate).

### RNA, editing, and targeted delivery

Kidney-tropic siRNA against URAT1, macrophage-targeted inflammasome silencing, inhaled mRNA–IL-1Ra, and Q141K editing are independent hypotheses. Their biological elegance does not establish target-cell delivery, exposure, durability, safety, clinical value, or a development timeline.

See [siRNA–URAT1](./sirna-urat1-modality.md), [inhaled mRNA–IL-1Ra](./inhaled-mrna-il1ra-pulse-computational.md), [Q141K chaperone work](./abcg2-modulators.md), and [chassis-pending interventions](./chassis-pending-interventions.md).

### Complement and NLRP3 routes

Complement regulators, small-molecule NLRP3 candidates, GSDMD inhibitors, SPMs, and IL-1 blockers act at different nodes. Node separation can justify a factorial experiment; it does not establish that the components add or that every chokepoint needs coverage. Production host and sourcing are downstream of the biological case.

See [NLRP3 exploit map](./nlrp3-exploit-map.md), [complement C5a](./complement-c5a-gout.md), [SPM resolution](./spm-resolution-pathway.md), and [delivery route matrix](./delivery-route-matrix.md).

## Open decisions

- Which renal-targeted route reaches URAT1 or ABCG2 with sufficient tissue selectivity and functional urate-flux change?
- Which exact luminal-UOX configurations, if any, pass physiological product-formation and redox-safety gates?
- Which PDB configuration produces the intended terminal products and changes urate disposal without unacceptable community effects?
- Which NLRP3-node candidates reproduce target-proximal effects at human-relevant exposure in gout-relevant systems?
- Which local-delivery architecture controls UOX peroxide, retention, tissue injury, and immunogenicity under matched conditions?
- Which biomarker systems measure a mechanism closely enough to guide experiments without being mistaken for efficacy?

## Decision rule

Rank experimental questions by gout relevance, evidence gap, safety, and falsifiability. Select a route only after the target mechanism and required compartment are explicit. Retire or redirect a route at the scope justified by the evidence; no single failed chassis or modality determines the project.
