# comp-008: *Faecalibacterium prausnitzii* heterologous expression feasibility

**Question:** Is *F. prausnitzii* A2-165 (= *F. duncaniae* per Sakamoto 2022) engineering-tractable for OE-relevant payloads (uricase, lactoferrin, soluble CR1 SCR1-4, butyryl-CoA:acetate CoA-transferase), and which payloads rank highest by composite feasibility?

**Verdict (top-line):**

| Payload | Composite (base) | Range | Verdict |
|---|---|---|---|
| Butyrate-pathway boost (native BCoAT) | **0.748** | [0.641, 0.822] | **GREEN** |
| sCR1 SCR1-4 truncation | 0.565 | [0.433, 0.678] | YELLOW |
| Human lactoferrin | 0.540 | [0.423, 0.659] | YELLOW |
| *A. flavus* uricase | 0.393 | [0.271, 0.523] | YELLOW (toward RED) |

**Winner: butyrate-pathway boost (native BCoAT overexpression).** It is the only GREEN payload at the base score and remains GREEN with the toolkit gap excluded — the native-payload factors (CAI=1.0, native physiology, native pathway, no secretion, no disulfides) carry the geometric mean through the shared engineering-toolkit-maturity drag.

**Most surprising finding: uricase scores LOW, and the bottleneck is the host-physiology mismatch (uricase requires molecular O2; F. prausnitzii is a strict anaerobe), not the engineering toolkit.** Even with a perfect transformation toolkit, the chemistry can't run in the anoxic colonic lumen. This is a strategic reclassification — uricase should be removed from the F. prausnitzii payload menu and held on the koji track or moved to a facultative-anaerobe LBP chassis (*E. coli* Nissle).

**Status:** **Complete 2026-05-16.** Single-pass computational feasibility; no wet lab.

**Reproducible artifact:** `python3 analyze.py` from this folder.

**Interpretive wiki page:** [`wiki/f-prausnitzii-heterologous-expression-computational.md`](../../../f-prausnitzii-heterologous-expression-computational.md)

**Tracking index:** [`wiki/computational-experiments.md`](../../../computational-experiments.md) — comp-008 row promoted from Planned to Analyses

---

## Why this experiment exists

`wiki/engineered-lbp-chassis.md` (2026-05-05) established the engineered Live Biotherapeutic Product chassis as a peer track to koji and named *F. prausnitzii* as the primary candidate species. Phase 2 follow-up P2-4 was queued: a computational feasibility analysis of OE-relevant payloads in F. prausnitzii — codon usage, GC content, secretion machinery, transformation toolkit maturity, payload tractability ranking.

This comp populates that follow-up.

---

## Method

| Step | What | Tool |
|---|---|---|
| 1 | Identify OE-relevant payloads from `wiki/engineered-lbp-chassis.md` §"Other plausible payloads (Phase 2 to scope)" | manual |
| 2 | Fetch UniProt sequence + functional metadata for each payload (Q00511 uricase, P02788 lactoferrin, P17927 CR1, C7H5K4 BCoAT) | UniProt REST + WebFetch |
| 3 | Encode chassis profile (genome stats, physiology, secretion machinery, toolkit maturity) from Fraccascia 2022, Sheridan 2023, Martín 2023, Quévrain 2016 | manual + PubMed + Paperclip |
| 4 | Score eight feasibility factors per payload (0.0 catastrophic to 1.0 no obstacle), with sensitivity ranges (low/high) for each | `analyze.py` |
| 5 | Geometric mean across factors -> composite feasibility score | `analyze.py` |
| 6 | Apply GREEN/YELLOW/RED thresholds (≥0.60 / 0.30–0.59 / <0.30) | `analyze.py` |
| 7 | Compute toolkit-conditional ranking (excludes the shared engineering-toolkit factor) | `analyze.py` |
| 8 | Generate `outputs/results.json` + `outputs/summary.md` | `analyze.py` |

