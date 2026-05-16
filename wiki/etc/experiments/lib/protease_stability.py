"""
experiments/lib/protease_stability.py

Shared library for AlphaFold pLDDT-based protease stability analysis.
Used by any comp-NNN experiment that maps protease cleavage-site vulnerability
against structural confidence under defined fermentation conditions.

Exports functions only — no main(). Each experiment's analyze.py is the
orchestrator that imports what it needs and defines its own main().

Usage in an experiment's analyze.py:
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))
    from protease_stability import (
        load_sequence, load_plddt, load_proteases,
        compute_sequence_stats, run_all_proteases,
    )
"""

import json
from pathlib import Path

# pLDDT classification thresholds (AlphaFold confidence score, 0-100)
PLDDT_BURIED = 80.0      # >= 80: well-folded, likely buried
PLDDT_PARTIAL = 65.0     # 65-80: partially exposed
                          # < 65: disordered / surface-exposed

# Accessibility risk weights (fraction of maximum protease-driven risk)
ACCESSIBILITY_SCORES = {
    "buried":            0.1,
    "partially_exposed": 0.4,
    "exposed":           1.0,
}


# ---------------------------------------------------------------------------
# I/O helpers
# ---------------------------------------------------------------------------

def load_sequence(fasta_path):
    """Load a single protein sequence from a FASTA file. Returns string."""
    seq = ""
    with open(fasta_path) as f:
        for line in f:
            if not line.startswith(">"):
                seq += line.strip()
    return seq


def load_plddt(plddt_path):
    """
    Load per-residue AlphaFold pLDDT scores.
    Expects JSON: {"1": 97.2, "2": 95.1, ...} (1-indexed, string keys).
    Returns dict with int keys.
    """
    with open(plddt_path) as f:
        raw = json.load(f)
    return {int(k): float(v) for k, v in raw.items()}


def load_proteases(spec_path):
    """
    Load protease specificity + fermentation conditions from JSON.
    Returns (proteases_dict, conditions_dict).
    Expected JSON shape:
      { "proteases": { "<name>": { ...per-protease fields... } },
        "shio_koji_conditions": { "NaCl_pct": 17.5, ... } }
    Each protease entry must include "ph_activity_at_shio_koji" (float 0-1).
    """
    with open(spec_path) as f:
        data = json.load(f)
    return data["proteases"], data["shio_koji_conditions"]


# ---------------------------------------------------------------------------
# Core computation
# ---------------------------------------------------------------------------

def interpolate_salt_inhibition(protease_data, nacl_pct):
    """
    Linear interpolation of residual protease activity between the 10% and 20%
    NaCl reference points stored in protease_data["salt_inhibition"].
    Returns float (fraction of uninhibited activity, 0-1).
    """
    si = protease_data["salt_inhibition"]
    lo_pct, lo_act = 10.0, si["NaCl_10pct_residual_activity"]
    hi_pct, hi_act = 20.0, si["NaCl_20pct_residual_activity"]
    t = max(0.0, min(1.0, (nacl_pct - lo_pct) / (hi_pct - lo_pct)))
    return lo_act + t * (hi_act - lo_act)


def site_plddt(plddt, pos, seq_len, window=3):
    """
    Mean pLDDT of residues within ±window positions of a cleavage site.
    pos is 1-indexed. Returns 0.0 if no scores found in window.
    """
    scores = [
        plddt[i]
        for i in range(max(1, pos - window), min(seq_len, pos + window + 1))
        if i in plddt
    ]
    return sum(scores) / len(scores) if scores else 0.0


def classify_accessibility(mean_plddt,
                            buried_threshold=PLDDT_BURIED,
                            partial_threshold=PLDDT_PARTIAL):
    """Classify a residue window as buried / partially_exposed / exposed."""
    if mean_plddt >= buried_threshold:
        return "buried"
    elif mean_plddt >= partial_threshold:
        return "partially_exposed"
    else:
        return "exposed"


