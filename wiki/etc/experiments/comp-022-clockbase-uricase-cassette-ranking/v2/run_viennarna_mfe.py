#!/usr/bin/env python3
"""
comp-022 v2 step 4: ViennaRNA MFE on the 5' translation-initiation region.

For each unique (codon_variant, signal_peptide) pair in the v1 shortlist:
  - Construct the mRNA = generic 5'UTR + signal_peptide ORF + first 30 codons of uricase
  - Run RNA.fold (ViennaRNA Python binding) to get minimum-free-energy structure
  - Record MFE in kcal/mol (folded RNA has negative MFE)
  - Compute a 5p_softening_metric = MFE_per_nucleotide (more negative = more structure)

Output: outputs/viennarna_mfe.csv

Also computes the v1 GC-clamp proxy on the same sequence, so we can compute a
Spearman correlation between v1 proxy and real MFE in analyze_v2.py.
"""

import csv
import json
import random
from pathlib import Path

import RNA  # ViennaRNA

HERE = Path(__file__).parent
V1_DIR = HERE.parent
V1_INPUTS = V1_DIR / "inputs"
V1_OUTPUTS = V1_DIR / "outputs"
V2_OUTPUTS = HERE / "outputs"
V2_OUTPUTS.mkdir(parents=True, exist_ok=True)

# Load codon table + parts + sequence
with (V1_INPUTS / "parts_list.json").open() as f:
    PARTS = json.load(f)
with (V1_INPUTS / "a_oryzae_codon_usage.json").open() as f:
    CODON_TABLE = json.load(f)

def load_fasta(path):
    seq = []
    with open(path) as f:
        for line in f:
            if line.startswith(">"):
                continue
            seq.append(line.strip())
    return "".join(seq)

URICASE_AA = load_fasta(V1_INPUTS / "Q00511.fasta")
assert len(URICASE_AA) == 302

# Build AA -> codons lookup (mirrors v1's analyze.py)
AA_TO_CODONS = {}
for codon, info in CODON_TABLE["codons"].items():
    aa = info["aa"]
    if aa == "*":
        continue
    AA_TO_CODONS.setdefault(aa, []).append((codon, info["rscu"], info["freq_per1000"]))
for aa in AA_TO_CODONS:
    AA_TO_CODONS[aa].sort(key=lambda c: -c[1])

# --- Codon back-translators (must match v1 analyze.py logic) ---

def codon_gc(c):
    return sum(1 for x in c if x in "GC") / 3.0

def bt_native_flavus(aa_seq, seed=46):
    rng = random.Random(seed)
    out = []
    for aa in aa_seq:
        codons = AA_TO_CODONS[aa]
        if len(codons) >= 3:
            idx = rng.randint(1, min(3, len(codons) - 1))
            out.append(codons[idx][0])
        elif len(codons) >= 2:
            out.append(codons[1][0])
        else:
            out.append(codons[0][0])
    return "".join(out)

def bt_max_cai(aa_seq):
    return "".join(AA_TO_CODONS[aa][0][0] for aa in aa_seq)

def bt_balanced(aa_seq, seed=42):
    rng = random.Random(seed)
    out = []
    for aa in aa_seq:
        codons = AA_TO_CODONS[aa]
        out.append(rng.choices([c[0] for c in codons], weights=[c[1] for c in codons], k=1)[0])
    return "".join(out)

def bt_max_cai_gc54(aa_seq):
    out = []
    for i, aa in enumerate(aa_seq):
        codons = AA_TO_CODONS[aa]
        ws = max(0, i - 29)
        local = out[ws:i]
        lg = sum(codon_gc(c) for c in local)
        chosen = None
        for codon, _, _ in codons:
            wg = (lg + codon_gc(codon)) / (len(local) + 1)
            if wg <= 0.54:
                chosen = codon
                break
        if chosen is None:
            chosen = min(codons, key=lambda c: codon_gc(c[0]))[0]
        out.append(chosen)
    return "".join(out)

def bt_harmonized(aa_seq, seed=43):
    rng = random.Random(seed)
    out = []
    for aa in aa_seq:
        codons = AA_TO_CODONS[aa]
        if len(codons) == 1:
            out.append(codons[0][0])
        else:
            idx = min(len(codons) - 1, rng.randint(0, min(2, len(codons) - 1)))
            out.append(codons[idx][0])
    return "".join(out)

def bt_rare_avoid(aa_seq, seed=44):
    rng = random.Random(seed)
    out = []
    for aa in aa_seq:
        codons = [c for c in AA_TO_CODONS[aa] if c[1] >= 0.4]
        if not codons:
            codons = AA_TO_CODONS[aa]
        out.append(rng.choices([c[0] for c in codons], weights=[c[1] for c in codons], k=1)[0])
    return "".join(out)

def bt_low_gc(aa_seq):
    out = []
    for aa in aa_seq:
        chosen = min(AA_TO_CODONS[aa], key=lambda c: (codon_gc(c[0]), -c[1]))
        out.append(chosen[0])
    return "".join(out)

def bt_high_gc(aa_seq):
    out = []
    for aa in aa_seq:
        chosen = max(AA_TO_CODONS[aa], key=lambda c: (codon_gc(c[0]), c[1]))
        out.append(chosen[0])
    return "".join(out)

def bt_5p_softened(aa_seq, n_soft=30):
    return bt_low_gc(aa_seq[:n_soft]) + bt_max_cai(aa_seq[n_soft:])

def bt_5p_softened_balanced(aa_seq, n_soft=30, seed=45):
    return bt_low_gc(aa_seq[:n_soft]) + bt_balanced(aa_seq[n_soft:], seed=seed)

