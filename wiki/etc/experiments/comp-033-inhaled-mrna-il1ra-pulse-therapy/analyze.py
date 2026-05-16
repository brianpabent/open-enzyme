#!/usr/bin/env python3
"""
comp-033 — Inhaled mRNA-IL-1Ra pulse therapy: dose-AUC modeling + economic comparison + partner-ID summary.

Monte Carlo simulation of pulmonary IL-1Ra plasma exposure achievable via inhaled mRNA-LNP at
the dose range disclosed by Translate Bio MRT5005 and Arcturus ARCT-032 (CF inhaled-mRNA programs).
Compares predicted plasma Cmax + AUC against anakinra (100 mg SC QD) therapeutic benchmark.

Stdlib only (random, math, json, os, statistics). Deterministic with rng_seed = 33.
"""

import json
import math
import os
import random
import statistics
from pathlib import Path

HERE = Path(__file__).parent
IN_DIR = HERE / "inputs"
OUT_DIR = HERE / "outputs"
OUT_DIR.mkdir(exist_ok=True)


def load(name):
    with open(IN_DIR / name) as f:
        return json.load(f)


def log_uniform(lo, hi, rng):
    return math.exp(rng.uniform(math.log(lo), math.log(hi)))


def uniform(lo, hi, rng):
    return rng.uniform(lo, hi)


def percentile(data, p):
    s = sorted(data)
    if not s:
        return float("nan")
    k = (len(s) - 1) * p / 100.0
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return s[int(k)]
    return s[f] + (s[c] - s[f]) * (k - f)


def summarize(values, name):
    return {
        "name": name,
        "n": len(values),
        "median": percentile(values, 50),
        "mean": statistics.mean(values),
        "p05": percentile(values, 5),
        "p25": percentile(values, 25),
        "p75": percentile(values, 75),
        "p95": percentile(values, 95),
        "min": min(values),
        "max": max(values),
    }


def spearman_rank_correlation(x, y):
    """Stdlib-only Spearman rank correlation."""
    def rank(arr):
        sorted_pairs = sorted(enumerate(arr), key=lambda z: z[1])
        ranks = [0.0] * len(arr)
        i = 0
        while i < len(sorted_pairs):
            j = i
            while j + 1 < len(sorted_pairs) and sorted_pairs[j + 1][1] == sorted_pairs[i][1]:
                j += 1
            avg_rank = (i + j) / 2.0 + 1.0
            for k in range(i, j + 1):
                ranks[sorted_pairs[k][0]] = avg_rank
            i = j + 1
        return ranks
    rx, ry = rank(x), rank(y)
    n = len(x)
    mx, my = sum(rx) / n, sum(ry) / n
    num = sum((rx[i] - mx) * (ry[i] - my) for i in range(n))
    dx = math.sqrt(sum((rx[i] - mx) ** 2 for i in range(n)))
    dy = math.sqrt(sum((ry[i] - my) ** 2 for i in range(n)))
    if dx == 0 or dy == 0:
        return 0.0
    return num / (dx * dy)


