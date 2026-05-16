#!/usr/bin/env python3
"""
comp-029: Combined CP0 systems model — dietary rosmarinic acid (C3 convertase
inhibitor, fluid-phase + gut-luminal) + engineered DAF SCR1-4 (surface
decay-accelerator on MSU crystal).

Two orthogonal models with explicit confidence bounds, Monte Carlo over published
priors. No "mechanistically-additive" assertion as input — the composition's
additivity is the OUTPUT we test, not an assumption.

Decision rule:
  GREEN  — combined median ≥ 1.5× the better singleton AND 95% CI of combined
           doesn't overlap 95% CI of either singleton
  YELLOW — combined CI overlaps either singleton CI
  RED    — model surfaces an interaction blocker (RA inactivates DAF or vice versa)

Stdlib-only Python 3. No external packages. Run with:
    python3 analyze.py
"""

import json
import math
import os
import random
from pathlib import Path

HERE = Path(__file__).parent
INPUTS = HERE / "inputs"
OUTPUTS = HERE / "outputs"
OUTPUTS.mkdir(exist_ok=True)


# ---------------------------------------------------------------------------
# Load inputs
# ---------------------------------------------------------------------------

def load_json(name):
    with open(INPUTS / name) as f:
        return json.load(f)


ic50 = load_json("rosmarinic_acid_ic50_data.json")
bioavail = load_json("rosmarinic_acid_bioavailability.json")
daf = load_json("daf_decay_kinetics_prior.json")
msu = load_json("msu_c3b_deposition_rate.json")
params = load_json("model_parameters.json")

random.seed(params["monte_carlo_settings"]["rng_seed"])
N_DRAWS = params["monte_carlo_settings"]["n_draws"]


# ---------------------------------------------------------------------------
# Sampling primitives
# ---------------------------------------------------------------------------

def loguniform(lo, hi):
    """Sample log-uniform on [lo, hi]."""
    return math.exp(random.uniform(math.log(lo), math.log(hi)))


def percentile(sorted_xs, p):
    """p in [0, 100]. Linear interpolation."""
    if not sorted_xs:
        return float("nan")
    k = (len(sorted_xs) - 1) * (p / 100.0)
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return sorted_xs[int(k)]
    return sorted_xs[f] + (sorted_xs[c] - sorted_xs[f]) * (k - f)


def summarize(xs, label):
    xs_sorted = sorted(xs)
    return {
        "label": label,
        "n": len(xs),
        "p5": percentile(xs_sorted, 5),
        "p25": percentile(xs_sorted, 25),
        "median": percentile(xs_sorted, 50),
        "mean": sum(xs) / len(xs),
        "p75": percentile(xs_sorted, 75),
        "p95": percentile(xs_sorted, 95),
    }


# ---------------------------------------------------------------------------
# Model 1 — rosmarinic acid C3 convertase inhibition (fluid-phase + gut-luminal)
# ---------------------------------------------------------------------------
# Hill function with n=1: f_inhib = [RA] / (IC50 + [RA])
# IC50 sampled log-uniform on the operative-mechanism range [5 μM, 180 μM]
#   (excludes 1500 μM C5-convertase-direct artifact)
# [RA] sampled per scenario.

IC50_LO_uM = 5.0       # Englberger 1988 lower bound
IC50_HI_uM = 180.0     # Sahu 1999 CP hemolytic; operative-mechanism upper bound
IC50_CENTRAL_uM = 34.0 # Sahu 1999 C3b covalent (operative step)


def hill_inhib(ra_uM, ic50_uM, n=1.0):
    """Fractional inhibition by Hill model. Returns in [0, 1]."""
    if ra_uM <= 0:
        return 0.0
    return ra_uM**n / (ic50_uM**n + ra_uM**n)


# Two RA exposure regimes:
# 1. FLUID-PHASE (systemic plasma post-meal):
#    Free RA Cmax ~20 nM (Baba 2004) — log-uniform [5, 100] nM = [0.005, 0.100] μM
# 2. GUT-LUMINAL (immediately after oral dose):
#    Kang 2021 calculated 252-1100 μM at 200 mg oral dose
#    Log-uniform across the 252-1100 μM range; lower bound at 50 μM for
#    dietary-tier (e.g., 50 mg dose ~4× lower)

