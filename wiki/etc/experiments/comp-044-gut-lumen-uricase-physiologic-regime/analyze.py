#!/usr/bin/env python3
"""comp-044: bounded oral-uricase capacity-regime analysis (stdlib only)."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "inputs" / "model_parameters.json"
OUTPUT_DIR = ROOT / "outputs"


def capacity_ratio(p, dose_mg, urate_uM, km_uM, hours, oxygen, access, survival):
    substrate_fraction = 1.0 if urate_uM is None else urate_uM / (km_uM + urate_uM)
    umol = (
        dose_mg
        * p["uricase_specific_activity_U_per_mg"]
        * p["in_vivo_ph_activity_factor_scenario_multiplier"]
        * 60.0
        * hours
        * substrate_fraction
        * oxygen
        * access
        * survival
    )
    mg = umol * p["molecular_weight_urate_g_per_mol"] / 1000.0
    return mg / p["legacy_intestinal_urate_flux_mg_per_day"]


def regime(ratio):
    # Only ratio=1 has a direct mass-balance interpretation. The 0.25 and 4
    # boundaries are descriptive bins for scanning the selected design grid.
    if ratio < 0.25:
        return "strongly_capacity_limited"
    if ratio < 1.0:
        return "capacity_limited"
    if ratio < 4.0:
        return "transition"
    return "capacity_exceeds_legacy_flux"


def main():
    p = json.loads(INPUT.read_text())
    named = []
    for scenario in p["named_scenarios"]:
        row = {"scenario": scenario["name"], "doses": {}}
        for dose in p["doses_mg"]:
            ratio = capacity_ratio(
                p, dose, scenario["urate_uM"], scenario["Km_uM"], scenario["hours"],
                scenario["oxygen_factor"], scenario["access_factor"], scenario["survival_factor"]
            )
            row["doses"][str(int(dose))] = {"capacity_ratio": ratio, "regime": regime(ratio)}
        named.append(row)

    grid = p["exhaustive_grid"]
    keys = ["urate_uM", "Km_uM", "hours", "oxygen_factor", "access_factor", "survival_factor"]
    combinations = list(itertools.product(*(grid[k] for k in keys)))
    grid_summary = {}
    for dose in p["doses_mg"]:
        ratios = []
        counts = {k: 0 for k in [
            "strongly_capacity_limited", "capacity_limited", "transition", "capacity_exceeds_legacy_flux"
        ]}
        for values in combinations:
            x = dict(zip(keys, values))
            ratio = capacity_ratio(
                p, dose, x["urate_uM"], x["Km_uM"], x["hours"], x["oxygen_factor"],
                x["access_factor"], x["survival_factor"]
            )
            ratios.append(ratio)
            counts[regime(ratio)] += 1
        total = len(ratios)
        grid_summary[str(int(dose))] = {
            "n_scenarios": total,
            "min_ratio": min(ratios),
            "max_ratio": max(ratios),
            "regime_counts": counts,
            "fraction_below_one": (counts["strongly_capacity_limited"] + counts["capacity_limited"]) / total,
            "fraction_at_or_above_one": 1.0 - (counts["strongly_capacity_limited"] + counts["capacity_limited"]) / total
        }

    diagnostic = next(x for x in named if x["scenario"] == "jejunal_baseline_no_extra_penalties")
    expected = {"5": 0.093196847, "25": 0.465984233, "50": 0.931968467}
    for dose, value in expected.items():
        assert abs(diagnostic["doses"][dose]["capacity_ratio"] - value) < 1e-6

    results = {
        "experiment": "comp-044",
        "verdict": "LEGACY FLAT-DOSE REGIME NOT ROBUST",
        "interpretation": "Regime classification changes when the model's own substrate, time, oxygen, access, and survival terms are applied. No serum-urate efficacy is inferred.",
        "named_scenarios": named,
        "exhaustive_grid": grid_summary,
        "limitations": [
            "pH, effective oxygen-dependent activity, access, and survival factors are nonmechanistic scenario variables, not measured patient parameters.",
            "The legacy 233 mg/day flux denominator is a population prior, not a local compartment concentration.",
            "Fixed-concentration capacity is an upper-bound screen; substrate depletion and replenishment require a dynamic gut model.",
            "The grid is a discrete full-factorial over selected levels. Fractions of grid cells are design-space occupancy, not probabilities or uncertainty distributions.",
            "Only the ratio=1 boundary has a direct mass-balance meaning; the 0.25 and 4 bins are descriptive heuristics.",
            "No renal compensation, reabsorption, microbiome metabolism, topology, or serum-urate mapping is modeled. A dynamic compartmental mass balance is required before dose decisions."
        ]
    }

    OUTPUT_DIR.mkdir(exist_ok=True)
    (OUTPUT_DIR / "results.json").write_text(json.dumps(results, indent=2) + "\n")

    lines = [
        "# comp-044 summary — gut-lumen uricase physiological regime", "",
        "**Verdict: LEGACY FLAT-DOSE REGIME NOT ROBUST.** Applying substrate concentration, Km and a finite active window reverses the regime classification for the central jejunal diagnostic before oxygen, access, or survival penalties are added. This experiment does **not** predict ΔSUA.", "",
        "## Named-scenario capacity ratios", "",
        "| Scenario | 5 mg | 25 mg | 50 mg |", "|---|---:|---:|---:|"
    ]
    for row in named:
        vals = [row["doses"][str(d)]["capacity_ratio"] for d in [5, 25, 50]]
        lines.append(f"| {row['scenario']} | {vals[0]:.4f} | {vals[1]:.4f} | {vals[2]:.4f} |")
    lines += ["", "Ratio <1 means enzyme capacity is below the legacy daily-flux denominator under that scenario; ratio ≥1 does not prove full luminal capture because spatial replenishment and reabsorption remain out of model.", "", "## Discrete full-factorial sensitivity grid", "", "The fractions below one describe occupancy of the selected equally weighted design grid; they are not biological probabilities.", "", "| Dose | Scenarios | Fraction <1 | Min ratio | Max ratio |", "|---:|---:|---:|---:|---:|"]
    for dose in ["5", "25", "50"]:
        row = grid_summary[dose]
        lines.append(f"| {dose} mg | {row['n_scenarios']} | {row['fraction_below_one']:.3f} | {row['min_ratio']:.6f} | {row['max_ratio']:.1f} |")
    lines += ["", "## Decision", "", "Retire comp-019's quantitative ΔSUA and flat-dose claims. Retain the biological gut-sink hypothesis as open. The next decision gate is a physiological topology × oxygen × peroxide experiment, informed by comp-045.", "", "## Limitations", ""]
    lines += [f"- {x}" for x in results["limitations"]]
    (OUTPUT_DIR / "summary.md").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
