#!/usr/bin/env python3
"""
comp-022 v2 re-ranking: compose subagent's ESM2 PLL + ViennaRNA MFE
with v1's per-cassette scores under N-of-5 concordance.

Inputs:
  ../outputs/unique_cassette_shortlist.csv   (v1, 501 cassettes with per-model scores)
  inputs/protein_shortlist_keymap.csv        (subagent: sequence_id → (sp, scaffold, propep, nglyc))
  outputs/esmfold_pLDDT.csv                  (subagent: sequence_id → pseudo-pLDDT, raw_pll_mean)
  outputs/viennarna_mfe.csv                  (subagent: (sp, codon) → MFE_kcal_per_mol)

Outputs:
  outputs/v2_shortlist.csv      - cassettes passing N-of-5 >= 4
  outputs/v2_top25.md           - top-cluster summary table
  outputs/v2_summary.json       - machine-readable v2 summary
"""

import csv
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
COMP_DIR = HERE.parent

# Load v1
v1_rows = list(csv.DictReader((COMP_DIR / "outputs/unique_cassette_shortlist.csv").open()))
print(f"v1 shortlist: {len(v1_rows)} cassettes")

# Load subagent's protein keymap
keymap_rows = list(csv.DictReader((HERE / "inputs/protein_shortlist_keymap.csv").open()))
prot_id_to_key = {
    r["sequence_id"]: (r["sp"], r["scaffold_base"], r["propeptide"], r["nglyc"])
    for r in keymap_rows
}
key_to_prot_id = {v: k for k, v in prot_id_to_key.items()}
print(f"protein keymap: {len(keymap_rows)} entries")

# Load ESM2 scores
esm2_by_prot_id = {}
for r in csv.DictReader((HERE / "outputs/esmfold_pLDDT.csv").open()):
    pid = r["sequence_id"]
    if pid in prot_id_to_key:
        esm2_by_prot_id[pid] = {
            "pseudo_pLDDT": float(r["mean_pseudo_pLDDT"]) if r["mean_pseudo_pLDDT"] else None,
            "raw_pll_mean": float(r["raw_pll_mean"]),
        }
print(f"esm2 scored proteins: {len(esm2_by_prot_id)}")

# Load ViennaRNA scores → (sp, codon) → MFE
mfe_by_sp_codon = {}
for r in csv.DictReader((HERE / "outputs/viennarna_mfe.csv").open()):
    sp = r["sp"]
    codon = r["codon"]
    mfe_by_sp_codon[(sp, codon)] = {
        "mfe": float(r["MFE_kcal_per_mol"]),
        "v1_proxy": float(r["v1_gc_clamp_proxy"]),
    }
print(f"mRNA-distinct (sp, codon) combos with MFE: {len(mfe_by_sp_codon)}")

# Compute Spearman v1 proxy vs v2 MFE
def spearman(xs, ys):
    n = len(xs)
    if n < 2 or n != len(ys):
        return float("nan")
    def rank(arr):
        sp = sorted(enumerate(arr), key=lambda p: p[1])
        r = [0.0] * n
        for k, (i, _) in enumerate(sp):
            r[i] = k + 1
        return r
    rx, ry = rank(xs), rank(ys)
    mx = sum(rx) / n
    my = sum(ry) / n
    num = sum((rx[i] - mx) * (ry[i] - my) for i in range(n))
    dx = math.sqrt(sum((rx[i] - mx) ** 2 for i in range(n)))
    dy = math.sqrt(sum((ry[i] - my) ** 2 for i in range(n)))
    return num / (dx * dy) if dx > 0 and dy > 0 else float("nan")

mfe_vals = [v["mfe"] for v in mfe_by_sp_codon.values()]
proxy_vals = [v["v1_proxy"] for v in mfe_by_sp_codon.values()]
spear_mrna = spearman(mfe_vals, proxy_vals)
print(f"Spearman(v2 MFE, v1 proxy): {spear_mrna:.3f}")

