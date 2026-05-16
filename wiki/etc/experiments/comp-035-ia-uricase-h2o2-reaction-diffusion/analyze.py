#!/usr/bin/env python3
"""
comp-035: Intra-articular uricase H2O2 reaction-diffusion analysis across three
spatial-coupling architectures (Pickering emulsion / fusion protein / free co-formulated).

Reaction-diffusion with Damkohler-number analysis. Stdlib-only Python 3.
Reproduces deterministically with RNG seed 35.

Model summary
-------------
A single uricase active site produces H2O2 at rate q_URI = kcat_URI * [urate]/(Km + [urate])
[for [urate] << Km, simplifies to (kcat/Km) * [urate]; for [urate] >> Km, simplifies to kcat].

In a uniform mixture, the steady-state [H2O2] is governed by
  V * dC/dt = q_URI * N_URI - k_eff_CAT * N_CAT * C - k_clear * V * C = 0
where k_eff_CAT = kcat_CAT / Km_CAT (linear-regime catalase, valid for [H2O2] << Km_CAT ~ 1 M).
This gives the well-mixed bulk [H2O2]_bulk.

For SPATIALLY-COUPLED architectures, the relevant question is not the bulk steady state
but the LOCAL steady state at the uricase active site / architecture boundary. We model
this with a spherical-shell reaction-diffusion solution: a point source of H2O2 at the
uricase site, with catalase distributed at characteristic distance L (the architecture's
spatial-coupling length scale), surrounded by aqueous synovial fluid.

The Damkohler number Da = (catalase scavenging rate at distance L) / (diffusive transport
rate over distance L) = (k_cat_eff_CAT * [CAT]_local * L^2) / D_H2O2.

When Da >> 1: catalase scavenges before diffusion → low escape flux.
When Da ~ 1: partial escape.
When Da << 1: H2O2 escapes architecture before scavenging → high tissue-flux risk.

For the Pickering case, the architecture is a SHELL of catalase at the droplet surface
surrounding interfacial uricase. The radial 1D diffusion-reaction model with a thin
catalase shell yields an explicit escape fraction f_escape = D / (D + k_CAT_shell * L^2 / 2)
where k_CAT_shell is the catalase clearance rate per unit volume in the shell.

For the fusion-protein case, the uricase and catalase active sites are colocated at
separation L_fusion (1-5 nm); the local catalase concentration in the immediate vicinity
of the uricase site is effectively 1 catalase per ~L_fusion^3 volume. We compute the
probability that an H2O2 molecule diffusing away from the uricase site is intercepted by
the colocated catalase via a Smoluchowski-rate-limit calculation.

For the free co-formulated case, the catalase is uniformly distributed at concentration
[CAT]_bulk; an H2O2 molecule has a characteristic capture distance L_capture = sqrt(D /
(k_CAT_eff * [CAT]_bulk)). If L_capture >> 1 µm, H2O2 readily escapes into surrounding
tissue before scavenging.

Each architecture's escape flux is then projected onto the joint-volume steady-state to
predict the [H2O2] at the joint-tissue boundary (synovium / cartilage interface).

Monte Carlo over the input priors (kinetic constants, diffusion coefficients, geometry)
generates the distribution of predictions. The verdict (GREEN / YELLOW / RED) is applied
to the predicted [H2O2] vs the toxicity threshold band.

Sensitivity analysis via Spearman rank correlation between inputs and the
joint-tissue-boundary [H2O2] output.
"""

import json
import math
import os
import random
import sys
import time
from collections import defaultdict
from pathlib import Path

# ----- repro -----
SEED = 35
random.seed(SEED)

# ----- constants -----
N_AVOGADRO = 6.022e23  # /mol

# ----- paths -----
HERE = Path(__file__).resolve().parent
INPUTS = HERE / "inputs"
OUTPUTS = HERE / "outputs"
OUTPUTS.mkdir(exist_ok=True, parents=True)

# ----- monte carlo settings -----
N_MC = 20000


def load_inputs():
    kin = json.loads((INPUTS / "kinetic_constants.json").read_text())
    diff = json.loads((INPUTS / "diffusion_constants.json").read_text())
    geom = json.loads((INPUTS / "architecture_geometry.json").read_text())
    tox = json.loads((INPUTS / "toxicity_thresholds.json").read_text())
    joint = json.loads((INPUTS / "joint_geometry.json").read_text())
    return kin, diff, geom, tox, joint


def log_uniform(lo, hi):
    if lo <= 0:
        lo = 1e-30
    return math.exp(random.uniform(math.log(lo), math.log(hi)))


def uniform(lo, hi):
    return random.uniform(lo, hi)


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


# ===================== reaction rate helpers =====================


def uricase_h2o2_production_rate_per_active_site(kcat, Km, urate_M):
    """Returns H2O2 production rate per uricase active site, in mol/s.

    Each uricase turnover produces 1 H2O2.
    """
    v = kcat * urate_M / (Km + urate_M)  # s^-1
    return v  # H2O2 molecules per active site per second; multiply by 1 (stoich) and / N_A for mol


def catalase_first_order_rate_constant_per_M_per_s(kcat_over_km):
    """Catalase pseudo-first-order: rate = k * [CAT] * [H2O2], with k = kcat/Km (M^-1 s^-1).

    For [H2O2] << Km_CAT (always the case for synovial-relevant concentrations < 1 mM),
    the effective destruction rate of H2O2 per molecule per second is
        r_destruction = k * [CAT_active_sites_in_M]

    Returns k (M^-1 s^-1).
    """
    return kcat_over_km


# ===================== Architecture 1: Pickering emulsion =====================