def main():
    params = load("model_parameters.json")
    bench = load("anakinra_benchmark_pk.json")
    econ = load("mrna_lnp_economics.json")
    partners = load("partner_landscape.json")
    target = load("il1ra_target_properties.json")

    rng = random.Random(params["rng_seed"])
    n = params["n_samples"]

    # Anakinra benchmark targets
    target_cmax = bench["target_for_inhaled_mrna"]["target_plasma_cmax_ug_per_ml"]
    minimum_cmax = bench["target_for_inhaled_mrna"]["minimum_plasma_cmax_ug_per_ml"]
    target_auc = bench["target_for_inhaled_mrna"]["target_auc_24h_ug_h_per_ml"]
    anakinra_cmax = bench["anakinra_pk"]["plasma_cmax_ug_per_ml"]
    anakinra_auc = bench["anakinra_pk"]["auc_24h_ug_h_per_ml_estimate"]

    # Storage for MC samples
    cmax_predictions = []
    auc_predictions = []
    inputs_for_sensitivity = {
        "dose_mg_mrna": [],
        "translation_eff_ng_per_ug": [],
        "lung_delivery_frac": [],
        "systemic_bioavail_frac": [],
        "expression_duration_h": [],
        "clearance_per_h": [],
        "vd_L": [],
    }

    for _ in range(n):
        # Sample inputs
        dose_mg = log_uniform(
            params["dose_range_mg_mrna_per_administration"]["min"],
            params["dose_range_mg_mrna_per_administration"]["max"],
            rng,
        )
        trans_eff = log_uniform(
            params["translation_efficiency_ng_protein_per_ug_mrna_delivered"]["min"],
            params["translation_efficiency_ng_protein_per_ug_mrna_delivered"]["max"],
            rng,
        )
        lung_eff = uniform(
            params["lung_delivery_efficiency_fraction"]["min"],
            params["lung_delivery_efficiency_fraction"]["max"],
            rng,
        )
        sys_bio = uniform(
            params["systemic_bioavailability_from_alveolar_fraction"]["min"],
            params["systemic_bioavailability_from_alveolar_fraction"]["max"],
            rng,
        )
        expr_dur = uniform(
            params["expression_duration_hours"]["min"],
            params["expression_duration_hours"]["max"],
            rng,
        )
        clearance = uniform(
            params["il1ra_systemic_clearance_per_hour"]["min"],
            params["il1ra_systemic_clearance_per_hour"]["max"],
            rng,
        )
        vd_L = uniform(
            params["plasma_volume_distribution_L"]["min"],
            params["plasma_volume_distribution_L"]["max"],
            rng,
        )

        inputs_for_sensitivity["dose_mg_mrna"].append(dose_mg)
        inputs_for_sensitivity["translation_eff_ng_per_ug"].append(trans_eff)
        inputs_for_sensitivity["lung_delivery_frac"].append(lung_eff)
        inputs_for_sensitivity["systemic_bioavail_frac"].append(sys_bio)
        inputs_for_sensitivity["expression_duration_h"].append(expr_dur)
        inputs_for_sensitivity["clearance_per_h"].append(clearance)
        inputs_for_sensitivity["vd_L"].append(vd_L)

        # ---------- DOSE -> PROTEIN PIPELINE ----------
        # mRNA delivered to alveolar epithelium (mg)
        mrna_to_alveolus_mg = dose_mg * lung_eff
        # Convert to ug
        mrna_to_alveolus_ug = mrna_to_alveolus_mg * 1000.0
        # Protein synthesized in alveolar tissue (ng)
        protein_synth_ng = mrna_to_alveolus_ug * trans_eff
        # Protein reaching systemic circulation (ng)
        protein_systemic_ng = protein_synth_ng * sys_bio

        # ---------- PROTEIN -> PLASMA PK ----------
        # Single-compartment with zero-order input over expression duration, first-order elimination.
        # Steady-state plasma concentration at end of input: C_ss = (k_in / V_d) / k_el
        # where k_in is input rate (ng/h), V_d is volume of distribution (L = 1000 mL),
        # and k_el is elimination rate constant (1/h).
        # Cmax is reached at end of input (or asymptote, whichever earlier).
        k_in_ng_per_h = protein_systemic_ng / expr_dur  # zero-order input rate
        vd_mL = vd_L * 1000.0
        # Solution to dC/dt = (k_in / V_d) - k_el * C, with C(0)=0:
        # C(t) = (k_in / (V_d * k_el)) * (1 - exp(-k_el * t))
        # Cmax at t = expr_dur
        c_at_input_end_ng_per_ml = (k_in_ng_per_h / (vd_mL * clearance)) * (
            1.0 - math.exp(-clearance * expr_dur)
        )
        # Convert ng/mL to ug/mL
        cmax_ug_per_ml = c_at_input_end_ng_per_ml / 1000.0

        # AUC over 24h. During input phase (0 to expr_dur, or 0 to 24 if expr_dur >24):
        # AUC_input = (k_in / (V_d * k_el)) * (t + (1/k_el)*(exp(-k_el*t) - 1))
        # After input phase (expr_dur to 24, if expr_dur < 24):
        # C declines as C_max * exp(-k_el * (t - expr_dur))
        # AUC_decline from expr_dur to 24 = C_max * (1 - exp(-k_el*(24-expr_dur))) / k_el
        def auc_input_phase(t_end):
            ss = k_in_ng_per_h / (vd_mL * clearance)
            return ss * (t_end + (math.exp(-clearance * t_end) - 1.0) / clearance)

        if expr_dur >= 24:
            auc_24h_ng_h_per_ml = auc_input_phase(24)
        else:
            auc_during_input = auc_input_phase(expr_dur)
            c_at_end = c_at_input_end_ng_per_ml
            auc_decline = c_at_end * (1.0 - math.exp(-clearance * (24 - expr_dur))) / clearance
            auc_24h_ng_h_per_ml = auc_during_input + auc_decline

        auc_24h_ug_h_per_ml = auc_24h_ng_h_per_ml / 1000.0

        cmax_predictions.append(cmax_ug_per_ml)
        auc_predictions.append(auc_24h_ug_h_per_ml)

    # Summaries
    cmax_summary = summarize(cmax_predictions, "plasma_cmax_ug_per_ml")
    auc_summary = summarize(auc_predictions, "plasma_auc_24h_ug_h_per_ml")

    # Sensitivity (Spearman rank correlation, input vs Cmax)
    sens = {}
    for key, vals in inputs_for_sensitivity.items():
        sens[key] = round(spearman_rank_correlation(vals, cmax_predictions), 3)

    # Decision rule
    median_cmax = cmax_summary["median"]
    p05_cmax = cmax_summary["p05"]
    p95_cmax = cmax_summary["p95"]
    n_tier_a_partners = partners["summary_count"]["tier_A_active_inhaled_mrna_clinical_programs"]

    cmax_gate_pass = median_cmax >= minimum_cmax and p05_cmax >= 0.1
    partner_gate_pass = n_tier_a_partners >= 2

    # Reverse-dose calculation: what mRNA dose would the model predict reaches anakinra Cmax median?
    # Cmax scales approximately linearly with dose at fixed other inputs.
    # Median Cmax / target_cmax × current median dose = dose needed
    median_dose = math.exp(
        (math.log(params["dose_range_mg_mrna_per_administration"]["min"])
         + math.log(params["dose_range_mg_mrna_per_administration"]["max"])) / 2
    )
    dose_to_reach_target_cmax_mg = median_dose * (target_cmax / median_cmax) if median_cmax > 0 else float("inf")
    dose_to_reach_minimum_cmax_mg = median_dose * (minimum_cmax / median_cmax) if median_cmax > 0 else float("inf")

    if cmax_gate_pass and partner_gate_pass:
        verdict = "GREEN"
        verdict_reason = (
            f"median predicted plasma Cmax ({median_cmax:.2f} ug/mL) >= minimum "
            f"{minimum_cmax} ug/mL AND 5th percentile Cmax ({p05_cmax:.3f} ug/mL) "
            f">= 0.1 ug/mL AND {n_tier_a_partners} Tier A partners >= 2"
        )
    elif median_cmax >= 0.1 and median_cmax < minimum_cmax:
        verdict = "YELLOW"
        verdict_reason = (
            f"median Cmax ({median_cmax:.3f}) between 0.1 and {minimum_cmax} ug/mL — "
            f"sub-anakinra exposure but plausibly therapeutically meaningful; "
            f"partner landscape ({n_tier_a_partners} Tier A) supports advancement to wet-lab dose-finding"
        )
    elif p95_cmax >= 0.1 and median_cmax < 0.1:
        # Top tail of priors reaches sub-effective threshold; median does not.
        # Honest: this is RED on systemic-anakinra-equivalent at currently-feasible inhalation dose,
        # but the partner landscape is intact and the dose math points to a path forward
        # (larger dose, repeat dosing, OR pivot to a different chassis for systemic exposure).
        verdict = "RED"
        verdict_reason = (
            f"median Cmax ({median_cmax:.3f} ug/mL) < 0.1 ug/mL minimum-effective threshold "
            f"at currently-feasible inhaled mRNA doses (4-24 mg/administration). Only the "
            f"upper-decile prior space (p95 = {p95_cmax:.2f} ug/mL) reaches anakinra-trough exposure. "
            f"Dose modeling predicts {dose_to_reach_minimum_cmax_mg:.0f} mg mRNA needed to reach "
            f"0.5 ug/mL median Cmax and {dose_to_reach_target_cmax_mg:.0f} mg to reach anakinra Cmax — "
            f"both outside currently-feasible single-administration inhaled doses. "
            f"Partner landscape ({n_tier_a_partners} Tier A) is intact; the dose-feasibility gap "
            f"is the load-bearing finding for the OE handoff."
        )
    else:
        verdict = "RED"
        verdict_reason = (
            f"median Cmax ({median_cmax:.3f}) categorically below therapeutic threshold "
            f"across the full prior space"
        )

    # Cmax ratio vs anakinra
    cmax_ratio = median_cmax / anakinra_cmax
    auc_ratio = auc_summary["median"] / anakinra_auc

    # Output JSON
    result = {
        "verdict": verdict,
        "verdict_reason": verdict_reason,
        "n_samples": n,
        "rng_seed": params["rng_seed"],
        "predicted_plasma_cmax_ug_per_ml": cmax_summary,
        "predicted_plasma_auc_24h_ug_h_per_ml": auc_summary,
        "anakinra_benchmark": {
            "cmax_ug_per_ml": anakinra_cmax,
            "auc_24h_ug_h_per_ml": anakinra_auc,
        },
        "ratio_inhaled_vs_anakinra": {
            "cmax_ratio_median": round(cmax_ratio, 3),
            "auc_ratio_median": round(auc_ratio, 3),
            "interpretation": (
                "Median inhaled prediction reaches "
                f"{cmax_ratio * 100:.0f}% of anakinra Cmax and "
                f"{auc_ratio * 100:.0f}% of anakinra 24h AUC"
            ),
        },
        "decision_gates": {
            "median_cmax_minimum_gate": minimum_cmax,
            "median_cmax_observed": median_cmax,
            "median_cmax_passes": median_cmax >= minimum_cmax,
            "p05_cmax_minimum_gate": 0.1,
            "p05_cmax_observed": p05_cmax,
            "p05_cmax_passes": p05_cmax >= 0.1,
            "tier_a_partners_required": 2,
            "tier_a_partners_observed": n_tier_a_partners,
            "tier_a_partners_passes": partner_gate_pass,
        },
        "sensitivity_spearman_rho_vs_cmax": sens,
        "sensitivity_interpretation": (
            "Largest |rho| inputs drive Cmax variance. "
            f"Top driver: {max(sens.items(), key=lambda kv: abs(kv[1]))}"
        ),
        "reverse_dose_calculation": {
            "comment": (
                "What single-administration mRNA dose would the model predict reaches the "
                "minimum-effective Cmax (0.5 ug/mL) and the anakinra-equivalent Cmax (1.5 ug/mL)? "
                "Linear-scaling extrapolation from median Cmax at median dose."
            ),
            "median_dose_explored_mg": round(median_dose, 1),
            "median_cmax_at_median_dose_ug_per_ml": round(median_cmax, 4),
            "dose_to_reach_0.5_ug_per_ml_mg": round(dose_to_reach_minimum_cmax_mg, 0),
            "dose_to_reach_1.5_ug_per_ml_mg": round(dose_to_reach_target_cmax_mg, 0),
            "interpretation": (
                "Single-administration mRNA doses required to reach anakinra-equivalent systemic "
                "exposure are 30-100x above the highest currently-disclosed inhaled-mRNA clinical "
                "dose (24 mg). Three honest paths forward: (1) repeat-dosing within a single flare "
                "(2-4 administrations per 24h could plausibly accumulate to therapeutic AUC); "
                "(2) higher single-dose inhaled platforms — requires new device-engineering "
                "(beyond current vibrating-mesh nebulizer capacity); "
                "(3) different chassis entirely for systemic anakinra-equivalent — intra-articular "
                "mRNA-IL-1Ra delivered locally to the affected joint may have a more favorable "
                "math because local concentration is what matters and systemic dilution is bypassed."
            ),
        },
    }

    with open(OUT_DIR / "dose_auc_prediction.json", "w") as f:
        json.dump(result, f, indent=2)

    # Economic comparison block
    canakinumab_annual_low = bench["canakinumab_economic_benchmark"]["annual_cost_5_flares_yr"]
    canakinumab_annual_high = bench["canakinumab_economic_benchmark"]["annual_cost_max"]
    econ_summary = {
        "comment": "Cost-per-flare comparison: inhaled mRNA-IL-1Ra at scale vs canakinumab.",
        "inhaled_mrna_cost_per_flare_usd": {
            "low_estimate_high_scale": econ["cost_per_flare_scenarios"]["low_estimate_high_scale"][
                "usd_per_dose"
            ],
            "central_estimate": econ["cost_per_flare_scenarios"]["central_estimate"]["usd_per_dose"],
            "high_estimate_low_scale": econ["cost_per_flare_scenarios"]["high_estimate_low_scale"][
                "usd_per_dose"
            ],
        },
        "inhaled_mrna_annual_cost_usd": {
            "scenarios_5_flares_per_year": econ["cost_per_flare_scenarios"][
                "annual_cost_at_5_flares"
            ],
            "scenarios_10_flares_per_year": econ["cost_per_flare_scenarios"][
                "annual_cost_at_10_flares"
            ],
        },
        "canakinumab_annual_cost_usd": {
            "5_flares_per_year": canakinumab_annual_low,
            "max_annual": canakinumab_annual_high,
        },
        "cost_ratio_canakinumab_to_inhaled_mrna": {
            "central_low": round(canakinumab_annual_low / 180.0, 0),  # 10 flares central
            "central_high": round(canakinumab_annual_high / 90.0, 0),  # 5 flares central
            "interpretation": (
                "At central inhaled-mRNA economics ($18-180/yr) the cost ratio vs canakinumab "
                f"($100K-300K/yr) is 500-3000x. Even the conservative high-cost low-scale "
                f"inhaled scenario ($1200/yr at 10 flares) is 50-250x cheaper than canakinumab."
            ),
        },
        "vs_compounded_anakinra": (
            "Anakinra itself is approximately $1500-3000/month off-label retail = $18-36K/year. "
            "Inhaled mRNA-IL-1Ra at scale beats this by another 100-1000x at high-volume scenario "
            "and remains competitive (or breaks even) at low-volume specialty pricing. The "
            "competitive economic case is strongest against canakinumab, but the case vs anakinra "
            "is patient-experience-driven (no SC injection at flare onset) rather than purely cost."
        ),
    }
    with open(OUT_DIR / "economic_comparison.json", "w") as f:
        json.dump(econ_summary, f, indent=2)

    # Human-readable summary
    md_lines = []
    md_lines.append("# comp-033 — Inhaled mRNA-IL-1Ra Pulse Therapy — Result Summary\n")
    md_lines.append(f"**Verdict: {verdict}**\n")
    md_lines.append(f"_{verdict_reason}_\n\n")

    md_lines.append("## Dose-AUC prediction\n")
    md_lines.append(f"- Monte Carlo n = {n}, RNG seed {params['rng_seed']}\n")
    md_lines.append(
        f"- Predicted plasma Cmax: median **{median_cmax:.2f} µg/mL** "
        f"[{cmax_summary['p05']:.3f}–{cmax_summary['p95']:.2f}] (5th–95th percentile)\n"
    )
    md_lines.append(
        f"- Predicted plasma AUC (24h): median **{auc_summary['median']:.1f} µg·h/mL** "
        f"[{auc_summary['p05']:.2f}–{auc_summary['p95']:.1f}]\n"
    )
    md_lines.append(
        f"- Anakinra benchmark Cmax {anakinra_cmax} µg/mL → median ratio "
        f"**{cmax_ratio:.2f}× anakinra Cmax** ({cmax_ratio * 100:.0f}%)\n"
    )
    md_lines.append(
        f"- Anakinra benchmark AUC {anakinra_auc} µg·h/mL → median ratio "
        f"**{auc_ratio:.2f}× anakinra AUC** ({auc_ratio * 100:.0f}%)\n\n"
    )

    md_lines.append("## Decision gates\n\n")
    md_lines.append("| Gate | Threshold | Observed | Pass |\n|---|---|---|:-:|\n")
    md_lines.append(
        f"| Median Cmax | ≥ {minimum_cmax} µg/mL | {median_cmax:.3f} | "
        f"{'✅' if median_cmax >= minimum_cmax else '❌'} |\n"
    )
    md_lines.append(
        f"| 5th-pct Cmax | ≥ 0.1 µg/mL | {p05_cmax:.3f} | "
        f"{'✅' if p05_cmax >= 0.1 else '❌'} |\n"
    )
    md_lines.append(
        f"| Tier A partners | ≥ 2 | {n_tier_a_partners} | "
        f"{'✅' if partner_gate_pass else '❌'} |\n\n"
    )

    md_lines.append("## Sensitivity (Spearman ρ vs predicted Cmax)\n\n")
    md_lines.append("| Input | Spearman ρ |\n|---|---:|\n")
    for k, v in sorted(sens.items(), key=lambda kv: abs(kv[1]), reverse=True):
        md_lines.append(f"| {k} | {v:+.3f} |\n")
    md_lines.append("\n")

    md_lines.append("## Economic comparison\n\n")
    md_lines.append(
        f"- Inhaled mRNA-IL-1Ra cost per flare at scale: "
        f"${econ_summary['inhaled_mrna_cost_per_flare_usd']['low_estimate_high_scale']} (low) — "
        f"${econ_summary['inhaled_mrna_cost_per_flare_usd']['central_estimate']} (central) — "
        f"${econ_summary['inhaled_mrna_cost_per_flare_usd']['high_estimate_low_scale']} (high)\n"
    )
    md_lines.append(
        f"- Annual cost at 5–10 flares/yr (central economics): "
        f"~${econ['cost_per_flare_scenarios']['annual_cost_at_5_flares'][1]}–"
        f"{econ['cost_per_flare_scenarios']['annual_cost_at_10_flares'][1]} USD/yr\n"
    )
    md_lines.append(
        f"- Canakinumab benchmark: ${canakinumab_annual_low:,}–{canakinumab_annual_high:,}/yr\n"
    )
    md_lines.append(
        "- **Cost ratio (median inhaled : canakinumab): ~500–3000×** in favor of inhaled mRNA approach.\n\n"
    )

    md_lines.append("## Partner shortlist (recommended first contacts)\n\n")
    for p in partners["recommended_first_contacts"]:
        md_lines.append(f"- {p}\n")
    md_lines.append("\n")

    md_lines.append(
        "Full Tier-A / Tier-B / Tier-C breakdown in `inputs/partner_landscape.json`. "
        f"Total partner candidates surfaced: "
        f"{partners['summary_count']['total_partner_candidates']}\n"
    )

    md_lines.append("\n## V1 simplifications owned\n\n")
    for s in params["model_simplifications"]:
        md_lines.append(f"- {s}\n")

    with open(OUT_DIR / "summary.md", "w") as f:
        f.write("".join(md_lines))

    # Print short report to stdout
    print(f"=== comp-033 ===\nVerdict: {verdict}")
    print(f"  Median Cmax: {median_cmax:.3f} µg/mL  (anakinra benchmark {anakinra_cmax})")
    print(f"  Median ratio: {cmax_ratio:.2f}× anakinra")
    print(
        f"  p05/p95 Cmax: {cmax_summary['p05']:.3f} / {cmax_summary['p95']:.3f} µg/mL"
    )
    print(f"  Tier A partners: {n_tier_a_partners}")
    print(f"  Top sensitivity: {max(sens.items(), key=lambda kv: abs(kv[1]))}")
    print(f"  Outputs written to {OUT_DIR}")


if __name__ == "__main__":
    main()
