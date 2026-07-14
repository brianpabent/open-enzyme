# comp-043 — EcN periplasmic disulfide-folding + colonic-protease scaling: C1-INH (2) vs DAF SCR1-4 (8) vs lactoferrin (16)

**Status:** Complete — 2026-07-13
**Interpretive wiki page:** [`wiki/daf-lactoferrin-ecn-folding-feasibility-computational.md`](../../../daf-lactoferrin-ecn-folding-feasibility-computational.md)
**Tracking index:** [`wiki/computational-experiments.md`](../../../computational-experiments.md) → comp-043

## Question

comp-037 showed EcN's periplasmic DsbA/DsbC machinery can plausibly fold C1-INH (2 disulfides). A
synthesis card overreached: *"so EcN is superior to koji for PDI-heavy payloads like DAF SCR1-4
(8 disulfides) and lactoferrin (16 disulfides)."* This experiment tests whether EcN's periplasmic
disulfide-folding + colonic-protease survival actually **scales** with disulfide count, by scoring
all three payloads head-to-head under one harmonized colonic-EcN environment.

**This is explicitly NOT a genome-scale metabolic model (GEM).** A GEM models metabolic flux, not
folding-machinery competition — the wrong tool (that was the card's error). This is a
comp-006/comp-037-style structural + sequence folding-feasibility analysis.

## Method — three orthogonal axes, limiting-factor composite

1. **Axis 1 — disulfide-folding burden vs. DsbA/DsbC capacity.** Architecture-weighted "effective
   folding demand" (disulfide count × per-bond loop-length weight; long-range C-lobe-spanning bonds
   weighted heaviest as the DsbC-isomerization-limited class), compared to a precedent-derived
   capacity band (conservative 5 / moderate 8 / optimistic 12). Sensitivity-tested across the band.
2. **Axis 2 — strictly-degradative colonic-luminal protease exposure.** AlphaFold pLDDT-based
   cleavage scan (shared `lib/protease_stability.py`) on the folded-core region, five-protease
   colonic-EcN panel. C1-INH excludes the RCL (exposed by design).
3. **Axis 3 — glycosylation dependence for FUNCTION.** Categorical, evidence-based (EcN cannot
   glycosylate). The question is whether loss of glycans abolishes therapeutic function, not whether
   the protein is glycosylated.

Composite = limiting-factor (Liebig) gate: folding must succeed first; secondary axes set the
quality of a folding-plausible verdict.

## Headline result

| Payload | Disulfides | Composite verdict |
|---|---|---|
| C1-INH (serpin) | 2 | **VIABLE** (folding not the gate; comp-037 kinetic caveat still applies) |
| DAF SCR1-4 (CCP/sushi) | 8 | **PROVISIONAL** (folding-capacity-gated) |
| Lactoferrin (transferrin-lobe) | 16 | **NOT-VIABLE** (folding-limited across the whole capacity band) |

The plausible-to-not-plausible crossover sits **at DAF SCR1-4 (8 disulfides)**; its exact location
is gated by the one unmeasured parameter — the DsbA/DsbC oxidative-folding capacity at 8-16
disulfide scale. **The card's blanket "PDI-heavy" claim is REFUTED as stated.**

## Reproduce

```bash
cd wiki/etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility
python3 analyze.py
```

Python stdlib only (imports the repo-local `experiments/lib/protease_stability.py`). Deterministic.
Writes `outputs/results.json` + `outputs/summary.md`. The run asserts every disulfide Cys position
and count against the sequence and aborts on mismatch (CLAUDE.md Rule 4 grep-verify gate).

## Files

```
analyze.py                         orchestrator (three axes + composite + ranking + crossover)
inputs/
  P05155.fasta / P08174.fasta / P02788.fasta      sequences (reused, frozen)
  alphafold_*_plddt.json                          per-residue AlphaFold pLDDT (reused, frozen)
  disulfide_topology.json                         grep-verified DISULFID pairs + regions + glyco sites
  colonic_ecn_protease_panel.json                 5-protease colonic-EcN panel (from comp-037)
  provenance.md                                   sources, fetch dates, capacity-anchor honesty note
outputs/
  results.json                                    machine-readable, all axes + ranking + crossover
  summary.md                                      human-readable artifact cited by the wiki page
```

## Key limitations

- **Axis-1 capacity band is an inference, not a measurement** — no published DsbA/DsbC capacity
  metric at 8-16 disulfide scale (`chaperone-orthogonal-stacking.md` §8 item 8). This is why DAF
  SCR1-4 is PROVISIONAL, not GREEN.
- **pLDDT ≠ SASA** — comp-034 showed the burial proxy under-counts exposed helical/linker sites
  ~10× (the lactoferrin inter-lobe linker specifically). Axis 2 is a secondary axis and moot for
  lactoferrin (folding fails first).
- **Loop-length weighting is a monotone proxy**, not a measured DsbC k_cat.
- **Secretion topology, commensal proteases, bile-acid unfolding out-of-model.**
- **Predicts folding FEASIBILITY, not titer or in vivo efficacy.** A "VIABLE"/"PROVISIONAL" folding
  verdict is a wet-lab prior, not a demonstrated result.
