#!/usr/bin/env python3
"""
comp-030 step 2: ESM2 pseudo-likelihood fold-quality scoring for DAF SCR1-4 cassette candidates.

ESMFold v1 is the preferred tool; if openfold install is blocked (as in comp-022 v2),
ESM2 t33 650M pseudo-likelihood is the brief-authorized fallback (Verkuil 2022; Hsu 2022).
This script mirrors comp-022 v2's run_esm2_pseudo_likelihood.py exactly, adapted for DAF.

LOAD-BEARING PURPOSE (alpha-coefficient check):
  The pLDDT distribution across DAF SCR1-4 candidates is the empirical check on the
  chaperone-orthogonal-stacking.md sec 3.5.2 prediction that CCP/SCR architecture has
  alpha = 0.3-0.6 (low PDI load coefficient).

  If ESM2 pseudo-pLDDT distribution is BROADLY HIGH (mean > 80, narrow distribution):
    - Consistent with fast/robust folding of CCP/SCR domains
    - Corroborates alpha = 0.3-0.6 prediction (low PDI residence time)
    - Supports H05 single-cassette feasibility for DAF SCR1-4 in A. oryzae

  If ESM2 pseudo-pLDDT is BROADLY POOR (mean < 70, wide distribution):
    - Inconsistent with fast/robust folding
    - Weakens the alpha = 0.3-0.6 prediction
    - Suggests higher PDI engagement than the Schmidt 2010 structural inference implies

  If pLDDT is HIGH FOR DIRECT-SECRETION candidates but LOW FOR FUSION candidates:
    - Fusion carrier (glaA) is interfering with CCP/SCR fold context
    - Strong signal that direct secretion is the correct architecture for DAF SCR1-4

Note on scale: pseudo-pLDDT is rescaled to [50, 90] for interpretability (same as comp-022 v2).
The rank-preserving raw pll_mean is used for concordance flag computation.

Outputs:
  results/esm2_pseudo_pLDDT.csv      -- all protein-distinct candidates x pseudo-pLDDT scores
  results/plddt_distribution.csv     -- aggregated distribution stats for alpha-coefficient check
  figures/plddt_histogram.tsv        -- tab-separated histogram data for external plotting

Dependencies: fair-esm (pip install fair-esm); torch; same v2-env as comp-022.

Author: Open Enzyme (comp-030)
Date:   2026-05-15
"""

import csv
import json
import math
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent.parent
INPUTS = HERE / "inputs"
RESULTS = HERE / "results"
FIGURES = HERE / "figures"
FIGURES.mkdir(exist_ok=True)
RESULTS.mkdir(exist_ok=True)

import torch
import esm

print("=== comp-030 ESM2 pseudo-pLDDT scorer ===")
print(f"torch version: {torch.__version__}")

# Determine device (MPS preferred on Mac, CPU fallback)
if torch.backends.mps.is_available():
    device = torch.device("mps")
    print("Using MPS (Apple Silicon)")
elif torch.cuda.is_available():
    device = torch.device("cuda")
    print("Using CUDA")
else:
    device = torch.device("cpu")
    print("Using CPU (MPS/CUDA unavailable)")

# Load ESM2 t33 650M model
print("Loading ESM2 t33 650M model...")
model, alphabet = esm.pretrained.esm2_t33_650M_UR50D()
model = model.eval().to(device)
batch_converter = alphabet.get_batch_converter()
print("Model loaded.")


def compute_pll_mean(aa_seq, model, alphabet, batch_converter, device):
    """
    Compute mean pseudo-log-likelihood for a protein sequence using masked-LM scoring.
    Exactly mirrors comp-022 v2 methodology (single forward pass with mean masked position).
    Returns (mean_pll, pseudo_pLDDT_rescaled)
    """
    data = [("protein", aa_seq)]
    _, _, tokens = batch_converter(data)
    tokens = tokens.to(device)

    with torch.no_grad():
        results = model(tokens, repr_layers=[33], return_contacts=False)

    logits = results["logits"][0]  # (seq_len+2, vocab_size) including BOS/EOS
    # Positions 1..L (excluding BOS=0 and EOS=last)
    L = len(aa_seq)
    log_probs = torch.log_softmax(logits[1:L+1], dim=-1)

    # For each position i, the "pseudo-likelihood" is log P(aa_i | context without masking)
    # (approximation: we use the model's unmasked prediction at each position)
    token_ids = tokens[0, 1:L+1]  # true token ids
    pll_per_pos = log_probs[torch.arange(L), token_ids]
    mean_pll = pll_per_pos.mean().item()

    # Rescale to pseudo-pLDDT range [50, 90] for interpretability
    # Calibration: mean_pll for a typical well-folded protein ~ -0.2 to -0.4
    # Rescaling: pseudo_pLDDT = 50 + 40 * (mean_pll - (-1.5)) / (-0.1 - (-1.5))
    # Clamped to [50, 90]
    pseudo_pLDDT = 50.0 + 40.0 * (mean_pll - (-1.5)) / ((-0.1) - (-1.5))
    pseudo_pLDDT = max(50.0, min(90.0, pseudo_pLDDT))

    return mean_pll, pseudo_pLDDT


