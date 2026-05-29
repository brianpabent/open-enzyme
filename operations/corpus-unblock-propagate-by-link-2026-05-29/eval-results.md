# Workstream D — Pass-2 model eval results (2026-05-29)

Full-corpus single-shot synthesis via `scripts/fresh-synthesis.py` against the live corpus (commit `7668587`, ~928K–995K input tokens depending on provider tokenizer). Independent judge: Claude Opus 4.8 (different vendor than both candidates → satisfies the cross-vendor judging criterion). `--max-tokens 16000`.

## Scorecard

| Model | Window (spec) | Ingested full corpus? | Output | Cost | Quality | Verdict |
|---|---|---|---|---|---|---|
| **`meta-llama/llama-4-scout`** | 10M | ✅ 994,599 tok ingested | ❌ **0 output tokens** (content null) | $0.08 (input only, **wasted**) | n/a — produced nothing | **FAIL on default route** |
| **`x-ai/grok-4.20`** | 2M | ✅ 928,755 tok | ✅ 4,854 tok, full structured synthesis | **$1.17** | **High** — see below | **VIABLE Pass-2 primary** |
| `deepseek/deepseek-v4-pro` (incumbent primary) | 1.0M | ❌ overflows | — | — | (the problem) | broken at current corpus size |
| `google/gemini-2.5-pro` (incumbent fallback) | 1.048M live | barely (trimmed only) | — | — | — | fallback only |

## Llama 4 Scout — the cheap-huge promise did not materialize (this route)

- **Sanity check passed:** small prompt → "SCOUT OK", `finish_reason: stop`, served by **Groq**.
- **Full-corpus call:** ingested all 994,599 tokens (the 10M window genuinely held it) and **charged $0.08 for input — but returned 0 completion tokens, null content.** The model accepted the context and generated nothing.
- **Diagnosis:** advertised 10M is Meta's *model* spec; the *serving provider* (Groq, via the default OpenRouter route) does not deliver usable generation at ~1M-token input. This is the exact "advertised window ≠ usable window, provider route matters" risk flagged in spec §D2 — and it's worse than a clean failure, since you pay for input and get nothing.
- **Open follow-up (not blocking):** probe alternate providers for Llama 4 Scout on OpenRouter (provider routing override) to see if any serve real long-context generation. Only worth it if the ~16× input-cost saving becomes load-bearing.

## Grok 4.20 — high-quality, usable, full-corpus-coherent

Read the corpus correctly (identified the ABCG2 gut-sink thesis, Q141K/butyrate-HDAC rescue, androgen-urate axis reframe, comp-001–039) and produced a properly structured synthesis with evidence tags, PMIDs, file refs, and costed suggested actions. Specific strengths:

- **Caught a real contradiction the corpus carries:** the Fu 2025 (PMID 40589746) lactoferrin CP5b/M2-polarization claim is from a *combination* formulation (cordycepin + lactoferrin + Sargassum), so attributing M2 polarization to lactoferrin alone is an overclaim — recommends downgrading CP5b to "speculative indirect." Sharp, correct, and actionable.
- **Lost-in-the-middle: passed.** Pulled details from across the whole corpus, not just head/tail — CFH Y402H (rs1061170), comp-039 two-model consensus, theaflavins Tier-1 promotion, §3.11 exertion-challenge, §1.28 Tier-2 cordycepin assay. Strong evidence it actually synthesized the full breadth.
- **Proper differential analysis** vs the daemon's last synthesis (confirmed / partial / push-back / rejected / missed-by-daemon / missed-here).

**Minor caveats:** one connection (lactoferrin substrate-supply synergy) is emitted twice near-verbatim (lines 38 & 47) — a mild long-context coherence wobble; and a cosmetic wrong-date artifact in the output header ("2026-05-21"). Neither disqualifying.

## Recommendation

1. **Grok 4.20 is a viable immediate unblock as Pass-2 primary.** It works at the *current* corpus size (which DeepSeek cannot), with ~1M tokens of growth headroom, at ~$1.17/run (~3× DeepSeek's ~$0.40 — ~$12/mo vs ~$4/mo at ~10 sweeps/month; marginal in absolute terms). One config change.
2. **Keep a different-vendor fallback** (heterogeneity guard): Grok primary + Gemini 2.5 Pro fallback now; add DeepSeek back as a second fallback once Workstreams A+B bring the corpus under its 1.0M cap. Pipeline stays multi-vendor (Pass 1 / Pass 2 Grok / Pass 3) — actually *more* diverse than before.
3. **A/B/C are not obviated — their role shifts from "emergency unblock" to "quality + cost + durability":** dedup (A) lowers Grok's per-run input cost and improves synthesis signal; propagate-by-link (B) bends the growth curve so even 2M doesn't get eaten; guard fixes (C) would have hard-failed Scout's pay-for-nothing empty-output instead of silently charging.
4. **Scout:** park as an alternate-provider probe; do not rely on the default (Groq) route.

## Agentic daemon-equivalent confirmation (Codex round-2 #2 follow-up) — EXECUTED 2026-05-29

The first-pass screen above was single-shot. Per Codex #2, Grok was re-run through the **real daemon Pass-2 harness** — `scripts/synthesize.py --commit-sha HEAD --model x-ai/grok-4.20` — which exercises the agentic tool loop and near-cap growth that is the actual failure mode. Required C1 first (add Grok's 2M cap to `CONTEXT_WINDOW_TOKENS`, else the pre-flight rejects).

**Result: PASS.**
- `in=934,289  out=7,624  cost=$1.1869  exit 0`, no fallback (`reviewer_fallback_used: False`).
- **Cited 70 wiki files via the `read_file` tool** — spanning `wiki/etc/` pages, all 9 hypothesis cards (H01–H09), and comp-NNN pages across the corpus. Confirms tool support + multi-turn context accumulation work, and that 934K prompt + tool growth stays comfortably under the 2M window.
- Output (`logs/v4-synthesis-2026-05-29-HEAD.md`) is a correctly-formatted Pass-2 synthesis following the daemon's own conventions (New Connections with `[CHAIN-DEPTH]`/`[PHASE-A-MATCH]` markers, Contradictions, Experiments, Open Questions, Priority Actions, Riskiest Assumption, Sources cited).

**Conclusion:** Grok 4.20 is validated as Pass-2 primary on *both* the quality screen and the agentic daemon-equivalent run. The routing switch (§D8) is unblocked.

## Reproduce

```bash
python3 scripts/fresh-synthesis.py --model x-ai/grok-4.20 --max-tokens 16000
python3 scripts/fresh-synthesis.py --model meta-llama/llama-4-scout --max-tokens 16000
```
Output logs: `logs/fresh-synth-grok4.20-2026-05-29.md`, (Scout produced no output file — empty completion).
