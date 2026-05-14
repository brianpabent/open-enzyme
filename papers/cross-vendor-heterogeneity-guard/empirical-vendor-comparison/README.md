# Empirical vendor-comparison pilot

> **Canonical numbers and narrative live in `../draft.md` §6.** This README documents the artifact directory structure and reproducible pipeline. The canonical post-audit numbers are cross-vendor 82.3%, within-vendor 90.8%; Gemini answered SKL correctly on r1; the audit-trail claim-coding mismatch was caught by an independent cross-vendor manuscript review on 2026-05-14 and is preserved as the §6 meta-catch in the paper. Computed outputs (`outputs/agreement-matrix.json`, `outputs/within-vendor-matrix.json`, `outputs/summary.md`, `outputs/within-vendor-summary.md`) and the claim files (`outputs/claims/*.json`) are post-correction. `paper-section-draft.md` in this directory is a superseded intermediate draft retained for provenance; where it differs from `../draft.md` §6, the latter is canonical.

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
python3 run_experiment.py                 # fires all prompts at all vendors at replicate 1
python3 run_experiment.py --replicate 2   # fires replicate 2 (writes to <vendor>-r2.md)
python3 run_experiment.py --replicate 3   # fires replicate 3 (writes to <vendor>-r3.md)
python3 run_experiment.py --force         # re-runs everything for the active replicate
python3 run_experiment.py --only-prompt 01-uricase --only-vendor deepseek --replicate 2
python3 analysis.py                       # computes cross-vendor agreement from responses/ + outputs/claims/
python3 analysis_within_vendor.py         # computes within-vendor agreement across replicates
```

The original pilot ran $2.20 at N=1 replicate per cell. The within-vendor replicate study added 64 more calls (32 cells × 2 additional replicates) for an incremental $4.38, bringing total project cost to $6.58 against a $10 ceiling. See `provenance.md` for token-level accounting.

## Intra-vendor variance study (replicate sampling)

To partition the corrected 17.7% cross-vendor disagreement into (a) real cross-vendor heterogeneity and (b) within-vendor temperature stochasticity, each of the 32 (prompt, vendor) cells was called twice more at the same prompt, same temperature (0.7), same per-vendor max_tokens cap. The original pilot run is replicate 1 (`<vendor>-r1.md`); the additional calls are replicate 2 (`<vendor>-r2.md`) and replicate 3 (`<vendor>-r3.md`). Each replicate response is coded against the same atomic-claim taxonomy from the original run; replicate verdicts are at `outputs/claims/<prompt-id>-r{2,3}.json`.

Within-vendor pairwise agreement is computed across the three replicates per cell (r1-r2, r1-r3, r2-r3 = three pairs per cell), aggregated across 32 cells. Output at `outputs/within-vendor-matrix.json` and `outputs/within-vendor-summary.md`.

**Headline within-vendor agreement: 90.8%** (versus 82.3% cross-vendor), implying that roughly half of the corrected cross-vendor disagreement reflects real vendor-prior difference and roughly half reflects within-vendor temperature noise. Per-vendor stability does *not* support the reasoning-mode hypothesis: Anthropic (94.0%) is the most stable, with reasoning and non-reasoning models bracketing each other. See `../draft.md` §6 for the canonical interpretation.

## V1 simplifications worth flagging

- N=8 prompts is small. The paper section calls this "pilot evidence" not "definitive."
- Manual claim extraction means the agreement coding has irreducible human judgment in it. Each claim file is in JSON so the verdicts are auditable per-claim. A separate reviewer running through the same response files independently would be a stronger validation.
- The initial pilot called each vendor once per prompt; the intra-vendor variance study described above addressed that limitation with N=3 replicates per cell. N=3 captures modal behavior; if within-vendor variance is real, three samples surface it. N=10+ replicates per cell would tighten per-vendor stability estimates and is v2 work.
- The Gemini and Anthropic max_tokens caps were calibrated mid-run after observing truncations. Two prompts (02, 03 for Gemini; 03 for Anthropic) were partially truncated. Re-runs at the higher cap are documented in `provenance.md`; the analysis uses the highest-coverage response per (prompt, vendor) pair.
- Prompts are synthetic-but-realistic rather than drawn directly from daemon Pass 2 production logs. Three prompts (04, 06, 08) are designed to mirror Pass 2 synthesis task shape but were not actually fired by the daemon. Prompt 07 is taken near-directly from the manuscript's own review-prompts catalog and is the closest to a real daemon call in the set.
- The single most striking inter-vendor finding (PTS1 disagreement on prompt 01) is documented in the paper section. That finding is itself a heterogeneity-guard validation: two of three non-refusing vendors gave the canonical SKL answer, one returned a near-neighbor wrong tripeptide, and one vendor refused the prompt entirely. The first coding pass incorrectly recorded Gemini r1 as SSH; the corrected claim file preserves that as an `audit_correction`.

## What was found

See `outputs/summary.md` and the paper section draft at `paper-section-draft.md` in this directory.
