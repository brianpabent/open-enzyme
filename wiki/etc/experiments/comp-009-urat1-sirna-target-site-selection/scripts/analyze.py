#!/usr/bin/env python3
"""
comp-009: URAT1 mRNA target site selection for siRNA  (RERUN 2026-07-14)
========================================================================

Question: which 21-nt target sites on the ACTUAL SLC22A12 (URAT1) mRNA
(RefSeq NM_144585.4) satisfy the combined Reynolds + Ui-Tei + immunogenicity
filters and rank highest on a real-accessibility composite score?

WHY THIS IS A RERUN (comp-review 2026-07-14):
  The original comp-009 back-translated the URAT1 *protein* into an artificial
  most-frequent-codon CDS and scanned THAT. Because siRNA targeting is
  nucleotide-sequence-specific, every reported guide sequence was an artifact
  of the arbitrary codon choice and did not map to the real transcript. This
  rerun replaces the artificial CDS with the real NM_144585.4 mRNA (5'UTR +
  CDS + 3'UTR) and replaces the isolated-21-mer self-folding heuristic with a
  real ViennaRNA RNAplfold local-accessibility calculation over the full mRNA.

Inputs (in ../inputs/):
  - NM_144585.4_mrna.fasta : real human SLC22A12 mRNA, RefSeq NM_144585.4,
      transcript variant 1 (fetched from NCBI nuccore 2026-07-14). CDS is
      338..1999 (1-based) per the RefSeq annotation.
  - urat1_orthologs.fasta  : human/chimp/mouse/rat URAT1 protein sequences
      (used ONLY for a CDS-region amino-acid conservation *hint*, not a
      nucleotide-level cross-species-reuse claim).
  - design_parameters.json : Reynolds/Ui-Tei/immunogenicity thresholds.

Outputs (to ../outputs/):
  - target_sites.json : passing 21-mer windows with per-filter scores + region
  - shortlist.csv     : top-N ranked candidates
  - summary.md        : human-readable summary cited from the wiki page

Dependencies: ViennaRNA (NOT stdlib) for RNAplfold accessibility.
  uv venv; uv pip install ViennaRNA   (see README reproduction section)

Honest scope (unchanged limitations, now correctly labelled):
  - No off-target clearance: no seed-region search against the human
    transcriptome is performed. Guides are TARGET-SITE candidates only.
  - Conservation is amino-acid-level (region hint), not nucleotide-level
    ortholog-mRNA alignment; cross-species reuse must be verified on real
    ortholog transcripts before it can be claimed.
"""

from __future__ import annotations
import csv
import json
import math
import sys
from pathlib import Path

try:
    import RNA  # ViennaRNA
except ImportError:
    sys.exit("ERROR: ViennaRNA not installed. See README reproduction section "
             "(uv pip install ViennaRNA). This rerun requires real RNAplfold.")

EXP_DIR = Path(__file__).resolve().parent.parent
INPUTS = EXP_DIR / "inputs"
OUTPUTS = EXP_DIR / "outputs"
OUTPUTS.mkdir(exist_ok=True)

# RefSeq NM_144585.4 CDS annotation (1-based inclusive)
CDS_START = 338
CDS_END = 1999
WINDOW = 21
RNAPLFOLD_W = 80   # local folding window
RNAPLFOLD_L = 40   # max base-pair span


# ----------------------------------------------------------------------------
# FASTA parsing
# ----------------------------------------------------------------------------

def parse_fasta(path: Path) -> dict[str, str]:
    records: dict[str, str] = {}
    current_id, current_seq = None, []
    for line in path.read_text().splitlines():
        if line.startswith(">"):
            if current_id is not None:
                records[current_id] = "".join(current_seq)
            current_id = line[1:].split()[0]
            current_seq = []
        elif line.strip():
            current_seq.append(line.strip())
    if current_id is not None:
        records[current_id] = "".join(current_seq)
    return records


def species_from_header(header: str) -> str:
    h = header.upper()
    if "HUMAN" in h:
        return "human"
    if "PANTR" in h or "CHIMP" in h:
        return "chimp"
    if "MOUSE" in h:
        return "mouse"
    if "RAT" in h:
        return "rat"
    return header