def find_cleavage_sites(seq, protease_data, plddt, nacl_pct, ph_factor=None):
    """
    Scan a protein sequence for P1/P1' recognition sites matching protease_data
    and score each by structural accessibility × effective protease activity.

    ph_factor: fraction of pH-optimal activity at the fermentation pH (0-1).
               If None, reads from protease_data["ph_activity_at_shio_koji"].

    Returns list of site dicts, sorted by risk_score descending.

    Risk score = accessibility_weight × salt_residual_activity × ph_factor
    """
    if ph_factor is None:
        ph_factor = protease_data.get("ph_activity_at_shio_koji", 1.0)

    p1_set  = set(protease_data.get("P1_preferred", []))
    p1p_set = set(protease_data.get("P1_prime_preferred", []))
    salt_activity = interpolate_salt_inhibition(protease_data, nacl_pct)
    effective_activity = salt_activity * ph_factor
    seq_len = len(seq)

    sites = []
    for i in range(seq_len - 1):
        aa_p1  = seq[i]
        aa_p1p = seq[i + 1]
        pos    = i + 1  # 1-indexed

        p1_match  = (not p1_set)  or (aa_p1  in p1_set)
        p1p_match = (not p1p_set) or (aa_p1p in p1p_set)
        if not (p1_match and p1p_match):
            continue

        mean_plddt_val = site_plddt(plddt, pos, seq_len)
        accessibility  = classify_accessibility(mean_plddt_val)
        acc_score      = ACCESSIBILITY_SCORES[accessibility]
        risk_score     = round(acc_score * effective_activity, 3)

        sites.append({
            "position":               pos,
            "P1":                     aa_p1,
            "P1_prime":               aa_p1p,
            "mean_plddt_window":      round(mean_plddt_val, 1),
            "accessibility":          accessibility,
            "salt_residual_activity": round(salt_activity, 3),
            "ph_activity_factor":     round(ph_factor, 3),
            "effective_protease_activity": round(effective_activity, 3),
            "risk_score":             risk_score,
        })

    return sorted(sites, key=lambda x: -x["risk_score"])


def compute_sequence_stats(plddt):
    """
    Summarise per-residue pLDDT distribution.
    Returns dict with length, mean, min, max, % above 80, % above 90.
    """
    vals = list(plddt.values())
    n = len(vals)
    return {
        "length":                 n,
        "mean_plddt":             round(sum(vals) / n, 1),
        "min_plddt":              round(min(vals), 1),
        "max_plddt":              round(max(vals), 1),
        "pct_residues_above_80":  round(100 * sum(1 for v in vals if v >= 80) / n, 1),
        "pct_residues_above_90":  round(100 * sum(1 for v in vals if v >= 90) / n, 1),
    }


def summarize_protease(sites, protease_data, conditions):
    """
    Aggregate per-site results for one protease into a summary dict.
    sites: output of find_cleavage_sites().
    """
    nacl_pct   = conditions["NaCl_pct"]
    ph_factor  = protease_data.get("ph_activity_at_shio_koji", 1.0)
    salt_act   = interpolate_salt_inhibition(protease_data, nacl_pct)
    top5       = sites[:5]

    return {
        "full_name":                         protease_data["full_name"],
        "total_recognition_sites":           len(sites),
        "exposed_sites":                     sum(1 for s in sites if s["accessibility"] == "exposed"),
        "partially_exposed_sites":           sum(1 for s in sites if s["accessibility"] == "partially_exposed"),
        "buried_sites":                      sum(1 for s in sites if s["accessibility"] == "buried"),
        "salt_residual_activity_at_nacl":    round(salt_act, 3),
        "ph_activity_factor":                round(ph_factor, 3),
        "effective_activity":                round(salt_act * ph_factor, 3),
        "max_risk_score":                    round(sites[0]["risk_score"], 3) if sites else 0,
        "mean_risk_score_top5":              round(
            sum(s["risk_score"] for s in top5) / len(top5), 3
        ) if top5 else 0,
        "top_5_sites":                       top5,
    }


def run_all_proteases(seq, plddt, proteases, conditions):
    """
    Run find_cleavage_sites + summarize_protease for every protease in the dict.
    Returns dict keyed by protease name, values are summarize_protease() output.
    ph_factor is read from each protease's "ph_activity_at_shio_koji" field.
    """
    nacl_pct = conditions["NaCl_pct"]
    results  = {}
    for name, pdata in proteases.items():
        sites          = find_cleavage_sites(seq, pdata, plddt, nacl_pct)
        results[name]  = summarize_protease(sites, pdata, conditions)
    return results
