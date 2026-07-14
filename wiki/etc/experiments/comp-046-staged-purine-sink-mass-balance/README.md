# comp-046 — Staged purine-sink mass balance

**Status:** Complete first pass — 2026-07-13

## Question

When are proximal nucleoside interception, microoxic UOX, and distal anaerobic PDB genuinely complementary rather than redundant—or counterproductive?

## Method

The corrected model keeps two 100-unit ledgers separate:

1. **Dietary precursor ledger:** whole-cell GR-5 nucleoside interception, microbial salvage/retention, free-base liberation, absorbed material, and unabsorbed material. Every grid cell conserves mass.
2. **Endogenous luminal-urate ledger:** UOX and PDB capture under either overlap-adjusted well-mixed access or spatial UOX→residual-transfer→PDB access.

A 6,561-cell discrete full-factorial spans broad, explicitly non-clinical parameter levels. Outputs are conserved fate ledgers and an architecture boundary, not probabilities or serum urate.

## Reproduce

```bash
cd wiki/etc/experiments/comp-046-staged-purine-sink-mass-balance
python3 analyze.py
```

Python standard library only. The discrete full-factorial is deterministic; outputs are reproducible.

## Headline result

The upstream stage is beneficial only when whole-cell GR-5 cleavage is coupled to microbial salvage/retention or reduced absorption. Cleavage alone is not removal. Spatial staging is not guaranteed to win: it beats overlap-adjusted well-mixed access only when residual transfer is efficient enough. Dietary and endogenous ledgers are never summed into one efficacy number.

The decisive experiment is isotope-resolved: nucleosides, free bases, microbial incorporation, transepithelial transfer, urate, and PDB products must all be measured.

## Files

- `analyze.py` — conserved ledgers, architecture boundary, and sensitivity analysis
- `inputs/model_parameters.json` — discrete scenario levels and architecture definitions
- `inputs/provenance.md` — evidence boundary
- `inputs/query-strategy.json` — query-framing artifact
- `outputs/results.json` — machine-readable **summary** results (aggregates + architecture boundary), reproducible from the full-factorial by rerunning `analyze.py`; the 6,561 per-cell rows are not committed
- `outputs/summary.md` — interpretive output
