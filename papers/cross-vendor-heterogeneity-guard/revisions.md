# Revision log — cross-vendor heterogeneity-guard paper

Catches from the cross-vendor review process during drafting of this manuscript. This log is the load-bearing input to Appendix B of the final paper.

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

**Self-verification note:** §1 deliberately does not cite outside literature, so the load-bearing claims are restated propositions from §4. Verified internal consistency with §4 — definitions of epistemic homogenization, cross-vendor vs. within-vendor, training-distribution prior are used identically across §1 and §4.

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

### Catch 6 — Semantic Scholar rate-limit incident (2026-05-13)

The literature-review-agent's Phase 2 verification pass — sequential 1-QPS S2 `paper/search` queries with Levenshtein > 0.70 / non-empty-abstract / year-≤-cutoff checks — partially failed under the unauthenticated S2 endpoint's rate limit. First pass at 1.0s spacing got 3 records before HTTP 429. Retry pass at 8.0s spacing recovered 1 more. Remaining 7 candidates hit `rate-limited and retries exhausted` even with extended backoff.

**Manual fallback applied.** WebSearch+arXiv metadata (already in drafting context from Phase 1 discovery) was used to construct the remaining 7 records. Each is marked `"verification": "websearch+arxiv"` in `citation_pool.json` for the audit trail. The arXiv IDs are load-bearing — they are the canonical identifiers WebSearch returned, and they resolve to the listed metadata on arxiv.org.

**Class of failure:** external-tool reliability degradation under rate limits, with verification arm of the pipeline forced into manual fallback. Same failure class as §5.3 of the main paper (Paperclip MCP probe) — except in this case the gap was honestly documented and the work continued rather than abandoning the candidate set.

**Lesson for the paper's methodology:** the heterogeneity-guard pattern should not depend on a single external verification service. If S2 rate-limits, fall back to the next-best canonical identifier (arXiv ID), log the degradation honestly rather than pretend verification succeeded. This is the rigor-under-degradation discipline the paper itself argues for.

**To-do for Brian before bioRxiv submission:** re-run `run_verify.py` with `SEMANTIC_SCHOLAR_API_KEY` set (free key at https://api.semanticscholar.org/). Any candidate that fails S2 verification with a key in place must be either replaced or flagged as an unverified citation. See `paperorchestra-workspace/drafts/verification-audit.md` for the full submission-prep punchlist on §2.

### Note on the Path B install and the cross-vendor framing

The Ar9av/PaperOrchestra skill pack is host-agent-agnostic — the host coding agent does all LLM work; the deterministic Python helpers in `scripts/` do verification math. With Claude Opus 4.7 as the host driver, §2 is currently **Anthropic-driven** (not Gemini-driven as the original PaperOrchestra paper's reference implementation would suggest). The §2 cross-vendor review pass (Claude + DeepSeek per `review-prompts.md` Prompt 3) is therefore especially load-bearing — it is the only architectural step on §2 that provides actual cross-vendor heterogeneity. Without that review pass, §2 has no cross-vendor coverage at all and undermines the paper's own methodology argument.

The literature-review-agent's Semantic Scholar verification is a separate, narrower defense — against fabricated or mis-titled citations specifically. Even with a working S2 key, it does not provide vendor heterogeneity; it provides fact-existence verification.

---

## Future sessions

Each subsequent drafting session appends a section to this file: what was drafted, who reviewed it, what was caught, what was changed in response. The final paper's Appendix B is generated from this log.
