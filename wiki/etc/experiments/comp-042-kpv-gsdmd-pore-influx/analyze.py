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
dying flare-driving cells. KPV (Lys-Pro-Val), which inhibits intracellular NLRP3
and NF-kB, is proposed as the ideal payload.

Two assumptions are load-bearing:
  A1 -- FLUX SUFFICIENCY: over a pore's short open lifetime (1-30 min), does enough
        KPV diffuse in to clear its intracellular IC50 (~10 nM, Dalmasso 2008)?
  A2 -- SELECTIVITY over the PepT1 baseline (the quietly weak one): KPV ALREADY
        enters cells (including immune cells) via the PepT1 transporter (SLC15A1),
        independent of any pore. So the pore only confers SELECTIVITY if it delivers
        meaningfully MORE than PepT1 already does AND healthy (non-pyroptotic) cells
        do not already admit KPV via PepT1. The crux is synovial-macrophage PepT1
        expression -- uncharacterized in the literature.

THE MODEL (transport / mass-balance; NO MD, NO docking)
-------------------------------------------------------
Per-pore diffusive permeability of a short wide cylindrical aperture, INCLUDING
access (convergence) resistance (Hille / Hall):

    p_pore = H * D * pi * r_p^2 / (L_pore + pi*r_p/2)          [m^3/s]

