#!/usr/bin/env python3
"""
comp-047 — ABCG2 Q141K pharmacological-chaperone re-screen (Axis 1: real docking).

REPLACES comp-032's descriptor/class-prior heuristic with actual AutoDock Vina
docking against a prepared ABCG2 receptor, at TWO grid boxes:

  - fold_site  (NBD region around residue 141)  -> where a chaperone could bind
  - transport  (Walker A P-loop / ATP site)      -> binding here flags an
                                                    ATP-competitive inhibitor
                                                    (disqualifying)

Each ligand is docked to:
  1. fold_site   on Q141K receptor  -> fold_q141k_affinity
  2. fold_site   on WT   receptor   -> fold_wt_affinity   (WT/mutant selectivity proxy)
  3. transport   on WT   receptor   -> transport_affinity (ATP-site avoidance check)

Affinities are Vina's best-mode score in kcal/mol (more negative = stronger).

Chaperone-likeness is expressed with TRANSPARENT metrics over REAL docking
numbers — NOT a drug-class prior. See classify() for the exact rule. Axis 2
(empirical ChEMBL known-ABCG2 activity) is layered on separately (chembl_axis2.py)
and merged in build_results.py; the known-inhibitor role_tag from the curated
control set is also carried through.

Determinism: fixed Vina --seed and --cpu, fixed RDKit embed seed. Exact scores
depend on (seed, cpu, exhaustiveness) — all pinned and printed in the repro command.

Usage:
  analyze.py --subset 6      # validation subset (controls + a few)
  analyze.py                 # full 135-molecule run
"""
import argparse, json, os, shutil, subprocess, sys, time, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
VINA = os.environ.get("OE_VINA_BIN") or shutil.which("vina")
OBABEL = os.environ.get("OE_OBABEL_BIN") or shutil.which("obabel")

REC_WT = HERE / "work/receptor/abcg2_wt.pdbqt"
REC_Q141K = HERE / "work/receptor/abcg2_q141k.pdbqt"
LIGDIR = HERE / "work/ligands"
DOCKDIR = HERE / "work/docking"
LOG = HERE / "logs/run.log"

SEED = 20260714
EXHAUSTIVENESS = 8
CPU = 4

from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import RDLogger
RDLogger.DisableLog("rdApp.*")
from meeko import MoleculePreparation, PDBQTWriterLegacy


def require_toolchain():
    missing = []
    if not VINA or not Path(VINA).is_file():
        missing.append("AutoDock Vina (`OE_VINA_BIN` or `vina` on PATH)")
    if not OBABEL or not Path(OBABEL).is_file():
        missing.append("Open Babel (`OE_OBABEL_BIN` or `obabel` on PATH)")
    if missing:
        raise SystemExit("missing required executable(s): " + "; ".join(missing))


def log(msg):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    with open(LOG, "a") as f:
        f.write(line + "\n")


def strip_counterion(mol):
    """Return the largest organic fragment (by heavy-atom count). Salts like
    sodium butyrate (CCCC(=O)[O-].[Na+]) produce disconnected PDBQT that Vina
    rejects; docking the parent anion is the correct behavior."""
    frags = Chem.GetMolFrags(mol, asMols=True, sanitizeFrags=True)
    if len(frags) <= 1:
        return mol
    return max(frags, key=lambda m: m.GetNumHeavyAtoms())


def protonate_smiles(smiles):
    """Deterministic pH 7.4 protonation via Open Babel; returns SMILES or None."""
    try:
        p = subprocess.run([OBABEL, f"-:{smiles}", "-osmi", "-p", "7.4"],
                           capture_output=True, text=True, timeout=60)
        out = p.stdout.strip().split("\t")[0].strip()
        return out or None
    except Exception:
        return None


