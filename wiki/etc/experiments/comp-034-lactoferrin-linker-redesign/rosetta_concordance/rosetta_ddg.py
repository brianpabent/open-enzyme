#!/usr/bin/env python3
"""
comp-034 Rosetta concordance leg — relaxed-neighborhood ddG + helix retention
for the inter-lobe linker (UniProt P02788, residues 353-363).

Adds the physics-based fold-stability metric that was BLOCKED until PyRosetta
was licensed/installed (2026-05-29). Tests the central mechanistic tension the
other 5 concordance metrics cannot see:
  - proline arms  -> does the helix-breaker destabilize the inter-lobe helix?
  - charge/polar  -> does an all-acidic/polar string destabilize via repulsion?

Protocol (relaxed-neighborhood ddG, monomer fold stability):
  1. FastRelax WT structure restricted to the linker neighborhood (within
     NBR_CUTOFF A of residues 353-363), backbone+sidechain, with coordinate
     constraints to the AF start coords (prevents global drift). Score ref2015.
  2. For each candidate: from the relaxed-WT pose, apply the linker point
     mutations (MutateResidue, no repack), then FastRelax the same neighborhood
     movemap, score. ddG = mut_score - wt_score.
  3. N_TRAJ independent trajectories; report mean +/- sd.
  4. DSSP secondary structure of the 353-363 segment in relaxed WT and each
     mutant -> helix retention (fraction of linker residues still H/G/I).

NOT gold-standard cartesian_ddg. This is a relaxed-neighborhood torsion-space
ddG screen; it is one concordance VOTE, not a sole decider. cartesian_ddg is
the rigorous follow-up for borderline candidates.
"""
import argparse, json, os, shutil, statistics, sys, tempfile, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
PDB = HERE.parent / "proteinmpnn_rerun" / "AF-P02788-F1-model_v6.pdb"


def staged_pdb():
    """Rosetta's file reader mishandles spaces in paths (the repo lives under
    '.../Open Enzyme/...'). Stage a spaceless copy in a temp dir before loading."""
    d = Path(tempfile.gettempdir()) / "comp034_rosetta"
    d.mkdir(parents=True, exist_ok=True)
    dst = d / "af_p02788.pdb"
    shutil.copy(str(PDB), str(dst))
    return str(dst)

LINKER_START, LINKER_END = 353, 363          # UniProt == AF model numbering
WT_LINKER = "SEEEVAARRAR"

CANDIDATES = {
    "WT_SEEEVAARRAR":           "SEEEVAARRAR",   # reference, ddG == 0 by definition
    "V357P_SEEEPAARRAR":        "SEEEPAARRAR",   # conservative proline (3/5)
    "S353E_V357P_EEEEPAARRAR":  "EEEEPAARRAR",   # primary proline (4/5)
    "MPNN_NEEEQQQEEEQ":         "NEEEQQQEEEQ",   # MPNN-native aggressive (5/5)
    "MPNN_NEEEQEEQDQQ":         "NEEEQEEQDQQ",   # MPNN-native sibling (4/5)
    "AGGR_PRO_EEEEPAAPPAP":     "EEEEPAAPPAP",   # multi-proline stress extreme
}

NBR_CUTOFF = 8.0
ONE2THREE = None  # filled after pyrosetta import not needed; MutateResidue takes 1-letter via toolbox


def diffs_for(seq):
    return [(LINKER_START + i, WT_LINKER[i], seq[i]) for i in range(11) if seq[i] != WT_LINKER[i]]


def build_neighborhood_movemap(pose):
    import pyrosetta
    from pyrosetta.rosetta.core.select.residue_selector import (
        ResidueIndexSelector, NeighborhoodResidueSelector)
    idx = ResidueIndexSelector()
    idx.set_index_range(LINKER_START, LINKER_END)
    nbr = NeighborhoodResidueSelector(idx, NBR_CUTOFF, True)  # include focus
    sel = nbr.apply(pose)
    mm = pyrosetta.rosetta.core.kinematics.MoveMap()
    mm.set_bb(False); mm.set_chi(False); mm.set_jump(False)
    n_move = 0
    for i in range(1, pose.total_residue() + 1):
        if sel[i]:
            mm.set_bb(i, True); mm.set_chi(i, True); n_move += 1
    return mm, n_move


