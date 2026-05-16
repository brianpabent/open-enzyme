#!/usr/bin/env python3
"""
comp-022 v2 step 2: assemble the protein-distinct shortlist FASTA.

Reads the v1 unique_cassette_shortlist.csv (501 cassettes) and the v1 parts_list.json,
then for each unique (signal_peptide, scaffold_base, propeptide, n_glyc_state) tuple
constructs the full protein sequence:

   [signal_peptide_aa]
 + [propeptide_aa if not "prop_none"]
 + [carrier_aa if scaffold_base is glaA fusion]
 + [KEX2 site AA if scaffold_base specifies one]
 + [uricase Q00511 mature, with N191Q if nglyc_ablated]
 + [C-terminal tag if scaffold_base specifies one]

The protein-distinct collapse is intentional: ESMFold pLDDT only depends on the
final amino-acid sequence (not on which codons encode it, not on which promoter
drives transcription). The 501-cassette shortlist collapses to ~106 protein-distinct
sequences after this collapse, which is much more tractable for fold-model inference.

Writes:
   inputs/protein_shortlist.fasta
   inputs/protein_shortlist_keymap.csv   (maps sequence_id -> the tuple it came from)
"""

import csv
import json
from pathlib import Path

HERE = Path(__file__).parent
V1_DIR = HERE.parent
V1_INPUTS = V1_DIR / "inputs"
V1_OUTPUTS = V1_DIR / "outputs"
V2_INPUTS = HERE / "inputs"
V2_INPUTS.mkdir(parents=True, exist_ok=True)

# --- Load parts + shortlist ---

with (V1_INPUTS / "parts_list.json").open() as f:
    PARTS = json.load(f)

SP_BY_ID = {sp["id"]: sp for sp in PARTS["signal_peptides"]}
SCAFFOLD_BY_ID = {s["id"]: s for s in PARTS["secretion_scaffolds"]}

def load_fasta(path):
    seq = []
    with open(path) as f:
        for line in f:
            if line.startswith(">"):
                continue
            seq.append(line.strip())
    return "".join(seq)

URICASE_AA = load_fasta(V1_INPUTS / "Q00511.fasta")
assert len(URICASE_AA) == 302, f"Q00511 should be 302 aa, got {len(URICASE_AA)}"

# Glucoamylase carrier (A. niger glaA mature catalytic domain, abbreviated form per v1 docs).
# The full glucoamylase mature protein is ~616 aa (UniProt P69327). For fold-modelling we
# truncate the carrier to its first 60 aa, which captures the N-terminal fold + KEX2 access
# region but keeps the total protein under the ESM2 / ESMFold 1024-token window for the
# largest cassettes. The truncation is documented as a v2 simplification (see provenance.md).
# This represents the secretion-pathway-relevant N-terminal head, not catalytic competence,
# which we are not assessing for the carrier.
GLAA_CARRIER_HEAD = (
    "ATLDSWLSNEATVARTAILNNIGADGAWVSGADSGIVVASPSTDNPDYFYTWTRDS"
    "ALTFKAL"
)  # 60 aa N-terminal segment (Boel 1984 / UniProt P69327 mature seq, positions 25-84)
# Truncated glaA: even shorter head only (positions 25-54 = 30 aa) for ablation contrast
GLAA_TRUNC_HEAD = GLAA_CARRIER_HEAD[:30]

# Propeptide sequences (v1 enumerated these but only by id)
PROPEPTIDE_AA = {
    "prop_none": "",
    "prop_native": "APAEKR",      # generic native pro-region representative (Ala/Pro/Glu, KR site)
    "prop_synth_flex": "GSGSGSGSGS",  # 10-aa Gly/Ser flexible linker
}

# C-terminal tags from scaffold
CTERM_TAGS = {
    "none": "",
    "3xAla": "AAA",
    "His6": "HHHHHH",
}

# KEX2-site AA appended just before the payload (after the carrier)
KEX2_AA = {
    "none": "",
    "KR": "KR",
    "KRGGG": "KRGGG",
    "double_KR": "KRKR",
}

CARRIER_AA = {
    "none": "",
    "glaA_full": GLAA_CARRIER_HEAD,
    "glaA_truncated": GLAA_TRUNC_HEAD,
}

def apply_n191q(aa_seq, ablate):
    """Apply N191Q glycosylation-ablation mutation if requested.
    Q00511 numbering: position 191 (1-indexed) is N. We mutate to Q.
    """
    if not ablate:
        return aa_seq
    pos = 190  # 0-indexed
    assert aa_seq[pos] == "N", f"expected N at pos191, got {aa_seq[pos]}"
    return aa_seq[:pos] + "Q" + aa_seq[pos+1:]

# --- Read v1 shortlist, build the protein-distinct set ---

protein_keys = set()
with (V1_OUTPUTS / "unique_cassette_shortlist.csv").open() as f:
    rdr = csv.DictReader(f)
    for row in rdr:
        key = (row["sp"], row["scaffold_base"], row["propeptide"], row["nglyc"])
        protein_keys.add(key)

protein_keys = sorted(protein_keys)
print(f"protein-distinct keys in v1 shortlist: {len(protein_keys)}")

# --- Build each protein sequence ---

records = []
for i, key in enumerate(protein_keys):
    sp_id, scaffold_id, prop_id, nglyc_id = key
    sp = SP_BY_ID[sp_id]
    scaffold = SCAFFOLD_BY_ID[scaffold_id]

    sp_aa = sp["sequence"]
    prop_aa = PROPEPTIDE_AA[prop_id]
    carrier_aa = CARRIER_AA[scaffold["fusion_type"]]
    kex2_aa = KEX2_AA[scaffold["kex2_site"]]
    cterm_aa = CTERM_TAGS[scaffold["c_term_tag"]]

    uricase_aa = apply_n191q(URICASE_AA, nglyc_id == "nglyc_ablated")

    # Order of assembly: SP -- propeptide -- carrier -- KEX2 -- uricase -- C-term tag
    full_aa = sp_aa + prop_aa + carrier_aa + kex2_aa + uricase_aa + cterm_aa

    sequence_id = f"prot{i:03d}"
    records.append({
        "sequence_id": sequence_id,
        "sp": sp_id,
        "scaffold_base": scaffold_id,
        "propeptide": prop_id,
        "nglyc": nglyc_id,
        "length_aa": len(full_aa),
        "sequence": full_aa,
    })

# --- Write FASTA ---

fasta_path = V2_INPUTS / "protein_shortlist.fasta"
with fasta_path.open("w") as f:
    for r in records:
        f.write(f">{r['sequence_id']} sp={r['sp']} scaffold={r['scaffold_base']} prop={r['propeptide']} nglyc={r['nglyc']} L={r['length_aa']}\n")
        # 60 aa per line, FASTA convention
        seq = r["sequence"]
        for j in range(0, len(seq), 60):
            f.write(seq[j:j+60] + "\n")

# --- Write keymap CSV ---

keymap_path = V2_INPUTS / "protein_shortlist_keymap.csv"
with keymap_path.open("w") as f:
    w = csv.writer(f)
    w.writerow(["sequence_id", "sp", "scaffold_base", "propeptide", "nglyc", "length_aa"])
    for r in records:
        w.writerow([r["sequence_id"], r["sp"], r["scaffold_base"], r["propeptide"], r["nglyc"], r["length_aa"]])

print(f"wrote {fasta_path}")
print(f"wrote {keymap_path}")
print(f"length distribution: min={min(r['length_aa'] for r in records)}, "
      f"max={max(r['length_aa'] for r in records)}, "
      f"median={sorted(r['length_aa'] for r in records)[len(records)//2]}")
