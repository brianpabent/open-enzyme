#!/usr/bin/env python3
"""comp-046: conserved dietary/endogenous purine ledgers (stdlib only)."""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parent
P = json.loads((ROOT / "inputs" / "model_parameters.json").read_text())
OUT = ROOT / "outputs"


def mean(xs):
    return sum(xs) / len(xs)


def quantile(xs, q):
    values = sorted(xs)
    pos = q * (len(values) - 1)
    lo, hi = int(math.floor(pos)), int(math.ceil(pos))
    return values[lo] if lo == hi else values[lo] * (hi - pos) + values[hi] * (pos - lo)


def summary(xs):
    return {"median": quantile(xs, 0.5), "p05": quantile(xs, 0.05), "p95": quantile(xs, 0.95)}


def corr(xs, ys):
    mx, my = mean(xs), mean(ys)
    numerator = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    denominator = math.sqrt(sum((x - mx) ** 2 for x in xs) * sum((y - my) ** 2 for y in ys))
    return numerator / denominator if denominator else 0.0


def dietary_ledger(total, intercept, salvage, nucleoside_absorption, base_relative_absorption):
    unintercepted = total * (1.0 - intercept)
    intercepted = total * intercept
    microbial_salvage = intercepted * salvage
    liberated_base = intercepted - microbial_salvage
    base_absorption = min(1.0, nucleoside_absorption * base_relative_absorption)
    ledger = {
        "unintercepted_nucleoside_absorbed": unintercepted * nucleoside_absorption,
        "unintercepted_nucleoside_unabsorbed": unintercepted * (1.0 - nucleoside_absorption),
        "microbial_salvage_or_retention": microbial_salvage,
        "liberated_base_absorbed": liberated_base * base_absorption,
        "liberated_base_unabsorbed": liberated_base * (1.0 - base_absorption)
    }
    assert abs(sum(ledger.values()) - total) < 1e-9
    return ledger


def architecture_capture(uox, pdb, overlap, transfer):
    hi, lo = max(uox, pdb), min(uox, pdb)
    well_mixed = hi + (1.0 - overlap) * lo * (1.0 - hi)
    staged = uox + (1.0 - uox) * transfer * pdb
    assert 0.0 <= well_mixed <= 1.0
    assert 0.0 <= staged <= 1.0
    return well_mixed, staged


