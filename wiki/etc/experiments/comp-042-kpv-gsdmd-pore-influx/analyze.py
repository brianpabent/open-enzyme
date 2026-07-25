#!/usr/bin/env python3
"""
comp-042: KPV self-delivery through GSDMD pyroptotic pores vs. the constitutive
PepT1 route -- a diffusive-flux / mass-balance stress-test of the "Trojan-horse"
selectivity thesis for KPV specifically.

Stdlib-only Python 3. Deterministic given RNG seed 42.

THE QUESTION
------------
During a gout flare, pyroptotic macrophages open GSDMD pores (~20 nm inner
diameter). The Trojan-horse thesis (gsdmd-pore-delivery-paradox.md) is that
membrane-impermeant anti-inflammatory payloads flood selectively into exactly the
dying flare-driving cells. KPV (Lys-Pro-Val) has been proposed as a payload because
its reported NF-kB/NLRP3-related effects sit upstream in the inflammatory cascade.

Two assumptions are load-bearing:
  A1 -- EXPOSURE-PROXY SUFFICIENCY: over a pore's short open lifetime (1-30 min),
        does the modeled passive pore contribution exceed the lowest extracellular
        concentration effective in the Dalmasso 2008 PepT1-positive cell assay
        (~10 nM)? This is a cross-compartment engineering proxy, not an intracellular
        IC50 or efficacy bar.
  A2 -- SELECTIVITY over the PepT1 baseline: KPV can enter PepT1-positive cells,
        including the Jurkat immune-cell model in Dalmasso 2008, independent of a
        pore. A pore-specific advantage therefore depends on the matched baseline
        in intact cells. Synovial-macrophage PepT1 function and KPV accumulation
        remain uncharacterized.

THE MODEL (transport / mass-balance; NO MD, NO docking)
-------------------------------------------------------
Per-pore diffusive permeability of a short wide cylindrical aperture, INCLUDING
access (convergence) resistance (Hille / Hall):

    p_pore = H * D * pi * r_p^2 / (L_pore + pi*r_p/2)          [m^3/s]

where H is the steric-electrostatic hindrance factor (central 1.0; conservative
engineering sensitivity 0.5-1.0). Across the declared solute- and pore-radius
bounds, the pore radius is approximately 8-24x the KPV radius. The pore conduit is
negatively charged and favors cationic cargo
(Xia 2021). The access term pi*r_p/2 (~15.7 nm at r_p=10 nm)
dominates the channel term L_pore (~7 nm) -- i.e. this is an access-resistance-
limited pore, so the exact channel length is low-sensitivity.

Total pore conductance of a pyroptotic cell = N_pores * p_pore. Treating the cell as
a well-mixed compartment of volume V, the passive pore contribution approaches
extracellular [KPV] with a first-order EQUILIBRATION time constant:

    tau_eq = V / (N_pores * p_pore)
    C_in(t) = C_ext * (1 - exp(-t / tau_eq))
    peak C_in = C_ext * (1 - exp(-tau_life / tau_eq))

The planned outputs expose tau_eq, peak fraction, and every lifetime x pore-count
grid cell. No pore-lifetime conclusion is preregistered.

PepT1 COMPARATOR (a potential competing route in both cell states):
Because synovial-macrophage Vmax, efflux, turnover, degradation, membrane potential,
and proton coupling are unmeasured, a Michaelis-Menten-shaped accumulation equation
is used only as a response-surface heuristic:

    C_in,healthy(C_ext) = C_in_max_healthy * C_ext / (Km + C_ext)
    C_in_max_healthy    = AR_lin * Km    (so low-C_ext slope AR_lin = C_in,healthy/C_ext)

AR_lin (the dimensionless linear-regime accumulation ratio) encodes the UNKNOWN
synovial-macrophage PepT1 functional expression (scenarios: absent / low / moderate /
high-concentrative). The pore model gives
C_pore = f_pore * C_ext, where f_pore is the finite equilibration fraction. C_pore
is the modeled passive pore contribution, not total KPV in a pyroptotic cell;
concurrent PepT1 transport in that cell is not modeled.

HEURISTIC RATIO  S_model = C_pore / C_in,healthy
                         = f_pore * (Km + C_ext) / C_in_max_healthy.
  - Linear regime (SC/oral, C_ext << Km): S ~= f_pore/AR_lin.
  - Saturating regime (IA, C_ext >> Km): S can rise with C_ext, but
    C_in_max_healthy remains unknown.
The modeled ratio depends on AR_lin and C_ext/Km; it is not a physiological estimate.

METRICS (>=3 orthogonal) evaluated per dosing route (IA / SC / oral):
  M1 -- modeled passive pore contribution / extracellular cell-assay
        effective-concentration proxy (exposure-proxy sufficiency; A1)
  M2 -- heuristic ratio S_model vs healthy-cell comparator (A2 diagnostic),
        evaluated at the central case and over the declared 3 route-concentration
        bounds x 3 Km bounds x 4 PepT1-expression scenarios
  M3 -- robustness: sweep pore lifetime (1-30 min) x pores/cell (1-1e4)
        for all routes; one-pore rows are stress cases outside the 10-1e4
        main pore-count design range

DECISION FILTER: a route qualifies only if it clears BOTH the preregistered exposure
proxy threshold (M1 >= 1x) AND empirical selectivity evidence. Numerical M2
ratio crossings at the preregistered 3x diagnostic line are not evidence of
qualification: the PepT1
expression state and healthy-cell accumulation model are unmeasured in synovial
macrophages. No route may qualify on A2 until an empirical healthy-cell comparator
resolves that uncertainty.
"""

