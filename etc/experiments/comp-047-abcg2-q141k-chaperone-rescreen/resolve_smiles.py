#!/usr/bin/env python3
"""
comp-047 SMILES resolution.

comp-032's library has NO SMILES (only physicochemical descriptors), so we
resolve each drug name -> isomeric SMILES from PubChem PUG-REST. We also append
explicit negative-control ABCG2 inhibitors that the design requires.

Output: work/ligands/smiles_resolved.json
  { name: {smiles, source, cid, role_tag} }

role_tag classifies controls:
  cftr_corrector  -> POSITIVE control (must earn rank from docking, no prior)
  abcg2_inhibitor -> NEGATIVE control (must NOT rank as top chaperone)
  other           -> screening compound
"""
import json, time, urllib.request, urllib.parse, sys

HERE = "wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen"
LIB = f"{HERE}/inputs/fda_approved_drug_library.json"
OUT = f"{HERE}/work/ligands/smiles_resolved.json"

# name -> PubChem query alias for names PubChem won't resolve as-is
ALIASES = {
    "ko143": "Ko143",
    "fumitremorgin_c": "fumitremorgin C",
    "4-phenylbutyric_acid": "4-phenylbutyric acid",
    "sodium_butyrate": "sodium butyrate",
    "geldanamycin_17_aag": "tanespimycin",         # 17-AAG
    "ver155008": "VER-155008",
    "cyclosporine_a": "cyclosporine",
    "metformin_extended_release": "metformin",
    "glycerol_phenylbutyrate": "glycerol phenylbutyrate",
    "sodium_phenylbutyrate": "sodium 4-phenylbutyrate",
    "tauroursodeoxycholic_acid": "tauroursodeoxycholic acid",
    "n_acetylcysteine": "acetylcysteine",
    "egcg": "epigallocatechin gallate",
    "mcc950": "MCC950",
    "dapansutrile": "dapansutrile",
    "geldanamycin": "geldanamycin",
}

# Explicit negative controls to APPEND (design requires; not all in library)
EXTRA_INHIBITORS = {
    "novobiocin": "novobiocin",
}

# Which library drug_class / class_prior values map to control role tags.
CFTR_CLASSES = {"cftr_corrector", "cftr_potentiator"}
# Known ABCG2 inhibitors/substrates present in the library (by name) — flagged
# as negative controls for the "must not rank as chaperone" check.
LIB_INHIBITOR_NAMES = {
    "ko143", "fumitremorgin_c", "tariquidar", "elacridar",
    "ketoconazole", "itraconazole", "cyclosporine_a",
    "novobiocin",
    # ABCG2 substrates (transported; high-affinity pocket binders)
    "mitoxantrone", "topotecan", "etoposide", "sulfasalazine", "methotrexate",
}


def pubchem_smiles(query):
    q = urllib.parse.quote(query)
    for prop in ("IsomericSMILES", "SMILES", "CanonicalSMILES"):
        url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{q}/property/{prop}/JSON"
        try:
            with urllib.request.urlopen(url, timeout=25) as r:
                d = json.loads(r.read().decode())
            props = d["PropertyTable"]["Properties"][0]
            smi = props.get(prop) or props.get("SMILES") or props.get("ConnectivitySMILES")
            cid = props.get("CID")
            if smi:
                return smi, cid, f"pubchem:{prop}"
        except Exception:
            continue
    return None, None, None


def role_of(name, mol):
    cp = (mol or {}).get("class_prior", "")
    if name in ("ivacaftor", "tezacaftor", "elexacaftor", "lumacaftor") or cp in CFTR_CLASSES:
        return "cftr_corrector"
    if name in LIB_INHIBITOR_NAMES:
        return "abcg2_inhibitor"
    return "other"


def main():
    lib = json.load(open(LIB))
    mols = {m["name"]: m for m in lib["molecules"]}
    names = list(mols.keys()) + list(EXTRA_INHIBITORS.keys())

    out = {}
    failures = []
    for i, name in enumerate(names, 1):
        query = ALIASES.get(name, EXTRA_INHIBITORS.get(name, name.replace("_", " ")))
        smi, cid, src = pubchem_smiles(query)
        role = role_of(name, mols.get(name))
        if smi:
            out[name] = {"smiles": smi, "cid": cid, "source": src,
                         "query": query, "role_tag": role}
        else:
            failures.append(name)
            out[name] = {"smiles": None, "cid": None, "source": None,
                         "query": query, "role_tag": role}
        print(f"[{i:3d}/{len(names)}] {name:32s} {'OK ' if smi else 'FAIL'} {src or ''}")
        time.sleep(0.20)  # be polite to PUG-REST

    json.dump(out, open(OUT, "w"), indent=2)
    print(f"\nResolved {len(out)-len(failures)}/{len(out)}. Failures: {failures}")


if __name__ == "__main__":
    main()