def pickering_steady_state_h2o2(
    *,
    kcat_URI,
    Km_URI_M,
    urate_M,
    kcat_over_km_CAT,
    droplet_radius_m,
    interfacial_density_per_um2,
    URI_to_CAT_ratio,
    URI_fraction,
    D_H2O2_synovial,
    joint_volume_mL,
    k_clear_per_s,
):
    """Reaction-diffusion steady state for Pickering emulsion architecture.

    Geometry: spherical droplet of radius r_d with URI and CAT co-confined at the
    oil-water interface. H2O2 is produced at the interface (in the aqueous phase
    immediately adjacent to URI) and either:
      (a) is scavenged by adjacent surface CAT (donor-acceptor distance d_FRET ~4-10 nm)
      (b) diffuses radially outward into the aqueous synovial fluid.

    Returns:
      C_local: local steady-state [H2O2] at the droplet surface (M)
      C_joint_bulk: well-mixed bulk synovial [H2O2] after dispersion (M)
      escape_fraction: fraction of generated H2O2 escaping past the catalase shell
      Da: Damkohler number for shell scavenging vs diffusion
      q_per_droplet_mol_per_s: H2O2 generation rate per droplet (mol/s)
    """
    # Surface area per droplet
    A_droplet_um2 = 4 * math.pi * (droplet_radius_m * 1e6) ** 2  # in µm^2
    # Enzymes per droplet
    n_total_per_droplet = interfacial_density_per_um2 * A_droplet_um2
    n_URI_per_droplet = n_total_per_droplet * URI_fraction
    n_CAT_per_droplet = n_total_per_droplet * (1 - URI_fraction)

    # Uricase H2O2 production rate per active site (s^-1, = H2O2 molecules per second)
    v_URI = uricase_h2o2_production_rate_per_active_site(kcat_URI, Km_URI_M, urate_M)
    q_per_droplet_molec_per_s = v_URI * n_URI_per_droplet  # molecules/s per droplet
    q_per_droplet_mol_per_s = q_per_droplet_molec_per_s / N_AVOGADRO

    # Catalase shell scavenging: model the interfacial CAT as a thin shell of thickness
    # ~5 nm just outside the droplet (where FRET measurements place donor-acceptor).
    # The local CAT concentration in the shell is enormous: pack n_CAT_per_droplet
    # catalase molecules into a shell volume of 4*pi*r_d^2 * thickness.
    shell_thickness_m = 5e-9  # 5 nm — comparable to the Liu 2025 FRET distance
    V_shell_m3 = 4 * math.pi * droplet_radius_m**2 * shell_thickness_m
    CAT_in_shell_M = (n_CAT_per_droplet / N_AVOGADRO) / (V_shell_m3 * 1000)  # convert m^3 to L
    # Active sites: catalase tetramer has 4 hemes; n_CAT_per_droplet is molecules — multiply by 4
    CAT_active_sites_in_shell_M = CAT_in_shell_M * 4

    # First-order destruction rate within the shell (s^-1)
    k_dest_in_shell = kcat_over_km_CAT * CAT_active_sites_in_shell_M  # s^-1

    # Damkohler number: Da = k_dest * thickness^2 / D = ratio of reaction rate to diffusion
    # across the shell.
    Da = k_dest_in_shell * shell_thickness_m**2 / D_H2O2_synovial

    # Probability that an H2O2 produced at the inner edge of the shell escapes through
    # to the outer surface without reaction: solution of the 1D diffusion-reaction PDE
    # across a thin shell with reaction k_dest.
    # For a thin reactive shell with reaction k, the escape fraction is approximately
    #   f_escape = 1 / cosh( sqrt(Da) )
    # for the symmetric boundary case (production at one face, absorbing at the other).
    # This is the canonical Thiele-modulus result.
    thiele = math.sqrt(Da)
    if thiele > 50:
        f_escape = 2 * math.exp(-thiele)  # numerical guard
    else:
        f_escape = 1.0 / math.cosh(thiele)
    f_escape = max(f_escape, 1e-30)

    # H2O2 escape rate per droplet (mol/s)
    q_escape_mol_per_s = q_per_droplet_mol_per_s * f_escape

    # Local [H2O2] AT the droplet surface (just outside the catalase shell):
    # For a point source of strength q at the surface of a sphere of radius r_d, the
    # steady-state concentration profile in 3D infinite medium with first-order sink
    # k_clear is C(r) = (q / (4*pi*D*r)) * exp(-r/lambda)
    # where lambda = sqrt(D/k_clear). At r = r_d:
    if k_clear_per_s > 0:
        lam = math.sqrt(D_H2O2_synovial / k_clear_per_s)
    else:
        lam = 1e6
    # C_local in M
    if droplet_radius_m > 0 and D_H2O2_synovial > 0:
        C_local = (
            q_escape_mol_per_s
            / (4 * math.pi * D_H2O2_synovial * droplet_radius_m)
            * math.exp(-droplet_radius_m / lam)
            / 1000  # mol/m^3 -> M (M = mol/L = 1000 mol/m^3)
        )
    else:
        C_local = float("inf")

    # Bulk well-mixed synovial [H2O2]:
    # Per-droplet escape rate × droplet count / (V_joint × clearance_rate)
    # But we need droplet count: total enzyme / per-droplet enzyme.
    # Pickering droplets per dose: total CAT amount / (n_CAT_per_droplet × MW_CAT)
    # We'll work in concentration terms: bulk H2O2 generation rate per L = escape flux per droplet × n_droplets per L
    # For the Liu 2025 dose: 0.23 mg CAT in 20 µL; if injected into 3 mL joint volume,
    # ~0.077 µg/mL CAT × scaling.
    # We need total CAT in joint and partition into droplets.
    # Use 0.23 mg CAT in joint with mass distributed over n_droplet droplets each with
    # n_CAT_per_droplet × MW_CAT.
    # Total CAT mass per joint = 0.23e-3 g (assume full dose into joint)
    # MW CAT = 240 kDa = 240e3 g/mol → mol = 0.23e-6 / 240e3 = 9.58e-13 mol → 5.77e11 molecules
    # n_droplets = 5.77e11 / n_CAT_per_droplet
    CAT_total_molec = 0.23e-3 / 240e3 * N_AVOGADRO  # for 0.23 mg in joint
    n_droplets_per_joint = CAT_total_molec / max(n_CAT_per_droplet, 1)

    V_joint_m3 = joint_volume_mL * 1e-6  # mL to m^3 (1 mL = 1e-6 m^3)
    V_joint_L = joint_volume_mL * 1e-3  # mL to L
    total_escape_rate_mol_per_s = q_escape_mol_per_s * n_droplets_per_joint
    # Bulk catalase concentration AFTER escape: the catalase from all droplets, viewed
    # as a bulk concentration averaged over the joint volume, contributes additional
    # scavenging in the bulk solution. H2O2 escaping one droplet has a high chance of
    # being scavenged by another droplet's catalase before reaching tissue.
    # Total catalase active sites in the joint (mol): CAT_total_molec × 4 active sites / N_A
    CAT_bulk_active_sites_M = (CAT_total_molec * 4 / N_AVOGADRO) / V_joint_L

    # Steady-state bulk:
    #   q_total = (k_clear + k_bulk_CAT) * V * C
    # where k_bulk_CAT = kcat_over_km_CAT × CAT_bulk_active_sites_M
    k_bulk_CAT_per_s = kcat_over_km_CAT * CAT_bulk_active_sites_M
    effective_destruction_rate = k_clear_per_s + k_bulk_CAT_per_s
    if effective_destruction_rate > 0 and V_joint_m3 > 0:
        C_joint_bulk_mol_per_m3 = total_escape_rate_mol_per_s / (
            effective_destruction_rate * V_joint_m3
        )
    else:
        C_joint_bulk_mol_per_m3 = float("inf")
    C_joint_bulk = C_joint_bulk_mol_per_m3 / 1000  # mol/m^3 -> M

    return {
        "C_local_M": C_local,
        "C_joint_bulk_M": C_joint_bulk,
        "C_local_uM": C_local * 1e6,
        "C_joint_bulk_uM": C_joint_bulk * 1e6,
        "escape_fraction": f_escape,
        "Da": Da,
        "thiele_modulus": thiele,
        "CAT_in_shell_M": CAT_in_shell_M,
        "n_droplets_per_joint": n_droplets_per_joint,
        "q_per_droplet_mol_per_s": q_per_droplet_mol_per_s,
        "n_URI_per_droplet": n_URI_per_droplet,
        "n_CAT_per_droplet": n_CAT_per_droplet,
        "CAT_bulk_active_sites_M": CAT_bulk_active_sites_M,
        "k_bulk_CAT_per_s": k_bulk_CAT_per_s,
    }


