#!/usr/bin/env python3
"""
comp-030 step 3: N-of-5 >= 4 concordance reranking with ESM2 pseudo-pLDDT.

Joins Models 1-4 (from analyze.py: CAI, ViennaRNA MFE, chaperone load, promoter-SP prior)
with Model 5 (ESM2 pseudo-pLDDT from run_esm2.py) to compute final N-of-5 concordance.

Concordance gate: N-of-5 >= 4 (80%) -- same as comp-022 v2.
Each candidate gets a top-quintile flag per model (1 if top 20%).
Candidates with concordance_n >= 4 are promoted to the shortlist.

Unique cassette deduplication:
  After concordance, collapse by (promoter, sp, codon, scaffold_base, propeptide, nglyc)
  to remove duplicates across the 43,200-candidate space that share the same unique design.
  (For DAF SCR1-4 there is no propeptide/nglyc degeneracy issue like N191Q in uricase
  -- the design choices are explicit dimensions of the scoring space.)

Outputs:
  results/shortlist_n5ge4.csv       -- cassettes passing N-of-5 >= 4
  results/shortlist_n5eq5.csv       -- strictest tier (all 5 models top quintile)
  results/top25.md                  -- markdown top-25 table
  results/final_summary.json        -- headline numbers

Author: Open Enzyme (comp-030)
Date:   2026-05-15
"""

import csv
import json
import math
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent.parent
INPUTS = HERE / "inputs"
RESULTS = HERE / "results"

# ---------------------------------------------------------------------------
# Load pre-ESM2 candidate scores (from analyze.py)
# ---------------------------------------------------------------------------

print("Loading pre-ESM2 candidate scores...")
candidates = []
with (RESULTS / "all_candidates_scores.csv").open() as f:
    rdr = csv.DictReader(f)
    for row in rdr:
        for k in ["cai", "mfe", "chaperone_load", "promoter_sp_prior"]:
            row[k] = float(row[k])
        for k in ["concordance_n4", "top20_cai", "top20_mfe",
                  "top20_chaperone_load", "top20_promoter_sp_prior"]:
            row[k] = int(row[k])
        candidates.append(row)
print(f"  Loaded {len(candidates)} candidates.")

# ---------------------------------------------------------------------------
# Load ESM2 pseudo-pLDDT scores (from run_esm2.py)
# ---------------------------------------------------------------------------

print("\nLoading ESM2 pseudo-pLDDT scores...")
esm_by_key = {}   # (sp, scaffold_base, propeptide, nglyc) -> pseudo_pLDDT
esm_raw = {}      # same key -> raw_pll_mean
with (RESULTS / "esm2_pseudo_pLDDT.csv").open() as f:
    rdr = csv.DictReader(f)
    for row in rdr:
        k = (row["sp"], row["scaffold_base"], row["propeptide"], row["nglyc"])
        esm_by_key[k] = float(row["pseudo_pLDDT"])
        esm_raw[k] = float(row["raw_pll_mean"])
print(f"  Loaded ESM2 scores for {len(esm_by_key)} protein-distinct keys.")

# Attach ESM2 to candidates
n_missing = 0
for c in candidates:
    k = (c["sp"], c["scaffold_base"], c["propeptide"], c["nglyc"])
    if k in esm_by_key:
        c["esm_pLDDT"] = esm_by_key[k]
        c["esm_pll_raw"] = esm_raw[k]
    else:
        # Should not happen if run_esm2.py covered all protein keys
        c["esm_pLDDT"] = 65.0  # fallback: below top-quintile for any reasonable distribution
        c["esm_pll_raw"] = -1.0
        n_missing += 1
if n_missing:
    print(f"  WARNING: {n_missing} candidates had no ESM2 score; assigned fallback pLDDT=65.")

# ---------------------------------------------------------------------------
# Assign top-quintile flags for ESM2 (Model 5)
# Computed on full 43,200-cohort (since run_esm2 scored all protein-distinct combos)
# ---------------------------------------------------------------------------

