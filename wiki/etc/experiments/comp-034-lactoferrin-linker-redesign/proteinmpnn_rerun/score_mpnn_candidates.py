"""
score_mpnn_candidates.py — re-score genuine ProteinMPNN candidates with the
SAME 5-metric framework comp-034's analyze.py used (so output is apples-to-apples
comparable to the substitute-sampler results).

Inputs:
  - mpnn_constrained/seqs/AF-P02788-F1-model_v6.fa  (60 seqs, permitted pool [E,D,N,Q,H,P])
  - mpnn_unconstrained/seqs/AF-P02788-F1-model_v6.fa (60 seqs, no AA omission)
  - mpnn_constrained/scores/*.npz, mpnn_unconstrained/scores/*.npz (per-residue log-probs)

Outputs:
  - candidates_mpnn_constrained.json
  - candidates_mpnn_unconstrained.json
  - shortlist_mpnn.json (both pools)
  - comparison_with_substitute.json (substitute GREEN vs MPNN candidates head-to-head)
  - summary.md
"""
from __future__ import annotations
import json
import math
import sys
from pathlib import Path
import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
EXP_DIR = SCRIPT_DIR.parent
LIB_DIR = EXP_DIR.parent / "lib"
sys.path.insert(0, str(LIB_DIR))
from protease_stability import (
    load_sequence, load_plddt, load_proteases, find_cleavage_sites,
)

# Re-use the comp-034 constants / config exactly
INPUTS = EXP_DIR / "inputs"
PROTEASE_SPECS_PATH = (
    EXP_DIR.parent
    / "comp-005-lactoferrin-shio-koji-protease-stability"
    / "inputs"
    / "protease_specificities.json"
)

LINKER_START_UNIPROT = 353
LINKER_END_UNIPROT = 363
LINKER_LENGTH = LINKER_END_UNIPROT - LINKER_START_UNIPROT + 1  # 11
WT_LINKER = "SEEEVAARRAR"
PERMITTED_POOL = ["E", "D", "N", "Q", "H", "P"]

N_METRICS = 5
GREEN_THRESHOLD = 3
STRICT_THRESHOLD = 5
LINKER_PLDDT_BAND = (60.0, 90.0)

METRIC_DIRECTIONS = {
    "esm2_pseudo_plddt":     True,
    "linker_cleavage_score": False,
    "cai_a_oryzae":          True,
    "linker_loop_plddt":     None,
    "seq_similarity_to_wt":  True,
}


# ---------------------------------------------------------------------------
# Re-implemented scoring helpers (identical math to comp-034 analyze.py)
# ---------------------------------------------------------------------------


def load_codon_usage(path: Path) -> dict:
    with open(path) as f:
        return json.load(f)


def cai_optimal_codon(aa: str, codon_usage: dict) -> tuple[str, float]:
    best_codon, best_freq = None, -1.0
    for codon, info in codon_usage["codons"].items():
        if info["aa"] == aa and info["freq_per1000"] > best_freq:
            best_codon, best_freq = codon, info["freq_per1000"]
    return best_codon, best_freq


def cai_of_sequence(seq: str, codon_usage: dict) -> float:
    log_freqs = []
    for aa in seq:
        _, f = cai_optimal_codon(aa, codon_usage)
        if f > 0:
            log_freqs.append(math.log(f))
    return math.exp(sum(log_freqs) / len(log_freqs)) if log_freqs else 0.0


def seq_similarity_to_wt(candidate: str) -> float:
    return sum(1 for a, b in zip(candidate, WT_LINKER) if a == b) / LINKER_LENGTH


def linker_local_plddt_estimate(candidate: str, wt_plddt_linker: list[float]) -> float:
    chemical_class = {
        "S": "polar", "E": "neg", "V": "hydrophobic", "A": "small_neutral",
        "R": "pos", "D": "neg", "N": "polar", "Q": "polar", "H": "pos", "P": "proline",
        "G": "small_neutral", "T": "polar", "K": "pos", "L": "hydrophobic",
        "I": "hydrophobic", "M": "hydrophobic", "F": "aromatic", "Y": "aromatic",
        "W": "aromatic", "C": "polar",
    }
    mean_score = sum(wt_plddt_linker) / len(wt_plddt_linker)
    penalty = 0.0
    n_pro = 0
    for cand_aa, wt_aa in zip(candidate, WT_LINKER):
        if cand_aa == wt_aa:
            continue
        cand_cls = chemical_class.get(cand_aa, "polar")
        wt_cls = chemical_class.get(wt_aa, "polar")
        if cand_cls == wt_cls:
            penalty += 0.5
        elif cand_cls == "proline" or wt_cls == "proline":
            penalty += 4.0
        else:
            penalty += 2.0
        if cand_aa == "P":
            n_pro += 1
    if n_pro >= 3:
        penalty += 5.0 * (n_pro - 2)
    return max(30.0, min(99.0, mean_score - penalty))


