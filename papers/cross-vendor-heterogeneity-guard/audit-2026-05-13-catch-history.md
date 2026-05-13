---
title: Open Enzyme catch-history audit
date: 2026-05-13
auditor: Claude Sonnet (via Explore subagent, Claude Opus orchestrator)
scope: full repo git history + operational notes + synthesis directory + eval runs
context: candidate-catch sweep for the heterogeneity-guard methodology paper
status: primary source — preserve verbatim
---

# Open Enzyme catch-history audit (2026-05-13)

This document preserves the audit memo returned by a wide-scope Explore subagent on 2026-05-13, run during drafting of the cross-vendor-heterogeneity-guard methodology paper. The subagent walked git history across `wiki/`, `synthesis/`, `scripts/`, `logs/`, `operations/`, and `evals/`, and returned candidate catch moments not yet in the paper's §5 case studies.

**Why preserved verbatim:** the agent surfaced ~3 dozen distinct items with specific commit hashes and file paths. Curation/triage happens in `papers/future-work-pipeline.md` (which references this file); the raw memo stays unfiltered so we can re-curate later without re-running the audit.

**Verification status:** commit hashes and file paths in the memo are agent-reported. Each item used in the paper or in future work must be independently grep-verified against the codebase per the project's pre-commit grep-verify gate (`CLAUDE.md` Rule 4). The agent's summary describes what it intended to find, not necessarily what is canonical.

---

## AUDIT MEMO: Cross-Vendor Heterogeneity Guard — Operational Catch Moments Not Yet in §5

### Executive Summary

The Open Enzyme repository's git history, operational logs, and paper-drafting artifacts surface **at least 7 distinct catch classes and 31+ operational catch moments** not yet covered in the cross-vendor heterogeneity paper's current §5 case studies.

---

## 1. TOP CANDIDATES FOR NEW CONTENT — NOT YET IN PAPER

### 1.1 Workflow-Level Race Condition & Recovery (2026-04-28, Failure Class: CI Infrastructure)

**Date(s):** 2026-04-28 (commits `5e106e9`, run 25051936845)
**Source:** `scripts/SWEEP-ARCHITECTURE.md` §"Failure modes observed (2026-04-28)" + git log run analysis

**What happened:** Pass 1 (Sonnet propagate) completed and pushed; Pass 2 (Gemini synthesize) ran fully to completion, generating a 62-line synthesis log costing $0.7288; then `git push` failed with `! [rejected] main -> main (fetch first)` because concurrent commits had landed on `main` between Pass 1's push and Pass 2's push. Pass 3 never ran. The synthesis artifact existed only in the ephemeral GitHub Actions runner and was discarded on teardown.

**Root cause:** No `git pull --rebase origin main` before push after Pass 1.

**Downstream:** `scripts/SWEEP-ARCHITECTURE.md` §"Inter-pass artifact handoff (added 2026-04-28)" — redesign of Pass 1 → Pass 2 → Pass 3 handoff including `propagated_files` manifest, `cited_files` list, and agentic Pass 3 upgrade. Committed as `be5cbea`.

**Why interesting:** pure infrastructure catch — race condition in CI automation, structurally analogous to the pre-commit grep-verify gate for model hallucinations.

---

### 1.2 Transient API Outage + Retry Pattern (2026-04-28, Failure Class: External Dependency)

**Date(s):** 2026-04-28 (commit `3beb17f`, run 25049501442)
**Source:** `scripts/SWEEP-ARCHITECTURE.md` §"Run [25049501442]" + git log `05f8c74`

**What happened:** Pass 1 OpenRouter call returned HTTP 503. No retry mechanism. The shell wrapper exited non-zero on the first transient blip, terminating the full sweep. Separately Pass 2 hit HTTP 429 under high-volume sequential state.

**Downstream:** `05f8c74` (rebase-before-push + retry on stderr 5xx), `b5dd4e0` (retry-with-backoff on V4-Pro upstream rate limits). Exponential backoff 1s/2s/4s/8s on HTTP 5xx and 429.

**Why interesting:** orthogonal failure class to model confabulation — external service reliability.

---

### 1.3 Model-Swap Evaluation & Pass 3 Default Rotation (2026-05-07 to 2026-05-08)

**Date(s):** 2026-05-07 (eval run), 2026-05-08 09:32:05 (operational swap)
**Source:** `evals/pass-3-reviewer/2026-05-07-abc8de9-comparison.md`, commits `d612ad1`, `5d92079`, `e728d0d`

**Eval results on same synthesis log (6 markers, 17 trigger files, ~144K tokens inlined):**

