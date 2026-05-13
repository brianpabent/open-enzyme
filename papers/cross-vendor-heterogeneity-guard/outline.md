# Outline, Cross-vendor heterogeneity guard paper

**Working title:** Cross-vendor heterogeneity as a guard against epistemic homogenization in AI-assisted scientific literature synthesis

**Target venues, in order:**
1. bioRxiv preprint + arXiv cs.AI cross-post (immediate; zero gating)
2. *Patterns* (Cell Press), primary peer-review target
3. *Nature Computational Science*, stretch target
4. *PLOS Computational Biology*, open-access fallback

**Target length:** ~7,500 words main text + ~2 figures + ~2 tables + supplementary appendices

---

## Section-by-section

### Abstract (~250 words), drafted last
- Problem: single-vendor AI-assisted scientific synthesis converges on the synthesizer's biases over time
- Contribution: a four-pass cross-vendor architecture as a heterogeneity guard
- Demonstration: deployed on the Open Enzyme research wiki; logs four representative catches
- Reflexive note: this manuscript was drafted using the methodology it describes

### §1 Introduction (~600 words)
- AI-assisted knowledge graphs are becoming consequential infrastructure in scientific research workflows
- Risk: when one vendor's model is the sole synthesizer, the corpus accumulates that vendor's blind spots and biases
- This risk is structurally different from per-output hallucination, it's distributional drift in the corpus itself
- The paper's claim: cross-*vendor* (not just multi-model) review is the right granularity for the guard
- Roadmap of the paper

### §2 Related work (~1,000 words), biggest new-prose lift
- Multi-agent debate (Du et al. 2023 and follow-ons): within-vendor, focused on per-task accuracy
- Self-refine and self-critique (Madaan et al. 2023; Shinn et al. 2023): same-model reflection
- LLM-as-jury / panel approaches (Verga et al. 2024): typically same-vendor across model sizes
- Constitutional AI (Bai et al. 2022): same-vendor with explicit value alignment
- Ensemble methods in classical ML; mixture-of-experts: cross-architecture, but typically within the same training-distribution family
- The under-explored regime: cross-*vendor* (different companies, different training corpora, different RLHF pipelines)
- What this regime offers that the above miss: heterogeneity at the level of training-distribution prior, not just at the level of inference-time strategy

### §3 Architecture (~1,500 words + figure), ~80% drafted in `scripts/SWEEP-ARCHITECTURE.md`
- The four-pass sweep daemon: Sonnet propagate → Gemini synthesize → Opus critique → DeepSeek peer-review
- OpenRouter routing for vendor abstraction
- Trigger model: GitHub Actions on push to `wiki/*.md`; `[skip-wiki-sweep]` commit marker prevents recursion
- Failure-mode hardening: rebase-before-push race fix, transient API outage retry
- Architecture diagram (Figure 1)

### §4 Heterogeneity-guard rationale (~800 words), ~70% drafted in `wiki/open-source-platform.md`
- Definition: *epistemic homogenization* = convergence of a knowledge corpus on a single synthesizer's prior over time
- Why this is structurally different from per-output hallucination
- Why cross-vendor specifically (vs. multi-model within a vendor)
- The self-demonstrating moment: a different vendor caught this very risk first

### §5 Case studies (~1,200 words; four ~300-word vignettes)
- 5.1 Within-vendor cascade: DAF SCR1-4 disulfide-count hallucination, caught by next-day sweep + UniProt grep-verify
- 5.2 Upstream-of-subagent contamination: comp-018 contrived framing in subagent brief, caught by independent rerun (comp-020)
- 5.3 External-tool reliability test: Paperclip MCP `map` operator hallucination on uricase variant probe
- 5.4 Cross-vendor catches methodological risk: DeepSeek V4-Pro Connection 7 self-flag, the seminal moment that motivated the architecture

