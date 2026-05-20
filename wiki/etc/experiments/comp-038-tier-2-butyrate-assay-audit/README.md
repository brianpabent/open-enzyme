# comp-038 — Tier 2 Butyrate Assay Audit (agentic literature synthesis)

**Status:** Completed first pass 2026-05-20. Codex packet generation is the default live path; this run used Codex/GPT-5.5 in-session synthesis and made no OpenRouter model calls.

**Sub-type:** agentic-literature-synthesis (proposed comp-NNN extension; see [`operations/agentic-science-adoption.md`](../../../../operations/agentic-science-adoption.md))

## Question

Is there a Tier 2 butyrate quantification assay (colorimetric, enzymatic, or breath-hydrogen proxy) that can be validated against Tier 3 GC-MS to close the microbiome-metabolite quantification gap that currently blocks every microbiome-derived intervention downstream (engineered LBP butyrate-boost, bile-acid modulators, indole-based AhR agonists)?

## Why this experiment

- Named as `$0 desk audit before wet-lab investment` in [synthesis queue open-question-2](../../../../synthesis/queue/2026-05-20-open-question-2-is-there-a-tier2-butyrate-assay-colorimetric-enzymatic-or.md) (Pass 3 verdict: Confirmed, prioritize).
- Platform-level framing in [synthesis queue connection-5](../../../../synthesis/queue/2026-05-20-connection-5-the-tier2-butyrate-assay-gap-identified-in-the.md): the quantification-ladder framework currently has no validated Tier 2 home assay for any microbiome-derived metabolite (SCFAs, bile acids, indoles).
- Pure literature-synthesis task. No wet lab required for the desk audit itself.
- Cleanest possible first validation of the proposed agentic-literature-synthesis comp-NNN sub-type (per [`operations/agentic-science-adoption.md`](../../../../operations/agentic-science-adoption.md) Pattern 4 / comp-038 scaffold section).

## Methodology

This is the first agentic-literature-synthesis comp-NNN; the methodology is itself part of what's under review in this PR. First-pass shape:

