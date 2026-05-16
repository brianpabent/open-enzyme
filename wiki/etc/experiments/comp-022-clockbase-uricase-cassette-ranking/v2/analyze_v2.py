#!/usr/bin/env python3
"""
comp-022 v2 step 5: N-of-5 concordance re-ranking.

Joins the v1 per-cassette scores (CAI, chaperone load, promoter-SP prior; v1's
GC-clamp mRNA proxy is DROPPED in favor of ViennaRNA MFE) with the two v2 retrofits:

  - ESM2 pseudo-pLDDT  (fold-quality, ESMFold v1 fallback authorized by brief
                        because openfold install was blocked; rationale below)
  - ViennaRNA MFE      (5'-mRNA fold energy, real ViennaRNA 2.7.2 Python binding)

The 5 models in v2 concordance:
  1. CAI                                       (Tier 1,   higher better)
  2. ViennaRNA 5'-MFE                          (Tier 1',  higher MFE = less structure = better)
  3. Chaperone load                            (Tier 2,   lower better)
  4. Promoter x SP prior                       (Tier 4,   higher better)
  5. ESM2 pseudo-pLDDT                         (Tier 3,   higher better; fold-quality proxy)

v2 threshold: N-of-5 >= 4 (80% concordance). Tighter than v1's N-of-4 >= 3 (75%)
because we now have a real RNA fold model and a real protein language-model
fold-quality readout rather than proxies.

Why ESM2 pseudo-pLDDT instead of real ESMFold pLDDT:
  - ESMFold v1 in fair-esm 2.0.0 requires openfold; openfold install from git
    was blocked by the auto-mode classifier in this subagent env.
  - The brief explicitly authorizes ESM2 pseudo-likelihood fallback (Verkuil
    2022; Hsu 2022) as a fold-quality proxy. ESM2 is the language model that
    ESMFold uses internally; the per-residue pseudo-likelihood is a direct
    readout of the model's confidence in each residue's local fold context.
  - For RANK-ORDER comparison across cassettes (which is what concordance
    cares about), pseudo-likelihood preserves the relative ordering well.
  - We rescale ESM2 pll to a pseudo-pLDDT range [50, 90] to match the v2
    brief's expected score scale. This is a presentational rescaling and
    does NOT affect the rank-based top20 flag computation.
  - Documented as v2 simplification; v2.5 should retrofit real ESMFold once
    openfold install is unblocked.

Outputs:
  outputs/v2_shortlist.csv       cassettes passing N-of-5 >= 4
  outputs/v2_top25.md            top 25 by composite within the shortlist
  outputs/v2_summary.json        headline numbers + correlations
"""

import csv
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent
V1_DIR = HERE.parent
V1_OUTPUTS = V1_DIR / "outputs"
V2_OUTPUTS = HERE / "outputs"
V2_OUTPUTS.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Load v1 artifacts
# ---------------------------------------------------------------------------

with (V1_OUTPUTS / "report.json").open() as f:
    V1_REPORT = json.load(f)
V1_CUTOFFS = V1_REPORT["concordance_summary"]["quintile_cutoffs"]
print(f"v1 quintile cutoffs (43,200-cohort): {V1_CUTOFFS}")

# v1 shortlist: 501 unique cassettes that passed N-of-4 >= 3
v1_shortlist = []
with (V1_OUTPUTS / "unique_cassette_shortlist.csv").open() as f:
    rdr = csv.DictReader(f)
    for row in rdr:
        for k in ["cai", "mrna_5p", "chaperone_load", "promoter_sp_prior", "composite"]:
            row[k] = float(row[k])
        for k in ["concordance_n", "top20_cai", "top20_mrna_5p",
                  "top20_chaperone_load", "top20_promoter_sp_prior"]:
            row[k] = int(row[k])
        v1_shortlist.append(row)
print(f"v1 shortlist: {len(v1_shortlist)} cassettes")

# ---------------------------------------------------------------------------
# Load v2 retrofits
# ---------------------------------------------------------------------------

# ESM2 pseudo-pLDDT: keyed by sequence_id; keymap maps sequence_id -> protein-distinct tuple
keymap = {}  # sequence_id -> (sp, scaffold_base, propeptide, nglyc)
with (HERE / "inputs" / "protein_shortlist_keymap.csv").open() as f:
    rdr = csv.DictReader(f)
    for row in rdr:
        keymap[row["sequence_id"]] = (row["sp"], row["scaffold_base"], row["propeptide"], row["nglyc"])

