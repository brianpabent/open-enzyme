#!/usr/bin/env python3
"""
comp-034 structure-gated cleavage re-analysis (orthogonal method #1).

The existing comp-005/034 cleavage model uses **pLDDT as its accessibility
proxy** (lib/protease_stability.py: classify_accessibility(mean_plddt) ->
buried/partial/exposed -> 0.1/0.4/1.0 risk weight). The inter-lobe linker
(UniProt 353-363) has pLDDT 93-98, so EVERY linker residue is classified
"buried" (0.1x). But pLDDT is a CONFIDENCE score, not burial: a confidently
predicted, solvent-EXPOSED helix scores 95. So the model under-counts the
linker's sequence-driven cleavage risk ~10x for the wrong reason.

This script replaces the pLDDT proxy with two real structural quantities and
asks whether the variant ranking changes:
  1. Real solvent accessibility (SASA, relative to Tien 2013 max-ASA) — does
     the side chain actually face solvent?
  2. Conformation gate — proteases require an EXTENDED substrate across the
     active-site cleft (Tyndall 2005, "proteases universally recognize beta
     strands"); an alpha-helix resists cleavage even when solvent-exposed.

Net mechanistic reframe to test: the WT linker's real protection is its HELIX
CONFORMATION, not burial. Therefore proline substitutions, by breaking the
helix, can INCREASE conformational cleavage-accessibility even as they remove
protease-preferred residues — partially self-defeating. Charge/polar (MPNN)
arms keep the helix -> protected by conformation AND stripped of preferred
residues. Helix retention (from the Rosetta ddG leg) governs BOTH axes.

Conformation weights are heuristic but mechanistically grounded; results are
reported as DIRECTIONAL (which strategy wins), not precise cleavage rates.
"""
import json, shutil, sys, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXP = HERE.parent
LIB = EXP.parent / "lib"              # wiki/etc/experiments/lib
sys.path.insert(0, str(LIB))

PDB = EXP / "proteinmpnn_rerun" / "AF-P02788-F1-model_v6.pdb"
FASTA = EXP / "inputs" / "P02788.fasta"
PLDDT_JSON = EXP / "inputs" / "alphafold_P02788_plddt.json"
SPECS = (EXP.parent / "comp-005-lactoferrin-shio-koji-protease-stability"
         / "inputs" / "protease_specificities.json")
DDG_JSON = HERE / "rosetta_ddg_results_torsion3.json"   # helix retention per variant

LINKER_START, LINKER_END = 353, 363
WT_LINKER = "SEEEVAARRAR"

CANDIDATES = {
    "WT_SEEEVAARRAR":          "SEEEVAARRAR",
    "V357P_SEEEPAARRAR":       "SEEEPAARRAR",
    "S353E_V357P_EEEEPAARRAR": "EEEEPAARRAR",
    "MPNN_NEEEQQQEEEQ":        "NEEEQQQEEEQ",
    "MPNN_NEEEQEEQDQQ":        "NEEEQEEQDQQ",
    "AGGR_PRO_EEEEPAAPPAP":    "EEEEPAAPPAP",
}

# Tien et al. 2013 (PLoS ONE) theoretical max ASA (A^2), per residue type.
MAXASA = {"A":129,"R":274,"N":195,"D":193,"C":167,"E":223,"Q":225,"G":104,
          "H":224,"I":197,"L":201,"K":236,"M":224,"F":240,"P":159,"S":155,
          "T":172,"W":285,"Y":263,"V":174}

# real-SASA accessibility weight (same buckets as the lib's pLDDT proxy, so the
# only thing that changes is HOW accessibility is measured)
def sasa_acc_weight(rsasa):
    if rsasa < 0.05:  return 0.1, "buried"
    if rsasa < 0.25:  return 0.4, "partial"
    return 1.0, "exposed"

# conformation gate: proteases need extended substrate; helix protects
SS_CONF = {"H":0.2,"G":0.2,"I":0.2,"E":0.7,"B":0.7,"T":1.0,"S":1.0,"L":1.0," ":1.0,"-":1.0}


def staged_pdb():
    d = Path(tempfile.gettempdir()) / "comp034_rosetta"; d.mkdir(parents=True, exist_ok=True)
    dst = d / "af_p02788.pdb"; shutil.copy(str(PDB), str(dst)); return str(dst)


def reconstruct(full, linker):
    assert full[LINKER_START-1:LINKER_END] == WT_LINKER, "WT linker mismatch in FASTA"
    return full[:LINKER_START-1] + linker + full[LINKER_END:]


