---
title: Pass 3 reviewer model evals
date: 2026-05-07
tags: [eval, pass-3, sweep-daemon, model-selection]
---

# Pass 3 reviewer model evals

Side-by-side runs of candidate reviewer models against fixed Pass 3 tasks.
Same script (`scripts/sweep-3-review.py`), same synthesis log, same trigger
files, same prompt — only the `--model` flag varies.

This is the Pass-3 analogue of `evals/scenarios/` (which evaluates Pass 1
propagation models). Pass 3 is critique, not propagation, so the grading
criteria differ:

- **Cost** (objective) — input + output tokens × model pricing
- **Tool iterations** (objective) — how much research depth before
  self-termination; lower is faster but may miss verification work
- **Cache hit rate** (objective) — affects cost but not quality
- **Format compliance** — did the model emit only `> **Claude review`
  blockquotes separated by `<<<NEXT>>>`, or did it leak preamble /
  thinking-out-loud?
- **Verdict & overlap-tag distribution** — RESTATEMENT-heavy vs.
  NOVEL-heavy; aggressive Push-back vs. soft Partial
- **Specific catches** — did the reviewer notice the synthesizer's
  factual errors? Hallmark test: the H07 worked-example error in
  the 2026-05-07-abc8de9 sweep, where Gemini claimed
  `manual-literature-mining.md` doesn't cite H07 as a worked
  example — but the file has a literal `Worked example — H07 …`
  subsection. Any competent reviewer should catch this.

## File layout

```
evals/pass-3-reviewer/
├── README.md                            # this file
├── <date>-<sha>-<model-id>.txt          # raw review output (one per model run)
└── <date>-<sha>-comparison.md           # Brian-facing summary across models
```

`<sha>` is the synthesis log's commit SHA short form (e.g. `abc8de9`).
Model IDs use OpenRouter's slash-form with dots flattened (`openai/gpt-5.5`
→ `gpt-5.5`).

## Reproducing a run

The same trigger-files string used by the workflow's Pass 3 step. For the
2026-05-07 sweeps, all 17 trigger files happen to also be the cited files
(every Pass-2 reference was already a trigger), so we pass the same list
to both flags:

```bash
TRIGGER_FILES="$(printf 'wiki/%s\n' \
  abcg2-modulators.md \
  androgen-natural-modulation.md \
  androgen-urate-axis.md \
  autonomous-screening-methodology.md \
  computational-experiments.md \
  cross-validation.md \
  gut-lumen-sink.md \
  hypotheses/H07-clomid-intestinal-er-antagonism.md \
  hypotheses/README.md \
  intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md \
  koji-endgame-strain.md \
  manual-literature-mining.md \
  personal-genome-protocol.md \
  practitioner-toolkit.md \
  prps-purine-biosynthesis-chokepoint.md \
  t-abcg2-suppression-evidence-mining-computational.md \
  t-axis-adjuvant-urate-mapping-computational.md)"

python3 scripts/sweep-3-review.py \
  --synthesis-log logs/v4-synthesis-2026-05-07-abc8de9.md \
  --commit-sha "$(git rev-parse HEAD)" \
  --diff-base "6eced8cc47812c3a01644753012477214e53f47e" \
  --trigger-files "$TRIGGER_FILES" \
  --cited-files "$TRIGGER_FILES" \
  --marker-count 6 \
  --model openai/gpt-5.5 \
  > evals/pass-3-reviewer/2026-05-07-abc8de9-gpt-5.5.txt
```

The cost and iteration line lands on stderr; capture it manually for the
comparison doc.

## Why we run real-world replays, not synthetic tasks

Same logic as `evals/scenarios/`: the Pass 2 synthesis is hand-curated by
the Gemini synthesizer against the actual wiki state at a real commit, and
the Pass 3 review's "right answer" is whatever a thoughtful PhD-audience
reviewer would write given the inlined evidence. There's no automated
golden — Brian eyeballs the comparison doc. The objective metrics
(cost, iterations, format compliance, tag distribution) bound the
discussion; the qualitative quality call is human-in-the-loop.
