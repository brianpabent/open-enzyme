#!/usr/bin/env python3
"""
comp-047 sensitivity analysis (mandatory — comp-032 had none).

For the top fold-site candidates + controls, re-dock the fold_site@Q141K under
perturbations and report rank/affinity stability:
  - grid-box CENTER shifts (+/-2 A along each axis, one +3 A diagonal)
  - grid-box SIZE (18, 26 A vs base 22)
  - Vina SEED (two alternate seeds)
  - ligand PROTONATION (neutral as-drawn SMILES vs base pH 7.4)

A candidate whose fold-site affinity and relative rank survive these
perturbations is a robust finding; one that only ranks under one grid choice
is not (design requirement).

Usage: sensitivity.py            # uses outputs/results.json, top 8 + controls
"""
import json, subprocess, time
from pathlib import Path
from statistics import pstdev, mean

HERE = Path("wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen")
VBIN = Path("/private/tmp/claude-501/-Users-brianabent-Documents-Claude-Projects-abent-Open-Enzyme/f6201cb6-d810-4925-b759-1443e5b758de/scratchpad/docking-smoketest/.venv/bin")
VINA = "/private/tmp/claude-501/-Users-brianabent-Documents-Claude-Projects-abent-Open-Enzyme/f6201cb6-d810-4925-b759-1443e5b758de/scratchpad/docking-smoketest/vina"
OBABEL = str(VBIN / "obabel")
REC_Q141K = HERE / "work/receptor/abcg2_q141k.pdbqt"
SDIR = HERE / "work/sensitivity"
SDIR.mkdir(exist_ok=True)

from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import RDLogger
RDLogger.DisableLog("rdApp.*")
from meeko import MoleculePreparation, PDBQTWriterLegacy

EXH = 8
CPU = 4


def prep_variant(name, smiles, protonate):
    out = SDIR / f"{name}__{'prot' if protonate else 'neutral'}.pdbqt"
    if out.exists() and out.stat().st_size > 0:
        return out
    smi = smiles
    if protonate:
        try:
            p = subprocess.run([OBABEL, f"-:{smiles}", "-osmi", "-p", "7.4"],
                               capture_output=True, text=True, timeout=60)
            smi = p.stdout.strip().split("\t")[0].strip() or smiles
        except Exception:
            pass
    mol = Chem.MolFromSmiles(smi)
    if mol is None:
        return None
    mol = Chem.AddHs(mol)
    params = AllChem.ETKDGv3(); params.randomSeed = 42
    if AllChem.EmbedMolecule(mol, params) != 0:
        params.useRandomCoords = True
        if AllChem.EmbedMolecule(mol, params) != 0:
            return None
    try:
        AllChem.MMFFOptimizeMolecule(mol, maxIters=500)
    except Exception:
        pass
    try:
        pdbqt, ok, err = PDBQTWriterLegacy.write_string(MoleculePreparation().prepare(mol)[0])
        if not ok:
            return None
        out.write_text(pdbqt)
        return out
    except Exception:
        return None


def dock(ligand, center, size, seed, tag):
    outp = SDIR / f"{ligand.stem}__{tag}.pdbqt"
    cmd = [VINA, "--receptor", str(REC_Q141K), "--ligand", str(ligand),
           "--center_x", str(center[0]), "--center_y", str(center[1]), "--center_z", str(center[2]),
           "--size_x", str(size[0]), "--size_y", str(size[1]), "--size_z", str(size[2]),
           "--exhaustiveness", str(EXH), "--seed", str(seed), "--cpu", str(CPU), "--out", str(outp)]
    try:
        subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        for line in outp.read_text().splitlines():
            if line.startswith("REMARK VINA RESULT:"):
                return float(line.split()[3])
    except Exception:
        return None
    return None


