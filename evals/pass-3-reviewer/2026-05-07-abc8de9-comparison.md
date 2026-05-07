---
title: Pass 3 reviewer comparison — 2026-05-07-abc8de9 sweep
date: 2026-05-07
synthesis_log: logs/v4-synthesis-2026-05-07-abc8de9.md
synthesizer: google/gemini-2.5-pro
markers: 6
trigger_file_count: 17
models_compared: [anthropic/claude-opus-4-7, openai/gpt-5.5]
tags: [eval, pass-3, sweep-daemon, model-selection]
---

# Pass 3 reviewer comparison — 2026-05-07 (abc8de9 sweep)

Both models reviewed the same Gemini 2.5 Pro synthesis with 6
`{{PEER-REVIEW}}` markers, same inlined evidence (~144K tokens), same
prompt. Only the model flag differed.

## Objective metrics

| Metric | Opus 4.7 | GPT-5.5 | Ratio |
|---|---|---|---|
| Cost | **$8.4433** | **$1.0875** | **7.76× cheaper** |
| Tool iterations | 11 | 2 | 5.5× fewer |
| Total input tokens | 2,989,739 | 458,489 | 6.5× fewer |
| Cached input tokens | 2,726,732 (91%) | 303,104 (66%) | — |
| Output tokens | 5,441 | 5,301 | ≈ same |
| Marker-count match (6 expected) | ✓ | ✓ | — |
| Format compliance | ✗ (preamble before first blockquote, ~1KB stripped manually) | ✓ (clean blockquotes from line 1) | GPT-5.5 wins |

The cost gap is much wider than the headline pricing ratio (3× input,
2.5× output) suggests because GPT-5.5 self-terminated after 2 tool
rounds vs. Opus's 11 — it shipped far less message-history overhead per
call.

## Verdict & overlap-tag distribution

| Marker | Opus 4.7 verdict | Opus tag | GPT-5.5 verdict | GPT-5.5 tag |
|---|---|---|---|---|
| 1 — PRPS chokepoint | Partial | EXTENSION | Confirmed | RESTATEMENT |
| 2 — Sequencing dual-use | Confirmed | NOVEL | Confirmed | RESTATEMENT |
| 3 — manual-lit-mining ↔ H07 | **Push back** | RESTATEMENT | Partial | RESTATEMENT |
| 4 — H07 stack-design flip | **Confirmed, prioritize** | NOVEL | Partial | RESTATEMENT |
| 5 — ClockBase verification pattern | Confirmed | EXTENSION | Partial | RESTATEMENT |
| 6 — Practitioner-toolkit reframe | Confirmed | EXTENSION | Confirmed | RESTATEMENT |

**Tag distribution:** Opus 1×NOVEL, 3×EXTENSION, 1×RESTATEMENT (1 finding
not in this trio set, see the actual file). GPT-5.5 6×RESTATEMENT.
GPT-5.5 is dramatically more conservative on novelty — every finding
got tagged RESTATEMENT, suggesting it interprets "the wiki already
mentions this" as restatement even when the synthesizer's specific
*composition* is new.

**Verdict severity:** Opus has 1×Push-back and 1×Confirmed-prioritize
(stronger ends of the verdict ladder); GPT-5.5 stayed in
Confirmed/Partial range, never escalating to Push-back or
Confirmed-prioritize.

## Quality-decisive specific catches

Both models verified against the same inlined evidence. Where they
diverge is what they *do* with what they verified.

### The H07 worked-example error (synthesizer factual error, headline test)

The Gemini synthesis claimed `manual-literature-mining.md` does not cite
H07 as a worked example. The file contains a literal `Worked example —
H07 Clomid intestinal-ER-antagonism thesis` subsection. **Both models
caught this.**

- **Opus:** Push back, RESTATEMENT. "verified false against the inlined
  evidence." Recommended downgrading the finding.
- **GPT-5.5:** Partial, RESTATEMENT. "is no longer true in the current
  source." Recommended adding only the missing reciprocal cross-reference.