def prep_ligand(name, smiles):
    """SMILES -> protonated 3D -> PDBQT. Returns path or None."""
    out = LIGDIR / f"{name}.pdbqt"
    if out.exists() and out.stat().st_size > 0:
        return out
    prot = protonate_smiles(smiles) or smiles
    mol = Chem.MolFromSmiles(prot)
    if mol is None:
        mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    mol = strip_counterion(mol)  # keep largest organic fragment (salts break Vina)
    if mol is None:
        return None
    mol = Chem.AddHs(mol)
    params = AllChem.ETKDGv3()
    params.randomSeed = 42
    if AllChem.EmbedMolecule(mol, params) != 0:
        # retry with random coords for stubborn macrocycles
        params.useRandomCoords = True
        if AllChem.EmbedMolecule(mol, params) != 0:
            return _obabel_gen3d(name, prot)
    try:
        AllChem.MMFFOptimizeMolecule(mol, maxIters=500)
    except Exception:
        pass
    try:
        setups = MoleculePreparation().prepare(mol)
        pdbqt, ok, err = PDBQTWriterLegacy.write_string(setups[0])
        if not ok:
            return _obabel_gen3d(name, prot)
        out.write_text(pdbqt)
        return out
    except Exception:
        return _obabel_gen3d(name, prot)


def _obabel_gen3d(name, smiles):
    """Fallback ligand prep: obabel gen3d directly to PDBQT."""
    out = LIGDIR / f"{name}.pdbqt"
    try:
        p = subprocess.run([OBABEL, f"-:{smiles}", "-O", str(out), "--gen3d", "-p", "7.4"],
                           capture_output=True, text=True, timeout=180)
        if out.exists() and out.stat().st_size > 0:
            return out
    except Exception:
        pass
    return None


def dock(ligand, receptor, box, tag):
    """Run Vina, return best-mode affinity (kcal/mol) or None."""
    outpdbqt = DOCKDIR / f"{ligand.stem}__{tag}.pdbqt"
    cx, cy, cz = box["center"]
    sx, sy, sz = box["size"]
    cmd = [VINA, "--receptor", str(receptor), "--ligand", str(ligand),
           "--center_x", str(cx), "--center_y", str(cy), "--center_z", str(cz),
           "--size_x", str(sx), "--size_y", str(sy), "--size_z", str(sz),
           "--exhaustiveness", str(EXHAUSTIVENESS), "--seed", str(SEED),
           "--cpu", str(CPU), "--out", str(outpdbqt)]
    try:
        subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        if not outpdbqt.exists():
            return None
        for line in outpdbqt.read_text().splitlines():
            if line.startswith("REMARK VINA RESULT:"):
                return float(line.split()[3])
    except Exception:
        return None
    return None


