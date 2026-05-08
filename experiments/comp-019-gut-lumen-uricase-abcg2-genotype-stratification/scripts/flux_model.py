#!/usr/bin/env python3
"""
comp-019 — Gut-Lumen Uricase x ABCG2 Genotype Flux Model
========================================================

Phase B in-silico flux model. Predicts steady-state delta-SUA in:
  - WT/WT (100% functional ABCG2)
  - Q141K heterozygous (75% functional)
  - Q141K homozygous (50% functional)
  - Severe ABCG2 dysfunction (25% functional)
under three uricase-dose scenarios (low / mid / high).

Model logic
-----------
1. Daily mass balance: total urate production = renal + intestinal + (any uricase)
2. Intestinal compartment: ABCG2-mediated secretion follows Michaelis-Menten
   v = Vmax * [S] / (Km + [S])
   In vivo, [S] (lumen urate) is ~0.6 uM at baseline, far below Km (8240 uM).
   So secretion rate ~ (Vmax / Km) * [S] — i.e., LINEAR in substrate.
3. Adding luminal uricase pulls lumen [S] toward zero (uricase is fast: kcat/Km
   for A. flavus uricase >> ABCG2 transport rate). This effectively doubles
   the basolateral->apical urate gradient (since the apical "back-pressure"
   from accumulated lumen urate is cleared).
4. Genotype scaling: secretion capacity = baseline * functional_class.
   Anchored against Miyazaki 2025 direct measurement.
5. Renal partial compensation: when gut excretion changes by dF, kidney
   compensates by (1 - r) * dF where r is the compensation fraction
   (central estimate 0.30, i.e. kidney offsets 30% of the gut delta).
6. Steady-state SUA: assume ~1-month timescale equilibration. Delta-SUA
   per day at new steady state =
     delta-flux (mg/day) / clearance (L/day).
   We instead use the algebraic shortcut: delta-SUA/SUA-baseline =
     -delta-flux / total-baseline-flux (1st-order kinetic approximation).

Sensitivity: Monte Carlo over parameter uncertainty bounds in
flux_model_parameters.json. Outputs central estimate + 90% CI.

Usage:
  python3 flux_model.py
Outputs land in ../outputs/.
"""

import json
import math
import random
from pathlib import Path
from collections import defaultdict


# ----------------------------------------------------------------------
# I/O paths
# ----------------------------------------------------------------------
HERE = Path(__file__).resolve().parent
INPUTS_DIR = HERE.parent / "inputs"
OUTPUTS_DIR = HERE.parent / "outputs"
OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)


# ----------------------------------------------------------------------
# Load parameters
# ----------------------------------------------------------------------
def load_params() -> dict:
    with open(INPUTS_DIR / "flux_model_parameters.json", "r") as f:
        return json.load(f)