def main():
    import pyrosetta
    from protease_stability import load_sequence, load_plddt, load_proteases, find_cleavage_sites

    pyrosetta.init("-mute all -ignore_unrecognized_res true -detect_disulf false", silent=True)
    pose = pyrosetta.pose_from_pdb(staged_pdb())

    # --- real per-residue SASA (relative) for the linker region ---
    sc = pyrosetta.rosetta.core.scoring.sasa.SasaCalc()
    sc.calculate(pose)
    rsd_sasa = sc.get_residue_sasa()
    ss = pyrosetta.rosetta.core.scoring.dssp.Dssp(pose).get_dssp_secstruct()

    print("=== WT linker: pLDDT-proxy accessibility  vs  REAL structure ===")
    plddt = load_plddt(PLDDT_JSON)
    print(f"{'resi':>4} {'aa':>2} {'pLDDT':>6} {'proxy':>8} | {'rSASA':>6} {'realacc':>8} {'SS':>3} {'conf':>5}")
    for r in range(LINKER_START, LINKER_END+1):
        aa = pose.residue(r).name1()
        rsasa = rsd_sasa[r] / MAXASA[aa]
        w, real = sasa_acc_weight(rsasa)
        pl = plddt[r]; proxy = "buried" if pl >= 80 else ("partial" if pl >= 65 else "exposed")
        print(f"{r:>4} {aa:>2} {pl:6.1f} {proxy:>8} | {rsasa:6.2f} {real:>8} {ss[r-1]:>3} {SS_CONF.get(ss[r-1],1.0):>5}")

    # accessibility-independent per-residue values from the real structure
    real_acc = {}
    for r in range(LINKER_START, LINKER_END+1):
        aa = pose.residue(r).name1()
        rsasa = rsd_sasa[r] / MAXASA[aa]
        real_acc[r] = sasa_acc_weight(rsasa)[0]
    wt_conf_per_res = {r: SS_CONF.get(ss[r-1], 1.0) for r in range(LINKER_START, LINKER_END+1)}

    # --- cleavage scoring per variant under 3 models ---
    full = load_sequence(FASTA)
    proteases, conditions = load_proteases(SPECS)
    nacl = conditions["NaCl_pct"]
    helix = {}
    if DDG_JSON.exists():
        dd = json.load(open(DDG_JSON))["results"]
        helix = {k: v.get("linker_helix_frac", None) for k, v in dd.items()}

    def variant_scores(linker_seq, helix_frac):
        seq = reconstruct(full, linker_seq)
        seq_only = pldd = struct = 0.0
        for pdata in proteases.values():
            for s in find_cleavage_sites(seq, pdata, plddt, nacl):
                pos = s["position"]
                if not (LINKER_START <= pos <= LINKER_END):
                    continue
                raw = s["effective_protease_activity"]          # accessibility-independent
                seq_only += raw                                  # (a) sequence + conditions only
                pldd += s["risk_score"]                          # (b) existing model (pLDDT proxy)
                # (c) structure-gated: real SASA x conformation.
                # conformation from variant helix retention (uniform over linker; approx),
                # falling back to WT per-residue SS where helix_frac unknown.
                if helix_frac is not None:
                    conf = helix_frac * 0.2 + (1 - helix_frac) * 1.0
                else:
                    conf = wt_conf_per_res.get(pos, 1.0)
                struct += raw * real_acc.get(pos, 1.0) * conf
        return round(seq_only, 3), round(pldd, 3), round(struct, 3)

    print("\n=== linker cleavage risk under three accessibility models ===")
    print(f"{'candidate':26s} {'helix':>5} | {'seqOnly':>8} {'existing':>9} {'structGated':>12}")
    rows = []
    for name, lk in CANDIDATES.items():
        hf = helix.get(name)
        so, pl, st = variant_scores(lk, hf)
        rows.append((name, lk, hf, so, pl, st))
        print(f"{name:26s} {('%.3f'%hf) if hf is not None else '  ?  ':>5} | {so:8.3f} {pl:9.3f} {st:12.3f}")

    out = {
        "_meta": {
            "analysis": "structure-gated cleavage re-analysis (orthogonal method #1)",
            "reframe": "existing model uses pLDDT as accessibility proxy; pLDDT!=burial. "
                       "Replaced with real SASA (Tien2013 rel) + conformation gate (helix protects).",
            "conformation_weights": SS_CONF, "sasa_buckets": "rSASA<0.05 buried, <0.25 partial, else exposed",
            "caveat": "conformation weights heuristic; mutant SASA approximated by WT-backbone SASA; "
                      "directional (which strategy wins), not precise cleavage rates.",
            "nacl_pct": nacl,
        },
        "variants": [{"name": n, "linker": lk, "helix_frac": hf,
                      "cleavage_seq_only": so, "cleavage_existing_pLDDTproxy": pl,
                      "cleavage_structure_gated": st} for n, lk, hf, so, pl, st in rows],
    }
    Path(HERE / "structure_gated_cleavage_results.json").write_text(json.dumps(out, indent=2))
    print("\n[wrote] structure_gated_cleavage_results.json")


if __name__ == "__main__":
    main()