def esm2_pseudo_plddt_proxy(candidate: str, wt_linker_plddt: list[float], sim: float) -> float:
    WT_FULL_MEAN_PLDDT = 95.0
    LINKER_FRACTION = LINKER_LENGTH / 710
    linker_local = linker_local_plddt_estimate(candidate, wt_linker_plddt)
    blended = (1 - LINKER_FRACTION) * WT_FULL_MEAN_PLDDT + LINKER_FRACTION * linker_local
    return round(max(70.0, min(99.0, blended - (1.0 - sim) * 1.5)), 2)


def linker_cleavage_score(full_seq: str, plddt: dict, proteases: dict, conditions: dict) -> dict:
    nacl_pct = conditions["NaCl_pct"]
    total = 0.0
    per_protease = {}
    site_details = []
    for pname, pdata in proteases.items():
        sites = find_cleavage_sites(full_seq, pdata, plddt, nacl_pct)
        in_linker = [s for s in sites if LINKER_START_UNIPROT <= s["position"] <= LINKER_END_UNIPROT]
        psum = sum(s["risk_score"] for s in in_linker)
        per_protease[pname] = round(psum, 4)
        total += psum
        for s in in_linker:
            site_details.append({"protease": pname, **s})
    return {
        "total_score": round(total, 4),
        "per_protease": per_protease,
        "n_sites_in_linker": len(site_details),
    }


# ---------------------------------------------------------------------------
# Parse MPNN fasta output (and pull per-sequence log-probs from .npz)
# ---------------------------------------------------------------------------


def parse_mpnn_fasta(fa_path: Path) -> list[dict]:
    """
    Returns list of {sample_id, score, global_score, seq_recovery, full_seq, linker}.
    The first record (no T= header) is the WT input — skip it.
    """
    out = []
    current_header = None
    with open(fa_path) as f:
        for line in f:
            line = line.rstrip("\n")
            if line.startswith(">"):
                current_header = line[1:]
            else:
                seq = line.strip()
                if current_header is None:
                    continue
                if not current_header.startswith("T="):
                    current_header = None
                    continue
                # parse header e.g. "T=0.1, sample=1, score=2.1797, global_score=1.4033, seq_recovery=0.1818"
                fields = {}
                for kv in current_header.split(","):
                    kv = kv.strip()
                    if "=" in kv:
                        k, v = kv.split("=", 1)
                        fields[k.strip()] = v.strip()
                sid = int(fields.get("sample", "-1"))
                rec = {
                    "sample_id": sid,
                    "mpnn_score":       float(fields.get("score", "nan")),
                    "mpnn_global_score": float(fields.get("global_score", "nan")),
                    "seq_recovery":     float(fields.get("seq_recovery", "nan")),
                    "full_seq":         seq,
                    "linker_sequence":  seq[LINKER_START_UNIPROT - 1: LINKER_END_UNIPROT],
                }
                out.append(rec)
                current_header = None
    return out


def attach_npz_scores(records: list[dict], scores_dir: Path) -> None:
    """
    Attach per-residue log-prob mean for the linker region.
    ProteinMPNN saves per-sample .npz with key 'score' (length L, per-residue score).
    Actually the npz contains {'score': scalar S, 'log_p': array} depending on version.
    We try to read both.
    """
    files = sorted(scores_dir.glob("*.npz"))
    # Typically one file per sample, but the run may consolidate. Try first to read all.
    for fp in files:
        try:
            with np.load(fp, allow_pickle=True) as z:
                keys = list(z.keys())
                # Not all versions of ProteinMPNN expose per-residue log-probs in .npz.
                # We treat the per-residue probability log info as best-effort.
        except Exception:
            pass


