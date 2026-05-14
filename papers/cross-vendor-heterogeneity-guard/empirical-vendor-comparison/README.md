# Empirical vendor-comparison pilot

Pilot study designed to give the cross-vendor heterogeneity paper (this directory's parent) actual data on how often the four vendor models disagree on the same prompt, rather than only the case-study + architectural argument the rest of the manuscript carries.

## What the study tested

Eight prompts spanning the daemon's operational task types:

| Prompt | Task type | Provenance |
|---|---|---|
| 01-uricase-mechanism-factual | factual recall | synthetic-but-realistic biochemistry lookup |
| 02-abcg2-q141k-factual-quant | factual quantitative | synthetic-but-realistic human-genetics + transporter |
| 03-nlrp3-mechanism-inference | mechanism inference | synthetic, immunology mechanism puzzle |
| 04-koji-uricase-hypothesis-gen | hypothesis generation | synthetic experimental-design task |
| 05-rasburicase-ada-mechanism | mechanism inference | synthetic, drug-immunogenicity question |
| 06-cross-document-synthesis | synthesis | mirrors daemon Pass 2 cross-document task with two short wiki excerpts |
| 07-self-demonstrating-review | adversarial review | adapted near-directly from `papers/cross-vendor-heterogeneity-guard/review-prompts.md` Prompt 1 |
| 08-cordycepin-koji-feasibility | hypothesis + mechanism | synthetic metabolic-engineering feasibility prompt |

Each prompt fired against four vendor models via OpenRouter:

| Vendor key | OpenRouter slug | Role in daemon pipeline |
|---|---|---|
| `deepseek` | `deepseek/deepseek-v4-pro` | Pass 2 synthesizer (primary), Pass 1 propagator |
| `gemini` | `google/gemini-2.5-pro` | Pass 2 fallback |
| `openai` | `openai/gpt-5.5` | Pass 3 reviewer |
| `anthropic` | `anthropic/claude-opus-4-7` | Interactive hypothesis-development layer (vibe-science) |

## Method

`run_experiment.py` reads each prompt's body (frontmatter stripped) and submits identical text to each vendor with the same temperature (0.7) and per-vendor max-tokens caps. Each response is saved with YAML frontmatter recording the served model, token usage, latency, cost, finish_reason, and a SHA256 hash of the prompt and response (12-char prefix) for the audit trail.

Per-vendor `max_tokens` differ because DeepSeek V4-Pro and OpenAI GPT-5.5 are reasoning models that consume internal reasoning tokens before emitting visible content (empirically 3.5K-5K reasoning tokens for these prompts); Gemini 2.5 Pro and Anthropic Claude Opus 4.7 produce more compact visible output and need lower caps to keep cost bounded. Final caps after pilot iteration:

- deepseek: 8000 max tokens
- openai: 8000 max tokens
- gemini: 5000 max tokens (bumped from 3000 mid-run after observed truncations)
- anthropic: 4000 max tokens (bumped from 2500 mid-run after observed truncation)

Claim extraction was manual. For each prompt, the human coder (Claude Code session run 2026-05-14) read all four responses and extracted atomic claims, then assigned each vendor a verdict: `affirm`, `disagree` (with named alternative), `ignore`, or `refusal`. Claim files live in `outputs/claims/<prompt-id>.json`. The coding rubric is documented in each claim file's `coding_notes`.

Pairwise agreement is computed by `analysis.py` over the six pairs spanning four vendors. Aggregation drops "one-ignored" pairs from the denominator (one vendor not addressing a claim is not a substantive disagreement). Refusals are recorded separately.

## Reproducing

```bash
# Set OPENROUTER_API_KEY in env or repo-root .env
python3 run_experiment.py                 # fires all prompts at all vendors, skipping cached
python3 run_experiment.py --force         # re-runs everything
python3 run_experiment.py --only-prompt 01-uricase --only-vendor deepseek
python3 analysis.py                       # computes agreement metrics from responses/ + outputs/claims/
```

Total cost of the pilot was $2.20 (well under the $15 budget; see `provenance.md` for token-level accounting).

## V1 simplifications worth flagging

- N=8 prompts is small. The paper section calls this "pilot evidence" not "definitive."
- Manual claim extraction means the agreement coding has irreducible human judgment in it. Each claim file is in JSON so the verdicts are auditable per-claim. A separate reviewer running through the same response files independently would be a stronger validation.
- Each vendor was called exactly once per prompt (single-shot, no replicate sampling). Within-vendor temperature noise is not measured. Replicate sampling within-vendor at the same temperature was outside scope.
- The Gemini and Anthropic max_tokens caps were calibrated mid-run after observing truncations. Two prompts (02, 03 for Gemini; 03 for Anthropic) were partially truncated. Re-runs at the higher cap are documented in `provenance.md`; the analysis uses the highest-coverage response per (prompt, vendor) pair.
- Prompts are synthetic-but-realistic rather than drawn directly from daemon Pass 2 production logs. Three prompts (04, 06, 08) are designed to mirror Pass 2 synthesis task shape but were not actually fired by the daemon. Prompt 07 is taken near-directly from the manuscript's own review-prompts catalog and is the closest to a real daemon call in the set.
- The single most striking inter-vendor finding (PTS1 disagreement on prompt 01) is documented in the paper section. That finding is itself a heterogeneity-guard validation: three vendors gave three different three-letter sequences for the same biochemical fact, and one vendor refused the prompt entirely.

## What was found

See `outputs/summary.md` and the paper section draft at `paper-section-draft.md` in this directory.