def main():
    levels = P["full_factorial_levels"]
    keys = list(levels)
    rows = []
    for values in itertools.product(*(levels[k] for k in keys)):
        x = dict(zip(keys, values))
        dietary = dietary_ledger(
            P["dietary_purine_units"],
            x["gr5_nucleoside_intercept_fraction"],
            x["whole_cell_microbial_salvage_fraction"],
            x["nucleoside_absorption_fraction"],
            x["free_base_absorption_relative_to_nucleoside"]
        )
        control_absorbed = P["dietary_purine_units"] * x["nucleoside_absorption_fraction"]
        gr5_absorbed = dietary["unintercepted_nucleoside_absorbed"] + dietary["liberated_base_absorbed"]
        precursor_reduction = (control_absorbed - gr5_absorbed) / control_absorbed

        mixed, staged = architecture_capture(
            x["uox_capture_fraction"], x["pdb_capture_fraction"],
            x["well_mixed_shared_pool_overlap"], x["staged_residual_transfer_efficiency"]
        )
        rows.append({
            **x,
            "dietary_ledger": dietary,
            "control_absorbed_precursor_units": control_absorbed,
            "gr5_absorbed_precursor_units": gr5_absorbed,
            "gr5_precursor_reduction_fraction": precursor_reduction,
            "well_mixed_endogenous_urate_capture_fraction": mixed,
            "staged_endogenous_urate_capture_fraction": staged,
            "staging_minus_well_mixed_fraction": staged - mixed
        })

    precursor_reductions = [r["gr5_precursor_reduction_fraction"] for r in rows]
    mixed_capture = [r["well_mixed_endogenous_urate_capture_fraction"] for r in rows]
    staged_capture = [r["staged_endogenous_urate_capture_fraction"] for r in rows]
    differences = [r["staging_minus_well_mixed_fraction"] for r in rows]
    architecture_counts = {
        "staging_greater": sum(d > 1e-12 for d in differences),
        "well_mixed_greater": sum(d < -1e-12 for d in differences),
        "equal": sum(abs(d) <= 1e-12 for d in differences)
    }

    central = {k: levels[k][1] for k in keys}
    central_ledger = dietary_ledger(
        P["dietary_purine_units"], central["gr5_nucleoside_intercept_fraction"],
        central["whole_cell_microbial_salvage_fraction"], central["nucleoside_absorption_fraction"],
        central["free_base_absorption_relative_to_nucleoside"]
    )
    central_mixed, central_staged = architecture_capture(
        central["uox_capture_fraction"], central["pdb_capture_fraction"],
        central["well_mixed_shared_pool_overlap"], central["staged_residual_transfer_efficiency"]
    )

    sensitivity_precursor = sorted(
        ({"parameter": k, "pearson_r": corr([r[k] for r in rows], precursor_reductions)} for k in keys),
        key=lambda z: abs(z["pearson_r"]), reverse=True
    )
    sensitivity_architecture = sorted(
        ({"parameter": k, "pearson_r": corr([r[k] for r in rows], differences)} for k in keys),
        key=lambda z: abs(z["pearson_r"]), reverse=True
    )

    results = {
        "experiment": "comp-046",
        "verdict": "TWO CONDITIONAL HYPOTHESES, NOT ONE ADDITIVE EFFICACY CLAIM",
        "n_full_factorial_grid_cells": len(rows),
        "dietary_precursor_ledger": {
            "gr5_precursor_reduction_fraction": summary(precursor_reductions),
            "grid_fraction_gr5_increases_absorbed_precursor": sum(x < 0 for x in precursor_reductions) / len(rows),
            "central_conserved_ledger": central_ledger,
            "sensitivity": sensitivity_precursor
        },
        "endogenous_luminal_urate_ledger": {
            "well_mixed_capture_fraction": summary(mixed_capture),
            "staged_capture_fraction": summary(staged_capture),
            "staging_minus_well_mixed_fraction": summary(differences),
            "architecture_grid_counts": architecture_counts,
            "central_well_mixed_capture_fraction": central_mixed,
            "central_staged_capture_fraction": central_staged,
            "sensitivity": sensitivity_architecture
        },
        "architecture_boundary": "staging wins only when uox + (1-uox)*transfer*pdb exceeds max(uox,pdb) + (1-overlap)*min(uox,pdb)*(1-max(uox,pdb))",
        "limitations": [
            "Grid occupancy is not probability; levels are deliberately broad design cases.",
            "The GR-5 stage represents whole-cell cleavage plus salvage/retention, not DeoD causality alone.",
            "Dietary precursor and endogenous luminal urate are separate accounting structures and are not summed (dietary = conserved 100-unit fate ledger; endogenous = capture-fraction architecture comparison, NOT a conserved ledger -- endogenous_luminal_urate_units is stored but unused).",
            "Architecture equations are hypotheses requiring measured kinetics, overlap, transfer loss, residence time, and PDB viability.",
            "The model omits microbial turnover and re-release, cross-feeding, renal compensation, inflammation, colonization, and serum-urate dynamics."
        ]
    }
    OUT.mkdir(exist_ok=True)
    (OUT / "results.json").write_text(json.dumps(results, indent=2) + "\n")

    d = results["dietary_precursor_ledger"]
    e = results["endogenous_luminal_urate_ledger"]
    total_arch = sum(e["architecture_grid_counts"].values())
    lines = [
        "# comp-046 summary — staged purine-sink conserved ledgers", "",
        "**Verdict: TWO CONDITIONAL HYPOTHESES, NOT ONE ADDITIVE EFFICACY CLAIM.** Whole-cell GR-5 helps the dietary precursor ledger only if cleavage is coupled to enough microbial salvage/retention or reduced base absorption. Spatial UOX→PDB staging helps the endogenous luminal-urate ledger only if residual transfer is efficient enough relative to same-pool overlap. The ledgers are not summed into ΔSUA.", "",
        f"The discrete full-factorial contains **{results['n_full_factorial_grid_cells']} grid cells**. Occupancy is not biological probability.", "",
        "## Dietary purine-precursor ledger", "",
        "Central ledger (100 normalized dietary purine units):", "",
        "| Fate | Units |", "|---|---:|"
    ]
    for key, value in d["central_conserved_ledger"].items():
        lines.append(f"| {key} | {value:.3f} |")
    pr = d["gr5_precursor_reduction_fraction"]
    lines += ["", f"Across the selected grid, whole-cell GR-5 changes absorbed precursor by a median reduction of **{pr['median']:.3f} relative to the matched untreated absorbed precursor** (5th–95th percentile {pr['p05']:.3f}–{pr['p95']:.3f}). In {d['grid_fraction_gr5_increases_absorbed_precursor']:.3f} of grid cells it increases absorbed precursor. These are design-space occupancies, not incidence estimates.", "", "## Endogenous luminal-urate architecture ledger", "", "| Architecture | Median captured fraction | 5th–95th percentile |", "|---|---:|---:|"]
    for label, key in [("Well-mixed/overlapping", "well_mixed_capture_fraction"), ("Spatially staged", "staged_capture_fraction")]:
        row = e[key]
        lines.append(f"| {label} | {row['median']:.3f} | {row['p05']:.3f}–{row['p95']:.3f} |")
    c = e["architecture_grid_counts"]
    diff = e["staging_minus_well_mixed_fraction"]
    lines += ["", f"Staging is greater in {c['staging_greater']}/{total_arch} grid cells, well-mixed access is greater in {c['well_mixed_greater']}/{total_arch}, and they are equal in {c['equal']}/{total_arch}. Median staged-minus-well-mixed capture is {diff['median']:.3f}; it is not assumed positive.", "", "**Boundary:** staging wins only when `uox + (1-uox) × transfer × pdb` exceeds the overlap-adjusted well-mixed capture equation documented in the artifact.", "", "## Experimental consequence", "", "Use isotope-resolved dietary flux to measure nucleosides, free bases, microbial biomass incorporation, and transepithelial transfer. Separately, use a sequential microoxic→anoxic urate reactor to measure UOX capture, residual transfer, PDB capture, every pathway product, and viability. Do not infer architecture additivity by summing the two ledgers.", "", "## Limitations", ""]
    lines += [f"- {x}" for x in results["limitations"]]
    (OUT / "summary.md").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
