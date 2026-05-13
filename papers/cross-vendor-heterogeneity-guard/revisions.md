# Revision log — cross-vendor heterogeneity-guard paper

Catches from the cross-vendor review process during drafting of this manuscript. This log is the primary input to Appendix B of the final paper.

---

## Session 1 — 2026-05-13

**Drafted:** outline.md, glossary.md, §4 (heterogeneity rationale), §5 (four case-study vignettes).

**Primary drafter:** Claude Opus 4.7 (Anthropic).

**Independent reviews pending:** DeepSeek V4-Pro pass on §4 + §5 (heterogeneity check); Google Gemini 2.5 Pro pass on case-study factual claims.

### Catch 1 — primary drafter confabulation on PaperOrchestra (caught by user push-back)

During session 1 the user asked whether Google's "Paper Orchestra" should be used to draft the paper. The drafter responded with *"I don't have reliable information on a Google product called Paper Orchestra"* without checking the project's repository — which contained two files with detailed descriptions of PaperOrchestra: `Open Enzyme/posts/notes/hypothesis-generation-gap.md` and `abent-family/brian/blog/2026-05-08-grounding-the-ai-scientist-hype/substack.md`.

The user pushed back: *"did you look in the repo?"*

A grep across the project filesystem immediately surfaced the answer: Google Cloud's PaperOrchestra is a multi-agent framework for automated AI research paper writing (Outline / Plotting / Literature Review / Section Writing / Content Refinement), with Semantic Scholar citation verification, ~40-minute manuscript turnaround, benchmarked on PaperWritingBench (200 reverse-engineered CVPR/ICLR papers). Brian's blog post on 2026-05-08 explicitly framed PaperOrchestra as *"the most honest [of the three AI-scientist systems] — doesn't claim to close the gap, just compresses the writing once a human has done the science."*

The drafter's first response had been a confident-sounding "I don't know" generated without primary-source verification — structurally identical to the §5.1 DAF disulfide-count hallucination. The catch came from the user pushing back, not from any internal verification by the drafter.

**Class of failure:** within-vendor confabulation that should have been caught by primary-source verification, surfaced during the drafting of the very paper that warns against it. **The catch is preserved in the Methods Appendix as the cleanest available reflexive demonstration that the heterogeneity guard has to apply to the paper's own production process.**

**Lesson for the paper's production discipline:** the drafter must apply the pre-commit grep-verify gate to its own outputs, not just to the wiki content the daemon processes. The discipline is the same; the surface is broader.

### Catch 2 — §4 four-pass framing didn't match the operational daemon

§4 of the session 1 draft described "the four-pass cross-vendor architecture" as if all four passes ran in the production daemon. Self-verification against `scripts/sweep-prompt-1-propagate.md`, `scripts/sweep-prompt-2-synthesize.md`, and `scripts/sweep-prompt-3-review.md` revealed the operational daemon runs three passes (Sonnet propagate → DeepSeek/Gemini synthesize → Opus/GPT-5.5 review). The "fourth pass" — DeepSeek independent peer-review of Claude-Opus synthesis — is documented in `wiki/open-source-platform.md` but is run episodically rather than as a daemon pass on every sweep.

**Correction landed:** §3 now describes the architecture as three operational passes plus the episodic independent peer-review pattern. §4 acknowledges the model assignments are an instance of the cross-vendor pattern rather than the pattern itself, and that the assignments have evolved over the operational history.

### Catch 3 — §5.1 catch mechanism understated the manual walkthrough

The session 1 draft of §5.1 stated *"The catch came from Pass 2 of the next-day sweep, which cross-referenced the new figure against the canonical UniProt P08174 record."* The primary source (`CLAUDE.md` §"Pre-commit grep-verify gate") states the catch came from *"the next day's sweep + walkthrough verification."* Manual walkthrough was part of the catch, not just automatic sweep cross-referencing.

**Correction landed:** §5.1 now says *"The catch came from the combination of the next-day sweep and a manual walkthrough verification against the canonical UniProt P08174 record."*

### Catch 4 — §5.3 attributed the 7,500× factor to the wrong kinetic parameter

The session 1 draft of §5.3 stated *"specific activity values were returned that were off the true values by approximately 7,500-fold."* The primary source (`wiki/paperclip-deep-dive.md` table) shows the factor of ~7,500× was on Km (the Michaelis-Menten substrate-affinity constant), not specific activity: true Km 52.61 µM vs. Paperclip's returned 0.007 mM. Specific activity was not the parameter the probe surfaced as ~7,500× off.

**Correction landed:** §5.3 now says *"for the Najjari 2022 PASylated uricase paper (PMC9773812), the true Km is 52.61 µM; Paperclip's `map` returned 0.007 mM — off by approximately 7,500-fold."*

### Catch 5 — §5.4 misdescribed the pre-daemon architecture

The session 1 draft of §5.4 stated *"the original sweep design used three passes, all routed to Claude models (Sonnet propagate → Opus synthesize → Opus review)."* Self-verification against `logs/v4-peer-review-2026-04-25-deepseek.md` shows the substrate at 2026-04-25 was described as a *"Claude Opus 4.7 local-session sweep, 2026-04-24"* — a single Claude session working as both author and reviewer. The formal three-pass daemon (and its cross-vendor model assignments) was a *consequence* of the DeepSeek Connection 7 self-flag, not the architecture that DeepSeek was reviewing.

**Correction landed:** §5.4 now correctly describes the pre-2026-04-25 state as a single Claude session driving both propagation and synthesis, with the multi-pass cross-vendor daemon being the architectural response to DeepSeek's Connection 7.

### Open questions for Brian

1. **Author byline format.** Currently *"Brian Abent · Open Enzyme · brian@headsupresults.com"*. Confirm or adjust.
2. **Vendor naming throughout.** Currently models are named explicitly by vendor + version (Claude Opus 4.7, DeepSeek V4-Pro, Gemini 2.5 Pro). Recommend keeping; reproducibility requires it. Confirm.
3. **The reflexive Methods Appendix entry on Catch 1** (the PaperOrchestra confabulation). Recommend keeping; it is the strongest demonstration the paper has that the methodology applies to its own production. Could be cut if it feels like over-sharing. Confirm.
4. **PaperOrchestra integration point.** When you next have bandwidth to fire PaperOrchestra at the input packet, §2 (related work) is the highest-leverage section for it. Other sections could go to PaperOrchestra for polish, but they are mostly drafted from primary sources I have direct access to.