where H is the steric-electrostatic hindrance factor (~1: KPV radius ~0.5 nm is
15-40x smaller than the pore radius, and the pore conduit is negatively charged and
FAVORS KPV's +1 charge, Xia 2021). The access term pi*r_p/2 (~15.7 nm at r_p=10 nm)
dominates the channel term L_pore (~7 nm) -- i.e. this is an access-resistance-
limited pore, so the exact channel length is low-sensitivity.

Total pore conductance of a pyroptotic cell = N_pores * p_pore. Treating the cell as
a well-mixed compartment of volume V, intracellular [KPV] approaches extracellular
[KPV] with a first-order EQUILIBRATION time constant:

    tau_eq = V / (N_pores * p_pore)
    C_in(t) = C_ext * (1 - exp(-t / tau_eq))
    peak C_in = C_ext * (1 - exp(-tau_life / tau_eq))

KEY PHYSICS RESULT: for a 20 nm pore, N_pores >= ~10, and a macrophage of ~3000 um3,
tau_eq is SECONDS to tens of seconds -- far shorter than the minutes-scale pore
lifetime. So the cell equilibrates its interior to the extracellular concentration
almost completely. The naive "moles-in over lifetime / cell volume" estimate (integral
of flux at a fixed gradient) OVER-shoots C_ext by orders of magnitude, which simply
confirms the cell saturates: peak intracellular [KPV] is CAPPED at C_ext. This
quantitatively answers gsdmd-pore-delivery-paradox.md Open Question #4.

PepT1 BASELINE (present in BOTH pyroptotic and healthy cells):
Healthy-cell steady-state KPV via Michaelis-Menten uptake balanced by efflux/turnover
is written as a saturating accumulation:

    C_in,healthy(C_ext) = C_in_max_healthy * C_ext / (Km + C_ext)
    C_in_max_healthy    = AR_lin * Km    (so low-C_ext slope AR_lin = C_in,healthy/C_ext)

AR_lin (the dimensionless linear-regime accumulation ratio) encodes the UNKNOWN
synovial-macrophage PepT1 functional expression (scenarios: absent / low / moderate /
high-concentrative). In the pyroptotic cell the huge pore conductance short-circuits
PepT1 and clamps C_in,pyroptotic = C_ext.

SELECTIVITY RATIO  S = C_in,pyroptotic / C_in,healthy = C_ext / [C_in_max_healthy * C_ext/(Km+C_ext)]
                     = (Km + C_ext) / C_in_max_healthy.
  - Linear regime (SC/oral, C_ext << Km):  S ~= Km/C_in_max_healthy = 1/AR_lin  -> fully gated by PepT1 expression.
  - Saturating regime (IA, C_ext >> Km):   S ~= C_ext/C_in_max_healthy -> can rise, but C_in_max_healthy is unknown.
Either way S is set by unknown synovial-macrophage PepT1 kinetics.

METRICS (>=3 orthogonal) evaluated per dosing route (IA / SC / oral):
  M1 -- peak intracellular [KPV] / IC50        (flux/therapeutic sufficiency; A1)
  M2 -- selectivity ratio S vs healthy cell    (pore benefit over PepT1 baseline; A2)
  M3 -- robustness: sweep pore lifetime (1-30 min) x pores/cell (10-1e4)

DECISION FILTER: a route "passes" only if it clears BOTH a therapeutic threshold
(M1 >= 1x IC50) AND a meaningful selectivity threshold (M2 >= 3x) with the named
assumptions holding.
"""

import json
import math
import random
from pathlib import Path

# ----- repro -----
SEED = 42
random.seed(SEED)

# ----- paths -----
HERE = Path(__file__).resolve().parent
INPUTS = HERE / "inputs"
OUTPUTS = HERE / "outputs"
OUTPUTS.mkdir(exist_ok=True, parents=True)

N_MC = 20000

# ----- unit helpers -----
UM_TO_MOL_PER_M3 = 1.0e-3   # 1 uM = 1e-6 mol/L = 1e-3 mol/m^3
MOL_PER_M3_TO_UM = 1.0e3    # inverse
NM_TO_UM = 1.0e-3


def load_inputs():
    kpv = json.loads((INPUTS / "kpv_properties.json").read_text())
    pore = json.loads((INPUTS / "pore_geometry.json").read_text())
    mac = json.loads((INPUTS / "macrophage_geometry.json").read_text())
    pk = json.loads((INPUTS / "pept1_and_ic50.json").read_text())
    routes = json.loads((INPUTS / "route_concentrations.json").read_text())
    return kpv, pore, mac, pk, routes


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
    """Healthy-cell steady-state intracellular [KPV] via PepT1 (saturating)."""
    C_in_max = AR_lin * Km_uM
    return C_in_max * C_ext_uM / (Km_uM + C_ext_uM)


def naive_flux_limited_conc_uM(N_pores, p_pore, C_ext_uM, tau_life_s, V_m3):
    """Naive 'moles in over lifetime / cell volume' assuming a FIXED extracellular
    gradient (no intracellular build-up). This is an UPPER BOUND that ignores
    saturation; comparing it to C_ext shows how badly the cell saturates."""
    C_ext_molm3 = C_ext_uM * UM_TO_MOL_PER_M3
    moles_in = N_pores * p_pore * C_ext_molm3 * tau_life_s  # mol
    conc_molm3 = moles_in / V_m3
    return conc_molm3 * MOL_PER_M3_TO_UM, moles_in


# ===================== central deterministic pass =====================

def central_values(kpv, pore, mac, pk, routes):
    D = kpv["aqueous_diffusion_coefficient_m2_per_s"]["central"]
    H = 1.0  # hindrance ~1 (justified in provenance)
    r_pore = (pore["inner_diameter_nm"]["central"] * 1e-9) / 2.0
    L_pore = pore["channel_length_nm"]["central"] * 1e-9
    N_pores = pore["pores_per_pyroptotic_cell"]["central"]
    tau_life = pore["open_lifetime_seconds"]["central"]
    V_m3 = mac["cell_volume_um3"]["central"] * 1e-18
    Km = pk["pept1_kpv_kinetics"]["Km_used_uM"]["central"]
    ic50_uM = pk["kpv_intracellular_ic50"]["central_nM"] * NM_TO_UM

    p_pore = pore_permeability_m3_s(D, r_pore, L_pore, H)
    tau_eq, frac = equilibration(V_m3, N_pores, p_pore, tau_life)

    scenarios = pk["pept1_expression_scenarios"]
    route_names = ["intra_articular", "subcutaneous", "oral"]

    out = {
        "pore_permeability_m3_per_s": p_pore,
        "equilibration_time_constant_s": tau_eq,
        "equilibration_peak_fraction_central": frac,
        "ic50_uM": ic50_uM,
        "Km_uM": Km,
        "routes": {},
    }
    for rn in route_names:
        C_ext = routes[rn]["C_ext_synovial_uM"]["central"]
        C_in_pyro = C_ext * frac  # equilibration-capped intracellular in pyroptotic cell
        naive_uM, moles_in = naive_flux_limited_conc_uM(N_pores, p_pore, C_ext, tau_life, V_m3)
        sel = {}
        for sname in ["absent", "low", "moderate", "high"]:
            AR = scenarios[sname]["AR_lin"]
            C_in_healthy = healthy_pept1_conc_uM(C_ext, AR, Km)
            if C_in_healthy <= 0:
                S = float("inf")
            else:
                S = C_in_pyro / C_in_healthy
            sel[sname] = {
                "AR_lin": AR,
                "C_in_healthy_uM": C_in_healthy,
                "selectivity_ratio": S,
            }
        out["routes"][rn] = {
            "C_ext_synovial_uM": C_ext,
            "C_in_pyroptotic_uM": C_in_pyro,
            "ratio_over_ic50": C_in_pyro / ic50_uM,
            "naive_flux_limited_uM_UPPERBOUND": naive_uM,
            "naive_over_C_ext": naive_uM / C_ext if C_ext > 0 else float("inf"),
            "moles_in_over_lifetime_mol": moles_in,
            "selectivity_by_pept1_scenario": sel,
        }
    return out


# ===================== Monte Carlo =====================

def monte_carlo(kpv, pore, mac, pk, routes):
    route_names = ["intra_articular", "subcutaneous", "oral"]
    ratio_samples = {rn: [] for rn in route_names}
    frac_samples = []
    tau_eq_samples = []

    D_lo = kpv["aqueous_diffusion_coefficient_m2_per_s"]["lower"]
    D_hi = kpv["aqueous_diffusion_coefficient_m2_per_s"]["upper"]
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
    ic_lo = pk["kpv_intracellular_ic50"]["lower_nM"]
    ic_hi = pk["kpv_intracellular_ic50"]["upper_nM"]

    for _ in range(N_MC):
        D = log_uniform(D_lo, D_hi)
        r_pore = (log_uniform(d_lo, d_hi) * 1e-9) / 2.0
        L_pore = log_uniform(L_lo, L_hi) * 1e-9
        N_pores = log_uniform(N_lo, N_hi)
        tau_life = log_uniform(t_lo, t_hi)
        V_m3 = log_uniform(V_lo, V_hi) * 1e-18
        ic50_uM = log_uniform(ic_lo, ic_hi) * NM_TO_UM

        p_pore = pore_permeability_m3_s(D, r_pore, L_pore, 1.0)
        tau_eq, frac = equilibration(V_m3, N_pores, p_pore, tau_life)
        frac_samples.append(frac)
        tau_eq_samples.append(tau_eq)

        for rn in route_names:
            c_lo = routes[rn]["C_ext_synovial_uM"]["lower"]
            c_hi = routes[rn]["C_ext_synovial_uM"]["upper"]
            C_ext = log_uniform(c_lo, c_hi)
            C_in_pyro = C_ext * frac
            ratio_samples[rn].append(C_in_pyro / ic50_uM)

    mc = {
        "n_samples": N_MC,
        "equilibration_fraction": stats(frac_samples),
        "equilibration_tau_eq_s": stats(tau_eq_samples),
        "ratio_over_ic50": {},
        "prob_clear_ic50": {},
    }
    for rn in route_names:
        mc["ratio_over_ic50"][rn] = stats(ratio_samples[rn])
        mc["prob_clear_ic50"][rn] = sum(1 for x in ratio_samples[rn] if x >= 1.0) / len(ratio_samples[rn])
    return mc


# ===================== robustness sweep (M3) =====================

def robustness_sweep(kpv, pore, mac, pk, routes):
    D = kpv["aqueous_diffusion_coefficient_m2_per_s"]["central"]
    r_pore = (pore["inner_diameter_nm"]["central"] * 1e-9) / 2.0
    L_pore = pore["channel_length_nm"]["central"] * 1e-9
    V_m3 = mac["cell_volume_um3"]["central"] * 1e-18
    ic50_uM = pk["kpv_intracellular_ic50"]["central_nM"] * NM_TO_UM
    p_pore = pore_permeability_m3_s(D, r_pore, L_pore, 1.0)

    lifetimes = [60, 300, 900, 1800]     # 1, 5, 15, 30 min
    pore_counts = [1, 10, 100, 1000, 10000]
    C_ia = routes["intra_articular"]["C_ext_synovial_uM"]["central"]
    C_sc = routes["subcutaneous"]["C_ext_synovial_uM"]["central"]

    grid = []
    for N in pore_counts:
        for tl in lifetimes:
            tau_eq, frac = equilibration(V_m3, N, p_pore, tl)
            grid.append({
                "pores_per_cell": N,
                "lifetime_s": tl,
                "tau_eq_s": tau_eq,
                "equilibration_fraction": frac,
                "IA_C_in_uM": C_ia * frac,
                "IA_ratio_over_ic50": (C_ia * frac) / ic50_uM,
                "IA_clears_ic50": (C_ia * frac) / ic50_uM >= 1.0,
                "SC_C_in_uM": C_sc * frac,
                "SC_ratio_over_ic50": (C_sc * frac) / ic50_uM,
                "SC_clears_ic50": (C_sc * frac) / ic50_uM >= 1.0,
            })
    return {
        "note": "Central pore/cell/IC50; sweep lifetime x pores-per-cell. Shows the A1 flux verdict is robust: for pores_per_cell >= 10 the cell equilibrates within a lifetime and IA/SC clear IC50; only the physically implausible single-pore case is flux-limited at short lifetimes.",
        "pore_permeability_m3_per_s": p_pore,
        "grid": grid,
    }


# ===================== selectivity grid (A2) =====================

def selectivity_grid(kpv, pore, mac, pk, routes, frac_central):
    Km = pk["pept1_kpv_kinetics"]["Km_used_uM"]["central"]
    scenarios = pk["pept1_expression_scenarios"]
    route_names = ["intra_articular", "subcutaneous", "oral"]
    grid = {}
    for rn in route_names:
        C_ext = routes[rn]["C_ext_synovial_uM"]["central"]
        C_in_pyro = C_ext * frac_central
        row = {"C_ext_uM": C_ext, "C_in_pyroptotic_uM": C_in_pyro, "by_scenario": {}}
        for sname in ["absent", "low", "moderate", "high"]:
            AR = scenarios[sname]["AR_lin"]
            C_in_healthy = healthy_pept1_conc_uM(C_ext, AR, Km)
            S = float("inf") if C_in_healthy <= 0 else C_in_pyro / C_in_healthy
            row["by_scenario"][sname] = {
                "AR_lin": AR,
                "C_in_healthy_uM": C_in_healthy,
                "selectivity_ratio": S,
                "meaningful_selectivity_ge_3x": (S >= 3.0),
            }
        grid[rn] = row
    return {
        "note": "Selectivity S = C_in,pyroptotic / C_in,healthy across the four PepT1 expression scenarios. S collapses to 1/AR_lin in the linear (SC/oral) regime and rises with C_ext/Km in the saturating (IA) regime. In EVERY route the value is set by the unknown synovial-macrophage PepT1 expression (AR_lin) -- that is the headline empirical limitation.",
        "caveat_S_is_optimistic": "The healthy-cell curve C_in,healthy = C_in_max*C_ext/(Km+C_ext) is a HEURISTIC saturating ceiling, not a transporter steady state -- it describes RATE saturation, not the equilibrium intracellular concentration. A genuinely equilibrating transporter gives C_in,healthy -> C_ext (S -> 1); an electrogenic H+-coupled/concentrative PepT1 plus the intact-cell membrane potential (Vm ~ -50 to -70 mV; Nernst factor ~7-14x for a +1 cation) gives C_in,healthy > C_ext (S < 1, anti-selective). So the TRUE selectivity is <= the values tabulated here, especially at IA. This only strengthens the skeptical read. (In the PYROPTOTIC cell Vm collapses through the pore, which is exactly why C_in,pyroptotic is capped at C_ext with no Nernst boost.)",
        "caveat_PD_timing": "This is a TRANSPORT model. It does not capture that KPV is an UPSTREAM inhibitor (NLRP3 assembly / NF-kB priming) while GSDMD pores open DOWNSTREAM of inflammasome firing -- so even perfectly selective pore-delivery arrives after KPV's target has largely acted and IL-1beta has been released. Pharmacodynamically the pore selects for cells where an upstream inhibitor is too late; see interpretive page.",
        "Km_uM": Km,
        "grid": grid,
    }


# ===================== verdict logic =====================

def verdicts(central, mc, selg):
    """Per-route: A1 (flux/IC50) and A2 (selectivity) -> combined route verdict."""
    route_names = ["intra_articular", "subcutaneous", "oral"]
    v = {}
    for rn in route_names:
        r = central["routes"][rn]
        ratio = r["ratio_over_ic50"]
        p_clear = mc["prob_clear_ic50"][rn]
        # A1 flux sufficiency
        if ratio >= 10 and p_clear >= 0.9:
            a1 = "GREEN"
        elif ratio >= 1.0 and p_clear >= 0.5:
            a1 = "YELLOW"
        else:
            a1 = "RED"
        # A2 selectivity: meaningful (>=3x) only if it holds across MOST plausible
        # PepT1 scenarios. It does not (fails for moderate/high) -> unquantifiable.
        sc = selg["grid"][rn]["by_scenario"]
        n_meaningful = sum(1 for s in ["absent", "low", "moderate", "high"]
                           if sc[s]["meaningful_selectivity_ge_3x"])
        # Meaningful selectivity survives ONLY in the PepT1 absent/low scenarios.
        # Functional PepT1 in immune cells is demonstrated (Dalmasso 2008, Jurkat),
        # so the 'absent' scenario is the least likely -> selectivity is genuinely
        # unquantifiable, not confidently present.
        if n_meaningful >= 3:
            a2 = "GREEN"
        elif n_meaningful == 2:
            a2 = "YELLOW-unquantifiable"
        else:
            a2 = "RED-unquantifiable"
        # combined: route passes filter only if A1 GREEN and A2 GREEN
        if a1 == "GREEN" and a2 == "GREEN":
            combined = "PASS"
        elif a1 in ("GREEN", "YELLOW") and a2.startswith("YELLOW"):
            combined = "MARGINAL-selectivity-unproven"
        else:
            combined = "FAIL"
        v[rn] = {
            "A1_flux_sufficiency": a1,
            "A1_ratio_over_ic50_central": ratio,
            "A1_prob_clear_ic50": p_clear,
            "A2_selectivity": a2,
            "A2_scenarios_with_meaningful_selectivity": n_meaningful,
            "combined_route_verdict": combined,
        }
    return v


def overall_verdict(v):
    # A1 across routes
    any_green_a1 = any(v[r]["A1_flux_sufficiency"] == "GREEN" for r in v)
    any_pass = any(v[r]["combined_route_verdict"] == "PASS" for r in v)
    text = (
        "YELLOW (provisional). The physics of KPV self-delivery is sound "
        "(A1 flux-sufficiency GREEN for intra-articular, marginal for subcutaneous): "
        "a 20 nm pore equilibrates intracellular [KPV] to the extracellular synovial "
        "concentration within seconds, so any route reaching >= the ~10 nM IC50 in "
        "synovial fluid clears the intracellular therapeutic bar. BUT the Trojan-horse "
        "SELECTIVITY thesis (A2) -- the actual reason to prefer pore delivery -- is "
        "UNQUANTIFIABLE for KPV: because KPV already enters cells via PepT1, the pore's "
        "selectivity over the PepT1 baseline is gated entirely by synovial-macrophage "
        "PepT1 expression, which is uncharacterized. No route clears BOTH the therapeutic "
        "AND a meaningful-selectivity threshold with confidence. "
        "Provisional because it rests on 3 compounding named assumptions: (i) pores/cell "
        ">= ~10, (ii) design-space SC/oral synovial PK, (iii) the PepT1 AR_lin scenario band."
    )
    return {
        "overall": "YELLOW-provisional",
        "any_route_A1_GREEN": any_green_a1,
        "any_route_PASSES_both_filters": any_pass,
        "statement": text,
    }


def main():
    kpv, pore, mac, pk, routes = load_inputs()

    central = central_values(kpv, pore, mac, pk, routes)
    mc = monte_carlo(kpv, pore, mac, pk, routes)
    selg = selectivity_grid(kpv, pore, mac, pk, routes,
                            central["equilibration_peak_fraction_central"])
    robust = robustness_sweep(kpv, pore, mac, pk, routes)
    v = verdicts(central, mc, selg)
    overall = overall_verdict(v)

    # Non-finite floats (inf = infinite selectivity when healthy-cell KPV conc is 0)
    # are not valid JSON. Replace with null so all committed outputs parse under a
    # strict JSON parser (the human-readable summary.md still shows "inf" via fmt()).
    def _json_safe(o):
        if isinstance(o, float):
            return o if (o == o and o != float("inf") and o != float("-inf")) else None
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
    for rn in ["intra_articular", "subcutaneous", "oral"]:
        print(f"  {rn}: A1={v[rn]['A1_flux_sufficiency']} "
              f"(ratio/IC50 central={v[rn]['A1_ratio_over_ic50_central']:.3g}, "
              f"P(clear)={v[rn]['A1_prob_clear_ic50']:.2f}), "
              f"A2={v[rn]['A2_selectivity']} -> {v[rn]['combined_route_verdict']}")
    print(f"  equilibration tau_eq central = {central['equilibration_time_constant_s']:.2f} s")


def fmt(x, sig=3):
    if x == float("inf"):
        return "inf"
    if x == 0:
        return "0"
    return f"{x:.{sig}g}"


def write_summary(central, mc, selg, robust, v, overall):
    L = []
    L.append("# comp-042 -- KPV self-delivery through GSDMD pyroptotic pores vs. the PepT1 baseline\n")
    L.append("**Auto-generated by `analyze.py` (stdlib-only, deterministic, seed 42).**\n")
    L.append(f"## Overall verdict: {overall['overall']}\n")
    L.append(overall["statement"] + "\n")

    L.append("## Core physics\n")
    L.append(f"- Per-pore permeability (with access resistance): {fmt(central['pore_permeability_m3_per_s'])} m^3/s")
    L.append(f"- Equilibration time constant tau_eq (central: 200 pores, 3000 um3): "
             f"**{fmt(central['equilibration_time_constant_s'])} s** "
             f"-> intracellular [KPV] reaches {fmt(100*central['equilibration_peak_fraction_central'],4)}% "
             f"of extracellular within a {int(300)} s lifetime.")
    L.append(f"- Monte Carlo equilibration fraction: median "
             f"{fmt(mc['equilibration_fraction']['median'])}, p5 {fmt(mc['equilibration_fraction']['p5'])}\n")
    L.append("Interpretation: the pore is so wide and numerous that the macrophage interior "
             "equilibrates to the extracellular concentration in seconds. Peak intracellular "
             "[KPV] is therefore CAPPED at the synovial [KPV] -- the naive 'moles-in/volume' "
             "estimate overshoots C_ext by orders of magnitude (see central_results.json "
             "`naive_over_C_ext`), which just confirms saturation. This quantitatively answers "
             "gsdmd-pore-delivery-paradox.md Open Question #4 (pore lifetime): even the SHORT "
             "end of the lifetime range is far longer than needed.\n")

    L.append("## Metric 1 -- peak intracellular [KPV] / IC50 (flux sufficiency, A1)\n")
    L.append("| Route | synovial [KPV] (uM) | intracellular [KPV] (uM) | / IC50 (10 nM) | P(clear IC50) | A1 |")
    L.append("|---|---|---|---|---|---|")
    for rn in ["intra_articular", "subcutaneous", "oral"]:
        r = central["routes"][rn]
        L.append(f"| {rn.replace('_',' ')} | {fmt(r['C_ext_synovial_uM'])} | "
                 f"{fmt(r['C_in_pyroptotic_uM'])} | {fmt(r['ratio_over_ic50'])}x | "
                 f"{fmt(mc['prob_clear_ic50'][rn])} | {v[rn]['A1_flux_sufficiency']} |")
    L.append("")

    L.append("## Metric 2 -- selectivity ratio over PepT1 baseline (A2)\n")
    L.append("Selectivity S = intracellular[pyroptotic] / intracellular[healthy]. Healthy-cell "
             "uptake is via PepT1 (present in immune cells; Dalmasso 2008). AR_lin = the unknown "
             "synovial-macrophage PepT1 linear accumulation ratio.\n")
    L.append("| Route | PepT1 absent | low (AR 0.3) | moderate (AR 1) | high (AR 3) |")
    L.append("|---|---|---|---|---|")
    for rn in ["intra_articular", "subcutaneous", "oral"]:
        sc = selg["grid"][rn]["by_scenario"]
        L.append(f"| {rn.replace('_',' ')} | "
                 f"{fmt(sc['absent']['selectivity_ratio'])} | "
                 f"{fmt(sc['low']['selectivity_ratio'])} | "
                 f"{fmt(sc['moderate']['selectivity_ratio'])} | "
                 f"{fmt(sc['high']['selectivity_ratio'])} |")
    L.append("")
    L.append("The pore confers meaningful selectivity ONLY in the 'PepT1 absent/low' scenarios. "
             "If synovial macrophages express functional PepT1 (moderate/high), selectivity "
             "collapses to ~1 or below (healthy cells already admit -- or even concentrate -- KPV). "
             "**Which scenario is real is unknown -> A2 is YELLOW-unquantifiable for every route** "
             "(YELLOW, not RED: the absent/low-PepT1 scenarios numerically clear, so this is "
             "unquantifiable-marginal, not a hard fail; matches the computed per-route verdicts).\n")
    L.append("**Pharmacodynamic-timing caveat (added 2026-07-14):** even where transport is "
             "sufficient, KPV is an *upstream* inflammasome inhibitor, whereas GSDMD pores form "
             "*downstream* of inflammasome firing. So a payload arriving through the pore arrives "
             "after its target step has already fired -- transport sufficiency does NOT imply "
             "therapeutic-timing sufficiency for KPV specifically. This is the second independent "
             "reason KPV is the wrong proof-of-concept payload for pore self-delivery (the first "
             "being PepT1 confounding). A downstream-acting, transporter-orphan payload is the clean probe.\n")

    L.append("## Metric 3 -- robustness sweep (pore lifetime x pores/cell)\n")
    L.append("| pores/cell | lifetime (s) | tau_eq (s) | equilib. frac | IA clears IC50 | SC clears IC50 |")
    L.append("|---|---|---|---|---|---|")
    for g in robust["grid"]:
        L.append(f"| {g['pores_per_cell']} | {g['lifetime_s']} | {fmt(g['tau_eq_s'])} | "
                 f"{fmt(g['equilibration_fraction'])} | {g['IA_clears_ic50']} | {g['SC_clears_ic50']} |")
    L.append("")
    L.append("The A1 verdict is robust: for pores/cell >= 10 the cell equilibrates within any "
             "lifetime in range and IA clears IC50 by ~4 orders of magnitude; SC clears it by ~3x. "
             "Only the physically implausible single-pore case is flux-limited at short lifetimes.\n")

    L.append("## Per-route combined verdict (decision filter: PASS needs A1 GREEN AND A2 GREEN)\n")
    L.append("| Route | A1 | A2 | Combined |")
    L.append("|---|---|---|---|")
    for rn in ["intra_articular", "subcutaneous", "oral"]:
        L.append(f"| {rn.replace('_',' ')} | {v[rn]['A1_flux_sufficiency']} | "
                 f"{v[rn]['A2_selectivity']} | {v[rn]['combined_route_verdict']} |")
    L.append("")
    L.append("**No route PASSES both filters.** Intra-articular delivers KPV superbly (A1) but "
             "at doses that flood ALL synovial cells and saturate PepT1 in healthy cells too, so "
             "there is no pore-specific selectivity. Subcutaneous is marginal on flux and "
             "unquantifiable on selectivity. Oral fails on absolute synovial concentration.\n")

    L.append("## The single biggest limitation\n")
    L.append("Synovial-macrophage PepT1 (SLC15A1) functional expression is uncharacterized. It is "
             "the sole determinant of whether the pore beats the constitutive KPV import route, and "
             "it is not in the literature. Everything in the A2 column is gated on it. KPV is, in "
             "effect, the WRONG payload to DEMONSTRATE pore-selectivity, precisely because it "
             "already has an independent transporter route -- a truly transporter-orphan "
             "membrane-impermeant payload would be the clean selectivity test.\n")

    (OUTPUTS / "summary.md").write_text("\n".join(L))


if __name__ == "__main__":
    main()
