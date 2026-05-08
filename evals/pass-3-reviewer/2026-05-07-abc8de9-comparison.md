---
title: Pass 3 reviewer comparison — 2026-05-07-abc8de9 sweep
date: 2026-05-08
synthesis_log: logs/v4-synthesis-2026-05-07-abc8de9.md
synthesizer: google/gemini-2.5-pro
markers: 6
trigger_file_count: 17
models_compared: [anthropic/claude-opus-4-7, openai/gpt-5.5 (default prompt), openai/gpt-5.5 (gpt-5.5-tuned prompt)]
tags: [eval, pass-3, sweep-daemon, model-selection]
---

# Pass 3 reviewer comparison — 2026-05-07 (abc8de9 sweep)

All three runs reviewed the same Gemini 2.5 Pro synthesis with 6
`{{PEER-REVIEW}}` markers, same inlined evidence (~144K tokens). The
first two used the canonical Pass 3 prompt (`scripts/sweep-prompt-3-review.md`,
written for Anthropic models). The third used a GPT-5.5-tuned prompt
(`scripts/sweep-prompt-3-review-gpt55.md`) restructured per OpenAI's
GPT-5.5 prompt-engineering guidance: outcome-first ordering, decision
rules instead of `ALWAYS`/`NEVER` for judgment calls, retrieval budget
biased toward MORE verification, explicit OVERLAP-tag default
(EXTENSION when uncertain), explicit verdict-severity triggers.

## Objective metrics

| Metric | Opus 4.7 (canonical prompt) | GPT-5.5 (canonical prompt) | GPT-5.5 (tuned prompt) |
|---|---|---|---|
| Cost | **$8.4433** | **$1.0875** | **$1.6615** |
| vs. Opus | 1.0× | 7.76× cheaper | 5.08× cheaper |
| Tool-using rounds | 11 | 2 | 7 |
| Total tool calls | 11 | 2 | ~22 |
| Total input tokens | 2,989,739 | 458,489 | 1,286,497 |
| Cached input | 91% | 66% | 86% |
| Output tokens | 5,441 | 5,301 | 6,856 |
| Format compliance | ✗ (preamble drift) | ✓ | ✓ |
| Marker-count match (6) | ✓ | ✓ | ✓ |

