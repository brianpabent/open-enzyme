---
title: "Pass 3 reviewer eval — DeepSeek candidate plan"
date: 2026-06-01
tags: [eval, pass-3, sweep-daemon, model-selection, deepseek]
status: planned (not yet run)
---

# Pass 3 reviewer eval — DeepSeek candidate

## Motivation

Evaluate **DeepSeek (V4-Pro or current)** as the Pass 3 (review/critique) model, replacing or alternating with the current GPT-5.5.

Three reasons:

1. **GPT-5.5 review-quality frustration.** During the 2026-06-01 walkthrough of the 2026-05-30 sweep, GPT-5.5 produced two misses of the same family — *treating a corpus value as ground truth* (see "Catch-tests" below). Brian flagged similar frustration on the prior walk.
2. **DeepSeek was strong on Pass 2.** DeepSeek V4-Pro was the Pass 2 synthesizer until 2026-05-29, when it was swapped to Grok 4.20 **only** because the corpus crossed DeepSeek's ~1M context cap (Pass 2 reads the full corpus). The swap was forced by context window, not by quality dissatisfaction — we were happy with DeepSeek's Pass 2 work. Pass 3 input is much smaller (one synthesis log + cited files, not the full corpus), so the context constraint that pushed DeepSeek off Pass 2 **does not apply to Pass 3**.
3. **Cost.** GPT-5.5 is $5 / $30 per Mtok (in/out). DeepSeek is materially cheaper. Pass 3 runs every sweep; the savings compound.

## What needs building

- **A DeepSeek-tuned Pass 3 prompt** — `scripts/sweep-prompt-3-review-deepseek.md`. Prompts are model-tuned in this repo (`sweep-prompt-3-review-gpt55.md` for GPT-5.5, `sweep-prompt-3-review.md` for Anthropic models). DeepSeek needs its own. **Must carry the same decision rules the others now have**, especially:
  - The **corpus-absence-is-NOT-refutation** rule (added 2026-06-01 to both existing prompts) → world-claims checkable only against corpus presence/absence get `Defer. [VERIFY: lit-scan]`, never `Push back.`/`Rejected.` on absence alone.
  - The chassis-agnostic discipline, the verdict-severity rules, the OVERLAP/GAP tags, and the multi-axis verification discipline (grep the *detailed* source, not just the first corpus location — see Catch-test 2).

## Test input

Use the **2026-05-30 sweep** (`0317c56`, the one walked 2026-06-01) — 22 real items across 6 section types, realistic and already human-reviewed during the walk, so we have ground truth for what a good reviewer should have said. Reproduce per `README.md` "Reproducing a run": same `scripts/sweep-3-review.py`, same synthesis log + trigger files, vary `--model`.

## Catch-tests (the gold — both are real GPT-5.5 misses from the 2026-06-01 walk)

These are the Pass-3 analogue of the existing H07 hallmark test. A competent reviewer should handle both:

1. **Theaflavins × ABCG2 (connection-1).** The synthesizer claimed theaflavins are functional ABCG2 inhibitors "sharing the tannin-class profile." GPT-5.5 pushed back citing only `theaflavins.md`'s absence of an ABCG2 note. The correct behavior (per the corpus-absence rule): flag the claim as unverifiable against corpus and emit `Defer. [VERIFY: lit-scan]` rather than treating absence as refutation. (Ground truth: a multilingual lit scan showed the claim was *inverted* — theaflavins up-regulate ABCG2 in vivo, Tai 2020. No reviewer without lit-scan tools can know "inverted," but the *right* move is to route to the scan, not reject.) **Scoring:** does the candidate route-to-verification vs. reject-on-absence?

2. **§1.25 stale cost (experiment-3).** The synthesizer quoted §1.25 cost $4,445–6,745 (the current header). GPT-5.5 "pushed back" citing $3,500–5,500 as the real number — but that was a **stale summary-table value** the header contradicts (the header was re-scoped 2026-05-17; the table wasn't updated). GPT-5.5 cited the first corpus location it found as ground truth without noticing the two locations disagree. **Scoring:** does the candidate (a) avoid asserting a single corpus number as ground truth without cross-checking, and ideally (b) flag the *internal inconsistency* between header and table?

3. **Existing H07 hallmark** (from 2026-05-07-abc8de9) — keep as a regression check.

## Heterogeneity consideration (weigh, don't ignore)

DeepSeek is **already the Pass 1 (propagate) model**. Moving Pass 3 to DeepSeek means DeepSeek does both propagation and review, and GPT-5.5 (the only OpenAI presence in the pipeline) drops out. The multi-model-heterogeneity guard (`wiki/etc/open-source-platform.md` §"Multi-model synthesis as guard against epistemic homogenization") weakens: a DeepSeek-shared blind spot could survive both propagation and review unchallenged. This is a real tradeoff against the cost + quality win. Mitigations to consider in the eval recommendation:

- Keep GPT-5.5 (or another vendor) as a periodic Pass-3 cross-check rather than full replacement.
- If DeepSeek takes Pass 3, consider moving Pass 1 to a different vendor to preserve cross-vendor coverage.
- Accept reduced heterogeneity if the cost + catch-rate win is large enough — but make the call explicitly, don't let it happen by default.

## Grading (per `README.md`)

Cost (in/out tokens × pricing), tool iterations (research depth before self-termination), cache hit rate, format compliance (only `> **... review` blockquotes separated by `<<<NEXT>>>`), verdict + overlap-tag distribution, and the catch-tests above. Output: `2026-05-30-0317c56-deepseek-*.txt` raw runs + a `2026-05-30-0317c56-comparison.md` Brian-facing summary vs. GPT-5.5.

## Origin

Surfaced during the 2026-06-01 synthesis walkthrough after two GPT-5.5 Pass-3 misses (Items 1 and 7). Brian: "Maybe we could do an eval of using deep seek in pass 3 — save us money, might get a better outcome. Probably need to tune a new prompt for deepseek for that pass, but that's okay."