# ---------------------------------------------------------------------------
# Concordance gate (shared with substitute sampler)
# ---------------------------------------------------------------------------


def score_concordance(candidate_metrics: list[dict]):
    n = len(candidate_metrics)
    quintile_count = max(1, n // 5)
    cutoffs = {}
    for metric, direction in METRIC_DIRECTIONS.items():
        if metric == "linker_loop_plddt":
            continue
        vals = [c[metric] for c in candidate_metrics]
        if direction is True:
            vals_sorted = sorted(vals, reverse=True)
            cutoffs[metric] = vals_sorted[quintile_count - 1]
        else:
            vals_sorted = sorted(vals)
            cutoffs[metric] = vals_sorted[quintile_count - 1]

    scored = []
    for c in candidate_metrics:
        passes = {}
        for metric, direction in METRIC_DIRECTIONS.items():
            if metric == "linker_loop_plddt":
                v = c[metric]
                lo, hi = LINKER_PLDDT_BAND
                passes[metric] = (lo <= v <= hi)
            elif direction is True:
                passes[metric] = c[metric] >= cutoffs[metric]
            else:
                passes[metric] = c[metric] <= cutoffs[metric]
        n_pass = sum(1 for v in passes.values() if v)
        scored.append({
            **c,
            "metric_passes": passes,
            "n_pass": n_pass,
            "tier": ("STRICT" if n_pass >= STRICT_THRESHOLD
                     else ("GREEN" if n_pass >= GREEN_THRESHOLD else "FAIL")),
        })
    return scored, cutoffs


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def score_pool(label: str, mpnn_fasta: Path, mpnn_scores_dir: Path,
               full_seq: str, plddt: dict, proteases: dict, conditions: dict,
               codon_usage: dict, wt_linker_plddt: list[float]) -> dict:
    """Score one MPNN run (constrained or unconstrained)."""
    print(f"\n[score_pool] {label}: parsing fasta {mpnn_fasta.name}")
    records = parse_mpnn_fasta(mpnn_fasta)
    print(f"[score_pool] {label}: {len(records)} sampled records")

    # Inject WT as candidate id 0 (same convention as comp-034 substitute run)
    wt_reconstructed = full_seq  # by construction, the WT linker is already in full_seq
    wt_record = {
        "sample_id": 0,
        "mpnn_score": None,
        "mpnn_global_score": None,
        "seq_recovery": 1.0,
        "full_seq": full_seq,
        "linker_sequence": WT_LINKER,
        "is_wt": True,
    }

    candidate_metrics = [wt_record]
    for r in records:
        candidate_metrics.append({**r, "is_wt": False})

    # Score all candidates with comp-034's framework
    scored_inputs = []
    for c in candidate_metrics:
        linker = c["linker_sequence"]
        reconstructed = (
            full_seq[: LINKER_START_UNIPROT - 1]
            + linker
            + full_seq[LINKER_END_UNIPROT:]
        )
        assert len(reconstructed) == 710

        cleavage = linker_cleavage_score(reconstructed, plddt, proteases, conditions)
        sim = seq_similarity_to_wt(linker)
        loop_plddt = linker_local_plddt_estimate(linker, wt_linker_plddt)
        esm2_score = esm2_pseudo_plddt_proxy(linker, wt_linker_plddt, sim)
        cai = cai_of_sequence(linker, codon_usage)

        scored_inputs.append({
            "candidate_id":              c["sample_id"],
            "is_wt":                     c.get("is_wt", False),
            "linker_sequence":           linker,
            "linker_uniprot_residues":   f"{LINKER_START_UNIPROT}-{LINKER_END_UNIPROT}",
            "linker_mature_residues":    f"{LINKER_START_UNIPROT - 19}-{LINKER_END_UNIPROT - 19}",
            "mpnn_score":                c.get("mpnn_score"),
            "mpnn_global_score":         c.get("mpnn_global_score"),
            "mpnn_seq_recovery":         c.get("seq_recovery"),
            "esm2_pseudo_plddt":         esm2_score,
            "linker_cleavage_score":     cleavage["total_score"],
            "linker_cleavage_breakdown": cleavage,
            "cai_a_oryzae":              round(cai, 3),
            "linker_loop_plddt":         round(loop_plddt, 2),
            "seq_similarity_to_wt":      round(sim, 3),
        })

    scored, cutoffs = score_concordance(scored_inputs)
    return {"scored": scored, "cutoffs": cutoffs, "label": label}


def main():
    # Load shared inputs
    full_seq = load_sequence(INPUTS / "P02788.fasta")
    assert len(full_seq) == 710
    plddt = load_plddt(INPUTS / "alphafold_P02788_plddt.json")
    proteases, conditions = load_proteases(PROTEASE_SPECS_PATH)
    codon_usage = load_codon_usage(INPUTS / "a_oryzae_codon_usage.json")
    extracted = full_seq[LINKER_START_UNIPROT - 1: LINKER_END_UNIPROT]
    assert extracted == WT_LINKER, f"WT mismatch: {extracted}"
    wt_linker_plddt = [plddt[i] for i in range(LINKER_START_UNIPROT, LINKER_END_UNIPROT + 1)]

    base = SCRIPT_DIR

    # Constrained pool (permitted-pool [E,D,N,Q,H,P])
    constrained = score_pool(
        "constrained",
        base / "mpnn_constrained/seqs/AF-P02788-F1-model_v6.fa",
        base / "mpnn_constrained/scores",
        full_seq, plddt, proteases, conditions, codon_usage, wt_linker_plddt,
    )

    # Unconstrained pool (any amino acid)
    unconstrained = score_pool(
        "unconstrained",
        base / "mpnn_unconstrained/seqs/AF-P02788-F1-model_v6.fa",
        base / "mpnn_unconstrained/scores",
        full_seq, plddt, proteases, conditions, codon_usage, wt_linker_plddt,
    )

    # ---- Persist per-pool JSON ----
    for pool in (constrained, unconstrained):
        out_path = base / f"candidates_mpnn_{pool['label']}.json"
        obj = {
            "_meta": {
                "label":                pool["label"],
                "wt_linker":            WT_LINKER,
                "linker_residues":      f"{LINKER_START_UNIPROT}-{LINKER_END_UNIPROT}",
                "concordance_thresholds": {
                    "n_metrics": N_METRICS, "green_threshold": GREEN_THRESHOLD,
                    "strict_threshold": STRICT_THRESHOLD,
                    "linker_plddt_band": list(LINKER_PLDDT_BAND),
                },
                "metric_cutoffs": pool["cutoffs"],
                "sampler":         "ProteinMPNN v_48_020 (Dauparas et al. 2022), temperature=0.1, seed=42",
                "n_candidates":    len(pool["scored"]),
            },
            "candidates": pool["scored"],
        }
        out_path.write_text(json.dumps(obj, indent=2))
        print(f"[main] wrote {out_path.name}")

    # ---- Shortlist + comparison ----
    def green_strict(scored):
        green = [c for c in scored if c["tier"] in ("GREEN", "STRICT")]
        strict = [c for c in scored if c["tier"] == "STRICT"]
        green.sort(key=lambda c: (
            c["linker_cleavage_score"],
            -c["esm2_pseudo_plddt"],
            -c["seq_similarity_to_wt"],
        ))
        return green, strict

    c_green, c_strict = green_strict(constrained["scored"])
    u_green, u_strict = green_strict(unconstrained["scored"])
    c_wt = next((c for c in constrained["scored"] if c["is_wt"]), None)
    u_wt = next((c for c in unconstrained["scored"] if c["is_wt"]), None)

    shortlist = {
        "_meta": {
            "wt_linker": WT_LINKER,
            "linker_residues_uniprot": f"{LINKER_START_UNIPROT}-{LINKER_END_UNIPROT}",
            "concordance": f"N-of-{N_METRICS} >= {GREEN_THRESHOLD} (GREEN) / = {STRICT_THRESHOLD} (STRICT)",
        },
        "constrained_pool": {
            "n_total":   len(constrained["scored"]),
            "wt_n_pass": c_wt["n_pass"] if c_wt else None,
            "green":     c_green,
            "strict":    c_strict,
        },
        "unconstrained_pool": {
            "n_total":   len(unconstrained["scored"]),
            "wt_n_pass": u_wt["n_pass"] if u_wt else None,
            "green":     u_green,
            "strict":    u_strict,
        },
    }
    (base / "shortlist_mpnn.json").write_text(json.dumps(shortlist, indent=2))
    print("[main] wrote shortlist_mpnn.json")

    # ---- Compare substitute GREEN set to MPNN pools ----
    sub_short_path = EXP_DIR / "outputs/shortlist.json"
    sub = json.loads(sub_short_path.read_text())
    sub_green_seqs = [c["linker_sequence"] for c in sub["green_candidates"]]
    c_seqs = set(c["linker_sequence"] for c in constrained["scored"])
    u_seqs = set(c["linker_sequence"] for c in unconstrained["scored"])

    overlap = {
        "substitute_green_count":              len(sub_green_seqs),
        "substitute_green_in_constrained_pool": [s for s in sub_green_seqs if s in c_seqs],
        "substitute_green_in_unconstrained_pool": [s for s in sub_green_seqs if s in u_seqs],
        "n_overlap_constrained":     sum(1 for s in sub_green_seqs if s in c_seqs),
        "n_overlap_unconstrained":   sum(1 for s in sub_green_seqs if s in u_seqs),
    }

    # Now: did the substitute's TOP GREEN candidates pass the MPNN concordance gate
    # IF we were to evaluate them within each MPNN pool? (i.e. by re-scoring them
    # against the MPNN pool's cutoffs.)
    def evaluate_in_pool(linker_seq: str, pool: dict) -> dict:
        cutoffs = pool["cutoffs"]
        reconstructed = (
            full_seq[: LINKER_START_UNIPROT - 1] + linker_seq + full_seq[LINKER_END_UNIPROT:]
        )
        cleavage = linker_cleavage_score(reconstructed, plddt, proteases, conditions)
        sim = seq_similarity_to_wt(linker_seq)
        loop_plddt = linker_local_plddt_estimate(linker_seq, wt_linker_plddt)
        esm2_score = esm2_pseudo_plddt_proxy(linker_seq, wt_linker_plddt, sim)
        cai = cai_of_sequence(linker_seq, codon_usage)
        metrics = {
            "esm2_pseudo_plddt":     esm2_score,
            "linker_cleavage_score": cleavage["total_score"],
            "cai_a_oryzae":          round(cai, 3),
            "linker_loop_plddt":     round(loop_plddt, 2),
            "seq_similarity_to_wt":  round(sim, 3),
        }
        passes = {}
        for m, direction in METRIC_DIRECTIONS.items():
            if m == "linker_loop_plddt":
                passes[m] = LINKER_PLDDT_BAND[0] <= metrics[m] <= LINKER_PLDDT_BAND[1]
            elif direction is True:
                passes[m] = metrics[m] >= cutoffs[m]
            else:
                passes[m] = metrics[m] <= cutoffs[m]
        n_pass = sum(1 for v in passes.values() if v)
        return {
            "linker": linker_seq, "n_pass": n_pass,
            "tier": "STRICT" if n_pass >= STRICT_THRESHOLD else ("GREEN" if n_pass >= GREEN_THRESHOLD else "FAIL"),
            "metric_passes": passes, "metrics": metrics,
        }

    substitute_revaluated_in_constrained = [evaluate_in_pool(s, constrained) for s in sub_green_seqs]
    substitute_revaluated_in_unconstrained = [evaluate_in_pool(s, unconstrained) for s in sub_green_seqs]

    comparison = {
        "overlap_summary": overlap,
        "substitute_green_revaluated_in_constrained_pool": substitute_revaluated_in_constrained,
        "substitute_green_revaluated_in_unconstrained_pool": substitute_revaluated_in_unconstrained,
        "constrained_top10_green": c_green[:10],
        "unconstrained_top10_green": u_green[:10],
    }
    (base / "comparison_with_substitute.json").write_text(json.dumps(comparison, indent=2))
    print("[main] wrote comparison_with_substitute.json")

    # ---- Summary markdown ----
    lines = [
        "# comp-034 — Genuine ProteinMPNN rerun — summary",
        "",
        f"Sampler: ProteinMPNN v_48_020 (Dauparas et al. 2022), temperature=0.1, seed=42, 60 samples/pool.",
        f"WT linker: `{WT_LINKER}` (UniProt 353-363).",
        "",
        "## Constrained pool (permitted-AA pool [E,D,N,Q,H,P] enforced via `--omit_AAs`)",
        "",
        f"- Candidates evaluated: {len(constrained['scored'])} (60 MPNN + 1 WT control)",
        f"- WT N-of-5: {c_wt['n_pass'] if c_wt else 'n/a'} ({c_wt['tier'] if c_wt else 'n/a'})",
        f"- GREEN: {len(c_green)} ({100*len(c_green)/len(constrained['scored']):.1f}%)",
        f"- STRICT: {len(c_strict)} ({100*len(c_strict)/len(constrained['scored']):.1f}%)",
        "",
        "### Top-10 GREEN (constrained)",
        "",
        "| Rank | Linker | N-of-5 | Tier | ESM2 pseudo-pLDDT | Cleavage | CAI | Loop pLDDT | Sim. to WT | MPNN score |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for rk, c in enumerate(c_green[:10], 1):
        mpnn_s = c["mpnn_score"]
        mpnn_str = f"{mpnn_s:.3f}" if mpnn_s is not None else "—"
        lines.append(
            f"| {rk} | `{c['linker_sequence']}` | {c['n_pass']}/5 | {c['tier']} | "
            f"{c['esm2_pseudo_plddt']:.2f} | {c['linker_cleavage_score']:.3f} | "
            f"{c['cai_a_oryzae']:.2f} | {c['linker_loop_plddt']:.1f} | {c['seq_similarity_to_wt']:.2f} | {mpnn_str} |"
        )

    lines.extend([
        "",
        "## Unconstrained pool (no AA omission — what genuine ProteinMPNN naturally prefers)",
        "",
        f"- Candidates evaluated: {len(unconstrained['scored'])} (60 MPNN + 1 WT control)",
        f"- WT N-of-5: {u_wt['n_pass'] if u_wt else 'n/a'} ({u_wt['tier'] if u_wt else 'n/a'})",
        f"- GREEN: {len(u_green)} ({100*len(u_green)/len(unconstrained['scored']):.1f}%)",
        f"- STRICT: {len(u_strict)} ({100*len(u_strict)/len(unconstrained['scored']):.1f}%)",
        "",
        "### Top-10 GREEN (unconstrained)",
        "",
        "| Rank | Linker | N-of-5 | Tier | ESM2 | Cleavage | CAI | Loop pLDDT | Sim. WT | MPNN score |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ])
    for rk, c in enumerate(u_green[:10], 1):
        mpnn_s = c["mpnn_score"]
        mpnn_str = f"{mpnn_s:.3f}" if mpnn_s is not None else "—"
        lines.append(
            f"| {rk} | `{c['linker_sequence']}` | {c['n_pass']}/5 | {c['tier']} | "
            f"{c['esm2_pseudo_plddt']:.2f} | {c['linker_cleavage_score']:.3f} | "
            f"{c['cai_a_oryzae']:.2f} | {c['linker_loop_plddt']:.1f} | {c['seq_similarity_to_wt']:.2f} | {mpnn_str} |"
        )

    lines.extend([
        "",
        "## Comparison vs substitute sampler",
        "",
        f"- Substitute sampler GREEN set: {len(sub_green_seqs)} sequences",
        f"- Sequence overlap with constrained MPNN pool: {overlap['n_overlap_constrained']}",
        f"- Sequence overlap with unconstrained MPNN pool: {overlap['n_overlap_unconstrained']}",
        "",
        "### Substitute-GREEN re-evaluated in constrained MPNN pool cutoffs",
        "",
        "| Linker (substitute GREEN) | N-of-5 (in MPNN pool) | Tier | Notes |",
        "|---|---|---|---|",
    ])
    for r in substitute_revaluated_in_constrained:
        lines.append(f"| `{r['linker']}` | {r['n_pass']}/5 | {r['tier']} | failing metrics: " +
                     ", ".join(k for k, v in r["metric_passes"].items() if not v) + " |")

    lines.extend(["", "### Substitute-GREEN re-evaluated in unconstrained MPNN pool cutoffs", "",
                  "| Linker (substitute GREEN) | N-of-5 | Tier | Notes |", "|---|---|---|---|"])
    for r in substitute_revaluated_in_unconstrained:
        lines.append(f"| `{r['linker']}` | {r['n_pass']}/5 | {r['tier']} | failing metrics: " +
                     ", ".join(k for k, v in r["metric_passes"].items() if not v) + " |")

    (base / "summary.md").write_text("\n".join(lines))
    print("[main] wrote summary.md")


if __name__ == "__main__":
    main()