BACK_TRANSLATORS = {
    "native_uaZ":           bt_native_flavus,
    "cai_max":              bt_max_cai,
    "cai_balanced":         bt_balanced,
    "cai_max_gc54":         bt_max_cai_gc54,
    "harmonized":           bt_harmonized,
    "rare_avoid":           bt_rare_avoid,
    "low_gc":               bt_low_gc,
    "high_gc":              bt_high_gc,
    "5p_softened":          bt_5p_softened,
    "5p_softened_balanced": bt_5p_softened_balanced,
}

# Generic 5'UTR (60 nt, A/T-rich, A. oryzae context; not promoter-specific by design).
# This is a minimal viable 5'UTR that mimics the Kozak-distal region; absolute MFE depends
# on this sequence but the ranking across cassettes is preserved since the same 5'UTR is
# used for all.
GENERIC_5UTR = "AAATATTACACAACATCACATAAATCAACCATCATCATAAACTAATCATCAATCATCAATC"
assert len(GENERIC_5UTR) == 61

SP_BY_ID = {sp["id"]: sp for sp in PARTS["signal_peptides"]}

def backtranslate_sp(sp_aa, codon_id):
    """Back-translate the signal peptide using the same codon strategy as the body."""
    fn = BACK_TRANSLATORS[codon_id]
    return fn(sp_aa)

# --- v1 GC-clamp proxy (copy exactly from analyze.py) ---

def v1_proxy(nt_seq, n_5p_nt=120):
    head = nt_seq[:n_5p_nt]
    gc_count = sum(1 for c in head if c in "GC")
    gc_frac = gc_count / len(head)
    gc_score = max(0.0, 1.0 - 2.0 * max(0.0, gc_frac - 0.40))
    clamp_count = 0
    run = 0
    last = None
    for c in head:
        if c in "GC" and c == last:
            run += 1
            if run == 3:
                clamp_count += 1
        else:
            run = 1
        last = c
    clamp_score = max(0.0, 1.0 - 0.1 * clamp_count)
    complement = str.maketrans("ACGT", "TGCA")
    palindromes = 0
    for i in range(len(head) - 3):
        kmer = head[i:i+4]
        rc = kmer.translate(complement)[::-1]
        for j in range(i + 6, min(i + 50, len(head) - 3)):
            if head[j:j+4] == rc:
                palindromes += 1
                break
    palindrome_score = max(0.0, 1.0 - 0.05 * palindromes)
    return (gc_score + clamp_score + palindrome_score) / 3.0

# --- Read shortlist for unique (codon, sp) pairs ---

pairs = set()
with (V1_OUTPUTS / "unique_cassette_shortlist.csv").open() as f:
    rdr = csv.DictReader(f)
    for row in rdr:
        pairs.add((row["codon"], row["sp"]))

pairs = sorted(pairs)
print(f"Unique (codon, SP) pairs to fold: {len(pairs)}")

# --- Fold each pair's 5' region ---

rows = []
for i, (codon_id, sp_id) in enumerate(pairs):
    sp_aa = SP_BY_ID[sp_id]["sequence"]
    sp_nt = backtranslate_sp(sp_aa, codon_id)
    body_nt = BACK_TRANSLATORS[codon_id](URICASE_AA[:30])  # first 30 codons of uricase
    # mRNA = 5'UTR + SP ORF + first 30 codons of uricase
    # Use DNA alphabet, but ViennaRNA expects U; do explicit T->U conversion
    mrna_dna = GENERIC_5UTR + sp_nt + body_nt
    mrna_rna = mrna_dna.replace("T", "U")

    # Fold the first 150 nt of mRNA (5'UTR + initiation window, Kudla 2009 region)
    # If shorter, use whole sequence.
    fold_window = mrna_rna[:150]

    fc = RNA.fold_compound(fold_window)
    structure, mfe = fc.mfe()
    mfe_per_nt = mfe / len(fold_window)

    proxy = v1_proxy(mrna_dna, n_5p_nt=120)

    rows.append({
        "variant_id": f"{codon_id}__{sp_id}",
        "codon": codon_id,
        "sp": sp_id,
        "fold_window_nt": len(fold_window),
        "MFE_kcal_per_mol": mfe,
        "MFE_per_nt": mfe_per_nt,
        "v1_gc_clamp_proxy": proxy,
    })

    if i < 3 or i >= len(pairs) - 3:
        print(f"  [{i+1}/{len(pairs)}] {codon_id} x {sp_id}: MFE={mfe:.2f} kcal/mol, "
              f"per-nt={mfe_per_nt:.3f}, v1_proxy={proxy:.3f}")

# --- Write output ---

out_path = V2_OUTPUTS / "viennarna_mfe.csv"
with out_path.open("w") as f:
    w = csv.writer(f)
    w.writerow(["variant_id", "codon", "sp", "fold_window_nt",
                "MFE_kcal_per_mol", "MFE_per_nt", "v1_gc_clamp_proxy"])
    for r in rows:
        w.writerow([r["variant_id"], r["codon"], r["sp"], r["fold_window_nt"],
                    f"{r['MFE_kcal_per_mol']:.3f}", f"{r['MFE_per_nt']:.5f}",
                    f"{r['v1_gc_clamp_proxy']:.5f}"])

print(f"\nwrote {out_path}")
print(f"MFE range: {min(r['MFE_kcal_per_mol'] for r in rows):.2f} to "
      f"{max(r['MFE_kcal_per_mol'] for r in rows):.2f} kcal/mol")
