# comp-046 — Staged purine-sink mass balance

**Status:** Complete first pass — 2026-07-13

## Question

Two separate questions: when does whole-cell GR-5 interception reduce modeled absorbed dietary precursor, and when does spatial UOX→PDB access capture more endogenous luminal urate than the selected overlap-adjusted well-mixed architecture? This model does not test joint three-stage complementarity or counterproductivity relative to either sink alone.

## Method

The corrected model keeps two normalized questions separate:

1. **Dietary precursor ledger:** whole-cell GR-5 nucleoside interception, microbial salvage/retention, free-base liberation, absorbed material, and unabsorbed material. Every grid cell conserves mass.
2. **Endogenous luminal-urate architecture comparison:** capture fractions under either overlap-adjusted well-mixed access or spatial UOX→residual-transfer→PDB access. This is not a conserved fate ledger because uncaptured residual material is not explicitly tracked.

Two independent 81-cell discrete full-factorials span broad, explicitly non-clinical parameter levels. Outputs are one conserved dietary fate ledger plus an endogenous capture-fraction comparison and architecture boundary—not probabilities or serum urate.

## Reproduce

```bash
cd wiki/etc/experiments/comp-046-staged-purine-sink-mass-balance
python3 analyze.py
```

Python standard library only. Both discrete full-factorials are deterministic; outputs are reproducible.

## Headline result

The upstream stage is beneficial only when whole-cell GR-5 cleavage is coupled to microbial salvage/retention or reduced absorption. Cleavage alone is not removal. Spatial staging is not guaranteed to win: it beats overlap-adjusted well-mixed access only when residual transfer is efficient enough. The dietary ledger and endogenous comparison are never combined into one efficacy number.

The decisive experiment is isotope-resolved: nucleosides, free bases, microbial incorporation, transepithelial transfer, urate, and PDB products must all be measured. The dietary ledger and endogenous capture comparison are never summed into one efficacy number.

## Files

- `analyze.py` — conserved dietary fate ledger, endogenous architecture boundary, and separate sensitivity analyses
- `inputs/model_parameters.json` — discrete scenario levels and architecture definitions
- `inputs/provenance.md` — evidence boundary
- `inputs/query-strategy.json` — query-framing artifact
- `outputs/results.json` — machine-readable **summary** results (aggregates + architecture boundary), reproducible from the two 81-cell full-factorials by rerunning `analyze.py`; per-cell rows are not committed
- `outputs/summary.md` — interpretive output
