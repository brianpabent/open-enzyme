#!/usr/bin/env python3
"""
comp-030: ClockBase-style combinatorial ranking of A. oryzae DAF/CD55 SCR1-4
expression cassettes.

Target: DAF/CD55 SCR1-4 truncated construct (aa 35-285, UniProt P08174)
Host:   A. oryzae (RIB40 reference; NSlD-deltaPi10 for high-expression variants)

Design-space: 6 promoters x 12 signal peptides x 10 codon variants x 60 secretion scaffolds
            = 43,200 combinations (mirrors comp-022 cardinality).

Pipeline (5 orthogonal scoring models; all apply to all 43,200 candidates via pre-computation):

  Model 1 - CAI:
    Codon Adaptation Index (Sharp & Li 1987 PMID 3547335) under A. oryzae codon table.
    Per-codon-variant (10 evaluations, then broadcast to all cassettes sharing that variant).

  Model 2 - ViennaRNA MFE:
    Real ViennaRNA 2.7.2 MFE of 5' mRNA region (150-nt window:
    generic A-rich 5'UTR + SP ORF + first 30 codons of DAF SCR1-4 mature sequence).
    Per (codon, SP) pair (120 unique pairs max; usually fewer after SP-only grouping).
    Replaces v1 GC-clamp proxy used in comp-022 v1 (Spearman rho = 0.241 vs real MFE).

  Model 3 - Chaperone load:
    Architecture-adjusted PDI load per chaperone-orthogonal-stacking.md sec 3.5.
    Formula: effective_load = disulfide_count x alpha
    For DAF SCR1-4: 8 disulfide bonds x CCP/SCR alpha = 0.3-0.6 => 2.4-4.8 effective.
    Uses alpha = 0.45 (central estimate) for scoring; sensitivity to alpha range noted.
    Per-scaffold-base (10 evaluations, then broadcast).
    Lower effective_load = better (less chaperone competition).

  Model 4 - Promoter x SP compatibility prior:
    Literature-derived relative strength x secretion-efficiency multipliers.
    Per (promoter, SP) pair (72 unique pairs).

  Model 5 - ESM2 pseudo-pLDDT:
    ESMFold v1 authorized fallback: ESM2 t33 650M pseudo-likelihood as fold-quality proxy.
    ESMFold v1 requires openfold; if blocked, ESM2 pseudo-likelihood (Verkuil 2022; Hsu 2022)
    is the documented fallback (same model ESMFold uses internally).
    Per protein-distinct (SP, scaffold_base, propeptide, nglyc) tuple.
    LOAD-BEARING: This axis provides the alpha-coefficient check.
    If pLDDT distribution is broadly high (>80) across most candidates, CCP/SCR
    fast-folding / low-PDI-load hypothesis (alpha = 0.3-0.6) is corroborated.
    If pLDDT is broadly poor, the hypothesis is weaker.

Concordance gate: N-of-5 >= 4 (80%) -- same threshold as comp-022 v2.
  Each candidate gets a top-quintile flag per model (1 if top 20%).
  Candidates with concordance_n >= 4 are promoted to the shortlist.

Design-space factorization:
  6 promoters x 12 SP x 10 codon variants x 60 scaffolds = 43,200

  Scaffold factorization (60):
    10 base scaffolds:
      - direct_natag_pts1ok (no C-term tag; native terminator; PTS1-exposed)
      - direct_3xAla_pts1blk (3xAla C-term tag; PTS1 blocked)
      - direct_his6_pts1ok (His6 C-term tag; PTS1 exposed -- DAF has no intrinsic PTS1
        but tag can interact with peroxisomal import in some substrates; labeled "ok" to
        mirror comp-022 naming -- DAF SCR1-4 does not have a C-terminal SKL, so PTS1
        routing is not a concern for this target; see note in Limitations)
      - glaA_KR_pts1ok (full glaA fusion + KR KEX2 site)
      - glaA_KR_3xAla (full glaA + KR + 3xAla)
      - glaA_KRGGG_pts1ok (full glaA + KRGGG KEX2 site)
      - glaA_KRGGG_3xAla (full glaA + KRGGG + 3xAla)
      - glaA_trunc_KR_pts1ok (truncated glaA + KR)
      - glaA_trunc_KR_3xAla (truncated glaA + KR + 3xAla)
      - tandem_KEX2_pts1ok (full glaA + double_KR)
    x 3 propeptide states: {none, short_kex2_pro, long_kex2_pro}
    x 2 N-glyc states: {nglyc_native, nglyc_ablated}
    = 10 x 3 x 2 = 60 scaffolds

Pre-commit verification gate:
  All load-bearing numbers are grep-verified against primary sources (see provenance.md).
  Key verifications:
  - 8 disulfide bonds: UniProt P08174 DISULFID feature annotations, accessed 2026-05-15
  - alpha = 0.3-0.6: chaperone-orthogonal-stacking.md sec 3.5.2, primary source Schmidt 2010
    PMC2806952 (NMR/SAXS CCP rigid-unit evidence)
  - CAI methodology: Sharp & Li 1987 PMID 3547335
  - ViennaRNA MFE: Kudla 2009 PMID 19359587 (5' mRNA structure -> translation initiation)
  - Codon table: Machida 2005 PMID 16372010 + Nakao 1992 PMID 1482437 (A. oryzae RIB40)

Author: Open Enzyme (comp-030 / claude/sonnet via Agent tool)
Date:   2026-05-15
"""