| Metric | Opus 4.7 | GPT-5.5 (canonical prompt) | GPT-5.5 (tuned prompt) |
|--------|----------|---------------------------|----------------------|
| Cost | $8.44 | $1.09 (7.76× cheaper) | $1.66 (5.08× cheaper) |
| Tool-using rounds | 11 | 2 | 7 |
| Cached input tokens | 91% | 66% | 86% |
| RESTATEMENT-bias (6 markers) | 1/6 | 6/6 | 4/6 |
| EXTENSION verdicts | 3 | 0 | 2 |
| Push-back verdicts | 1 | 0 | 2 |

**Downstream:** commit `e728d0d` swapped Pass 3 default to GPT-5.5 with the tuned prompt.

**Why interesting:** purely empirical model-selection. Lesson: cross-vendor heterogeneity requires cross-vendor prompt tuning (an Anthropic-style prompt under-performs on OpenAI without adaptation).

---

### 1.4 Prompt Caching as Implicit Heterogeneity (2026-05-06)

**Date(s):** 2026-05-06 (commit `c0fd16e`)
**Source:** commit `c0fd16e` "scripts: add Anthropic prompt caching to Pass 3"; `evals/pass-3-reviewer/2026-05-07-abc8de9-comparison.md` (Opus 4.7 achieved 91% cache-hit rate)

**Why interesting:** third failure-class candidate — implicit heterogeneity via vendor-specific optimization. Anthropic's prompt caching, OpenAI's structured outputs, Gemini's natively-fluent multilingual support are not about model quality but about capability profiles. Architecture must adapt to each.

---

### 1.5 Post-Hoc Instrumentation Bug Discovery via Subagent (2026-05-13)

**Date(s):** 2026-05-13 (commit `877b089`)
**Source:** commit `877b089` "papers: catch 31 — sonnet subagent surfaced instrumentation bug in synthesize.py"

**What happened:** While drafting the heterogeneity-guard paper, a Sonnet subagent caught an observability gap in `synthesize.py` — fallback flag fired on OpenRouter alias expansion regardless of actual fallback.

**Why interesting:** observational catch with no model hallucination, brief bias, or API failure involved. Cross-vendor read surfaces observability gaps single-vendor loops miss.

---

### 1.6 Subagent Brief Contamination Verification Costs ~$5 (2026-05-08)

**Date(s):** 2026-05-08
**Source:** `operations/notable-moments.md` 2026-05-08 entry; `operations/comp-018-vs-comp-020-retrospective.md`

**Cost of verification:** ~$5 in subagent tokens + 30-60 min wall-clock.

**Why interesting:** brief hygiene is a prerequisite for heterogeneity to be effective. Contamination upstream of the subagent can't be caught by cross-vendor review downstream.

---

### 1.7 Three-Layer Citation Laundering in Supplement Industry (2026-05-07)

**Date(s):** 2026-05-07 (discovery), 2026-05-09 (comp-015 v2)
**Source:** `operations/notable-moments.md` 2026-05-07 entry; commits `a61f0d9`, `c32a623`

**Three layers caught:**
- **L1:** "37% testosterone elevation" figure traces to Talbott 2013 PMID 23705671 — salivary T in mixed-sex moderately-stressed cohort, treated by supplement marketing for a decade as serum free-T in hypogonadal men
- **L2:** "Shin KH 2024 enclomiphene vs clomiphene" citation appears in parent + daughter wiki pages, doesn't exist in PubMed. Actual paper is Saffati G et al. 2024 PMID 39434750
- **L3:** "eurycomanone is an XO inhibitor" — neither cited PMID claims XO inhibition. True mechanism is multi-target transporter modulation + PRPS suppression. **Direction-of-effect flipped:** v1 GOUT-UNFAVORABLE → v2 GOUT-FAVORABLE

**Why interesting:** corpus-level contamination that single vendors inherit identically from training. Multi-vendor cross-checks don't help — all vendors see the same contaminated training corpus. What protected: verification-of-verification (independent subagent checks the verification subagent against primary source).

---

### 1.8 Synthesis Filesystem Migration — Multi-Pass Design Review (2026-05-08)

**Date(s):** 2026-05-08
**Source:** `operations/specs/2026-05-08-synthesis-filesystem-migration-*.md` (spec-review, spec-rereview, code-review, third-pass-review); commits `74bf294`, `4e5bc3f`, `abc2671`, `a3df0a6`

**What happened:** Major architectural refactor (queue/ → history/ → done/ atomic handoff), specified, cross-reviewed (Opus spec-review → re-review → code review). Spec review surfaced 6 named deficiencies (N1-N6). Code review returned NEEDS-REWORK.

**Why interesting:** heterogeneity as collaborative design-review discipline, not just sweep automation. Structurally analogous to academic peer review.

---

## 2. WORKFLOW CHANGES & OPERATIONAL DISCIPLINES NOT YET IN PAPER

### 2.1 Hardened Cursor Advancement (2026-05-07)