import json
import math
import random
import sys
from pathlib import Path

# ----- repro -----
SEED = 42
random.seed(SEED)
EXPECTED_PYTHON = (3, 14, 5)

# ----- paths -----
HERE = Path(__file__).resolve().parent
INPUTS = HERE / "inputs"
OUTPUTS = HERE / "outputs"
OUTPUTS.mkdir(exist_ok=True, parents=True)

N_MC = 20000
ROUTE_NAMES = ["intra_articular", "subcutaneous", "oral"]
SCENARIO_NAMES = ["absent", "low", "moderate", "high"]
BOUND_NAMES = ["lower", "central", "upper"]
HEURISTIC_RATIO_THRESHOLD = 3.0

# ----- unit helpers -----
UM_TO_MOL_PER_M3 = 1.0e-3   # 1 uM = 1e-6 mol/L = 1e-3 mol/m^3
MOL_PER_M3_TO_UM = 1.0e3    # inverse
NM_TO_UM = 1.0e-3


def load_inputs():
    kpv = json.loads((INPUTS / "kpv_properties.json").read_text())
    pore = json.loads((INPUTS / "pore_geometry.json").read_text())
    mac = json.loads((INPUTS / "macrophage_geometry.json").read_text())
    pk = json.loads((INPUTS / "pept1_and_effective_concentration.json").read_text())
    routes = json.loads((INPUTS / "route_concentrations.json").read_text())
    return kpv, pore, mac, pk, routes


def check_runtime():
    actual = sys.version_info[:3]
    if actual != EXPECTED_PYTHON:
        expected_text = ".".join(str(value) for value in EXPECTED_PYTHON)
        actual_text = ".".join(str(value) for value in actual)
        raise RuntimeError(
            f"This design requires CPython {expected_text}; got {actual_text}"
        )


def log_uniform(lo, hi):
    if lo <= 0:
        return 0.0
    return math.exp(random.uniform(math.log(lo), math.log(hi)))


def percentile(xs, p):
    xs = sorted(xs)
    if not xs:
        return float("nan")
    k = (len(xs) - 1) * p
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return xs[int(k)]
    return xs[f] + (xs[c] - xs[f]) * (k - f)


def stats(xs):
    if not xs:
        return {"n": 0}
    return {
        "n": len(xs),
        "mean": sum(xs) / len(xs),
        "median": percentile(xs, 0.5),
        "p5": percentile(xs, 0.05),
        "p25": percentile(xs, 0.25),
        "p75": percentile(xs, 0.75),
        "p95": percentile(xs, 0.95),
        "min": min(xs),
        "max": max(xs),
    }


# ===================== physics =====================

def pore_permeability_m3_s(D, r_pore_m, L_pore_m, hindrance=1.0):
    """Diffusive permeability of one short cylindrical pore including two-sided
    access (convergence) resistance.

        R_channel = L / (D * pi * r^2)
        R_access  = 1 / (2 * D * r)    (both sides combined; 1/(4Dr) each side)
        p = 1 / (R_channel + R_access) = H * D*pi*r^2 / (L + pi*r/2)
    """
    channel = L_pore_m / (D * math.pi * r_pore_m ** 2)
    access = 1.0 / (2.0 * D * r_pore_m)
    return hindrance / (channel + access)


def equilibration(V_m3, N_pores, p_pore, tau_life_s):
    """Return (tau_eq_s, peak_fraction) for well-mixed influx through N pores."""
    total_cond = N_pores * p_pore  # m^3/s
    if total_cond <= 0:
        return float("inf"), 0.0
    tau_eq = V_m3 / total_cond
    frac = 1.0 - math.exp(-tau_life_s / tau_eq)
    return tau_eq, frac


def healthy_pept1_conc_uM(C_ext_uM, AR_lin, Km_uM):
    """Unvalidated healthy-cell KPV accumulation heuristic."""
    C_in_max = AR_lin * Km_uM
    return C_in_max * C_ext_uM / (Km_uM + C_ext_uM)


def selectivity_record(C_pore_uM, C_in_healthy_uM):
    """Return an explicit strict-JSON representation of the heuristic ratio.

    A zero healthy-cell baseline makes the mathematical ratio positive infinity.
    JSON has no numeric infinity, so the ratio is null and the adjacent state field
    distinguishes that value from missing or unknown data. C_pore_uM is the modeled
    passive pore contribution, not total pyroptotic-cell accumulation.
    """
    if C_pore_uM < 0 or C_in_healthy_uM < 0:
        raise ValueError("Concentrations must be non-negative")
    if C_in_healthy_uM == 0 and C_pore_uM == 0:
        return {
            "selectivity_ratio": None,
            "selectivity_ratio_state": "undefined_zero_over_zero",
            "heuristic_ratio_ge_3x": False,
        }
    if C_in_healthy_uM == 0:
        return {
            "selectivity_ratio": None,
            "selectivity_ratio_state": "positive_infinity_zero_healthy_baseline",
            "heuristic_ratio_ge_3x": True,
        }
    ratio = C_pore_uM / C_in_healthy_uM
    return {
        "selectivity_ratio": ratio,
        "selectivity_ratio_state": "finite",
        "heuristic_ratio_ge_3x": ratio >= HEURISTIC_RATIO_THRESHOLD,
    }


