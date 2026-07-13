---
title: "Uricase Topology × Oxygen × Peroxide — Computational Design (comp-045)"
date: 2026-07-13
tags: [uricase, gout, EcN, koji, oxygen, hydrogen-peroxide, topology, computational, comp-045]
related:
  - computational-experiments.md
  - validation-experiments.md
  - gut-lumen-uricase-physiologic-regime-computational.md
  - gut-lumen-sink.md
  - engineered-koji-protocol.md
sources:
  - "Gao et al. 2025 — PMID 41038159; PMCID PMC12629798"
  - "Zhao et al. 2022 — PMID 35491895; PMCID PMC9067508"
  - "Li et al. 2023 — PMCID PMC10242094"
  - "EcN C6 uricase — PMCID PMC10013758"
---

# Uricase Topology × Oxygen × Peroxide — Computational Design (comp-045)

## Question

How should intracellular, secreted, surface-displayed, and koji-secreted UOX be compared across substrate, oxygen, and peroxide constraints without encoding a topology winner in advance?

## Verdict

**YELLOW — joint empirical comparison required; no topology eliminated.** Intracellular UOX+YgfU has the cleanest direct precedent for putting substrate import, UOX, KatG, and VHb in one cell. Secreted and displayed UOX avoid the importer gate and also benefited from PULSE's joint KatG+VHb module, but extracellular peroxide exposure and the source of low-oxygen benefit remain unresolved.

## Why this matters

The corpus previously described PULSE largely as secreted UOX and treated intracellular koji catalase as if it neutralized H2O2 before UOX secretion. The PULSE primary paper instead compared three UOX topologies and used all three in its chronic-rat mixture. H2O2 is generated when active UOX meets urate, so reaction-site localization—not chassis membership alone—determines whether catalase is directly co-localized.

## Method summary

comp-045 is a deterministic evidence-state and experimental-design model. It formalizes:

- four topologies: intracellular+YgfU, LamB secretion, InakN display, and free koji secretion;
- no peroxide module, intracellular KatG/native catalase, or a proposed compartment-matched catalase construct;
- ±VHb where the chassis supports it;
- separate oxic and microoxic contexts;
- 0.59 µM human-baseline prior, 50 µM sensitivity, and 250 µM PULSE-benchmark urate.

Evidence is graded as direct support, indirect empirical support, proposed direct test, controlled-but-not-proven-sufficient, unresolved, or unsupported. No efficacy score is assigned.

## Key results

The design contains:

- 19 non-duplicative topology × peroxide × VHb conditions;
- three urate concentrations;
- three independent biological runs per oxygen context;
- six randomized 96-well plates, with 81 used wells per plate;
- inactive-UOX, chassis-only, and PULSE-mixture controls matched at 0.59/50/250 µM, plus explicit 0 µM no-urate and medium controls.

Oxic and microoxic conditions are separated by plate, every plate carries the same anchors, and topology is randomized within each plate. The primary readouts are urate, product formation, H2O2, dissolved oxygen, viability, and UOX localization.

## Independent mechanism axes

1. **Substrate access:** intracellular UOX requires YgfU; extracellular and surface UOX do not.
2. **Peroxide exposure:** intracellular KatG is directly co-localized only with intracellular UOX. PULSE provides indirect empirical support for KatG+VHb benefit in secreted and displayed forms, but does not establish that epithelial extracellular H2O2 is controlled.
3. **Oxygen handling:** VHb improves cellular oxygen utilization but cannot create oxygen. Its direct relevance is strongest for intracellular UOX; dissolved oxygen and demand remain required readouts for every topology.

## Limitations

- KatG and VHb were introduced jointly in key precedents; the new factorial separates them precisely because their independent effects are unresolved.
- Co-secreted/fused and surface-tethered catalase are proposed constructs, not published PULSE configurations.
- Intracellular “compartment-matched catalase” is not a separate arm because it duplicates intracellular KatG/native catalase.
- “Oxic” is a controlled context, not proof that oxygen supply exceeds UOX demand.
- Cross-plate anchors help normalization but do not eliminate biological-run effects.
- The design does not model expression burden, proteolysis, mucus retention, colonization, or containment.
- Independent peer review rejected the initial binary “hard gate” model and plate-confounded layout; the final artifact uses graded evidence and randomized context-specific plates.

## Impact on experimental priorities

This reframes topology selection from narrative preference to a **decision experiment**. The PULSE three-form mixture is the positive benchmark. Free secreted koji remains testable, but it cannot claim automatic peroxide closure from intracellular catalase; a matched-catalase arm is required.

## Cross-references

- [Reproducible artifact and plate maps](./etc/experiments/comp-045-uricase-topology-oxygen-peroxide-design/)
- [Physiological-regime audit](./gut-lumen-uricase-physiologic-regime-computational.md)
- [Validation experiments](./validation-experiments.md)
- [Gut-lumen sink](./gut-lumen-sink.md)