# ----------------------------------------------------------------------
# Core flux model — single deterministic evaluation
# ----------------------------------------------------------------------
def evaluate_scenario(
    *,
    functional_class: float,
    uricase_dose_mg_per_day: float,
    uricase_specific_activity_U_per_mg: float,
    intestinal_baseline_fraction: float,
    total_daily_production_mg: float,
    renal_compensation_fraction: float,
    sua_baseline_mg_dL: float,
) -> dict:
    """
    Compute predicted delta-SUA (mg/dL) and supporting fluxes.

    Returns a dict with:
      baseline_intestinal_mg : intestinal urate excretion at baseline (no uricase)
      baseline_renal_mg      : renal urate excretion at baseline
      baseline_intestinal_genotype_adjusted_mg : intestinal flux at this genotype
      delta_intestinal_with_uricase_mg : added flux from uricase x ABCG2 gradient
      net_delta_flux_mg : after renal compensation
      delta_sua_mg_dL : predicted serum urate change
      uricase_capacity_mg_per_day : raw enzyme capacity (substrate-saturating bound)
    """
    # 1. Baseline mass balance (WT, healthy kidney)
    baseline_renal = total_daily_production_mg * (1 - intestinal_baseline_fraction)
    baseline_intestinal_wt = total_daily_production_mg * intestinal_baseline_fraction

    # 2. Genotype-adjusted baseline intestinal capacity
    #    (functional_class = 1.0 for WT; 0.5 for Q141K hom; etc.)
    baseline_intestinal_geno = baseline_intestinal_wt * functional_class
    # The remainder shifts to kidney (Matsuo 2014 directional finding) under
    # baseline conditions — but kidney capacity is already at-or-near ceiling
    # in gout patients, so the SUA equilibrates upward. Without uricase,
    # delta_SUA from genotype alone is captured implicitly in the patient's
    # baseline SUA. We're computing delta-SUA from uricase intervention,
    # so this term is the reference.

    # 3. Uricase capacity in raw enzyme terms.
    #    1 U = 1 umol/min at pH 8.5, 37C.
    #    Per day: 1 U sustained = 1 umol/min * 1440 min/day = 1440 umol/day.
    #    Convert to mg uric acid: 1440 umol * 168.11 ug/umol / 1000 = 242 mg/day per U.
    #    Adjust for in-vivo specific-activity attenuation (~75% at colon pH).
    in_vivo_activity_factor = 0.75
    enzyme_capacity_umol_per_day = (
        uricase_dose_mg_per_day
        * uricase_specific_activity_U_per_mg
        * in_vivo_activity_factor
        * 1440  # min/day
    )
    enzyme_capacity_mg_per_day = enzyme_capacity_umol_per_day * 168.11 / 1000

    # 4. The KEY question: does uricase capacity exceed the intestinal urate
    #    flux from blood->gut at this genotype? If yes, uricase clamps lumen
    #    [urate] near zero (substrate-limited regime). If no, uricase saturates
    #    (capacity-limited regime).
    delivered_intestinal_flux_mg_per_day = baseline_intestinal_geno
    capacity_ratio = enzyme_capacity_mg_per_day / max(delivered_intestinal_flux_mg_per_day, 1.0)

    # 5. Effect of uricase on net intestinal urate elimination.
    #    Substrate-limited regime (capacity_ratio >= 1.0): uricase drains
    #    everything that comes through, so delta_intestinal scales with the
    #    gradient improvement. With baseline lumen urate near zero (it's
    #    already low, ~0.6 uM), the gradient improvement is bounded by
    #    the reabsorption fraction of the ~30% urate that normally cycles
    #    back. Per Yu 2015 / Bhatnagar 2016 review, ~30-50% of secreted
    #    intestinal urate is reabsorbed in the colon. So the maximum
    #    additional flux uricase can extract is ~30-50% of the delivered
    #    flux — this is the "sink amplification factor."
    #    Capacity-limited regime (capacity_ratio < 1.0): max additional
    #    flux is the enzyme capacity itself.
    sink_amplification_factor = 0.40  # central; uricase prevents reabsorption of
                                      # ~40% of secreted urate
    if capacity_ratio >= 1.0:
        # Substrate-limited: uricase clamps lumen, gradient improvement
        # = sink_amplification * delivered_flux
        delta_intestinal = sink_amplification_factor * delivered_intestinal_flux_mg_per_day
    else:
        # Capacity-limited: bounded by enzyme throughput
        delta_intestinal = min(
            enzyme_capacity_mg_per_day,
            sink_amplification_factor * delivered_intestinal_flux_mg_per_day,
        )

    # 6. Renal partial compensation. When gut excretion increases by
    #    delta_intestinal, the kidney down-regulates excretion by
    #    renal_compensation_fraction * delta_intestinal.
    net_delta_flux = delta_intestinal * (1 - renal_compensation_fraction)

    # 7. Delta-SUA via 1st-order steady-state approximation.
    #    Baseline mass balance: total production = total elimination (steady).
    #    SUA_new / SUA_baseline = (production - delta_elimination) / production
    #    delta_SUA = -SUA_baseline * (delta_elimination / production)
    delta_sua_mg_dL = -sua_baseline_mg_dL * (net_delta_flux / total_daily_production_mg)

    return {
        "baseline_renal_mg": baseline_renal,
        "baseline_intestinal_wt_mg": baseline_intestinal_wt,
        "baseline_intestinal_genotype_adjusted_mg": baseline_intestinal_geno,
        "uricase_capacity_mg_per_day": enzyme_capacity_mg_per_day,
        "capacity_ratio": capacity_ratio,
        "delta_intestinal_with_uricase_mg": delta_intestinal,
        "net_delta_flux_mg": net_delta_flux,
        "delta_sua_mg_dL": delta_sua_mg_dL,
    }