def naive_flux_limited_conc_uM(N_pores, p_pore, C_ext_uM, tau_life_s, V_m3):
    """Naive pore-influx 'moles in over lifetime / cell volume' assuming a FIXED
    extracellular gradient (no intracellular build-up). This is an upper bound for
    the modeled passive pore contribution that ignores saturation; comparing it to
    C_ext shows when the well-mixed compartment approaches equilibrium."""
    C_ext_molm3 = C_ext_uM * UM_TO_MOL_PER_M3
    moles_in = N_pores * p_pore * C_ext_molm3 * tau_life_s  # mol
    conc_molm3 = moles_in / V_m3
    return conc_molm3 * MOL_PER_M3_TO_UM, moles_in


# ===================== central deterministic pass =====================

def central_values(kpv, pore, mac, pk, routes):
    D = kpv["aqueous_diffusion_coefficient_m2_per_s"]["central"]
    H = kpv["pore_hindrance_factor"]["central"]
    r_pore = (pore["inner_diameter_nm"]["central"] * 1e-9) / 2.0
    L_pore = pore["channel_length_nm"]["central"] * 1e-9
    N_pores = pore["pores_per_pyroptotic_cell"]["central"]
    tau_life = pore["open_lifetime_seconds"]["central"]
    V_m3 = mac["cell_volume_um3"]["central"] * 1e-18
    Km = pk["pept1_kpv_kinetics"]["Km_used_uM"]["central"]
    effective_proxy_uM = (
        pk["kpv_cell_assay_effective_concentration_proxy"]["central_nM"] * NM_TO_UM
    )

    p_pore = pore_permeability_m3_s(D, r_pore, L_pore, H)
    tau_eq, frac = equilibration(V_m3, N_pores, p_pore, tau_life)

    scenarios = pk["pept1_expression_scenarios"]
    out = {
        "selectivity_ratio_null_semantics": {
            "positive_infinity": {
                "condition": "selectivity_ratio_state is positive_infinity_zero_healthy_baseline",
                "meaning": "positive infinity",
                "not_missing_data": True,
            },
            "undefined": {
                "condition": "selectivity_ratio_state is undefined_zero_over_zero",
                "meaning": "undefined 0/0",
                "not_missing_data": True,
            },
        },
        "pore_permeability_m3_per_s": p_pore,
        "pore_hindrance_factor": H,
        "equilibration_time_constant_s": tau_eq,
        "equilibration_peak_fraction_central": frac,
        "central_pores_per_cell": N_pores,
        "central_pore_lifetime_s": tau_life,
        "central_cell_volume_um3": mac["cell_volume_um3"]["central"],
        "cell_assay_effective_concentration_proxy_uM": effective_proxy_uM,
        "Km_uM": Km,
        "routes": {},
    }
    for rn in ROUTE_NAMES:
        C_ext = routes[rn]["C_ext_synovial_uM"]["central"]
        C_pore = C_ext * frac
        naive_uM, moles_in = naive_flux_limited_conc_uM(N_pores, p_pore, C_ext, tau_life, V_m3)
        sel = {}
        for sname in SCENARIO_NAMES:
            AR = scenarios[sname]["AR_lin"]
            C_in_healthy = healthy_pept1_conc_uM(C_ext, AR, Km)
            sel[sname] = {
                "AR_lin": AR,
                "C_in_healthy_uM": C_in_healthy,
                **selectivity_record(C_pore, C_in_healthy),
            }
        out["routes"][rn] = {
            "C_ext_synovial_uM": C_ext,
            "modeled_passive_pore_contribution_uM": C_pore,
            "ratio_over_effective_concentration_proxy": C_pore / effective_proxy_uM,
            "naive_flux_limited_uM_UPPERBOUND": naive_uM,
            "naive_over_C_ext": naive_uM / C_ext if C_ext > 0 else float("inf"),
            "moles_in_over_lifetime_mol": moles_in,
            "pore_vs_healthy_heuristic_by_pept1_scenario": sel,
        }
    return out


# ===================== Monte Carlo =====================

