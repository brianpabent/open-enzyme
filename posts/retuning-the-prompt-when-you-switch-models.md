---
title: A 5× cost cut from one prompt rewrite
date: 2026-05-08
status: draft
tags: [prompt-engineering, llm-cost, model-evaluation, sweep-daemon, methodology]
---

# A 5× cost cut from one prompt rewrite

I run a small open-source biology project with a multi-pass review pipeline. Each substantive edit to the research wiki triggers four passes — Claude propagates, Gemini synthesises, a third model peer-reviews the synthesis, DeepSeek peer-reviews *that*. The third pass — the verdict-and-pushback layer — was running on Claude Opus 4.7 at roughly $8 per sweep, which adds up faster than I'd like for a daemon that fires on every push.

I switched the third pass to GPT-5.5 today. The cost dropped to $1.66 — about 5× cheaper. But the interesting part isn't the cost. It's that the *first* time I ran GPT-5.5 with the existing prompt, I got results I would not have shipped, and I almost concluded the model was the problem. It wasn't. The prompt was.

If you take one thing away from this post: **when you switch model vendors, retune the prompt.** Default prompts inherit assumptions about how the previous model thinks. Carrying them over silently leaves quality on the table.

## The first run, with the existing prompt

Same task, three runs, identical inputs (same Gemini synthesis, same 6 markers to review, same ~144K tokens of inlined evidence):

|  | Opus 4.7 | GPT-5.5 (existing prompt) | GPT-5.5 (tuned prompt) |
|---|---|---|---|
| Cost | $8.44 | $1.09 | **$1.66** |
| Tool calls | 11 | 2 | ~22 |
| Push-back verdicts | 1 | **0** | 2 |
| EXTENSION tags | 3 | **0** | 2 |

GPT-5.5 with the existing prompt was 7.7× cheaper than Opus, but it terminated after 2 tool calls (Opus did 11), tagged every finding as a "restatement" of existing wiki content (Opus tagged a mix of novel/extension/restatement), and never once escalated a verdict to "push back" on the synthesizer's factual errors. It produced reviews that were technically correct, never wrong, and never load-bearing. Six findings reviewed, zero of them pushed back on. That's not the job.

