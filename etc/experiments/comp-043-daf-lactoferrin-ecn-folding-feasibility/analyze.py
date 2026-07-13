#!/usr/bin/env python3
"""
comp-043: Does E. coli Nissle 1917 (EcN) periplasmic disulfide-folding (DsbA/DsbC) +
          colonic-luminal protease survival scale from C1-INH (2 disulfides, comp-037)
          to DAF SCR1-4 (8 disulfides) and lactoferrin (16 disulfides)?

Motivation
----------
comp-037 showed EcN's periplasmic DsbA/DsbC machinery can plausibly fold C1-INH (2 disulfides,
serpin). A synthesis card overreached: "so EcN is superior to koji for PDI-heavy payloads like
DAF SCR1-4 (8) and lactoferrin (16)." That leap is UNTESTED. This experiment evaluates the three
payloads head-to-head across three orthogonal axes and finds where — by disulfide count — EcN's
periplasmic folding stops being plausible.

This is NOT a genome-scale metabolic model (GEM). A GEM models metabolic flux, not folding-machinery
competition — it is the wrong tool for this question (that was the card's error). This is a
comp-006/comp-037-style structural + sequence folding-feasibility analysis:
  Axis 1 — disulfide-folding burden vs. DsbA/DsbC oxidative-folding capacity
  Axis 2 — strictly-degradative colonic-luminal protease exposure (AlphaFold pLDDT scan)
  Axis 3 — glycosylation dependence for FUNCTION (EcN cannot glycosylate)

The composite verdict is a LIMITING-FACTOR gate (Liebig's law): folding must succeed first; if the
disulfide-folding axis fails, the protease and glycosylation axes are moot. This mirrors comp-008's
"chemistry can't run" gate for uricase in an obligate anaerobe.

HONESTY CONSTRAINT (load-bearing)
---------------------------------
Per chaperone-orthogonal-stacking.md §8 item 6: NO published DsbA/DsbC capacity metric exists at the
8-16 disulfide scale. The reference-capacity anchor used on Axis 1 is therefore an INFERENCE from
E. coli periplasmic-expression PRECEDENT, not a measurement. It is the single biggest optimistic
assumption in this analysis and is sensitivity-tested across a conservative/moderate/optimistic band.
Every payload verdict that rests on it is labelled PROVISIONAL where the band straddles the decision.

Usage: python3 analyze.py   (from this directory)
Outputs: outputs/results.json, outputs/summary.md

All load-bearing numbers grep-verified against UniProt (see inputs/provenance.md):
  C1-INH      P05155  2 disulfides   (grep -c '^FT   DISULFID' -> 2)
  DAF SCR1-4  P08174  8 disulfides   (all in Sushi 1-4, aa 35-285)
  lactoferrin P02788 16 disulfides   (bilobal transferrin fold)
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))
from protease_stability import (
    load_sequence,
    load_plddt,
    load_proteases,
    compute_sequence_stats,
    find_cleavage_sites,
)

INPUTS = Path(__file__).parent / "inputs"
OUTPUTS = Path(__file__).parent / "outputs"
OUTPUTS.mkdir(exist_ok=True)

import random
random.seed(20260713)

# ---------------------------------------------------------------------------
# Axis 1 parameters — DsbA/DsbC oxidative-folding capacity model
# ---------------------------------------------------------------------------
#
# Per-bond isomerization-difficulty weight as a function of the disulfide loop length
# L = |Cys_i - Cys_j| in sequence.  Rationale:
#   DsbA introduces disulfides vectorially as the chain emerges into the periplasm; SHORT-range
#   bonds (both Cys close in sequence) form correctly with DsbA alone.  LONG-range bonds require the
#   whole intervening chain to be translocated and held before the partner Cys is available, and
#   correcting the mispairings that result is the DsbC-isomerase-limited step.  Very-long-range bonds
#   (the C-lobe-spanning 424-705 / 446-668 / 502-696 bonds of lactoferrin) are the hierarchical
#   folding signature that makes transferrin-fold proteins hard for a periplasmic oxidase system.
#
# These weights are a transparent, monotone proxy — NOT a measured DsbC k_cat.  They convert a raw
# disulfide count into an architecture-aware "effective folding demand."
W_LOCAL = 1.0        # L <= 50   : within a compact module; DsbA-competent
W_MID = 1.5          # 50 < L <= 150 : moderate range; some DsbC isomerization
W_LONGRANGE = 2.5    # L > 150   : C-lobe-spanning; high DsbC isomerization demand
MID_CUTOFF = 50
LONG_CUTOFF = 150
# Per-crossing (interleaved / knotted) DsbC-isomerization surcharge. Loop-length alone captures the
# "held-open until the distal Cys emerges" burden; crossings capture the ORTHOGONAL "mispairing-prone"
# burden that DsbC isomerase exists to correct. DAF's canonical sushi Cys1-Cys3 / Cys2-Cys4 topology
# is 4 interleaved pairs with SHORT loops — invisible to loop-length weighting but real DsbC demand.
# (Peer-review fix 2026-07-13: crossings were computed but not fed into demand, under-counting DAF.)
# NOTE: DsbC is the E. coli periplasmic isomerase; the koji framework's "CCP folds fast" (Schmidt
# 2010) is EUKARYOTIC PDI and does NOT transfer as reassurance for a bacterial oxidase.
W_CROSSING = 0.5

# Reference DsbA/DsbC periplasmic oxidative-folding CAPACITY band (effective-demand units).
# ** THESE ARE PRECEDENT-DERIVED ESTIMATES, NOT MEASURED CAPACITIES (see honesty constraint). **
#   CONSERVATIVE (5.0): certolizumab pegol (Cimzia) Fab' — industrially manufactured by secreted
#       periplasmic expression in ~WT E. coli; ~5 disulfides, mostly local. The demonstrated routine
#       ceiling for a functional secreted disulfide-bonded therapeutic in a near-wild-type periplasm.
#   MODERATE (8.0): Fab-class precedent + credit for DsbC-isomerase co-expression (standard strain
#       engineering that extends the accessible disulfide range without exotic redox rewiring).
#   OPTIMISTIC (12.0): engineered oxidizing strains (SHuffle: trxB/gor + cytoplasmic DsbC). These
#       enable higher-disulfide formats, but full aglycosylated IgG (16 disulfides) remains a
#       low-yield, heavily-engineered achievement — NOT the bar for a plausible LBP payload. 12.0 is
#       deliberately set BELOW 16 to reflect that full-IgG-scale folding is not "routinely viable."
CAPACITY_CONSERVATIVE = 5.0
CAPACITY_MODERATE = 8.0
CAPACITY_OPTIMISTIC = 12.0
CAPACITY_ANCHORS = {
    "conservative": CAPACITY_CONSERVATIVE,
    "moderate": CAPACITY_MODERATE,
    "optimistic": CAPACITY_OPTIMISTIC,
}

# Folding-nonviability mapping from the demand/capacity ratio.
#   ratio <= 0.5 -> 0.0 (folding plausible)
#   ratio  = 1.0 -> 0.5 (folding at the capacity edge)
#   ratio >= 1.5 -> 1.0 (folding-limited)
def folding_nonviability(ratio):
    return max(0.0, min(1.0, (ratio - 0.5) / 1.0))

# ---------------------------------------------------------------------------
# Axis 3 parameters — glycosylation-dependence-for-FUNCTION penalty
# ---------------------------------------------------------------------------
# Categorical, evidence-based. The question is NOT "is the protein glycosylated" (all three are);
# it is "does loss of glycosylation abolish the therapeutic FUNCTION in a gut-luminal format?"
GLYCO_PENALTY = {
    "not_required": 0.0,   # function polypeptide-encoded; glycans irrelevant to luminal activity
    "aids_not_required": 0.3,  # glycans aid protease resistance/stability but core function survives
    "required": 0.8,       # glycosylation mechanistically required for function
}


def load_topology():
    with open(INPUTS / "disulfide_topology.json") as f:
        return json.load(f)["payloads"]


def connectivity_metrics(disulfides):
    """Architecture descriptors from the disulfide connectivity graph."""
    loops = [b - a for (a, b) in disulfides]
    n = len(disulfides)
    long_range = sum(1 for L in loops if L > LONG_CUTOFF)     # C-lobe-spanning class
    mid_range = sum(1 for L in loops if MID_CUTOFF < L <= LONG_CUTOFF)
    local = sum(1 for L in loops if L <= MID_CUTOFF)
    # crossings: pairs (a,b),(c,d) with a<c<b<d  (interleaved / knotted topology)
    crossings = 0
    for i in range(n):
        a, b = disulfides[i]
        for j in range(i + 1, n):
            c, d = disulfides[j]
            lo, hi = (a, b) if a < b else (b, a)
            lo2, hi2 = (c, d) if c < d else (d, c)
            if (lo < lo2 < hi < hi2) or (lo2 < lo < hi2 < hi):
                crossings += 1
    # effective folding demand: architecture-weighted disulfide count
    def w(L):
        if L <= MID_CUTOFF:
            return W_LOCAL
        elif L <= LONG_CUTOFF:
            return W_MID
        return W_LONGRANGE
    loop_demand = sum(w(L) for L in loops)
    crossing_demand = W_CROSSING * crossings
    effective_demand = round(loop_demand + crossing_demand, 2)
    return {
        "disulfide_count": n,
        "loop_lengths": loops,
        "max_loop_length": max(loops) if loops else 0,
        "local_bonds_L_le_50": local,
        "mid_range_bonds_50_150": mid_range,
        "long_range_bonds_gt_150": long_range,
        "topological_crossings": crossings,
        "loop_length_demand": round(loop_demand, 2),
        "crossing_demand": round(crossing_demand, 2),
        "effective_folding_demand": effective_demand,
    }


def folding_axis(conn):
    """Axis 1 — disulfide-folding burden vs. DsbA/DsbC capacity, across the capacity band."""
    demand = conn["effective_folding_demand"]
    per_anchor = {}
    for name, cap in CAPACITY_ANCHORS.items():
        ratio = round(demand / cap, 3)
        per_anchor[name] = {
            "capacity": cap,
            "demand_capacity_ratio": ratio,
            "folding_nonviability": round(folding_nonviability(ratio), 3),
        }
    nv_band = [per_anchor[a]["folding_nonviability"] for a in CAPACITY_ANCHORS]
    nv_lo, nv_hi = min(nv_band), max(nv_band)
    # Verdict on the folding axis alone:
    if nv_hi < 0.35:
        verdict = "FOLDING-PLAUSIBLE"      # plausible across the whole capacity band
    elif nv_lo > 0.75:
        verdict = "FOLDING-LIMITED"        # limited across the whole capacity band
    else:
        verdict = "FOLDING-EDGE"           # straddles the capacity band -> capacity-gated
    return {
        "effective_folding_demand": demand,
        "per_capacity_anchor": per_anchor,
        "folding_nonviability_band": [round(nv_lo, 3), round(nv_hi, 3)],
        "point_estimate_moderate": per_anchor["moderate"]["folding_nonviability"],
        "verdict": verdict,
    }


def protease_axis(seq, plddt, proteases, conditions, core_region, exclude_region=None):
    """Axis 2 — strictly-degradative colonic-luminal protease exposure on the FOLDED core.

    Uses the shared pLDDT-based library. Filters cleavage sites to the folded-core residue window,
    optionally excluding a sub-region (the serpin RCL, which is exposed BY DESIGN and whose cleavage
    is mechanism-overlapping, not strictly degradative)."""
    nacl_pct = conditions["NaCl_pct"]
    lo, hi = core_region
    per_protease = {}
    worst_score = 0.0
    worst_protease = None
    total_exposed = 0
    for name, pdata in proteases.items():
        sites = find_cleavage_sites(seq, pdata, plddt, nacl_pct)
        core = [s for s in sites if lo <= s["position"] <= hi]
        if exclude_region is not None:
            elo, ehi = exclude_region
            core = [s for s in core if not (elo <= s["position"] <= ehi)]
        max_score = core[0]["risk_score"] if core else 0.0
        exposed = sum(1 for s in core if s["accessibility"] == "exposed")
        total_exposed += exposed
        per_protease[name] = {
            "max_risk_score": round(max_score, 3),
            "exposed_sites": exposed,
            "sites_in_core": len(core),
        }
        if max_score > worst_score:
            worst_score = max_score
            worst_protease = name
    if worst_score < 0.15:
        verdict = "LOW"
    elif worst_score < 0.30:
        verdict = "MODERATE"
    elif worst_score < 0.50:
        verdict = "HIGH"
    else:
        verdict = "RED"
    return {
        "max_risk_score": round(worst_score, 3),
        "worst_protease": worst_protease,
        "total_exposed_sites_in_core": total_exposed,
        "per_protease": per_protease,
        "verdict": verdict,
    }


def glyco_axis(payload_key, topo):
    """Axis 3 — glycosylation dependence for FUNCTION."""
    p = topo[payload_key]
    n_sites = len(p["n_glyc_sites"])
    # Evidence-based classification (see disulfide_topology.json n_glyc_note + provenance.md):
    if payload_key == "C1-INH":
        cls = "not_required"
        rationale = (
            "N-glycans drive plasma half-life (Bos 1998 PMID 9799502); the serpin suicide-inhibitor "
            "mechanism (RCL presentation -> acyl-enzyme covalent trap) is polypeptide-encoded. For a "
            "gut-luminal format, plasma half-life is irrelevant. Deglycosylated C1-INH is functionally "
            "inhibitory (Bos 1998)."
        )
    elif payload_key == "DAF_SCR1-4":
        cls = "aids_not_required"
        rationale = (
            "Single N-glycan (N95, SCR1). Decay-accelerating activity is a protein-protein interaction "
            "(SCR2-4 bind C3b/C4b and accelerate convertase decay) — not glycan-dependent. The bulk "
            "glycan liability (O-glycans) is on the truncated stalk. Loss of N95 glycan is unlikely to "
            "abolish function but is not affirmatively demonstrated for an aglycosyl SCR1-4 fragment."
        )
    elif payload_key == "lactoferrin":
        cls = "aids_not_required"
        rationale = (
            "3 N-glycans (N156/N497/N642). Iron sequestration + lactoferricin antimicrobial activity are "
            "polypeptide-encoded; glycans contribute to protease resistance and thermal stability. "
            "Non-native (fungal) glycans are tolerated with native fold (Sun 1999 PMID 10089347, "
            "A. awamori hLf). CRITICAL: glycosylation is NOT the function-killer for lactoferrin in EcN — "
            "the disulfide-FOLDING axis is. In EcN the glycans are entirely absent, removing their "
            "protease-resistance contribution and COMPOUNDING (not causing) the folding problem."
        )
    else:
        cls = "aids_not_required"
        rationale = ""
    return {
        "n_glyc_sites_annotated": n_sites,
        "ecn_can_glycosylate": False,
        "class": cls,
        "penalty": GLYCO_PENALTY[cls],
        "rationale": rationale,
    }


def composite_verdict(fold, prot, glyco):
    """Limiting-factor (Liebig) composite: folding is the gate; if folding plausible, the operative
    secondary axis (protease or glyco) sets the quality of the verdict."""
    axes = {
        "disulfide_folding": fold["point_estimate_moderate"],
        "protease_exposure": prot["max_risk_score"],   # already ~[0,0.5]
        "glyco_dependence": glyco["penalty"],
    }
    limiting_axis = max(axes, key=axes.get)
    # Weighted composite reported for transparency (folding dominant).
    weighted = round(0.6 * fold["point_estimate_moderate"]
                     + 0.25 * min(1.0, prot["max_risk_score"] / 0.5)
                     + 0.15 * glyco["penalty"], 3)

    # Verdict driven by the FOLDING axis band (the gate), refined by secondary axes.
    fv = fold["verdict"]
    if fv == "FOLDING-LIMITED":
        verdict = "NOT-VIABLE"
        driver = "folding-limited across the entire plausible DsbA/DsbC capacity band"
    elif fv == "FOLDING-EDGE":
        verdict = "PROVISIONAL"
        driver = "folding-capacity-gated: viability flips across the (unmeasured) DsbA/DsbC capacity band"
    else:  # FOLDING-PLAUSIBLE
        if prot["verdict"] in ("HIGH", "RED"):
            verdict = "PROVISIONAL"
            driver = f"folding plausible but protease exposure {prot['verdict']}"
        elif glyco["class"] == "required":
            verdict = "NOT-VIABLE"
            driver = "folding plausible but glycosylation mechanistically required and EcN cannot glycosylate"
        else:
            verdict = "VIABLE"
            driver = ("disulfide-axis viable across the capacity band; protease LOW; glyco not "
                      "function-limiting. CAVEAT: Axis 1 scores disulfide formation/isomerization "
                      "burden, NOT native-fold attainment — serpin metastability (recombinant C1-INH "
                      "is made in mammalian/milk systems, not E. coli) is an unmodeled attainment risk")
    return {
        "axes": axes,
        "limiting_axis": limiting_axis,
        "weighted_composite_nonviability": weighted,
        "verdict": verdict,
        "driver": driver,
    }


def main():
    topo = load_topology()
    proteases, conditions = load_proteases(INPUTS / "colonic_ecn_protease_panel.json")

    fasta = {"C1-INH": "P05155", "DAF_SCR1-4": "P08174", "lactoferrin": "P02788"}
    plddt_files = {
        "C1-INH": "alphafold_P05155_plddt.json",
        "DAF_SCR1-4": "alphafold_P08174_plddt.json",
        "lactoferrin": "alphafold_P02788_plddt.json",
    }

    results = {}
    for key in ["C1-INH", "DAF_SCR1-4", "lactoferrin"]:
        p = topo[key]
        seq = load_sequence(INPUTS / f"{fasta[key]}.fasta")
        plddt = load_plddt(INPUTS / plddt_files[key])

        # ---- grep-verify gate: assert every Cys position + expected count ----
        assert len(seq) == p["seq_length"], f"{key}: length {len(seq)} != {p['seq_length']}"
        for (a, b) in p["disulfides"]:
            assert seq[a - 1] == "C" and seq[b - 1] == "C", (
                f"{key}: disulfide C{a}-C{b} verification failed "
                f"(got {seq[a-1]}{a}-{seq[b-1]}{b})"
            )
        expected_counts = {"C1-INH": 2, "DAF_SCR1-4": 8, "lactoferrin": 16}
        assert len(p["disulfides"]) == expected_counts[key], (
            f"{key}: expected {expected_counts[key]} disulfides, got {len(p['disulfides'])}"
        )

        conn = connectivity_metrics(p["disulfides"])
        fold = folding_axis(conn)

        core = p["folded_core_region"]
        exclude = p["rcl_region"]  # None for DAF/LF; RCL for C1-INH
        prot = protease_axis(seq, plddt, proteases, conditions, core, exclude_region=exclude)

        glyco = glyco_axis(key, topo)
        comp = composite_verdict(fold, prot, glyco)

        # Restrict pLDDT stats to the folded-core window for a fair structural comparison.
        core_plddt = {i: v for i, v in plddt.items() if core[0] <= i <= core[1]}

        results[key] = {
            "uniprot": p["uniprot"],
            "full_name": p["full_name"],
            "fold_architecture": p["fold_architecture"],
            "engineering_construct_aa": p["engineering_construct"],
            "engineering_construct_note": p["engineering_construct_note"],
            "structural_stats_folded_core": compute_sequence_stats(core_plddt),
            "connectivity": conn,
            "axis1_disulfide_folding": fold,
            "axis2_protease_exposure": prot,
            "axis3_glyco_dependence": glyco,
            "composite": comp,
        }

    # ---------------------------------------------------------------------
    # Head-to-head ranking + crossover determination
    # ---------------------------------------------------------------------
    order = sorted(
        results,
        key=lambda k: (results[k]["composite"]["axes"]["disulfide_folding"],
                       results[k]["connectivity"]["disulfide_count"]),
    )
    ranking = [
        {
            "payload": k,
            "disulfides": results[k]["connectivity"]["disulfide_count"],
            "effective_folding_demand": results[k]["connectivity"]["effective_folding_demand"],
            "composite_verdict": results[k]["composite"]["verdict"],
        }
        for k in order
    ]

    # Crossover: highest disulfide count that is still VIABLE, and lowest that is NOT-VIABLE.
    viable = [results[k]["connectivity"]["disulfide_count"]
              for k in results if results[k]["composite"]["verdict"] == "VIABLE"]
    provisional = [results[k]["connectivity"]["disulfide_count"]
                   for k in results if results[k]["composite"]["verdict"] == "PROVISIONAL"]
    not_viable = [results[k]["connectivity"]["disulfide_count"]
                  for k in results if results[k]["composite"]["verdict"] == "NOT-VIABLE"]
    crossover = {
        "highest_viable_disulfide_count": max(viable) if viable else None,
        "provisional_disulfide_counts": sorted(provisional),
        "lowest_not_viable_disulfide_count": min(not_viable) if not_viable else None,
        "interpretation": (
            "EcN periplasmic DsbA/DsbC folding is plausible up to ~2 disulfides (C1-INH, VIABLE); "
            "PROVISIONAL / capacity-gated at 8 disulfides (DAF SCR1-4); and NOT plausible at 16 "
            "disulfides (lactoferrin, folding-limited across the entire capacity band). The plausible-"
            "to-not-plausible crossover sits AT DAF SCR1-4 (8 disulfides) and its exact location is "
            "gated by the one unmeasured parameter — the DsbA/DsbC oxidative-folding capacity metric "
            "at 8-16 disulfide scale, which does not exist in the published literature."
        ),
    }

    # Count compounding optimistic assumptions feeding any "viable"-leaning verdict.
    optimistic_assumptions = [
        "Reference DsbA/DsbC capacity band (5/8/12) is precedent-derived, NOT a measured capacity "
        "(no published metric at 8-16 disulfide scale — chaperone-orthogonal-stacking.md §8 item 6).",
        "Axis 1 scores disulfide FORMATION/ISOMERIZATION burden, NOT native-fold ATTAINMENT. Serpin "
        "metastability (C1-INH) and transferrin molten-globule hierarchy (lactoferrin) are additional "
        "unmodeled attainment risks — disulfides are necessary, not sufficient, for a functional fold. "
        "Recombinant C1-INH is manufactured in mammalian/milk systems, not E. coli, for this reason.",
        "The OPTIMISTIC anchor (12.0, SHuffle trxB/gor + cytoplasmic DsbC) describes CYTOPLASMIC "
        "disulfide formation. A cytoplasmically-folded protein does not route through the "
        "Sec→periplasm→outer-membrane luminal-secretion path this LBP format requires — so the "
        "optimistic anchor is compartment-mismatched with the secreted format. The realistic ceiling "
        "for a SECRETED payload is nearer the conservative/moderate anchors, which pushes DAF SCR1-4 "
        "toward the folding-limited end of its band (i.e., DAF's 'viable-only-at-optimistic' read "
        "leans on an anchor that may not apply).",
        "pLDDT is used as a burial proxy for the protease axis (comp-034 showed this under-counts "
        "SASA-exposed helical/linker sites ~10x, e.g. the lactoferrin inter-lobe linker).",
        "Per-bond loop-length weighting (1.0/1.5/2.5) + per-crossing surcharge (0.5) are transparent "
        "monotone proxies for DsbC isomerization demand, not measured k_cat values.",
        "Secretion topology (Sec/YebF/Type I) and its effect on OmpT/DegP exposure is not modeled.",
        "Colonic commensal-microbiome protease load and bile-acid unfolding are out-of-model.",
        "The koji lactoferrin precedent (>2 g/L) is Aspergillus AWAMORI (Ward 1995), a sister species "
        "of A. oryzae koji — genus-level evidence, not koji proper.",
    ]

    output = {
        "experiment": "comp-043",
        "question": (
            "Does EcN periplasmic disulfide-folding (DsbA/DsbC) + colonic-protease survival scale "
            "from C1-INH (2 disulfides, comp-037) to DAF SCR1-4 (8) and lactoferrin (16)?"
        ),
        "chassis": "Engineered E. coli Nissle 1917 (EcN) LBP, luminal-secreted format",
        "environment": "Colonic lumen, pH 6-7, 37C, ~0.15 M NaCl; bile-acid + commensal proteases out-of-model",
        "method_note": (
            "NOT a genome-scale metabolic model (a GEM models flux, not folding-machinery competition). "
            "Structural + sequence folding-feasibility analysis across three orthogonal axes with a "
            "limiting-factor (Liebig) composite."
        ),
        "capacity_anchors": CAPACITY_ANCHORS,
        "capacity_anchor_provenance": {
            "conservative_5.0": "Certolizumab pegol Fab' — secreted periplasmic E. coli manufacture, ~5 disulfides",
            "moderate_8.0": "Fab-class precedent + DsbC-isomerase co-expression credit",
            "optimistic_12.0": "Engineered oxidizing strain (SHuffle trxB/gor + cytoplasmic DsbC); set BELOW full-IgG 16",
            "HONESTY": "No published DsbA/DsbC capacity metric exists at 8-16 disulfide scale. These are "
                       "precedent-derived inferences, NOT measurements. This is the single biggest assumption.",
        },
        "payloads": results,
        "ranking_by_folding_burden": ranking,
        "crossover": crossover,
        "optimistic_assumptions": optimistic_assumptions,
        "card_claim_evaluated": (
            "'EcN is superior to koji for PDI-heavy payloads like DAF SCR1-4 (8 disulfides) and "
            "lactoferrin (16 disulfides).'"
        ),
        "card_claim_verdict": "REFUTED as stated (blanket 'PDI-heavy' claim)",
        "bounded_thesis": (
            "EcN's periplasmic DsbA/DsbC folding plausibly extends to LOW-to-MODERATE disulfide, "
            "COMPACT-fold, glycosylation-independent payloads (C1-INH VIABLE 2 disulfides; DAF SCR1-4 "
            "PROVISIONAL 8 disulfides, CCP/sushi fold). It does NOT plausibly scale to lactoferrin "
            "(16 disulfides, bilobal transferrin fold with C-lobe-spanning long-range bonds). Moreover "
            "koji is NOT dominated: koji (eukaryotic ER + PDI/ERO1 + glycosylation) folds DAF SCR1-4 "
            "at LOW protease risk (comp-012) and has a >2 g/L lactoferrin precedent (Ward 1995, "
            "A. awamori; Sun 1999 native fold). So EcN is a plausible ALTERNATIVE at low/moderate "
            "disulfide scale, not a superior chassis for PDI-heavy payloads — and is inferior to koji "
            "for lactoferrin specifically."
        ),
    }

    with open(OUTPUTS / "results.json", "w") as f:
        json.dump(output, f, indent=2)
    write_summary(output, OUTPUTS / "summary.md")

    print("comp-043 complete. Head-to-head:")
    for r in ranking:
        print(f"  {r['payload']:<12} {r['disulfides']:>2} disulf  "
              f"eff.demand {r['effective_folding_demand']:>5}  -> {r['composite_verdict']}")
    print(f"Crossover: {crossover['highest_viable_disulfide_count']} viable / "
          f"{crossover['provisional_disulfide_counts']} provisional / "
          f"{crossover['lowest_not_viable_disulfide_count']} not-viable (disulfides)")
    print(f"Card claim: {output['card_claim_verdict']}")


def write_summary(d, path):
    R = d["payloads"]
    order = [r["payload"] for r in d["ranking_by_folding_burden"]]
    name_map = {"C1-INH": "C1-INH (serpin, 2 SS)",
                "DAF_SCR1-4": "DAF SCR1-4 (CCP/sushi, 8 SS)",
                "lactoferrin": "Lactoferrin (transferrin-lobe, 16 SS)"}

    lines = [
        "# comp-043 — EcN periplasmic disulfide-folding + colonic-protease scaling: "
        "C1-INH (2) vs DAF SCR1-4 (8) vs lactoferrin (16)",
        "",
        f"**Question:** {d['question']}",
        f"**Chassis:** {d['chassis']}",
        f"**Environment:** {d['environment']}",
        f"**Method:** {d['method_note']}",
        "",
        "> **Honesty constraint (load-bearing):** " + d["capacity_anchor_provenance"]["HONESTY"],
        "",
        "---",
        "",
        "## Head-to-head verdict",
        "",
        "| Payload | Disulfides | Eff. folding demand | Composite verdict | Driver |",
        "|---|---|---|---|---|",
    ]
    for k in order:
        c = R[k]["composite"]
        conn = R[k]["connectivity"]
        lines.append(
            f"| {name_map[k]} | {conn['disulfide_count']} | {conn['effective_folding_demand']} | "
            f"**{c['verdict']}** | {c['driver']} |"
        )
    lines += [
        "",
        f"**Crossover:** {d['crossover']['interpretation']}",
        "",
        "---",
        "",
        "## Axis 1 — Disulfide-folding burden vs. DsbA/DsbC capacity",
        "",
        "Reference capacity band (effective-demand units) — **precedent-derived estimates, not measured:**",
        "",
        f"- conservative {d['capacity_anchors']['conservative']} — {d['capacity_anchor_provenance']['conservative_5.0']}",
        f"- moderate {d['capacity_anchors']['moderate']} — {d['capacity_anchor_provenance']['moderate_8.0']}",
        f"- optimistic {d['capacity_anchors']['optimistic']} — {d['capacity_anchor_provenance']['optimistic_12.0']}",
        "",
        "| Payload | SS count | max loop | long-range (>150) | crossings | eff. demand "
        "(loop+cross) | nonviab @cons/mod/opt | folding verdict |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for k in order:
        conn = R[k]["connectivity"]
        f1 = R[k]["axis1_disulfide_folding"]
        pa = f1["per_capacity_anchor"]
        lines.append(
            f"| {name_map[k]} | {conn['disulfide_count']} | {conn['max_loop_length']} | "
            f"{conn['long_range_bonds_gt_150']} | {conn['topological_crossings']} | "
            f"{conn['effective_folding_demand']} ({conn['loop_length_demand']}+{conn['crossing_demand']}) | "
            f"{pa['conservative']['folding_nonviability']}/{pa['moderate']['folding_nonviability']}/"
            f"{pa['optimistic']['folding_nonviability']} | **{f1['verdict']}** |"
        )
    lines += [
        "",
        "Interpretation: folding-nonviability runs 0 (plausible) -> 1 (folding-limited). C1-INH stays "
        "plausible across the whole band; DAF SCR1-4 STRADDLES it (viable only at optimistic capacity); "
        "lactoferrin is folding-limited even at optimistic capacity (its 3 C-lobe-spanning long-range "
        "bonds — 424-705, 446-668, 502-696 — are the transferrin-fold hierarchical-folding signature "
        "that a periplasmic oxidase is poorly suited to).",
        "",
        "---",
        "",
        "## Axis 2 — Strictly-degradative colonic-luminal protease exposure (folded core)",
        "",
        "| Payload | Folded core (aa) | Max risk | Worst protease | Exposed sites | Verdict |",
        "|---|---|---|---|---|---|",
    ]
    for k in order:
        pr = R[k]["axis2_protease_exposure"]
        core = R[k]["engineering_construct_aa"]
        lines.append(
            f"| {name_map[k]} | {core[0]}-{core[1]} | {pr['max_risk_score']} | "
            f"`{pr['worst_protease']}` | {pr['total_exposed_sites_in_core']} | **{pr['verdict']}** |"
        )
    lines += [
        "",
        "Note: C1-INH excludes the RCL (aa 452-467) — exposed BY DESIGN for the serpin mechanism; its "
        "cleavage is a kinetic-competition question (comp-037), not strictly degradative. Protease "
        "exposure is a SECONDARY axis — moot for lactoferrin, whose folding fails first.",
        "",
        "---",
        "",
        "## Axis 3 — Glycosylation dependence for FUNCTION (EcN cannot glycosylate)",
        "",
        "| Payload | N-glyc sites | Class | Penalty | Kills function in EcN? |",
        "|---|---|---|---|---|",
    ]
    for k in order:
        g = R[k]["axis3_glyco_dependence"]
        kills = "No" if g["class"] != "required" else "Yes"
        lines.append(
            f"| {name_map[k]} | {g['n_glyc_sites_annotated']} | {g['class']} | {g['penalty']} | {kills} |"
        )
    lines += [""]
    for k in order:
        g = R[k]["axis3_glyco_dependence"]
        lines.append(f"- **{name_map[k]}:** {g['rationale']}")
    lines += [
        "",
        "**Key honest finding on Axis 3:** glycosylation-dependence does NOT independently kill DAF or "
        "lactoferrin function in EcN — both retain core polypeptide-encoded function without glycans "
        "(DAF decay-acceleration is protein-protein; lactoferrin iron-binding tolerates non-native "
        "glycans, Sun 1999). The dominant filter is Axis 1 (disulfide folding), not Axis 3. Over-"
        "attributing the lactoferrin problem to glycosylation would be a mechanism error.",
        "",
        "---",
        "",
        "## Card claim evaluated",
        "",
        f"**Claim:** {d['card_claim_evaluated']}",
        "",
        f"**Verdict: {d['card_claim_verdict']}.**",
        "",
        d["bounded_thesis"],
        "",
        "---",
        "",
        "## Compounding optimistic assumptions (verdict is PROVISIONAL where these stack)",
        "",
    ]
    for a in d["optimistic_assumptions"]:
        lines.append(f"- {a}")
    lines += [
        "",
        "Because 3+ optimistic assumptions compound toward any 'viable'-leaning read, the DAF SCR1-4 "
        "verdict is labelled **PROVISIONAL** and the single biggest unresolved question is named "
        "explicitly: the DsbA/DsbC oxidative-folding capacity metric at 8-16 disulfide scale.",
        "",
        "---",
        "",
        "*Generated by `analyze.py`. Uses `experiments/lib/protease_stability.py`. Disulfide counts "
        "grep-verified against UniProt P05155 (2), P08174 (8), P02788 (16). See `inputs/provenance.md`.*",
    ]
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
