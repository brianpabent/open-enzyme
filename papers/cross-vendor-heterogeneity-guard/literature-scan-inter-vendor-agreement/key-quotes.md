# Key verbatim quotes from the most relevant papers

Generated 2026-05-14. Each block: paper anchor (arXiv ID + section if available), verbatim quote, and a marker indicating whether the quote was extracted from the paper itself or from a verified abstract / summary.

`[ABSTRACT]` = quote from the paper's abstract on arXiv (high confidence)
`[SUMMARY-EXTRACTED]` = quote extracted via WebFetch from arXiv HTML rendering (high confidence)
`[SEARCH-SUMMARY]` = quote surfaced by web-search summarization of the paper content (medium confidence; should be re-verified against full text before use as load-bearing)
`[UNVERIFIED]` = the claim was not directly grep-confirmable from primary source within this scan; do not cite as load-bearing

---

## Correlated Errors in LLMs (Kim et al. 2025, arXiv:2506.07962, ICML 2025)

> "Models with the same provider (company), with the same base architecture, or with similar sizes have more correlated errors."

`[SUMMARY-EXTRACTED]` — Available via web-search summary of arXiv 2506.07962. Direction of effect confirmed across multiple summarization passes.

> "Larger and more accurate models have highly correlated errors, even with distinct architectures and providers."

`[SUMMARY-EXTRACTED]`

> "Models agree 60% of the time when both models err."

`[SUMMARY-EXTRACTED]` — Quote attributed to "one leaderboard dataset" — specific dataset name not extracted; verify against full PDF before citing as load-bearing.

> "Over 350 LLMs evaluated."

`[SUMMARY-EXTRACTED]` — Sample size confirmed via abstract.

---

## Mixed-Vendor Multi-Agent LLMs (Yuan et al. 2025, arXiv:2603.04421)

> "Mixed-vendor teams successfully pool complementary inductive biases to surface diagnoses that individual models miss."

`[SUMMARY-EXTRACTED]` — From arXiv HTML.

> "Homogeneous teams remain trapped in correlated failure modes that discussion alone cannot resolve."

`[SUMMARY-EXTRACTED]`

> "Performance gains inversely correlate with model similarity — gains peak when models exhibit distinct areas of expertise."

`[SUMMARY-EXTRACTED]`

**Hard numbers (RareBench Recall@1):**
- Mixed-Vendor: **39.31%**
- Best Single-Vendor Multi-Agent Collaboration (MAC): **36.63%** (Gemini)
- Best Single-LLM: **37.58%** (Gemini)

**MME subset (hardest):**
- Mixed-Vendor: **40.00%**
- Gemini Single-LLM: **30.00%**
- Lift: **+10 percentage points**

**Jaccard similarity (vendor output overlap on MME):**
- Range: **0.269 to 0.750**

`[SUMMARY-EXTRACTED]` — All numbers from arXiv HTML extraction. Verify against PDF before citing.

---

## Inter-Model Consensus on PhD-Level Stats (Amiri-Margavi et al. 2025, arXiv:2411.16797)

**Sample size:** **N=100** multiple-choice questions at PhD-level statistics (Bayesian inference, time series, survival analysis).

**Fleiss' Kappa per model (inter-rater agreement on PhD-level stats questions):**
| Model | Kappa | Interpretation |
|---|---|---|
| Claude | **0.7160** | Substantial |
| LLaMA | **0.5572** | Moderate |
| GPT-4 | **0.4275** | Moderate |
| Gemini | **0.2811** | Fair |

**Full-agreement rate when each model generated questions:**
- Claude: **86%** (CI: 0.80–0.93)
- GPT-4: **82%** (CI: 0.75–0.90)
- Gemini: **70%** (CI: 0.60–0.78)
- LLaMA: **65%** (CI: 0.55–0.74)