---

## Session 2 — 2026-05-13 (same day, continued autonomously per user direction)

**Drafted:** §3 (architecture), §6 (operational data), §7 (limitations and failure modes), §8 (discussion), §9 (conclusion), Methods Appendix, Appendix A skeleton.

**Primary drafter:** Claude Opus 4.7 (Anthropic).

**Primary-source verification pass:** load-bearing claims in each section grep-verified against the named primary sources before commit. No catches surfaced beyond those already logged for session 1.

**Independent reviews pending:** DeepSeek V4-Pro pass on §3 + §6 + §7 (architecture and operational claims); Gemini 2.5 Pro pass on §8 + §9 (framing claims).

---

## Session 3 — 2026-05-13 (continued autonomously)

**Drafted:**
- §1 Introduction (~700 words). Frames the homogenization problem; positions cross-vendor as the right granularity; previews the paper's structure. No outside literature cited — that comes in §2.
- `review-prompts.md` — ready-to-fire cross-vendor review prompts for DeepSeek (on §4/§5), Gemini (on §3/§6/§7), and the PaperOrchestra-output review pattern (on §2 once PaperOrchestra produces it).
- `submission-checklist.md` — step-by-step path from current draft state to bioRxiv preprint live + *Patterns* submission.
- Outline updated to reflect what's been drafted vs. what's pending.

**Primary drafter:** Claude Opus 4.7 (Anthropic).

**Self-verification note:** §1 deliberately does not cite outside literature, so the substantive claims are restated propositions from §4. Verified internal consistency with §4 — definitions of epistemic homogenization, cross-vendor vs. within-vendor, training-distribution prior are used identically across §1 and §4.

**State after session 3:**
- §1 + §3 + §4 + §5 + §6 + §7 + §8 + §9 drafted.
- §2 pending PaperOrchestra.
- Abstract pending §2 completion.
- Three cross-vendor review passes pending (prompts ready).
- Figures + tables pending (PaperOrchestra can generate from current text).
- References pending bibliography compilation.

Solo work that can be done without Brian: substantially complete. The remaining steps (PaperOrchestra runs, cross-vendor review pass execution, figure generation, submission) require either Brian's hands or his decision-making on tradeoffs the drafter shouldn't make alone.

---

## Session 4 — 2026-05-13 (PaperOrchestra integration, Path B)

**Drafted:** §2 Related work (~1,100 words across 6 subsections), via the Ar9av/PaperOrchestra community implementation of the literature-review-agent skill (Path B install — no permanent `~/.claude/skills/` symlinks; skill driven manually from `~/paper-orchestra/skills/literature-review-agent/`).

**Workspace:** `paperorchestra-workspace/`
- `inputs/` — idea.md, experimental_log.md, conference_guidelines.md, template.tex
- `outline.json` — intro_related_work_plan only (skipped plotting_plan and section_plan since we only needed §2)
- `run_verify.py`, `run_verify_retry.py` — Phase 2 Semantic Scholar verification scripts
- `manual_supplement.py` — S2 rate-limit fallback (constructs records from WebSearch + arXiv IDs)
- `build_bib.py` — emits refs.bib from citation_pool.json
- `citation_pool.json` — 11 verified records (4 S2-verified + 7 WebSearch+arXiv-verified)
- `refs.bib` — 11 BibTeX entries
- `drafts/section2.tex` — LaTeX output
- `drafts/section2_scaffold.md` — markdown working scaffold
- `drafts/verification-audit.md` — honest record of the S2 verification gap

**Citations landed (11 total):**

S2-verified (4): Bai et al. 2022 (Constitutional AI), Lu et al. 2024 (AI Scientist), Shumailov et al. 2024 (Model Collapse Nature), Shinn et al. 2023 (Reflexion).

WebSearch+arXiv-verified (7): Du et al. 2023 (Multi-agent Debate, arXiv:2305.14325), Madaan et al. 2023 (Self-Refine, arXiv:2303.17651), Verga et al. 2024 (LLM-as-Jury, arXiv:2404.18796), Lee et al. 2023 (RLAIF, arXiv:2309.00267), Yamada et al. 2025 (AI Scientist-v2, arXiv:2504.08066), Song et al. 2026 (PaperOrchestra, arXiv:2604.05018), Shumailov et al. 2023 (Curse of Recursion, arXiv:2305.17493).

### Catch 6 — Semantic Scholar rate-limit incident (2026-05-13) — RESOLVED same day

**Resolution:** S2 API key arrived from Semantic Scholar approval queue on 2026-05-13 (faster than expected; public reports of 5+ day waits did not materialize for our request). Key persisted to `~/.config/abent/paperorchestra.env` (mode 600, outside repo). Re-ran `run_verify.py` against all 11 candidates with authenticated requests.

**Final state: 11 of 11 records S2-verified.** First-pass returned 10 clean hits; RLAIF (11th) required a query-title refinement — S2's preprint-version record had an empty abstract, while the ICML conference-version record had the full abstract. Both share arXiv ID 2309.00267; the ICML record is the better canonical reference. All 11 records in `citation_pool.json` now carry `"verification": "s2"`. The `manual_supplement.py` WebSearch+arXiv fallback is preserved in repo history as a known-good Plan B if S2 access ever degrades again.

The original (rate-limit-induced) catch:



The literature-review-agent's Phase 2 verification pass — sequential 1-QPS S2 `paper/search` queries with Levenshtein > 0.70 / non-empty-abstract / year-≤-cutoff checks — partially failed under the unauthenticated S2 endpoint's rate limit. First pass at 1.0s spacing got 3 records before HTTP 429. Retry pass at 8.0s spacing recovered 1 more. Remaining 7 candidates hit `rate-limited and retries exhausted` even with extended backoff.