1. **Search corpus.** PubMed E-utilities snapshot for Stage 1 discovery, plus targeted vendor/protocol review for obvious kit false positives. PMC / DOI full text, Google Scholar, Google Patents, and Espacenet remain follow-up sources before any GREEN wet-lab recommendation. CNKI / J-STAGE are deferred for this butyrate-assay scope unless Stage 1 returns are sparse.
2. **Query strategy.** See [`inputs/query-strategy.json`](./inputs/query-strategy.json). Multi-framing per the new-comp-experiment skill's natural-product/microbiome discipline — assay-class framing AND validation-against-GC-MS framing AND application-context (clinical / animal / cell culture / fermentation breath-monitoring).
3. **PubMed source snapshot.** The live run queries PubMed E-utilities for every committed search string and writes `outputs/pubmed-snapshot.json` with PMID/title/abstract metadata. This is discovery metadata, not full-text verification.
4. **Local-curl source retrieval for firewall-sensitive domains.** Shared helper [`wiki/etc/experiments/lib/agentic_lit_synthesis.py`](../lib/agentic_lit_synthesis.py) includes `local_curl_fetch()` for CNKI / WanFang / J-STAGE / KISS-style sources that must be fetched from Brian's laptop network path rather than model-vendor egress. It is allowlist-gated and writes a provenance sidecar.
5. **Two-model translation for non-English sources.** If non-English source text is ingested, call `translate_source_two_model()` from the shared helper. It runs two independent models from different vendors (DeepSeek + GPT-5.5 for Chinese by default, with Opus as referee) and emits inline `[TRANSLATION-DISAGREEMENT]` annotations where nuance affects mechanism, dose, evidence tier, statistics, route, or scientific hedging.
6. **Role-split model stack.** See [`inputs/model-config.json`](./inputs/model-config.json). When Codex runs this experiment, Codex/GPT-5.5 performs the primary synthesis in-session from `outputs/codex-synthesis-packet.md` to avoid unnecessary OpenRouter spend. External OpenRouter roles (DeepSeek query critique, Opus judge / verifier, two-model translation) are opt-in when a second vendor is worth the marginal cost.
7. **N-trajectory consensus.** N=5 synthesis trajectories. In this run the trajectories were performed by Codex in-session over the same source packet, then collapsed into ranked candidates. The output labels this honestly rather than pretending five paid model calls occurred.
8. **Pairwise-style ranking.** Candidates were judged on (a) validation-against-GC-MS evidence quality, (b) cost / accessibility / kit availability, (c) sample-prep complexity, (d) dynamic range / matrix fit, and (e) OE relevance for stool and culture-supernatant work.
9. **Output:** `outputs/summary.md` — human-readable verdict with ranked assays, per-assay justification, limitations, and decision criterion for which assay to validate in OE's first wet-lab Tier 3 GC-MS comparison.
10. **Budget ceiling:** $0 incremental OpenRouter spend for the normal Codex-driven path. Optional paid external calls require the explicit `python3 analyze.py --run-openrouter` flag and must be reviewed against the config ceiling before use.
11. **Reproducibility artifacts:** model versions + temperatures + prompts + dated PubMed snapshot IDs committed under `inputs/` / `outputs/`. The reproducibility standard is NOT stdlib-only-determinism (which doesn't apply to LLM-driven analyses); it's *fully-documented inputs* + *consensus statistics* + *explicit cost controls*.

## Methodology decisions from the first run

See `operations/agentic-science-adoption.md` for full discussion.

1. **Aviary fork vs custom orchestration?** Decision for comp-038: start with a lightweight OE-native runner using shared helpers in `wiki/etc/experiments/lib/agentic_lit_synthesis.py`. Revisit Aviary only if this pattern becomes repeated enough to justify framework adoption.
2. **Which model in the synthesis seat?** Default when Codex is driving: Codex/GPT-5.5 in-session, using `outputs/codex-synthesis-packet.md`. OpenRouter GPT-5.5 is available only through explicit `--run-openrouter`.
3. **Which model in the judge seat?** Default for optional paid external review: Opus via OpenRouter (`anthropic/claude-opus-4.7`, overridable with `COMP038_JUDGE_MODEL`). Skip unless independent external judgment is worth the spend.
4. **Search-corpus inclusion of CNKI / J-STAGE for this specific question?** Deferred — butyrate assay literature is predominantly analytical chemistry, not natural-product / TCM. Revisit only if full-text/vendor follow-up remains sparse.

## File index

```
comp-038-tier-2-butyrate-assay-audit/
├── README.md                    # this file
├── inputs/
│   ├── query-strategy.json      # search queries per Tier-2-assay framing
│   ├── model-config.json        # non-secret model-role config
│   └── provenance.md            # planned sources + frozen run provenance
├── outputs/
│   ├── codex-synthesis-packet.md
│   ├── pubmed-snapshot.json
│   ├── results.json
│   └── summary.md
└── analyze.py                   # dry-run by default; --prepare-codex fetches sources; --run-openrouter spends budget
```

## How to reproduce

Dry-run artifact check:

```bash
python3 analyze.py
```

Prepare source packet for Codex synthesis without model API spend:

```bash
python3 analyze.py --prepare-codex
```

Optional paid OpenRouter run:

```bash
python3 analyze.py --run-openrouter
```

The OpenRouter path expects `OPENROUTER_API_KEY` in the repo-root `.env` (gitignored) or shell environment. Model role defaults live in `inputs/model-config.json` and can be overridden with `COMP038_QUERY_MODEL`, `COMP038_SYNTHESIS_MODEL`, `COMP038_JUDGE_MODEL`, and `COMP038_VERIFIER_MODEL`.

## Wiki cross-references

- Interpretive page: [`wiki/tier-2-butyrate-assay-audit-computational.md`](../../../tier-2-butyrate-assay-audit-computational.md)
- Tracking index entry: [`wiki/computational-experiments.md`](../../../computational-experiments.md) comp-038
- Informs: [`wiki/genotype-informed-supplement-workflow.md`](../../../genotype-informed-supplement-workflow.md) Tier 2 assay gap; [`wiki/quantification-ladder.md`](../../../quantification-ladder.md) microbiome-derived metabolites open gap; [`wiki/purine-degrading-bacteria.md`](../../../purine-degrading-bacteria.md) butyrate-at-enterocyte-nucleus concentration gap.
- Validation-experiments anchor: [`wiki/validation-experiments.md`](../../../validation-experiments.md) §1.14 (butyrate dose-response arm — the Tier 3 GC-MS anchor against which Tier 2 candidates would be validated).

## Provenance

Scaffolded 2026-05-20 as the first instance of the proposed comp-NNN agentic-literature-synthesis sub-type. See [`operations/agentic-science-adoption.md`](../../../../operations/agentic-science-adoption.md) for the methodology framework this experiment instantiates, and [`synthesis/strategic-reflections/2026-05-20-agentic-science-methodology.md`](../../../../synthesis/strategic-reflections/2026-05-20-agentic-science-methodology.md) for the strategic context (Tier 2 butyrate assay discovery is the cleanest possible test of the methodology against OE's actual stuck list).