def classify(fold_q141k, fold_wt, transport, known_inhibitor):
    """
    Transparent tier logic over REAL Vina numbers (no class prior).

    Disqualifiers (chaperone_candidate = 'no'):
      - known_inhibitor (curated/empirical ABCG2 activity) -> would block urate efflux
      - strong ATP-site binding AND not fold-selective (transport <= -7.0 and margin < 1.0)

    Non-disqualified:
      - 'yes'       : fold_q141k <= -7.0 AND margin >= 1.5
      - 'uncertain' : fold_q141k <= -6.0 AND margin >= 0.5
      - 'no'        : otherwise (weak binder or fold-indiscriminate)
    where margin = transport - fold_q141k  (>0 means fold-site preferred).
    """
    if fold_q141k is None or transport is None:
        return "error", None, {}
    margin = transport - fold_q141k
    sel = (fold_wt - fold_q141k) if fold_wt is not None else None  # >0 prefers mutant
    reasons = []
    if known_inhibitor:
        reasons.append("known/empirical ABCG2 inhibitor or substrate")
        tier = "no"
    elif transport <= -7.0 and margin < 1.0:
        reasons.append(f"strong ATP-site binding (transport={transport}) without fold-selectivity (margin={margin:.2f})")
        tier = "no"
    elif fold_q141k <= -7.0 and margin >= 1.5:
        tier = "yes"
    elif fold_q141k <= -6.0 and margin >= 0.5:
        tier = "uncertain"
    else:
        tier = "no"
        reasons.append(f"weak/indiscriminate (fold={fold_q141k}, margin={margin:.2f})")
    metrics = {"fold_vs_transport_margin": round(margin, 3),
               "q141k_vs_wt_selectivity": (round(sel, 3) if sel is not None else None),
               "disqualify_reasons": reasons}
    return tier, margin, metrics


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--subset", type=int, default=0,
                    help="dock only first N molecules (controls always included)")
    args = ap.parse_args()
    require_toolchain()
    LIGDIR.mkdir(parents=True, exist_ok=True)
    DOCKDIR.mkdir(parents=True, exist_ok=True)
    LOG.parent.mkdir(parents=True, exist_ok=True)
    (HERE / "outputs").mkdir(parents=True, exist_ok=True)

    boxes = json.load(open(HERE / "work/receptor/boxes.json"))
    fold_box = boxes["fold_site"]
    trans_box = boxes["transport_site"]
    smi = json.load(open(HERE / "work/ligands/smiles_resolved.json"))
    lib = {m["name"]: m for m in json.load(open(HERE / "inputs/fda_approved_drug_library.json"))["molecules"]}

    names = list(smi.keys())
    if args.subset:
        controls = [n for n in names if smi[n]["role_tag"] in ("cftr_corrector", "abcg2_inhibitor")]
        head = [n for n in names if n not in controls][:args.subset]
        # keep a compact validation set: a few controls + a few others
        names = (controls[:4] + head)
        log(f"SUBSET mode: {len(names)} molecules -> {names}")

    # RESUME: reuse completed ligands from a prior partial run (salvage 2026-07-14)
    partial_path = HERE / "outputs/_results_partial.json"
    results = json.load(open(partial_path)) if partial_path.exists() else {}
    done_ok = {n for n, r in results.items()
               if isinstance(r, dict) and r.get("chaperone_tier") not in (None, "error")}
    log(f"RESUME: {len(done_ok)} ligands already complete; {len([n for n in names if n not in done_ok])} to dock")
    t0 = time.time()
    for i, name in enumerate(names, 1):
        if name in done_ok:
            continue
        rec = smi[name]
        if not rec["smiles"]:
            results[name] = {"error": "no smiles"}
            continue
        lig = prep_ligand(name, rec["smiles"])
        if lig is None:
            log(f"[{i}/{len(names)}] {name}: LIGAND PREP FAILED")
            results[name] = {"error": "ligand prep failed", "role_tag": rec["role_tag"]}
            continue
        fq = dock(lig, REC_Q141K, fold_box, "fold_q141k")
        fw = dock(lig, REC_WT, fold_box, "fold_wt")
        tr = dock(lig, REC_WT, trans_box, "transport")
        known_inh = (rec["role_tag"] == "abcg2_inhibitor")
        tier, margin, metrics = classify(fq, fw, tr, known_inh)
        results[name] = {
            "role_tag": rec["role_tag"],
            "drug_class": lib.get(name, {}).get("drug_class", "n/a"),
            "cid": rec.get("cid"),
            "fold_q141k_affinity": fq,
            "fold_wt_affinity": fw,
            "transport_affinity": tr,
            "chaperone_tier": tier,
            **metrics,
            "known_inhibitor_flag": known_inh,
        }
        elapsed = time.time() - t0
        eta = elapsed / i * (len(names) - i)
        log(f"[{i}/{len(names)}] {name:28s} fold_q141k={fq} fold_wt={fw} transport={tr} tier={tier}  (ETA {eta/60:.1f}m)")
        # incremental save
        json.dump(results, open(HERE / "outputs/_results_partial.json", "w"), indent=2)

    meta = {"seed": SEED, "exhaustiveness": EXHAUSTIVENESS, "cpu": CPU,
            "fold_box": fold_box, "transport_box": trans_box,
            "n_molecules": len(results),
            "subset": args.subset,
            "generated": time.strftime("%Y-%m-%d %H:%M:%S")}
    out = {"_meta": meta, "results": results}
    fn = "results_subset.json" if args.subset else "results.json"
    json.dump(out, open(HERE / "outputs" / fn, "w"), indent=2)
    log(f"DONE. wrote outputs/{fn} ({len(results)} molecules) in {(time.time()-t0)/60:.1f} min")


if __name__ == "__main__":
    main()