**Date:** 2026-05-07 (commit `45db8eb`)
**Source:** commit message "workflow: advance cursor to Pass 3 review commit, not workflow trigger SHA"

**What happened:** workflow cursor was advancing to the workflow trigger SHA instead of the last Pass 3 review commit. Multi-commit batches lost earlier commits from the diff-base.

### 2.2 Per-Commit Truncation Tolerance (2026-05-08 to 2026-05-09)

**Dates:** 2026-05-08, 2026-05-09
**Source:** commits `dd513ee` (parser tolerance), `57f5adc` (truncation_drops audit trail), PR #6

**What happened:** Pass 2 hit token-budget limits and truncated mid-sentence. Parser failed hard on marker-count misalignment. Fix: log truncation to manifest, continue with partial synthesis, pass truncation manifest to Pass 3 as context.

---

## 3. FAILURE CLASSES NOT YET CATEGORIZED IN §5

### 3.1 Within-Vendor Confabulation Caught by User Push-Back (Not Pipeline)

**Date:** 2026-05-13 (papers drafting, Catch 1 in revisions.md)
**Source:** `papers/cross-vendor-heterogeneity-guard/revisions.md` Catch 1

**Incident:** Claude Opus answered "I don't have reliable information on a Google product called Paper Orchestra" without checking the repo. User push-back ("did you look in the repo?") immediately surfaced two files with detailed PaperOrchestra coverage.

**Why interesting:** confabulation the model SHOULD have caught by primary-source verification. Reflexively powerful: it happened while drafting the paper that warns against this exact failure mode.

### 3.2 Direction-of-Effect Reversal via Mechanism Verification (2026-05-07)

**Date:** 2026-05-07 (comp-015 v2, commit `c32a623`)
**Source:** commit `c32a623` "wiki: comp-015 v2 — t-axis adjuvant urate-target mapping (XO added; eurycomanone gout-favorable reversal)"

**What changed:** v1 tagged eurycomanone GOUT-UNFAVORABLE (assumed XO inhibitor); v2 verified mechanism is multi-target transporter modulation + PRPS-suppression — GOUT-FAVORABLE.

**Why interesting:** the reversal was caught by verification-of-verification, not by vendor heterogeneity. Different defensive mechanism than the paper currently emphasizes.

---

## 4. PRE-DAEMON VS. POST-DAEMON COMPARISON

### 4.1 Single-Session Manual Sweep vs. Three-Pass Daemon

**Pre-daemon (before 2026-04-25):**
- Trigger: Brian pushes to wiki/, manually fires Claude Opus 4.7 in local session
- Process: single agent walks corpus, emits to `operations/notable-moments.md` or `wiki/synthesis.md`
- Bottleneck: single-vendor training distribution, synchronous human attention
- Wall-clock: 1-3 hours per day

**Post-daemon (2026-04-25 onward):**
- Trigger: push to wiki/ fires GitHub Actions
- Process: 3 passes async, cross-vendor
- Wall-clock: ~9-12 min per run, unbounded runs per day
- Cost per sweep: $0.65–$1.20 at OpenRouter rates

**Catches per sweep window:**
- 2026-05-05 to 2026-05-13 (8 days post-daemon): 31+ explicit catch moments
- 2026-04-25 to 2026-05-05 (transition era): 2-3 major catches named (DAF disulfide, Paperclip, CP0 reframe)

### 4.2 Model Assignments Have Drifted Deliberately

Each drift driven by operational experience or explicit eval:
- Pass 1 → DeepSeek V4-Pro (commit `913eea2`, 2026-05-06)
- Pass 2 → DeepSeek primary, Gemini fallback (commit `a412109`, 2026-05-07)
- Pass 3 → GPT-5.5 with tuned prompt (commit `e728d0d`, 2026-05-08)

Upstream vendors (propagate, synthesize) prioritize speed + cost. Downstream vendors (review) prioritize depth + discrimination.

---

## 5. SURPRISING FINDINGS & CONTRADICTIONS TO CURRENT FRAMING

### 5.1 Convergence Without Coordination (2026-05-08)

Brian published "Grounding the AI Scientist Hype" blog (private repo) using DAF SCR1-4 as case study, same day the daemon's Pass 2 (Gemini) independently surfaced DAF SCR1-4 as a finding worth publicizing. Pass 3 (GPT-5.5) push-back "already documented" — correct for wiki, but the daemon doesn't read external surfaces.

**Why interesting:** generative property of heterogeneity (two independent reads converge on same valuable angle without coordination) + scope-limitation property (daemon correctly bounded to wiki; external-surface action stays human responsibility).

### 5.2 Multi-Vendor Disagreement on "What's Novel" (2026-05-07 eval)

Same synthesis, 6 markers:
- Opus 4.7: 2 NOVEL, 3 EXTENSION, 1 RESTATEMENT
- GPT-5.5 (canonical): 0/0/6
- GPT-5.5 (tuned): 0/2/4