import csv
import json
import math
import random
from collections import Counter
from pathlib import Path

import RNA  # ViennaRNA 2.7.2 Python binding

HERE = Path(__file__).parent.parent
INPUTS = HERE / "inputs"
RESULTS = HERE / "results"
RESULTS.mkdir(exist_ok=True)

COMP022_INPUTS = HERE.parent / "comp-022-clockbase-uricase-cassette-ranking" / "inputs"

# ---------------------------------------------------------------------------
# Load inputs
# ---------------------------------------------------------------------------

with (COMP022_INPUTS / "a_oryzae_codon_usage.json").open() as f:
    CODON_TABLE = json.load(f)


def load_fasta(path):
    seq = []
    with open(path) as f:
        for line in f:
            if line.startswith(">"):
                continue
            seq.append(line.strip().replace(" ", ""))
    return "".join(seq)


DAF_SCR14_AA = load_fasta(INPUTS / "P08174_scr14.fasta")
assert len(DAF_SCR14_AA) == 251, f"Expected 251 aa for DAF SCR1-4 (aa 35-285), got {len(DAF_SCR14_AA)}"
assert DAF_SCR14_AA.count('C') == 16, f"Expected 16 Cys (8 disulfides), got {DAF_SCR14_AA.count('C')}"
print(f"DAF SCR1-4 sequence loaded: {len(DAF_SCR14_AA)} aa, {DAF_SCR14_AA.count('C')} Cys (8 disulfide bonds)")

# ---------------------------------------------------------------------------
# Codon table utilities (identical to comp-022)
# ---------------------------------------------------------------------------

AA_TO_CODONS = {}
for codon, info in CODON_TABLE["codons"].items():
    aa = info["aa"]
    if aa == "*":
        continue
    AA_TO_CODONS.setdefault(aa, []).append((codon, info["rscu"], info["freq_per1000"]))
for aa in AA_TO_CODONS:
    AA_TO_CODONS[aa].sort(key=lambda c: -c[1])

# Build RSCU lookup for rare-codon cluster penalty
CODON_RSCU = {codon: info["rscu"] for codon, info in CODON_TABLE["codons"].items()}
CODON_AA = {codon: info["aa"] for codon, info in CODON_TABLE["codons"].items() if info["aa"] != "*"}

CODON_FREQ = {codon: info["freq_per1000"] for codon, info in CODON_TABLE["codons"].items()}


def codon_gc(c):
    return sum(1 for x in c if x in "GC") / 3.0


def calc_cai(nt_seq):
    """Geometric mean of per-codon w-values. w = freq / max_freq_for_same_aa."""
    codons = [nt_seq[i:i+3] for i in range(0, len(nt_seq), 3) if nt_seq[i:i+3] in CODON_AA]
    log_sum = 0.0
    n = 0
    for codon in codons:
        aa = CODON_AA[codon]
        max_rscu = AA_TO_CODONS[aa][0][1]  # already sorted by rscu desc
        w = CODON_RSCU.get(codon, 0.1) / max_rscu if max_rscu > 0 else 0.1
        log_sum += math.log(max(w, 1e-6))
        n += 1
    return math.exp(log_sum / n) if n > 0 else 0.0


def count_rare_clusters(nt_seq, rscu_threshold=0.4, cluster_size=3):
    """Count runs of >= cluster_size consecutive codons with RSCU < threshold."""
    codons = [nt_seq[i:i+3] for i in range(0, len(nt_seq), 3) if nt_seq[i:i+3] in CODON_AA]
    clusters = 0
    run = 0
    for codon in codons:
        if CODON_RSCU.get(codon, 0.0) < rscu_threshold:
            run += 1
            if run == cluster_size:
                clusters += 1
        else:
            run = 0
    return clusters


