#!/usr/bin/env python3
"""Verify the exact frozen receptor intermediates used by COMP-047."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXPECTED = json.loads((HERE / "inputs/receptor_expected.json").read_text())

STANDARD_RESIDUES = {
    "ALA", "ARG", "ASN", "ASP", "CYS", "GLN", "GLU", "GLY", "HIS", "ILE",
    "LEU", "LYS", "MET", "PHE", "PRO", "SER", "THR", "TRP", "TYR", "VAL",
}


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atom_records(path):
    records = []
    for line in path.read_text().splitlines():
        if line.startswith(("ATOM  ", "HETATM")):
            records.append(
                {
                    "line": line,
                    "atom": line[12:16].strip(),
                    "resname": line[17:20].strip(),
                    "chain": line[21:22].strip() or "_",
                    "resseq": int(line[22:26]),
                }
            )
    return records


def summarize(path):
    records = atom_records(path)
    residues = {
        (record["chain"], record["resseq"], record["resname"])
        for record in records
    }
    return records, {"atom_count": len(records), "residue_count": len(residues)}


def residue_summary(records, number):
    selected = [record for record in records if record["resseq"] == number]
    names = {record["resname"] for record in selected}
    if len(names) != 1:
        raise AssertionError(f"residue {number} has unexpected names: {sorted(names)}")
    return {"resname": next(iter(names)), "atoms": sorted(r["atom"] for r in selected)}


def verify_and_write():
    checks = []
    records_by_path = {}
    for relative_path, expected in EXPECTED["files"].items():
        path = HERE / relative_path
        actual_hash = sha256(path)
        if actual_hash != expected["sha256"]:
            raise AssertionError(
                f"hash mismatch for {relative_path}: {actual_hash} != {expected['sha256']}"
            )
        check = {"path": relative_path, "sha256": actual_hash, "status": "PASS"}
        if "atom_count" in expected:
            records, counts = summarize(path)
            records_by_path[relative_path] = records
            if counts["atom_count"] != expected["atom_count"]:
                raise AssertionError(f"atom count mismatch for {relative_path}")
            if counts["residue_count"] != expected["residue_count"]:
                raise AssertionError(f"residue count mismatch for {relative_path}")
            check.update(counts)
        checks.append(check)

    residue_paths = {
        "clean_wt": "work/receptor/abcg2_wt_clean.pdb",
        "clean_q141k": "work/receptor/abcg2_q141k_clean.pdb",
        "pdbqt_wt": "work/receptor/abcg2_wt.pdbqt",
        "pdbqt_q141k": "work/receptor/abcg2_q141k.pdbqt",
    }
    residue_checks = {}
    for label, relative_path in residue_paths.items():
        actual = residue_summary(records_by_path[relative_path], 141)
        if actual != EXPECTED["residue_141"][label]:
            raise AssertionError(
                f"residue-141 mismatch for {label}: {actual} "
                f"!= {EXPECTED['residue_141'][label]}"
            )
        residue_checks[label] = actual

    wt_clean = records_by_path["work/receptor/abcg2_wt_clean.pdb"]
    mutant_clean = records_by_path["work/receptor/abcg2_q141k_clean.pdb"]
    wt_non141 = [record["line"] for record in wt_clean if record["resseq"] != 141]
    mutant_non141 = [
        record["line"] for record in mutant_clean if record["resseq"] != 141
    ]
    if wt_non141 != mutant_non141:
        raise AssertionError("clean WT/Q141K files differ outside residue 141")

    nonstandard = {}
    for label in ("pdbqt_wt", "pdbqt_q141k"):
        relative_path = residue_paths[label]
        found = sorted(
            {
                f"{record['chain']}:{record['resseq']}:{record['resname']}"
                for record in records_by_path[relative_path]
                if record["resname"] not in STANDARD_RESIDUES
            }
        )
        if found != EXPECTED["allowed_pdbqt_warning"]["nonstandard_residues"]:
            raise AssertionError(f"unexpected nonstandard PDBQT residues: {label}={found}")
        nonstandard[label] = found

    boxes = json.loads((HERE / "work/receptor/boxes.json").read_text())
    expected_boxes = EXPECTED["boxes"]
    observed_boxes = {
        "fold_site_center": boxes["fold_site"]["center"],
        "transport_site_center": boxes["transport_site"]["center"],
        "fold_size": boxes["fold_site"]["size"],
        "transport_size": boxes["transport_site"]["size"],
        "center_separation_A": boxes["geometry"][
            "fold_to_transport_center_separation_A"
        ],
    }
    if observed_boxes["fold_site_center"] != expected_boxes["fold_site_center"]:
        raise AssertionError("fold-site center mismatch")
    if (
        observed_boxes["transport_site_center"]
        != expected_boxes["transport_site_center"]
    ):
        raise AssertionError("transport-site center mismatch")
    if observed_boxes["fold_size"] != expected_boxes["size"]:
        raise AssertionError("fold-site box size mismatch")
    if observed_boxes["transport_size"] != expected_boxes["size"]:
        raise AssertionError("transport-site box size mismatch")
    if (
        observed_boxes["center_separation_A"]
        != expected_boxes["center_separation_A"]
    ):
        raise AssertionError("box center-separation mismatch")

    output = {
        "schema_version": 1,
        "status": "PASS_WITH_DECLARED_WARNING",
        "checks": checks,
        "residue_141": residue_checks,
        "clean_structure_difference_scope": "all non-residue-141 ATOM records are byte-identical",
        "pdbqt_nonstandard_residues": nonstandard,
        "declared_warning": EXPECTED["allowed_pdbqt_warning"]["interpretation"],
        "boxes": observed_boxes,
    }
    output_path = HERE / "outputs/receptor_verification.json"
    output_path.write_text(json.dumps(output, indent=2) + "\n")
    print(f"{output['status']}: wrote {output_path}")
    return output


def main():
    verify_and_write()


if __name__ == "__main__":
    main()