def monte_carlo(kpv, pore, mac, pk, routes):
    ratio_samples = {rn: [] for rn in ROUTE_NAMES}
    frac_samples = []
    tau_eq_samples = []

    D_lo = kpv["aqueous_diffusion_coefficient_m2_per_s"]["lower"]
    D_hi = kpv["aqueous_diffusion_coefficient_m2_per_s"]["upper"]
    H_lo = kpv["pore_hindrance_factor"]["lower"]
    H_hi = kpv["pore_hindrance_factor"]["upper"]
    d_lo = pore["inner_diameter_nm"]["lower"]
    d_hi = pore["inner_diameter_nm"]["upper"]
    L_lo = pore["channel_length_nm"]["lower"]
    L_hi = pore["channel_length_nm"]["upper"]
    N_lo = pore["pores_per_pyroptotic_cell"]["lower"]
    N_hi = pore["pores_per_pyroptotic_cell"]["upper"]
    t_lo = pore["open_lifetime_seconds"]["lower"]
    t_hi = pore["open_lifetime_seconds"]["upper"]
    V_lo = mac["cell_volume_um3"]["lower"]
    V_hi = mac["cell_volume_um3"]["upper"]
    proxy_lo = pk["kpv_cell_assay_effective_concentration_proxy"]["lower_nM"]
    proxy_hi = pk["kpv_cell_assay_effective_concentration_proxy"]["upper_nM"]

    for _ in range(N_MC):
        D = log_uniform(D_lo, D_hi)
        H = log_uniform(H_lo, H_hi)
        r_pore = (log_uniform(d_lo, d_hi) * 1e-9) / 2.0
        L_pore = log_uniform(L_lo, L_hi) * 1e-9
        N_pores = log_uniform(N_lo, N_hi)
        tau_life = log_uniform(t_lo, t_hi)
        V_m3 = log_uniform(V_lo, V_hi) * 1e-18
        effective_proxy_uM = log_uniform(proxy_lo, proxy_hi) * NM_TO_UM

        p_pore = pore_permeability_m3_s(D, r_pore, L_pore, H)
        tau_eq, frac = equilibration(V_m3, N_pores, p_pore, tau_life)
        frac_samples.append(frac)
        tau_eq_samples.append(tau_eq)

        for rn in ROUTE_NAMES:
            c_lo = routes[rn]["C_ext_synovial_uM"]["lower"]
            c_hi = routes[rn]["C_ext_synovial_uM"]["upper"]
            C_ext = log_uniform(c_lo, c_hi)
            C_pore = C_ext * frac
            ratio_samples[rn].append(C_pore / effective_proxy_uM)

    mc = {
        "n_samples": N_MC,
        "sampling_policy": "Independent log-uniform design-space sampling over declared positive bounds. The resulting fractions are diagnostics, not calibrated probabilities.",
        "equilibration_fraction": stats(frac_samples),
        "equilibration_tau_eq_s": stats(tau_eq_samples),
        "ratio_over_effective_concentration_proxy": {},
        "fraction_design_space_draws_clearing_proxy": {},
    }
    for rn in ROUTE_NAMES:
        mc["ratio_over_effective_concentration_proxy"][rn] = stats(ratio_samples[rn])
        mc["fraction_design_space_draws_clearing_proxy"][rn] = (
            sum(1 for x in ratio_samples[rn] if x >= 1.0) / len(ratio_samples[rn])
        )
    return mc


# ===================== robustness sweep (M3) =====================

def robustness_sweep(kpv, pore, mac, pk, routes):
    D = kpv["aqueous_diffusion_coefficient_m2_per_s"]["central"]
    H = kpv["pore_hindrance_factor"]["central"]
    r_pore = (pore["inner_diameter_nm"]["central"] * 1e-9) / 2.0
    L_pore = pore["channel_length_nm"]["central"] * 1e-9
    V_m3 = mac["cell_volume_um3"]["central"] * 1e-18
    effective_proxy_uM = (
        pk["kpv_cell_assay_effective_concentration_proxy"]["central_nM"] * NM_TO_UM
    )
    p_pore = pore_permeability_m3_s(D, r_pore, L_pore, H)

    lifetimes = [60, 300, 900, 1800]     # 1, 5, 15, 30 min
    pore_counts = [1, 10, 100, 1000, 10000]
    C_ia = routes["intra_articular"]["C_ext_synovial_uM"]["central"]
    C_sc = routes["subcutaneous"]["C_ext_synovial_uM"]["central"]
    C_oral = routes["oral"]["C_ext_synovial_uM"]["central"]

    grid = []
    for N in pore_counts:
        for tl in lifetimes:
            tau_eq, frac = equilibration(V_m3, N, p_pore, tl)
            grid.append({
                "pores_per_cell": N,
                "lifetime_s": tl,
                "tau_eq_s": tau_eq,
                "equilibration_fraction": frac,
                "IA_modeled_passive_pore_contribution_uM": C_ia * frac,
                "IA_ratio_over_effective_concentration_proxy": (
                    C_ia * frac
                ) / effective_proxy_uM,
                "IA_clears_effective_concentration_proxy": (
                    C_ia * frac
                ) / effective_proxy_uM >= 1.0,
                "SC_modeled_passive_pore_contribution_uM": C_sc * frac,
                "SC_ratio_over_effective_concentration_proxy": (
                    C_sc * frac
                ) / effective_proxy_uM,
                "SC_clears_effective_concentration_proxy": (
                    C_sc * frac
                ) / effective_proxy_uM >= 1.0,
                "oral_modeled_passive_pore_contribution_uM": C_oral * frac,
                "oral_ratio_over_effective_concentration_proxy": (
                    C_oral * frac
                ) / effective_proxy_uM,
                "oral_clears_effective_concentration_proxy": (
                    C_oral * frac
                ) / effective_proxy_uM >= 1.0,
            })
    return {
        "note": "Deterministic lifetime x pores-per-cell diagnostic with all other pore, cell, route-concentration, and effective-concentration-proxy inputs held central. The one-pore rows are explicit stress cases outside the main 10-10000-pore design range. The grid does not assign plausibility to a pore-count value or establish efficacy.",
        "pore_count_scope": {
            "main_design_range": [10, 10000],
            "stress_case": 1,
            "stress_case_is_outside_main_range": True,
        },
        "pore_permeability_m3_per_s": p_pore,
        "pore_hindrance_factor": H,
        "grid": grid,
    }


# ===================== selectivity grid + sensitivity (A2) =====================

def classify_heuristic_ratio_pattern(n_clear, n_cases):
    if n_clear == n_cases:
        return "always_at_or_above_3x_in_declared_grid"
    if n_clear == 0:
        return "never_at_or_above_3x_in_declared_grid"
    return "crosses_3x_in_some_declared_grid_cases"