**Why geometric mean.** Every factor must succeed for the engineering campaign to deliver a functional product. Arithmetic mean would let a single fundamental-incompatibility factor (e.g., uricase's O2 requirement at 0.10) be swamped by mature-tooling factors at 0.9. Geometric mean is the right composition rule for multiplicative-success engineering campaigns. (Same rationale as comp-024.)

**Why eight factors.** The factor set spans the engineering campaign surface — DNA-level tractability (cluster size, GC content), enzymatic / physiological compatibility (secretion pathway, host physiology, folding complexity), engineering environment (toolkit maturity, precedent), and host-product interaction (toxicity / fitness).

**Why a toolkit-conditional ranking is reported alongside the base.** The engineering-toolkit gap is a FIXED FACILITY cost — pay it once (estimated 1-2 yr investment to adapt the Lachnospiraceae conjugation protocol), and every payload's score lifts. Reporting the base ranking only would understate the conditional payload ordering after that toolkit is built. Both rankings inform different strategic decisions.

## Files

```
experiments/comp-008-f-prausnitzii-heterologous-expression/
├── README.md                       (this file)
├── analyze.py                      (stdlib-only scoring script)
├── inputs/
│   ├── payloads.json               (4 payload metadata records; UniProt-verified)
│   ├── chassis_profile.json        (F. prausnitzii A2-165 / F. duncaniae profile)
│   └── provenance.md               (source / version / fetch-date table; load-bearing number verification)
└── outputs/
    ├── results.json                (machine-readable: per-payload scores, ranges, verdicts, ranking)
    └── summary.md                  (human-readable: headline, chassis profile, per-payload analysis, roadmap)
```

## How to reproduce

```bash
cd experiments/comp-008-f-prausnitzii-heterologous-expression/
python3 analyze.py
```

Outputs land in `outputs/`. Stdlib only — no `pip install` required.

## Limitations

See `inputs/provenance.md` §"Limitations of input data" and `outputs/summary.md` §"Limitations" for the full list. Headline limitations:

1. **Factor scores are expert estimates**, not derived from large-scale empirical heterologous-expression datasets in F. prausnitzii (which don't exist). Sensitivity ranges (low/high) per factor are documented in the JSON output.
2. **CAI values are framework-estimated**, not RSCU-table-computed. Wet-lab cassette design needs a proper codon-frequency table.
3. **Disulfide-folding-in-anoxic-environment** is an open empirical question for lactoferrin and sCR1 scoring.
4. **The engineering-toolkit-maturity factor (0.25 across payloads) is the dominant variance source.** A 2026-27 transformation-protocol publication for F. prausnitzii would lift every score by ~0.10-0.15.
5. **No F. prausnitzii transformation-efficiency baseline** — Roseburia inulinivorans conjugation efficiency (10^-4 to 10^-6 per recipient per Sheridan 2019) is the proxy.

## Cross-references

- Originating context: [`wiki/engineered-lbp-chassis.md`](../../../engineered-lbp-chassis.md) §"Other plausible payloads (Phase 2 to scope)" and §"Open Follow-Ups" P2-4 — surfaced this comp as the chassis Phase 2 feasibility analysis
- Hypothesis card: [`wiki/hypotheses/H02-engineered-lbp-thesis.md`](../../../hypotheses/H02-engineered-lbp-thesis.md) — engineered LBP thesis (stub)
- Sister analyses (other chassis): [`wiki/dual-chassis-ecn-pdb-uricase-computational.md`](../../../dual-chassis-ecn-pdb-uricase-computational.md) (comp-031, E. coli Nissle + Pediococcus uricase), [`wiki/c-utilis-uricase-cassette-compatibility-computational.md`](../../../c-utilis-uricase-cassette-compatibility-computational.md) (comp-011, C. utilis uricase cassette)
- Payload precedents: [`wiki/uricase.md`](../../../uricase.md) (uricase mechanism), [`wiki/lactoferrin.md`](../../../lactoferrin.md) (lactoferrin TNFα-cycle relief), [`wiki/complement-c5a-gout.md`](../../../complement-c5a-gout.md) (CP0 framework), [`wiki/purine-degrading-bacteria.md`](../../../purine-degrading-bacteria.md) (purine degradation in commensals)
- Computational tracking: [`wiki/computational-experiments.md`](../../../computational-experiments.md) — comp-008 promoted from Planned to Analyses
- Comparator method: [`experiments/comp-024-complestatin-bgc-lbp-feasibility/`](../comp-024-complestatin-bgc-lbp-feasibility/) — same geometric-mean rubric, applied to a different chassis x payload question