# ---------------------------------------------------------------------------
# Back-translators (identical logic to comp-022 v2 run_viennarna_mfe.py)
# ---------------------------------------------------------------------------

def bt_native_daf(aa_seq, seed=46):
    """Native-sequence style: mid-rank codons (mimics natural human -> koji translation)."""
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
    "native_daf":            bt_native_daf,         # Human-derived; mid-rank A. oryzae codons
    "cai_max":               bt_max_cai,
    "cai_balanced":          bt_balanced,
    "cai_max_gc54":          bt_max_cai_gc54,
    "harmonized":            bt_harmonized,
    "rare_avoid":            bt_rare_avoid,
    "low_gc":                bt_low_gc,
    "high_gc":               bt_high_gc,
    "5p_softened":           bt_5p_softened,
    "5p_softened_balanced":  bt_5p_softened_balanced,
}

# ---------------------------------------------------------------------------
# Parts definition (mirrors comp-022; signal peptides + promoters identical)
# These are loaded from comp-022's parts_list.json for shared-provenance convenience.
# ---------------------------------------------------------------------------

# Load from comp-022 parts_list to share provenance
with (COMP022_INPUTS / "parts_list.json").open() as f:
    COMP022_PARTS = json.load(f)

PROMOTERS = COMP022_PARTS["promoters"]        # 6 promoters
SIGNAL_PEPTIDES = COMP022_PARTS["signal_peptides"]  # 12 SPs

SP_BY_ID = {sp["id"]: sp for sp in SIGNAL_PEPTIDES}
PROMOTER_BY_ID = {p["id"]: p for p in PROMOTERS}

# ---------------------------------------------------------------------------
# Secretion scaffolds for DAF SCR1-4 (60 total = 10 base x 3 propeptide x 2 nglyc)
# Note: DAF SCR1-4 has NO intrinsic C-terminal PTS1 motif (SKL), unlike uricase.
# The "pts1ok" / "pts1blk" labeling mirrors comp-022 for code compatibility; for
# DAF SCR1-4 specifically, PTS1 routing is not a concern -- DAF SCR1-4's C-terminus
# ends with ...KSLTS (aa 281-285), not SKL. Labels are legacy from comp-022 framework.
# ---------------------------------------------------------------------------

# Architecture-adjusted chaperone load formula:
# effective_load = disulfide_count x alpha + glycosylation_term + fusion_carrier_load
# DAF SCR1-4: 8 disulfides x alpha_central = 0.45 (central CCP/SCR estimate; range 0.3-0.6)
# Alpha range sensitivity: see results/sensitivity_alpha.csv

DAF_DISULFIDES = 8  # verified: UniProt P08174 DISULFID annotations, 2026-05-15
ALPHA_CENTRAL = 0.45  # central estimate for CCP/SCR fold (range 0.3-0.6); Schmidt 2010 PMC2806952
DAF_INTRINSIC_LOAD = DAF_DISULFIDES * ALPHA_CENTRAL  # 3.6 effective PDI load (central)

# Scaffold base chaperone loads (same architecture as comp-022; values verified from
# chaperone-orthogonal-stacking.md sec 3.5.3 + comp-022 scaffold scores):
SCAFFOLD_LOADS = {
    "direct_natag_pts1ok":    DAF_INTRINSIC_LOAD + 0.0,   # 3.6 -- direct, no C-term mod
    "direct_3xAla_pts1blk":   DAF_INTRINSIC_LOAD + 0.0,   # 3.6 -- 3xAla tag, no extra load
    "direct_his6_pts1ok":     DAF_INTRINSIC_LOAD + 0.0,   # 3.6 -- His6 tag, no extra load
    "glaA_KR_pts1ok":         DAF_INTRINSIC_LOAD + 10.2,  # glaA full carrier (9 disulfides x 1.0 alpha + glycosylation)
    "glaA_KR_3xAla":          DAF_INTRINSIC_LOAD + 9.9,
    "glaA_KRGGG_pts1ok":      DAF_INTRINSIC_LOAD + 10.1,
    "glaA_KRGGG_3xAla":       DAF_INTRINSIC_LOAD + 9.8,
    "glaA_trunc_KR_pts1ok":   DAF_INTRINSIC_LOAD + 5.2,   # truncated glaA carrier
    "glaA_trunc_KR_3xAla":    DAF_INTRINSIC_LOAD + 4.9,
    "tandem_KEX2_pts1ok":     DAF_INTRINSIC_LOAD + 10.8,  # double KEX2; saturation penalty
}