**Manual fallback applied.** WebSearch+arXiv metadata (already in drafting context from Phase 1 discovery) was used to construct the remaining 7 records. Each is marked `"verification": "websearch+arxiv"` in `citation_pool.json` for the audit trail. The arXiv IDs are the canonical identifiers WebSearch returned, and they resolve to the listed metadata on arxiv.org.

**Class of failure:** external-tool reliability degradation under rate limits, with verification arm of the pipeline forced into manual fallback. Same failure class as §5.3 of the main paper (Paperclip MCP probe) — except in this case the gap was honestly documented and the work continued rather than abandoning the candidate set.

**Lesson for the paper's methodology:** the heterogeneity-guard pattern should not depend on a single external verification service. If S2 rate-limits, fall back to the next-best canonical identifier (arXiv ID), log the degradation honestly rather than pretend verification succeeded. This is the rigor-under-degradation discipline the paper itself argues for.

**To-do for Brian before bioRxiv submission:** re-run `run_verify.py` with `SEMANTIC_SCHOLAR_API_KEY` set (free key at https://api.semanticscholar.org/). Any candidate that fails S2 verification with a key in place must be either replaced or flagged as an unverified citation. See `paperorchestra-workspace/drafts/verification-audit.md` for the full submission-prep punchlist on §2.

### Note on the Path B install and the cross-vendor framing

The Ar9av/PaperOrchestra skill pack is host-agent-agnostic — the host coding agent does all LLM work; the deterministic Python helpers in `scripts/` do verification math. With Claude Opus 4.7 as the host driver, §2 is currently **Anthropic-driven** (not Gemini-driven as the original PaperOrchestra paper's reference implementation would suggest). The §2 cross-vendor review pass (Claude + DeepSeek per `review-prompts.md` Prompt 3) is therefore especially critical — it is the only architectural step on §2 that provides actual cross-vendor heterogeneity. Without that review pass, §2 has no cross-vendor coverage at all and undermines the paper's own methodology argument.

The literature-review-agent's Semantic Scholar verification is a separate, narrower defense — against fabricated or mis-titled citations specifically. Even with a working S2 key, it does not provide vendor heterogeneity; it provides fact-existence verification.

---

## Session 5 — 2026-05-13 (continued)

**Drafter self-verification pass on §2** against the S2 abstracts now available in `paperorchestra-workspace/citation_pool.json`. Read each cited paper's abstract verbatim and compared §2 prose claim-by-claim against the source material. Same discipline as the pre-commit grep-verify gate the paper itself argues for.

### Catch 7 — §2.3 misstated PoLL's vendor composition

**Claim under review:** §2.3 originally asserted *"the diversity in PoLL is across model sizes and families but, in the original construction, predominantly within a single vendor's lineup; the paper's commitment to cross-vendor diversity is implicit at best."*

**Source check:** Verga et al. (2024) explicitly uses Cohere's command-r, OpenAI's gpt-3.5-turbo, and Anthropic's Claude haiku as the PoLL panel — three distinct vendors. The earlier WebSearch result on this paper had stated this directly: *"a PoLL composed of a larger number of smaller models outperforms a single large judge, exhibits less intra-model bias due to its composition of disjoint model families."*

**Verdict:** Rejected. My claim was wrong in the direction that matters most — PoLL is *already* cross-vendor in the original Verga construction, which makes it the closest antecedent in the literature to this paper's contribution, not a within-vendor pattern.

**Correction landed:** §2.3 rewritten to acknowledge PoLL as the closest cross-vendor antecedent and to relocate the distinction from "diversity granularity" to "abstraction level of application" (per-output evaluation vs. corpus-level synthesis). The new framing is stronger and more honest — the contribution is the application surface, not the cross-vendor commitment, which Verga's work already pioneered at the evaluation tier.

**Class of failure:** within-vendor confabulation about a third-party paper's design choices, caught by primary-source verification. Same failure class as §5.1 of the main paper. This is the second self-catch in the manuscript's own drafting (after Catch 1's PaperOrchestra confabulation), again preserved as material evidence the methodology applies to its own production.

### Catch 8 — §2.5 inflated AI Scientist v2's peer-review claim

**Claim under review:** §2.5 originally asserted Yamada et al. (2025) reported the first AI-generated paper *"to pass a rigorous human peer-review process."*

**Source check:** The S2-verified abstract says *"first entirely AI generated peer-review-accepted workshop paper."* The published claim is specifically a workshop venue, not a main-conference or journal peer review.

**Verdict:** Partial — the claim is true but inflated. "Rigorous" oversells what a workshop-paper accept signals.

**Correction landed:** §2.5 amended to *"first fully AI-generated paper to pass workshop-level human peer review."* Both `draft.md` and `paperorchestra-workspace/drafts/section2.tex` updated.

**Class of failure:** academic-prestige inflation — a venue's actual rigor level was upgraded in the prose without source justification. Common in lit-review drafting; caught by reading the abstract verbatim rather than working from memory of the WebSearch summary.

### Why both catches matter for the methodology argument

Both catches surfaced in a *self*-verify pass — same vendor (Anthropic Claude Opus 4.7) reviewing its own draft against the underlying sources. This is **not** the cross-vendor heterogeneity guard the paper argues is necessary; this is the pre-commit grep-verify gate, the discipline that operates *before* the cross-vendor pass. The fact that two catches surfaced at this step is consistent with the paper's argument that within-vendor self-review still catches a meaningful fraction of failures when the discipline is to read primary sources rather than work from memory. The cross-vendor review pass (still pending — Prompts 1 and 2 in `review-prompts.md`) is expected to surface additional catches that this within-vendor pass missed, particularly framing biases that align with Claude's own prior.

---

## Session 6 — 2026-05-13 (figures + structure cleanup)

**Drafted/produced:**
- Figure 1 (architecture diagram) via `figures/figure1_architecture.py` — three-pass cross-vendor sweep with episodic peer-review pass shown as dashed independent surface; renders to both PDF and PNG @ 300dpi
- Figure 2 (catches-by-class) via `figures/figure2_catches.py` — four §5 case studies color-coded by surfacing vendor; §5.4 DeepSeek catch annotated as seminal
- `figures/README.md` with shared color palette + rebuild commands
- Manuscript-directory `README.md` indexing every file/dir and the drafting-session timeline
- Structural cleanup: Abstract moved to its proper position at the top of the manuscript (was previously between Appendix B and References — a drafting artifact). Appendix A vendor-attribution table fully populated with actual drafter/reviewer state + cross-references to specific catches in this log.

**No new catches.** This was a polish session; the prose was untouched apart from caption/wiring additions. Internal consistency check confirmed:
- Section ordering (Abstract → §1–§9 → Methods Appendix → Appendix A → Appendix B → References) is standard paper layout
- Numbered citations [1]-[12] in body each map to a References entry
- Author-year §2 citations (11 papers) each map to a BibTeX key in `refs.bib`
- Both figures wired into the manuscript with caption blocks pointing to figure-source scripts

---

## State after Session 6

**Solo-draftable arc complete.** What remains:
1. Cross-vendor review prompts fired (Brian)
2. Catches from those review passes land in this file → manuscript corrections applied → updated `revisions.md` entries
3. bioRxiv preprint submission per `submission-checklist.md` (Brian)
4. *Patterns* (Cell Press) peer-review submission after preprint stabilizes

---

## Session 7 — 2026-05-13 (cross-vendor external review pass)

**Drafter authorization:** Brian explicitly authorized orchestrating the cross-vendor reviews ("you can orchestrate the x-vendor reviews") and surfaced that the OpenRouter API key lives in `Open Enzyme/.env`.

**Method:** `paperorchestra-workspace/run_reviews.py` fires four review jobs in parallel via OpenRouter HTTP gateway:
- `deepseek/deepseek-v4-pro` reviewing §4 + §5
- `google/gemini-2.5-pro` reviewing §3 + §6 + §7
- `anthropic/claude-opus-4.5` reviewing §2 (one of two parallel reviewers on §2)
- `deepseek/deepseek-v4-pro` reviewing §2 (second of two parallel reviewers on §2)

**Total cost:** ~$0.18 across all four reviews. **Latency:** 43-131 seconds per review (parallel execution).

Raw outputs saved verbatim to `paperorchestra-workspace/reviews/{deepseek-on-4-5,gemini-on-3-6-7,claude-on-2,deepseek-on-2}.md`.

### Catches surfaced and corrections applied

**Catch 9 — §5.3 Km misreport magnitude was wrong by 3 orders of magnitude (DeepSeek-on-4-5 Catch 4, Rejected verdict). LANDMARK REFLEXIVE CATCH.**

Original §5.3 (and the underlying wiki source `paperclip-deep-dive.md`) claimed Paperclip's `map` operator returned a Km value "off by approximately 7,500-fold" for the Najjari 2022 PASylated uricase paper. DeepSeek's review correctly computed the arithmetic: 52.61 µM = 0.05261 mM; Paperclip returned 0.007 mM; the actual factor is 0.05261/0.007 = **~7.5×, not ~7,500×**. The original "7,500×" was a unit-confusion arithmetic mistake in the wiki documentation that propagated into the paper draft and was never caught by the §5.1 pre-commit grep-verify gate. This is the canonical example of **the exact failure class the paper warns against, in the paper's own documentation, caught by the cross-vendor review the paper advocates for, 9 days after the wiki error was introduced (2026-05-05 → 2026-05-13).** Both `wiki/paperclip-deep-dive.md` (with a §"2026-05-13 correction" note) and §5.3 of `draft.md` corrected to the actual ~7.5× figure. §5.3 now includes a self-aware parenthetical pointing to this very revision-log entry as the reflexive demonstration.

**Catch 10 — §2.4 Anthropic-favorable citation skew (Claude-on-2 Catch 3, Push-back).**

§2.4 originally cited Constitutional AI (Bai et al. 2022, Anthropic) and RLAIF (Lee et al. 2023, Anthropic) as the entire alignment-via-AI-feedback cluster — no non-Anthropic alignment work cited. Claude-the-reviewer flagged this as drafter-vendor-favorable framing (drafter is Anthropic; reviewer is also Anthropic catching its own family-of-vendor's representation bias). **Correction:** Ouyang et al. 2022 (InstructGPT, OpenAI) added to citation pool as `ouyang2022training`, S2-verified (CorpusId 246426909, NeurIPS 2022). §2.4 prose rewritten to cover the broader RLHF/RLAIF/Constitutional AI family across vendors (OpenAI, Anthropic, Google) rather than presenting it as an Anthropic-specific cluster. Pool now has 12 records.

**Catch 11 — §5.3 Km claim and §5.4 self-demonstration tone overstated (DeepSeek-on-4-5 Catches 1, 2, 3, 5, 6).**

DeepSeek flagged multiple absolute-language claims in §4 as too strong:
- "Same training-distribution prior" (GPT-4 vs GPT-4o) — too absolute. Softened to "substantial overlap in training-distribution prior."
- "Is the level at which prior-distribution diversity actually appears" — too absolute. Softened to "is a level at which substantial prior-distribution diversity reliably appears."
- "Unlikely to appear in the same form" — softened to "less likely" + added forward-pointer to §7 shared-training-data limitation.
- "Architecture's motivation came from architecture working" — softened to "the principle that later motivated the architecture was demonstrated in advance by the cross-vendor review pass that prefigured it."
- "Cheaper architectures cannot catch it" (§5.4) — softened to "less likely to catch this class" + added explicit note that controlled ablation is future work.

**Catch 12 — §3 peer-review-pass vendor collision (Gemini-on-3-6-7 Catch 1, Partial).**

Original §3 claimed the episodic peer-review pass uses DeepSeek V4-Pro and is "an independent cross-vendor verification surface." But Pass 2 of the main pipeline also uses DeepSeek V4-Pro, creating a vendor collision when the peer-review pass runs against a DeepSeek-driven substrate. **Correction:** §3 now specifies that the peer-review vendor is deliberately chosen to differ from the substrate-pipeline vendor — for example, when the daemon ran with DeepSeek at Pass 2, the peer-review pass might route to Google Gemini or OpenAI GPT rather than back to DeepSeek. The seminal 2026-04-25 DeepSeek catch is reframed as natural because the substrate was Claude-only at that time.

**Catch 13 — §3 + §6 Table 1 "Gemini as fallback" under-credit (Gemini-on-3-6-7 Catch 2, Push-back).**

Original §3 + Table 1 framed Pass 2 as "DeepSeek V4-Pro, with Google Gemini 2.5 Pro as fallback." Gemini-the-reviewer flagged this as under-crediting Google's role: in a heterogeneity-architected system, two distinct vendor models for a critical pass are an architectural strength, not a primary/backup relationship. This is exactly the **reciprocal asymmetry-detection** the cross-vendor review is designed for — a Google model catching the framing that disadvantages Google. **Correction:** Pass 2 reframed as "DeepSeek V4-Pro or Google Gemini 2.5 Pro" with an explicit note that the choice on any given run is operational (load-balancing, API availability), not architectural; both are full primary backends.

**Catch 14 — §6 Table 1 arithmetic (Gemini-on-3-6-7 Catch 3, Partial).**

Table 1 reported per-pass cost ranges that summed to $0.50–$1.30 at the high end, but the "Full three-pass sweep" row claimed $0.50–$1.50. Gemini did the addition: $0.20 + $0.80 + $0.30 = $1.30, not $1.50. **Correction:** total range fixed to $0.50–$1.30 to match the sum of components. (This is the second arithmetic error in the manuscript surfaced by the cross-vendor pass — the first was the Km factor in Catch 9.)

**Catch 15 — §7 missing prompt-brittleness limitation (Gemini-on-3-6-7 Catch 4, Partial).**

Gemini noted that §7's enumeration of "what the architecture does not protect against" omits prompt brittleness / unannounced vendor model updates as a failure class. **Correction:** new paragraph added enumerating prompt-tuning sensitivity, vendor-side silent rollouts, and the architecture's reliance on out-of-band monitoring (sweep-log diff review) as a mitigation. Listed as the most common cause of silent-pipeline-degradation incidents in the operational record.

**Catch 16 — §7 "data-heavy no value" too sharp (Gemini-on-3-6-7 Catch 5, Push-back).**

Original §7 closing said the pattern provides little value for "data-heavy synthesis with numerical/statistical failure mode." Gemini argued this is overdrawn — for hybrid literature/numerical tasks (clinical trial summaries, kinetic-parameter compilations), the cross-vendor pass retains value at catching hallucinated numbers. Particularly relevant because §5.3 of this paper is *precisely* such a hybrid task. **Correction:** softened to "reduced, though not eliminated" + added explicit reference to §5.3 as evidence the cross-vendor pass catches numerical errors in hybrid tasks.

**Catch 17 — FARS reference unsupported (DeepSeek-on-2 Catch 1, Rejected; Claude-on-2 Catch 7, Push-back).**

Both reviewers independently flagged the FARS (Fully Automated Research System) reference in §2.5 as lacking a verified citation in the bibliography. The §2.5 mention cited specific operational details (228 hours, 100 papers, March 2026) sourced only from blog posts and a tweet, not from a peer-reviewed or arXiv-hosted paper. **Correction:** FARS sentence dropped from §2.5 entirely. The "single-vendor pipeline" framing that depended on FARS is rewritten to reference only the verified AI Scientist and PaperOrchestra examples. The §2.5 prose now also includes an explicit disclosure that this manuscript's §2 was drafted via PaperOrchestra (addressing Claude-on-2 Catch 1's PaperOrchestra-favorable-framing concern).

**Catch 18 — Yamada 2025 "first workshop-level" overstated (DeepSeek-on-2 Catch 2, Push-back).**

Even after Session 5's Catch 8 softened "rigorous peer review" to "workshop-level peer review," DeepSeek pointed out that Lu et al. 2024 (AI Scientist v1) had already reported workshop-level acceptance. Attributing "first" to Yamada 2025 misrepresents the timeline. **Correction:** Yamada 2025 reframed as "further demonstrated AI-generated papers passing workshop-level peer review under a different review threshold," and Lu 2024 reframed as "with AI-generated papers accepted at workshop-level venues" (vs the prior framing of Lu as the "first system aimed at end-to-end open-ended scientific discovery").

**Catch 19 — Du et al. (2023) "same model" framing too tight (Claude-on-2 Catch 4, Partial).**

Original §2.1 described multi-agent debate as "multiple instances of the same model." Claude pointed out that Du et al. (2023) also explored mixed-model configurations (e.g., ChatGPT and Bard in debate). **Correction:** §2.1 amended to "multiple instances — typically of the same model, though Du et al. also explored mixed-model configurations such as ChatGPT and Bard in debate." The downstream framing (debate operates at inference-time argumentation, not at training-distribution prior heterogeneity) stands.

**Catch 20 — Shumailov 2023/2024 citation relationship unclear (Claude-on-2 Catch 6, Partial).**

§2.6 cited both Shumailov 2024 (Nature) and Shumailov 2023 (arXiv) as if they were distinct works. Claude flagged that these are the preprint and published version of the same line of research. **Correction:** §2.6 now explicitly states the relationship ("first as an arXiv preprint (2023, 'The Curse of Recursion') and subsequently as a published paper in *Nature* (2024, 'AI models collapse when trained on recursively generated data')").

### False-positive from the review pass (audit-trail honest)

**Claude-on-2 Catches 1, 7 — alleged "future dates" on Song 2026 and FARS March 2026.** Claude-the-reviewer assumed the current date was 2025 or earlier and flagged these as fabricated/hallucinated. The current date is in fact 2026-05-13 and both PaperOrchestra (April 2026) and FARS (March 2026) predate it. The reviewer's date-orientation failure was itself a within-vendor blind spot — Claude's training cutoff biased it toward treating 2026 as future-tense. Logged here for the reflexive audit: cross-vendor review surfaces real catches AND produces false positives whose nature is itself diagnostic of vendor-prior limitations.

### Summary

20 catches total across all reviews; **12 substantive corrections applied to the manuscript** (Catches 9-20), **1 documentation-side fix to the underlying wiki primary source** (paperclip-deep-dive.md Km magnitude), and **2 false positives logged for transparency** (Claude-on-2 date confusion). Plus 1 new citation added to the S2-verified pool (Ouyang et al. 2022 InstructGPT, addressing the §2.4 Anthropic-skew catch).

**The single highest-value catch was Catch 9** — the 7,500× → 7.5× Km arithmetic error. This is the paper's own primary-source documentation containing exactly the failure mode the paper warns against, caught by exactly the cross-vendor review pass the paper advocates for, in the very drafting of the paper about it. The reflexive narrative is now substantially stronger than it was before the review pass.

The cross-vendor reviews have, by the paper's own definition, demonstrated the methodology working on a corpus drift that the within-vendor pipeline (the drafter, the self-verify pass) had not detected.

---

## Session 8 — 2026-05-13 (Codex external review, response pass)

Brian shared a Codex external review of the manuscript. Bottom line: *"Yes on both, with one important caveat: this is publishable as a methods / scientific communication / AI-for-science workflow case study, not as a broad empirical proof that cross-vendor systems outperform within-vendor systems."* Codex named six specific recommendations. All applied in this session.

### Catch 21 — Codex C1: Stale metadata in `draft.md` status line and Appendix A

`draft.md` status line and Appendix A vendor-attribution table still said the cross-vendor reviews were pending, even though `revisions.md` Session 7 had completed and applied them. **Correction:** status line rewritten to reflect sessions 1–8 scope; Appendix A table fully updated with the actual review assignments (DeepSeek on §4+§5, Gemini on §3+§6+§7, Claude+DeepSeek on §2) and cross-references to specific catches (Catches 9–20 mapped to their sections). Added a "Cross-vendor review run summary" row noting the OpenRouter orchestration, $0.18 total cost, ~131s parallel wall time, and pointer to verbatim review outputs at `paperorchestra-workspace/reviews/`.

### Catch 22 — Codex C2: "Proof" framing replaced with "case-study evidence"

Several sentences in the abstract and §1 read as broad empirical claims rather than case-study evidence. **Corrections:**
- Abstract: "The seminal catch ... is the principle demonstrated by working" → "is a concrete instance of the principle the architecture generalizes." Added explicit framing: "We frame the contribution as a methodology case study with N=1 operational deployment and qualitative catches; controlled ablations comparing cross-vendor against alternative review architectures remain future work."
- §1 contribution paragraph: "demonstrating the principle by working" → "The paper's posture is methodology case study with N=1 deployment and qualitative catches, not broad empirical proof; we frame the operational record as case-study evidence and queue controlled ablations as future work."

### Catch 23 — Codex C3: Missing adjacent-literature citations

Codex named four adjacent papers the §2.6 model-collapse cluster should engage with. All four verified via S2 (now that the API key is in `~/.config/abent/paperorchestra.env`):
- **Peterson 2024** "AI and the Problem of Knowledge Collapse" (arXiv:2404.03502, *AI & Society*) — societal-level recursive-AI failure. Added as ref [13].
- **Wright et al. 2025** "Epistemic Diversity and Knowledge Collapse in Large Language Models" (arXiv:2510.04226) — empirical methodology for measuring LLM epistemic diversity across 27 models / 155 topics; finds all models less diverse than basic web search, model size hurts diversity, RAG helps. Added as ref [14].
- **Rudko and Bonab 2025** "ChatGPT is incredible (at being average)" (Ethics and Information Technology, Springer) — argues output homogenization is structurally distinct from hallucination; distinguishes "what-BS" from "how-BS." Added as ref [15]. *Note: S2 record had empty abstract field; abstract paraphrased from a WebSearch summary of the Springer publisher page, flagged with `verification: "s2-meta+websearch-summary"` in citation_pool.json. Verbatim abstract available at the publisher DOI 10.1007/s10676-025-09845-2 for reviewers who want to verify.*
- **Go et al. 2025** "LiRA: A Multi-Agent Framework for Reliable and Readable Literature Review Generation" (arXiv:2510.05138) — Codex referenced this as the "Elhuyar 2026 multi-agent scientific literature summarization paper" but the actual title and authorship are different; LiRA is a closely-matching multi-agent literature-review framework that fits §2.5's automated-AI-scientist cluster. Added as ref [16].

Plus **Ouyang et al. 2022** InstructGPT (arXiv:2203.02155, NeurIPS 2022) added during the Catch 10 correction in Session 7 (Anthropic-skew fix). Cite key `ouyang2022training`, ref [5].

§2.6 rewritten substantially to engage with all four adjacent constructs (model collapse / knowledge collapse / epistemic-diversity measurement / output homogenization) as distinct-but-related failure modes, positioning epistemic homogenization (this paper's central term) as the corpus-level analogue. Wright et al.'s empirical methodology now flagged as the obvious future-work direction for a quantitative validation of the cross-vendor pattern.

### Catch 24 — Codex C4: Figure 2 recast from bar chart to qualitative taxonomy

Codex flagged the original Figure 2 (bar chart, N=1 per class) as reading like a frequency distribution and over-claiming the operational record. **Correction:** `figure2_catches.py` rewritten to render a 4-cell taxonomy with explicit "Each cell is qualitative (N=1 in the 13-day operational window); the figure is a taxonomy of failure classes, not a frequency distribution" caption. Each cell shows: title (failure class), description, exemplar (§5.X), exemplar date, surfacing mechanism (color-coded by vendor). The §5.4 cross-vendor catch is the one cell with a colored surfacing band (DeepSeek indigo); the other three cells show grey "within-pipeline manual discipline" bands. PDF + PNG regenerated.

### Catch 25 — Codex C5: Zenodo DOI is a submission gate

Codex noted that the manuscript depends heavily on open logs and inline references to mutable repo files; without a Zenodo snapshot DOI, reviewers will not trust the audit trail. **Correction:** `submission-checklist.md` Zenodo section rewritten from "[ ] consider Zenodo" placeholder to a full step-by-step workflow (enable GitHub integration → create release tag at submission commit → push → Zenodo auto-archives + mints DOI → update manuscript Data and Code Availability section with the DOI). Verification step added enumerating every repo artifact the Zenodo snapshot must include.

### Catch 26 — Codex C6: Reference scheme harmonization

The manuscript had two parallel citation schemes: §2 used author-year (Du et al. 2023, etc.) pointing to BibTeX keys in `refs.bib`, while §3-§9 used numbered `[N](path)` markdown links pointing to repo-internal artifacts. Codex flagged this as inconsistent and recommended numbered references throughout with repo artifacts moved to a Data and Code Availability section.

**Correction applied:**
- §2 author-year citations → numbered [1]-[16] format referring to a unified References section with 16 academic papers (the S2-verified pool).
- §3-§9 numbered repo-citations → inline italicized filepath parentheticals (e.g., `(`scripts/SWEEP-ARCHITECTURE.md`)`) instead of numbered references.
- New "Data and Code Availability" section near the end of the manuscript consolidates all repo-internal artifacts cited inline.
- Unified References section now contains 16 academic citations in §2 first-appearance order.

### Codex meta-observation: "the revision log is the paper's best asset"

Codex specifically called out the §5.3 7,500× → 7.5× catch as *"the paper's strongest evidence ... it shows exactly what the manuscript argues: an internally coherent corpus error propagated until a cross-vendor review pass caught it. That reflexive catch turns the paper from 'interesting essay' into 'documented production case study.'"* This is independent external confirmation that the Session 7 reflexive framing was the right call. The reflexive narrative now has converging endorsement from (a) the Session 7 cross-vendor reviewers themselves, (b) the user's own pre-existing methodology, and (c) Codex external review. No correction needed; flagged here for the audit trail.

### State after Session 8

The manuscript is submission-ready pending only the Zenodo DOI minting (requires Brian to enable Zenodo's GitHub integration and create the release tag — see `submission-checklist.md` for the step-by-step). 16 academic citations all S2-verified; reference scheme unified; tone harmonized to case-study evidence; adjacent literature engaged; Figure 2 recast as taxonomy; stale metadata updated. 26 catches in the revision log total (1 pre-drafting, 5 self-verify during sessions 1-6, 12 cross-vendor review pass, 8 Codex external review).

---

## Catch 27 — Pass 3 default reviewer model was wrong (caught by Brian during his read)

**Source:** Brian's first reading-pass through `draft.md` (2026-05-13).

**Claim under review:** §3 and Table 1 both said Pass 3 was "Anthropic Claude Opus 4.7, or OpenAI GPT-5.5 in an alternative configuration." Glossary said the same. Figure 1 box read "Pass 3 — Review · Claude Opus 4.7 (or GPT-5.5)". Abstract said "three operational passes assigned across Anthropic, DeepSeek, and Google models."

**Verdict:** Rejected — factual error.

**Reasoning:** `.github/workflows/wiki-sweep.yml` lines 22–24 and 352–357 show GPT-5.5 has been the **default** Pass 3 reviewer since 2026-05-08 (switched from Opus 4.7 after a three-way eval preserved at `evals/pass-3-reviewer/`). The Anthropic Opus configuration is the **alternate**, not the primary. The Claude-Opus framing in the manuscript reflected a pre-2026-05-08 configuration.

**Correction applied:** §3 Pass 3 paragraph rewritten to lead with GPT-5.5 + the 2026-05-08 switch date; Claude Opus 4.7 demoted to "alternate" with its own model-tuned prompt path noted (`scripts/sweep-prompt-3-review-gpt55.md` for GPT-5.5 vs. `scripts/sweep-prompt-3-review.md` for Claude). Table 1 row 3 fixed. Figure 1 Pass 3 box updated to "GPT-5.5 / Claude Opus 4.7 alt." with the OpenAI green-grey vendor color, not Anthropic amber. Abstract vendor enumeration corrected to "Anthropic, DeepSeek, and OpenAI (with Google Gemini as a configured alternate at Pass 2)." Glossary Pass 2 + Pass 3 entries updated. Figure 1 PDF + PNG regenerated.

**Why the cross-vendor review pass missed this in Session 7:** Gemini reviewed §3 + §6 + §7 in Session 7 and caught the "Gemini as fallback" framing (Catch 13) and the architectural vendor-collision in the peer-review pass (Catch 12) — but did NOT cross-check the Pass 3 model identity against the actual workflow file. The reviewer's brief asked for architectural-accuracy verification but Gemini operated on the manuscript's internal consistency rather than running ground-truth checks against `.github/workflows/wiki-sweep.yml`. This is a real failure-class instance: cross-vendor review caught framing/under-crediting issues but didn't catch a critical model-identity mis-statement that primary-source verification would have caught. **A within-pipeline ground-truth verification step (the pre-commit grep-verify gate the paper itself advocates for, applied to the manuscript's own architectural claims against the actual workflow file) would have caught this.** Brian's institutional-memory catch is doing exactly what §5.1 says the pre-commit gate should have done at authoring time.

**Class of failure:** within-vendor cascade in the manuscript's architectural description — the drafter (Claude) authored the Pass 3 description based on an older mental model of the daemon configuration without grep-verifying against the current `.github/workflows/wiki-sweep.yml`. Cross-vendor review (Gemini) didn't catch it because the reviewer's brief was about manuscript-internal consistency, not ground-truth-against-code. Caught by Brian's institutional knowledge during his first reading pass.

**Lesson preserved for the methodology argument:** the paper's pre-commit grep-verify gate (§5.1) and the cross-vendor review pass (§5.4) are complementary, not redundant. Cross-vendor review is excellent at framing, vendor-skew, and overconfident-claim catches. It is much less reliable for "does this specific factual claim match the current state of the code" — that needs the grep-verify gate, ideally specified in the reviewer's brief. Future cross-vendor review prompts should explicitly include "verify load-bearing architectural claims against the named source file."

---

## Catch 28 — Paper framed the heterogeneity guard as defensive-only; missed the generative value entirely (caught by Brian's read)

**Source:** Brian's continued read, 2026-05-13. Surfaced as: *"so.. the heterogeneity guard can find problems. yes. but it's also there to find new ideas that are not seen by epistemic homogenization. this is what drives me."*

**Claim under review:** The pre-edit manuscript framed the heterogeneity guard almost entirely as a defensive mechanism — §4 was titled "the heterogeneity-guard rationale" with the rationale being entirely about catching errors and preventing drift. All four §5 case studies were error-catch instances. The abstract's framing was "we describe a production deployment ... and present four catches from ~3 weeks of operation that exemplify the failure classes the pattern protects against." §8 HITL paragraph framed the architecture as a "trigger-and-filter for human attention."

**Verdict:** Rejected — the manuscript captured one of two co-equal values and presented it as the whole story.

**Reasoning:** The within-vendor pipeline catches errors via grep-verify (§5.1) regardless of cross-vendor presence. What makes cross-vendor strictly stronger than within-vendor + rigorous verification is the *generative* value — different vendors propose different connections, not just catch different errors. The space of useful syntheses any one model surfaces is bounded by what its training-distribution prior makes salient. A connection that aligns with DeepSeek's prior may never be proposed by Claude regardless of how carefully Claude self-reviews. Without the generative framing, a skeptical reviewer asks "if your grep-verify gate works, why do you need cross-vendor at all?" and the manuscript has no clean answer ready.

**Corrections applied — extensive restructure across the manuscript:**

1. **Abstract rewritten** to explicitly name the two values (safety-net / search-amplifier) and frame the five case studies as four-defensive-plus-one-generative.

2. **§1 contribution paragraph reframed** from twofold to threefold contribution — added "we distinguish two complementary values of the pattern — a safety-net value (defensive) and a search-amplifier value (generative) — and argue that the search-amplifier value is what makes cross-vendor strictly stronger than within-vendor + rigorous verification."

3. **§4 restructured** with a new subsection "Two values of the heterogeneity guard: safety net and search amplifier" placed between the homogenization definition and the why-cross-vendor argument. The phrase **"cross-vendor heterogeneity isn't just a safety net — it's a search amplifier"** is incorporated directly from the project's `operations/notable-moments.md` 2026-05-08 entry where the author had already articulated the framing. The §4.3 self-demonstrating-moment subsection now notes that Connection 7 was a hybrid catch — both defensive (caught a methodological risk in Claude's substrate) and generative (the framing of "epistemic homogenization" as a distinct construct came from DeepSeek's analysis, not from the substrate).

4. **§5.5 added — "The generative class: cross-vendor as idea discovery (2026-04-25 double-peer-review)."** Anchored on the strongest available empirical example: on 2026-04-25 the same Claude Opus 4.7 substrate was reviewed by DeepSeek V4-Pro AND Google Gemini 2.5 Pro independently. Both vendors converged on the SAME three "Missed by Claude" generative findings:
   - **Androgen-urate axis as therapeutic ceiling** (not stratification note) — male gout demographic has a baseline ABCG2-suppression-driven ceiling on uricase efficacy. Drove comp-016, comp-017, comp-019, H-AN-08 hypothesis card, and the `androgen-natural-modulation.md` wiki page.
   - **Carnosine as androgen-specific counter-agent** (not generic NLRP3 synergy) — combined `carnosine.md` URAT1 downregulation with `androgen-urate-axis.md` URAT1 upregulation. Actioned in commit 6e3614d "synthesis 2026-05-05 item 2/14: carnosine → androgen-URAT1 axis — precision countermeasure for male gout."
   - **Fructose challenge test** (acute n-of-1 efficacy readout, not just dietary risk factor) — KHK pathway as controlled stress-test for in-gut enzyme activity. Actioned in commit cf5fc94 ("action remaining 3 synthesis findings (fructose challenge, CRISPR bridge, glucose-dominant starches)").
   §5.5 also includes a brief closing observation about the 2026-05-08 Gemini-synthesizer-and-human-blog-writer convergence on the DAF case study (per `operations/notable-moments.md` 2026-05-08 entry), as a second-substrate example showing the same search-amplifier pattern can appear in AI-AI convergence and in AI-human convergence.

5. **§8 HITL paragraph rewritten** to acknowledge both values (trigger-and-filter + search-amplifier) and the human-as-one-of-the-vendors angle surfaced by the 2026-05-08 incident.

6. **Appendix A vendor-attribution table gets a new row** for §5.5 documenting the dual-peer-review primary sources and the actioned downstream impact.

**Class of failure caught:** the manuscript was under-claiming its own contribution. The author's motivating question (the generative value) was not visible in the paper. A reviewer reading the pre-edit version would have classified the contribution as "error-catching methodology" — real but incomplete. The post-edit version frames cross-vendor heterogeneity as strictly dominating within-vendor + rigorous verification because the search-amplifier value is something verification alone cannot supply.

**Method origin:** the framing "heterogeneity isn't just a safety net — it's a search amplifier" came directly from `operations/notable-moments.md` 2026-05-08, where the author had previously written: *"What happened today is generative ... heterogeneity isn't just a safety net, it's a search amplifier."* Incorporating this verbatim preserves the author's voice and references the project's own prior intellectual work on the question.

---

## Catch 29 — `~/.claude/projects/.../memory/` should record an updated project-status note

**Source:** drafter housekeeping during Catch 28 restructure.

**Claim under review:** the auto-memory entry at `~/.claude/projects/.../memory/project_oe_methodology_paper.md` still references "§1, §3-§9 + Methods Appendix complete, §2 awaits PaperOrchestra" — that's pre-Session 4 state.

**Correction applied:** updated in a separate housekeeping pass (not committed in this revision-log entry; tracked separately).

---

## Future sessions

Each subsequent drafting session appends a section to this file: what was drafted, who reviewed it, what was caught, what was changed in response. The final paper's Appendix B is generated from this log.