def assign_top20(items, key, higher_better=True):
    n = len(items)
    cutoff_idx = max(1, n // 5)
    sorted_vals = sorted([x[key] for x in items], reverse=higher_better)
    cutoff = sorted_vals[cutoff_idx - 1]
    flag_key = f"top20_{key}"
    for item in items:
        if higher_better:
            item[flag_key] = 1 if item[key] >= cutoff else 0
        else:
            item[flag_key] = 1 if item[key] <= cutoff else 0
    return cutoff

# Use raw pll (rank-preserving) for top20 computation, not the rescaled pseudo_pLDDT
esm_cut_raw = assign_top20(candidates, "esm_pll_raw", higher_better=True)
# Also compute on rescaled for reporting
esm_cut_pLDDT = None
vals_pLDDT = sorted([c["esm_pLDDT"] for c in candidates], reverse=True)
esm_cut_pLDDT = vals_pLDDT[max(1, len(candidates)//5) - 1]
print(f"ESM2 top-quintile cutoff: raw pll >= {esm_cut_raw:.4f} (pseudo-pLDDT >= {esm_cut_pLDDT:.1f})")

# Rename flag for consistency with N-of-5 computation
for c in candidates:
    c["top20_esm"] = c["top20_esm_pll_raw"]

# ---------------------------------------------------------------------------
# N-of-5 concordance
# ---------------------------------------------------------------------------

for c in candidates:
    c["concordance_n5"] = (c["top20_cai"] + c["top20_mfe"] + c["top20_chaperone_load"] +
                           c["top20_promoter_sp_prior"] + c["top20_esm"])

conc_dist = Counter(c["concordance_n5"] for c in candidates)
print("\nN-of-5 concordance distribution (final, all 43,200 candidates):")
for n in sorted(conc_dist.keys(), reverse=True):
    pct = 100 * conc_dist[n] / len(candidates)
    print(f"  N-of-5 = {n}: {conc_dist[n]:6d} ({pct:.1f}%)")

# ---------------------------------------------------------------------------
# Composite score (5-model min-max normalized mean)
# ---------------------------------------------------------------------------

def normalize_field(items, key, higher_better=True):
    vals = [x[key] for x in items]
    lo, hi = min(vals), max(vals)
    span = hi - lo if hi > lo else 1.0
    nk = f"norm_{key}"
    for x in items:
        v = (x[key] - lo) / span
        x[nk] = v if higher_better else 1.0 - v

normalize_field(candidates, "cai", True)
normalize_field(candidates, "mfe", True)
normalize_field(candidates, "chaperone_load", False)
normalize_field(candidates, "promoter_sp_prior", True)
normalize_field(candidates, "esm_pLDDT", True)

for c in candidates:
    c["composite_v1"] = (c["norm_cai"] + c["norm_mfe"] + c["norm_chaperone_load"] +
                          c["norm_promoter_sp_prior"] + c["norm_esm_pLDDT"]) / 5.0

# ---------------------------------------------------------------------------
# Shortlists
# ---------------------------------------------------------------------------

shortlist_n5ge4 = [c for c in candidates if c["concordance_n5"] >= 4]
shortlist_n5ge4.sort(key=lambda c: (-c["concordance_n5"], -c["composite_v1"]))

shortlist_n5eq5 = [c for c in candidates if c["concordance_n5"] == 5]
shortlist_n5eq5.sort(key=lambda c: -c["composite_v1"])

print(f"\nShortlist N-of-5 >= 4: {len(shortlist_n5ge4)} candidates")
print(f"Strict tier N-of-5 = 5: {len(shortlist_n5eq5)} candidates")

# Unique cassette designs (collapse promoter for architecture analysis since promoter
# doesn't change the SP/codon/scaffold architecture):
unique_arch = {}
for c in shortlist_n5ge4:
    arch_key = (c["sp"], c["codon"], c["scaffold_base"], c["propeptide"], c["nglyc"])
    if arch_key not in unique_arch or c["composite_v1"] > unique_arch[arch_key]["composite_v1"]:
        unique_arch[arch_key] = c
unique_designs = sorted(unique_arch.values(), key=lambda c: (-c["concordance_n5"], -c["composite_v1"]))

print(f"Unique architecture designs in N-of-5 >= 4 shortlist: {len(unique_designs)}")

# ---------------------------------------------------------------------------
# Did the §1.25 baseline architecture survive?
# §1.25 baseline: PamyB + amyB SP + direct secretion + A. oryzae codon-optimized
# (per validation-experiments.md §1.25 cassette design)
# ---------------------------------------------------------------------------

def is_1_25_baseline(c):
    """§1.25 baseline: PamyB + amyB SP (or amyB_pro) + direct secretion + no propeptide."""
    return (c["promoter"] == "PamyB"
            and c["sp"] in ("SPamyB", "SPamyB_pro")
            and "direct" in c["scaffold_base"]
            and c["propeptide"] == "none")

baseline_in_shortlist = [c for c in shortlist_n5ge4 if is_1_25_baseline(c)]
print(f"\n§1.25 baseline (PamyB + amyB-SP + direct + no propeptide) in N-of-5 >= 4: {len(baseline_in_shortlist)}")
if baseline_in_shortlist:
    best_baseline = max(baseline_in_shortlist, key=lambda c: c["composite_v1"])
    print(f"  Best baseline candidate: {best_baseline['promoter']} | {best_baseline['sp']} | "
          f"{best_baseline['codon']} | {best_baseline['scaffold_base']} | "
          f"composite={best_baseline['composite_v1']:.3f} | N-of-5={best_baseline['concordance_n5']}")

# Top cluster definition (to check if a different architecture wins)
def is_top_cluster(c):
    return (c["concordance_n5"] >= 4 and
            c["top20_cai"] == 1 and
            c["top20_mfe"] == 1 and
            c["top20_chaperone_load"] == 1 and
            c["top20_promoter_sp_prior"] == 1 and
            c["top20_esm"] == 1)

top_cluster_n5eq5 = [c for c in candidates if is_top_cluster(c)]
print(f"\nTop cluster (N-of-5 = 5, all 5 models top quintile): {len(top_cluster_n5eq5)}")
if top_cluster_n5eq5:
    top5 = sorted(top_cluster_n5eq5, key=lambda c: -c["composite_v1"])[:5]
    print(f"\nTop-5 cassettes (N-of-5 = 5, by composite score):")
    for i, c in enumerate(top5, 1):
        print(f"  {i}. {c['promoter']} | {c['sp']} | {c['codon']} | {c['scaffold_base']} | "
              f"CAI={c['cai']:.3f} | MFE={c['mfe']:.1f} | chap={c['chaperone_load']:.2f} | "
              f"prior={c['promoter_sp_prior']:.3f} | pLDDT={c['esm_pLDDT']:.1f} | "
              f"N5={c['concordance_n5']} | comp={c['composite_v1']:.3f}")

# ---------------------------------------------------------------------------
# Write outputs
# ---------------------------------------------------------------------------

# shortlist_n5ge4.csv
csv_fields = ["promoter", "sp", "codon", "scaffold_base", "propeptide", "nglyc",
              "cai", "mfe", "chaperone_load", "promoter_sp_prior", "esm_pLDDT",
              "top20_cai", "top20_mfe", "top20_chaperone_load",
              "top20_promoter_sp_prior", "top20_esm",
              "concordance_n5", "composite_v1"]

with (RESULTS / "shortlist_n5ge4.csv").open("w") as f:
    w = csv.writer(f)
    w.writerow(csv_fields)
    for c in shortlist_n5ge4:
        row = []
        for k in csv_fields:
            v = c.get(k, "")
            if isinstance(v, float):
                row.append(f"{v:.4f}")
            else:
                row.append(str(v))
        w.writerow(row)
print(f"\nWrote {len(shortlist_n5ge4)} rows to shortlist_n5ge4.csv")

with (RESULTS / "shortlist_n5eq5.csv").open("w") as f:
    w = csv.writer(f)
    w.writerow(csv_fields)
    for c in shortlist_n5eq5:
        row = []
        for k in csv_fields:
            v = c.get(k, "")
            if isinstance(v, float):
                row.append(f"{v:.4f}")
            else:
                row.append(str(v))
        w.writerow(row)
print(f"Wrote {len(shortlist_n5eq5)} rows to shortlist_n5eq5.csv")

# top25.md
with (RESULTS / "top25.md").open("w") as f:
    f.write("# comp-030 Top-25 cassettes (N-of-5 >= 4 concordance)\n\n")
    f.write(f"Run date: 2026-05-15\n\n")
    f.write(f"Target: DAF/CD55 SCR1-4 (aa 35-285, UniProt P08174, 8 disulfide bonds)\n\n")
    f.write(f"N-of-5 >= 4 shortlist: **{len(shortlist_n5ge4)}** candidates | ")
    f.write(f"Strictest tier (N-of-5 = 5): **{len(shortlist_n5eq5)}** candidates\n\n")
    f.write(f"§1.25 baseline (PamyB + amyB-SP + direct + no propeptide) in N-of-5 >= 4: ")
    f.write(f"**{len(baseline_in_shortlist)}** candidates\n\n")
    f.write("| Rank | Promoter | SP | Codon | Scaffold | Prop | N-glyc | CAI | MFE | ChapLoad | Prior | pLDDT | N-of-5 | Composite |\n")
    f.write("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
    for i, c in enumerate(shortlist_n5ge4[:25], 1):
        f.write(f"| {i} | {c['promoter']} | {c['sp']} | {c['codon']} | {c['scaffold_base']} "
                f"| {c['propeptide']} | {c['nglyc']} | {c['cai']:.3f} | {c['mfe']:.1f} "
                f"| {c['chaperone_load']:.2f} | {c['promoter_sp_prior']:.3f} | {c['esm_pLDDT']:.1f} "
                f"| {c['concordance_n5']} | {c['composite_v1']:.3f} |\n")

print(f"Wrote top-25 to {RESULTS / 'top25.md'}")

# Load alpha-coefficient check from ESM2 step
alpha_check = {}
alpha_check_path = RESULTS / "alpha_coefficient_check.json"
if alpha_check_path.exists():
    with alpha_check_path.open() as f:
        alpha_check = json.load(f)

# final_summary.json
summary = {
    "experiment_id": "comp-030",
    "target": "DAF/CD55 SCR1-4 (aa 35-285, UniProt P08174)",
    "date": "2026-05-15",
    "design_space_total": len(candidates),
    "design_space_factorization": "6 promoters x 12 SP x 10 codon variants x 60 scaffolds = 43,200",
    "concordance_distribution": {str(k): v for k, v in conc_dist.items()},
    "shortlist_n5ge4_size": len(shortlist_n5ge4),
    "shortlist_n5eq5_size": len(shortlist_n5eq5),
    "unique_architectures_in_n5ge4": len(unique_designs),
    "baseline_1_25_survival_in_n5ge4": len(baseline_in_shortlist),
    "baseline_1_25_description": "PamyB + amyB SP + direct secretion + any codon variant + no propeptide",
    "top_cluster_n5eq5": [
        {"rank": i+1,
         "promoter": c["promoter"], "sp": c["sp"], "codon": c["codon"],
         "scaffold_base": c["scaffold_base"], "propeptide": c["propeptide"],
         "nglyc": c["nglyc"],
         "cai": c["cai"], "mfe": c["mfe"], "chaperone_load": c["chaperone_load"],
         "promoter_sp_prior": c["promoter_sp_prior"], "esm_pLDDT": c["esm_pLDDT"],
         "concordance_n5": c["concordance_n5"], "composite_v1": c["composite_v1"]}
        for i, c in enumerate(sorted(shortlist_n5eq5, key=lambda c: -c["composite_v1"])[:10])
    ],
    "alpha_coefficient_check": alpha_check,
    "five_model_cutoffs": {
        "cai": None,  # loaded below from pre-ESM2 summary
        "mfe": None,
        "chaperone_load": None,
        "promoter_sp_prior": None,
        "esm_pll_raw_top20": esm_cut_raw,
        "esm_pseudo_pLDDT_top20": esm_cut_pLDDT,
    },
}

# Load cutoffs from pre-ESM2 summary
pre_sum_path = RESULTS / "summary_pre_esm2.json"
if pre_sum_path.exists():
    with pre_sum_path.open() as f:
        pre_sum = json.load(f)
    summary["five_model_cutoffs"].update(pre_sum.get("models_1_to_4_cutoffs", {}))

with (RESULTS / "final_summary.json").open("w") as f:
    json.dump(summary, f, indent=2)
print(f"Wrote final summary to {RESULTS / 'final_summary.json'}")

print("\n" + "=" * 60)
print("COMP-030 HEADLINE RESULTS")
print("=" * 60)
print(f"Design space:           {len(candidates)} candidates (43,200)")
print(f"N-of-5 >= 4 shortlist:  {len(shortlist_n5ge4)}")
print(f"N-of-5 = 5 strict:      {len(shortlist_n5eq5)}")
print(f"§1.25 baseline in N5:   {len(baseline_in_shortlist)}")
if alpha_check:
    verdict = alpha_check.get("alpha_coefficient_check_verdict", "not computed")
    mean_p = alpha_check.get("overall_pLDDT", {}).get("mean", "N/A")
    print(f"pLDDT mean (all):       {mean_p:.1f}" if isinstance(mean_p, float) else f"pLDDT mean: {mean_p}")
    print(f"Alpha-coeff verdict:    {verdict}")
print("=" * 60)
print("All outputs in experiments/comp-030-daf-cassette-ranking/results/")
EOF
