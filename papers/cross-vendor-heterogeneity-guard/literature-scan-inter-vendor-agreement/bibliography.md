# Annotated bibliography: inter-vendor LLM agreement / disagreement

Generated 2026-05-14 for the cross-vendor heterogeneity-guard paper.

Each entry: full citation, primary finding, domain, method, N, relevance to our paper.

Relevance scale: **strong** (directly measures cross-vendor output divergence on reasoning), **moderate** (measures cross-vendor performance but not output agreement), **weak** (tangentially related), **tangential** (cited for framing only).

---

## STRONG relevance

### 1. Kim, Garg, Peng, & Garg (2025). Correlated Errors in Large Language Models. arXiv:2506.07962. ICML 2025.

- **Primary finding:** On one leaderboard dataset, LLMs agree 60% of the time when both make mistakes. Models with the same provider, same base architecture, or similar sizes have more correlated errors. Critically, **larger and more accurate models have highly correlated errors even with distinct architectures and providers** — diversity in vendor alone does not eliminate homogenization.
- **Domain:** General LLM benchmarks (two leaderboards + a resume-screening task).
- **Method:** Pairwise error-correlation analysis across model pairs.
- **N:** Over 350 LLMs evaluated.
- **Relevance to our paper:** **STRONG — counter-evidence.** This is the most important paper to cite. It supports the mechanism that vendor diversity matters (within-vendor models are more correlated), but also qualifies the claim: as models scale, errors converge across vendors anyway. Our paper's heterogeneity-guard claim should engage with this directly — diversity is real but bounded.

### 2. Yuan, Zhang, Kim, & Rajpurkar (2025). Do Mixed-Vendor Multi-Agent LLMs Improve Clinical Diagnosis? arXiv:2603.04421.

- **Primary finding:** Mixed-vendor LLM teams (o4-mini + Gemini-2.5-Pro + Claude-4.5-Sonnet) outperform single-vendor teams on clinical diagnosis. Recall@1 on RareBench: 39.31% mixed-vendor vs 36.63% best single-vendor MAC. On the hardest MME subset, mixed-vendor reached 40.00% vs Gemini's 30.00% single-model baseline (a **+10 percentage point** lift). **Performance gains inversely correlate with model similarity** — gains peak when models exhibit "distinct areas of expertise." Low Jaccard similarity between vendor outputs (MME range: 0.269–0.750) predicted larger coverage gains. Homogeneous teams remain "trapped in correlated failure modes that discussion alone cannot resolve."
- **Domain:** Clinical diagnosis (rare-disease and complex-case reasoning).
- **Method:** Multi-agent collaboration with same vs different vendor instantiations; recall@1 and top-1 accuracy.
- **N:** RareBench 498 cases (MME 40 + HMS 88 + LIRICAL 370) + DiagnosisArena 165 cases = 663 cases.
- **Relevance to our paper:** **STRONG — supporting evidence.** This is the cleanest direct support for the mechanism claim. Different vendors produce different inductive biases, and combining them rescues diagnoses single-vendor teams miss. Mirror finding for our pipeline architecture.

### 3. Amiri-Margavi, Jebellat, Jebellat, & Davoudi (2025). Enhancing Answer Reliability Through Inter-Model Consensus of Large Language Models. arXiv:2411.16797.

- **Primary finding:** Cross-vendor consensus on PhD-level statistical questions. Fleiss' Kappa per model: Claude 0.7160 (substantial), LLaMA 0.5572 (moderate), GPT-4 0.4275 (moderate), Gemini 0.2811 (fair). Full-agreement rates when each model generated questions: Claude 86%, GPT-4 82%, Gemini 70%, LLaMA 65%. Reliability percentages: Claude 92%, GPT-4 90%, Gemini 88%, LLaMA 77%. **Substantial disagreement across vendors on PhD-level statistical reasoning** — Gemini and LLaMA show much wider variability than Claude and GPT-4.
- **Domain:** Statistical reasoning, PhD-level multiple-choice (Bayesian inference, time series, survival analysis).
- **Method:** Cross-vendor majority voting; chi-square, Fleiss' Kappa, confidence intervals.
- **N:** 100 multiple-choice questions.
- **Relevance to our paper:** **STRONG — supporting evidence.** Quantifies inter-vendor disagreement on scientific reasoning with rigor. Use Fleiss kappa values as a direct empirical baseline.