def selectivity_grid(pk, routes, frac_central):
    km_bounds = pk["pept1_kpv_kinetics"]["Km_used_uM"]
    scenarios = pk["pept1_expression_scenarios"]
    central_grid = {}
    sensitivity_grid = {}
    sensitivity_summary = {}

    for rn in ROUTE_NAMES:
        C_ext = routes[rn]["C_ext_synovial_uM"]["central"]
        Km = km_bounds["central"]
        C_pore = C_ext * frac_central
        row = {
            "C_ext_uM": C_ext,
            "modeled_passive_pore_contribution_uM": C_pore,
            "by_scenario": {},
        }
        for sname in SCENARIO_NAMES:
            AR = scenarios[sname]["AR_lin"]
            C_in_healthy = healthy_pept1_conc_uM(C_ext, AR, Km)
            row["by_scenario"][sname] = {
                "AR_lin": AR,
                "C_in_healthy_uM": C_in_healthy,
                **selectivity_record(C_pore, C_in_healthy),
            }
        central_grid[rn] = row

        cases = []
        by_scenario = {}
        for sname in SCENARIO_NAMES:
            by_scenario[sname] = {
                "case_count": 0,
                "heuristic_ratio_ge_3x_cases": 0,
                "finite_ratios": [],
                "positive_infinity_cases": 0,
                "undefined_cases": 0,
            }
        for concentration_bound in BOUND_NAMES:
            sensitivity_C_ext = routes[rn]["C_ext_synovial_uM"][concentration_bound]
            sensitivity_C_pore = sensitivity_C_ext * frac_central
            for km_bound in BOUND_NAMES:
                sensitivity_Km = km_bounds[km_bound]
                for sname in SCENARIO_NAMES:
                    AR = scenarios[sname]["AR_lin"]
                    C_in_healthy = healthy_pept1_conc_uM(
                        sensitivity_C_ext, AR, sensitivity_Km
                    )
                    ratio_record = selectivity_record(
                        sensitivity_C_pore, C_in_healthy
                    )
                    cases.append({
                        "route_concentration_bound": concentration_bound,
                        "Km_bound": km_bound,
                        "PepT1_scenario": sname,
                        "C_ext_uM": sensitivity_C_ext,
                        "Km_uM": sensitivity_Km,
                        "AR_lin": AR,
                        "modeled_passive_pore_contribution_uM": sensitivity_C_pore,
                        "C_in_healthy_uM": C_in_healthy,
                        **ratio_record,
                    })
                    summary = by_scenario[sname]
                    summary["case_count"] += 1
                    if ratio_record["heuristic_ratio_ge_3x"]:
                        summary["heuristic_ratio_ge_3x_cases"] += 1
                    if ratio_record["selectivity_ratio_state"] == "finite":
                        summary["finite_ratios"].append(
                            ratio_record["selectivity_ratio"]
                        )
                    elif (
                        ratio_record["selectivity_ratio_state"]
                        == "positive_infinity_zero_healthy_baseline"
                    ):
                        summary["positive_infinity_cases"] += 1
                    else:
                        summary["undefined_cases"] += 1

        route_summary = {}
        for sname in SCENARIO_NAMES:
            raw = by_scenario[sname]
            finite = raw.pop("finite_ratios")
            raw["finite_min_selectivity_ratio"] = min(finite) if finite else None
            raw["finite_max_selectivity_ratio"] = max(finite) if finite else None
            raw["heuristic_ratio_pattern"] = classify_heuristic_ratio_pattern(
                raw["heuristic_ratio_ge_3x_cases"], raw["case_count"]
            )
            route_summary[sname] = raw
        sensitivity_grid[rn] = cases
        sensitivity_summary[rn] = route_summary

    return {
        "selectivity_ratio_null_semantics": {
            "positive_infinity": {
                "condition": "selectivity_ratio_state is positive_infinity_zero_healthy_baseline",
                "meaning": "positive infinity",
                "not_missing_data": True,
            },
            "undefined": {
                "condition": "selectivity_ratio_state is undefined_zero_over_zero",
                "meaning": "undefined 0/0",
                "not_missing_data": True,
            },
        },
        "note": "S_model = modeled passive pore contribution / modeled healthy-cell accumulation under an unvalidated heuristic. Concurrent PepT1 transport in the pyroptotic cell is not modeled, so S_model is not total-cell pyroptotic-versus-healthy selectivity. The deterministic sensitivity grid crosses each declared route concentration bound with each declared Km bound and each PepT1-expression scenario. The scenarios are unweighted and are not probabilities or physiological estimates.",
        "decision_boundary": "A modeled ratio >=3x is an equation-response diagnostic, not physiological selectivity or an A2 qualification. A2 remains unresolved until synovial-macrophage PepT1 function and a matched healthy-cell accumulation baseline are measured.",
        "caveat_S_is_heuristic": "The healthy-cell curve C_in,healthy = C_in_max*C_ext/(Km+C_ext) borrows a rate-saturation shape as an accumulation heuristic. Without measured Vmax, efflux, turnover, degradation, membrane potential, and proton coupling in synovial macrophages, it is not a validated steady state or a proved upper/lower bound. Ratios can move in either direction; the grid is a diagnostic.",
        "caveat_PD_timing": "This is a transport model. KPV is framed as an upstream NLRP3/NF-kB inhibitor, while GSDMD pore formation is downstream of inflammasome activation. The model does not resolve residual targetable activity, cytokine-release timing, or efficacy; pore influx is therefore not therapeutic-timing sufficiency.",
        "central_Km_uM": km_bounds["central"],
        "sensitivity_dimensions": {
            "route_concentration_bounds": BOUND_NAMES,
            "Km_bounds": BOUND_NAMES,
            "PepT1_scenarios": SCENARIO_NAMES,
            "cases_per_route": len(BOUND_NAMES) * len(BOUND_NAMES) * len(SCENARIO_NAMES),
        },
        "fixed_during_sensitivity": {
            "equilibration_peak_fraction": frac_central,
            "varied_parameters": ["route C_ext", "Km_used", "PepT1 AR scenario"],
            "all_other_inputs": "central deterministic values, including pore hindrance factor 1.0",
        },
        "central_grid": central_grid,
        "sensitivity_grid": sensitivity_grid,
        "sensitivity_summary": sensitivity_summary,
    }


