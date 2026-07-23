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


def assert_config_consistency(p):
    """Fail if duplicated scenario/grid values drift from their named priors."""
    measured = p["measured_or_regulatory_priors"]
    scenario = p["scenario_only_values_not_measured_human_baselines"]

    expected_grid = {
        "urate_uM": [
            measured["human_jejunal_urate_uM"]["low"],
            measured["human_jejunal_urate_uM"]["central"],
            measured["human_jejunal_urate_uM"]["high"],
            scenario["postprandial_or_inflamed_urate_uM"],
            scenario["high_distal_urate_uM"],
        ],
        "Km_uM": [
            measured["uricase_Km_urate_uM"]["low"],
            measured["uricase_Km_urate_uM"]["central"],
            measured["uricase_Km_urate_uM"]["high"],
        ],
        "hours": [
            measured["small_bowel_active_window_hours"]["low"],
            measured["small_bowel_active_window_hours"]["central"],
            measured["small_bowel_active_window_hours"]["high"],
            24.0,
        ],
        "oxygen_factor": scenario["effective_oxygen_dependent_activity_multipliers"],
        "access_factor": scenario["substrate_access_factors"],
        "survival_factor": scenario["active_enzyme_survival_factors"],
    }
    assert p["exhaustive_grid"] == expected_grid, (
        "exhaustive_grid drifted from measured_or_regulatory_priors or "
        "scenario_only_values_not_measured_human_baselines"
    )

    central_urate = measured["human_jejunal_urate_uM"]["central"]
    central_km = measured["uricase_Km_urate_uM"]["central"]
    central_hours = measured["small_bowel_active_window_hours"]["central"]
    oxygen_levels = scenario["effective_oxygen_dependent_activity_multipliers"]
    access_levels = scenario["substrate_access_factors"]
    survival_levels = scenario["active_enzyme_survival_factors"]
    assert len(oxygen_levels) == len(access_levels) == len(survival_levels) == 3
    anoxic, microoxic, full_oxygen = oxygen_levels
    low_access, limited_access, full_access = access_levels
    low_survival, limited_survival, full_survival = survival_levels
    expected_named = {
        "legacy_vmax_24h": {
            "urate_uM": None, "Km_uM": central_km, "hours": 24.0,
            "oxygen_factor": full_oxygen,
            "access_factor": full_access,
            "survival_factor": full_survival,
        },
        "jejunal_baseline_no_extra_penalties": {
            "urate_uM": central_urate, "Km_uM": central_km, "hours": central_hours,
            "oxygen_factor": full_oxygen,
            "access_factor": full_access,
            "survival_factor": full_survival,
        },
        "jejunal_baseline_microoxic_access_limited": {
            "urate_uM": central_urate, "Km_uM": central_km, "hours": central_hours,
            "oxygen_factor": microoxic,
            "access_factor": limited_access,
            "survival_factor": limited_survival,
        },
        "postprandial_sensitivity_microoxic": {
            "urate_uM": scenario["postprandial_or_inflamed_urate_uM"],
            "Km_uM": central_km, "hours": central_hours,
            "oxygen_factor": microoxic,
            "access_factor": limited_access,
            "survival_factor": limited_survival,
        },
        "distal_high_substrate_anoxic_sensitivity": {
            "urate_uM": scenario["high_distal_urate_uM"],
            "Km_uM": central_km, "hours": 24.0,
            "oxygen_factor": anoxic,
            "access_factor": low_access,
            "survival_factor": low_survival,
        },
    }
    actual_named = {
        item["name"]: {key: value for key, value in item.items() if key != "name"}
        for item in p["named_scenarios"]
    }
    assert actual_named == expected_named, (
        "named_scenarios drifted from measured_or_regulatory_priors or "
        "scenario_only_values_not_measured_human_baselines"
    )


