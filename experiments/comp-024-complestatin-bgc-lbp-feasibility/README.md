# comp-024: Complestatin-family BGC heterologous expression feasibility in engineered-LBP chassis

**Question:** Is the complestatin-family NRPS biosynthetic gene cluster heterologous-expression-tractable in an engineered LBP chassis (*E. coli* Nissle 1917, *Bacteroides thetaiotaomicron*) as the next CP0 (complement priming) engineering payload?

**Verdict (top-line):** **YELLOW at best host (EcN, 0.544); RED in Bacteroides (0.225); RED for the original framing of complestatin BGC as next LBP-chassis CP0 payload.** The dominant blocking factor for both hosts is **O2-dependent tailoring chemistry** (ComI/ComJ P450 oxidative phenolic coupling + ComH nonheme halogenase + Hmo FMN oxidase) being fundamentally incompatible with the colonic-anaerobic-resident lifestyle. Without P450-mediated phenolic coupling, the linear peptide lacks the rigid crosslinked architecture that gives complestatin its C1q/C4b affinity (Park 2016 deletion derivatives M55/S56 are biologically inactive).

**More-tractable parallel:** The C1-INH (LBP-luminal) thread scores GREEN at 0.774 on EcN — substantially more tractable than complestatin BGC at 0.544. Recommendation: promote C1-INH to a real comp-NNN protease-stability analysis (parallel to comp-006 DAF/CD55), and park complestatin BGC as an aerobic-fermentation-production candidate (food-grade or pharma-grade actinomycete chassis), not as an LBP-track payload.

**Status:** **Complete 2026-05-16.** Single-pass computational feasibility; no wet lab.

**Reproducible artifact:** `python3 analyze.py` from this folder.

**Interpretive wiki page:** [`wiki/complestatin-bgc-lbp-feasibility-computational.md`](../../wiki/complestatin-bgc-lbp-feasibility-computational.md)

**Tracking index:** [`wiki/computational-experiments.md`](../../wiki/computational-experiments.md) — comp-024 row promoted from Planned to Analyses

---

## Why this experiment exists

comp-018 (2026-05-08) surfaced complestatin-family BGC heterologous expression in the engineered-LBP chassis peer track as one of two named-but-unscoped engineering parallel threads to H05 DAF SCR1-4 (the other being C1-INH recombinant expression). The framing was: **add a third mechanism class to CP0 coverage** (engineering DAF SCR1-4 + dietary rosmarinic acid + bacterial complestatin NRPS), each via a distinct chassis.

The user direction for comp-024: is the complestatin BGC tractable in the LBP chassis, or is the C1-INH thread the better next CP0 payload?

---

## Method

| Step | What | Tool |
|---|---|---|
| 1 | Identify complestatin BGC architecture from MIBiG + primary literature | manual + WebFetch |
| 2 | Encode BGC architecture (cluster size, NRPS modules, tailoring enzymes, precursor-supply genes) as `inputs/bgc_architecture.json` | manual |
| 3 | Encode candidate-host profiles (EcN, Bacteroides) with engineering toolkit, GC content, native precursor supply, O2 lifestyle, PPTase, P450 redox | manual |
| 4 | Score nine feasibility factors per host (0.0 catastrophic → 1.0 no obstacle) | `analyze.py` |
| 5 | Geometric mean across factors → overall feasibility score | `analyze.py` |
| 6 | Apply GREEN/YELLOW/RED thresholds (≥0.60 / 0.30–0.59 / <0.30) | `analyze.py` |
| 7 | Comparator: same framework applied to C1-INH (LBP-luminal) parallel thread | `analyze.py` |
| 8 | Generate `outputs/results.json` + `outputs/summary.md` | `analyze.py` |

**Why geometric mean.** Every factor must succeed for the engineering campaign to deliver a functional product. Arithmetic mean would let a single fundamental-incompatibility factor (e.g., O2 dependence at 0.05) be swamped by mature-tooling factors at 0.9. Geometric mean is the right composition rule for multiplicative-success engineering campaigns.

