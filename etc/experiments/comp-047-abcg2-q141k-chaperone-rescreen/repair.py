#!/usr/bin/env python3
"""
comp-047 targeted re-dock / repair.

Re-docks named molecules with the (fixed) analyze.prep_ligand — e.g. salts whose
disconnected counterion broke Vina in the main run — and patches outputs/results.json
in place. Reuses analyze.py's prep/dock/classify so numbers stay consistent.

Usage: repair.py sodium_butyrate sodium_phenylbutyrate
"""
import json, sys
from pathlib import Path
import analyze as A

HERE = A.HERE


def main(names):
    boxes = json.load(open(HERE / "work/receptor/boxes.json"))
    fold_box, trans_box = boxes["fold_site"], boxes["transport_site"]
    smi = json.load(open(HERE / "work/ligands/smiles_resolved.json"))
    lib = {m["name"]: m for m in json.load(open(HERE / "inputs/fda_approved_drug_library.json"))["molecules"]}
    res = json.load(open(HERE / "outputs/results.json"))
    R = res["results"]

    for name in names:
        rec = smi[name]
        # force fresh ligand prep
        (A.LIGDIR / f"{name}.pdbqt").unlink(missing_ok=True)
        lig = A.prep_ligand(name, rec["smiles"])
        if lig is None:
            print(f"{name}: prep still failed")
            continue
        fq = A.dock(lig, A.REC_Q141K, fold_box, "fold_q141k")
        fw = A.dock(lig, A.REC_WT, fold_box, "fold_wt")
        tr = A.dock(lig, A.REC_WT, trans_box, "transport")
        known = (rec["role_tag"] == "abcg2_inhibitor")
        tier, margin, metrics = A.classify(fq, fw, tr, known)
        R[name] = {"role_tag": rec["role_tag"],
                   "drug_class": lib.get(name, {}).get("drug_class", "n/a"),
                   "cid": rec.get("cid"),
                   "fold_q141k_affinity": fq, "fold_wt_affinity": fw,
                   "transport_affinity": tr, "chaperone_tier": tier,
                   **metrics, "known_inhibitor_flag": known}
        print(f"{name}: fold_q141k={fq} fold_wt={fw} transport={tr} tier={tier}")

    json.dump(res, open(HERE / "outputs/results.json", "w"), indent=2)
    print("patched outputs/results.json")


if __name__ == "__main__":
    main(sys.argv[1:])
