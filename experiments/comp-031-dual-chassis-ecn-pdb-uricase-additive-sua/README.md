# comp-031 — Dual-chassis EcN PDB + uricase additive SUA prediction

**Question (from `wiki/chassis-pending-interventions.md` §"Multi-chassis stacks" M1):** does a dual-chassis stack of engineered EcN expressing the 2,8-dioxopurine PDB cluster (CBT2.0 precedent, Li 2025 PMID 41070194) co-administered with a PULSE-style luminal uricase deliver additive serum urate reduction beyond either arm alone? And does PDB-derived butyrate compound with the gut-lumen uricase sink via ABCG2 induction / Q141K trafficking rescue?

**Verdict: YELLOW (provisional)** — combined dual-chassis intervention is meaningfully better than either single arm but additivity is well below the naive sum because the two urate-consumption arms compete for the same scarce luminal urate substrate. The PDB pathway adds an INDEPENDENT mechanism axis via butyrate-mediated PPARγ ABCG2 induction + HDAC-mediated Q141K trafficking rescue. Combined predicted ΔSUA: **−1.8 to −1.9 mg/dL across genotypes** (90% CI roughly −2.2 to −1.3 mg/dL).

**Engineering handoff: route PDB and uricase to SEPARATE strains, not a dual-cassette EcN.** The substrate-competition penalty means single-chassis dual-cassette engineering gains ~nothing in additional SUA reduction relative to two separate strains co-administered. Avoid the regulatory and stability complexity of an 8-gene PDB cluster + uricase coordinated expression in one chassis.

## Reproduce

```bash
cd experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/
python3 analyze.py
```

Python stdlib only. Generates `outputs/results.json` and `outputs/summary.md`. Deterministic seed (42) for Monte Carlo reproducibility.

## File index

```
analyze.py                            # Analysis script
inputs/
  model_parameters.json               # All parameters with sources/tiers
  provenance.md                       # Detailed source citations + verification tier
outputs/
  results.json                        # Machine-readable Monte Carlo summaries
  summary.md                          # Human-readable: tables, headline, engineering handoff
README.md                             # This file
```

## Related

- `wiki/dual-chassis-ecn-pdb-uricase-computational.md` — interpretive wiki page
- `wiki/computational-experiments.md` — tracking index
- `wiki/purine-degrading-bacteria.md` — PDB pathway biology + CBT2.0 anchor
- `wiki/gut-lumen-sink.md` — PULSE uricase chassis context
- `wiki/abcg2-modulators.md` — Two distinct modulation modes (PPARγ vs HDAC)
- `wiki/chassis-pending-interventions.md` §"Multi-chassis stacks" M1 — the question this experiment answers
- `experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/` — substrate-limited regime that drives competition logic