def reverse_complement(seq: str) -> str:
    rna = seq.replace("T", "U")
    rc = {"A": "U", "U": "A", "G": "C", "C": "G"}
    return "".join(rc.get(b, "N") for b in reversed(rna))


def gc_content(seq: str) -> float:
    return 100.0 * sum(1 for b in seq if b in "GC") / len(seq) if seq else 0.0


# ----------------------------------------------------------------------------
# Reynolds + Ui-Tei positional scoring (unchanged — sequence rules are correct)
# ----------------------------------------------------------------------------

def reynolds_score(target_21mer: str) -> tuple[int, list[str]]:
    if len(target_21mer) != 21:
        return 0, []
    antisense = reverse_complement(target_21mer)
    passed, score = [], 0
    if 30 <= gc_content(target_21mer) <= 52:
        score += 1; passed.append("R1_GC30-52")
    if not any(target_21mer.count(b * 4) for b in "ACGT"):
        score += 1; passed.append("R2_no4runs")
    if len(antisense) >= 19 and antisense[18] == "A":
        score += 1; passed.append("R3_AS19=A")
    if len(antisense) >= 3 and antisense[2] == "A":
        score += 1; passed.append("R4_AS3=A")
    if len(antisense) >= 10 and antisense[9] == "U":
        score += 1; passed.append("R5_AS10=U")
    if len(antisense) >= 13 and antisense[12] != "G":
        score += 1; passed.append("R6_AS13!=G")
    if len(antisense) >= 19 and antisense[18] not in "GC":
        score += 1; passed.append("R7_AS19!=GC")
    if antisense and antisense[0] in "AU":
        score += 1; passed.append("R8_UI_AS1=AU")
    return score, passed


def ui_tei_au_count(antisense: str) -> int:
    return sum(1 for b in antisense[:7] if b in "AU") if len(antisense) >= 7 else 0


# ----------------------------------------------------------------------------
# Immunogenicity / TLR motif filter (unchanged)
# ----------------------------------------------------------------------------

TLR_MOTIFS = ["UGUGU", "GUCCUUCAA", "GUUGUGG", "UGUUGU"]


def has_immunogenic_motif(rna_seq: str) -> tuple[bool, list[str]]:
    rna = rna_seq.replace("T", "U")
    hits = [m for m in TLR_MOTIFS if m in rna]
    return (len(hits) > 0), hits


def is_gu_rich_window(rna_seq: str, window: int = 9, threshold: int = 7) -> bool:
    rna = rna_seq.replace("T", "U")
    for i in range(len(rna) - window + 1):
        if sum(1 for b in rna[i:i + window] if b in "GU") >= threshold:
            return True
    return False


# ----------------------------------------------------------------------------
# Real RNAplfold accessibility over the full mRNA
# ----------------------------------------------------------------------------

def rnaplfold_accessibility(mrna: str, u: int = WINDOW) -> dict[int, float]:
    """Return {end_position_1based: P(the u nt ending there are all unpaired)}
    using ViennaRNA RNAplfold. Higher = more accessible to RISC."""
    seq = mrna.replace("T", "U")
    md = RNA.md()
    md.window_size = RNAPLFOLD_W
    md.max_bp_span = RNAPLFOLD_L
    fc = RNA.fold_compound(seq, md, RNA.OPTION_WINDOW)
    access: dict[int, float] = {}

    def cb(v, v_size, i, maxsize, what, data):
        if what & RNA.PROBS_WINDOW_UP:
            # v[u] = probability the u-nt stretch ending at position i is unpaired
            if v is not None and len(v) > u and v[u] is not None:
                data[i] = float(v[u])
    fc.probs_window(u, RNA.PROBS_WINDOW_UP, cb, access)
    return access


# ----------------------------------------------------------------------------
# Cross-species conservation — AA-level REGION HINT only (relabelled)
# ----------------------------------------------------------------------------