# ----------------------------------------------------------------------
# Sensitivity analysis via Monte Carlo
# ----------------------------------------------------------------------
def sample_uniform(low: float, high: float) -> float:
    return random.uniform(low, high)


def monte_carlo_delta_sua(
    params: dict,
    *,
    functional_class: float,
    uricase_dose_mg_per_day: float,
    sua_baseline_mg_dL: float,
    n_samples: int = 5000,
) -> dict:
    """Monte Carlo sensitivity over parameter ranges in flux_model_parameters.json."""
    samples = []
    for _ in range(n_samples):
        prod_mg = sample_uniform(
            params["daily_mass_balance"]["total_daily_urate_production_mg_per_day"]["low"],
            params["daily_mass_balance"]["total_daily_urate_production_mg_per_day"]["high"],
        )
        gut_frac = sample_uniform(
            params["daily_mass_balance"]["intestinal_excretion_fraction_normal_kidney"]["low"],
            params["daily_mass_balance"]["intestinal_excretion_fraction_normal_kidney"]["high"],
        )
        spec_act = params["uricase_kinetic_priors"]["specific_activity_U_per_mg"]["central"]
        renal_comp = sample_uniform(
            params["renal_compensation_fraction"]["low"],
            params["renal_compensation_fraction"]["high"],
        )

        result = evaluate_scenario(
            functional_class=functional_class,
            uricase_dose_mg_per_day=uricase_dose_mg_per_day,
            uricase_specific_activity_U_per_mg=spec_act,
            intestinal_baseline_fraction=gut_frac,
            total_daily_production_mg=prod_mg,
            renal_compensation_fraction=renal_comp,
            sua_baseline_mg_dL=sua_baseline_mg_dL,
        )
        samples.append(result["delta_sua_mg_dL"])

    samples.sort()
    return {
        "median": samples[n_samples // 2],
        "p05": samples[int(0.05 * n_samples)],
        "p95": samples[int(0.95 * n_samples)],
        "mean": sum(samples) / n_samples,
        "stdev": math.sqrt(
            sum((s - sum(samples) / n_samples) ** 2 for s in samples) / (n_samples - 1)
        ),
    }


# ----------------------------------------------------------------------
# Main scenario sweep
# ----------------------------------------------------------------------
def main():
    random.seed(42)
    params = load_params()

    # Genotype scenarios + sex baseline-SUA scenarios
    genotypes = {
        "WT_male": {"functional_class": 1.00, "sua_baseline_mg_dL": 8.0, "label": "WT/WT, male gout patient"},
        "Q141K_het_male": {"functional_class": 0.75, "sua_baseline_mg_dL": 8.5, "label": "Q141K heterozygous, male gout patient"},
        "Q141K_hom_male": {"functional_class": 0.50, "sua_baseline_mg_dL": 9.5, "label": "Q141K homozygous, male gout patient"},
        "WT_female": {"functional_class": 1.00, "sua_baseline_mg_dL": 7.0, "label": "WT/WT, female gout patient"},
        "Q141K_het_female": {"functional_class": 0.75, "sua_baseline_mg_dL": 7.5, "label": "Q141K heterozygous, female gout patient"},
        "Q141K_hom_female": {"functional_class": 0.50, "sua_baseline_mg_dL": 8.0, "label": "Q141K homozygous, female gout patient"},
        "Severe_dysfunction_male": {"functional_class": 0.25, "sua_baseline_mg_dL": 10.5, "label": "Severe ABCG2 dysfunction (Q126*+Q141K compound), male"},
    }

    uricase_doses = {
        "low_5mg": params["uricase_dose_scenarios"]["low_dose_mg_per_day"],
        "mid_25mg": params["uricase_dose_scenarios"]["mid_dose_mg_per_day"],
        "high_50mg": params["uricase_dose_scenarios"]["high_dose_mg_per_day"],
    }

    results = {
        "_metadata": {
            "model_version": "comp-019 v1.0",
            "model_assumptions": [
                "ABCG2 operates in linear regime in vivo (lumen urate ~0.6 uM << Km 8240 uM)",
                "Uricase clamps lumen urate to ~0; sink amplification factor 0.40 (40% of secreted urate would have been reabsorbed without uricase)",
                "Genotype scales secretion capacity linearly per Matsuo 2014 + Miyazaki 2025 framework",
                "Renal compensation offsets 30% of gut delta-flux (sensitivity: 0-50%)",
                "1st-order steady-state approximation for delta-SUA",
            ],
            "monte_carlo_n": 5000,
            "random_seed": 42,
        },
        "central_estimates": {},
        "monte_carlo": {},
    }

    # Central estimates (deterministic) + MC sensitivity (90% CI)
    for geno_key, geno in genotypes.items():
        results["central_estimates"][geno_key] = {}
        results["monte_carlo"][geno_key] = {}
        for dose_key, dose_mg in uricase_doses.items():
            central = evaluate_scenario(
                functional_class=geno["functional_class"],
                uricase_dose_mg_per_day=dose_mg,
                uricase_specific_activity_U_per_mg=params["uricase_kinetic_priors"]["specific_activity_U_per_mg"]["central"],
                intestinal_baseline_fraction=params["daily_mass_balance"]["intestinal_excretion_fraction_normal_kidney"]["central"],
                total_daily_production_mg=params["daily_mass_balance"]["total_daily_urate_production_mg_per_day"]["central"],
                renal_compensation_fraction=params["renal_compensation_fraction"]["central"],
                sua_baseline_mg_dL=geno["sua_baseline_mg_dL"],
            )
            results["central_estimates"][geno_key][dose_key] = central

            mc = monte_carlo_delta_sua(
                params,
                functional_class=geno["functional_class"],
                uricase_dose_mg_per_day=dose_mg,
                sua_baseline_mg_dL=geno["sua_baseline_mg_dL"],
                n_samples=5000,
            )
            results["monte_carlo"][geno_key][dose_key] = mc

    # Write JSON results
    with open(OUTPUTS_DIR / "flux_model_results.json", "w") as f:
        json.dump(results, f, indent=2)

    # Write human-readable summary
    write_summary_md(results, genotypes, uricase_doses, params)

    # Print compact console table
    print("=" * 80)
    print("comp-019 — Gut-Lumen Uricase x ABCG2 Genotype Flux Model")
    print("=" * 80)
    print(f"\n{'Scenario':<35} {'Low 5mg':<14} {'Mid 25mg':<14} {'High 50mg':<14}")
    print("-" * 80)
    for geno_key, geno in genotypes.items():
        line = f"{geno['label'][:34]:<35}"
        for dose_key in ("low_5mg", "mid_25mg", "high_50mg"):
            mc = results["monte_carlo"][geno_key][dose_key]
            line += f" {mc['median']:+.2f} mg/dL    "
        print(line)
    print()
    print("All values are predicted delta-SUA at steady state (Monte Carlo medians).")
    print("Negative = serum urate reduction. See outputs/flux_model_summary.md for 90% CI.")


def write_summary_md(results, genotypes, uricase_doses, params):
    lines = []
    lines.append("# comp-019 — Flux Model Results Summary\n")
    lines.append("Predicted delta-SUA (mg/dL) at steady state by ABCG2 genotype and uricase dose.\n")
    lines.append("Negative values = serum urate reduction.\n")
    lines.append("\n## Central estimates (deterministic)\n")
    lines.append("| Scenario | Low 5 mg/d | Mid 25 mg/d | High 50 mg/d |")
    lines.append("|---|---|---|---|")
    for geno_key, geno in genotypes.items():
        row = f"| {geno['label']} |"
        for dose_key in ("low_5mg", "mid_25mg", "high_50mg"):
            d = results["central_estimates"][geno_key][dose_key]["delta_sua_mg_dL"]
            row += f" {d:+.2f} |"
        lines.append(row)
    lines.append("")
    lines.append("\n## Monte Carlo 90% CI (n=5000)\n")
    lines.append("| Scenario | Low 5 mg/d (median, 90% CI) | Mid 25 mg/d (median, 90% CI) | High 50 mg/d (median, 90% CI) |")
    lines.append("|---|---|---|---|")
    for geno_key, geno in genotypes.items():
        row = f"| {geno['label']} |"
        for dose_key in ("low_5mg", "mid_25mg", "high_50mg"):
            mc = results["monte_carlo"][geno_key][dose_key]
            row += f" {mc['median']:+.2f} ({mc['p05']:+.2f} to {mc['p95']:+.2f}) |"
        lines.append(row)
    lines.append("")
    lines.append("\n## Capacity-vs-substrate diagnostic\n")
    lines.append("Whether enzyme capacity exceeds delivered intestinal urate flux at this genotype + dose.")
    lines.append("Ratio >= 1.0 means substrate-limited (uricase clamps lumen, sink amplification factor 0.40 applies).")
    lines.append("Ratio < 1.0 means capacity-limited (delta-intestinal bounded by enzyme dose).\n")
    lines.append("| Scenario | Low 5 mg/d ratio | Mid 25 mg/d ratio | High 50 mg/d ratio |")
    lines.append("|---|---|---|---|")
    for geno_key, geno in genotypes.items():
        row = f"| {geno['label']} |"
        for dose_key in ("low_5mg", "mid_25mg", "high_50mg"):
            r = results["central_estimates"][geno_key][dose_key]["capacity_ratio"]
            row += f" {r:.2f} |"
        lines.append(row)
    lines.append("")
    lines.append("\n## Model assumptions\n")
    for a in results["_metadata"]["model_assumptions"]:
        lines.append(f"- {a}")
    lines.append("")
    lines.append("\n## Headline interpretation\n")
    lines.append("- **WT/WT non-Q141K males DO show meaningful delta-SUA** in the flux model. The mechanism is not Q141K-dependent.")
    lines.append("- **Q141K-positive carriers show LESS absolute reduction** because the gut compartment they're losing access to is already partially compromised — the substrate flux that uricase can amplify is smaller.")
    lines.append("- **Severe ABCG2 dysfunction (~25% functional) shows the smallest absolute response** despite having the highest baseline SUA — the gut compartment is so impaired that even a perfect uricase has little substrate to work with. This is the platform's structural ceiling for the worst-impaired patients.")
    lines.append("- The flux model contradicts the binary 'mechanism only works in Q141K' framing. The mechanism works ACROSS genotypes; the magnitude scales with the residual ABCG2 capacity at any given genotype.")
    lines.append("- **Most platform-relevant conclusion:** the gut-lumen uricase target demographic should NOT be narrowed to Q141K-positive patients. The opposite — non-Q141K patients have the LARGEST per-patient response. Q141K-positive patients are still candidates but for a different reason (high unmet ULT need, allopurinol resistance).")
    lines.append("")
    with open(OUTPUTS_DIR / "flux_model_summary.md", "w") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    main()
