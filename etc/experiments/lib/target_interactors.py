"""
experiments/lib/target_interactors.py

Shared helper: assemble a conservative target-relationship exclusion set for a
molecular-target compound screen.

Encodes the UNION RULE documented in
wiki/etc/chembl-cross-check.md §"ChEMBL scope & blind spots":

    conservative exclusions  =  ChEMBL activity  ∪  UniProt-exposed DrugBank relationships

This is a screening exclusion rule, not a complete biological-interactor set:
  - ChEMBL activity records do not cover every transporter substrate.
  - A DrugBank identifier exposed in a UniProt flat-file cross-reference
    establishes a target relationship but does NOT type that relationship as
    substrate, inhibitor, or clinical interaction.
  - Assign a relationship subtype only from an independent per-drug source such
    as a primary paper, FDA label, TransPortal, PharmGKB, or a directly inspected
    DrugBank transporter annotation.

Canonical case — comp-047 (ABCG2 Q141K): the FDA CRESTOR label identifies
rosuvastatin as a BCRP substrate; the UniProt-exposed DrugBank set independently
flags a relationship, while the bounded ChEMBL check returned no ABCG2 activity
row. The FDA label, not the generic cross-reference, supports the substrate type.

Network:
  - UniProt (rest.uniprot.org) is in the OE sandbox allowlist -> the
    DrugBank relationship side runs IN-SANDBOX and is available when UniProt is
    reachable.
  - ChEMBL REST (www.ebi.ac.uk) is NOT allowlisted -> the activity side needs
    network access (run with dangerouslyDisableSandbox, or supply ChEMBL results
    from another reviewed source and merge). chembl_activity() degrades to
    (None, ...) when unreachable rather than failing the run.

stdlib only. Name matching is normalized-exact (lowercase, '_'->' ', collapse
whitespace); salt/hyphen/synonym variants can miss — see _norm() and the
Limitations note in any comp that uses this.

CLI:
  python target_interactors.py --uniprot Q9UNQ0 --library work/ligands/smiles_resolved.json \
      --chembl-target CHEMBL5393 --out outputs/target_relationship_exclusions.json
  python target_interactors.py --uniprot Q9UNQ0 --library names.txt --no-chembl
"""
import argparse
import json
import re
import subprocess
import urllib.parse

UNIPROT_TXT = "https://rest.uniprot.org/uniprotkb/{acc}.txt"
CHEMBL_MOL_SEARCH = "https://www.ebi.ac.uk/chembl/api/data/molecule/search.json?q={q}&limit=1"
CHEMBL_ACTIVITY = ("https://www.ebi.ac.uk/chembl/api/data/activity.json"
                   "?target_chembl_id={t}&molecule_chembl_id={m}&limit=1000")

_WS = re.compile(r"\s+")


def _get(url, timeout=30):
    """Fetch via curl. curl is the reliable path inside the OE sandbox — raw
    Python SSL can be blocked even for allowlisted hosts (rest.uniprot.org), while
    curl honors the allowlist. Matches the lib/ curl convention. Non-allowlisted
    hosts (ChEMBL REST) require the caller to run with dangerouslyDisableSandbox."""
    p = subprocess.run(["curl", "-sL", "--max-time", str(timeout), url],
                       capture_output=True, text=True, timeout=timeout + 15)
    if p.returncode != 0 or not p.stdout:
        raise RuntimeError(f"curl failed for {url}: rc={p.returncode} {p.stderr[:200]}")
    return p.stdout


def _norm(name):
    """Normalize a compound name for cross-source matching: lowercase, treat '_'
    as space, collapse whitespace, strip. Deliberately does NOT touch hyphens
    (meaningful in many drug names)."""
    return _WS.sub(" ", str(name).replace("_", " ").strip().lower())


def fetch_uniprot_drugbank_relationships(acc, timeout=30):
    """{normalized_name: original_name} for every DrugBank drug the UniProt entry
    cross-references.

    Parses lines like:  DR   DrugBank; DB00437; Allopurinol.
    The line establishes a relationship only; it does not encode its subtype.
    """
    txt = _get(UNIPROT_TXT.format(acc=acc), timeout)
    out = {}
    for line in txt.splitlines():
        if line.startswith("DR   DrugBank;"):
            parts = line.split(";")
            if len(parts) >= 3:
                name = parts[2].strip().rstrip(".")
                if name:
                    out[_norm(name)] = name
    return out


def fetch_uniprot_reactions(acc, timeout=30):
    """Canonical catalytic/transport substrates from the entry's CC 'Reaction='
    lines (authoritative physiological substrates + any KM/Vmax nearby)."""
    txt = _get(UNIPROT_TXT.format(acc=acc), timeout)
    rxns = []
    for line in txt.splitlines():
        if "Reaction=" in line:
            rxns.append(line.split("Reaction=", 1)[1].strip())
    return rxns


