# comp-044 — Gut-lumen uricase physiological regime

**Status:** Complete first pass — 2026-07-13

## Question

Does comp-019's conclusion that 5–50 mg/day oral uricase is always substrate-limited survive when its own luminal-urate concentration and Km are actually used, together with finite residence time, oxygen availability, substrate access, and enzyme survival?

## Method

The script converts uricase dose and label specific activity to a bounded urate-degradation capacity, then explicitly multiplies by Michaelis–Menten substrate occupancy, active-window duration, and nonmechanistic pH/activity, effective oxygen-dependent activity, substrate-access, and active-enzyme-survival scenario multipliers. It evaluates five named scenarios and a discrete full-factorial grid of 1,620 cells per dose (4,860 across all three doses). Grid occupancy is not a probability distribution. It deliberately does not map capacity to serum urate.

## Reproduce

```bash
cd wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime
python3 analyze.py
```

Python standard library only. Outputs are deterministic.

## Headline result

The legacy 24-hour Vmax calculation gives approximately the published 32.6× / 163.1× / 326.2× WT ratios. Using this experiment's explicit 233 mg/day denominator, then applying 0.59 µM urate, Km 25 µM, and a three-hour window gives 0.093× / 0.466× / 0.932× before any oxygen, accessibility, or survival penalty. The previous flat-dose classification is therefore not robust.

This does not disprove the gut-lumen sink. It removes an unsupported quantitative shortcut and identifies the measurements needed to recover a defensible dose model.

## Files

- `analyze.py` — deterministic bounded sensitivity analysis
- `inputs/model_parameters.json` — evidence priors and clearly labeled scenario values
- `inputs/provenance.md` — claim-level provenance and exclusions
- `inputs/query-strategy.json` — literature-query framing artifact
- `outputs/results.json` — machine-readable results
- `outputs/summary.md` — human-readable result

## Key limitation

The analysis still holds concentration fixed within each active window and compares it with a whole-day flux denominator. The 0.25 and 4 regime bins are descriptive; only ratio 1 has direct mass-balance meaning. A later dynamic model requires measured local urate replenishment, topology-specific oxygen and enzyme survival, reabsorption, and spatial residence. Therefore comp-044 is a regime-audit prior, not a clinical efficacy model or a basis for dose selection.
