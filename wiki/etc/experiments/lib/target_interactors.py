"""
experiments/lib/target_interactors.py

Shared helper: assemble the complete "known interactor" set for a molecular
target — the disqualifier axis any transporter / enzyme compound screen needs.

Encodes the UNION RULE documented in
wiki/etc/chembl-cross-check.md §"ChEMBL scope & blind spots":

    known interactors of target Y  =  ChEMBL inhibitors  ∪  DrugBank/UniProt substrates

Neither source alone is complete:
  - ChEMBL logs INHIBITION (IC50/Ki/Kd) and structurally MISSES SUBSTRATES.
  - DrugBank (approved-drugs only, reached free via UniProt cross-refs) captures
    substrate + clinical-interaction relationships but misses research-tool
    inhibitors (e.g. Ko143, fumitremorgin C) that ChEMBL does have.

Canonical case — comp-047 (ABCG2 Q141K): rosuvastatin is a textbook ABCG2
SUBSTRATE (Q141K raises its plasma AUC ~2x) yet returns 0 ChEMBL records; it is
caught only by the DrugBank axis. Using ChEMBL alone as the disqualifier silently
dropped it. This helper exists so no future screen repeats that by hand.

Network:
  - UniProt (rest.uniprot.org) is in the OE sandbox allowlist -> the
    DrugBank / substrate side runs IN-SANDBOX and is always available (it is the
    half ChEMBL misses).
  - ChEMBL REST (www.ebi.ac.uk) is NOT allowlisted -> the inhibitor side needs
    network access (run with dangerouslyDisableSandbox, or supply ChEMBL results
    from the bio-research ChEMBL MCP and merge). chembl_inhibitor() degrades to
    (None, ...) when unreachable rather than failing the run.

stdlib only. Name matching is normalized-exact (lowercase, '_'->' ', collapse
whitespace); salt/hyphen/synonym variants can miss — see _norm() and the
Limitations note in any comp that uses this.

CLI:
  python target_interactors.py --uniprot Q9UNQ0 --library work/ligands/smiles_resolved.json \
      --chembl-target CHEMBL5393 --out outputs/known_interactors.json
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


def fetch_uniprot_drugbank(acc, timeout=30):
    """{normalized_name: original_name} for every DrugBank drug the UniProt entry
    cross-references (the target's substrate + clinical-interaction drug set).

    Parses lines like:  DR   DrugBank; DB00437; Allopurinol.
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


def chembl_inhibitor(mol_name, target_chembl_id, timeout=30):
    """Best-effort ChEMBL inhibition check for one molecule vs one target.

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


def known_interactors(acc, compound_names, target_chembl_id=None, include_chembl=True):
    """Assemble the union disqualifier set for `compound_names` against target `acc`.

    Substrate axis (DrugBank via UniProt) is always run. Inhibitor axis (ChEMBL)
    runs when include_chembl and target_chembl_id are given AND ChEMBL is reachable.
    """
    db = fetch_uniprot_drugbank(acc)
    per = {}
    for name in compound_names:
        sub = _norm(name) in db
        inh, pchembl, cid = (None, None, None)
        if include_chembl and target_chembl_id:
            inh, pchembl, cid = chembl_inhibitor(str(name).replace("_", " "), target_chembl_id)
        per[name] = {
            "drugbank_substrate_or_interaction": sub,
            "chembl_inhibitor": inh,           # True / False / None(not queried)
            "chembl_best_pchembl": pchembl,
            "chembl_id": cid,
            "known_interactor": bool(sub) or (inh is True),
        }
    union = sorted([n for n, r in per.items() if r["known_interactor"]])
    chembl_ran = include_chembl and bool(target_chembl_id) and any(
        r["chembl_inhibitor"] is not None for r in per.values())
    return {
        "_meta": {
            "uniprot": acc,
            "target_chembl_id": target_chembl_id,
            "drugbank_list_size": len(db),
            "chembl_queried": chembl_ran,
            "chembl_note": None if chembl_ran else
                "ChEMBL inhibitor axis NOT run (unreachable in-sandbox or --no-chembl). "
                "Substrate axis (DrugBank/UniProt) is complete; supply ChEMBL via REST "
                "(dangerouslyDisableSandbox) or the ChEMBL MCP to complete the union.",
            "union_rule": "known interactors = ChEMBL inhibitors UNION DrugBank/UniProt substrates",
        },
        "per_compound": per,
        "known_interactor_union": union,
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
    ap = argparse.ArgumentParser(description="Assemble the known-interactor union for a target.")
    ap.add_argument("--uniprot", required=True, help="UniProt accession (e.g. Q9UNQ0)")
    ap.add_argument("--library", required=True, help="JSON (names as keys/list) or newline text file")
    ap.add_argument("--chembl-target", default=None, help="ChEMBL target id (e.g. CHEMBL5393)")
    ap.add_argument("--no-chembl", action="store_true", help="skip the ChEMBL inhibitor axis")
    ap.add_argument("--out", default=None, help="write JSON here (else stdout summary)")
    args = ap.parse_args()

    names = _load_library(args.library)
    res = known_interactors(args.uniprot, names, target_chembl_id=args.chembl_target,
                            include_chembl=not args.no_chembl)
    if args.out:
        json.dump(res, open(args.out, "w"), indent=2)
    m = res["_meta"]
    print(f"target {m['uniprot']} | library {len(names)} | DrugBank list {m['drugbank_list_size']} "
          f"| ChEMBL axis {'run' if m['chembl_queried'] else 'SKIPPED'}")
    print(f"known interactors (union): {len(res['known_interactor_union'])}")
    for n in res["known_interactor_union"]:
        r = res["per_compound"][n]
        tags = []
        if r["drugbank_substrate_or_interaction"]:
            tags.append("drugbank")
        if r["chembl_inhibitor"]:
            tags.append(f"chembl(p{r['chembl_best_pchembl']})")
        print(f"  {n:28s} {'+'.join(tags)}")
    if args.out:
        print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