### 4. Mousavi Davoudi, Davodi, Amiri-Margavi, Fard, & Jafari (2025). Collective Reasoning Among LLMs: A Framework for Answer Validation Without Ground Truth. arXiv:2502.20758.

- **Primary finding:** Follow-up to Amiri-Margavi 2025, same four-vendor setup (GPT-4-0125, LLaMA-3-70B, Claude-3-Opus, Gemini-1.5-Flash) on doctoral-level probability problems. Claude and Gemini frame questions more coherently (tighter CIs, greater concordance). LLaMA exhibits wider confidence bands and lower agreement. Cross-vendor disagreement persists as a measurable, model-specific property.
- **Domain:** Doctoral-level probability problems.
- **Method:** Chi-square, Fleiss' Kappa, CI on cross-vendor responses; majority-vote consensus without ground truth.
- **N:** Not specified in available content.
- **Relevance to our paper:** **STRONG — supporting evidence.** Reinforces #3 with a different domain (probability theory). Pair-cite with #3 to show the finding is not domain-specific.

### 5. Verga, Hofstatter, Althammer, Su, Piktus, et al. (2024). Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models. arXiv:2404.18796.

- **Primary finding:** Panel of LLM evaluators (PoLL) composed of "disjoint model families" outperforms single large-model judges and exhibits **less intra-model bias due to composition of disjoint model families** — direct support for the cross-vendor mechanism. Operates at >7x cheaper cost than single large judges.
- **Domain:** LLM-as-judge evaluation; three judge settings across six datasets.
- **Method:** Pairwise comparative judgement aggregation across a panel.
- **N:** Six datasets, three judge configurations.
- **Relevance to our paper:** **STRONG — supporting evidence.** "Disjoint model families" is the exact mechanism our pipeline relies on. Cite as prior architectural validation.

### 6. Zhang, Yu, Wang, Cohan, Wang (2025). Stop Overvaluing Multi-Agent Debate — We Must Rethink Evaluation and Embrace Model Heterogeneity. arXiv:2502.08788.

- **Primary finding:** Systematic evaluation of 5 MAD methods across 9 benchmarks using 4 foundational models. Multi-agent debate with **homogeneous** models often fails to beat single-agent baselines (Chain-of-Thought, Self-Consistency). The fix: **model heterogeneity acts as a universal antidote** to consistently improve MAD frameworks. Position-paper conclusion: the field must "actively embrace model heterogeneity as a core design principle."
- **Domain:** Multi-agent LLM debate across 9 reasoning benchmarks.
- **Method:** Meta-analysis comparing MAD variants and homogeneous vs heterogeneous configurations.
- **N:** 5 MAD methods x 9 benchmarks x 4 base models.
- **Relevance to our paper:** **STRONG — supporting evidence.** Same architectural recommendation our pipeline follows. Cite for the "model heterogeneity is a universal antidote" claim.

---

## MODERATE relevance

### 7. Wright, Masud, Moore, Yadav, Antoniak, Christensen, Park, & Augenstein (2025). Epistemic Diversity and Knowledge Collapse in Large Language Models. arXiv:2510.04226.

- **Primary finding:** All 27 tested LLMs are less epistemically diverse than basic web search. Model size has a **negative impact** on epistemic diversity (larger = more homogeneous). RAG improves diversity but improvement varies by cultural context. Newer models generate more diverse claims than older models.
- **Domain:** Open-ended factual claims across 12 countries, 155 topics.
- **Method:** Claim-extraction from outputs, diversity quantified per-claim.
- **N:** 27 LLMs x 155 topics x 200 prompt templates = 1,080,000+ generation calls.
- **Relevance to our paper:** **MODERATE.** Measures diversity *of model outputs*, not cross-vendor agreement specifically — but speaks directly to the homogenization mechanism. Useful for framing the "epistemic homogenization" threat our pipeline guards against.

### 8. Hodel & West (2025). Epistemic diversity across language models mitigates knowledge collapse. arXiv:2512.15011.

- **Primary finding:** Ecosystem-level diversity (M=4 models) is optimal for resisting iterative knowledge collapse during self-training cycles. Single-model ecosystems show rapid perplexity increase; M=16 shows improved resilience.
- **Domain:** Self-training simulation on Wikitext-2.
- **Method:** 10-iteration self-training across M=1, 2, 4, 16 models.
- **N:** GPT-2 + OPT-125m (NOT cross-vendor — same model type instances).
- **Relevance to our paper:** **MODERATE.** Theoretical support for ecosystem diversity but uses model-type rather than vendor variation. Cite for the systemic argument; flag the methodology limitation if using.

