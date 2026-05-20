# comp-038 — Tier 2 Butyrate Assay Audit (agentic literature synthesis)

**Status:** Scaffolded 2026-05-20. analyze.py and run deferred pending methodology review.

**Sub-type:** agentic-literature-synthesis (proposed comp-NNN extension; see [`operations/agentic-science-adoption.md`](../../../../operations/agentic-science-adoption.md))

## Question

Is there a Tier 2 butyrate quantification assay (colorimetric, enzymatic, or breath-hydrogen proxy) that can be validated against Tier 3 GC-MS to close the microbiome-metabolite quantification gap that currently blocks every microbiome-derived intervention downstream (engineered LBP butyrate-boost, bile-acid modulators, indole-based AhR agonists)?

## Why this experiment

- Named as `$0 desk audit before wet-lab investment` in [synthesis queue open-question-2](../../../../synthesis/queue/2026-05-20-open-question-2-is-there-a-tier2-butyrate-assay-colorimetric-enzymatic-or.md) (Pass 3 verdict: Confirmed, prioritize).
- Platform-level framing in [synthesis queue connection-5](../../../../synthesis/queue/2026-05-20-connection-5-the-tier2-butyrate-assay-gap-identified-in-the.md): the quantification-ladder framework currently has no validated Tier 2 home assay for any microbiome-derived metabolite (SCFAs, bile acids, indoles).
- Pure literature-synthesis task. No wet lab required for the desk audit itself.
- Cleanest possible first validation of the proposed agentic-literature-synthesis comp-NNN sub-type (per [`operations/agentic-science-adoption.md`](../../../../operations/agentic-science-adoption.md) Pattern 4 / comp-038 scaffold section).

## Methodology — proposed, pending review

This is the first agentic-literature-synthesis comp-NNN; the methodology is itself part of what's under review in this PR. Proposed shape:

1. **Search corpus.** PubMed + PMC + Google Scholar + Google Patents + Espacenet. Optional extension to CNKI / J-STAGE if initial Aviary-fit testing supports it (per Tooling Decision #1 in `operations/agentic-science-adoption.md`).
2. **Query strategy.** See [`inputs/query-strategy.json`](./inputs/query-strategy.json). Multi-framing per the new-comp-experiment skill's natural-product/microbiome discipline — assay-class framing AND validation-against-GC-MS framing AND application-context (clinical / animal / cell culture / fermentation breath-monitoring).
3. **N-trajectory consensus.** N=5 parallel trajectories. Each runs the full search → candidate-extraction → ranking pipeline independently. Only assays surfaced by ≥3 of 5 trajectories advance to the final tournament.
4. **Pairwise-tournament ranking.** Full pairwise over the consensus set (typically ≤6 candidates), judged on (a) validation-against-GC-MS evidence quality, (b) cost / accessibility / kit availability, (c) sample-prep complexity, (d) dynamic range coverage of physiologically-relevant butyrate concentrations (10 µM – 100 mM lumenal; ~1-10 µM serum).
5. **Output:** `outputs/summary.md` — human-readable verdict with top-3 ranked assays, per-assay justification, consensus-statistics block ("identified in K of N trajectories"), limitations, and decision criterion for which assay to validate in OE's first wet-lab Tier 3 GC-MS comparison.
6. **Budget ceiling:** $25 total (hard-capped in `analyze.py`). Wall clock target: <90 min.
7. **Reproducibility artifacts:** model versions + temperatures + prompts + dated PubMed snapshot IDs committed under `inputs/`. The reproducibility standard is NOT stdlib-only-determinism (which doesn't apply to LLM-driven analyses); it's *fully-documented inputs* + *consensus statistics* + *budget-capped runtime*.

## Methodology questions to resolve before running

These are open. See `operations/agentic-science-adoption.md` for full discussion. Resolved decisions land here.

1. **Aviary fork vs custom orchestration?** Provisional: try Aviary first. If integration friction exceeds one day, fall back to a Claude+PaperQA2 custom orchestration over the proven primitives.
2. **Which model in the synthesis seat?** Claude Opus 4.7 (default for OE narrative work), or test Gemini 3 Deep Think on this specific task? Decision: use Opus 4.7 by default; bench Deep Think in a separate eval (Open Eval #1 in operations doc).
3. **Which model in the judge seat?** Robin uses Claude 3.7 Sonnet. OE proposed default: Claude Sonnet 4.6.
4. **Search-corpus inclusion of CNKI / J-STAGE for this specific question?** Probably no — butyrate assay literature is predominantly Western analytical chemistry, not natural-product / TCM. Skip for comp-038; revisit if Stage 1 results are sparse.

## File index

```
comp-038-tier-2-butyrate-assay-audit/
├── README.md                    # this file
├── inputs/
│   ├── query-strategy.json      # search queries per Tier-2-assay framing
│   └── provenance.md            # planned sources + fetch-dates
├── outputs/
│   └── .gitkeep                 # placeholder; results land here after run
└── (analyze.py — DEFERRED; written after methodology review sign-off)
```

## How to reproduce (after analyze.py is written)

Will be: `python3 analyze.py` from this folder, with appropriate API key environment variables for the chosen model stack (Claude / OpenAI / Gemini). Outputs land in `outputs/` deterministically given the same inputs/ + model versions + random seed.

## Wiki cross-references

- Interpretive page: **DEFERRED** — to be created at `wiki/tier-2-butyrate-assay-audit-computational.md` after the run, per the new-comp-experiment skill's Step 6.
- Tracking index entry: **DEFERRED** — to be added to `wiki/computational-experiments.md` Planned Analyses (or Analyses, post-run) table after methodology sign-off.
- Informs: [`wiki/genotype-informed-supplement-workflow.md`](../../../genotype-informed-supplement-workflow.md) Tier 2 assay gap; [`wiki/quantification-ladder.md`](../../../quantification-ladder.md) microbiome-derived metabolites open gap; [`wiki/purine-degrading-bacteria.md`](../../../purine-degrading-bacteria.md) butyrate-at-enterocyte-nucleus concentration gap.
- Validation-experiments anchor: [`wiki/validation-experiments.md`](../../../validation-experiments.md) §1.14 (butyrate dose-response arm — the Tier 3 GC-MS anchor against which Tier 2 candidates would be validated).

## Provenance

Scaffolded 2026-05-20 as the first instance of the proposed comp-NNN agentic-literature-synthesis sub-type. See [`operations/agentic-science-adoption.md`](../../../../operations/agentic-science-adoption.md) for the methodology framework this experiment instantiates, and [`synthesis/strategic-reflections/2026-05-20-agentic-science-methodology.md`](../../../../synthesis/strategic-reflections/2026-05-20-agentic-science-methodology.md) for the strategic context (Tier 2 butyrate assay discovery is the cleanest possible test of the methodology against OE's actual stuck list).
