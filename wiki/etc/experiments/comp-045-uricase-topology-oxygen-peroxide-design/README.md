# comp-045 — Uricase topology × oxygen × peroxide decision design

**Status:** Complete first pass — 2026-07-13

## Question

How should UOX localization, substrate import, catalase localization, VHb support, oxygen context, and urate concentration be compared without encoding a topology winner in advance?

## Method

This is a deterministic evidence-state and experimental-design model, not a pseudo-quantitative efficacy ranking. It formalizes four topologies, non-duplicative topology-appropriate peroxide strategies, two oxygen-support states, two oxygen contexts, and three urate concentrations. It assigns graded evidence states, adds substrate-matched inactive-UOX/chassis/PULSE-mixture controls plus explicit zero-urate controls, and generates six randomized plates: three independent biological runs for each oxygen context.

## Reproduce

```bash
cd wiki/etc/experiments/comp-045-uricase-topology-oxygen-peroxide-design
python3 analyze.py
```

Python standard library only. Outputs are deterministic.

## Headline result

Intracellular UOX+YgfU has direct precedent for substrate import and co-localized KatG/VHb support. Secreted and surface-displayed UOX avoid the importer gate and benefited from the joint KatG+VHb module in PULSE, but the source of that benefit and extracellular peroxide exposure remain unresolved. Compartment-matched extracellular/surface catalase is therefore a proposed test, not a presumed requirement or published solution.

The model supports a head-to-head factorial and eliminates no topology. PULSE's published intracellular/secreted/displayed mixture is retained as a positive benchmark alongside individual topology arms.

## Files

- `analyze.py` — constraint evaluation and plate-map generator
- `inputs/design_factors.json` — topology and hard-gate definitions
- `inputs/provenance.md` — primary-source anchors and inference boundary
- `inputs/query-strategy.json` — literature-query framing
- `outputs/results.json` — all conditions and plate map
- `outputs/summary.md` — decision summary