# ===================== Architecture 2: Fusion protein =====================


def fusion_steady_state_h2o2(
    *,
    kcat_URI,
    Km_URI_M,
    urate_M,
    kcat_over_km_CAT,
    active_site_separation_m,
    fusion_concentration_M,
    D_H2O2_synovial,
    joint_volume_mL,
    k_clear_per_s,
):
    """Reaction-diffusion for a uricase-catalase fusion protein.

    Geometry: each fusion molecule has a uricase domain and a catalase domain separated
    by distance L_fusion (1-5 nm). H2O2 generated at the uricase active site can:
      (a) diffuse to the colocated catalase domain (very short distance — fast)
      (b) diffuse out into the bulk where it encounters other fusion molecules' catalase
          domains at concentration [fusion] (= [CAT]_bulk).

    The Smoluchowski rate of intramolecular capture by the colocated catalase active site
    is k_intra = 4*pi*D*r_cat / (1 - r_cat/L) where r_cat is the catalase active-site
    radius (~1 nm) and L is the separation. For L = 2 nm and r_cat = 1 nm, this gives
    k_intra = 8*pi*D*r_cat = ~1.4e-11 m^3/s (extremely fast capture).

    Compare to escape rate to bulk: 1 H2O2 molecule diffuses away from the uricase active
    site with characteristic time tau_escape = L^2 / (6D). The probability of intra-
    molecular capture is P_capture = k_intra * n_cat / (k_intra * n_cat + k_escape_bulk)
    where n_cat = 1 (one colocated catalase) and k_escape_bulk is the rate of leaving the
    inner sphere of radius ~L without reaction.

    Simplified: for L_fusion < 5 nm and intramolecular catalase, intramolecular capture
    probability is ~1 (the diffusion-controlled rate is at the upper bound of enzyme
    kinetics). We use a more rigorous expression below.
    """
    # H2O2 production rate per uricase domain
    v_URI = uricase_h2o2_production_rate_per_active_site(kcat_URI, Km_URI_M, urate_M)  # s^-1

    # Intramolecular catalase capture: model as a 3D random walk return-to-origin problem.
    # The probability that an H2O2 molecule starting at distance L from a sphere of radius
    # r_capture (catalase active-site cavity, ~0.5-1 nm) is captured before escaping to
    # infinity in an infinite-medium 3D walk is:
    #   P_capture = r_capture / L
    # (canonical Smoluchowski result for first-passage to absorbing sphere in 3D.)
    r_capture_m = 0.7e-9  # ~7 Å effective capture radius (catalase active-site channel)
    P_capture_intra = min(0.999, r_capture_m / active_site_separation_m)

    # H2O2 that escapes the intramolecular trap enters the bulk and is scavenged by other
    # fusion molecules' catalase domains at concentration [fusion]. The bulk capture rate:
    # The effective second-order rate constant for bulk capture by free catalase is the
    # diffusion-controlled limit modified by the rate constant of catalase:
    #   k_bulk_eff = kcat_over_km_CAT  (already includes the Smoluchowski-like rate)
    # Concentration of catalase active sites in bulk:
    n_active_sites_per_fusion = 4  # one catalase tetramer = 4 hemes (assume CAT moiety is tetrameric)
    CAT_active_sites_M = fusion_concentration_M * n_active_sites_per_fusion
    # Bulk capture rate per H2O2 molecule:
    k_bulk_capture_per_s = kcat_over_km_CAT * CAT_active_sites_M

    # Bulk capture distance:
    if k_bulk_capture_per_s > 0:
        L_bulk_capture_m = math.sqrt(D_H2O2_synovial / k_bulk_capture_per_s)
    else:
        L_bulk_capture_m = 1e6

    # Fraction of H2O2 escaping into the synovial-tissue boundary:
    # f_total_escape ≈ (1 - P_capture_intra) × (1 - P_capture_bulk)
    # P_capture_bulk for a small joint of characteristic radius R_joint:
    R_joint_m = (3 * joint_volume_mL * 1e-6 / (4 * math.pi)) ** (1 / 3)  # equivalent sphere radius
    # Fraction NOT captured in bulk = exp(-R_joint / L_bulk_capture)
    P_NOT_capture_bulk = math.exp(-min(50, R_joint_m / max(L_bulk_capture_m, 1e-15)))
    P_capture_bulk = 1 - P_NOT_capture_bulk
    f_total_escape = (1 - P_capture_intra) * P_NOT_capture_bulk

    # Bulk steady-state: H2O2 that escapes intramolecular trap enters bulk, where it
    # is destroyed by (a) other fusion molecules' catalase domains (bulk catalase) and
    # (b) joint clearance.
    # Effective bulk H2O2 production rate (M/s):
    #   q_eff = v_URI * [URI in bulk] * (1 - P_capture_intra)
    # where [URI in bulk] = fusion_concentration_M (one URI per fusion, in active sites
    # multiply by 4 if uricase moiety is tetrameric; assume monomeric URI domain in
    # fusion).
    URI_active_sites_per_fusion = 1  # conservative; fusion architectures typically express monomeric uricase
    URI_active_M = fusion_concentration_M * URI_active_sites_per_fusion
    q_eff_M_per_s = v_URI * URI_active_M * (1 - P_capture_intra)

    # Bulk catalase destruction rate: same fusion concentration provides CAT
    CAT_active_M_bulk = fusion_concentration_M * n_active_sites_per_fusion
    k_bulk_destruction = kcat_over_km_CAT * CAT_active_M_bulk  # s^-1

    # Joint clearance + bulk catalase
    effective_destruction = k_clear_per_s + k_bulk_destruction
    if effective_destruction > 0:
        C_joint_bulk = q_eff_M_per_s / effective_destruction
    else:
        C_joint_bulk = float("inf")

    V_joint_m3 = joint_volume_mL * 1e-6
    V_joint_L = joint_volume_mL * 1e-3
    n_fusion_molecules = fusion_concentration_M * V_joint_L * N_AVOGADRO

    # Damkohler: intramolecular capture vs intramolecular escape
    Da_intra = P_capture_intra / max(1 - P_capture_intra, 1e-30)

    return {
        "C_joint_bulk_M": C_joint_bulk,
        "C_joint_bulk_uM": C_joint_bulk * 1e6,
        "P_capture_intra": P_capture_intra,
        "P_capture_bulk": P_capture_bulk,
        "f_total_escape": f_total_escape,
        "Da_intra": Da_intra,
        "L_bulk_capture_m": L_bulk_capture_m,
        "L_bulk_capture_um": L_bulk_capture_m * 1e6,
        "R_joint_m": R_joint_m,
        "n_fusion_molecules": n_fusion_molecules,
        "v_URI_per_active_site_per_s": v_URI,
        "q_eff_M_per_s_bulk": q_eff_M_per_s,
        "k_bulk_destruction_per_s": k_bulk_destruction,
        "CAT_active_M_bulk": CAT_active_M_bulk,
    }