esm_by_key = {}  # (sp, scaffold_base, propeptide, nglyc) -> pseudo_pLDDT
esm_by_key_raw = {}  # same key -> raw pll_mean (unscaled, used for top20 flag)
with (V2_OUTPUTS / "esmfold_pLDDT.csv").open() as f:
    rdr = csv.DictReader(f)
    for row in rdr:
        k = keymap[row["sequence_id"]]
        esm_by_key[k] = float(row["mean_pseudo_pLDDT"])
        esm_by_key_raw[k] = float(row["raw_pll_mean"])
print(f"loaded ESM2 pseudo-pLDDT for {len(esm_by_key)} protein-distinct keys")

# ViennaRNA MFE: keyed by (codon, sp)
mfe_by_pair = {}
proxy_by_pair = {}  # the v1 GC-clamp proxy on the same window, for sanity correlation
with (V2_OUTPUTS / "viennarna_mfe.csv").open() as f:
    rdr = csv.DictReader(f)
    for row in rdr:
        k = (row["codon"], row["sp"])
        mfe_by_pair[k] = float(row["MFE_kcal_per_mol"])
        proxy_by_pair[k] = float(row["v1_gc_clamp_proxy"])
print(f"loaded ViennaRNA MFE for {len(mfe_by_pair)} (codon, sp) pairs")

# ---------------------------------------------------------------------------
# Attach v2 scores to each shortlist row
# ---------------------------------------------------------------------------

for row in v1_shortlist:
    prot_key = (row["sp"], row["scaffold_base"], row["propeptide"], row["nglyc"])
    pair_key = (row["codon"], row["sp"])
    row["esm_pll"] = esm_by_key[prot_key]
    row["esm_pll_raw"] = esm_by_key_raw[prot_key]
    row["mfe"] = mfe_by_pair[pair_key]

# Sanity
assert all("esm_pll" in r for r in v1_shortlist)
assert all("mfe" in r for r in v1_shortlist)

# ---------------------------------------------------------------------------
# v2 top-quintile flags (on the v1 shortlist cohort, since v2 scores only
# exist for cassettes in the v1 shortlist; this is the correct scoping for
# "v2 is a tighter gate on v1 survivors").
# ---------------------------------------------------------------------------

