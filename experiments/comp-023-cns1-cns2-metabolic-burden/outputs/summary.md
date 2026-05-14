# comp-023 - cns1+cns2 cordycepin biosynthesis metabolic-burden FBA

**GEM:** iWV1314 (Vongsangnak 2008, BioModels MODEL1507180056). 2,361 reactions / 1,104 metabolites / 1,346 genes / 4 compartments.
**cobra version:** 0.31.1
**Glucose uptake:** 10.0 mmol/gDW/h (canonical FBA reference)
**Cordycepin demand anchor:** 564.64 mg/L/d (Jeennor 2023, PMID 38071331) → 0.0187 mmol/gDW/h (at 5.0 gDW/L)

## Per-scenario results

| Scenario | growth (h⁻¹) | Δ growth vs WT | max kojic (mmol/gDW/h) | kojic yield vs dual | max EGT (mmol/gDW/h) | EGT yield vs dual | cordycepin (mmol/gDW/h) | verdict |
|---|---|---|---|---|---|---|---|---|
| WT | 17.67844 | n/a | 5.7667 | n/a | 1.09841 | n/a | n/a | (reference) |
| dual (uricase + Lf) | 17.67480 | +0.02% | 5.7655 | 100.00% | 1.09819 | 100.00% | 0.00000 | **GREEN** |
| +cns1-cns2 (triple, cordycepin arm) | 17.67537 | +0.02% | 5.7657 | 100.00% | 1.09822 | 100.00% | 0.01873 | **GREEN** |
| +carnS+panD (triple, carnosine arm) | 17.67445 | +0.02% | 5.7654 | 100.00% | 1.09816 | 100.00% | 0.00000 | **GREEN** |
| +panD only | 17.67465 | +0.02% | 5.7654 | 100.00% | 1.09818 | 100.00% | 0.00000 | **GREEN** |
| +cns1-cns2 stress 10x titer | 17.68054 | -0.01% | 5.7674 | 100.03% | 1.09854 | 100.03% | 0.18728 | **GREEN** |
| +cns1-cns2 stress 100x titer | 17.73087 | -0.30% | 5.7748 | 100.16% | 1.11002 | 101.08% | 1.87284 | **GREEN** |
| +cns1-cns2 stress 1000x titer | 15.86486 | +10.26% | 5.2356 | 90.81% | 1.18541 | 107.94% | 18.72844 | **RED** |
| +cns1-cns2 stress 10000x titer | INFEASIBLE | - | - | - | - | - | - | **INFEASIBLE** |
| +cns1-cns2 stress 100000x titer | INFEASIBLE | - | - | - | - | - | - | **INFEASIBLE** |

## Decision-threshold logic

- **GREEN** = growth penalty < 10% AND kojic + EGT yields ≥ 80% of dual-cassette baseline → green-light a cordycepin arm in §1.9 extended design.
- **RED**   = growth penalty > 10% OR either native yield drops more than 20% → red-flag, route cordycepin to a separate strain or LBP chassis.
- **YELLOW** = anywhere between → wet-lab confirmation gate before commit.

## Headline verdict (cordycepin arm)

- **cns1+cns2 cordycepin arm:** GREEN
  - growth penalty vs WT: +0.02% (threshold ±10%)
  - kojic acid yield vs dual: 100.00% (threshold ≥80%)
  - ergothioneine yield vs dual: 100.00% (threshold ≥80%)
  - cordycepin produced: 564.6 mg/L/d (target 564.64 mg/L/d, Jeennor 2023 PMID 38071331)

## Notes / Limitations

1. **FBA, not pcSecKoji.** v1 uses plain flux-balance analysis with cassette burdens modeled as flux demands. PDI / chaperone / BiP / calnexin proteome-occupancy constraints are NOT in the model. This v1 captures the carbon, nitrogen, energy, and reducing-equivalent burden, NOT secretion-pathway proteome saturation. A v2 upgrade is `pcSec`-class modeling - see the brief.
2. **Lactoferrin burden is modeled as a generic translation + ER-folding cost on a glutamate/ATP drain proxy.** The 16-disulfide PDI/ERO1 load is approximated by elevating ATP-per-aa from 4.5 (uricase) to 6.0 (Lf). Real PDI saturation effects from `chaperone-orthogonal-stacking.md` §3.5 are out of scope for v1 FBA.
3. **Kojic acid and ergothioneine were not in the iWV1314 model.** We added simplified net reactions per published mechanism (Terabayashi 2010 / Marui 2011 for kojic acid; Hu 2014 / Bello 2012 for ergothioneine). Stoichiometry is approximate.
4. **Static demands.** Each cassette is treated as a fixed lower-bound flux. Real titers vary with growth phase, induction state, and substrate; FBA cannot capture dynamics.
5. **No adenosine deaminase competition modeling.** The host's native ADA (r1115-r1117) competes with cns1+cns2 for the adenosine substrate pool. FBA picks the optimal split; pentostatin-style protection (Xia 2017 PMID 29056419) would be needed in vivo if intracellular ADA flux is high.
6. **NADPH choice for Cns1 is best-guess.** The 2024 frontiersin review documents that the Cns1 cofactor (NADH vs NADPH) has not been mechanistically pinned. We used NADPH because it is the standard biosynthetic reductant in fungi. If the true cofactor is NADH, switching changes the carbon partition only marginally (NADH and NADPH pools are interchangeable via transhydrogenase in iWV1314).

## Provenance

See `inputs/provenance.md` for full source list and per-claim verification.