SCAFFOLD_BASES = [
    {"id": "direct_natag_pts1ok",    "fusion": "none",         "kex2": "none",      "pts1_exposed": True,  "load": SCAFFOLD_LOADS["direct_natag_pts1ok"]},
    {"id": "direct_3xAla_pts1blk",   "fusion": "none",         "kex2": "none",      "pts1_exposed": False, "load": SCAFFOLD_LOADS["direct_3xAla_pts1blk"]},
    {"id": "direct_his6_pts1ok",     "fusion": "none",         "kex2": "none",      "pts1_exposed": False, "load": SCAFFOLD_LOADS["direct_his6_pts1ok"]},
    {"id": "glaA_KR_pts1ok",         "fusion": "glaA_full",    "kex2": "KR",        "pts1_exposed": True,  "load": SCAFFOLD_LOADS["glaA_KR_pts1ok"]},
    {"id": "glaA_KR_3xAla",          "fusion": "glaA_full",    "kex2": "KR",        "pts1_exposed": False, "load": SCAFFOLD_LOADS["glaA_KR_3xAla"]},
    {"id": "glaA_KRGGG_pts1ok",      "fusion": "glaA_full",    "kex2": "KRGGG",     "pts1_exposed": True,  "load": SCAFFOLD_LOADS["glaA_KRGGG_pts1ok"]},
    {"id": "glaA_KRGGG_3xAla",       "fusion": "glaA_full",    "kex2": "KRGGG",     "pts1_exposed": False, "load": SCAFFOLD_LOADS["glaA_KRGGG_3xAla"]},
    {"id": "glaA_trunc_KR_pts1ok",   "fusion": "glaA_trunc",   "kex2": "KR",        "pts1_exposed": True,  "load": SCAFFOLD_LOADS["glaA_trunc_KR_pts1ok"]},
    {"id": "glaA_trunc_KR_3xAla",    "fusion": "glaA_trunc",   "kex2": "KR",        "pts1_exposed": False, "load": SCAFFOLD_LOADS["glaA_trunc_KR_3xAla"]},
    {"id": "tandem_KEX2_pts1ok",     "fusion": "glaA_full",    "kex2": "double_KR", "pts1_exposed": True,  "load": SCAFFOLD_LOADS["tandem_KEX2_pts1ok"]},
]

PROPEPTIDE_STATES = ["none", "short_kex2_pro", "long_kex2_pro"]
NGLYC_STATES = ["nglyc_native", "nglyc_ablated"]

# N-glycosylation sites in DAF SCR1-4 (mature protein aa 35-285):
# Native DAF SCR1-4 has predicted N-glycosylation; stalk truncation removes several sites.
# In the mature SCR1-4 fragment, N-glyc sites are minimal (0-1); the primary glycosylation
# in native DAF is on the stalk region (which is absent here). For scoring purposes,
# nglyc_ablated adds 0 extra penalty vs nglyc_native (both score the same chaperone load
# since the CCP/SCR fold has effectively no N-glyc sequons in the truncated form).
# This is a favorable feature for A. oryzae expression (fewer calnexin cycle requirements).
NGLYC_PENALTY = {"nglyc_native": 0.0, "nglyc_ablated": 0.0}  # No N-glyc sequons in SCR1-4

# Propeptide load modifier (minor KEX2-related chaperone engagement):
PROPEPTIDE_LOAD = {"none": 0.0, "short_kex2_pro": 0.1, "long_kex2_pro": 0.2}

# Build full scaffold list (60 = 10 x 3 x 2)
SCAFFOLDS = []
for sb in SCAFFOLD_BASES:
    for prop in PROPEPTIDE_STATES:
        for nglyc in NGLYC_STATES:
            effective_load = sb["load"] + NGLYC_PENALTY[nglyc] + PROPEPTIDE_LOAD[prop]
            SCAFFOLDS.append({
                "id": f"{sb['id']}__{prop}__{nglyc}",
                "scaffold_base": sb["id"],
                "fusion": sb["fusion"],
                "kex2": sb["kex2"],
                "pts1_exposed": sb["pts1_exposed"],
                "propeptide": prop,
                "nglyc": nglyc,
                "chaperone_load": effective_load,
            })

assert len(SCAFFOLDS) == 60, f"Expected 60 scaffolds, got {len(SCAFFOLDS)}"