def make_relax(scorefxn, movemap, repeats=1):
    """Cartesian-space FastRelax (ref2015_cart) — the Park 2016 / repo-cited
    (protein-engineering-strategy.md §5.2) standard for ddG. Cartesian
    minimization on a smoother landscape is far more reproducible than
    torsion-space relax-and-subtract."""
    import pyrosetta
    fr = pyrosetta.rosetta.protocols.relax.FastRelax(scorefxn, repeats)
    fr.set_movemap(movemap)
    fr.cartesian(True)
    fr.constrain_relax_to_start_coords(True)
    fr.coord_constrain_sidechains(True)
    fr.ramp_down_constraints(False)
    fr.min_type("lbfgs_armijo_nonmonotone")   # cartesian-compatible minimizer
    return fr


def linker_ss(pose):
    import pyrosetta
    # get_dssp_secstruct() returns full DSSP codes (H/G/I/E/B/T/S/L). The
    # dssp_reduced()+pose.secstruct() path silently returned all-L on this build.
    ss = pyrosetta.rosetta.core.scoring.dssp.Dssp(pose).get_dssp_secstruct()
    seg = ss[LINKER_START - 1:LINKER_END]   # residues 353-363
    helix = sum(1 for c in seg if c in "HGI")   # H=alpha, G=3-10, I=pi
    return seg, helix, round(helix / 11.0, 3)