def pairwise_identity(s1: str, s2: str) -> float:
    if not s1 or not s2:
        return 0.0
    n = min(len(s1), len(s2))
    return 100.0 * sum(1 for a, b in zip(s1[:n], s2[:n]) if a == b) / n


def aa_window_conservation(aa_start: int, aa_len: int,
                           seqs: dict[str, str]) -> dict[str, float]:
    human = seqs.get("human", "")
    h_win = human[aa_start:aa_start + aa_len]
    result = {"human": 100.0}
    for sp in ("chimp", "mouse", "rat"):
        s_win = seqs.get(sp, "")[aa_start:aa_start + aa_len]
        result[sp] = pairwise_identity(h_win, s_win) if len(s_win) >= aa_len else float("nan")
    return result


def region_of(start_1based: int, end_1based: int) -> str:
    """Classify a window by where its MIDPOINT falls."""
    mid = (start_1based + end_1based) // 2
    if mid < CDS_START:
        return "5'UTR"
    if mid > CDS_END:
        return "3'UTR"
    return "CDS"


def composite_score(reynolds: int, ui_tei_au: int, accessibility: float,
                    conservation_avg: float) -> float:
    return (3.75 * reynolds + 2.14 * ui_tei_au
            + 25.0 * accessibility + 0.30 * conservation_avg)


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------