### 9. Wang, Wang, Athiwaratkun, Zhang, & Zou (2024). Mixture-of-Agents Enhances Large Language Model Capabilities. arXiv:2406.04692. ICLR 2025 Spotlight.

- **Primary finding:** Layered multi-LLM architecture; identifies the "collaborativeness" phenomenon — an LLM tends to generate better responses when presented with outputs from other models, even less capable ones. Open-source MoA scores 65.1% on AlpacaEval 2.0 vs GPT-4 Omni's 57.5%.
- **Domain:** General instruction-following (AlpacaEval 2.0, MT-Bench, FLASK).
- **Method:** Layered ensemble of LLMs from multiple sources.
- **N:** AlpacaEval-scale; not a controlled inter-vendor agreement study.
- **Relevance to our paper:** **MODERATE.** Architectural precedent for multi-LLM pipelines but doesn't itself measure cross-vendor disagreement rates. Cite as architectural prior; not for empirical agreement claims.

### 10. Chiang, Zheng, Sheng, et al. / LMSYS (2024). Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference. arXiv:2403.04132.

- **Primary finding:** Crowdsourced pairwise comparison (6M+ votes), Elo ratings via Bradley-Terry model. GPT-4 as judge achieves >80% agreement with crowdsourced human preferences, matching human-human agreement. Expert validation: 72–83% agreement between crowdsourced votes and Berkeley grad students; inter-expert 79–90%.
- **Domain:** General LLM responses, all categories.
- **Method:** Pairwise blind comparison + Elo rating.
- **N:** 240K+ votes initial release; 6M+ ongoing.
- **Relevance to our paper:** **MODERATE.** Provides baseline numbers for what human-human and human-LLM agreement look like (80–85%). Useful for context, not a direct measurement of cross-vendor LLM-LLM disagreement on scientific reasoning.

---

## WEAK / TANGENTIAL

### 11. BioDesignBench (2026). Benchmarking and behavioral characterization of LLM agents for protein design. bioRxiv 2026.05.06.723381.

- **Status: PRIMARY-SOURCE-PENDING.** PDF fetch returned 403 from bioRxiv on 2026-05-12 and again on 2026-05-14. Claims below are from secondary summaries / search-result excerpts.
- **Primary finding (per abstract summary):** Four frontier LLMs (DeepSeek V3, GPT-5, Claude Sonnet 4.5, Gemini 2.5 Pro) on 76 expert-curated protein-design tasks. Agents select appropriate tools but evaluate candidates too shallowly, rarely compare alternatives, terminate prematurely. **Relative performance ordering NOT verified from primary source.** The earlier wiki claim that "DeepSeek V3 significantly outperforms GPT-5 and Gemini 2.5 Pro" is still PRIMARY-SOURCE-PENDING.
- **Domain:** Protein design (antibodies, enzymes, fluorescent proteins, binders, scaffolds).
- **Method:** Benchmarking + behavioral characterization (tool-gap vs science-gap decomposition).
- **N:** 76 tasks.
- **Relevance to our paper:** **WEAK with caveat.** The paper measures *task accuracy* across vendors, not *inter-vendor output agreement*. Don't conflate the two. The behavioral-characterization framework (tool gap vs science gap) is more directly portable to our pipeline than the raw accuracy numbers.
- **Action: do not cite as primary evidence for cross-vendor disagreement until PDF is verified.** Cite only for the existence of differential vendor performance on scientific tasks, and only after the bioRxiv PDF is in hand.

### 12. Adaptive Heterogeneous Multi-Agent Debate (A-HMAD) (2025). J. King Saud Univ. CIS, doi:10.1007/s44443-025-00353-3.

- **Primary finding:** Heterogeneous-role agents (Verifier + Solver etc) achieve 4–6% absolute accuracy gain over standard MAD. Reduces factual errors by >30% in biography facts.
- **Domain:** Educational and factual reasoning.
- **Method:** Specialized-role heterogeneous agents.
- **N:** Not extracted.
- **Relevance to our paper:** **WEAK.** Useful adjacent evidence for heterogeneity as architecture principle. Not cross-vendor specifically.

### 13. HELM / HELM-Lite (Liang et al. 2022, ongoing). Holistic Evaluation of Language Models. arXiv:2211.09110.

