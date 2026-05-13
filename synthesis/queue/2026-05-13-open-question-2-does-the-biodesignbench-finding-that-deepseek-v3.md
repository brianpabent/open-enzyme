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