def chembl_activity(mol_name, target_chembl_id, timeout=30):
    """Best-effort ChEMBL activity check for one molecule vs one target.

    Returns (has_activity, best_pchembl, chembl_id):
      - (True/False, float|None, id)  when reachable
      - (None, None, None)            when ChEMBL is unreachable (e.g. sandbox);
                                      caller should treat None as 'not queried'.
    """
    try:
        js = json.loads(_get(CHEMBL_MOL_SEARCH.format(q=urllib.parse.quote(mol_name)), timeout))
        mols = js.get("molecules") or []
        if not mols:
            return (False, None, None)
        cid = mols[0].get("molecule_chembl_id")
        act = json.loads(_get(CHEMBL_ACTIVITY.format(t=target_chembl_id, m=cid), timeout))
        acts = act.get("activities") or []
        if not acts:
            return (False, None, cid)
        pchembls = [float(a["pchembl_value"]) for a in acts if a.get("pchembl_value")]
        return (True, max(pchembls) if pchembls else None, cid)
    except Exception:
        return (None, None, None)


def build_conservative_exclusions(
    acc, compound_names, target_chembl_id=None, include_chembl=True
):
    """Assemble a conservative exclusion set for `compound_names` and target `acc`.

    The DrugBank-via-UniProt axis is relationship-only. The ChEMBL activity axis
    runs when include_chembl and target_chembl_id are given and ChEMBL is reachable.
    Neither axis assigns a substrate subtype.
    """
    db = fetch_uniprot_drugbank_relationships(acc)
    per = {}
    for name in compound_names:
        relationship = _norm(name) in db
        activity, pchembl, cid = (None, None, None)
        if include_chembl and target_chembl_id:
            activity, pchembl, cid = chembl_activity(
                str(name).replace("_", " "), target_chembl_id
            )
        per[name] = {
            "drugbank_relationship": relationship,
            "chembl_activity": activity,       # True / False / None(not queried)
            "chembl_best_pchembl": pchembl,
            "chembl_id": cid,
            "conservative_exclusion": relationship or (activity is True),
        }
    union = sorted([n for n, r in per.items() if r["conservative_exclusion"]])
    chembl_ran = include_chembl and bool(target_chembl_id) and any(
        r["chembl_activity"] is not None for r in per.values())
    return {
        "_meta": {
            "uniprot": acc,
            "target_chembl_id": target_chembl_id,
            "drugbank_relationship_list_size": len(db),
            "chembl_queried": chembl_ran,
            "chembl_note": None if chembl_ran else
                "ChEMBL activity axis NOT run (unreachable or --no-chembl). "
                "The UniProt-exposed DrugBank relationship axis still ran.",
            "exclusion_rule": "conservative exclusions = ChEMBL activity UNION UniProt-exposed DrugBank relationships",
            "typing_note": "DrugBank cross-references do not establish substrate/inhibitor subtype; verify subtype independently.",
        },
        "per_compound": per,
        "conservative_exclusions": union,
    }


def _load_library(path):
    """Accept either a JSON object/list of names (e.g. smiles_resolved.json keys)
    or a newline-delimited text file."""
    p = path
    if p.endswith(".json"):
        data = json.load(open(p))
        return list(data.keys()) if isinstance(data, dict) else list(data)
    return [ln.strip() for ln in open(p) if ln.strip()]


def main():
    ap = argparse.ArgumentParser(
        description="Assemble conservative ChEMBL-activity + DrugBank-relationship exclusions."
    )
    ap.add_argument("--uniprot", required=True, help="UniProt accession (e.g. Q9UNQ0)")
    ap.add_argument("--library", required=True, help="JSON (names as keys/list) or newline text file")
    ap.add_argument("--chembl-target", default=None, help="ChEMBL target id (e.g. CHEMBL5393)")
    ap.add_argument("--no-chembl", action="store_true", help="skip the ChEMBL activity axis")
    ap.add_argument("--out", default=None, help="write JSON here (else stdout summary)")
    args = ap.parse_args()

    names = _load_library(args.library)
    res = build_conservative_exclusions(
        args.uniprot,
        names,
        target_chembl_id=args.chembl_target,
        include_chembl=not args.no_chembl,
    )
    if args.out:
        json.dump(res, open(args.out, "w"), indent=2)
    m = res["_meta"]
    print(f"target {m['uniprot']} | library {len(names)} | DrugBank relationships {m['drugbank_relationship_list_size']} "
          f"| ChEMBL axis {'run' if m['chembl_queried'] else 'SKIPPED'}")
    print(f"conservative exclusions: {len(res['conservative_exclusions'])}")
    for n in res["conservative_exclusions"]:
        r = res["per_compound"][n]
        tags = []
        if r["drugbank_relationship"]:
            tags.append("drugbank-relationship")
        if r["chembl_activity"]:
            tags.append(f"chembl-activity(p{r['chembl_best_pchembl']})")
        print(f"  {n:28s} {'+'.join(tags)}")
    if args.out:
        print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