# ===================== Architecture 3: Free co-formulated =====================


def free_co_formulated_steady_state_h2o2(
    *,
    kcat_URI,
    Km_URI_M,
    urate_M,
    kcat_over_km_CAT,
    URI_concentration_M,
    CAT_concentration_M,
    D_H2O2_synovial,
    joint_volume_mL,
    k_clear_per_s,
):
    """Reaction-diffusion for free co-formulated catalase + uricase.

    Geometry: well-mixed solution of URI and CAT at concentrations [URI] and [CAT].
    Mean inter-enzyme spacing d ≈ ([URI]+[CAT]) * N_A )^(-1/3).
    H2O2 is produced uniformly throughout the volume; catalase scavenges H2O2 via
    second-order kinetics with rate constant kcat/Km.

    The characteristic capture length is L_capture = sqrt(D / (kcat/Km * [CAT]_M)).
    If L_capture > size of architecture/joint, escape is significant.
    """
    n_URI_active_sites_per_molecule = 4  # tetramer
    n_CAT_active_sites_per_molecule = 4
    URI_active_M = URI_concentration_M * n_URI_active_sites_per_molecule
    CAT_active_M = CAT_concentration_M * n_CAT_active_sites_per_molecule

    # Bulk H2O2 production rate per L:
    v_URI = uricase_h2o2_production_rate_per_active_site(kcat_URI, Km_URI_M, urate_M)
    # Production rate per liter (in molecules / L / s):
    q_per_L_molec_per_s = v_URI * URI_active_M * N_AVOGADRO  # ÷ does check: [URI_active_M] = mol/L, v_URI = molec/site/s
    # ⇒ q = mol/L * (molec/site/s) * (sites/mol) = molec/L/s. Off by Avogadro.
    # Re-derive: production rate in M/s = v_URI [per second] × [URI_active]_M
    q_M_per_s = v_URI * URI_active_M

    # Bulk catalase scavenging rate (M/s) = kcat_over_km * [CAT_active] * [H2O2]_bulk
    # At steady state: q_M_per_s = k_clear * [H2O2] + kcat_over_km * CAT_active * [H2O2]
    # ⇒ [H2O2]_ss = q_M_per_s / (k_clear + kcat_over_km * CAT_active_M)
    total_destruction_rate_per_s = k_clear_per_s + kcat_over_km_CAT * CAT_active_M
    if total_destruction_rate_per_s > 0:
        C_joint_bulk = q_M_per_s / total_destruction_rate_per_s
    else:
        C_joint_bulk = float("inf")

    # Capture length scale:
    if kcat_over_km_CAT * CAT_active_M > 0:
        L_capture_m = math.sqrt(D_H2O2_synovial / (kcat_over_km_CAT * CAT_active_M))
    else:
        L_capture_m = 1e6

    # Mean inter-enzyme spacing
    total_enzyme_M = URI_concentration_M + CAT_concentration_M
    if total_enzyme_M > 0:
        mean_spacing_m = (total_enzyme_M * N_AVOGADRO * 1000) ** (-1 / 3)  # mol/L -> /m^3 conv
    else:
        mean_spacing_m = 1e6

    # Damkohler: capture rate over capture length L_capture vs diffusion over same length
    # Da = (kcat_over_km_CAT * CAT_active_M) * L_capture^2 / D
    # By construction L_capture = sqrt(D / (k * [CAT])) so Da = 1 at capture length
    # The relevant Da for tissue-escape is computed at joint radius:
    V_joint_m3 = joint_volume_mL * 1e-6
    R_joint_m = (3 * V_joint_m3 / (4 * math.pi)) ** (1 / 3)
    Da_joint = (kcat_over_km_CAT * CAT_active_M) * R_joint_m**2 / D_H2O2_synovial

    return {
        "C_joint_bulk_M": C_joint_bulk,
        "C_joint_bulk_uM": C_joint_bulk * 1e6,
        "L_capture_m": L_capture_m,
        "L_capture_um": L_capture_m * 1e6,
        "mean_spacing_nm": mean_spacing_m * 1e9,
        "Da_joint": Da_joint,
        "q_M_per_s": q_M_per_s,
        "URI_active_M": URI_active_M,
        "CAT_active_M": CAT_active_M,
    }