def main():
    res = json.load(open(HERE / "outputs/results.json"))
    boxes = json.load(open(HERE / "work/receptor/boxes.json"))
    smi = json.load(open(HERE / "work/ligands/smiles_resolved.json"))
    c0 = boxes["fold_site"]["center"]
    base_size = boxes["fold_site"]["size"]

    results = res["results"]
    # rank candidates by fold_q141k affinity (most negative first), exclude errors
    ranked = sorted(
        [(n, r) for n, r in results.items()
         if isinstance(r.get("fold_q141k_affinity"), (int, float))],
        key=lambda kv: kv[1]["fold_q141k_affinity"])
    top = [n for n, r in ranked if r["role_tag"] == "other"][:8]
    controls = [n for n, r in results.items()
                if r.get("role_tag") in ("cftr_corrector", "abcg2_inhibitor")
                and isinstance(r.get("fold_q141k_affinity"), (int, float))]
    # keep controls set compact: 4 CFTR + 4 inhibitors
    cftr = [n for n in controls if results[n]["role_tag"] == "cftr_corrector"][:4]
    inh = [n for n in controls if results[n]["role_tag"] == "abcg2_inhibitor"][:4]
    targets = top + cftr + inh

    perturbations = [
        ("base",        c0,                          base_size,        20260714, True),
        ("cx+2",        [c0[0]+2, c0[1], c0[2]],     base_size,        20260714, True),
        ("cx-2",        [c0[0]-2, c0[1], c0[2]],     base_size,        20260714, True),
        ("cy+2",        [c0[0], c0[1]+2, c0[2]],     base_size,        20260714, True),
        ("diag+3",      [c0[0]+3, c0[1]+3, c0[2]+3], base_size,        20260714, True),
        ("size18",      c0,                          [18,18,18],       20260714, True),
        ("size26",      c0,                          [26,26,26],       20260714, True),
        ("seed12345",   c0,                          base_size,        12345,    True),
        ("seed99999",   c0,                          base_size,        99999,    True),
        ("neutral_pH",  c0,                          base_size,        20260714, False),
    ]

    out = {"_meta": {"perturbations": [p[0] for p in perturbations],
                     "base_center": c0, "base_size": base_size,
                     "targets": targets},
           "per_molecule": {}}
    t0 = time.time()
    for name in targets:
        rec = smi[name]
        row = {}
        for tag, center, size, seed, protonate in perturbations:
            lig = prep_variant(name, rec["smiles"], protonate)
            if lig is None:
                row[tag] = None
                continue
            aff = dock(lig, center, size, seed, tag)
            row[tag] = aff
        vals = [v for v in row.values() if isinstance(v, (int, float))]
        row["_stats"] = {
            "mean": round(mean(vals), 3) if vals else None,
            "std": round(pstdev(vals), 3) if len(vals) > 1 else None,
            "min": round(min(vals), 3) if vals else None,
            "max": round(max(vals), 3) if vals else None,
            "range": round(max(vals) - min(vals), 3) if vals else None,
        }
        out["per_molecule"][name] = row
        print(f"[{time.time()-t0:5.0f}s] {name:26s} base={row.get('base')} "
              f"mean={row['_stats']['mean']} std={row['_stats']['std']} range={row['_stats']['range']}", flush=True)

    # rank-stability across perturbations (Spearman-ish: how does ordering of
    # candidates shift per perturbation vs base?)
    cand = top
    def order(tag):
        pairs = [(n, out["per_molecule"][n].get(tag)) for n in cand
                 if isinstance(out["per_molecule"][n].get(tag), (int, float))]
        return [n for n, _ in sorted(pairs, key=lambda kv: kv[1])]
    base_order = order("base")
    rank_shift = {}
    for tag, *_ in perturbations:
        if tag == "base":
            continue
        o = order(tag)
        # count position changes in top-8 candidate ordering
        shifts = sum(1 for i, n in enumerate(o) if n in base_order and base_order.index(n) != i)
        rank_shift[tag] = {"order": o, "positions_changed": shifts}
    out["rank_stability"] = {"base_candidate_order": base_order, "per_perturbation": rank_shift}

    json.dump(out, open(HERE / "outputs/sensitivity.json", "w"), indent=2)
    print(f"\nDONE sensitivity in {(time.time()-t0)/60:.1f} min -> outputs/sensitivity.json")


if __name__ == "__main__":
    main()