def derive_verdict(named):
    """Apply the predeclared ratio-one decision rule, including contrary branches."""
    by_name = {row["scenario"]: row for row in named}
    legacy = by_name["legacy_vmax_24h"]["doses"]
    diagnostic = by_name["jejunal_baseline_no_extra_penalties"]["doses"]
    legacy_all_at_or_above_one = all(row["capacity_ratio"] >= 1.0 for row in legacy.values())
    diagnostic_all_at_or_above_one = all(
        row["capacity_ratio"] >= 1.0 for row in diagnostic.values()
    )
    if not legacy_all_at_or_above_one:
        return "LEGACY CONTROL NOT REPRODUCED"
    if diagnostic_all_at_or_above_one:
        return "LEGACY ROBUSTNESS NOT REJECTED"
    return "LEGACY FLAT-DOSE REGIME NOT ROBUST"


def self_check_decision_rule():
    def row(name, ratios):
        return {
            "scenario": name,
            "doses": {
                str(dose): {"capacity_ratio": ratio, "regime": regime(ratio)}
                for dose, ratio in zip((5, 25, 50), ratios)
            },
        }

    assert derive_verdict([
        row("legacy_vmax_24h", (2.0, 3.0, 4.0)),
        row("jejunal_baseline_no_extra_penalties", (1.1, 1.2, 1.3)),
    ]) == "LEGACY ROBUSTNESS NOT REJECTED"
    assert derive_verdict([
        row("legacy_vmax_24h", (2.0, 3.0, 4.0)),
        row("jejunal_baseline_no_extra_penalties", (0.9, 1.2, 1.3)),
    ]) == "LEGACY FLAT-DOSE REGIME NOT ROBUST"
    assert derive_verdict([
        row("legacy_vmax_24h", (0.9, 3.0, 4.0)),
        row("jejunal_baseline_no_extra_penalties", (0.5, 0.6, 0.7)),
    ]) == "LEGACY CONTROL NOT REPRODUCED"


def assert_reference_regression(p, diagnostic):
    """Protect the published reference arithmetic without fixing the verdict."""
    reference_inputs = {
        "specific_activity": 8.3,
        "pH_factor": 0.75,
        "flux_denominator": 233.0,
        "urate": 0.59,
        "Km": 25.0,
        "hours": 3.0,
    }
    measured = p["measured_or_regulatory_priors"]
    current_inputs = {
        "specific_activity": p["uricase_specific_activity_U_per_mg"],
        "pH_factor": p["in_vivo_ph_activity_factor_scenario_multiplier"],
        "flux_denominator": p["legacy_intestinal_urate_flux_mg_per_day"],
        "urate": measured["human_jejunal_urate_uM"]["central"],
        "Km": measured["uricase_Km_urate_uM"]["central"],
        "hours": measured["small_bowel_active_window_hours"]["central"],
    }
    if current_inputs != reference_inputs:
        return
    expected = {"5": 0.093196847, "25": 0.465984233, "50": 0.931968467}
    for dose, value in expected.items():
        assert abs(diagnostic["doses"][dose]["capacity_ratio"] - value) < 1e-6