**Reliability rate (alignment with question-generator's answer):**
- Claude: **92%**
- GPT-4: **90%**
- Gemini: **88%**
- LLaMA: **77%**

`[SUMMARY-EXTRACTED]` — From arXiv 2411.16797v2 HTML. High confidence (multiple summarization passes returned identical numbers).

---

## Replacing Judges with Juries (Verga et al. 2024, arXiv:2404.18796)

> "Using a PoLL composed of a larger number of smaller models outperforms a single large judge while exhibiting less intra-model bias due to its composition of disjoint model families."

`[ABSTRACT]` — Direct quote from arXiv abstract.

> "Operates at over seven times less expensive cost than single large-model judges."

`[ABSTRACT]`

---

## Stop Overvaluing Multi-Agent Debate (Zhang et al. 2025, arXiv:2502.08788)

> "Multi-Agent Debate often fail[s] to outperform simple single-agent baselines such as Chain-of-Thought and Self-Consistency, even when consuming significantly more inference-time computation."

`[ABSTRACT]`

> "Model heterogeneity acts as a universal antidote to consistently improve current MAD frameworks."

`[ABSTRACT]`

> "The field must critically rethink evaluation paradigms and actively embrace model heterogeneity as a core design principle."

`[ABSTRACT]`

**Study scope:** **5 representative MAD methods x 9 benchmarks x 4 foundational models.**

---

## Epistemic Diversity and Knowledge Collapse (Wright et al. 2025, arXiv:2510.04226)

> "Newer models tend to generate more diverse claims, [but] all models are less epistemically diverse than a basic web search."

`[ABSTRACT]`

> "Model size has a negative impact on epistemic diversity, while retrieval-augmented generation (RAG) has a positive impact."

`[ABSTRACT]`

**Study scope:** **27 LLMs x 155 topics (12 countries) x 200 prompt templates.**

---

## Mixture-of-Agents (Wang et al. 2024, arXiv:2406.04692, ICLR 2025 Spotlight)

> "An LLM tends to generate better responses when presented with outputs from other models, even if these other models are less capable by itself."

`[ABSTRACT]` — They name this the "collaborativeness of LLMs."

**Performance:** Open-source MoA scores **65.1%** on AlpacaEval 2.0 vs GPT-4 Omni's **57.5%**.

---

## Chatbot Arena (Chiang et al. 2024, arXiv:2403.04132)

> "Strong LLM judges like GPT-4 can match both controlled and crowdsourced human preferences well, achieving over 80% agreement, the same level of agreement between humans."

`[ABSTRACT]`

> "Expert validation studies indicate 72–83% agreement between crowdsourced Arena votes and Berkeley graduate student fact-checkers; inter-expert agreement is 79–90% on the same prompts."

`[SEARCH-SUMMARY]` — Verify against the full paper before citing as load-bearing.

**Scale:** **240K votes (initial)**, **6M+ votes** (ongoing).

---

## Prompt Sensitivity (Sclar et al. 2023, arXiv:2310.11324, ICLR 2024)

> "Several widely used open-source LLMs are extremely sensitive to subtle changes in prompt formatting in few-shot settings, with performance differences of up to 76 accuracy points when evaluated using LLaMA-2-13B."

`[SEARCH-SUMMARY]`

> "Format performance only weakly correlates between models, which puts into question the methodological validity of comparing models with an arbitrarily chosen, fixed prompt format."

`[SEARCH-SUMMARY]`

---

## BioDesignBench (bioRxiv 2026.05.06.723381)

`[UNVERIFIED]` — bioRxiv PDF returned HTTP 403 on 2026-05-12 and again on 2026-05-14. All claims below sourced from secondary summaries.

> "Agents generally select appropriate tools, but they evaluate candidate designs too shallowly, rarely compare alternatives, and terminate exploration prematurely."

`[UNVERIFIED]`

> "Four frontier LLMs — DeepSeek V3, GPT-5, Claude Sonnet 4.5, and Gemini 2.5 Pro — were evaluated under both unguided and guided modes."

`[UNVERIFIED]`

**Do not cite as primary evidence for cross-vendor disagreement.** The benchmark measures task accuracy, not output agreement. Once PDF is retrieved, re-extract and re-classify.