# ===================== verdict logic =====================

def verdicts(central, mc, selg):
    """Per-route A1 result plus unresolved A2 evidence state."""
    v = {}
    for rn in ROUTE_NAMES:
        r = central["routes"][rn]
        ratio = r["ratio_over_effective_concentration_proxy"]
        sample_fraction = mc["fraction_design_space_draws_clearing_proxy"][rn]
        # Preregistered engineering traffic-light rule, not a clinical probability.
        if ratio >= 10 and sample_fraction >= 0.9:
            a1 = "GREEN"
        elif ratio >= 1.0 and sample_fraction >= 0.5:
            a1 = "YELLOW"
        else:
            a1 = "RED"
        sc = selg["central_grid"][rn]["by_scenario"]
        n_meaningful = sum(1 for s in SCENARIO_NAMES
                           if sc[s]["heuristic_ratio_ge_3x"])
        a2 = "UNRESOLVED-unmeasured-PepT1-baseline"
        if a1 == "RED":
            combined = "NOT-QUALIFIED-A1"
        else:
            combined = "NOT-QUALIFIED-A2-UNRESOLVED"
        v[rn] = {
            "A1_exposure_proxy_state": a1,
            "A1_metric": "modeled passive pore contribution / extracellular cell-assay effective-concentration proxy",
            "A1_engineering_rule": "GREEN if central ratio >=10 and sampled fraction >=0.9; YELLOW if central ratio >=1 and sampled fraction >=0.5; otherwise RED",
            "A1_ratio_over_effective_concentration_proxy_central": ratio,
            "A1_fraction_design_space_draws_clearing_proxy": sample_fraction,
            "A2_pore_vs_healthy_baseline": a2,
            "A2_central_scenarios_with_heuristic_ratio_ge_3x": n_meaningful,
            "A2_sensitivity_summary": selg["sensitivity_summary"][rn],
            "combined_route_verdict": combined,
        }
    return v


def overall_verdict(v):
    any_green_a1 = any(v[r]["A1_exposure_proxy_state"] == "GREEN" for r in v)
    any_yellow_a1 = any(v[r]["A1_exposure_proxy_state"] == "YELLOW" for r in v)
    if any_green_a1:
        overall_code = "YELLOW-A2-unresolved"
    elif any_yellow_a1:
        overall_code = "YELLOW-A1-limited"
    else:
        overall_code = "RED-A1"
    a1_states = ", ".join(
        f"{route}={v[route]['A1_exposure_proxy_state']}" for route in ROUTE_NAMES
    )
    text = (
        f"{overall_code}. Computed A1 engineering states: {a1_states}. "
        "A1 compares the modeled passive pore contribution with an extracellular "
        "cell-assay effective-concentration proxy; it does not establish target "
        "engagement or efficacy. A2 remains unresolved because synovial-macrophage "
        "PepT1 function and the matched healthy-cell accumulation baseline are "
        "unmeasured. The heuristic grid reports every equation-response corner, "
        "including modeled ratios >=3x, but none qualifies a route."
    )
    return {
        "overall": overall_code,
        "overall_policy": "Derived from the best A1 engineering state, then capped below GREEN while A2 remains empirically unresolved",
        "any_route_A1_GREEN": any_green_a1,
        "any_route_QUALIFIES_both_filters": False,
        "A2_qualification_blocker": "unmeasured synovial-macrophage PepT1 function and healthy-cell accumulation baseline",
        "statement": text,
    }


def main():
    check_runtime()
    kpv, pore, mac, pk, routes = load_inputs()

    central = central_values(kpv, pore, mac, pk, routes)
    mc = monte_carlo(kpv, pore, mac, pk, routes)
    selg = selectivity_grid(
        pk, routes, central["equilibration_peak_fraction_central"]
    )
    robust = robustness_sweep(kpv, pore, mac, pk, routes)
    v = verdicts(central, mc, selg)
    overall = overall_verdict(v)

    # Known mathematical infinity is encoded explicitly by selectivity_record().
    # Reject any unexpected non-finite result instead of silently converting it.
    def _json_safe(o):
        if isinstance(o, float):
            if not math.isfinite(o):
                raise ValueError(f"Unexpected non-finite output: {o!r}")
            return o
        if isinstance(o, dict):
            return {k: _json_safe(val) for k, val in o.items()}
        if isinstance(o, list):
            return [_json_safe(val) for val in o]
        return o

    (OUTPUTS / "central_results.json").write_text(json.dumps(_json_safe(central), indent=2, allow_nan=False))
    (OUTPUTS / "monte_carlo.json").write_text(json.dumps(_json_safe(mc), indent=2, allow_nan=False))
    (OUTPUTS / "selectivity_grid.json").write_text(json.dumps(_json_safe(selg), indent=2, allow_nan=False))
    (OUTPUTS / "robustness_sweep.json").write_text(json.dumps(_json_safe(robust), indent=2, allow_nan=False))
    (OUTPUTS / "verdicts.json").write_text(json.dumps(
        _json_safe({"per_route": v, "overall": overall}), indent=2, allow_nan=False))

    write_summary(central, mc, selg, robust, v, overall)
    print("comp-042 complete. Overall:", overall["overall"])
    for rn in ROUTE_NAMES:
        print(f"  {rn}: A1={v[rn]['A1_exposure_proxy_state']} "
              f"(ratio/proxy central="
              f"{v[rn]['A1_ratio_over_effective_concentration_proxy_central']:.3g}, "
              f"sample fraction={v[rn]['A1_fraction_design_space_draws_clearing_proxy']:.2f}), "
              f"A2={v[rn]['A2_pore_vs_healthy_baseline']} -> "
              f"{v[rn]['combined_route_verdict']}")
    print(f"  equilibration tau_eq central = {central['equilibration_time_constant_s']:.2f} s")