def main() -> int:
    mrna_records = parse_fasta(INPUTS / "NM_144585.4_mrna.fasta")
    mrna_id, mrna = next(iter(mrna_records.items()))
    mrna = mrna.upper().replace("U", "T")
    print(f"Real mRNA: {mrna_id}  {len(mrna)} nt (CDS {CDS_START}-{CDS_END})",
          file=sys.stderr)

    ortho = parse_fasta(INPUTS / "urat1_orthologs.fasta")
    seqs: dict[str, str] = {}
    for header, seq in ortho.items():
        sp = species_from_header(header)
        if sp not in seqs or len(seq) > len(seqs[sp]):
            seqs[sp] = seq

    params = json.loads((INPUTS / "design_parameters.json").read_text())

    print("Running ViennaRNA RNAplfold accessibility over full mRNA...",
          file=sys.stderr)
    access = rnaplfold_accessibility(mrna, WINDOW)

    candidates: list[dict] = []
    # scan the full mRNA (5'UTR + CDS + 3'UTR); trim 30 nt from each end for
    # RNAplfold edge effects.
    for i in range(30, len(mrna) - WINDOW - 30):
        target = mrna[i:i + WINDOW]
        if "N" in target:
            continue
        start1, end1 = i + 1, i + WINDOW
        antisense = reverse_complement(target)

        r_score, r_passed = reynolds_score(target)
        au_count = ui_tei_au_count(antisense)
        has_tlr, tlr_hits = has_immunogenic_motif(antisense)
        gu_rich = is_gu_rich_window(antisense)
        immunogenic = has_tlr or gu_rich

        acc = access.get(end1, 0.0)  # P(unpaired) for the 21-mer ending at end1
        region = region_of(start1, end1)

        # conservation hint only for windows fully inside the CDS
        if region == "CDS" and start1 >= CDS_START and end1 <= CDS_END:
            aa_pos = (start1 - CDS_START) // 3
            aa_len = max(1, WINDOW // 3)
            cons = aa_window_conservation(aa_pos, aa_len, seqs)
            cons_nonhuman = [v for k, v in cons.items()
                             if k != "human" and not math.isnan(v)]
            cons_avg = sum(cons_nonhuman) / len(cons_nonhuman) if cons_nonhuman else 0.0
            aa_window = seqs.get("human", "")[aa_pos:aa_pos + aa_len]
        else:
            cons = {"chimp": float("nan"), "mouse": float("nan"), "rat": float("nan")}
            cons_avg = 0.0
            aa_window = ""

        candidates.append({
            "mrna_pos_1based": start1,
            "region": region,
            "aa_window_hint": aa_window,
            "target_sense_5to3": target.replace("T", "U"),
            "antisense_5to3": antisense,
            "gc_pct": round(gc_content(target), 1),
            "reynolds_score": r_score,
            "reynolds_passed": r_passed,
            "ui_tei_au_in_seed": au_count,
            "immunogenic": immunogenic,
            "tlr_motifs_hit": tlr_hits,
            "gu_rich": gu_rich,
            "rnaplfold_p_unpaired": round(acc, 4),
            "accessibility_score_0to1": round(acc, 3),
            "conservation_aa_hint_pct": {k: round(v, 1) if not math.isnan(v) else None
                                         for k, v in cons.items()},
            "conservation_nonhuman_avg": round(cons_avg, 1),
            "composite_score": round(composite_score(r_score, au_count, acc, cons_avg), 2),
        })

    total = len(candidates)
    after_gc = [c for c in candidates if 30 <= c["gc_pct"] <= 52]
    after_immuno = [c for c in after_gc if not c["immunogenic"]]
    filtered_out_immuno = len(after_gc) - len(after_immuno)
    after_homopolymer = [c for c in after_immuno if "R2_no4runs" in c["reynolds_passed"]]
    after_design_rules = [c for c in after_homopolymer
                          if c["reynolds_score"] >= 5 and c["ui_tei_au_in_seed"] >= 4]
    after_design_rules.sort(key=lambda c: c["composite_score"], reverse=True)

    shortlist: list[dict] = []
    min_sep = 60
    for c in after_design_rules:
        if all(abs(c["mrna_pos_1based"] - s["mrna_pos_1based"]) >= min_sep for s in shortlist):
            shortlist.append(c)
            if len(shortlist) >= params.get("output_shortlist_size", 10):
                break

    print(f"windows {total} | GC {len(after_gc)} | immuno {len(after_immuno)} | "
          f"homopol {len(after_homopolymer)} | rules {len(after_design_rules)} | "
          f"shortlist {len(shortlist)}", file=sys.stderr)

    region_counts = {r: sum(1 for c in shortlist if c["region"] == r)
                     for r in ("5'UTR", "CDS", "3'UTR")}

    full = {
        "metadata": {
            "experiment_id": "comp-009",
            "title": "URAT1 mRNA target site selection for siRNA (RERUN)",
            "date_run": "2026-07-14",
            "transcript": mrna_id,
            "transcript_length_nt": len(mrna),
            "cds_coords_1based": [CDS_START, CDS_END],
            "accessibility_method": f"ViennaRNA RNAplfold (u={WINDOW}, W={RNAPLFOLD_W}, L={RNAPLFOLD_L})",
            "window_size_nt": WINDOW,
            "windows_scored_total": total,
            "after_gc_filter": len(after_gc),
            "after_immunogenicity_filter": len(after_immuno),
            "filtered_out_by_immunogenicity": filtered_out_immuno,
            "after_homopolymer_exclusion": len(after_homopolymer),
            "after_design_rules_filter": len(after_design_rules),
            "shortlist_size": len(shortlist),
            "shortlist_region_counts": region_counts,
            "off_target_cleared": False,
            "conservation_level": "amino-acid region hint only (not nucleotide ortholog-mRNA alignment)",
        },
        "shortlist": shortlist,
        "all_passing_candidates": after_design_rules[:50],
    }
    (OUTPUTS / "target_sites.json").write_text(json.dumps(full, indent=2))

    with (OUTPUTS / "shortlist.csv").open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["rank", "mrna_pos_1based", "region", "target_sense_5to3",
                    "antisense_5to3", "gc_pct", "reynolds_score", "ui_tei_au_seed",
                    "rnaplfold_p_unpaired", "conservation_avg_hint", "composite_score"])
        for rank, c in enumerate(shortlist, start=1):
            w.writerow([rank, c["mrna_pos_1based"], c["region"], c["target_sense_5to3"],
                        c["antisense_5to3"], c["gc_pct"], c["reynolds_score"],
                        c["ui_tei_au_in_seed"], c["rnaplfold_p_unpaired"],
                        c["conservation_nonhuman_avg"], c["composite_score"]])

    L = [
        "# comp-009 — URAT1 mRNA target site selection — Summary (RERUN 2026-07-14)",
        "",
        f"**Transcript:** {mrna_id} ({len(mrna)} nt; CDS {CDS_START}-{CDS_END}). "
        f"**Accessibility:** real ViennaRNA RNAplfold (u={WINDOW}, W={RNAPLFOLD_W}, L={RNAPLFOLD_L}).",
        "",
        "> **This is a rerun.** The original comp-009 scanned an artificial "
        "back-translated CDS and its guide sequences did not map to the real "
        "transcript. This run uses the real NM_144585.4 mRNA (5'UTR + CDS + 3'UTR) "
        "and real local-accessibility folding.",
        "",
        "## Pipeline",
        "",
        f"- Sliding 21-nt windows over the full mRNA: **{total}** scored.",
        f"- Reynolds GC 30-52%: **{len(after_gc)}** survive.",
        f"- Immunogenicity (TLR7/8 + GU-rich): **{len(after_immuno)}** survive (kills {filtered_out_immuno}).",
        f"- 4-nt homopolymer exclusion: **{len(after_homopolymer)}** survive.",
        f"- Reynolds ≥5/8 AND Ui-Tei AU≥4/7: **{len(after_design_rules)}** survive.",
        f"- Composite ranking + 60-nt diversity: **{len(shortlist)}**-candidate shortlist "
        f"(regions: {region_counts}).",
        "",
        "## Verdict",
        "",
    ]
    if len(shortlist) >= 5:
        L += ["**GREEN (target-site availability only) — multiple viable real-transcript target sites.**", "",
              f"{len(shortlist)} candidate sites on the real NM_144585.4 mRNA survive Reynolds GC, "
              "Ui-Tei seed asymmetry, TLR/GU-rich immunogenicity, homopolymer exclusion, and rank on "
              "real RNAplfold accessibility. The H03 target-site-availability assumption is **supported "
              "on the real transcript** — but this is target-site availability ONLY, not a validated "
              "knockdown guide: **no off-target clearance was performed** (see Limitations), and "
              "cross-species reuse is an amino-acid-level hint, not a nucleotide-level claim."]
    elif len(shortlist) >= 2:
        L += ["**YELLOW — narrow real-transcript shortlist.**"]
    else:
        L += ["**RED — no viable real-transcript target-site shortlist.**"]

    L += ["", "## Top shortlist", "",
          "| Rank | mRNA pos | Region | Sense target (5'→3') | GC% | Reynolds | P(unpaired) | Cons hint | Score |",
          "|---|---|---|---|---|---|---|---|---|"]
    for rank, c in enumerate(shortlist, start=1):
        L.append(f"| {rank} | {c['mrna_pos_1based']} | {c['region']} | "
                 f"`{c['target_sense_5to3']}` | {c['gc_pct']} | {c['reynolds_score']}/8 | "
                 f"{c['rnaplfold_p_unpaired']} | {c['conservation_nonhuman_avg']}% | {c['composite_score']} |")

    L += ["", "## Limitations (correctly scoped)", "",
          "1. **No off-target clearance.** No seed-region (antisense pos 2-8) search against the human "
          "RefSeq transcriptome / 3'UTRome was performed (no local transcriptome BLAST DB in this "
          "environment). Guides are **target-site candidates only**, not off-target-cleared.",
          "2. **Conservation is an amino-acid REGION HINT** from the ortholog protein set, not a "
          "nucleotide-level alignment of ortholog mRNAs. A shared amino acid can differ at the wobble "
          "position, so cross-species siRNA reuse must be re-verified on real ortholog transcripts.",
          "3. **Accessibility** is RNAplfold local-window folding (Tafer 2008 correlation r≈0.6-0.7 with "
          "measured knockdown) — good for prioritisation, not absolute knockdown prediction.",
          "4. **Isoform:** transcript variant 1 (NM_144585.4) only; other SLC22A12 isoforms not scanned.",
          ""]
    (OUTPUTS / "summary.md").write_text("\n".join(L))
    print(f"Wrote outputs to {OUTPUTS}/", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