# Codon variants (10)
CODON_VARIANTS = list(BACK_TRANSLATORS.keys())
assert len(CODON_VARIANTS) == 10

# Full design space
N_PROMOTERS = len(PROMOTERS)          # 6
N_SP = len(SIGNAL_PEPTIDES)           # 12
N_CODON = len(CODON_VARIANTS)         # 10
N_SCAFFOLD = len(SCAFFOLDS)           # 60
N_TOTAL = N_PROMOTERS * N_SP * N_CODON * N_SCAFFOLD
print(f"\nDesign space: {N_PROMOTERS} promoters x {N_SP} SP x {N_CODON} codon variants x {N_SCAFFOLD} scaffolds = {N_TOTAL}")

# ---------------------------------------------------------------------------
# Model 1: CAI per codon variant
# Computed once per (codon_variant, SP) pair then broadcast.
# ---------------------------------------------------------------------------

print("\n=== Model 1: CAI per (codon, SP) pair ===")
cai_by_codon_sp = {}
rare_cluster_by_codon_sp = {}

for codon_id in CODON_VARIANTS:
    fn = BACK_TRANSLATORS[codon_id]
    # CAI and rare-cluster penalty on the mature DAF SCR1-4 ORF (SP-independent)
    nt_seq = fn(DAF_SCR14_AA)
    cai = calc_cai(nt_seq)
    rare_clusters = count_rare_clusters(nt_seq)
    for sp in SIGNAL_PEPTIDES:
        sp_id = sp["id"]
        cai_by_codon_sp[(codon_id, sp_id)] = cai
        rare_cluster_by_codon_sp[(codon_id, sp_id)] = rare_clusters

# Report per-codon-variant (SP-invariant since body sequence is what matters for CAI)
print(f"{'Codon Variant':<25} {'CAI':>6} {'Rare clusters':>15}")
for codon_id in CODON_VARIANTS:
    sp_id = SIGNAL_PEPTIDES[0]["id"]  # representative SP
    cai = cai_by_codon_sp[(codon_id, sp_id)]
    rc = rare_cluster_by_codon_sp[(codon_id, sp_id)]
    print(f"  {codon_id:<23} {cai:>6.3f} {rc:>15}")

# ---------------------------------------------------------------------------
# Model 2: ViennaRNA MFE per (codon, SP) pair
# 150-nt window: generic 5'UTR (61 nt) + SP ORF + first 30 codons of DAF SCR1-4
# ---------------------------------------------------------------------------

print("\n=== Model 2: ViennaRNA MFE per (codon, SP) pair ===")

# Generic 5'UTR: same as comp-022 (61 nt, A/T-rich; holds constant across all cassettes)
GENERIC_5UTR = "AAATATTACACAACATCACATAAATCAACCATCATCATAAACTAATCATCAATCATCAATC"
assert len(GENERIC_5UTR) == 61

mfe_by_codon_sp = {}
n_pairs = len(CODON_VARIANTS) * len(SIGNAL_PEPTIDES)
done = 0
for codon_id in CODON_VARIANTS:
    fn = BACK_TRANSLATORS[codon_id]
    # First 30 codons of DAF SCR1-4 mature sequence
    body_nt = fn(DAF_SCR14_AA[:30])
    for sp in SIGNAL_PEPTIDES:
        sp_id = sp["id"]
        sp_aa = sp["sequence"]
        sp_nt = fn(sp_aa)
        mrna_dna = GENERIC_5UTR + sp_nt + body_nt
        mrna_rna = mrna_dna.replace("T", "U")
        fold_window = mrna_rna[:150]
        fc = RNA.fold_compound(fold_window)
        _, mfe = fc.mfe()
        mfe_by_codon_sp[(codon_id, sp_id)] = mfe
        done += 1
        if done <= 3 or done >= n_pairs - 2:
            print(f"  [{done}/{n_pairs}] {codon_id} x {sp_id}: MFE={mfe:.2f} kcal/mol")

print(f"  MFE range: {min(mfe_by_codon_sp.values()):.2f} to {max(mfe_by_codon_sp.values()):.2f} kcal/mol")

# ---------------------------------------------------------------------------
# Model 3: Chaperone load per scaffold (pre-computed above in SCAFFOLDS)
# ---------------------------------------------------------------------------

print("\n=== Model 3: Chaperone load per scaffold (10 base scaffolds, central alpha=0.45) ===")
for sb in SCAFFOLD_BASES:
    print(f"  {sb['id']:<30} effective_load={sb['load']:.2f}")