The temptation was to shrug and conclude GPT-5.5 isn't a peer-review model. The right move was to read [OpenAI's GPT-5.5 prompt-engineering guide](https://developers.openai.com/api/docs/guides/prompt-guidance) first.

## What the guide actually says

Two patterns from the guide are load-bearing for an evaluative task like this:

1. **Outcome-first, not process-first.** "Avoid carrying over every instruction from an older prompt stack. Legacy prompts often over-specify the process because earlier models needed more help staying on track." My existing prompt had a numbered Process section ("1. Read the log, 2. Count markers, 3. For each marker..."). Anthropic models follow that fine. GPT-5.5 reads it as redundant choreography over an already-clear goal and clips the work short.

2. **Reserve `ALWAYS` and `NEVER` for true invariants.** For judgment calls — when to use a tool, how aggressive a verdict to issue, which tag to apply — use *decision rules* ("if X, do Y; if Z, default to W"). My existing prompt had ALWAYS/NEVER scattered through tag definitions. GPT-5.5 interpreted those as load-bearing constraints and resolved every ambiguity to the most conservative option.

The third change isn't in the guide explicitly but follows from it: **GPT-5.5's default tool-use bias is "minimise loops." If your task wants more verification, you have to write the retrieval budget in the dial-up direction**, not the dial-down direction. The guide gives a verbatim retrieval budget for normal Q&A: *"Make another retrieval call only when [enumerated triggers]."* For peer review, I needed the inverse: *"Make a tool call when ANY of [enumerated triggers] applies — err toward more verification, not less."*

## The rewrite

Three structural changes. Same length, same content, same invariants for output format (the merge script that substitutes reviews into our synthesis log is unchanged):

- **Replaced the Process section with a Goal + Success criteria + Stop rules block.** Outcome first.
- **Replaced ALWAYS/NEVER on tag and verdict definitions with explicit decision rules.** "Default to EXTENSION when uncertain. RESTATEMENT only when *every* element of the finding is already a named first-class topic in the wiki." Same for verdict severity: "Use Push-back when the synthesizer made a verifiable factual error. Downgrading to Partial to be polite obscures the error."
- **Inverted the retrieval budget.** "Make a tool call when ANY of [the synthesizer claims a page does/doesn't say X | the OVERLAP tag depends on whether something appears elsewhere | the finding cites a page outside the warm cache] applies. A 6-marker review with thorough verification typically takes 6–12 tool calls. Stopping at 2 rounds is under-verification, not efficiency."

Both prompts now live in the repo: [`scripts/sweep-prompt-3-review.md`](../scripts/sweep-prompt-3-review.md) (the original, still optimal for Anthropic models) and [`scripts/sweep-prompt-3-review-gpt55.md`](../scripts/sweep-prompt-3-review-gpt55.md) (the GPT-5.5-tuned version). The existing reviewer script accepts a `--prompt-file` flag. Switching is one workflow line.

## What changed empirically

Tuned GPT-5.5 escalated to Push-back twice (matching Opus's 1×, exceeding the canonical-prompt run's 0×). It cut its restatement-bias from 6/6 to 4/6. It made roughly 22 tool calls across 7 rounds, up from 2 across 1 round. Cost rose from $1.09 to $1.66 — modest, given the depth.

Two unexpected wins:

**The tuned prompt caught something the other two runs missed.** On one finding, the synthesizer claimed no wiki page connected the ClockBase autonomous-screening pattern to our internal verification-failure incident. The tuned GPT-5.5 grep'd the methodology page and found that connection is *already documented* — the synthesizer was asserting novelty against existing wiki content. Pushed back; correctly. Opus said "Confirmed" with a useful sharpening; canonical-prompt GPT-5.5 said "Partial" without catching the false-novelty claim. The retrieval-budget rule "always grep to verify what a page does/doesn't say" is what found it. Concrete, replicable, generalizable.

**GPT-5.5 was *more* correct than Opus on one finding.** A separate marker proposed elevating a clinical recommendation to "Priority Action." Opus tagged it Confirmed-prioritize and recommended elevation. Both GPT-5.5 runs (canonical and tuned) refused to elevate, citing that one of the underlying sub-claims is explicitly marked UNTESTED in our hypothesis card. They were right and Opus was wrong. A stack-design recommendation contingent on an untested sub-claim shouldn't be elevated to Priority Action regardless of how actionable the framing sounds. GPT-5.5's epistemic caution, baked into its defaults, is in some places the better calibration. The tuned prompt didn't override that; it refined it.

## What's the takeaway for someone running their own pipeline

Three things worth doing before concluding a model isn't fit for your task:

1. **Read the model vendor's prompt guide before you swap.** OpenAI, Anthropic, Google, and DeepSeek each publish guidance about how their current generation prefers to be prompted. The patterns differ in load-bearing ways. Read them when you change vendors. This took me 20 minutes; the eval that followed took me an hour. The cost reduction will pay both back the first sweep.

2. **Keep both prompts.** I now have one prompt for Anthropic models and one for GPT-5.5. They live next to each other in the repo. When the next interesting model lands, I'll write a third. Maintaining two prompts is cheaper than rerunning quality evals every time a new model ships.

3. **Run a real eval, not a vibe check.** The existing prompt vs. tuned prompt comparison was a side-by-side run on the *same* task with the *same* synthesis, the *same* 6 markers, the *same* 144K tokens of inlined evidence. The only variable was the prompt. Anything else is noise. The full comparison artifact is at [`evals/pass-3-reviewer/2026-05-07-abc8de9-comparison.md`](../evals/pass-3-reviewer/2026-05-07-abc8de9-comparison.md) if you want to see what an actual replayed-eval doc looks like for a non-trivial reviewer task.

The 5× cost reduction is the headline. The discipline behind it is the actual takeaway.

---

*Written 2026-05-08. Open Enzyme is an open-source library of engineered food-grade microbes producing therapeutic enzymes. The sweep daemon code, both prompts, and the full eval artifact are public in the repo.*
