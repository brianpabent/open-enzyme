#!/usr/bin/env python3
"""
comp-047 receptor prep + Q141K mutation + grid-box definition.

Produces:
  work/receptor/abcg2_wt_clean.pdb      -- cleaned WT (chain A, standard residues)
  work/receptor/abcg2_q141k_clean.pdb   -- Q141K static side-chain substitution
  work/receptor/boxes.json              -- fold-site & transport-site grid boxes

Q141K modeling is a STATIC side-chain substitution:
  backbone (N,CA,C,O) + CB + CG + CD retained from the GLN141 rotamer;
  OE1/NE2 dropped; CE + NZ built in extended (all-trans) geometry with
  idealized bond lengths (CD-CE 1.52 A, CE-NZ 1.49 A). No backbone relaxation,
  no rotamer optimization, no folding-energy minimization. This is a
  static-structure proxy for the mutant local environment, NOT a folding-ddG
  calculation. It is this experiment's acknowledged weakest link (see README).
"""
import json, sys
import numpy as np
from Bio.PDB import PDBParser, PDBIO, Select

HERE = "wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen"
PDB_IN = f"{HERE}/inputs/alphafold_Q9UNQ0_model_v6.pdb"
REC = f"{HERE}/work/receptor"

STD_AA = {
    "ALA","ARG","ASN","ASP","CYS","GLN","GLU","GLY","HIS","ILE","LEU","LYS",
    "MET","PHE","PRO","SER","THR","TRP","TYR","VAL",
}

def unit(v):
    n = np.linalg.norm(v)
    return v / n if n > 0 else v

def load():
    p = PDBParser(QUIET=True)
    return p.get_structure("abcg2", PDB_IN)

class ProteinSelect(Select):
    def accept_residue(self, r):
        return r.id[0] == " " and r.resname in STD_AA
    def accept_atom(self, a):
        # drop any hydrogens / altloc B
        if a.element == "H":
            return False
        if a.altloc not in (" ", "", "A"):
            return False
        return True

def write_clean_wt():
    s = load()
    io = PDBIO()
    io.set_structure(s)
    out = f"{REC}/abcg2_wt_clean.pdb"
    io.save(out, ProteinSelect())
    return out

def build_q141k():
    """Return a modified structure with GLN141 -> LYS static substitution."""
    s = load()
    chain = list(s[0].get_chains())[0]
    r141 = None
    for r in chain:
        if r.id[1] == 141 and r.id[0] == " ":
            r141 = r
            break
    assert r141 is not None and r141.resname == "GLN", f"expected GLN141, got {r141.resname if r141 else None}"

    CB = r141["CB"].coord.astype(float)
    CG = r141["CG"].coord.astype(float)
    CD = r141["CD"].coord.astype(float)

    # Build CE extending from CG->CD direction (all-trans), 1.52 A
    d_cg_cd = unit(CD - CG)
    CE = CD + d_cg_cd * 1.52
    # Build NZ extending from CD->CE direction, 1.49 A
    d_cd_ce = unit(CE - CD)
    NZ = CE + d_cd_ce * 1.49

    # Mutate: rename residue, drop OE1/NE2, add CE/NZ
    r141.resname = "LYS"
    for atn in ("OE1", "NE2"):
        if atn in r141:
            r141.detach_child(atn)
    from Bio.PDB.Atom import Atom
    # element, fullname formatting
    ce_atom = Atom("CE", CE, 30.0, 1.0, " ", " CE ", 9990, element="C")
    nz_atom = Atom("NZ", NZ, 30.0, 1.0, " ", " NZ ", 9991, element="N")
    r141.add(ce_atom)
    r141.add(nz_atom)

    io = PDBIO()
    io.set_structure(s)
    out = f"{REC}/abcg2_q141k_clean.pdb"
    io.save(out, ProteinSelect())
    # report
    print(f"  Q141K built: CE={np.round(CE,2)} NZ={np.round(NZ,2)}")
    print(f"  NZ is {np.linalg.norm(NZ-r141['CA'].coord):.2f} A from CA141")
    return out

def define_boxes():
    s = load()
    chain = list(s[0].get_chains())[0]
    res = {r.id[1]: r for r in chain if r.id[0] == " "}

    def centroid(nums, sidechain_only=False):
        pts = []
        for n in nums:
            if n not in res:
                continue
            for a in res[n]:
                if a.element == "H":
                    continue
                if sidechain_only and a.name in ("N", "CA", "C", "O"):
                    continue
                pts.append(a.coord.astype(float))
        return np.array(pts)

    # Fold-site: local NBD environment around residue 141.
    # Center on the centroid of the 141 side chain + first-shell contact
    # residues (135-146) to sit in the local groove, not on the CA.
    fold_pts = centroid([141], sidechain_only=True)
    shell_pts = centroid(list(range(137, 146)))
    fold_center = np.vstack([fold_pts, shell_pts]).mean(axis=0)

    # Transport / ATP pocket: Walker A P-loop (80-87). Canonical nucleotide
    # phosphate-binding site. (In this apo monomer the composite dimer ATP
    # site is not formed; Walker A is the most defensible single anchor.)
    walkerA_pts = centroid(list(range(80, 88)))
    atp_center = walkerA_pts.mean(axis=0)

    r141ca = res[141]["CA"].coord.astype(float)
    sep = float(np.linalg.norm(fold_center - atp_center))

    boxes = {
        "fold_site": {
            "center": [round(float(x), 3) for x in fold_center],
            "size": [22.0, 22.0, 22.0],
            "anchor": "residue 141 side chain + contact shell 137-145",
            "rationale": "candidate fold-stabilizing NBD site around Q141/K141",
        },
        "transport_site": {
            "center": [round(float(x), 3) for x in atp_center],
            "size": [22.0, 22.0, 22.0],
            "anchor": "Walker A P-loop residues 80-87",
            "rationale": "nucleotide phosphate-binding site; docking here flags likely inhibitor (disqualifying)",
        },
        "geometry": {
            "res141_CA": [round(float(x), 3) for x in r141ca],
            "fold_to_transport_center_separation_A": round(sep, 2),
            "note": "Boxes are >30 A apart; a molecule scoring well at both is rare and the fold-vs-transport contrast is meaningful.",
        },
    }
    with open(f"{REC}/boxes.json", "w") as f:
        json.dump(boxes, f, indent=2)
    print(f"  fold_site center   {boxes['fold_site']['center']}")
    print(f"  transport center   {boxes['transport_site']['center']}")
    print(f"  center separation  {sep:.2f} A")
    return boxes

if __name__ == "__main__":
    print("[1] cleaning WT ...")
    print("   ", write_clean_wt())
    print("[2] building Q141K static substitution ...")
    print("   ", build_q141k())
    print("[3] defining grid boxes ...")
    define_boxes()
    print("done.")