def main():
    p = json.loads(INPUT.read_text())
    assert_config_consistency(p)
    self_check_decision_rule()
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
    assert_reference_regression(p, diagnostic)
    verdict = derive_verdict(named)
    interpretations = {
        "LEGACY FLAT-DOSE REGIME NOT ROBUST": "COMP-019's unconditional flat-dose classification is not robust to COMP-044's tested substrate-occupancy and finite-window diagnostics. COMP-044 supplies no replacement dose, serum-urate effect, genotype ordering, physiological regime, efficacy model, topology or chassis selection, production-sufficiency, or safety conclusion.",
        "LEGACY ROBUSTNESS NOT REJECTED": "The legacy saturated control is reproduced and every central jejunal diagnostic dose remains at or above the ratio-one boundary. The audit does not establish dose sufficiency or serum-urate efficacy.",
        "LEGACY CONTROL NOT REPRODUCED": "The saturated 24-hour control fails to reproduce the legacy at-or-above-one classification across all doses, so the audit cannot adjudicate robustness or infer efficacy.",
    }

    results = {
        "experiment": "comp-044",
        "verdict": verdict,
        "decision_rule": {
            "boundary": "capacity_ratio = 1",
            "legacy_control_requirement": "all legacy_vmax_24h dose ratios must be at or above one",
            "not_robust_condition": "legacy control is reproduced and at least one jejunal_baseline_no_extra_penalties dose ratio is below one",
            "contrary_condition": "legacy control is reproduced and every jejunal_baseline_no_extra_penalties dose ratio remains at or above one"
        },
        "interpretation": interpretations[verdict],
        "input_provenance_status": {
            "uricase_specific_activity_U_per_mg": "inherited prior; not newly primary-source verified for quantitative planning",
            "uricase_Km_urate_uM": "inherited range; enzyme-context dependent and not newly primary-source verified",
            "small_bowel_active_window_hours": "inherited physiology range; not a measured comp-044 patient parameter",
            "legacy_intestinal_urate_flux_mg_per_day": "derived corpus prior; not a patient-specific or local-compartment measurement"
        },
        "named_scenarios": named,
        "exhaustive_grid": grid_summary,
        "limitations": [
            "pH, effective oxygen-dependent activity, access, and survival factors are nonmechanistic scenario variables, not measured patient parameters.",
            "Oxygen is represented only by a dimensionless scenario multiplier; oxygen stoichiometry, delivery, depletion, and kinetic coupling are not modeled.",
            "Hydrogen-peroxide production, scavenging, tissue exposure, and safety are not evaluated.",
            "The legacy 233 mg/day flux denominator is a population prior, not a local compartment concentration.",
            "Fixed-concentration capacity is an upper-bound screen; substrate depletion and replenishment require a dynamic gut model.",
            "The grid is a discrete full-factorial over selected levels. Fractions of grid cells are design-space occupancy, not probabilities or uncertainty distributions.",
            "Only the ratio=1 boundary has a direct mass-balance meaning; the 0.25 and 4 bins are descriptive heuristics.",
            "The 8.3 U/mg specific activity, Km range, 2-4 hour window, and 233 mg/day denominator are inherited priors, not newly primary-source verified quantitative-planning inputs.",
            "No renal compensation, reabsorption, microbiome metabolism, topology, or serum-urate mapping is modeled. A dynamic compartmental mass balance is required before dose decisions."
        ]
    }

    OUTPUT_DIR.mkdir(exist_ok=True)
    (OUTPUT_DIR / "results.json").write_text(json.dumps(results, indent=2) + "\n")

    if verdict == "LEGACY FLAT-DOSE REGIME NOT ROBUST":
        headline = "**Verdict: LEGACY FLAT-DOSE REGIME NOT ROBUST.** COMP-019's unconditional flat-dose classification is not robust to COMP-044's tested substrate-occupancy and finite-window diagnostics. COMP-044 supplies no replacement dose, ΔSUA, genotype ordering, physiological regime, efficacy model, topology or chassis selection, production-sufficiency, or safety conclusion."
        decision = "Keep the biological gut-sink hypothesis and its quantitative regime open. Build and characterize exact configurations before the configuration-level physiological screen; complete the separate peroxide-safety gate before animal escalation."
    elif verdict == "LEGACY ROBUSTNESS NOT REJECTED":
        headline = "**Verdict: LEGACY ROBUSTNESS NOT REJECTED.** Every prespecified central jejunal diagnostic dose remains at or above the ratio-one boundary after applying substrate concentration, Km, and the finite active window. This does not validate dose sufficiency or predict ΔSUA; it means this audit does not falsify the legacy classification."
        decision = "Do not retire or confirm the legacy flat-dose claim from this audit. Keep the gut-sink hypothesis and dose regime open pending the physiological topology × oxygen × peroxide experiment."
    else:
        headline = "**Verdict: LEGACY CONTROL NOT REPRODUCED.** The saturated 24-hour control does not reproduce the legacy at-or-above-one classification across all doses, so this run cannot adjudicate its robustness. No dose, efficacy, or serum-urate inference is permitted."
        decision = "Resolve the legacy-control mismatch before using this audit. The gut-sink hypothesis and dose regime remain open."

    lines = [
        "# comp-044 summary — gut-lumen uricase physiological regime", "",
        headline, "",
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
    lines += ["", "## Decision", "", decision, "", "## Limitations", ""]
    lines += [f"- {x}" for x in results["limitations"]]
    (OUTPUT_DIR / "summary.md").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
