#!/usr/bin/env python3
"""
Method #3 (host-tractable form): real mutant structures via Rosetta relax.

ESMFold/AF2 as an orthogonal ML predictor is blocked on this host (openfold +
deepspeed not installed; a hard Apple-Silicon/CPU build). Instead of an
independent predictor, this produces a genuine *relaxed mutant structure* for
each candidate (thread mutations -> cartesian relax -> keep min-energy pose ->
dump PDB) and recomputes per-residue SASA + secondary structure on each
mutant's OWN structure.

This removes the two approximations in structure_gated_cleavage.py:
  - mutant SASA was taken from the WT backbone -> now real per-mutant SASA
  - conformation gate used a uniform helix-fraction -> now real per-residue SS

PyRosetta is single-threaded, so this runs alongside the main cartesian ddG
job without meaningful contention on a multi-core host.
"""
import json, sys, statistics, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import rosetta_ddg as R                      # reuse relax/movemap/mutation/staging
EXP = HERE.parent
sys.path.insert(0, str(EXP.parent / "lib"))

FASTA = EXP / "inputs" / "P02788.fasta"
PLDDT_JSON = EXP / "inputs" / "alphafold_P02788_plddt.json"
SPECS = (EXP.parent / "comp-005-lactoferrin-shio-koji-protease-stability"
         / "inputs" / "protease_specificities.json")
POSE_DIR = HERE / "relaxed_mutant_poses"; POSE_DIR.mkdir(exist_ok=True)

LS, LE, WT = R.LINKER_START, R.LINKER_END, R.WT_LINKER
MAXASA = {"A":129,"R":274,"N":195,"D":193,"C":167,"E":223,"Q":225,"G":104,
          "H":224,"I":197,"L":201,"K":236,"M":224,"F":240,"P":159,"S":155,
          "T":172,"W":285,"Y":263,"V":174}
SS_CONF = {"H":0.2,"G":0.2,"I":0.2,"E":0.7,"B":0.7,"T":1.0,"S":1.0,"L":1.0," ":1.0,"-":1.0}

def acc_weight(rsasa):
    return 0.1 if rsasa < 0.05 else (0.4 if rsasa < 0.25 else 1.0)

def main():
    import pyrosetta
    from protease_stability import load_sequence, load_plddt, load_proteases, find_cleavage_sites
    pyrosetta.init("-mute all -ignore_unrecognized_res true -detect_disulf false -ex1 -ex2", silent=True)
    sfxn = pyrosetta.create_score_function("ref2015_cart")
    sfxn.set_weight(pyrosetta.rosetta.core.scoring.coordinate_constraint, 1.0)

    base = pyrosetta.pose_from_pdb(R.staged_pdb())
    mm, _ = R.build_neighborhood_movemap(base)
    full = load_sequence(FASTA)
    plddt = load_plddt(PLDDT_JSON)
    proteases, conditions = load_proteases(SPECS)
    nacl = conditions["NaCl_pct"]
    NTRAJ = 3

    per_mutant = {}
    for name, seq in R.CANDIDATES.items():
        best = None
        for t in range(NTRAJ):
            pyrosetta.rosetta.numeric.random.rg().set_seed(11000 + t)
            pose = pyrosetta.Pose(); pose.assign(base)
            if seq != WT:
                R.apply_mutations(pose, seq)
            R.make_relax(sfxn, mm, repeats=1).apply(pose)
            sc = float(sfxn(pose))
            if best is None or sc < best[0]:
                best = (sc, pyrosetta.Pose()); best[1].assign(pose)
            print(f"  {name:26s} traj{t+1}/{NTRAJ} score={sc:9.2f}", flush=True)
        score, pose = best
        pose.dump_pdb(str(POSE_DIR / f"{name}.pdb"))

        # real per-residue SASA + SS on THIS mutant's relaxed structure
        sc_ = pyrosetta.rosetta.core.scoring.sasa.SasaCalc(); sc_.calculate(pose)
        rsd_sasa = sc_.get_residue_sasa()
        ss = pyrosetta.rosetta.core.scoring.dssp.Dssp(pose).get_dssp_secstruct()
        per_res = {}
        for r in range(LS, LE+1):
            aa = pose.residue(r).name1()
            rsasa = rsd_sasa[r] / MAXASA[aa]
            per_res[r] = {"aa": aa, "rsasa": round(rsasa, 3), "acc": acc_weight(rsasa),
                          "ss": ss[r-1], "conf": SS_CONF.get(ss[r-1], 1.0)}
        helix_frac = round(sum(1 for r in range(LS, LE+1) if ss[r-1] in "HGI")/11.0, 3)

        # structure-gated cleavage using REAL per-residue mutant SASA + SS
        mseq = full[:LS-1] + seq + full[LE:]
        struct = 0.0
        for pdata in proteases.values():
            for s in find_cleavage_sites(mseq, pdata, plddt, nacl):
                pos = s["position"]
                if LS <= pos <= LE:
                    raw = s["effective_protease_activity"]
                    struct += raw * per_res[pos]["acc"] * per_res[pos]["conf"]
        per_mutant[name] = {"linker_seq": seq, "min_score_REU": round(score, 2),
                            "helix_frac_real": helix_frac,
                            "cleavage_structure_gated_realstruct": round(struct, 3),
                            "per_residue": per_res}
        print(f"  -> {name:26s} helix={helix_frac}  structGated(real)={round(struct,3)}", flush=True)

    (HERE / "refold_via_relax_results.json").write_text(json.dumps(per_mutant, indent=2))
    print("\n=== structure-gated cleavage on REAL relaxed mutant structures ===")
    print(f"{'candidate':26s} {'helix_real':>10} {'structGated_real':>17}")
    for n, r in sorted(per_mutant.items(), key=lambda kv: kv[1]["cleavage_structure_gated_realstruct"]):
        print(f"{n:26s} {r['helix_frac_real']:10.3f} {r['cleavage_structure_gated_realstruct']:17.3f}")
    print("\n[wrote] refold_via_relax_results.json  + relaxed_mutant_poses/*.pdb")

if __name__ == "__main__":
    main()