- **Primary finding:** Standardized benchmark across 30+ LLMs from multiple providers on 42 scenarios with 7 metrics. Establishes that prior to HELM, models were typically evaluated on only 17.9% of comparable scenarios; HELM raised coverage to 96.0%.
- **Domain:** General LLM evaluation framework.
- **Method:** Cross-provider standardized scenarios.
- **N:** 30+ models, 42 scenarios.
- **Relevance to our paper:** **TANGENTIAL.** Provides cross-vendor performance data but doesn't directly measure agreement rates. Frame as background for "yes, we have standardized cross-vendor evals, but they measure accuracy not agreement."

### 14. Sclar, Choi, et al. (2023). Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design. arXiv:2310.11324. ICLR 2024.

- **Primary finding:** LLMs show up to 76 accuracy-point swings from prompt-formatting changes alone. Format performance only weakly correlates between models — same prompt good for one vendor may be bad for another.
- **Domain:** Few-shot prompt formatting sensitivity.
- **Method:** Prompt-template ablations across models.
- **N:** Tested LLaMA-2-13B and other open-source models primarily.
- **Relevance to our paper:** **TANGENTIAL.** Establishes that cross-vendor prompt sensitivity is large enough to dominate signal — relevant for our methodology section (need to standardize prompts), not for the agreement mechanism claim directly.

### 15. Du, Li, Torralba, Tenenbaum, & Mordatch (2023). Improving Factuality and Reasoning in Language Models through Multiagent Debate. arXiv:2305.14325. ICML 2024.

- **Primary finding:** Multiple instances of the **same model** debating each other improve factual accuracy and reasoning. Note: this is **within-model** debate, not cross-vendor.
- **Domain:** General reasoning.
- **Method:** Multi-round debate among same-model instances.
- **N:** Not relevant to cross-vendor question.
- **Relevance to our paper:** **TANGENTIAL.** Often cited as the multi-agent debate foundation paper, but the cross-vendor extension is in Zhang 2025 (#6) and Yuan 2025 (#2), not here. Cite Du for the MAD framework, not for cross-vendor diversity claims.

---

## Quick-reference table

| # | Authors | Year | arXiv | Vendors tested | N | Cross-vendor agreement measured? | Relevance |
|---|---|---|---|---|---|---|---|
| 1 | Kim et al. | 2025 | 2506.07962 | 350+ models | 350+ | YES (error correlation) | STRONG (counter) |
| 2 | Yuan et al. | 2025 | 2603.04421 | OpenAI, Google, Anthropic | 663 cases | YES (Jaccard, recall delta) | STRONG (support) |
| 3 | Amiri-Margavi et al. | 2025 | 2411.16797 | OpenAI, Anthropic, Google, Meta | 100 Qs | YES (Fleiss kappa) | STRONG (support) |
| 4 | Mousavi Davoudi et al. | 2025 | 2502.20758 | OpenAI, Anthropic, Google, Meta | n/a | YES (Fleiss kappa) | STRONG (support) |
| 5 | Verga et al. | 2024 | 2404.18796 | "disjoint model families" | 6 datasets | YES (bias attribution) | STRONG (support) |
| 6 | Zhang et al. | 2025 | 2502.08788 | 4 base models | 5x9x4 | YES (heterogeneity meta-analysis) | STRONG (support) |
| 7 | Wright et al. | 2025 | 2510.04226 | 27 LLMs | 27x155x200 | INDIRECT (diversity, not agreement) | MODERATE |
| 8 | Hodel & West | 2025 | 2512.15011 | Same-model only | 7,500 dp | NO (ecosystem-level only) | MODERATE |
| 9 | Wang et al. | 2024 | 2406.04692 | Multiple | n/a | NO (performance, not agreement) | MODERATE |
| 10 | Chiang et al. | 2024 | 2403.04132 | 100+ | 6M+ votes | INDIRECT (pairwise prefs) | MODERATE |
| 11 | BioDesignBench | 2026 | bioRxiv | 4 vendors | 76 tasks | NO (accuracy only) | WEAK [UNVERIFIED] |
| 12 | A-HMAD | 2025 | doi:10.1007/s44443-025-00353-3 | Heterog roles | n/a | NO (role heterog) | WEAK |
| 13 | HELM / Liang et al. | 2022+ | 2211.09110 | 30+ | 30 x 42 | NO (accuracy benchmarks) | TANGENTIAL |
| 14 | Sclar et al. | 2023 | 2310.11324 | Various | n/a | NO (prompt sensitivity) | TANGENTIAL |
| 15 | Du et al. | 2023 | 2305.14325 | Same-model only | n/a | NO (within-model debate) | TANGENTIAL |