# ===================== Sampling priors =====================


def sample_inputs(kin, diff, geom, tox, joint):
    """Draw one Monte Carlo sample. Returns dict of sampled inputs + architecture concs."""
    s = {}
    # Kinetic constants
    s["kcat_URI"] = log_uniform(
        kin["uricase_a_flavus"]["kcat_per_s"]["lower"],
        kin["uricase_a_flavus"]["kcat_per_s"]["upper"],
    )
    s["Km_URI_M"] = log_uniform(
        kin["uricase_a_flavus"]["Km_urate_M"]["lower"],
        kin["uricase_a_flavus"]["Km_urate_M"]["upper"],
    )
    s["kcat_over_km_CAT"] = log_uniform(
        kin["catalase_bovine_liver"]["kcat_over_km_per_M_per_s"]["lower"],
        kin["catalase_bovine_liver"]["kcat_over_km_per_M_per_s"]["upper"],
    )
    # Diffusion
    s["D_H2O2_synovial"] = log_uniform(
        diff["h2o2_diffusion_synovial_fluid_37C_m2_per_s"]["lower"],
        diff["h2o2_diffusion_synovial_fluid_37C_m2_per_s"]["upper"],
    )
    # Joint geometry
    s["joint_volume_mL"] = log_uniform(
        joint["human_knee"]["synovial_fluid_volume_mL"]["lower"],
        joint["human_knee"]["synovial_fluid_volume_mL"]["upper"],
    )
    s["urate_M"] = log_uniform(
        joint["urate_substrate_concentration_at_msu_surface_mM"]["lower"] * 1e-3,
        joint["urate_substrate_concentration_at_msu_surface_mM"]["upper"] * 1e-3,
    )
    s["k_clear_per_s"] = log_uniform(
        joint["joint_clearance_h2o2_rate_per_s"]["lower"],
        joint["joint_clearance_h2o2_rate_per_s"]["upper"],
    )

    # Architecture-specific
    pick = geom["pickering_emulsion_liu_2025"]
    s["pick_droplet_diameter_nm"] = uniform(
        pick["droplet_hydrodynamic_diameter_nm"]["PECU_uri_cat_only"],
        pick["droplet_hydrodynamic_diameter_nm"]["PEBR_with_MTX"],
    )
    s["pick_interfacial_density_per_um2"] = log_uniform(
        pick["interfacial_enzyme_density_per_um2"]["operating_density_per_um2"]["lower"],
        pick["interfacial_enzyme_density_per_um2"]["operating_density_per_um2"]["upper"],
    )
    s["pick_URI_fraction"] = 4.0 / (4.0 + 1.0)  # 4:1 URI:CAT mass; assume similar per molecule

    fus = geom["uricase_catalase_fusion_protein"]
    s["fusion_active_site_sep_nm"] = uniform(
        fus["active_site_separation_nm"]["lower"], fus["active_site_separation_nm"]["upper"]
    )
    s["fusion_concentration_uM"] = log_uniform(
        fus["effective_concentration_uM"]["lower"], fus["effective_concentration_uM"]["upper"]
    )

    free = geom["free_co_formulated"]
    s["free_URI_uM"] = log_uniform(
        free["uri_concentration_uM"]["lower"], free["uri_concentration_uM"]["upper"]
    )
    s["free_CAT_uM"] = log_uniform(
        free["cat_concentration_uM"]["lower"], free["cat_concentration_uM"]["upper"]
    )
    return s


def run_one_sample(s):
    """Run all 3 architectures on one sample. Returns dict of outputs."""
    # Pickering
    pick_out = pickering_steady_state_h2o2(
        kcat_URI=s["kcat_URI"],
        Km_URI_M=s["Km_URI_M"],
        urate_M=s["urate_M"],
        kcat_over_km_CAT=s["kcat_over_km_CAT"],
        droplet_radius_m=s["pick_droplet_diameter_nm"] * 1e-9 / 2,
        interfacial_density_per_um2=s["pick_interfacial_density_per_um2"],
        URI_to_CAT_ratio=4.0,
        URI_fraction=s["pick_URI_fraction"],
        D_H2O2_synovial=s["D_H2O2_synovial"],
        joint_volume_mL=s["joint_volume_mL"],
        k_clear_per_s=s["k_clear_per_s"],
    )

    # Fusion
    fus_out = fusion_steady_state_h2o2(
        kcat_URI=s["kcat_URI"],
        Km_URI_M=s["Km_URI_M"],
        urate_M=s["urate_M"],
        kcat_over_km_CAT=s["kcat_over_km_CAT"],
        active_site_separation_m=s["fusion_active_site_sep_nm"] * 1e-9,
        fusion_concentration_M=s["fusion_concentration_uM"] * 1e-6,
        D_H2O2_synovial=s["D_H2O2_synovial"],
        joint_volume_mL=s["joint_volume_mL"],
        k_clear_per_s=s["k_clear_per_s"],
    )

    # Free
    free_out = free_co_formulated_steady_state_h2o2(
        kcat_URI=s["kcat_URI"],
        Km_URI_M=s["Km_URI_M"],
        urate_M=s["urate_M"],
        kcat_over_km_CAT=s["kcat_over_km_CAT"],
        URI_concentration_M=s["free_URI_uM"] * 1e-6,
        CAT_concentration_M=s["free_CAT_uM"] * 1e-6,
        D_H2O2_synovial=s["D_H2O2_synovial"],
        joint_volume_mL=s["joint_volume_mL"],
        k_clear_per_s=s["k_clear_per_s"],
    )

    return {"pickering": pick_out, "fusion": fus_out, "free": free_out}


# ===================== Verdict logic =====================


def architecture_verdict(C_uM, green_upper, yellow_upper):
    """GREEN < green_upper <= YELLOW < yellow_upper <= RED."""
    if math.isnan(C_uM) or C_uM < 0:
        return "UNDEFINED"
    if C_uM < green_upper:
        return "GREEN"
    elif C_uM < yellow_upper:
        return "YELLOW"
    else:
        return "RED"


def verdict_distribution(C_uM_list, green_upper, yellow_upper):
    counts = defaultdict(int)
    for c in C_uM_list:
        counts[architecture_verdict(c, green_upper, yellow_upper)] += 1
    total = max(len(C_uM_list), 1)
    return {k: v / total for k, v in counts.items()}