def assign_top20(items, key, higher_better=True):
    n = len(items)
    cutoff_idx = max(1, n // 5)  # top quintile = top 20%
    sorted_items = sorted(items, key=lambda x: x[key], reverse=higher_better)
    cutoff_value = sorted_items[cutoff_idx - 1][key]
    flag_name = f"top20_{key}"
    for item in items:
        if higher_better:
            item[flag_name] = 1 if item[key] >= cutoff_value else 0
        else:
            item[flag_name] = 1 if item[key] <= cutoff_value else 0
    return cutoff_value

# For ESM and MFE: compute top20 on shortlist cohort.
# Higher MFE (less negative) = less 5' structure = better translation init.
mfe_cut = assign_top20(v1_shortlist, "mfe", higher_better=True)
# Use raw_pll (rank-equivalent to scaled pseudo-pLDDT) for cleaner numerics.
esm_cut = assign_top20(v1_shortlist, "esm_pll", higher_better=True)
print(f"v2 cutoffs on shortlist cohort:")
print(f"  MFE top20 (least structured):    {mfe_cut:.2f} kcal/mol")
print(f"  ESM pseudo-pLDDT top20:           {esm_cut:.2f}")

# ---------------------------------------------------------------------------
# N-of-5 concordance
# ---------------------------------------------------------------------------

for row in v1_shortlist:
    row["concordance_n5"] = (row["top20_cai"]
                              + row["top20_mfe"]
                              + row["top20_chaperone_load"]
                              + row["top20_promoter_sp_prior"]
                              + row["top20_esm_pll"])

# Composite (5-model normalized average)
def normalize(items, key, higher_better=True):
    vals = [x[key] for x in items]
    lo, hi = min(vals), max(vals)
    span = hi - lo if hi > lo else 1.0
    nk = f"norm_{key}"
    for x in items:
        v = (x[key] - lo) / span
        x[nk] = v if higher_better else 1.0 - v

normalize(v1_shortlist, "cai", True)
normalize(v1_shortlist, "mfe", True)
normalize(v1_shortlist, "chaperone_load", False)
normalize(v1_shortlist, "promoter_sp_prior", True)
normalize(v1_shortlist, "esm_pll", True)
for row in v1_shortlist:
    row["composite_v2"] = (row["norm_cai"] + row["norm_mfe"] + row["norm_chaperone_load"]
                           + row["norm_promoter_sp_prior"] + row["norm_esm_pll"]) / 5.0

# Distribution
conc_dist = Counter(r["concordance_n5"] for r in v1_shortlist)
print("\nv2 concordance distribution on v1 shortlist:")
for n in sorted(conc_dist.keys(), reverse=True):
    pct = 100 * conc_dist[n] / len(v1_shortlist)
    print(f"  N-of-5 = {n}: {conc_dist[n]:4d} cassettes ({pct:.1f}%)")

# v2 shortlist (N-of-5 >= 4)
v2_shortlist = [r for r in v1_shortlist if r["concordance_n5"] >= 4]
v2_shortlist.sort(key=lambda r: (-r["concordance_n5"], -r["composite_v2"]))

# v1 strict baseline (N-of-4 = 4)
v1_n4_strict = [r for r in v1_shortlist if r["concordance_n"] == 4]
print(f"\nv1 shortlist (N-of-4 >= 3):  {len(v1_shortlist)} unique cassettes")
print(f"v1 strict   (N-of-4 = 4):    {len(v1_n4_strict)} unique cassettes")
print(f"v2 shortlist (N-of-5 >= 4):  {len(v2_shortlist)} unique cassettes")
print(f"v2 strict   (N-of-5 = 5):    {sum(1 for r in v1_shortlist if r['concordance_n5'] == 5)}")

# ---------------------------------------------------------------------------
# Did v1's top cluster survive?
# v1 top cluster: PamyB + amyB-SP + 5'-softened codon + direct + PTS1-blocking
# C-term tag + N191Q glyc ablation
# ---------------------------------------------------------------------------

def is_v1_top_cluster(row):
    return (row["promoter"] == "PamyB"
            and row["sp"] in ("SPamyB", "SPamyB_pro")
            and row["codon"] == "5p_softened"
            and row["scaffold_base"] in ("direct_3xAla_pts1blk", "direct_his6_pts1ok")
            and row["nglyc"] == "nglyc_ablated")

v1_top_in_short = [r for r in v1_shortlist if is_v1_top_cluster(r)]
v1_top_in_v2 = [r for r in v2_shortlist if is_v1_top_cluster(r)]
survival_pct = 100 * len(v1_top_in_v2) / max(1, len(v1_top_in_short))
print(f"\nv1 top cluster (PamyB+amyB-SP+5p_softened+direct+PTS1blk+N191Q):")
print(f"  Cassettes matching cluster in v1 shortlist:  {len(v1_top_in_short)}")
print(f"  Cassettes matching cluster in v2 shortlist:  {len(v1_top_in_v2)}")
print(f"  Survival: {survival_pct:.0f}%")

# Cassettes v1 promoted but v2 rejects on fold-quality grounds
# (in v1 shortlist, not in v2 shortlist, AND top20_esm_pll == 0)
v1_promoted_v2_rejected_fold = [r for r in v1_shortlist
                                 if r["concordance_n5"] < 4 and r["top20_esm_pll"] == 0]
print(f"\nv1-promoted but v2-rejected on fold-quality: {len(v1_promoted_v2_rejected_fold)} cassettes")

# ---------------------------------------------------------------------------
# Correlation: ViennaRNA MFE vs v1 GC-clamp proxy
# (on the (codon, sp) pair cohort)
# ---------------------------------------------------------------------------

def spearman(xs, ys):
    n = len(xs)
    if n < 2: return float("nan")
    def ranks(vals):
        order = sorted(range(n), key=lambda i: vals[i])
        r = [0.0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and vals[order[j+1]] == vals[order[i]]:
                j += 1
            avg = (i + j) / 2 + 1
            for k in range(i, j + 1):
                r[order[k]] = avg
            i = j + 1
        return r
    rx = ranks(xs); ry = ranks(ys)
    mx = sum(rx)/n; my = sum(ry)/n
    num = sum((rx[i]-mx)*(ry[i]-my) for i in range(n))
    dx = (sum((r-mx)**2 for r in rx))**0.5
    dy = (sum((r-my)**2 for r in ry))**0.5
    if dx == 0 or dy == 0: return float("nan")
    return num / (dx * dy)

def pearson(xs, ys):
    n = len(xs)
    if n < 2: return float("nan")
    mx = sum(xs)/n; my = sum(ys)/n
    num = sum((xs[i]-mx)*(ys[i]-my) for i in range(n))
    dx = (sum((x-mx)**2 for x in xs))**0.5
    dy = (sum((y-my)**2 for y in ys))**0.5
    if dx == 0 or dy == 0: return float("nan")
    return num / (dx * dy)

# Correlation on the unique (codon, sp) pair set (52 pairs):
pairs = sorted(mfe_by_pair.keys())
mfe_vals = [mfe_by_pair[p] for p in pairs]
proxy_vals = [proxy_by_pair[p] for p in pairs]
# Note sign: higher MFE = less structure = better; higher proxy = less structure = better.
# Expect positive correlation if v1 proxy is a good stand-in.
rho_pair = spearman(mfe_vals, proxy_vals)
r_pair = pearson(mfe_vals, proxy_vals)
print(f"\nViennaRNA MFE vs v1 GC-clamp proxy (n={len(pairs)} codon-SP pairs):")
print(f"  Spearman rho = {rho_pair:.3f}")
print(f"  Pearson r    = {r_pair:.3f}")

# ---------------------------------------------------------------------------
# Write outputs
# ---------------------------------------------------------------------------

# v2_shortlist.csv
csv_fields = ["promoter", "sp", "codon", "scaffold_base", "propeptide", "nglyc",
              "cai", "mfe", "chaperone_load", "promoter_sp_prior", "esm_pll",
              "top20_cai", "top20_mfe", "top20_chaperone_load",
              "top20_promoter_sp_prior", "top20_esm_pll",
              "concordance_n5", "composite_v2"]
with (V2_OUTPUTS / "v2_shortlist.csv").open("w") as f:
    w = csv.writer(f)
    w.writerow(csv_fields)
    for r in v2_shortlist:
        out = []
        for k in csv_fields:
            v = r[k]
            if isinstance(v, float):
                out.append(f"{v:.4f}")
            else:
                out.append(str(v))
        w.writerow(out)
print(f"\nwrote {V2_OUTPUTS/'v2_shortlist.csv'} ({len(v2_shortlist)} rows)")

# v2_top25.md
with (V2_OUTPUTS / "v2_top25.md").open("w") as f:
    f.write("# comp-022 v2 Top-25 cassettes (N-of-5 >= 4 concordance)\n\n")
    f.write(f"v2 run date: 2026-05-14\n\n")
    f.write(f"v2 shortlist size: **{len(v2_shortlist)}** unique cassettes ")
    f.write(f"(vs v1 N-of-4 >= 3 = {len(v1_shortlist)}; v1 N-of-4 = 4 strict = {len(v1_n4_strict)}).\n\n")
    f.write(f"v1-top-cluster (PamyB + amyB-SP + 5p_softened + direct + PTS1-blk + N191Q) survival in v2: ")
    f.write(f"**{len(v1_top_in_v2)} / {len(v1_top_in_short)}** ({survival_pct:.0f}%).\n\n")
    f.write(f"ViennaRNA MFE vs v1 GC-clamp proxy: Spearman rho = **{rho_pair:.3f}** (n={len(pairs)} pairs).\n\n")
    f.write("Five models: CAI (higher better), ViennaRNA 5'-MFE (higher = less structure = better), chaperone load (lower better), promoter x SP prior (higher better), ESM2 pseudo-pLDDT (higher better, ESMFold fallback per provenance.md).\n\n")
    f.write("| Rank | Promoter | SP | Codon | Scaffold | Prop | N-glyc | CAI | MFE | ChapLoad | Prior | ESM-pLDDT | N-of-5 | Composite |\n")
    f.write("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
    for i, r in enumerate(v2_shortlist[:25], 1):
        f.write(f"| {i} | {r['promoter']} | {r['sp']} | {r['codon']} | {r['scaffold_base']} "
                f"| {r['propeptide']} | {r['nglyc']} | {r['cai']:.3f} | {r['mfe']:.2f} "
                f"| {r['chaperone_load']:.2f} | {r['promoter_sp_prior']:.3f} | {r['esm_pll']:.1f} "
                f"| {r['concordance_n5']} | {r['composite_v2']:.3f} |\n")
print(f"wrote {V2_OUTPUTS/'v2_top25.md'}")

# v2_summary.json
summary = {
    "experiment_id": "comp-022 v2",
    "date": "2026-05-14",
    "v1_shortlist_size_n4_ge_3": len(v1_shortlist),
    "v1_strict_size_n4_eq_4": len(v1_n4_strict),
    "v2_shortlist_size_n5_ge_4": len(v2_shortlist),
    "v2_strict_size_n5_eq_5": sum(1 for r in v1_shortlist if r["concordance_n5"] == 5),
    "v2_cutoffs_on_shortlist_cohort": {
        "mfe_top20_cutoff_kcal_per_mol": mfe_cut,
        "esm_pseudo_pLDDT_top20_cutoff": esm_cut,
    },
    "v1_cutoffs_on_full_cohort": V1_CUTOFFS,
    "v2_concordance_distribution": {str(k): v for k, v in conc_dist.items()},
    "v1_top_cluster_survival": {
        "cluster_definition": "PamyB + (SPamyB or SPamyB_pro) + 5p_softened + (direct_3xAla_pts1blk or direct_his6_pts1ok) + nglyc_ablated",
        "cassettes_in_v1_shortlist_matching_cluster": len(v1_top_in_short),
        "cassettes_in_v2_shortlist_matching_cluster": len(v1_top_in_v2),
        "survival_pct": survival_pct,
    },
    "v1_promoted_v2_rejected_on_fold_quality": len(v1_promoted_v2_rejected_fold),
    "viennarna_mfe_vs_v1_proxy_correlation": {
        "spearman_rho_per_codon_sp_pair": rho_pair,
        "pearson_r_per_codon_sp_pair": r_pair,
        "n_pairs": len(pairs),
        "interpretation": ("Positive Spearman rho means v1 proxy and ViennaRNA MFE agree on rank order: "
                           "higher rho = v1 proxy was a good stand-in. Low/negative rho = v1 proxy was "
                           "misranking cassettes, and the v2 rerank materially changes the call."),
    },
    "esm_pll_pseudo_pLDDT_distribution_on_shortlist": {
        "min": min(r["esm_pll"] for r in v1_shortlist),
        "max": max(r["esm_pll"] for r in v1_shortlist),
        "mean": sum(r["esm_pll"] for r in v1_shortlist) / len(v1_shortlist),
    },
    "mfe_distribution_on_shortlist_kcal_per_mol": {
        "min": min(r["mfe"] for r in v1_shortlist),
        "max": max(r["mfe"] for r in v1_shortlist),
        "mean": sum(r["mfe"] for r in v1_shortlist) / len(v1_shortlist),
    },
    "fallbacks_owned": [
        "ESM2 pseudo-likelihood used in place of real ESMFold v1 pLDDT (openfold install was blocked by the auto-mode classifier as 'code from external'; brief explicitly authorized this fallback). Pseudo-pLDDT scale [50,90] is a presentational rescaling of raw mean log-prob; top20 flags use the rank-preserving order.",
        "ViennaRNA MFE computed over a 150-nt window (61-nt generic A-rich 5'UTR + signal peptide ORF + first 30 codons of uricase). 5'UTR is held constant across cassettes since v1 promoter variants don't model UTR sequence differences.",
        "Quintile cutoffs for ESM and MFE computed on the 501-cassette v1 shortlist cohort (not the 43,200-cohort) because v2 retrofits only score the v1 survivors. This is the correct interpretive frame: v2 is a tighter gate on v1 promotion, not a re-enumeration.",
        "MPS unavailable on this Python 3.13 + torch 2.12 stack (torch.backends.mps.is_built() = True but torch.backends.mps.is_available() = False); fell back to CPU. ESM2 inference still completed all 106 sequences in ~70 seconds at 8 threads.",
    ],
}
with (V2_OUTPUTS / "v2_summary.json").open("w") as f:
    json.dump(summary, f, indent=2)
print(f"wrote {V2_OUTPUTS/'v2_summary.json'}")

print("\n" + "=" * 60)
print("HEADLINE")
print("=" * 60)
print(f"v1 shortlist (N-of-4 >= 3):       {len(v1_shortlist)} unique cassettes")
print(f"v1 strict   (N-of-4 = 4):         {len(v1_n4_strict)} unique cassettes")
print(f"v2 shortlist (N-of-5 >= 4):       {len(v2_shortlist)} unique cassettes")
print(f"v2 strict   (N-of-5 = 5):         {sum(1 for r in v1_shortlist if r['concordance_n5'] == 5)} unique cassettes")
print(f"v1 top cluster survival:          {len(v1_top_in_v2)}/{len(v1_top_in_short)} ({survival_pct:.0f}%)")
print(f"ViennaRNA MFE vs v1 proxy:        Spearman rho = {rho_pair:.3f}")
print(f"v1->v2 rejections on fold gate:   {len(v1_promoted_v2_rejected_fold)} cassettes")
print("=" * 60)