**Why interesting:** cross-vendor heterogeneity doesn't resolve subjective dimensions (e.g., novelty threshold). It exposes them. The paper should acknowledge: heterogeneity surfaces disagreement, doesn't settle it.

### 5.3 Truncation + Graceful Degradation as Architectural Principle

Complementary to heterogeneity: when a component fails partially, the system degrades gracefully rather than cascading. Together, heterogeneity + graceful-degradation form a resilient system.

---

## 6. METHODOLOGICAL INSIGHTS NOT YET CODIFIED

### 6.1 Five-Rule Verification Protocol for External Tools

**Source:** `wiki/manual-literature-mining.md` §"Verification gate discipline"

1. Safe primitives only (search/cat/head/grep/scan); ban `map`/`reduce`
2. Anchor identity to canonical accessions, not inferred
3. Grep-verify all numbers before wiki entry
4. Never propagate aggregation summaries; re-derive from safe primitives
5. Cite line-anchored

### 6.2 Translation Protocol (Two-Model Cross-Check + Inline Disagreement)

**Source:** `CLAUDE.md` §"Translation protocol"

Structurally analogous to the multi-pass sweep, applied at the translation level rather than synthesis level. Could stand on its own as a discipline.

---

## 7. FINDINGS WITH QUANTIFIED IMPACT

| Finding | Dates | Cost | Impact | Tier |
|---------|-------|------|--------|------|
| Brief contamination (comp-018 vs 020) | 2026-05-08 | ~$5, 30-60min | Helicteres found at headline tier (4-20× missed); mechanism reframe | Verified |
| Citation laundering (androgen-urate axis) | 2026-05-07–09 | ~$3-4 | Direction-of-effect reversal; 3 wiki pages corrected | Verified |
| Pass 3 model swap (Opus → GPT-5.5 tuned) | 2026-05-07–08 | Eval cost | 5× cost reduction; verification depth 2 → 7 tool calls | Empirical eval |
| Prompt caching (Opus 4.7 Pass 3) | 2026-05-06+ | ~$0.20/review amortized | 91% cache-hit; effective ~75% cost reduction | Measured |
| Retry-with-backoff | 2026-04-28+ | ~$0.05/retry | Eliminated silent 503/429 failures; 100% recovery | Empirical |
| Truncation tolerance | 2026-05-08+ | ~$0.01/check | Large sweeps recover partial synthesis | Empirical |

---

## 8. PRIMARY SOURCES FOR VERIFICATION

| Finding | File | Commit | Notes |
|---------|------|--------|-------|
| Race condition + retry hardening | `scripts/SWEEP-ARCHITECTURE.md` | `f3aa802`, `be5cbea`, `05f8c74` | §"Failure modes observed" |
| Pass 3 model eval | `evals/pass-3-reviewer/2026-05-07-abc8de9-comparison.md` | `5d92079` | Full document |
| Brief contamination | `operations/comp-018-vs-comp-020-retrospective.md` | `a2a4035` | Comprehensive side-by-side |
| Citation laundering (tongkat ali) | `operations/notable-moments.md` 2026-05-07 entry | `e3ff73a` | Three-layer analysis |
| Paperclip tool reliability | `wiki/manual-literature-mining.md` + `operations/notable-moments.md` 2026-05-07 | `cca03f6`, `6665b3e` | Five-rule protocol |
| Paper drafting catches | `papers/cross-vendor-heterogeneity-guard/revisions.md` | `9a2aaf2` | 8 self-catches + appendix-B plan |
| Truncation tolerance | commits `57f5adc`, `dd513ee` | `259a8e8` (merge) | Parser impl |
| Translation protocol | `CLAUDE.md` | `f6d3c77` (2026-05-05) | §"Translation protocol" |

---

## 9. RECOMMENDATIONS

**Strongly recommended for paper inclusion:**
1. §3 or §4 insertion: race condition + retry hardening as a failure class ("Infrastructure-layer heterogeneity")
2. §5 expansion: citation laundering / verification-of-verification as a fourth case study (or §5.6)
3. §6 revision: quantify costs of different verification disciplines (brief scrubbing ~$5, V-of-V ~$3-4, retry negligible)
4. Appendix B addition: explicit note that the paper's own production surfaced Catch 1 (confabulation) and Catch 27 (Pass 3 model name error)
5. Methods note: distinguish "cross-vendor heterogeneity" (different vendors reading same substrate) from "verification-of-verification" (independent subagent checks first subagent against primary source)

**Not recommended for THIS paper (track separately):**
- Individual code-review catches on the synthesis-filesystem-migration spec
- Every CI/workflow hardening commit
- Translation-protocol details

---

*End audit memo.*