Both correct; Opus framed it more aggressively as a synthesizer error
deserving a Push-back, GPT-5.5 framed it as a softer Partial because half
the suggested action remains valid.

### The H07 stack-design flip (interesting divergence)

Opus elevated this to **Confirmed, prioritize** — the highest-signal
Pass-3 verdict — saying the stack-design flip (AIs/DIM more unfavorable,
direct urate modulators more favorable for SERM-using gout-comorbid
readers) is "directly actionable" and "deserves elevation to Priority
Action."

GPT-5.5 partially rejected this: "the positive H07 mechanism remains
unproven: comp-017 marks intestinal ER→ABCG2 as 'partially supported in
principle, magnitude weak' because Yu 2021 used 100 µM estradiol-tier
exposure, and H07 sub-claim 2 — clomiphene acting as an intestinal ER
antagonist — is explicitly 'UNTESTED.' Therefore the stack-design
inference about AIs/DIM being more unfavorable should stay framed as
contingent, not established."

**GPT-5.5 caught a load-bearing nuance Opus missed.** Sub-claim 2 is
genuinely UNTESTED in the current evidence, and the stack-design flip
inherits that uncertainty. Opus's "elevate to Priority Action" framing
under-weights the magnitude-weak / untested premise. This is the most
interesting empirical signal from the comparison: on a finding where
the right answer requires *epistemic caution* rather than verification
of a citation, GPT-5.5's more skeptical default produced the more
correct review.

### ClockBase preprint vs. peer-reviewed (GPT-5.5-only catch)

GPT-5.5 noted that `autonomous-screening-methodology.md` flags ClockBase
as a preprint with supplementary-methods details unverified, so the
synthesizer's "published, peer-reviewed pattern" phrasing should be
softened. Opus did not catch this.

### Pre-commit-gate plug-in suggestion (Opus-only sharpening)

Opus suggested the comp-NNN verification agent could also plug into the
`manual-literature-mining.md` §"Pre-commit verification gate" — same
pattern at different scopes. GPT-5.5 did not propose this consolidation.

## Format compliance gap

Opus emitted ~6 lines of out-loud reasoning ("grep still broken. I'll
rely on the inlined H07...") before the first `> **Claude review`
blockquote. The merge script splits on `<<<NEXT>>>` and would have
substituted that preamble into `wiki/synthesis.md` as part of the first
review. Required manual stripping (1,048 chars) before merging.

GPT-5.5's output started cleanly at `> **Claude review — Confirmed.`
with no preamble. Drop-in mergeable.

## Conclusion (Brian-eyeball, not algorithmic)

GPT-5.5 is **strictly cheaper, faster, and cleaner-formatted**, with
roughly comparable verification depth. On *epistemic-caution* findings
(H07 stack-design flip), GPT-5.5 was more correct. On *prose richness*
and *cross-document consolidation suggestions* (Pre-commit gate plug-in,
threshold caveats), Opus was richer.

Opus's `Confirmed, prioritize` verdict on the H07 stack-design flip is
a real signal — the verdict has practical consequences (it nudges H07
toward Priority Action treatment in the synthesis walkthrough) — but
GPT-5.5's caution on the same finding is *more correct* given that
sub-claim 2 is UNTESTED.

The 6× RESTATEMENT tag default is GPT-5.5's most worrying property: it
risks under-flagging genuinely novel compositions, which would erode
the multi-model heterogeneity guard's value. This is partially
discoverable from prompt engineering — telling the model "default to
EXTENSION over RESTATEMENT when unsure" might shift the distribution.

**Recommendation (mine, not Brian's):** GPT-5.5 is a strong default
candidate for Pass 3 if cost matters. The architecture already runs
DeepSeek as Pass 4 peer-review (`scripts/peer-review.py`), so Pass 3
errors don't propagate uncaught. Opus stays available as `--model
anthropic/claude-opus-4-7` for high-stakes sweeps where verdict
severity calibration matters more than the ~$7 / sweep cost gap.

Decision is Brian's. The artifacts are here for review:
- `2026-05-07-abc8de9-opus-4-7.txt`
- `2026-05-07-abc8de9-gpt-5.5.txt`