# DAF SCR1-4 note: unlike uricase, the glaA-KEX2 fusion architecture CAN make sense for
# CCP/SCR fold proteins because the CCP/SCR domains are compact and may benefit from the
# N-terminal carrier driving early secretion. However, the carrier (glaA) adds 9 disulfides
# + glycosylation, which is a much larger chaperone burden than the DAF SCR1-4 intrinsic
# load of 3.6. The framework predicts that direct secretion is still optimal.

# ---------------------------------------------------------------------------
# Model 4: Promoter x SP prior
# ---------------------------------------------------------------------------

print("\n=== Model 4: Promoter x SP compatibility prior ===")

# Promoter strengths (from comp-022 parts_list; same values)
PROMOTER_STRENGTH = {p["id"]: p["relative_strength"] for p in PROMOTERS}

# SP secretion efficiencies (from comp-022 provenance; same bounded estimates)
# Native koji SPs: higher efficiency; foreign cbhI: lower
SP_EFFICIENCY = {
    "SPamyB":         1.00, "SPamyB_pro":       1.03,
    "SPglaA":         0.98, "SPglaA_pro":        1.00,
    "SPpepO":         0.85, "SPpepO_pro":        0.87,
    "SPalpA":         0.82, "SPalpA_pro":        0.84,
    "SPlipase":       0.80, "SPlipase_pro":      0.82,
    "SPcbhI":         0.65, "SPcbhI_pro":        0.68,
}

# Compute promoter x SP prior (capped to [0, 1.2])
promoter_sp_prior = {}
for p in PROMOTERS:
    for sp in SIGNAL_PEPTIDES:
        ps = PROMOTER_STRENGTH[p["id"]]
        se = SP_EFFICIENCY.get(sp["id"], 0.70)
        # Combine: product, normalized against the max possible (PamyB x SPamyB_pro)
        raw = ps * se
        promoter_sp_prior[(p["id"], sp["id"])] = raw

# Normalize to [0,1]
max_prior = max(promoter_sp_prior.values())
for k in promoter_sp_prior:
    promoter_sp_prior[k] = promoter_sp_prior[k] / max_prior

# ---------------------------------------------------------------------------
# Build full 43,200-candidate table (pre-computed models only; ESM2 deferred to step 2)
# ---------------------------------------------------------------------------

print(f"\n=== Building full {N_TOTAL}-candidate table ===")

candidates = []
for promoter in PROMOTERS:
    pid = promoter["id"]
    for sp in SIGNAL_PEPTIDES:
        sp_id = sp["id"]
        for codon_id in CODON_VARIANTS:
            for scaffold in SCAFFOLDS:
                cai = cai_by_codon_sp[(codon_id, sp_id)]
                mfe = mfe_by_codon_sp[(codon_id, sp_id)]
                chap = scaffold["chaperone_load"]
                prior = promoter_sp_prior[(pid, sp_id)]
                candidates.append({
                    "promoter":       pid,
                    "sp":             sp_id,
                    "codon":          codon_id,
                    "scaffold_id":    scaffold["id"],
                    "scaffold_base":  scaffold["scaffold_base"],
                    "propeptide":     scaffold["propeptide"],
                    "nglyc":          scaffold["nglyc"],
                    "fusion":         scaffold["fusion"],
                    "kex2":           scaffold["kex2"],
                    "cai":            cai,
                    "mfe":            mfe,
                    "chaperone_load": chap,
                    "promoter_sp_prior": prior,
                })

assert len(candidates) == N_TOTAL
print(f"  Built {len(candidates)} candidates.")

# ---------------------------------------------------------------------------
# Assign top-quintile flags for Models 1-4 (ESM2 = Model 5 in step 2)
# ---------------------------------------------------------------------------