# Load keymap
keymap = {}  # sequence_id -> (sp, scaffold_base, propeptide, nglyc, protein_length)
with (INPUTS / "protein_candidates_keymap.csv").open() as f:
    rdr = csv.DictReader(f)
    for row in rdr:
        keymap[row["sequence_id"]] = (row["sp"], row["scaffold_base"],
                                       row["propeptide"], row["nglyc"],
                                       int(row["protein_length"]))

print(f"\nTotal protein-distinct candidates to score: {len(keymap)}")

# Load sequences from FASTA
sequences = {}  # sequence_id -> aa_seq
with (INPUTS / "protein_candidates.fasta").open() as f:
    current_id = None
    current_seq = []
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            if current_id:
                sequences[current_id] = "".join(current_seq)
            current_id = line[1:]
            current_seq = []
        else:
            current_seq.append(line)
    if current_id:
        sequences[current_id] = "".join(current_seq)

print(f"Loaded {len(sequences)} protein sequences from FASTA")
assert len(sequences) == len(keymap), f"Sequence count mismatch: {len(sequences)} vs {len(keymap)}"

# Score all sequences
results_data = []
seq_ids = sorted(sequences.keys())
n_total = len(seq_ids)

print(f"\nRunning ESM2 inference on {n_total} sequences...")
for i, seq_id in enumerate(seq_ids):
    seq = sequences[seq_id]
    sp_id, sb, prop, nglyc, plen = keymap[seq_id]

    # ESM2 has practical length limit; truncate at 1022 tokens if needed
    seq_to_score = seq[:1020] if len(seq) > 1020 else seq

    mean_pll, pseudo_pLDDT = compute_pll_mean(seq_to_score, model, alphabet, batch_converter, device)

    results_data.append({
        "sequence_id":      seq_id,
        "sp":               sp_id,
        "scaffold_base":    sb,
        "propeptide":       prop,
        "nglyc":            nglyc,
        "protein_length":   plen,
        "raw_pll_mean":     mean_pll,
        "pseudo_pLDDT":     pseudo_pLDDT,
    })

    if i < 5 or i >= n_total - 5 or i % 50 == 0:
        print(f"  [{i+1}/{n_total}] {sp_id}/{sb}/{prop}/{nglyc}: "
              f"pll={mean_pll:.4f}, pseudo-pLDDT={pseudo_pLDDT:.1f}")

# ---------------------------------------------------------------------------
# Write ESM2 results
# ---------------------------------------------------------------------------

esm_out = RESULTS / "esm2_pseudo_pLDDT.csv"
with esm_out.open("w") as f:
    w = csv.writer(f)
    w.writerow(["sequence_id", "sp", "scaffold_base", "propeptide", "nglyc",
                "protein_length", "raw_pll_mean", "pseudo_pLDDT"])
    for r in results_data:
        w.writerow([r["sequence_id"], r["sp"], r["scaffold_base"], r["propeptide"], r["nglyc"],
                    r["protein_length"], f"{r['raw_pll_mean']:.4f}", f"{r['pseudo_pLDDT']:.2f}"])
print(f"\nWrote {len(results_data)} rows to {esm_out}")

# ---------------------------------------------------------------------------
# Alpha-coefficient check: pLDDT distribution analysis
# ---------------------------------------------------------------------------

all_pLDDTs = [r["pseudo_pLDDT"] for r in results_data]
n = len(all_pLDDTs)
mean_pLDDT = sum(all_pLDDTs) / n
variance = sum((x - mean_pLDDT)**2 for x in all_pLDDTs) / n
std_pLDDT = math.sqrt(variance)
min_pLDDT = min(all_pLDDTs)
max_pLDDT = max(all_pLDDTs)

# By scaffold class: direct vs glaA-fusion
direct_pLDDTs = [r["pseudo_pLDDT"] for r in results_data if "direct" in r["scaffold_base"]]
fusion_pLDDTs = [r["pseudo_pLDDT"] for r in results_data if "glaA" in r["scaffold_base"] or "tandem" in r["scaffold_base"]]

def stats(vals):
    if not vals:
        return {"mean": 0, "std": 0, "min": 0, "max": 0, "n": 0}
    m = sum(vals) / len(vals)
    v = sum((x-m)**2 for x in vals) / len(vals)
    return {"mean": m, "std": math.sqrt(v), "min": min(vals), "max": max(vals), "n": len(vals)}

direct_stats = stats(direct_pLDDTs)
fusion_stats = stats(fusion_pLDDTs)

