---
title: Propagation eval scenarios — format and authoring
date: 2026-04-25
tags: [eval, propagation, infrastructure]
---

# Propagation eval scenarios

Each scenario is one fixed test case for `scripts/eval-propagation.py`. The
scenario pins a **before-state** (a commit SHA where a trigger file has landed
but propagation hasn't run yet) and the **expected target files** that a
production sweep actually updated. The harness drops a candidate model into
that state, lets it run, and grades the result against the expected targets.

This is replay-based eval, not synthetic. Every scenario is sourced from a
real historical sweep — the actual Pass 1 propagation that landed in `main`
is the de-facto golden answer. (It is not necessarily *correct*, but it is
hand-curated by Brian, which is the closest ground truth available.)

## Frontmatter fields

```yaml
---
name: short-stable-id-for-this-scenario
date: 2026-04-25
description: One-line summary of what triggered the propagation.
before_sha: <full SHA where the trigger file has landed but propagation has not>
trigger_files: wiki/foo.md, wiki/bar.md
expected_targets: wiki/baz.md, wiki/qux.md, wiki/GRAPH.md
golden_diff_sha: <full SHA of the actual production propagation commit>
---
```

The body of the scenario file is free-form context that gets injected into
the model's user prompt — describe the trigger and what an honest reviewer
would expect a Pass 1 model to do. Keep it terse; the model already has the
sweep brief and the trigger files themselves.

`expected_targets` should be the wiki/ files actually edited by the
production propagation commit. Exclude `wiki/synthesis.md` (Pass 2's
job, not Pass 1) and exclude any out-of-scope churn (logs, scripts).

## Picking a scenario

Good scenarios:
- The trigger is a single new wiki page or a bounded edit (clear test condition).
- The propagation touched 3–10 files (enough signal, not overwhelming).
- The connections are mechanistic, not stylistic (we're testing reasoning, not formatting).

Bad scenarios:
- The trigger commit also touched many other unrelated files.
- The propagation was tiny (1 file) — too little signal to discriminate models.
- The propagation was huge (20+ files) — multi-causal, hard to grade.

## Running

```bash
python3 scripts/eval-propagation.py \
    --scenario evals/scenarios/01-chembl-ic50-cross-check.md \
    --model deepseek/deepseek-v4-pro
```

Output goes to `logs/eval-propagation/<date>-<model>-<scenario>.md`.
