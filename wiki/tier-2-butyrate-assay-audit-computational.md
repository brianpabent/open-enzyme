---
title: "Tier 2 Butyrate Assay Audit — Computational Literature Synthesis (comp-038)"
date: 2026-05-20
tags: [computational, assay-validation, quantification-ladder, butyrate, scfa, microbiome, agentic-literature-synthesis]
related:
  - computational-experiments.md
  - validation-experiments.md
  - quantification-ladder.md
  - genotype-informed-supplement-workflow.md
  - purine-degrading-bacteria.md
sources:
  - "comp-038 outputs/results.json and outputs/summary.md, 2026-05-20"
  - "PMID 23542733 — HPLC-UV SCFA + lactate method for in vitro fermentation supernatants"
  - "PMID 42041444 — electrochemical fecal SCFA profiling"
  - "PMID 41082646 — exhaled breath condensate SCFA correlation caution"
  - "Abcam ab65341 protocol v17a — generic FFA kit excludes acetic, propionic, and butyric acid"
---

# Tier 2 Butyrate Assay Audit — Computational Literature Synthesis (comp-038)

**Status:** Complete first pass — 2026-05-20. **Experiment folder:** [`etc/experiments/comp-038-tier-2-butyrate-assay-audit/`](./etc/experiments/comp-038-tier-2-butyrate-assay-audit/). **Output:** [`outputs/summary.md`](./etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs/summary.md).

## Question

Is there a Tier 2 butyrate quantification assay — colorimetric, enzymatic, breath-proxy, electrochemical, or other low-cost intermediate method — that can be validated against Tier 3 GC-MS for OE's stool, serum, breath, or culture-supernatant use cases?

## Verdict

**YELLOW.** A ready-to-adopt simple/home colorimetric or breath-based butyrate assay did **not** surface. Two plausible Tier 2 candidates did surface, but both require full-text/protocol review and paired GC-MS validation before wet-lab adoption:

| Candidate | Matrix fit | Verdict | Evidence status |
|---|---|---|---|
| HPLC-UV SCFA + lactate assay for bacterial culture supernatants | Culture supernatant / engineered-strain work | **YELLOW** | PubMed abstract reports mM-range matrix-matched calibration and use for butyric-acid-producing bacteria; full text and OE spike-recovery still required. |
| Electrochemical fecal SCFA profiling with ANN deconvolution | Stool / fecal SCFA profiling | **YELLOW** | Emerging fecal SCFA platform; needs full-text butyrate-specific performance, reference-method correlation, and external validation. |
| Butyric-acid / SCFA ELISA kits | Serum/plasma/vendor-claimed matrices | **RED-provisional** | Vendor claims exist, but no PubMed/GC-MS validation surfaced; small-molecule specificity is a major concern. |
| Breath H2/CH4 | Breath | **RED** | Broad fermentation/adherence proxy, not butyrate-specific quantification. |
| Generic free-fatty-acid colorimetric kits | Serum/plasma/culture, vendor-dependent | **RED** | Representative FFA kit protocol excludes SCFAs including butyric acid. |

## Why This Matters

The [quantification ladder](./quantification-ladder.md) needs a cheap Tier 2 surface between visual/user-facing proxies and Tier 3 GC-MS / HPLC / LC-MS anchors. For microbiome-derived metabolites, that gap is especially painful: the [genotype-informed supplement workflow](./genotype-informed-supplement-workflow.md) can recommend butyrate-emphasis interventions for ABCG2 Q141K carriers, but it cannot yet verify butyrate delivery with a validated home or community-biolab Tier 2 assay.

comp-038 reframes that gap as two different problems:

1. **Culture-supernatant butyrate from engineered strains:** plausible Tier 2-lab path exists via HPLC-UV, with GC-MS as anchor.
2. **Stool/serum/home butyrate exposure:** no ready-to-adopt Tier 2 method surfaced; electrochemical fecal SCFA profiling is promising but not production-ready.

## Method Summary

The run used the committed query strategy in [`inputs/query-strategy.json`](./etc/experiments/comp-038-tier-2-butyrate-assay-audit/inputs/query-strategy.json), fetched a PubMed title/abstract snapshot via NCBI E-utilities, then performed five Codex/GPT-5.5 in-session synthesis trajectories from [`outputs/codex-synthesis-packet.md`](./etc/experiments/comp-038-tier-2-butyrate-assay-audit/outputs/codex-synthesis-packet.md). The completed run used the local Codex synthesis path and made **no OpenRouter model calls**.

The evidence gate was intentionally strict: PubMed title/abstract hits can surface candidates, but they cannot justify a GREEN wet-lab recommendation without full-text methods, protocol PDFs, vendor validation documents, or method-comparison data.

## Key Results

| Result | Interpretation |
|---|---|
| PubMed snapshot: 27 queries / 74 records | Enough for a first-pass assay landscape; not a full-text review. |
| HPLC-UV candidate: PMID 23542733 | Best near-term candidate for culture-supernatant butyrate in engineered-strain / fermentation work. |
| Electrochemical fecal candidate: PMID 42041444 | Best stool-specific future direction, but still research-platform grade. |
| Breath proxy literature | Useful for fermentation activity, not butyrate quantification. |
| Generic FFA colorimetric kits | False-friend class; representative protocol excludes acetic, propionic, and butyric acid. |

## Impact on Experimental Priorities

This does **not** unlock a home butyrate assay today. It does tighten the next experimental move:

- Keep **GC-MS as the Tier 3 anchor** for butyrate.
- For engineered-strain / culture-supernatant work, run a small paired validation of HPLC-UV against GC-MS using sodium-butyrate standards and OE-relevant culture matrices.
- For stool work, do a full-text and protocol review of the electrochemical fecal SCFA platform before spending on hardware or adaptation.
- Do not spend on breath hydrogen/methane or generic FFA colorimetric kits for butyrate quantification.

For [`validation-experiments.md` §1.14](./validation-experiments.md#114-additive-abcg2-suppression-by-androgens-tnf-butyrate-rescue-lactoferrin-synergy), this means the butyrate dose-response arm still needs a Tier 3 analytical anchor if concentration verification becomes load-bearing. HPLC-UV may become a cheaper intermediate check for culture-supernatant development, but not for the cellular dose-response arm without matrix validation.

## Limitations

- PubMed results are title/abstract/citation metadata, not full-text validation.
- Vendor and patent searches were targeted, not exhaustive.
- Commercial ELISA claims remain unverified and should not drive spend.
- No non-English corpus pass was run because this specific scope is analytical-chemistry-heavy and Stage 1 was not sparse; revisit if full-text/vendor follow-up stalls.
- The N=5 trajectories were performed in one Codex session to avoid OpenRouter spend, not by five independent paid model calls.

## Next Step

Run a focused full-text/protocol verification pass on PMID 23542733 and PMID 42041444, plus a vendor protocol audit for any butyric-acid/SCFA ELISA claims. If one candidate survives, design a small paired validation with sodium-butyrate spike/recovery and 10-20 real samples measured by the candidate Tier 2 method plus GC-MS.

## Cross-References

- [comp-038 experiment folder](./etc/experiments/comp-038-tier-2-butyrate-assay-audit/)
- [computational-experiments.md](./computational-experiments.md)
- [validation-experiments.md §1.14](./validation-experiments.md#114-additive-abcg2-suppression-by-androgens-tnf-butyrate-rescue-lactoferrin-synergy)
- [quantification-ladder.md](./quantification-ladder.md)
- [genotype-informed-supplement-workflow.md](./genotype-informed-supplement-workflow.md)