def apply_mutations(pose, seq):
    import pyrosetta
    from pyrosetta.rosetta.protocols.simple_moves import MutateResidue
    aa3 = {"A":"ALA","R":"ARG","N":"ASN","D":"ASP","C":"CYS","E":"GLU","Q":"GLN",
           "G":"GLY","H":"HIS","I":"ILE","L":"LEU","K":"LYS","M":"MET","F":"PHE",
           "P":"PRO","S":"SER","T":"THR","W":"TRP","Y":"TYR","V":"VAL"}
    for resi, wt_aa, mut_aa in diffs_for(seq):
        MutateResidue(resi, aa3[mut_aa]).apply(pose)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ntraj", type=int, default=10)
    ap.add_argument("--repeats", type=int, default=1, help="FastRelax ramp cycles per trajectory")
    ap.add_argument("--validate", action="store_true",
                    help="WT + V357P only, 1 trajectory, for protocol+timing check")
    ap.add_argument("--out", default=str(HERE / "rosetta_ddg_results.json"))
    args = ap.parse_args()

    import pyrosetta
    pyrosetta.init("-mute all -ignore_unrecognized_res true -detect_disulf false "
                   "-ex1 -ex2", silent=True)
    BASE_SEED = 11000   # per-trajectory seed = BASE_SEED + traj index (varied + reproducible)
    try:
        pr_ver = pyrosetta._version_string()
    except Exception:
        pr_ver = "pyrosetta (version accessor unavailable on this build)"
    scorefxn = pyrosetta.create_score_function("ref2015_cart")   # cartesian ddG standard
    # coordinate-constraint term so constrain_relax_to_start_coords is active
    scorefxn.set_weight(pyrosetta.rosetta.core.scoring.coordinate_constraint, 1.0)

    cands = CANDIDATES
    ntraj = args.ntraj
    if args.validate:
        cands = {k: CANDIDATES[k] for k in ("WT_SEEEVAARRAR", "V357P_SEEEPAARRAR")}
        ntraj = 1

    base = pyrosetta.pose_from_pdb(staged_pdb())
    mm, n_move = build_neighborhood_movemap(base)
    print(f"[setup] pose {base.total_residue()} res; neighborhood movable = {n_move} res "
          f"(within {NBR_CUTOFF} A of {LINKER_START}-{LINKER_END})", flush=True)

    results = {}
    t0 = time.time()
    for name, seq in cands.items():
        traj = []   # list of (score, ss_seg, helix_frac)
        for t in range(ntraj):
            pyrosetta.rosetta.numeric.random.rg().set_seed(BASE_SEED + t)
            pose = pyrosetta.Pose(); pose.assign(base)
            if seq != WT_LINKER:
                apply_mutations(pose, seq)
            fr = make_relax(scorefxn, mm, repeats=args.repeats)
            ts = time.time()
            fr.apply(pose)
            sc = float(scorefxn(pose))
            seg, _, frac = linker_ss(pose)
            traj.append((sc, seg, frac))
            print(f"  {name:26s} traj{t+1}/{ntraj}  score={sc:9.2f} REU  "
                  f"helixfrac={frac}  ({time.time()-ts:.1f}s)", flush=True)
        scores = [x[0] for x in traj]
        best = min(traj, key=lambda x: x[0])              # min-energy trajectory = best relax
        best3 = sorted(scores)[:3]
        results[name] = {
            "linker_seq": seq,
            "mutations": ["%s%d%s" % (a, p, b) for p, a, b in diffs_for(seq)],
            "min_score_REU": round(best[0], 2),            # primary estimator
            "mean_best3_REU": round(statistics.mean(best3), 2),
            "mean_REU": round(statistics.mean(scores), 2),
            "sd_REU": round(statistics.pstdev(scores) if len(scores) > 1 else 0.0, 2),
            "all_scores_REU": [round(s, 2) for s in scores],
            "n_traj": ntraj,
            "linker_ss_at_min": best[1],                   # SS of the best-relax structure
            "linker_helix_frac_at_min": best[2],
            "linker_helix_frac_modal": round(statistics.median([x[2] for x in traj]), 3),
        }

    # ddG relative to WT, by min-energy (primary) and mean (secondary)
    wt_min = results["WT_SEEEVAARRAR"]["min_score_REU"]
    wt_mean = results["WT_SEEEVAARRAR"]["mean_REU"]
    for r in results.values():
        r["ddG_min_REU"] = round(r["min_score_REU"] - wt_min, 2)
        r["ddG_mean_REU"] = round(r["mean_REU"] - wt_mean, 2)

    print(f"[done] {time.time()-t0:.1f}s total", flush=True)
    out = {
        "_meta": {
            "experiment": "comp-034 Rosetta concordance leg",
            "method": "relaxed-neighborhood torsion-space ddG (ref2015) + DSSP helix retention",
            "NOT": "gold-standard cartesian_ddg; concordance vote only",
            "pdb": PDB.name, "linker": f"{LINKER_START}-{LINKER_END} {WT_LINKER}",
            "nbr_cutoff_A": NBR_CUTOFF, "ntraj": ntraj, "base_seed": BASE_SEED,
            "pyrosetta": pr_ver,
        },
        "results": results,
    }
    Path(args.out).write_text(json.dumps(out, indent=2))
    print(f"[wrote] {args.out}", flush=True)
    # console summary (ranked by min-energy ddG, the primary estimator)
    print("\n=== ddG summary (REU; +ve = destabilizing vs WT) ===")
    print(f"  {'candidate':26s} {'ddG_min':>8s} {'ddG_mean':>9s} {'sd':>6s} {'helix@min':>9s}  seq")
    for name, r in sorted(results.items(), key=lambda kv: kv[1]["ddG_min_REU"]):
        print(f"  {name:26s} {r['ddG_min_REU']:+8.2f} {r['ddG_mean_REU']:+9.2f} {r['sd_REU']:6.2f} "
              f"{r['linker_helix_frac_at_min']:9.3f}  {r['linker_seq']}")


if __name__ == "__main__":
    main()
