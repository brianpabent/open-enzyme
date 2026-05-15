---
type: open-question
sweep_date: 2026-05-13
sweep_sha: 69103ce
section_index: 2
global_index: 9
pass3_verdict: Confirmed
overlap_tag: RESTATEMENT
---

# Does the BioDesignBench finding that DeepSeek V3 outperforms GPT-5 and Gemini 2.5 Pro on protein-design tasks hold for the specific tasks relevant to Open Enzyme (uricase variant scoring, chaperone-orthogonal stacking predictions, signal-peptide compatibility)?

2. **Does the BioDesignBench finding that DeepSeek V3 outperforms GPT-5 and Gemini 2.5 Pro on protein-design tasks hold for the specific tasks relevant to Open Enzyme (uricase variant scoring, chaperone-orthogonal stacking predictions, signal-peptide compatibility)?** The benchmark’s 76 tasks span diverse protein classes; it is not yet verified whether the DeepSeek advantage is uniform or restricted to certain task types. If the advantage is broad, it strengthens the architectural justification for using DeepSeek V4-Pro as the sweep daemon’s Pass 4 peer-reviewer. If narrow, the multi-model architecture should retain model diversity rather than consolidating on DeepSeek. (Context: `bio-ai-tools.md` §“BioDesignBench”; `open-source-platform.md` §“Multi-model synthesis”.)

> **Pass 3 review — Confirmed.** `[OVERLAP: RESTATEMENT]` This is a valid open question and already captured in the source page. `bio-ai-tools.md` says BioDesignBench covers 76 protein-design tasks, reports DeepSeek V3 outperforming GPT-5 and Gemini 2.5 Pro per abstract, and explicitly lists "whether V3 outperforms across all 76 tasks or only on some protein classes" as a verification item before promotion. The right disposition is to keep the question open until the PDF is fetched and the task-type breakdown is grep-verified.

---

## ✓ Actioned 2026-05-15 — significantly larger scope than the original framing

Brian pushed back on the original "vendor benchmarking" thread: he shared BioDesignBench to see what it teaches about **protein design**, not which language model performed best. And he flagged that we never tried the bioRxiv MCP server. Investigation revealed that `claude mcp list` showed both bioRxiv MCP and Paperclip MCP currently failing to connect, but the bioRxiv API endpoint (`api.biorxiv.org/details/...`) worked for metadata + verbatim abstract, and Brian dropping the PDF locally + `pdftotext -layout` unblocked the full text. The "Cloudflare blocked 2026-05-12 — PRIMARY-SOURCE-PENDING" gate was illusory; OE downstream work had built workflow around the abstract-only summary for three days, missing the actually-load-bearing finding.

**What the paper actually finds (verified against full PDF):** The headline is **behavioral, not capability-limited.** Top LLM agents (DeepSeek V3, GPT-5) pick the right tools but invoke scoring/evaluation at **only ~14% of expert intensity** and **never discard a generated candidate across 836 task-condition observations**. Forcing multi-metric evaluation (≥3 metric categories per candidate, compute-matched) recovers DeepSeek V3 by +9.3 points and GPT-5 by +15.9 points. The hardcoded pipeline (already multi-metric) gains nothing from the intervention — confirming the deficit is specifically behavioral. Tool-gap vs. science-gap decomposition: DeepSeek V3 + GPT-5 dominated by tool-gap; Gemini 2.5 Pro by science-gap. Public leaderboard + 17-tool MCP package available (MIT licence).

**Files shipped (six pieces per the revised Item 12 plan, minus the Gemini Pass 2 reconsideration Brian explicitly declined):**

1. **`wiki/bio-ai-tools.md` §BioDesignBench** — full rewrite. DOI corrected from `10.1101/` to `10.64898/`; PRIMARY-SOURCE-PENDING flag lifted; behavioral findings promoted to headline; full leaderboard cited (Human oracle 75.2, Human expert 61.7, DeepSeek V3 60.6, GPT-5 55.8, Hardcoded 54.5, Sonnet 4.5 50.5/41.2, Gemini 2.5 Pro 8.8/8.1); tool-gap/science-gap finding cited with per-model attribution; protein-design-mcp package documented as deployable; task taxonomy mapped (5 subjects × 2 design intents); contamination policy noted (task specs not publicly released). Cross-link to the new memory.
2. **`wiki/autonomous-screening-methodology.md`** — new "BioDesignBench evaluation-depth audit" section with per-comp-NNN audit table (comp-019 through comp-027) against three failure-mode axes. comp-024 and comp-027 flagged for audit follow-up; comp-022 named as the canonical exemplar. Three concrete action items.
3. **`scripts/sweep-prompt-3-review-gpt55.md`** and **`scripts/sweep-prompt-3-review.md`** — "Evaluation depth > tool coverage" sub-section added to each Pass 3 prompt's retrieval-budget area. Anchored to the BioDesignBench finding; sharpens the existing anti-shallow-eval language with empirical citation.
4. **`.claude/skills/walk-synthesis/SKILL.md` §4 briefing rules** — new rule #9 "Deep multi-metric evaluation discipline" requires comp-NNN subagent briefs to enforce (a) multiple candidates, (b) ≥3 orthogonal metric categories, (c) head-to-head + filter before termination. Anchored to BioDesignBench.
5. **`papers/cross-vendor-heterogeneity-guard/draft.md` §"Capability profile and exposed subjectivity"** — new "Empirical convergence with BioDesignBench" paragraph added. Frames BioDesignBench as independent convergent evidence (not load-bearing) for the heterogeneity-guard architecture's failure-mode targets. Cites the tool-gap/science-gap per-vendor pattern + the behavioral-not-capability finding.
6. **`wiki/daf-cd55-scr14-truncated-computational.md`** + **`wiki/lactoferrin.md`** — new "Open follow-up — RFdiffusion + ProteinMPNN tool-stack integration" sections on both pages with explicit "Fires when" triggers gated on the wet-lab work surfacing folding-yield problems the current ESM2 + Boltz-2 stack can't resolve. Phase 2 tasks listed for the integration if triggered.

**Brian-declined scope** (recorded for completeness): the proposed audit of OE's Pass 2 synthesizer choice (Gemini 2.5 Pro's BioDesignBench score of 8.8) was explicitly declined — Brian: "We've done our own evals, so I don't care that they had tooling issues." OE's Pass 2 use case (text-only corpus synthesis) is structurally different from BioDesignBench's tool-calling-heavy benchmark; the BioDesignBench Gemini result does not transfer.

**New memory saved:** [`memory/feedback_dont_treat_single_failed_fetch_as_durable_gate.md`](../../../.claude/projects/-Users-brianabent-Documents-Claude-Projects-abent/memory/feedback_dont_treat_single_failed_fetch_as_durable_gate.md) — the durable-gate failure mode this item exposed.