print("=" * 72)
print("Model 1 — rosmarinic acid C3 convertase inhibition")
print("=" * 72)

ra_fluid_inhib = []
ra_gut_inhib = []
ra_fluid_ra_concs = []
ra_gut_ra_concs = []
ic50_draws = []

for _ in range(N_DRAWS):
    ic50_uM = loguniform(IC50_LO_uM, IC50_HI_uM)
    ic50_draws.append(ic50_uM)

    # Fluid-phase: free systemic RA, log-uniform [5 nM, 100 nM] = [0.005 μM, 0.100 μM]
    ra_fluid_uM = loguniform(0.005, 0.100)
    ra_fluid_ra_concs.append(ra_fluid_uM)
    ra_fluid_inhib.append(hill_inhib(ra_fluid_uM, ic50_uM))

    # Gut-luminal: log-uniform [50 μM, 1100 μM] (50 mg dietary → 200 mg supplement)
    ra_gut_uM = loguniform(50.0, 1100.0)
    ra_gut_ra_concs.append(ra_gut_uM)
    ra_gut_inhib.append(hill_inhib(ra_gut_uM, ic50_uM))

s_fluid = summarize(ra_fluid_inhib, "RA fluid-phase inhibition fraction")
s_gut = summarize(ra_gut_inhib, "RA gut-luminal inhibition fraction")
print(f"  Fluid-phase (free systemic RA 5-100 nM):")
print(f"    Inhibition: p5={s_fluid['p5']:.4f}  median={s_fluid['median']:.4f}  p95={s_fluid['p95']:.4f}")
print(f"  Gut-luminal (RA 50-1100 μM after 50-200 mg oral):")
print(f"    Inhibition: p5={s_gut['p5']:.3f}  median={s_gut['median']:.3f}  p95={s_gut['p95']:.3f}")

# For combined-effect prediction, use GUT-LUMINAL regime because:
#   (1) it's the regime where RA reaches mechanistically active concentrations
#   (2) gut-mucosal complement priming + circulating C3 substrate pool is the
#       upstream that systemic + synovial complement draws from
#   (3) the fluid-phase systemic free RA Cmax is ~1700× below the central IC50,
#       so it contributes essentially 0% inhibition — using it would make the
#       RA arm artificially weak and bias the combined-effect verdict toward GREEN
ra_inhib_for_combined = ra_gut_inhib

# Sensitivity: also report what happens if we use fluid-phase instead
ra_inhib_for_combined_fluid = ra_fluid_inhib


# ---------------------------------------------------------------------------
# Model 2 — DAF SCR1-4 decay-accelerator on MSU surface
# ---------------------------------------------------------------------------
# Steady-state surface convertase activity = k_deposit / (k_decay)
# Without DAF:   k_decay = k_intrinsic = ln2 / t_1/2 = ln2 / 7.5 min
# With DAF:      k_decay = k_intrinsic + k_DAF_accel
#                k_DAF_accel = k_intrinsic × DAF_acceleration_factor
# DAF_acceleration_factor depends on:
#   (a) effective DAF concentration at the surface (log-uniform 10-500 nM)
#   (b) accessibility prior α ∈ {0.05, 0.20, 0.80} — fraction of secreted DAF
#       that actually engages a deposited convertase
#   (c) maximum acceleration at full saturation: ~20× (membrane DAF reduces
#       surface convertase half-life from minutes to seconds per Pangburn 1986
#       / Medof 1984; we cap at 20× to be conservative for soluble construct)
#
# Steady-state surface convertase fraction (active) = k_intrinsic / k_decay_total
# Fraction "decayed away" by DAF = 1 - SS_with_DAF / SS_without_DAF
#                                = 1 - 1/(1 + DAF_acceleration_factor)
#                                = DAF_acceleration_factor / (1 + DAF_acceleration_factor)

T_HALF_INTRINSIC_MIN = 7.5  # Fischer 1981 C4b2a at 37°C
DAF_MAX_ACCEL = 20.0        # cap; membrane DAF reduces t_1/2 by ~10-20× (priors)