**Why nine factors.** The factor set was chosen to span the engineering campaign's full surface — DNA-level tractability (cluster size, GC content), enzymatic compatibility (PPTase, P450 redox), substrate supply (non-canonical amino acids), host-physiology fit (O2 dependence vs. anaerobe lifestyle), engineering-environment maturity (toolkit, precedent), and product-host interaction (toxicity / self-resistance). Each factor reflects a known load-bearing question in NRPS heterologous expression literature.

## Files

```
experiments/comp-024-complestatin-bgc-lbp-feasibility/
├── README.md                       (this file)
├── analyze.py                      (stdlib-only scoring script)
├── inputs/
│   ├── bgc_architecture.json       (Chiu 2001 + Park 2016 + MIBiG BGC0000326)
│   ├── chassis_profiles.json       (EcN / Bacteroides / F. prausnitzii reference profiles + C1-INH comparator)
│   └── provenance.md               (source / version / fetch-date table; load-bearing number verification)
└── outputs/
    ├── results.json                (machine-readable: factor scores, geometric means, verdicts per host)
    └── summary.md                  (human-readable: headline, BGC architecture, scoring tables, wet-lab handoff)
```

## How to reproduce

```bash
cd experiments/comp-024-complestatin-bgc-lbp-feasibility/
python3 analyze.py
```

Outputs land in `outputs/`. Stdlib only — no `pip install` required.

## Limitations

See `inputs/provenance.md` §"Limitations of input data" for the full list. Headline limitations:

1. **Module substrate specificity is partly inferred** from sequence homology to vancomycin/chloroeremomycin-class NRPSs (Trauger & Walsh 2000), not all individually validated in vitro for complestatin specifically.
2. **β-hydroxytyrosine biosynthesis gene is inferred** (OxyD-class P450), not explicitly annotated in Chiu 2001.
3. **Factor scores are expert estimates**, not derived from large-scale heterologous-expression empirical datasets. The geometric mean is robust to ±0.1 variation in individual scores but the verdict could shift if any factor is meaningfully miscalibrated. See `outputs/summary.md` for the per-factor justifications.
4. **No precedent for complestatin BGC in E. coli or Bacteroides** — the negative-evidence factor scoring (0.35 EcN, 0.10 Bacteroides) reflects literature-search outcomes, not direct demonstration of failure. Absence of precedent ≠ proof of infeasibility, only that no validated path exists today.
5. **Aerobic-fermentation production route is out of scope.** This analysis is specifically about LBP-chassis (in-situ luminal) expression. If the question were "can complestatin be produced in *S. lividans* TK24 or *E. coli* under aerobic fermentation," the verdict would be very different — Park 2016 already demonstrated *S. lividans* works.
6. **CAI values are genus-typical estimates**, ±0.1.

## Cross-references

- Originating context: [`wiki/upstream-complement-modulator-sweep-computational.md`](../../wiki/upstream-complement-modulator-sweep-computational.md) (comp-018) — surfaced the complestatin engineering thread
- Chassis class: [`wiki/engineered-lbp-chassis.md`](../../wiki/engineered-lbp-chassis.md) — defines the LBP track architecture
- Sister hypothesis: [`wiki/hypotheses/H05-daf-scr14-cp0-thesis.md`](../../wiki/hypotheses/H05-daf-scr14-cp0-thesis.md) — koji-secreted DAF SCR1-4, the primary CP0 engineering payload
- CP0 framework: [`wiki/complement-c5a-gout.md`](../../wiki/complement-c5a-gout.md) — chokepoint definition + therapeutic landscape
- Comparator analysis: [`wiki/daf-cd55-protease-stability-computational.md`](../../wiki/daf-cd55-protease-stability-computational.md) (comp-006) — methodology pattern for C1-INH follow-up
- Computational tracking: [`wiki/computational-experiments.md`](../../wiki/computational-experiments.md)