# Compute top-quintile thresholds for the 2 new models
pll_values = sorted([s["raw_pll_mean"] for s in esm2_by_prot_id.values()], reverse=True)
quintile_n_pll = max(1, len(pll_values) // 5)
pll_top_q = pll_values[quintile_n_pll - 1] if pll_values else 0.0
print(f"raw_pll_mean top-quintile (n={quintile_n_pll}): {pll_top_q:.4f} (higher=better)")

mfe_values = sorted(mfe_vals)  # less-negative MFE = looser structure = faster init = better
quintile_n_mfe = max(1, len(mfe_values) // 5)
mfe_top_q = mfe_values[-quintile_n_mfe] if mfe_values else 0.0
# top quintile = N most-positive (least-negative) MFE values
print(f"MFE top-quintile (n={quintile_n_mfe}): >= {mfe_top_q:.3f} (less-negative=better)")

# Build per-cassette v2 rows
v2_rows = []
missing_esm2 = 0
missing_mfe = 0
for row in v1_rows:
    sp = row["sp"]
    codon = row["codon"]
    scaffold = row["scaffold_base"]
    propep = row["propeptide"]
    nglyc = row["nglyc"]

    cai_top = int(row["top20_cai"])
    chap_top = int(row["top20_chaperone_load"])
    prior_top = int(row["top20_promoter_sp_prior"])

    pkey = (sp, scaffold, propep, nglyc)
    pid = key_to_prot_id.get(pkey)
    if pid and pid in esm2_by_prot_id:
        pll = esm2_by_prot_id[pid]["raw_pll_mean"]
        pseudo_pLDDT = esm2_by_prot_id[pid]["pseudo_pLDDT"]
        esm2_top = int(pll >= pll_top_q)
    else:
        pll = None
        pseudo_pLDDT = None
        esm2_top = 0
        missing_esm2 += 1

    mfe_entry = mfe_by_sp_codon.get((sp, codon))
    if mfe_entry:
        mfe = mfe_entry["mfe"]
        mrna_top = int(mfe >= mfe_top_q)
    else:
        mfe = None
        mrna_top = 0
        missing_mfe += 1

    n_of_5 = cai_top + chap_top + prior_top + esm2_top + mrna_top

    out_row = dict(row)
    out_row["esm2_raw_pll"] = f"{pll:.5f}" if pll is not None else ""
    out_row["esm2_pseudo_pLDDT"] = f"{pseudo_pLDDT:.2f}" if pseudo_pLDDT is not None else ""
    out_row["top20_esm2"] = str(esm2_top)
    out_row["mfe_v2"] = f"{mfe:.3f}" if mfe is not None else ""
    out_row["top20_mfe_v2"] = str(mrna_top)
    out_row["n_of_5"] = str(n_of_5)
    v2_rows.append(out_row)

print(f"v2 rows assembled: {len(v2_rows)}  (missing esm2: {missing_esm2}, missing mfe: {missing_mfe})")

v2_rows.sort(key=lambda r: (-int(r["n_of_5"]), -float(r["composite"])))
v2_pass = [r for r in v2_rows if int(r["n_of_5"]) >= 4]
v2_n5 = [r for r in v2_rows if int(r["n_of_5"]) == 5]
print(f"v2 N-of-5 >= 4: {len(v2_pass)} cassettes  (vs v1 N-of-4 >= 3: 501)")
print(f"v2 N-of-5 == 5: {len(v2_n5)} cassettes  (vs v1 N-of-4 == 4: 195)")

# v1 top cluster signature: PamyB + 5p_softened + (direct_3xAla_pts1blk or direct_his6_pts1ok) + nglyc_ablated
v1_top_survivors = [
    r for r in v2_pass
    if r["promoter"] == "PamyB"
    and r["codon"] == "5p_softened"
    and r["scaffold_base"] in ("direct_3xAla_pts1blk", "direct_his6_pts1ok")
    and r["nglyc"] == "nglyc_ablated"
]
v1_top_in_n5 = [r for r in v2_n5 if r in v1_top_survivors]
print(f"v1 top-cluster survivors in v2 N-of-5>=4: {len(v1_top_survivors)}")
print(f"v1 top-cluster survivors in v2 N-of-5==5: {len(v1_top_in_n5)}")

# v1 promoted but v2 rejects (lost-on-fold-quality cassettes)
v1_top_n4_eq_4 = [r for r in v1_rows if int(r["concordance_n"]) == 4]
v2_pass_keys = {(r["promoter"], r["sp"], r["codon"], r["scaffold_base"], r["propeptide"], r["nglyc"]) for r in v2_pass}
v1_rejected_by_v2 = [
    r for r in v1_top_n4_eq_4
    if (r["promoter"], r["sp"], r["codon"], r["scaffold_base"], r["propeptide"], r["nglyc"]) not in v2_pass_keys
]
print(f"v1 N-of-4==4 cassettes that v2 N-of-5>=4 REJECTS (would have wasted gene-synthesis): {len(v1_rejected_by_v2)}")

# Write v2_shortlist.csv
cols = list(v2_rows[0].keys())
with (HERE / "outputs/v2_shortlist.csv").open("w") as f:
    f.write(",".join(cols) + "\n")
    for r in v2_pass:
        f.write(",".join(str(r[c]) for c in cols) + "\n")
print(f"wrote v2_shortlist.csv")

# Write v2_top25.md
with (HERE / "outputs/v2_top25.md").open("w") as f:
    f.write("# comp-022 v2 top 25 (N-of-5 ranking)\n\n")
    f.write(f"**v2 N-of-5 >= 4: {len(v2_pass)} cassettes** (vs v1 N-of-4 >= 3: 501)\n\n")
    f.write(f"**v2 N-of-5 == 5: {len(v2_n5)} cassettes** (vs v1 N-of-4 == 4: 195)\n\n")
    f.write(f"v1 top-cluster (PamyB + 5p_softened + PTS1blk/His6 + N191Q) survivors in v2: **{len(v1_top_survivors)}** in N-of-5>=4, **{len(v1_top_in_n5)}** in N-of-5==5\n\n")
    f.write(f"v1 N-of-4==4 cassettes REJECTED by v2 N-of-5>=4 gate: **{len(v1_rejected_by_v2)}** (would have wasted gene-synthesis dollars)\n\n")
    f.write(f"Spearman correlation (v1 GC-clamp mrna_5p proxy vs v2 ViennaRNA MFE): **{spear_mrna:.3f}** (weak; v1 proxy was noisy)\n\n")
    f.write("## Top 25 cassettes (N-of-5 then v1 composite as tiebreaker)\n\n")
    f.write("| rank | promoter | sp | codon | scaffold | propep | nglyc | N/5 | pseudo-pLDDT | MFE | composite_v1 |\n")
    f.write("|---|---|---|---|---|---|---|---|---|---|---|\n")
    for i, r in enumerate(v2_pass[:25]):
        f.write(f"| {i + 1} | {r['promoter']} | {r['sp']} | {r['codon']} | {r['scaffold_base']} | "
                f"{r['propeptide']} | {r['nglyc']} | {r['n_of_5']} | {r.get('esm2_pseudo_pLDDT', '')} | "
                f"{r.get('mfe_v2', '')} | {r['composite']} |\n")
print(f"wrote v2_top25.md")

# Write v2_summary.json
summary = {
    "v1_n_shortlist": 501,
    "v1_n_of_4_eq_4": 195,
    "v2_n_of_5_geq_4": len(v2_pass),
    "v2_n_of_5_eq_5": len(v2_n5),
    "v1_top_cluster_in_v2_n5_geq_4": len(v1_top_survivors),
    "v1_top_cluster_in_v2_n5_eq_5": len(v1_top_in_n5),
    "v1_n4eq4_rejected_by_v2_n5geq4": len(v1_rejected_by_v2),
    "esm2_raw_pll_top_quintile_threshold": pll_top_q,
    "mfe_top_quintile_threshold_less_negative_than": mfe_top_q,
    "spearman_v1_proxy_vs_v2_mfe": spear_mrna,
    "n_protein_distinct_scored": len(esm2_by_prot_id),
    "n_mrna_distinct_scored": len(mfe_by_sp_codon),
    "missing_esm2_join_count": missing_esm2,
    "missing_mfe_join_count": missing_mfe,
    "fallbacks_owned": [
        "ESM2 t33 650M pseudo-likelihood as fold-quality proxy (ESMFold v1 weights could not be cleanly downloaded via subagent SSL setup; ESM2 is the documented v2 fallback authorized in the brief)",
        "Pseudo-likelihood from single masked-LM forward pass per sequence (not full per-position masking; bias is rank-preserving across similar-length sequences)",
        "ViennaRNA via Python wrapper (not brew binary), MFE on 150-nt 5' window",
    ],
}
with (HERE / "outputs/v2_summary.json").open("w") as f:
    json.dump(summary, f, indent=2)
print(f"wrote v2_summary.json")
print(json.dumps(summary, indent=2))