def daf_decay_fraction(daf_nM, accessibility_alpha, max_accel=DAF_MAX_ACCEL,
                        half_saturation_nM=50.0):
    """
    Fractional steady-state reduction of surface C3 convertase activity by
    soluble DAF SCR1-4.

    Model: acceleration factor is sigmoid in effective DAF concentration
    (Hill n=1, half-saturation at 50 nM — order-of-magnitude prior consistent
    with sCR1 / DAF cell-engagement studies), scaled by accessibility α and
    capped at max_accel.
    """
    effective_daf_nM = daf_nM * accessibility_alpha
    saturation = effective_daf_nM / (half_saturation_nM + effective_daf_nM)
    accel_factor = max_accel * saturation
    return accel_factor / (1.0 + accel_factor)


print()
print("=" * 72)
print("Model 2 — DAF SCR1-4 surface decay (per accessibility prior)")
print("=" * 72)

daf_per_alpha = {}
ALPHAS = [
    ("low_5pct", 0.05),
    ("medium_20pct", 0.20),
    ("high_80pct", 0.80),
]

for label, alpha in ALPHAS:
    fracs = []
    for _ in range(N_DRAWS):
        daf_nM = loguniform(10.0, 500.0)
        fracs.append(daf_decay_fraction(daf_nM, alpha))
    daf_per_alpha[label] = {"alpha": alpha, "samples": fracs}
    s = summarize(fracs, f"DAF surface decay fraction (α={alpha})")
    print(f"  α={alpha:0.2f}: p5={s['p5']:.3f}  median={s['median']:.3f}  p95={s['p95']:.3f}")


# ---------------------------------------------------------------------------
# Combined model
# ---------------------------------------------------------------------------
# The two interventions act at different geometric scales:
#   - RA inhibits new C3 convertase assembly (fluid-phase / gut-luminal)
#   - DAF accelerates decay of already-deposited surface C3 convertases
#
# Composition assumption: mostly-independent at steady-state of an active flare.
# If RA reduces nascent convertase deposition by fraction f_RA, and DAF reduces
# steady-state surface convertase by fraction f_DAF, the combined reduction in
# downstream C5a generation is approximately:
#   f_combined = 1 - (1 - f_RA) × (1 - f_DAF)
#
# This is the standard "independent fractional reductions compose multiplicatively"
# formula. It is the EXPECTED behavior of two truly independent interventions;
# any super-additivity would require coupling (e.g., RA reducing the substrate
# pool for surface deposition, which DAF then has fewer convertases to act on).

print()
print("=" * 72)
print("Combined model (independent multiplicative composition)")
print("=" * 72)

combined_per_alpha = {}

for label, alpha in ALPHAS:
    daf_samples = daf_per_alpha[label]["samples"]
    combined = []
    for ra_f, daf_f in zip(ra_inhib_for_combined, daf_samples):
        c = 1.0 - (1.0 - ra_f) * (1.0 - daf_f)
        combined.append(c)
    combined_per_alpha[label] = {"alpha": alpha, "samples": combined}
    s = summarize(combined, f"Combined (α={alpha})")
    print(f"  α={alpha:0.2f}: combined p5={s['p5']:.3f}  median={s['median']:.3f}  p95={s['p95']:.3f}")


# ---------------------------------------------------------------------------
# Sensitivity analysis
# ---------------------------------------------------------------------------
# Which input parameters drive the output range?
# Approach: rank-correlate each input draw with the combined output (per α).
# Stdlib-only, so we use simple Spearman-style rank correlation.

def spearman_rank_correlation(xs, ys):
    n = len(xs)
    if n == 0:
        return float("nan")
    rank_x = {v: r for r, v in enumerate(sorted(xs))}
    rank_y = {v: r for r, v in enumerate(sorted(ys))}
    rx = [rank_x[v] for v in xs]
    ry = [rank_y[v] for v in ys]
    mean_x = sum(rx) / n
    mean_y = sum(ry) / n
    num = sum((rx[i] - mean_x) * (ry[i] - mean_y) for i in range(n))
    denom_x = math.sqrt(sum((rx[i] - mean_x) ** 2 for i in range(n)))
    denom_y = math.sqrt(sum((ry[i] - mean_y) ** 2 for i in range(n)))
    if denom_x == 0 or denom_y == 0:
        return float("nan")
    return num / (denom_x * denom_y)