def fmt(x, sig=3):
    if x is None:
        return "null"
    if x == 0:
        return "0"
    return f"{x:.{sig}g}"


def fmt_selectivity(record, sig=3):
    if record["selectivity_ratio_state"] == "positive_infinity_zero_healthy_baseline":
        return "∞"
    return fmt(record["selectivity_ratio"], sig)


def write_summary(central, mc, selg, robust, v, overall):
    L = []
    L.append("# comp-042 -- KPV self-delivery through GSDMD pyroptotic pores vs. the PepT1 baseline\n")
    L.append("**Auto-generated by `analyze.py` (stdlib-only, deterministic, seed 42).**\n")
    L.append(f"## Overall verdict: {overall['overall']}\n")
    L.append(overall["statement"] + "\n")

    L.append("## Core physics\n")
    L.append(f"- Per-pore permeability (with access resistance): {fmt(central['pore_permeability_m3_per_s'])} m^3/s")
    L.append(
        f"- Equilibration time constant tau_eq (central: "
        f"{fmt(central['central_pores_per_cell'])} pores, "
        f"{fmt(central['central_cell_volume_um3'])} um3): "
        f"**{fmt(central['equilibration_time_constant_s'])} s** "
        f"-> the modeled passive pore contribution reaches "
        f"{fmt(100*central['equilibration_peak_fraction_central'],4)}% "
        f"of extracellular within a "
        f"{fmt(central['central_pore_lifetime_s'])} s lifetime."
    )
    L.append(f"- Monte Carlo equilibration fraction: median "
             f"{fmt(mc['equilibration_fraction']['median'])}, p5 {fmt(mc['equilibration_fraction']['p5'])}\n")
    L.append(
        "Interpretation within the central model: the modeled passive pore contribution "
        "is capped at the extracellular value. The naive fixed-gradient calculation is retained only "
        "as an upper-bound diagnostic. Pore-lifetime conclusions apply only to the "
        "declared solute, parameter, lifetime, and pore-count regimes.\n"
    )

    L.append("## Metric 1 -- modeled passive pore contribution / extracellular cell-assay effective-concentration proxy (A1)\n")
    L.append("| Route | synovial [KPV] (uM) | modeled passive pore contribution (uM) | / 10 nM proxy | sampled design-space fraction >= proxy | A1 engineering state |")
    L.append("|---|---|---|---|---|---|")
    for rn in ROUTE_NAMES:
        r = central["routes"][rn]
        L.append(f"| {rn.replace('_',' ')} | {fmt(r['C_ext_synovial_uM'])} | "
                 f"{fmt(r['modeled_passive_pore_contribution_uM'])} | "
                 f"{fmt(r['ratio_over_effective_concentration_proxy'])}x | "
                 f"{fmt(mc['fraction_design_space_draws_clearing_proxy'][rn])} | "
                 f"{v[rn]['A1_exposure_proxy_state']} |")
    L.append("")
    L.append("The 10 nM reference is the lowest extracellular concentration reported effective "
             "in a PepT1-positive cell assay. It is not an intracellular IC50. The sampled "
             "fractions come from unweighted log-uniform design-space draws and are not "
             "calibrated probabilities. A1 therefore ranks modeled exposure against an "
             "engineering proxy; it does not establish target engagement, therapeutic timing, "
             "or efficacy.\n")
    L.append("Route concentrations are design inputs, not established synovial exposures: "
             "IA is arithmetic from unsourced dose and compartment-volume assumptions; "
             "SC and oral are named PK design spaces.\n")

    L.append("## Metric 2 -- heuristic ratio over the PepT1 comparator (A2 diagnostic)\n")
    L.append("S_model = modeled passive pore contribution / modeled intracellular[healthy]. "
             "Concurrent PepT1 transport in the pyroptotic cell is not modeled, so this "
             "is not total-cell pyroptotic-versus-healthy selectivity. AR_lin is an "
             "unweighted PepT1 design scenario, not a measured synovial-macrophage "
             "accumulation ratio.\n")
    L.append("| Route | PepT1 absent | low (AR 0.3) | moderate (AR 1) | high (AR 3) |")
    L.append("|---|---|---|---|---|")
    for rn in ROUTE_NAMES:
        sc = selg["central_grid"][rn]["by_scenario"]
        L.append(f"| {rn.replace('_',' ')} | "
                 f"{fmt_selectivity(sc['absent'])} | "
                 f"{fmt_selectivity(sc['low'])} | "
                 f"{fmt_selectivity(sc['moderate'])} | "
                 f"{fmt_selectivity(sc['high'])} |")
    L.append("")
    L.append("These are equation-response diagnostics, not physiological selectivity or an "
             "A2 qualification. The declared "
             "route-concentration and Km bounds are crossed below; the PepT1-expression "
             "scenarios are unweighted and the healthy-cell accumulation curve is heuristic. "
             "Which scenario describes synovial macrophages is unknown, so A2 remains unresolved.\n")
    L.append("### A2 sensitivity: route concentration x Km\n")
    L.append("| Route | PepT1 scenario | heuristic ratio >=3x cases / 9 | finite S_model range | pattern |")
    L.append("|---|---|---|---|---|")
    for rn in ROUTE_NAMES:
        for sname in SCENARIO_NAMES:
            s = selg["sensitivity_summary"][rn][sname]
            if s["positive_infinity_cases"] == s["case_count"]:
                value_range = "∞ (zero healthy baseline)"
            else:
                value_range = (
                    f"{fmt(s['finite_min_selectivity_ratio'])}–"
                    f"{fmt(s['finite_max_selectivity_ratio'])}"
                )
            L.append(
                f"| {rn.replace('_',' ')} | {sname} | "
                f"{s['heuristic_ratio_ge_3x_cases']} / {s['case_count']} | "
                f"{value_range} | {s['heuristic_ratio_pattern']} |"
            )
    L.append("")
    L.append("A >=3x point shows what the heuristic equation permits; it does not demonstrate "
             "pore-specific selectivity. The absent-PepT1 rows use "
             "`selectivity_ratio: null` in strict JSON with "
             "`selectivity_ratio_state: positive_infinity_zero_healthy_baseline`; this means "
             "mathematical positive infinity, not missing data.\n")
    L.append("**Pharmacodynamic-timing caveat:** even where transport is "
             "sufficient, KPV is an *upstream* inflammasome inhibitor, whereas GSDMD pores form "
             "*downstream* of inflammasome firing. So a payload arriving through the pore arrives "
             "after inflammasome activation -- transport sufficiency does NOT imply "
             "therapeutic-timing sufficiency for KPV specifically. The model does not resolve "
             "residual targetable activity or cytokine-release timing. This is the second independent "
             "reason KPV is poorly matched to a clean proof-of-concept for pore self-delivery "
             "(the first being PepT1 confounding). A downstream-acting, transporter-orphan "
             "payload is the cleaner probe.\n")

    L.append("## Metric 3 -- robustness sweep (pore lifetime x pores/cell)\n")
    L.append("The one-pore rows are stress cases outside the main 10–10,000-pore design range. "
             "All route concentrations remain the design inputs described above.\n")
    L.append("| pores/cell | lifetime (s) | tau_eq (s) | equilib. frac | route | modeled passive pore contribution (uM) | ratio / proxy | clears proxy |")
    L.append("|---|---|---|---|---|---|---|---|")
    for g in robust["grid"]:
        for route_label, field_prefix in [
            ("intra articular", "IA"),
            ("subcutaneous", "SC"),
            ("oral", "oral"),
        ]:
            L.append(
                f"| {g['pores_per_cell']} | {g['lifetime_s']} | "
                f"{fmt(g['tau_eq_s'])} | {fmt(g['equilibration_fraction'])} | "
                f"{route_label} | "
                f"{fmt(g[f'{field_prefix}_modeled_passive_pore_contribution_uM'])} | "
                f"{fmt(g[f'{field_prefix}_ratio_over_effective_concentration_proxy'])} | "
                f"{g[f'{field_prefix}_clears_effective_concentration_proxy']} |"
            )
    L.append("")
    ia_clear = sum(
        1 for g in robust["grid"]
        if g["IA_clears_effective_concentration_proxy"]
    )
    sc_clear = sum(
        1 for g in robust["grid"]
        if g["SC_clears_effective_concentration_proxy"]
    )
    oral_clear = sum(
        1 for g in robust["grid"]
        if g["oral_clears_effective_concentration_proxy"]
    )
    L.append(
        f"With all non-swept inputs held central, IA clears the exposure proxy in "
        f"{ia_clear}/{len(robust['grid'])} grid cells and SC in "
        f"{sc_clear}/{len(robust['grid'])}; oral clears it in "
        f"{oral_clear}/{len(robust['grid'])}. Equilibration fraction varies across the grid; "
        "the analysis assigns no plausibility weight to pore counts because per-cell count "
        "is unmeasured.\n"
    )

    L.append("## Per-route qualification\n")
    L.append("| Route | A1 | A2 | Combined |")
    L.append("|---|---|---|---|")
    for rn in ROUTE_NAMES:
        L.append(f"| {rn.replace('_',' ')} | {v[rn]['A1_exposure_proxy_state']} | "
                 f"{v[rn]['A2_pore_vs_healthy_baseline']} | "
                 f"{v[rn]['combined_route_verdict']} |")
    L.append("")
    L.append(
        "No route qualifies while A2 is empirically unresolved. The per-route table above "
        "reports the computed A1 state; heuristic >=3x A2 points remain diagnostics until "
        "a matched healthy-cell comparator is measured.\n"
    )

    L.append("## The single biggest limitation\n")
    L.append("Synovial-macrophage PepT1 (SLC15A1) functional expression is uncharacterized. It is "
             "the dominant empirical gap in whether the pore beats the constitutive KPV import "
             "route; the heuristic ratio also varies with C_ext/Km. Everything in the A2 column "
             "is conditional on the unmeasured healthy-cell baseline. KPV is, in "
             "effect, a poor payload to demonstrate pore-selectivity because it already has an "
             "independent transporter route. A transporter-orphan membrane-impermeant payload "
             "would be the cleaner selectivity test.\n")

    (OUTPUTS / "summary.md").write_text("\n".join(L))


if __name__ == "__main__":
    main()