# ===================== Sensitivity (Spearman rank correlation) =====================


def rank(xs):
    """Return ranks of xs (1-based, ties averaged)."""
    n = len(xs)
    indexed = sorted(range(n), key=lambda i: xs[i])
    ranks = [0.0] * n
    i = 0
    while i < n:
        j = i
        while j + 1 < n and xs[indexed[j + 1]] == xs[indexed[i]]:
            j += 1
        avg_rank = (i + j) / 2.0 + 1
        for k in range(i, j + 1):
            ranks[indexed[k]] = avg_rank
        i = j + 1
    return ranks


def spearman(x, y):
    rx = rank(x)
    ry = rank(y)
    n = len(rx)
    mean_rx = sum(rx) / n
    mean_ry = sum(ry) / n
    num = sum((rx[i] - mean_rx) * (ry[i] - mean_ry) for i in range(n))
    den_x = math.sqrt(sum((rx[i] - mean_rx) ** 2 for i in range(n)))
    den_y = math.sqrt(sum((ry[i] - mean_ry) ** 2 for i in range(n)))
    if den_x == 0 or den_y == 0:
        return 0.0
    return num / (den_x * den_y)


def sensitivity_analysis(samples_list, outputs_list, output_key):
    """Spearman correlation between each input dimension and a specific output."""
    sample_keys = sorted(samples_list[0].keys())
    y = [o[output_key] for o in outputs_list]
    results = {}
    for k in sample_keys:
        x = [s[k] for s in samples_list]
        try:
            results[k] = spearman(x, y)
        except Exception as e:
            results[k] = None
    return results


# ===================== Main =====================