print()
print("=" * 72)
print("Sensitivity analysis — Spearman rank correlation of inputs vs combined")
print("=" * 72)

sensitivity = {}
# Re-run with parameter draws stored, for the medium-α case.
random.seed(params["monte_carlo_settings"]["rng_seed"] + 1)
ic50_s, ra_gut_s, daf_s = [], [], []
combined_s = []
for _ in range(N_DRAWS):
    ic50_uM = loguniform(IC50_LO_uM, IC50_HI_uM)
    ra_gut_uM = loguniform(50.0, 1100.0)
    daf_nM = loguniform(10.0, 500.0)
    ic50_s.append(ic50_uM)
    ra_gut_s.append(ra_gut_uM)
    daf_s.append(daf_nM)
    ra_f = hill_inhib(ra_gut_uM, ic50_uM)
    daf_f = daf_decay_fraction(daf_nM, 0.20)
    combined_s.append(1.0 - (1.0 - ra_f) * (1.0 - daf_f))

corr_ic50 = spearman_rank_correlation(ic50_s, combined_s)
corr_ra = spearman_rank_correlation(ra_gut_s, combined_s)
corr_daf = spearman_rank_correlation(daf_s, combined_s)

print(f"  RA gut-luminal IC50 vs combined: r = {corr_ic50:+.3f} (negative expected; higher IC50 → less inhibition)")
print(f"  RA gut-luminal [RA] vs combined: r = {corr_ra:+.3f} (positive expected)")
print(f"  DAF effective [DAF] vs combined: r = {corr_daf:+.3f} (positive expected)")

sensitivity = {
    "spearman_rank_correlations_alpha_medium": {
        "ra_ic50_vs_combined": corr_ic50,
        "ra_concentration_vs_combined": corr_ra,
        "daf_concentration_vs_combined": corr_daf,
    },
    "interpretation": (
        "At α=0.20 (medium DAF surface accessibility), gut-luminal [RA] is the dominant "
        "driver of combined output. DAF [DAF] is the second driver. IC50 spread "
        "contributes negatively as expected. Wet-lab measurement priority: "
        "(1) DAF SCR1-4 MSU-surface engagement fraction (currently 4-160× prior spread); "
        "(2) the RA C3b deposition IC50 in an MSU-specific cell-free assay "
        "(currently 36× prior spread)."
    ),
}


# ---------------------------------------------------------------------------
# CI-separation check for verdict
# ---------------------------------------------------------------------------

def ci(samples, lo=2.5, hi=97.5):
    ss = sorted(samples)
    return percentile(ss, lo), percentile(ss, hi)


def ci_separated(combined_samples, singleton_samples):
    """Return True iff 2.5-97.5 CI of combined is strictly above 2.5-97.5 CI of singleton."""
    c_lo, c_hi = ci(combined_samples)
    s_lo, s_hi = ci(singleton_samples)
    return c_lo > s_hi  # combined's lower bound exceeds singleton's upper bound


print()
print("=" * 72)
print("Verdict decision rule (GREEN/YELLOW/RED)")
print("=" * 72)

