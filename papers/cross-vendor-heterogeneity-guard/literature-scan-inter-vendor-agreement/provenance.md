# Search provenance log

Scan executed 2026-05-14, ~10:30–10:55 AST. Tools used: WebSearch + WebFetch (Claude Code).

## Search terms tried (in order)

1. `"inter-model agreement" LLM cross-vendor scientific reasoning benchmark`
2. `multi-agent LLM debate Du 2023 "Improving Factuality" Claude GPT disagreement`
3. `LLM ensemble diversity disagreement GPT-4 Claude Gemini scientific tasks`
4. `cross-LLM consistency reliability medical question answering`
5. `"model heterogeneity" LLM ensemble factuality complementary errors`
6. `LLM consensus inter-rater agreement Fleiss kappa Claude GPT Gemini scientific`
7. `BioDesignBench LLM agent protein design DeepSeek bioRxiv 2026`
8. `"LLM-as-a-judge" inter-annotator agreement different vendors`
9. `"complementary" LLM outputs different vendors scientific reasoning bioinformatics`
10. `"MedQA" GPT-4 Claude Gemini agreement medical reasoning`
11. `"output divergence" LLM different providers same prompt hallucination`
12. `"mixture of agents" "MoA" LLM Claude GPT ensemble Wang 2024`
13. `"chatbot arena" head-to-head LLM pairwise agreement benchmark`
14. `HELM holistic evaluation LLM cross-model comparison benchmark Stanford`
15. `"epistemic diversity" LLM ensemble model heterogeneity`
16. `Du multi-agent debate "GPT" "Bard" cross model heterogeneous`
17. `"LLM jury" multiple models scientific evaluation agreement`
18. `"frontier model" agreement disagreement reasoning benchmark different families`
19. `"correlated errors" foundation models multiple providers same training data`
20. `"epistemic homogenization" "knowledge collapse" LLM diversity`
21. `BioDesignBench Google Scholar 76 tasks protein design behavioral characterization`
22. `"prompt sensitivity" GPT Claude variance same task scientific`
23. `"GPQA" Claude GPT Gemini scientific reasoning performance comparison`
24. `"semantic similarity" LLM vendor outputs same prompt cross-model variance`
25. `"Stop Overvaluing Multi-Agent Debate" arXiv 2502.08788`

## Direct fetches (WebFetch)

| URL | Outcome | Notes |
|---|---|---|
| arXiv:2411.16797 (abs) | OK | Extracted abstract + methods |
| arXiv:2305.14325 (abs) | OK (partial) | Confirmed Du 2023 is within-model debate, not cross-vendor |
| arXiv:2502.20758 (abs) | OK | Confirmed follow-up to Amiri-Margavi 2025 |
| arXiv:2411.16797v2 (HTML) | OK | Extracted Fleiss kappa table + N=100 |
| arXiv:2603.04421 (HTML) | OK | Extracted all sample sizes + lift numbers |
| bioRxiv 2026.05.06.723381v1 | **HTTP 403** | BioDesignBench PDF blocked — same as 2026-05-12 attempt |
| bioRxiv 2026.05.06.723381v1.full.pdf | **HTTP 403** | Confirmed bioRxiv 403 still blocking; PRIMARY-SOURCE-PENDING flag stands |
| arXiv:2510.04226 (abs) | OK | Wright 2025 epistemic diversity — extracted 27/155/200 |
| arXiv:2406.04692 (abs) | OK | MoA paper — confirmed no direct cross-vendor agreement metric |
| arXiv:2502.20758 (abs) | OK | Mousavi Davoudi 2025 |
| arXiv:2404.18796 (abs) | OK | Verga 2024 PoLL — confirmed "disjoint model families" framing |
| arXiv:2506.07962 (abs) | OK | Kim 2025 Correlated Errors — 350+ LLMs confirmed |
| arXiv:2512.15011v1 (HTML) | OK | Hodel & West — confirmed NOT cross-vendor (GPT-2 + OPT-125m only) |

## Dead ends / weak hits

- The Trends in Cognitive Sciences paper (cell.com S1364-6613(26)00003-3) on "homogenizing effect of LLMs on human expression" came up but is about LLM impact on human thought, not LLM-to-LLM agreement. Skipped.
- LLM-TOPLA (Findings of EMNLP 2024) on diversity-maximizing ensembles came up but does not measure inter-vendor agreement directly. Skipped.
- Multilingual consistency work (Springer chapter on health-Q across EN/DE/TR/ZH) tests within-model multilingual variance, not cross-vendor agreement. Skipped.
- M3MAD-Bench (arXiv:2601.02854) on multi-modal multi-agent debate flagged but not pulled — outside the heterogeneity-guard scope.
- Adaptive Heterogeneous MAD (Springer JKSU 2025) included as tangential — role heterogeneity, not vendor heterogeneity.
- Du et al. 2023 (Improving Factuality through Multiagent Debate) — initially flagged as candidate primary source, but verified to be within-model debate (multiple instances of same LLM), not cross-vendor. Marked as TANGENTIAL.

## Sources searched

- arXiv (cs.CL, stat.AP)
- bioRxiv (one paper relevant, primary source unavailable)
- OpenReview (ICLR, NeurIPS, ICML proceedings)
- ACL Anthology (via search)
- ResearchGate (for cached preprints)
- ICML 2025 proceedings (Kim 2025 confirmed accepted)
- Google Scholar (via web search results)

## Sources NOT directly searched (but indirectly surfaced)

- PubMed: not separately queried; medical-domain LLM work surfaced via general web search
- ACL Anthology direct: indirectly via search results
- NeurIPS proceedings direct: indirectly via search results

## Time spent

Wall-clock ~25 minutes of active searching + ~5 minutes writing. Within budget.

## Confidence calibration

- **High confidence** (verified abstract + sample size + method): papers #1–#10 in bibliography.md
- **Medium confidence** (web-search summary, abstract not directly fetched): #11–#15
- **PRIMARY-SOURCE-PENDING** (bioRxiv 403): BioDesignBench. Same as 2026-05-12 status. No new information added to wiki.

## Verification gates passed

- Sample sizes for the top three citations verified from arXiv HTML extraction.
- Fleiss kappa values from Amiri-Margavi 2025 verified from arXiv 2411.16797v2 HTML rendering (one pass via WebFetch).
- Yuan 2025 recall numbers verified from arXiv 2603.04421v1 HTML rendering (one pass via WebFetch).
- Kim 2025 "60% agreement when both err" verified from search-summary cross-reference but not from primary PDF — flagged in key-quotes.md as `[SUMMARY-EXTRACTED]`, recommend full-text re-verification before paper submission.
- BioDesignBench claims marked `[UNVERIFIED]` consistent with the wiki's existing PRIMARY-SOURCE-PENDING flag.
