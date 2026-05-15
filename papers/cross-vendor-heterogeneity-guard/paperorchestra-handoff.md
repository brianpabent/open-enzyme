# PaperOrchestra handoff packet

Self-contained brief for handing this paper to Google Cloud's PaperOrchestra. Single author (Brian Abent). The work is done; PaperOrchestra's job is the writing-up consolidation, plus authoring §2 related work (the section where outside literature is pulled in).

---

## What kind of paper

**Working title:** *Cross-vendor heterogeneity as a guard against epistemic homogenization in AI-assisted scientific literature synthesis.*

**Type:** Methodology paper. Argues that cross-vendor (different companies' models) heterogeneity is the right granularity for guarding against bias accumulation in long-lived AI-maintained knowledge corpora, distinct from within-vendor multi-model approaches in the existing multi-agent literature. Uses the Open Enzyme wiki-sweep daemon as the worked example, with four concrete catches from the operational record as case studies.

**Author:** Brian Abent (Open Enzyme · brian.abent@gmail.com). Single author.

**Voice:** Academic-formal. Plain prose around precise terms. PhD-level audience but written so a CS-literate non-PhD can follow every substantive claim. Every precise technical term has a parenthetical gloss on first use. Glossary file (`glossary.md`) is the authoritative term list.

**Target venues (in order):**
1. **bioRxiv preprint + arXiv cs.AI cross-post**, immediate, zero gating.
2. ***Patterns*** (Cell Press), primary peer-review target. Methods + data science + biology applications.
3. ***Nature Computational Science***, stretch target.
4. ***PLOS Computational Biology***, open-access fallback.

Target length: ~7,500 words main text + ~2 figures + ~2 tables + supplementary appendices.

---

## What's already drafted (input materials)

In the same directory as this file:

- **`outline.md`**, section-by-section scope, draft order, target venues, effort estimate.
- **`draft.md`**, sections drafted as of 2026-05-13:
  - §3 Architecture (~1,500 words)
  - §4 Heterogeneity-guard rationale (~800 words)
  - §5 Case studies (four ~300-word vignettes, ~1,200 words total)
  - §6 Operational data (~600 words)
  - §7 Limitations and failure modes (~600 words)
  - §8 Discussion (~500 words)
  - §9 Conclusion (~200 words)
  - Methods Appendix on cross-vendor production process used for this manuscript
  - Appendix A skeleton (vendor attribution by section)
- **`glossary.md`**, every precise term in §3–§9 with plain-English glosses. Use this to keep the voice consistent.
- **`revisions.md`**, catches logged during drafting, including a reflexive self-catch (the primary drafter confabulated PaperOrchestra's existence on first ask, caught by user push-back). This is preserved in the Methods Appendix as the cleanest demonstration that the methodology applies to the paper's own production. The reflexive narrative is **central to the paper's argument**; do not strip it.

---

## What PaperOrchestra is being asked to do

### Primary ask: §2 Related work (~1,000 words)

The section that pulls in outside literature. This is the section where PaperOrchestra's Literature Review agent (Semantic Scholar citation verification) and Section Writing agent are most valuable.

**Position the cross-vendor heterogeneity-guard pattern against:**

1. **Multi-agent debate** (Du et al. 2023, "Improving Factuality and Reasoning in Language Models through Multiagent Debate"; subsequent debate-framework papers). Within-vendor, focused on per-task accuracy. Multiple instances of the same model argue toward consensus.
2. **Self-refine / self-critique** (Madaan et al. 2023, "Self-Refine: Iterative Refinement with Self-Feedback"; Shinn et al. 2023, "Reflexion"). Same-model reflection loops; no heterogeneity at all.
3. **LLM-as-jury / panel approaches** (Verga et al. 2024, "Replacing Judges with Juries"). Typically same-vendor across model sizes; no cross-vendor commitment.
4. **Constitutional AI** (Bai et al. 2022, "Constitutional AI: Harmlessness from AI Feedback"). Same-vendor with explicit value alignment.
5. **Classical ensemble methods and mixture-of-experts**. Cross-architecture, but typically within the same training-distribution family. The heterogeneity is at the model-architecture level, not the training-corpus or RLHF-pipeline level.
6. **Recent automated-research systems** (Sakana's "AI Scientist," Analemma's FARS, Google's own PaperOrchestra). End-to-end-aspirational; none of them deploy cross-vendor heterogeneity as an architectural commitment.

**The argument the section needs to make:**
- All prior work in this space operates either within a single vendor (debate, self-refine, jury, Constitutional AI) or at a different abstraction level than vendor (ensembles, MoE).
- The under-explored regime is *cross-vendor* heterogeneity, models trained by different companies, on different data, with different RLHF pipelines.
- This regime is where prior-distribution diversity actually appears, because the relevant variance is in training-distribution prior, not in inference-time stochasticity.
- The paper's contribution is to develop this regime as an explicit architectural pattern and demonstrate it operationally.

Voice: academic-formal, plain prose, no marketing language. Cite via Semantic Scholar verification. Do not over-claim novelty, be precise about what is and is not new (the *pattern* is a special case of ensemble logic; the *application at the vendor level for AI-assisted scientific synthesis* is the novel claim).

### Secondary asks: polish and consolidation

PaperOrchestra is also welcome to:

1. **Draft §1 Introduction (~600 words).** Frame the homogenization problem; survey why this risk worsens as autonomous-research systems scale; preview the architecture and case studies. Should land naturally after §2 is drafted.
2. **Polish §3–§9** for academic-formal voice consistency. Keep claims and citations intact; tighten prose where needed; do not strip the reflexive Methods Appendix narrative. Do not remove the per-section primary-source citations.
3. **Draft the Abstract (~250 words)** after the body is complete.
4. **Compile and format the References bibliography**, including Semantic Scholar verification for every cited paper.
5. **Generate Figure 1 (architecture diagram)** based on the §3 description.
6. **Generate Table 1 (per-pass model assignment + cost + latency)** based on the §6 operational data.
7. **Compose Appendix C (Code and data availability)** with placeholders for the Zenodo DOI to be filled in at submission time.

---

## What PaperOrchestra is **not** being asked to do

1. **Do not rewrite §4 or §5.** These are the conceptual spine and the concrete demonstrations; they have been grep-verified against the primary sources and are the manuscript's spine. Voice consistency tightening is fine; rewriting is not.
2. **Do not strip the reflexive Methods Appendix entry on Catch 1.** This is the paper's strongest argument made by demonstration. The primary drafter (Claude) confabulated PaperOrchestra's existence on first ask; the catch was the user pushing back; the lesson is that the heterogeneity guard has to apply to the paper's own production. Preserve this in full.
3. **Do not make claims about the operational record beyond what is in §6.** The false-positive rate, longitudinal data, etc. are explicitly flagged as future work in §6, do not invent quantitative claims.
4. **Do not collapse the cross-vendor framing to "multi-agent" or "multi-model."** The whole argument of the paper is that those framings are insufficient; mis-framing this in the abstract or introduction would undermine the paper.

---

## Primary sources for §2 grounding (in addition to PaperOrchestra's Semantic Scholar pulls)

External:
- Du, Y. et al. "Improving Factuality and Reasoning in Language Models through Multiagent Debate." 2023.
- Madaan, A. et al. "Self-Refine: Iterative Refinement with Self-Feedback." 2023.
- Shinn, N. et al. "Reflexion: Language Agents with Verbal Reinforcement Learning." 2023.
- Verga, P. et al. "Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models." 2024.
- Bai, Y. et al. "Constitutional AI: Harmlessness from AI Feedback." Anthropic, 2022.
- Sakana AI Scientist papers and subsequent system descriptions.
- Analemma FARS deployment blog post and technical details.
- PaperOrchestra paper / system description (the official write-up of the system being used for this draft).

Internal (for cross-references):
- `wiki/open-source-platform.md` §"Multi-model synthesis as guard against epistemic homogenization", the original wiki statement of the heterogeneity-guard rationale.
- `scripts/SWEEP-ARCHITECTURE.md`, the daemon's engineering doc; primary source for §3 architecture details.
- `scripts/sweep-prompt-1-propagate.md`, `sweep-prompt-2-synthesize.md`, `sweep-prompt-3-review.md`, the operational prompts.
- `logs/v4-peer-review-2026-04-25-deepseek.md`, the seminal DeepSeek peer-review pass; primary source for §5.4.
- `logs/sweep-state.json`, `logs/sweep-log.md`, operational data for §6.
- `CLAUDE.md` §"Pre-commit grep-verify gate", §5.1 catch primary source.
- `wiki/daf-cd55-scr14-truncated-computational.md` §1.5, §5.1 catch correction note.
- `operations/comp-018-vs-comp-020-retrospective.md`, §5.2 catch primary source.
- `wiki/paperclip-deep-dive.md`, §5.3 catch primary source.
- `abent-family/brian/blog/2026-05-08-grounding-the-ai-scientist-hype/substack.md`, author's own analysis of the AI-scientist landscape (citation [12]).

---

## Cross-vendor review of PaperOrchestra's §2 output

Per the paper's own methodology: PaperOrchestra's output on §2 must be independently reviewed by **Anthropic Claude (Opus 4.7)** and **DeepSeek V4-Pro** before it lands in the manuscript. Catches go into `revisions.md`. The reflexive narrative requires this loop, the cross-vendor pattern applied to the section where new outside literature enters the paper.

Specifically, the reviewers should check:

1. **Citation accuracy.** Every cited paper exists, the year is right, the claim attributed to the paper actually appears in the paper. (Semantic Scholar verifies existence; the reviewers verify attribution.)
2. **Framing of prior work.** Each prior approach is described accurately; no straw-manning; no over-claiming the paper's novelty.
3. **The cross-vendor / within-vendor distinction.** The section should not collapse this into a generic "multi-agent" framing. Reviewers should flag any sentence where the distinction is blurred.
4. **Bias toward Anthropic-favorable framing.** If the reviewer is Claude, watch for over-promotion of Anthropic work or under-citation of competing vendors' research. If the reviewer is DeepSeek, watch for the inverse. The heterogeneity guard catches asymmetries in *each* reviewer's prior.

Catches from this review pass land in `revisions.md` under "Session 3, §2 PaperOrchestra draft, cross-vendor review."

---

## Submission process

1. PaperOrchestra produces §2 + polish on §3–§9 + abstract + intro + bibliography + figures + tables.
2. Brian reviews. Glossary check applies to any new precise terms PaperOrchestra introduced.
3. Cross-vendor review pass on §2 specifically (Claude + DeepSeek).
4. Revisions log finalized.
5. Submission package assembled: PDF, LaTeX source, supplementary materials (code + logs + Zenodo DOI for snapshot).
6. **bioRxiv preprint + arXiv cs.AI cross-post first.** Citable artifact lands immediately.
7. Submit to *Patterns* (Cell Press) for peer review.
