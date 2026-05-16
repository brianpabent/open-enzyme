# comp-023: cns1+cns2 cordycepin biosynthesis metabolic burden FBA

## Question

Does adding the bacterial cns1+cns2 cordycepin biosynthesis pathway (Jeennor 2023, PMID 38071331, 564 mg/L/day in *A. oryzae*) on top of the dual uricase + lactoferrin cassette in the [koji-endgame-strain](../../../koji-endgame-strain.md) §1 design impose a prohibitive metabolic burden?

Decision thresholds (per `wiki/computational-experiments.md` comp-023 row):

- **GREEN** = growth penalty <10% AND kojic + EGT yields ≥80% of dual-cassette baseline → cordycepin arm OK
- **RED**   = growth penalty >10% OR either native yield drops >20% → route cordycepin to a separate strain or LBP chassis
- **YELLOW** = anywhere between → wet-lab confirmation gate before commit

## Method (target shape)

1. Load Vongsangnak 2008 iWV1314 *A. oryzae* GEM (BioModels MODEL1507180056, SBML).
2. Configure glucose-minimal media: close all 81 default uptake reactions, re-open only D-glucose + NH₃ + O₂ + P + S. Also close reverse-direction "Excretion" reactions r2281-r2298 which act as central-metabolism inflows in default state.
3. Add native metabolite reactions for kojic acid + ergothioneine (not in iWV1314); simplified net stoichiometry per published mechanism.
4. Build 5 primary scenarios + 5 stress-test scenarios:
   - WT
   - dual (uricase + Lf)
   - +cns1-cns2 (cordycepin arm at Jeennor 2023 empirical titer 564 mg/L/d)
   - +carnS+panD (carnosine arm; cytosolic third-cassette alternative)
   - +panD only
   - +cns1-cns2 stress 10× / 100× / 1,000× / 10,000× / 100,000× the Jeennor titer
5. Run FBA on each scenario; extract growth rate (r1897), max kojic flux (re-optimize on EX_KOJIC with biomass ≥ 99% of scenario optimum), max ergothioneine flux, cordycepin flux.
6. Apply decision-threshold logic; emit decision-table.

## Cassette stoichiometry

| Cassette | Reaction added | Anchor titer |
|---|---|---|
| Uricase | aa drain: glutamate + 4.5 ATP → ADP + Pi (per aa) | 40 mg/L/d |
| Lactoferrin | aa drain: glutamate + 6.0 ATP → ADP + Pi (per aa, PDI-heavy proxy) | 500 mg/L/d (§1.9 success threshold) |
| cns1+cns2 | adenosine + ATP + NADPH → cordycepin + ADP + Pi + NADP⁺ + H⁺ | 564 mg/L/d (Jeennor 2023) |
| carnS | β-alanine + L-histidine + ATP → carnosine + AMP + PPi | ~50 mg/L/d placeholder |
| panD | L-aspartate + H⁺ → β-alanine + CO₂ | ~100 mg/L/d placeholder |
| Kojic acid (native) | D-glucose + O₂ + NADP⁺ → kojic acid + 2 H₂O + NADPH + H⁺ | Native; FBA-optimized |
| Ergothioneine (native) | L-histidine + 3 SAM + L-cysteine + O₂ → ergothioneine + 3 SAH + pyruvate + NH₃ + H₂O | Native; FBA-optimized |

## Files

- `analyze.py`: cobrapy pipeline; runs all scenarios + writes outputs
- `inputs/iWV1314.xml`: Vongsangnak 2008 SBML deposit (BioModels MODEL1507180056)
- `inputs/provenance.md`: full source list + per-claim verification log
- `outputs/results.json`: machine-readable per-scenario metrics + decision-table
- `outputs/summary.md`: human-readable; the artifact cited in the wiki page

## Cross-references

- [`wiki/cordycepin-cassette-burden-computational.md`](../../../cordycepin-cassette-burden-computational.md): interpretive wiki page
- [`wiki/computational-experiments.md`](../../../computational-experiments.md): comp-023 entry in tracking index
- [`wiki/chaperone-orthogonal-stacking.md`](../../../chaperone-orthogonal-stacking.md): line 238 names this proteome-burden gap; comp-023 closes it
- [`wiki/medicinal-mushroom-complement-track.md`](../../../medicinal-mushroom-complement-track.md): Jeennor 2023 precedent context + pentostatin discussion
- [`wiki/koji-endgame-strain.md`](../../../koji-endgame-strain.md): §1.9 extended design beneficiary

## Reproduction

```bash
cd experiments/comp-023-cns1-cns2-metabolic-burden
python3 -m pip install --user cobra==0.31.1
python3 analyze.py
```

Outputs are deterministic; re-running regenerates identical `outputs/`. Python 3.13.7 / cobrapy 0.31.1 / GLPK was the run environment for the v1 commit.