def main():
    t0 = time.time()
    kin, diff, geom, tox, joint = load_inputs()

    green_upper = tox["synovial_tissue_threshold_derived_uM"]["GREEN_below_uM"]["central"]
    yellow_upper = tox["synovial_tissue_threshold_derived_uM"]["RED_above_uM"]["central"]

    print(f"comp-035: Monte Carlo with N = {N_MC}, seed = {SEED}")
    print(f"GREEN threshold: <{green_upper} µM steady-state H2O2 at tissue boundary")
    print(f"YELLOW band: {green_upper}-{yellow_upper} µM")
    print(f"RED threshold: >{yellow_upper} µM")
    print()

    samples = []
    pickering_C = []
    fusion_C = []
    free_C = []
    pickering_Da = []
    fusion_Pintra = []
    free_Da = []
    pickering_escape = []
    pickering_local_C = []
    fusion_Lcap = []
    free_Lcap = []

    for i in range(N_MC):
        s = sample_inputs(kin, diff, geom, tox, joint)
        out = run_one_sample(s)
        samples.append(s)
        pickering_C.append(out["pickering"]["C_joint_bulk_uM"])
        pickering_local_C.append(out["pickering"]["C_local_uM"])
        fusion_C.append(out["fusion"]["C_joint_bulk_uM"])
        free_C.append(out["free"]["C_joint_bulk_uM"])
        pickering_Da.append(out["pickering"]["Da"])
        fusion_Pintra.append(out["fusion"]["P_capture_intra"])
        free_Da.append(out["free"]["Da_joint"])
        pickering_escape.append(out["pickering"]["escape_fraction"])
        fusion_Lcap.append(out["fusion"]["L_bulk_capture_um"])
        free_Lcap.append(out["free"]["L_capture_um"])

    # Aggregate stats
    pickering_stats = stats(pickering_C)
    fusion_stats = stats(fusion_C)
    free_stats = stats(free_C)
    pickering_local_stats = stats(pickering_local_C)
    pickering_Da_stats = stats(pickering_Da)
    fusion_Pintra_stats = stats(fusion_Pintra)
    free_Da_stats = stats(free_Da)
    pickering_escape_stats = stats(pickering_escape)
    fusion_Lcap_stats = stats(fusion_Lcap)
    free_Lcap_stats = stats(free_Lcap)

    # Verdicts
    pickering_verdict = verdict_distribution(pickering_C, green_upper, yellow_upper)
    fusion_verdict = verdict_distribution(fusion_C, green_upper, yellow_upper)
    free_verdict = verdict_distribution(free_C, green_upper, yellow_upper)
    pickering_local_verdict = verdict_distribution(pickering_local_C, green_upper, yellow_upper)

    # Sensitivity
    sens_pickering = sensitivity_analysis(
        samples,
        [{"x": c} for c in pickering_C],
        "x",
    )
    sens_fusion = sensitivity_analysis(samples, [{"x": c} for c in fusion_C], "x")
    sens_free = sensitivity_analysis(samples, [{"x": c} for c in free_C], "x")

    # Per-architecture verdict on the MEDIAN sample
    headline_pickering = architecture_verdict(
        pickering_stats["median"], green_upper, yellow_upper
    )
    headline_fusion = architecture_verdict(
        fusion_stats["median"], green_upper, yellow_upper
    )
    headline_free = architecture_verdict(
        free_stats["median"], green_upper, yellow_upper
    )

    # ===== Edge-case scenarios — worst-case dose / kinetic regimes =====
    # Run additional focused scenarios to test architecture robustness.
    edge_cases = {}

    def force_sample(template, **overrides):
        s = dict(template)
        s.update(overrides)
        return s

    template = sample_inputs(kin, diff, geom, tox, joint)  # one random base

    edge_scenarios = {
        "low_CAT_dose_1uM": {"free_CAT_uM": 1.0, "fusion_concentration_uM": 1.0},
        "high_dose_100uM": {"free_CAT_uM": 100.0, "free_URI_uM": 100.0, "fusion_concentration_uM": 100.0},
        "high_urate_5mM": {"urate_M": 5e-3},
        "low_urate_0.1mM": {"urate_M": 1e-4},
        "low_clearance_0.001": {"k_clear_per_s": 0.001},
        "high_kcat_URI_20": {"kcat_URI": 20.0},
        "low_kcat_over_km_CAT_1e7": {"kcat_over_km_CAT": 1e7},
        "small_joint_MTP1_0.3mL": {"joint_volume_mL": 0.3},
        "uneven_free_URI_100uM_CAT_1uM": {"free_URI_uM": 100.0, "free_CAT_uM": 1.0},
    }

    for name, override in edge_scenarios.items():
        # Fix all other parameters at central values for clean comparison
        central = {
            "kcat_URI": kin["uricase_a_flavus"]["kcat_per_s"]["central"],
            "Km_URI_M": kin["uricase_a_flavus"]["Km_urate_M"]["central"],
            "kcat_over_km_CAT": kin["catalase_bovine_liver"]["kcat_over_km_per_M_per_s"]["central"],
            "D_H2O2_synovial": diff["h2o2_diffusion_synovial_fluid_37C_m2_per_s"]["central"],
            "joint_volume_mL": joint["human_knee"]["synovial_fluid_volume_mL"]["central"],
            "urate_M": joint["urate_substrate_concentration_at_msu_surface_mM"]["central"] * 1e-3,
            "k_clear_per_s": joint["joint_clearance_h2o2_rate_per_s"]["central"],
            "pick_droplet_diameter_nm": (
                geom["pickering_emulsion_liu_2025"]["droplet_hydrodynamic_diameter_nm"]["PECU_uri_cat_only"]
                + geom["pickering_emulsion_liu_2025"]["droplet_hydrodynamic_diameter_nm"]["PEBR_with_MTX"]
            )
            / 2,
            "pick_interfacial_density_per_um2": geom["pickering_emulsion_liu_2025"]["interfacial_enzyme_density_per_um2"]["operating_density_per_um2"]["central"],
            "pick_URI_fraction": 4.0 / 5.0,
            "fusion_active_site_sep_nm": geom["uricase_catalase_fusion_protein"]["active_site_separation_nm"]["central"],
            "fusion_concentration_uM": geom["uricase_catalase_fusion_protein"]["effective_concentration_uM"]["central"],
            "free_URI_uM": geom["free_co_formulated"]["uri_concentration_uM"]["central"],
            "free_CAT_uM": geom["free_co_formulated"]["cat_concentration_uM"]["central"],
        }
        s_edge = force_sample(central, **override)
        out_edge = run_one_sample(s_edge)
        edge_cases[name] = {
            "pickering_C_joint_uM": out_edge["pickering"]["C_joint_bulk_uM"],
            "fusion_C_joint_uM": out_edge["fusion"]["C_joint_bulk_uM"],
            "free_C_joint_uM": out_edge["free"]["C_joint_bulk_uM"],
            "verdicts": {
                "pickering": architecture_verdict(out_edge["pickering"]["C_joint_bulk_uM"], green_upper, yellow_upper),
                "fusion": architecture_verdict(out_edge["fusion"]["C_joint_bulk_uM"], green_upper, yellow_upper),
                "free": architecture_verdict(out_edge["free"]["C_joint_bulk_uM"], green_upper, yellow_upper),
            },
        }

    (OUTPUTS / "edge_case_scenarios.json").write_text(json.dumps(edge_cases, indent=2))

    # Write outputs
    damkohler_summary = {
        "pickering_Da_shell": pickering_Da_stats,
        "pickering_escape_fraction": pickering_escape_stats,
        "fusion_P_capture_intra": fusion_Pintra_stats,
        "fusion_bulk_capture_length_um": fusion_Lcap_stats,
        "free_Da_joint_scale": free_Da_stats,
        "free_capture_length_um": free_Lcap_stats,
        "interpretation": {
            "pickering": (
                "Pickering Da_shell measures catalase shell scavenging rate vs H2O2 "
                "diffusion across the shell thickness. Da >> 1 means H2O2 is "
                "destroyed before crossing the shell — architecture closes the gap."
            ),
            "fusion": (
                "Fusion P_capture_intra is the Smoluchowski first-passage probability "
                "that H2O2 generated at the uricase active site is captured by the "
                "intramolecular catalase domain before escape to bulk. P_capture > 0.5 "
                "means most H2O2 is captured locally."
            ),
            "free": (
                "Free-coformulated Da_joint compares bulk catalase capture rate over the "
                "joint volume vs diffusion across joint radius. Da >> 1 means catalase "
                "captures H2O2 before it diffuses to the tissue boundary."
            ),
        },
    }
    (OUTPUTS / "damkohler_per_architecture.json").write_text(
        json.dumps(damkohler_summary, indent=2)
    )

    steady_state_summary = {
        "pickering_C_joint_bulk_uM": pickering_stats,
        "pickering_C_local_at_droplet_uM": pickering_local_stats,
        "fusion_C_joint_bulk_uM": fusion_stats,
        "free_C_joint_bulk_uM": free_stats,
    }
    (OUTPUTS / "steady_state_h2o2.json").write_text(
        json.dumps(steady_state_summary, indent=2)
    )

    escape_summary = {
        "pickering_escape_fraction_through_catalase_shell": pickering_escape_stats,
        "fusion_total_escape_fraction_through_intra_and_bulk": stats(
            [(1 - p) for p in fusion_Pintra]
        ),
        "free_NO_intramolecular_scavenging_so_only_bulk_capture": (
            "Free coformulated has no intramolecular trap. The relevant 'escape' is "
            "the joint-volume bulk steady-state, reported in steady_state_h2o2.json."
        ),
    }
    (OUTPUTS / "escape_flux.json").write_text(json.dumps(escape_summary, indent=2))

    sensitivity_summary = {
        "pickering_top_drivers": sorted(
            sens_pickering.items(), key=lambda kv: abs(kv[1] or 0), reverse=True
        )[:8],
        "fusion_top_drivers": sorted(
            sens_fusion.items(), key=lambda kv: abs(kv[1] or 0), reverse=True
        )[:8],
        "free_top_drivers": sorted(
            sens_free.items(), key=lambda kv: abs(kv[1] or 0), reverse=True
        )[:8],
        "note": (
            "Spearman rank correlation between each Monte Carlo input dimension and "
            "the architecture's predicted joint-bulk steady-state [H2O2] (µM). "
            "Higher |r| ⇒ that input dominates the output uncertainty."
        ),
    }
    (OUTPUTS / "sensitivity_analysis.json").write_text(
        json.dumps(sensitivity_summary, indent=2)
    )

    ranking_summary = {
        "verdict_distributions": {
            "pickering_joint_bulk": pickering_verdict,
            "pickering_local_at_droplet": pickering_local_verdict,
            "fusion_joint_bulk": fusion_verdict,
            "free_joint_bulk": free_verdict,
        },
        "headline_verdict_median": {
            "pickering": headline_pickering,
            "fusion": headline_fusion,
            "free": headline_free,
        },
        "decision_rule": {
            "GREEN_upper_uM": green_upper,
            "YELLOW_upper_uM": yellow_upper,
            "logic": (
                "GREEN: median predicted [H2O2] at joint-tissue boundary < GREEN_upper; "
                "YELLOW: median in [GREEN_upper, YELLOW_upper); RED: median ≥ YELLOW_upper."
            ),
        },
        "ranking_lowest_to_highest_h2o2": sorted(
            [
                ("pickering", pickering_stats["median"]),
                ("fusion", fusion_stats["median"]),
                ("free_co_formulated", free_stats["median"]),
            ],
            key=lambda kv: kv[1],
        ),
    }
    (OUTPUTS / "architecture_ranking.json").write_text(
        json.dumps(ranking_summary, indent=2)
    )

    elapsed = time.time() - t0

    # Summary markdown
    summary_md = f"""# comp-035 Analysis Summary (v1)

Generated: 2026-05-16 — RNG seed {SEED}, N = {N_MC} Monte Carlo samples — elapsed {elapsed:.2f}s

## Decision rule

| Band | Steady-state [H₂O₂] at joint-tissue boundary |
|---|---|
| GREEN | < {green_upper} µM |
| YELLOW | {green_upper}-{yellow_upper} µM |
| RED | > {yellow_upper} µM |

## Predicted steady-state [H₂O₂] at joint-tissue boundary

| Architecture | p5 | median | p95 | Headline verdict (median) |
|---|---|---|---|---|
| Pickering emulsion (Liu 2025 geometry) | {pickering_stats['p5']:.2e} µM | {pickering_stats['median']:.2e} µM | {pickering_stats['p95']:.2e} µM | **{headline_pickering}** |
| Fusion protein | {fusion_stats['p5']:.2e} µM | {fusion_stats['median']:.2e} µM | {fusion_stats['p95']:.2e} µM | **{headline_fusion}** |
| Free co-formulated | {free_stats['p5']:.2e} µM | {free_stats['median']:.2e} µM | {free_stats['p95']:.2e} µM | **{headline_free}** |

(Pickering LOCAL [H₂O₂] just outside the droplet shell: p5 {pickering_local_stats['p5']:.2e}, median {pickering_local_stats['median']:.2e}, p95 {pickering_local_stats['p95']:.2e} µM.)

## Damkohler / coupling regime

| Architecture | Quantity | p5 | median | p95 |
|---|---|---|---|---|
| Pickering | Da_shell | {pickering_Da_stats['p5']:.2e} | {pickering_Da_stats['median']:.2e} | {pickering_Da_stats['p95']:.2e} |
| Pickering | escape fraction | {pickering_escape_stats['p5']:.2e} | {pickering_escape_stats['median']:.2e} | {pickering_escape_stats['p95']:.2e} |
| Fusion | P_capture_intra | {fusion_Pintra_stats['p5']:.3f} | {fusion_Pintra_stats['median']:.3f} | {fusion_Pintra_stats['p95']:.3f} |
| Fusion | bulk-capture L (µm) | {fusion_Lcap_stats['p5']:.2e} | {fusion_Lcap_stats['median']:.2e} | {fusion_Lcap_stats['p95']:.2e} |
| Free | Da_joint | {free_Da_stats['p5']:.2e} | {free_Da_stats['median']:.2e} | {free_Da_stats['p95']:.2e} |
| Free | capture L (µm) | {free_Lcap_stats['p5']:.2e} | {free_Lcap_stats['median']:.2e} | {free_Lcap_stats['p95']:.2e} |

## Architecture ranking (lowest to highest predicted [H₂O₂])

1. {ranking_summary['ranking_lowest_to_highest_h2o2'][0][0]}: {ranking_summary['ranking_lowest_to_highest_h2o2'][0][1]:.2e} µM
2. {ranking_summary['ranking_lowest_to_highest_h2o2'][1][0]}: {ranking_summary['ranking_lowest_to_highest_h2o2'][1][1]:.2e} µM
3. {ranking_summary['ranking_lowest_to_highest_h2o2'][2][0]}: {ranking_summary['ranking_lowest_to_highest_h2o2'][2][1]:.2e} µM

## Verdict distribution

| Architecture | P(GREEN) | P(YELLOW) | P(RED) |
|---|---|---|---|
| Pickering (joint bulk) | {pickering_verdict.get('GREEN', 0):.3f} | {pickering_verdict.get('YELLOW', 0):.3f} | {pickering_verdict.get('RED', 0):.3f} |
| Fusion | {fusion_verdict.get('GREEN', 0):.3f} | {fusion_verdict.get('YELLOW', 0):.3f} | {fusion_verdict.get('RED', 0):.3f} |
| Free coformulated | {free_verdict.get('GREEN', 0):.3f} | {free_verdict.get('YELLOW', 0):.3f} | {free_verdict.get('RED', 0):.3f} |

## Top sensitivity drivers

### Pickering
{chr(10).join(f"- {k}: r = {v:.3f}" for k, v in sensitivity_summary['pickering_top_drivers'][:5])}

### Fusion
{chr(10).join(f"- {k}: r = {v:.3f}" for k, v in sensitivity_summary['fusion_top_drivers'][:5])}

### Free coformulated
{chr(10).join(f"- {k}: r = {v:.3f}" for k, v in sensitivity_summary['free_top_drivers'][:5])}

## Edge-case scenarios

| Scenario | Pickering [H₂O₂] (µM) | Fusion [H₂O₂] (µM) | Free [H₂O₂] (µM) | Picker | Fus | Free |
|---|---|---|---|---|---|---|
{chr(10).join(f"| {n} | {ec['pickering_C_joint_uM']:.2e} | {ec['fusion_C_joint_uM']:.2e} | {ec['free_C_joint_uM']:.2e} | {ec['verdicts']['pickering']} | {ec['verdicts']['fusion']} | {ec['verdicts']['free']} |" for n, ec in edge_cases.items())}

## Reproduction

```bash
cd experiments/comp-035-ia-uricase-h2o2-reaction-diffusion
python3 analyze.py
```

Stdlib-only Python 3. Deterministic given seed {SEED}. All inputs in `inputs/`, all outputs regenerated under `outputs/`.
"""
    (OUTPUTS / "summary.md").write_text(summary_md)

    print(summary_md)
    print(f"\nDone. Elapsed: {elapsed:.2f}s")


if __name__ == "__main__":
    main()
