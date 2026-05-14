# Provenance and audit trail

Per-call records of the pilot run on 2026-05-14, in `responses/_cost_log.jsonl`. Each line records prompt_id, vendor key, requested model slug, OpenRouter-served model slug, prompt-tokens, completion-tokens, latency, status (ok / empty / error), and any error message.

## Run timeline

Single Claude Code session on 2026-05-14 starting ~11:00 AST. The first vendor call (DeepSeek on prompt 01) fired at 11:02:15 UTC. The full eight-prompt × four-vendor sweep completed at approximately 11:50 UTC. Total wall-clock for the experiment was ~48 minutes; the bulk of that was OpenAI GPT-5.5 reasoning latency (typically 120-200 seconds per call) and DeepSeek V4-Pro reasoning latency (typically 70-180 seconds per call).

## Mid-run script changes

Two changes to `run_experiment.py` were made during the run, both visible in git history:

1. **DeepSeek empty-response on `finish_reason=length`** caught at first call. DeepSeek V4-Pro is a reasoning model and consumed all 1500 of the initial token budget on internal reasoning, emitting no visible content. The `MAX_TOKENS` constant was bumped to 4000, then split into a per-vendor `MAX_TOKENS_BY_VENDOR` dict with values calibrated to each vendor's reasoning behavior.

2. **Anthropic cost recorded as $0.0000** caught on prompt 02. The `PRICING_USD_PER_MTOK` dict was keyed on `anthropic/claude-opus-4-7` but OpenRouter sometimes returns the served slug as `anthropic/claude-4.7-opus`. Both slugs were added to the pricing dict, and the `analysis.py` script recomputes any zero cost-of-record from served-model + token counts.

The changes to `MAX_TOKENS_BY_VENDOR` were applied while the run was in progress, so prompts 02-08 were called with the lower (mid-run-stale) caps for Gemini (3000) and Anthropic (2500). Several Gemini responses (prompts 02, 03, 04, 06) and several Anthropic responses (prompt 03 mid-paragraph) were truncated mid-output. These truncations are recorded in each affected response file's frontmatter (`finish_reason: length`) and surface in the analysis as `ignore` verdicts on un-addressed sub-claims. Truncated responses were not re-run for this pilot; the analysis treats their uncovered sub-claims as coverage gaps, not disagreement signals.

## Vendor-by-vendor cost summary

Recomputed from raw token counts × per-vendor pricing (current as of 2026-05-14). Includes both the initial run and the targeted re-runs of Gemini and Anthropic at higher max_tokens caps after the initial run's truncation events.

| Vendor | Slug | OK calls (used) | Refusals | Cost |
|---|---|---|---|---|
| deepseek | `deepseek/deepseek-v4-pro` | 8 | 0 | ~$0.035 |
| gemini | `google/gemini-2.5-pro` | 8 | 0 | ~$0.18 |
| openai | `openai/gpt-5.5` | 8 | 0 | ~$0.56 |
| anthropic | `anthropic/claude-opus-4-7` | 7 | 1 | ~$1.43 |
| **TOTAL** | | **31** | **1** | **$2.20** |

(Final precise figure from `analysis.py`: $2.2022. The pilot stayed well under the $15 budget. Anthropic dominates cost because of its 5x pricing premium relative to the next-most-expensive vendor.)

## Refusal events

| Prompt | Vendor | finish_reason | native_finish_reason | Notes |
|---|---|---|---|---|
| 01-uricase-mechanism-factual | anthropic | stop | refusal | Anthropic Claude Opus 4.7 refused the prompt's "do not confabulate" wording. Verified by independent probe: shorter forms of the same factual question yielded full responses; the trigger appears to be a specific phrasing convention in the original prompt. No content emitted. Recorded as `status: EMPTY` in the response file. |

## Truncation events

The following responses were truncated mid-output by `finish_reason=length`:

| Prompt | Vendor | Output tokens | Visible content covered |
|---|---|---|---|
| 02-abcg2-q141k-factual-quant | gemini | 2996 | Reached section 2 only (4 of 5 sub-questions un-addressed) |
| 03-nlrp3-mechanism-inference | gemini | 2996 | Reached partial section 1 only (mechanism 1 partial; 2/3 of mechanisms + alternative un-addressed) |
| 03-nlrp3-mechanism-inference | anthropic | 2500 | Reached mid-final-paragraph of alternative-mechanism section; key content captured |
| 03-nlrp3-mechanism-inference | openai | 8000 | Hit upper cap; covered all required elements but trailed off mid-citation list |
| 04-koji-uricase-hypothesis-gen | gemini | 2996 | Reached only mid-assumptions block before truncating |
| 04-koji-uricase-hypothesis-gen | anthropic | 2500 | Truncated mid-experiment-3 (covered 1-2 of 3 experiments fully) |
| 05-rasburicase-ada-mechanism | gemini | 2996 | Truncated mid-section-2 (covered rasburicase mechanisms only, no pegloticase comparison) |
| 06-cross-document-synthesis | gemini | 2996 | Reached only mid-section-1 (4 of 4 sub-questions effectively un-addressed) |
| 06-cross-document-synthesis | anthropic | 2500 | Truncated at summary line; main 4-question content covered |

Truncations affect Gemini and Anthropic disproportionately because the mid-run-fixed `MAX_TOKENS_BY_VENDOR` change did not apply retroactively. A production replication using the corrected caps (5000 for Gemini, 4000 for Anthropic) would close most of these gaps.

## Response-text SHA-256 prefixes

Each response file's YAML frontmatter records a 12-character prefix of the response body's SHA-256 hash, and a 12-character prefix of the prompt body's SHA-256 hash. This is sufficient for grep-verifiable claims of "this analysis was run against this specific response text." The full SHA-256 of any response can be recomputed by re-hashing the response body (everything after the closing `---` of frontmatter).

## How to verify any specific claim

1. The PTS1 disagreement on prompt 01: open `responses/01-uricase-mechanism-factual/<vendor>.md` and search for "SKL" / "SRL" / "SSH" in the body. Verdict coded in `outputs/claims/01-uricase-mechanism-factual.json` claim C1.5.
2. The pegloticase production-host push-back on prompt 05: open `responses/05-rasburicase-ada-mechanism/openai.md` and search for "Minor factual correction." Verdict coded in `outputs/claims/05-rasburicase-ada-mechanism.json` claim C5.4.
3. The Anthropic refusal on prompt 01: open `responses/01-uricase-mechanism-factual/anthropic.md` and read frontmatter `finish_reason: stop` + `status: EMPTY` + body `(empty content)`. Documented further in this file's "Refusal events" table.

## Raw OpenRouter response inspection

For prompt-01 Anthropic refusal, the full OpenRouter response was inspected directly via `curl` during diagnosis (see Claude Code session transcript 2026-05-14). The key fields were:

```
"finish_reason": "stop",
"native_finish_reason": "refusal",
"message": {"role": "assistant", "content": null, "refusal": null, "reasoning": null}
```

OpenRouter's `native_finish_reason: refusal` with `refusal: null` indicates the upstream provider (Anthropic API) classified the prompt as triggering a content policy without emitting a refusal message. This is the model-side refusal signal, not a content-filter trip; verified by the independent probe showing the same factual question (rephrased) answers cleanly.