def assign_top20_flag(items, key, higher_better=True, flag_key=None):
    if flag_key is None:
        flag_key = f"top20_{key}"
    n = len(items)
    cutoff_idx = max(1, n // 5)
    sorted_vals = sorted([x[key] for x in items], reverse=higher_better)
    cutoff = sorted_vals[cutoff_idx - 1]
    for item in items:
        if higher_better:
            item[flag_key] = 1 if item[key] >= cutoff else 0
        else:
            item[flag_key] = 1 if item[key] <= cutoff else 0
    return cutoff


cai_cut = assign_top20_flag(candidates, "cai", higher_better=True)
mfe_cut = assign_top20_flag(candidates, "mfe", higher_better=True)
chap_cut = assign_top20_flag(candidates, "chaperone_load", higher_better=False)
prior_cut = assign_top20_flag(candidates, "promoter_sp_prior", higher_better=True)

print(f"\nTop-quintile cutoffs (on 43,200-cohort):")
print(f"  CAI >= {cai_cut:.4f}")
print(f"  MFE >= {mfe_cut:.2f} kcal/mol (less negative = less 5' structure = better initiation)")
print(f"  Chaperone load <= {chap_cut:.2f}")
print(f"  Promoter-SP prior >= {prior_cut:.4f}")

# N-of-4 concordance (pre-ESM2; used for shortlisting for ESM2 run)
for c in candidates:
    c["concordance_n4"] = (c["top20_cai"] + c["top20_mfe"] +
                           c["top20_chaperone_load"] + c["top20_promoter_sp_prior"])

# ---------------------------------------------------------------------------
# Build protein-distinct shortlist for ESM2 scoring
# Protein sequence is determined by: (SP, scaffold_base, propeptide, nglyc)
# (Promoter and codon_variant don't change the protein sequence)
# ---------------------------------------------------------------------------

print("\n=== Building protein-distinct shortlist for ESM2 ===")

# For ESM2 efficiency: score all protein-distinct (sp, scaffold_base, propeptide, nglyc) combos
# that appear in ANY candidate passing N-of-4 >= 2 (broader than strict gate to avoid excluding
# candidates that might be rescued by the ESM2 axis)
protein_keys_needed = set()
for c in candidates:
    if c["concordance_n4"] >= 2:  # broad pre-filter
        pkey = (c["sp"], c["scaffold_base"], c["propeptide"], c["nglyc"])
        protein_keys_needed.add(pkey)

# Also include all unique protein combinations regardless (for distribution analysis)
all_protein_keys = set()
for c in candidates:
    pkey = (c["sp"], c["scaffold_base"], c["propeptide"], c["nglyc"])
    all_protein_keys.add(pkey)

print(f"  Total protein-distinct combinations: {len(all_protein_keys)}")
print(f"  Protein keys in N-of-4 >= 2 pre-filter: {len(protein_keys_needed)}")

# Build FASTA for each protein: SP + mature DAF SCR1-4 + optional C-term tag
# Protein sequence for each key:
def build_protein_sequence(sp_id, scaffold_base, propeptide, nglyc):
    """
    Returns the full secreted-protein AA sequence for ESM2 scoring.
    ESM2 receives: SP + mature DAF SCR1-4 (with propeptide if present) + C-term tag.
    nglyc state affects glycan occupancy (not AA sequence for ESM2 -- no change to AA seq).
    """
    sp_aa = SP_BY_ID[sp_id]["sequence"]
    mature = DAF_SCR14_AA  # 251 aa

    # Propeptide addition (N-terminal; between SP cleavage and mature N-term):
    if propeptide == "short_kex2_pro":
        prop_aa = "NTQQEA"  # representative 6-aa KEX2-cleavable propeptide
    elif propeptide == "long_kex2_pro":
        prop_aa = "NTQQEAAELKR"  # representative 11-aa KEX2-cleavable propeptide
    else:
        prop_aa = ""

    # C-terminal tag (from scaffold_base):
    if "3xAla" in scaffold_base:
        ctag = "AAA"
    elif "his6" in scaffold_base:
        ctag = "HHHHHH"
    else:
        ctag = ""

    # glaA fusion adds carrier at N-term before SP cleavage (after KEX2 site)
    # For ESM2 of the SECRETED domain: model the mature domain only (post-cleavage)
    # = prop_aa + mature + ctag (what PDI sees in the ER)
    return sp_aa + prop_aa + mature + ctag


# Build protein FASTA for ESM2
protein_seqs = {}  # key -> AA seq
for pkey in all_protein_keys:
    sp_id, sb, prop, nglyc = pkey
    seq_id = f"sp_{sp_id}__sb_{sb}__prop_{prop}__nglyc_{nglyc}"
    seq_id = seq_id.replace(" ", "_")
    protein_seqs[pkey] = (seq_id, build_protein_sequence(sp_id, sb, prop, nglyc))

# Write FASTA for ESM2
fasta_path = INPUTS / "protein_candidates.fasta"
keymap_path = INPUTS / "protein_candidates_keymap.csv"

with fasta_path.open("w") as f:
    for pkey, (seq_id, seq) in sorted(protein_seqs.items(), key=lambda x: x[1][0]):
        f.write(f">{seq_id}\n")
        for i in range(0, len(seq), 70):
            f.write(seq[i:i+70] + "\n")
print(f"  Wrote {len(protein_seqs)} protein sequences to {fasta_path}")

with keymap_path.open("w") as f:
    w = csv.writer(f)
    w.writerow(["sequence_id", "sp", "scaffold_base", "propeptide", "nglyc", "protein_length"])
    for pkey, (seq_id, seq) in sorted(protein_seqs.items(), key=lambda x: x[1][0]):
        sp_id, sb, prop, nglyc = pkey
        w.writerow([seq_id, sp_id, sb, prop, nglyc, len(seq)])
print(f"  Wrote keymap to {keymap_path}")

# ---------------------------------------------------------------------------
# Save intermediate results (pre-ESM2)
# ---------------------------------------------------------------------------

print("\n=== Writing intermediate results (pre-ESM2) ===")

# Concordance distribution
conc_dist_4 = Counter(c["concordance_n4"] for c in candidates)
print("N-of-4 concordance distribution (Models 1-4, pre-ESM2):")
for n in sorted(conc_dist_4.keys(), reverse=True):
    pct = 100 * conc_dist_4[n] / N_TOTAL
    print(f"  N-of-4 = {n}: {conc_dist_4[n]:6d} ({pct:.1f}%)")

# Top candidates pre-ESM2 (for validation that architecture makes sense)
top_pre_esm2 = sorted([c for c in candidates if c["concordance_n4"] >= 3],
                      key=lambda c: (-c["concordance_n4"],
                                     -c["cai"],
                                     c["chaperone_load"]))[:50]

pre_esm2_path = RESULTS / "pre_esm2_top50.csv"
fields = ["promoter", "sp", "codon", "scaffold_base", "propeptide", "nglyc",
          "cai", "mfe", "chaperone_load", "promoter_sp_prior", "concordance_n4",
          "top20_cai", "top20_mfe", "top20_chaperone_load", "top20_promoter_sp_prior"]
with pre_esm2_path.open("w") as f:
    w = csv.writer(f)
    w.writerow(fields)
    for c in top_pre_esm2:
        row = [c.get(k, "") for k in fields]
        w.writerow(row)
print(f"  Wrote pre-ESM2 top-50 to {pre_esm2_path}")

# Save all candidate scores (compressed: unique combinations only)
# Unique (promoter, sp, codon, scaffold_base, propeptide, nglyc) tuples
print(f"\nSaving all {N_TOTAL} candidate scores...")
all_candidates_path = RESULTS / "all_candidates_scores.csv"
with all_candidates_path.open("w") as f:
    w = csv.writer(f)
    w.writerow(fields)
    for c in candidates:
        row = []
        for k in fields:
            v = c.get(k, "")
            if isinstance(v, float):
                row.append(f"{v:.4f}")
            else:
                row.append(str(v))
        w.writerow(row)
print(f"  Wrote {N_TOTAL} rows to {all_candidates_path}")

# Save summary JSON
summary_pre = {
    "experiment_id": "comp-030",
    "date": "2026-05-15",
    "target": "DAF/CD55 SCR1-4 (aa 35-285, UniProt P08174)",
    "target_disulfides": DAF_DISULFIDES,
    "target_cys": DAF_SCR14_AA.count('C'),
    "alpha_central": ALPHA_CENTRAL,
    "alpha_range": [0.3, 0.6],
    "intrinsic_daf_pdi_load_central": DAF_INTRINSIC_LOAD,
    "design_space": {
        "promoters": N_PROMOTERS,
        "signal_peptides": N_SP,
        "codon_variants": N_CODON,
        "scaffolds": N_SCAFFOLD,
        "total": N_TOTAL,
    },
    "models_1_to_4_cutoffs": {
        "cai_top20_cutoff": cai_cut,
        "mfe_top20_cutoff_kcal_per_mol": mfe_cut,
        "chaperone_load_top20_cutoff": chap_cut,
        "promoter_sp_prior_top20_cutoff": prior_cut,
    },
    "concordance_n4_distribution_pre_esm2": {str(k): v for k, v in conc_dist_4.items()},
    "protein_distinct_combinations_total": len(all_protein_keys),
    "protein_distinct_combinations_pre_filter_n4_ge_2": len(protein_keys_needed),
    "esm2_step": "pending -- run run_esm2.py next",
}
with (RESULTS / "summary_pre_esm2.json").open("w") as f:
    json.dump(summary_pre, f, indent=2)
print(f"  Wrote pre-ESM2 summary to {RESULTS / 'summary_pre_esm2.json'}")

print("\n=== analyze.py complete. Run run_esm2.py next. ===")
EOF