The tuned prompt unlocked actual verification depth: GPT-5.5 went from
2 tool calls to ~22 across 7 rounds, with the cost only rising 1.5×
(still 5× cheaper than Opus). The retrieval-budget pattern from the
GPT-5.5 guide ("Make a tool call when ANY of [enumerated triggers]
applies") was the load-bearing change.

## Verdict & overlap-tag distribution

| Marker | Opus 4.7 | GPT-5.5 (canonical) | GPT-5.5 (tuned) |
|---|---|---|---|
| 1 — PRPS chokepoint | Partial / EXTENSION | Confirmed / RESTATEMENT | Partial / RESTATEMENT |
| 2 — Sequencing dual-use | Confirmed / NOVEL | Confirmed / RESTATEMENT | Confirmed / **EXTENSION** |
| 3 — manual-lit-mining ↔ H07 | **Push back** / RESTATEMENT | Partial / RESTATEMENT | **Push back** / RESTATEMENT |
| 4 — H07 stack-design flip | **Confirmed, prioritize** / NOVEL | Partial / RESTATEMENT | Partial / **EXTENSION** |
| 5 — ClockBase verification pattern | Confirmed / EXTENSION | Partial / RESTATEMENT | **Push back** / RESTATEMENT |
| 6 — Practitioner-toolkit reframe | Confirmed / EXTENSION | Confirmed / RESTATEMENT | Confirmed / RESTATEMENT |

**Tag distribution shift:**

| Tag | Opus | GPT-5.5 canonical | GPT-5.5 tuned |
|---|---|---|---|
| NOVEL | 2 | 0 | 0 |
| EXTENSION | 3 | 0 | 2 |
| RESTATEMENT | 1 | 6 | 4 |

The tuned prompt cut RESTATEMENT-bias from 6/6 to 4/6 and unlocked 2
EXTENSION tags. NOVEL still didn't fire — GPT-5.5's conservatism on the
strongest novelty claim is durable, not just a default issue. This may
or may not be a real ceiling: the prompt's rule for NOVEL is "no
element of the finding is named anywhere in the wiki," and given the
inlined evidence covers 17 trigger files containing all the cited
elements, GPT-5.5 may correctly conclude that no Pass 2 finding
qualifies as fully NOVEL. Opus tagged 2 NOVEL — both arguably
defensible as EXTENSION instead.

**Verdict-severity shift:**

| Verdict | Opus | GPT-5.5 canonical | GPT-5.5 tuned |
|---|---|---|---|
| Confirmed, prioritize | 1 | 0 | 0 |
| Push back | 1 | 0 | **2** |
| Partial | 1 | 3 | 2 |
| Confirmed | 3 | 3 | 2 |

The tuned prompt successfully escalated GPT-5.5 to Push-back twice
(matching/exceeding Opus's 1× Push-back). It did NOT escalate to
Confirmed-prioritize on the H07 stack-design flip — see "decisive
finding" below.

## Decisive findings

### H07 stack-design flip (Opus elevates; both GPT-5.5 runs hold contingent)

Opus tagged this **Confirmed, prioritize / NOVEL** — recommended
elevation to Priority Action because the stack-design flip is "directly
actionable" for SERM-using gout-comorbid readers.

Both GPT-5.5 runs (canonical and tuned) tagged this **Partial** because
H07 sub-claim 1 is "magnitude-weak" (Yu 2021 used 100 µM E2, 5–6 orders
above physiological) and sub-claim 2 (clomiphene as intestinal ER
antagonist) is explicitly UNTESTED. Both correctly identified that the
stack-design implication is conditional, not settled.

GPT-5.5 (both runs) is more correct here. The tuned prompt has explicit
verdict-severity triggers that *would* have permitted escalation to
Confirmed-prioritize — but GPT-5.5 chose not to escalate, citing the
untested premise. That's epistemically right: a stack-design flip
contingent on an untested sub-claim doesn't deserve elevation to
Priority Action, regardless of how actionable the framing sounds.

### ClockBase verification pattern (tuned GPT-5.5 catches a Push-back Opus and canonical GPT-5.5 missed)

Marker 5 claims the ClockBase verification-agent pattern applied to
comp-NNN is a novel cross-page synthesis. **Tuned GPT-5.5 grep'd
`autonomous-screening-methodology.md` and discovered it already maps
ClockBase's hypothesis-then-verify pattern onto comp-NNN, names the
DAF SCR1-4 incident as the canonical failure mode, and proposes that
every comp-NNN run produce a primary report plus an independent
verification-pass report.** So the synthesizer's "no page has connected
this" claim is false.

This is a Push-back-worthy factual catch. Opus said Confirmed; canonical
GPT-5.5 said Partial; only the tuned GPT-5.5 caught it. The retrieval
budget from the tuned prompt — "always grep to verify what a page
does/doesn't say" — is what found it. Concrete demonstration that
prompt tuning unlocked verification GPT-5.5 wouldn't perform on its
own defaults.

### H07 worked-example error (all three caught it; severity differs)

All three runs caught the synthesizer's claim that
`manual-literature-mining.md` doesn't cite H07 as a worked example
(verified false against inlined evidence — there's a literal subsection
titled "Worked example — H07 Clomid intestinal-ER-antagonism thesis").

- Opus: **Push back** / RESTATEMENT
- GPT-5.5 canonical: Partial / RESTATEMENT
- GPT-5.5 tuned: **Push back** / RESTATEMENT

The tuned prompt successfully calibrated GPT-5.5 to match Opus's
severity on this finding. The canonical-prompt run softened to Partial,
which obscures the synthesizer's error.

### Stale-Suggested-Action catches (tuned GPT-5.5 noted these on multiple markers)

Tuned GPT-5.5 caught that several Suggested Actions in the synthesis
were already done in the wiki:

- Marker 1: `fructose-connection.md` already has a "PRPS connection"
  paragraph; `gout-pathophysiology.md` already has a first-class PRPS
  section + map row.
- Marker 4: H07-side comp-017 cross-references are already in H07's
  status text.
- Marker 5: `autonomous-screening-methodology.md` already proposes the
  verification-agent architecture.

This is a class of finding that's specifically valuable for the
synthesis walkthrough: it tells Brian which Suggested Actions can be
crossed off without further work. Opus also caught some (marker 1's
`gout-pathophysiology.md` PRPS section), but tuned GPT-5.5 was more
systematic about it because the retrieval budget pushed it to grep
each Suggested Action.

## Conclusion

The tuned prompt addressed every load-bearing concern from the
canonical-prompt GPT-5.5 run:

- ✅ **RESTATEMENT bias reduced** from 6/6 to 4/6 (2 EXTENSION tags
  unlocked). NOVEL still didn't fire, but plausibly correct given the
  evidence.
- ✅ **Verdict severity calibrated** — 2× Push-back (matching Opus) on
  load-bearing factual errors. H07 stack-design flip held at Partial,
  which is more correct than Opus's Confirmed-prioritize given
  sub-claim 2 is UNTESTED.
- ✅ **Tool-use depth** went from 2 calls to ~22, with the cost rising
  only 1.5× (still 5× cheaper than Opus).
- ✅ **Format compliance** stayed clean (no preamble drift).
- ✅ **New catch surfaced** that neither prior run found (ClockBase
  verification agent already proposed in `autonomous-screening-methodology.md`).

Cost gap remains decisive: tuned GPT-5.5 at $1.66 vs. Opus at $8.44 is
5× cheaper. Quality is now comparable on most markers; on epistemic-
caution findings (H07 stack-design flip), GPT-5.5 is *more* correct.

**Recommendation (mine, not Brian's):** Make `openai/gpt-5.5` with
`scripts/sweep-prompt-3-review-gpt55.md` the default Pass 3 model.
Keep Opus + canonical prompt available as `--model anthropic/claude-opus-4-7
--prompt-file scripts/sweep-prompt-3-review.md` for sweeps where
verdict-severity calibration is genuinely worth the 5× cost premium.

Open question for future evals: does the tuned prompt also work well
for Anthropic models, or does it need to stay GPT-5.5-specific? If
the tuned prompt produces equivalent-or-better results on Sonnet 4.6,
we could collapse to a single prompt with Sonnet as a cheaper-than-Opus
quality baseline. Worth one more side-by-side run on the next sweep.

Decision is Brian's. Artifacts:
- `2026-05-07-abc8de9-opus-4-7.txt`
- `2026-05-07-abc8de9-gpt-5.5.txt` (canonical prompt)
- `2026-05-07-abc8de9-gpt-5.5-tuned.txt` (GPT-5.5-specific prompt)