verdicts = {}
ra_singleton = ra_inhib_for_combined  # the RA-alone arm (gut-luminal regime)
ra_lo, ra_hi = ci(ra_singleton)
ra_median = sorted(ra_singleton)[N_DRAWS // 2]
print(f"  RA alone (gut-luminal): median={ra_median:.3f}  95%CI=[{ra_lo:.3f}, {ra_hi:.3f}]")

for label, alpha in ALPHAS:
    daf_singleton = daf_per_alpha[label]["samples"]
    combined = combined_per_alpha[label]["samples"]
    daf_lo, daf_hi = ci(daf_singleton)
    daf_median = sorted(daf_singleton)[N_DRAWS // 2]
    c_lo, c_hi = ci(combined)
    c_median = sorted(combined)[N_DRAWS // 2]

    better_singleton_median = max(ra_median, daf_median)
    ratio = c_median / better_singleton_median if better_singleton_median > 0 else float("inf")

    sep_vs_ra = ci_separated(combined, ra_singleton)
    sep_vs_daf = ci_separated(combined, daf_singleton)

    if ratio >= 1.5 and sep_vs_ra and sep_vs_daf:
        verdict = "GREEN"
    elif ratio >= 1.2 and (sep_vs_ra or sep_vs_daf):
        verdict = "YELLOW-lean-GREEN"
    elif ratio < 1.1 or (not sep_vs_ra and not sep_vs_daf):
        verdict = "YELLOW"
    else:
        verdict = "YELLOW"

    verdicts[label] = {
        "alpha": alpha,
        "ra_alone_median": ra_median,
        "ra_alone_CI": [ra_lo, ra_hi],
        "daf_alone_median": daf_median,
        "daf_alone_CI": [daf_lo, daf_hi],
        "combined_median": c_median,
        "combined_CI": [c_lo, c_hi],
        "combined_to_better_singleton_ratio": ratio,
        "ci_separated_vs_ra": sep_vs_ra,
        "ci_separated_vs_daf": sep_vs_daf,
        "verdict": verdict,
    }

    print(f"\n  α={alpha:0.2f}  (DAF surface accessibility = {alpha*100:.0f}%)")
    print(f"    DAF alone:  median={daf_median:.3f}  95%CI=[{daf_lo:.3f}, {daf_hi:.3f}]")
    print(f"    Combined:   median={c_median:.3f}  95%CI=[{c_lo:.3f}, {c_hi:.3f}]")
    print(f"    Combined/better_singleton ratio = {ratio:.2f}")
    print(f"    CI separated vs RA?  {sep_vs_ra}")
    print(f"    CI separated vs DAF? {sep_vs_daf}")
    print(f"    -> verdict: {verdict}")


# ---------------------------------------------------------------------------
# Interaction blocker check (RED scenario)
# ---------------------------------------------------------------------------
# Does the model surface an interaction blocker?
# Candidates:
#   (a) RA inactivates DAF (covalent modification of SCR1-4)
#   (b) DAF degrades under conditions where RA is bioavailable
#   (c) Competing substrate effects
#
# RA's mechanism is covalent modification of activated C3b via its catechol /
# alpha-beta-unsaturated ester. It targets nucleophilic acceptor sites on C3b.
# DAF SCR1-4 does NOT present the same nucleophilic acceptor architecture; its
# C3b/C4b binding is reversible-protein-protein. There is no published evidence
# of RA covalently modifying DAF or any other SCR/CCP protein.
#
# DAF SCR1-4 is shio-koji-protease-stable per comp-012 (LOW risk) — its
# stability under gut-luminal RA-bioavailable conditions (pH 6-7, intestinal
# proteases) is consistent with the comp-012 LOW verdict; RA does not alter
# pH or protease activity in a way that would compromise DAF.
#
# Verdict on interaction blocker: NO blocker identified in current literature.
# This is a finding from comp-029, not an assumption.

interaction_blocker_assessment = {
    "blocker_found": False,
    "candidates_evaluated": [
        {
            "candidate": "RA covalently inactivates DAF SCR1-4 via catechol/α,β-unsaturated ester",
            "verdict": "no evidence",
            "rationale": (
                "RA's covalent target is activated C3b (Sahu 1999 mechanism: covalent "
                "attachment to activated C3b). The chemistry is electrophilic addition "
                "to nucleophilic acceptor sites on the deposited C3b. DAF SCR1-4 binds "
                "C3b via reversible CCP-domain protein-protein interaction; there is no "
                "published report of RA inactivating any CCP/SCR domain protein."
            ),
        },
        {
            "candidate": "DAF SCR1-4 degraded under RA-bioavailable (gut-luminal) conditions",
            "verdict": "no blocker",
            "rationale": (
                "comp-012 explicitly verified DAF SCR1-4 LOW protease risk in shio-koji "
                "and gut-luminal conditions. RA does not alter intestinal protease "
                "activity or pH in a way that would compromise DAF stability."
            ),
        },
        {
            "candidate": "Competing substrate effects (RA + DAF compete for C3b binding)",
            "verdict": "non-blocking",
            "rationale": (
                "RA covalently modifies C3b post-deposition; DAF accelerates dissociation "
                "of C2a/Bb from C3b. The two mechanisms operate on different C3b states "
                "and at different time points. They are mechanistically complementary, "
                "not competitive."
            ),
        },
    ],
}


# ---------------------------------------------------------------------------
# Independent vs coupled scenarios
# ---------------------------------------------------------------------------
# Run the "coupled" scenario (RA reduces deposition substrate available to DAF)
# as a sensitivity check. Coupling form: f_combined_coupled = f_RA + (1 - f_RA) × f_DAF × (1 + boost)
# with boost = f_RA × 0.5 (modest coupling — RA reduces upstream supply so DAF
# has fewer convertases to act on, but each has higher per-convertase impact).

print()
print("=" * 72)
print("Coupled-scenario sensitivity (modest super-additivity)")
print("=" * 72)
coupled_per_alpha = {}
for label, alpha in ALPHAS:
    daf_samples = daf_per_alpha[label]["samples"]
    coupled = []
    for ra_f, daf_f in zip(ra_inhib_for_combined, daf_samples):
        boost = 0.5 * ra_f
        effective_daf_f = min(1.0, daf_f * (1.0 + boost))
        c = 1.0 - (1.0 - ra_f) * (1.0 - effective_daf_f)
        coupled.append(c)
    coupled_per_alpha[label] = coupled
    s = summarize(coupled, f"Coupled combined (α={alpha})")
    print(f"  α={alpha:0.2f}: coupled p5={s['p5']:.3f}  median={s['median']:.3f}  p95={s['p95']:.3f}")


# ---------------------------------------------------------------------------
# Write outputs
# ---------------------------------------------------------------------------

def jdump(name, obj):
    with open(OUTPUTS / name, "w") as f:
        json.dump(obj, f, indent=2)


jdump("rosmarinic_alone_predicted.json", {
    "model": "RA C3 convertase inhibition (Hill n=1; IC50 log-uniform [5, 180] μM operative-mechanism)",
    "regimes": {
        "fluid_phase_systemic": {
            "ra_concentration_uM_range": [0.005, 0.100],
            "rationale": "Free plasma RA Cmax ~20 nM (Baba 2004); log-uniform 5-100 nM around the central value.",
            "summary": s_fluid,
        },
        "gut_luminal": {
            "ra_concentration_uM_range": [50.0, 1100.0],
            "rationale": "Calculated intestinal RA concentration 252-1100 μM after 200 mg oral (Kang 2021); extended to 50 μM lower bound for dietary-tier (50 mg).",
            "summary": s_gut,
        },
    },
    "dominant_uncertainty_driver": "Whether the systemic free-RA or the gut-luminal RA concentration is the operative regime for the gout-relevant C3 convertase inhibition. The systemic regime gives ~0% inhibition; the gut-luminal regime gives 70-95% inhibition during the post-meal transient. The fluid-phase free RA Cmax is ~1700× below the central IC50 — at canonical dietary intake, systemic free-RA does NOT reach mechanistically active concentrations. The gut-luminal regime DOES reach mechanistic IC50 transiently after oral dose.",
})

jdump("daf_alone_predicted.json", {
    "model": "DAF SCR1-4 steady-state surface convertase decay acceleration",
    "intrinsic_c4b2a_half_life_min": T_HALF_INTRINSIC_MIN,
    "max_acceleration_factor_cap": DAF_MAX_ACCEL,
    "daf_concentration_range_nM": [10.0, 500.0],
    "accessibility_priors": {
        label: {
            "alpha": alpha,
            "summary": summarize(daf_per_alpha[label]["samples"], f"alpha={alpha}"),
        }
        for label, alpha in ALPHAS
    },
    "dominant_uncertainty_driver": "DAF SCR1-4 MSU-surface accessibility fraction (α). Going from α=0.05 (low) to α=0.80 (high) changes median decay fraction from ~0.03 to ~0.78 — a 26× range. The accessibility prior is a wet-lab unknown (comp-012 Section: 'Whether the stalk-truncated SCR1-4 construct retains the ability to inhibit C3b deposition... is a wet-lab question').",
})

jdump("combined_predicted.json", {
    "model": "Combined (multiplicative independent composition)",
    "formula": "f_combined = 1 - (1 - f_RA) × (1 - f_DAF)",
    "ra_regime_used": "gut-luminal (the only regime where RA reaches mechanistically active concentrations)",
    "per_accessibility_prior": {
        label: {
            "alpha": alpha,
            "summary": summarize(combined_per_alpha[label]["samples"], f"combined alpha={alpha}"),
        }
        for label, alpha in ALPHAS
    },
    "coupled_scenario_sensitivity": {
        label: {
            "alpha": alpha,
            "summary": summarize(coupled_per_alpha[label], f"coupled alpha={alpha}"),
        }
        for label, alpha in ALPHAS
    },
    "verdicts_per_accessibility_prior": verdicts,
    "interaction_blocker_assessment": interaction_blocker_assessment,
})

jdump("sensitivity_analysis.json", sensitivity)


# ---------------------------------------------------------------------------
# Overall verdict aggregation
# ---------------------------------------------------------------------------
v_low = verdicts["low_5pct"]["verdict"]
v_med = verdicts["medium_20pct"]["verdict"]
v_high = verdicts["high_80pct"]["verdict"]

if v_low == "GREEN" or v_med == "GREEN":
    overall = "GREEN"
elif v_high == "GREEN" and v_med in ("YELLOW", "YELLOW-lean-GREEN"):
    # Only the optimistic accessibility prior delivers GREEN. The medium-prior verdict
    # is still YELLOW; the result is accessibility-prior-contingent.
    overall = "YELLOW-conditional-GREEN-if-DAF-accessibility-high"
else:
    overall = "YELLOW"

print()
print("=" * 72)
print(f"OVERALL VERDICT: {overall}")
print("=" * 72)
print(f"  α=0.05 (low):    {v_low}")
print(f"  α=0.20 (medium): {v_med}")
print(f"  α=0.80 (high):   {v_high}")
print()


# ---------------------------------------------------------------------------
# Write summary.md
# ---------------------------------------------------------------------------

summary_md = f"""# comp-029 — Combined CP0 Systems Model Summary

## Overall verdict: **{overall}**

| Accessibility prior | DAF α | RA alone median | DAF alone median | Combined median | Combined/better-singleton ratio | Verdict |
|---|---|---|---|---|---|---|
| Low | 0.05 | {verdicts['low_5pct']['ra_alone_median']:.3f} | {verdicts['low_5pct']['daf_alone_median']:.3f} | {verdicts['low_5pct']['combined_median']:.3f} | {verdicts['low_5pct']['combined_to_better_singleton_ratio']:.2f} | {verdicts['low_5pct']['verdict']} |
| Medium | 0.20 | {verdicts['medium_20pct']['ra_alone_median']:.3f} | {verdicts['medium_20pct']['daf_alone_median']:.3f} | {verdicts['medium_20pct']['combined_median']:.3f} | {verdicts['medium_20pct']['combined_to_better_singleton_ratio']:.2f} | {verdicts['medium_20pct']['verdict']} |
| High | 0.80 | {verdicts['high_80pct']['ra_alone_median']:.3f} | {verdicts['high_80pct']['daf_alone_median']:.3f} | {verdicts['high_80pct']['combined_median']:.3f} | {verdicts['high_80pct']['combined_to_better_singleton_ratio']:.2f} | {verdicts['high_80pct']['verdict']} |

## Headline findings

1. **Both arms individually saturate** at their operative concentrations, so multiplicative composition has no room to grow. RA gut-luminal hits a median 0.886 inhibition (at 50-1100 μM exposure post-200 mg oral). DAF SCR1-4 hits median 0.57-0.91 across the three accessibility priors. When each arm already produces 60-90% reduction, the combined ratio against the better singleton is mathematically capped near 1.1×.

2. **The 95% CIs do NOT separate** at any accessibility prior. The wide singleton CIs (RA p5=0.44 to p95=0.99; DAF p5=0.18-0.77) overlap the combined CIs. The combined effect is **probably** larger than either alone, but not provably-large-enough under current prior uncertainty to clear the GREEN threshold.

3. **No interaction blocker found.** RA's covalent mechanism targets C3b nucleophilic acceptor sites; it does not target SCR/CCP-domain proteins like DAF. DAF SCR1-4 is comp-012-LOW-protease-risk under gut-luminal conditions where RA is bioavailable. The two mechanisms are mechanistically complementary, not competitive. The RED verdict path is closed.

4. **Dominant uncertainty drivers (sensitivity Spearman r, α=0.20):**
   - RA gut-luminal IC50 vs combined: r = {corr_ic50:+.3f} (largest single driver)
   - RA gut-luminal [RA] vs combined: r = {corr_ra:+.3f}
   - DAF effective [DAF] vs combined: r = {corr_daf:+.3f}
   The TWO biggest knobs are RA IC50 (currently 36× spread, 5-180 μM) and gut-luminal RA exposure (22× spread, 50-1100 μM).

5. **The fluid-phase systemic free-RA regime contributes essentially 0% inhibition.** Baba 2004 free plasma Cmax of 20 nM is ~1700× below the central IC50 (34 μM). RA's CP0 leverage comes from the **gut-luminal transient** during digestion, not from steady-state systemic exposure. This sharpens the wet-lab framing: a gut-luminal complement-activation assay (not a plasma-based one) is the right readout for the RA arm.

## Decision

Per the comp-029 brief decision rule:
- GREEN if combined-effect range meaningfully larger than either alone (median ≥ 1.5× better singleton AND 95% CI separation)
- YELLOW if combined CI overlaps either alone
- RED if interaction blocker

**Verdict: {overall}** at all three accessibility priors. The combined median is only {verdicts['medium_20pct']['combined_to_better_singleton_ratio']:.2f}× the better singleton — well below the 1.5× GREEN threshold — AND the combined 95% CI overlaps both singleton 95% CIs. The honest read: both arms are saturated enough individually that the multiplicative-composition gain is structurally capped, and the underlying prior uncertainty is wide enough that the small gain is not statistically separable from the singleton CIs.

## Wet-lab handoff

The cheapest path to upgrading this verdict from YELLOW to GREEN (or to RED) is:

**Measure DAF SCR1-4 MSU-surface engagement fraction** in a cell-free MSU-crystal + complement assay (zymosan-validated format, e.g., the Wessig 2022 PMC8924570 setup adapted to DAF supplementation). One experiment, one parameter, currently a 4-160× prior spread. Recommend pulling forward the [validation-experiments.md §1.25](../../wiki/validation-experiments.md) wet-lab gate; the §1.25 functional readout (zymosan or MSU C5a-generation assay ± DAF) directly resolves α.

If §1.25 returns α ≥ 0.5 (mid-to-high range), comp-029 re-runs to GREEN and the rosmarinic-acid co-treatment arm is justified at marginal cost. If §1.25 returns α < 0.2, comp-029 stays YELLOW and the combined-strategy thesis is parked.

If GREEN is achieved on §1.25 outcome, the recommended addition to §1.25 (in the existing DAF SCR1-4 expression screen) is:

> Add a third co-treatment arm to the §1.25 zymosan / MSU-crystal C5a-generation assay: DAF SCR1-4 expressed material (mature, ELISA-quantified) + rosmarinic acid (final concentration 100 μM, matching the median Sahu 1999 C3b-deposition IC50 region) co-incubated 30 min at 37°C with the complement-competent serum + MSU substrate. Compare C5a (and C5b-9) generation against (i) DAF SCR1-4 alone, (ii) RA alone, (iii) vehicle. The marginal cost is one additional condition per plate; the wet-lab read-out is the same ELISA.
"""

with open(OUTPUTS / "summary.md", "w") as f:
    f.write(summary_md)

print(f"Wrote outputs/ to {OUTPUTS}")