### §6 Operational data (~600 words + 2 tables/figures)
- Cost per sweep (OpenRouter pricing data)
- Latency per pass
- Vendor distribution of catches across the sweep history
- False-positive rate estimate (catches that proved spurious on review)
- Table 1: per-pass model assignment + cost + latency
- Figure 2: catches-by-vendor breakdown

### §7 Limitations and failure modes (~600 words)
- Operational failures (rebase race, API outages), what the architecture does NOT protect against
- Shared training-data leakage: vendors share web-crawl corpora; common-cause biases persist
- Cost overhead: four passes vs. one is ~4× the API spend
- Latency overhead: ~9-12 minutes per sweep vs. seconds for a single pass
- Audience scope: when this matters (consequential corpora, regulated domains) and when it doesn't

### §8 Discussion (~500 words)
- How many vendors is enough?
- Does the guard scale to non-text modalities (vision, structure prediction, multi-omics)?
- Implications for autonomous-research systems where AI-assisted synthesis is the critical step
- The reflexive observation: a methodology paper drafted using its own methodology is empirical evidence the methodology works

### §9 Conclusion (~200 words)
- Cross-vendor heterogeneity is a tractable engineering pattern for AI-assisted scientific synthesis
- The Open Enzyme deployment is one instance; the pattern generalizes
- Open code, open logs, open invitation to replicate

### Appendix A, Vendor attribution by section
- Which model drafted, which model reviewed, what catches surfaced

### Appendix B, Revision log
- Catches from the cross-vendor review during drafting of this manuscript

### Appendix C, Code and data availability
- Sweep daemon code repository
- Representative log snapshots
- Zenodo DOI for the submission-time snapshot

### References
- ~30-50 citations. Multi-agent / debate / reflection / ensemble literature is the bulk. Plus Open Enzyme self-citations for the wiki primary sources.

---

## Draft order

1. §4 (heterogeneity rationale), the conceptual spine ✅ Session 1
2. §5 (case studies), the concrete demonstrations ✅ Session 1
3. §3 (architecture), compress from `SWEEP-ARCHITECTURE.md` ✅ Session 2
4. §6 (operational data), extract from logs ✅ Session 2
5. §7, §8, §9 (limitations, discussion, conclusion) ✅ Session 2
6. Methods Appendix + Appendix A skeleton ✅ Session 2
7. §1 (introduction), written after the body has shape ✅ Session 3
8. §2 (related work), drafted via Ar9av/PaperOrchestra literature-review-agent (Path B), 11 S2-verified citations ✅ Sessions 4–5
9. Abstract ✅ Session 5
10. Drafter self-verify on §2 against S2 abstracts (caught 2 framing errors) ✅ Session 5
11. Table 1 (per-pass cost/latency/vendor) ✅ Session 5
12. Glossary additions for §2 terms (RLAIF, PoLL, model collapse) ✅ Session 5
13. Cross-vendor review passes on §3–§9 per `review-prompts.md`, **PENDING** (Brian fires)
14. Cross-vendor review of PaperOrchestra's §2 output, **PENDING** (Brian fires)
15. Figures (Fig 1 architecture diagram, Fig 2 catches-by-class), **PENDING**
16. Final reference compilation + bibliography formatting consistency check, **PENDING**
17. Submission package per `submission-checklist.md`, **PENDING**

**Solo-draftable work effectively complete after Session 6.** The manuscript has Abstract, §1 through §9, Methods Appendix, fully populated Appendix A (vendor attribution), Appendix B placeholder pointing to `revisions.md`, Table 1 (per-pass cost/latency), Figure 1 (architecture), Figure 2 (catches-by-class), and the full §2 with 11 S2-verified citations. Eight catches landed across sessions in `revisions.md` (six during drafting + two from drafter self-verify on §2 against S2 abstracts). Reference completeness audited: numbered citations [1]-[12] in body match the references list; author-year §2 citations match BibTeX keys in `refs.bib`. What remains requires either Brian's hands (cross-vendor external review prompt firings, decisions on byline / reflexive-narrative inclusion, bioRxiv submission) or downstream review-pass catches that have not yet surfaced.