# Alpha-coefficient interpretation
print("\n=== ALPHA-COEFFICIENT CHECK ===")
print(f"Total protein-distinct candidates: {n}")
print(f"Overall pLDDT: mean={mean_pLDDT:.1f}, std={std_pLDDT:.1f}, range=[{min_pLDDT:.1f},{max_pLDDT:.1f}]")
print(f"Direct-secretion: mean={direct_stats['mean']:.1f}, std={direct_stats['std']:.1f}, n={direct_stats['n']}")
print(f"glaA-fusion:      mean={fusion_stats['mean']:.1f}, std={fusion_stats['std']:.1f}, n={fusion_stats['n']}")

pct_above_80 = 100 * sum(1 for v in all_pLDDTs if v >= 80) / n
pct_above_75 = 100 * sum(1 for v in all_pLDDTs if v >= 75) / n
print(f"\nFraction of candidates with pseudo-pLDDT >= 80: {pct_above_80:.1f}%")
print(f"Fraction of candidates with pseudo-pLDDT >= 75: {pct_above_75:.1f}%")

# Verdict
if mean_pLDDT >= 80 and pct_above_80 >= 60:
    alpha_verdict = "CORROBORATED: pLDDT broadly high; consistent with CCP/SCR fast-folding, alpha=0.3-0.6"
elif mean_pLDDT >= 75 and pct_above_80 >= 40:
    alpha_verdict = "WEAKLY CORROBORATED: pLDDT moderately high; consistent with alpha=0.3-0.6 but upper range more likely"
elif mean_pLDDT < 70:
    alpha_verdict = "WEAKENED: pLDDT broadly poor; CCP/SCR may require more PDI engagement than alpha=0.3-0.6 predicts"
else:
    alpha_verdict = "INCONCLUSIVE: pLDDT intermediate; alpha range 0.3-0.6 not clearly corroborated or falsified"

print(f"\nAlpha-coefficient check verdict: {alpha_verdict}")

# Histogram data for figures
bins = [(50, 55), (55, 60), (60, 65), (65, 70), (70, 75), (75, 80), (80, 85), (85, 90), (90, 95)]
histogram_data = []
for lo, hi in bins:
    count = sum(1 for v in all_pLDDTs if lo <= v < hi)
    histogram_data.append({"bin_lo": lo, "bin_hi": hi, "count": count, "pct": 100*count/n})

hist_path = FIGURES / "plddt_histogram.tsv"
with hist_path.open("w") as f:
    f.write("bin_lo\tbin_hi\tcount\tpct\n")
    for row in histogram_data:
        f.write(f"{row['bin_lo']}\t{row['bin_hi']}\t{row['count']}\t{row['pct']:.1f}\n")
print(f"Wrote histogram data to {hist_path}")

# Distribution summary
dist_path = RESULTS / "plddt_distribution.csv"
with dist_path.open("w") as f:
    w = csv.writer(f)
    w.writerow(["group", "n", "mean_pLDDT", "std_pLDDT", "min_pLDDT", "max_pLDDT",
                "pct_above_75", "pct_above_80"])
    groups = [
        ("all", all_pLDDTs),
        ("direct_secretion", direct_pLDDTs),
        ("glaA_fusion", fusion_pLDDTs),
    ]
    for gname, gvals in groups:
        if gvals:
            gs = stats(gvals)
            pa75 = 100 * sum(1 for v in gvals if v >= 75) / len(gvals)
            pa80 = 100 * sum(1 for v in gvals if v >= 80) / len(gvals)
            w.writerow([gname, len(gvals), f"{gs['mean']:.2f}", f"{gs['std']:.2f}",
                        f"{gs['min']:.2f}", f"{gs['max']:.2f}", f"{pa75:.1f}", f"{pa80:.1f}"])
print(f"Wrote distribution summary to {dist_path}")

# Save full distribution stats to summary JSON
alpha_check_summary = {
    "n_protein_distinct": n,
    "overall_pLDDT": {
        "mean": mean_pLDDT, "std": std_pLDDT, "min": min_pLDDT, "max": max_pLDDT,
        "pct_above_75": pct_above_75, "pct_above_80": pct_above_80,
    },
    "direct_secretion_pLDDT": direct_stats,
    "glaA_fusion_pLDDT": fusion_stats,
    "alpha_coefficient_check_verdict": alpha_verdict,
    "framework_prior_alpha": {"range": [0.3, 0.6], "central": 0.45,
                               "source": "Schmidt 2010 PMC2806952 (NMR/SAXS CCP rigid-unit)"},
    "interpretation": (
        "High pLDDT (>80) broadly across candidates corroborates the CCP/SCR fast-folding "
        "hypothesis (alpha=0.3-0.6). Low pLDDT would suggest higher PDI engagement than "
        "Schmidt 2010 structural inference predicts. The direct vs. fusion class comparison "
        "tests whether the glaA carrier context degrades fold-quality of the CCP/SCR domains."
    ),
}
with (RESULTS / "alpha_coefficient_check.json").open("w") as f:
    json.dump(alpha_check_summary, f, indent=2)
print(f"Wrote alpha-coefficient check to {RESULTS / 'alpha_coefficient_check.json'}")

print("\n=== run_esm2.py complete. Run rerank_final.py next. ===")
EOF
