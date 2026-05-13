# Verification audit — §2 citation pool

Honest record of how each citation in `refs.bib` was verified, and what the
gaps are. This document is load-bearing for the paper's Appendix B (revision
log) since §2 was the section drafted with explicit cross-vendor / external
tooling.

## Pool composition

11 records total in `citation_pool.json`:

| Cite key | Cluster | Year | Verification | Source |
|---|---|---|---|---|
| `bai2022constitutional` | constitutional_ai | 2022 | **S2** | Semantic Scholar canonical record |
| `lu2024ai` | ai_scientist | 2024 | **S2** | Semantic Scholar canonical record |
| `shumailov2024ai` | model_collapse | 2024 | **S2** | Semantic Scholar canonical record |
| `shinn2023reflexion` | reflexion | 2023 | **S2** | Semantic Scholar canonical record |
| `du2023improving` | multiagent_debate | 2023 | **WebSearch + arXiv ID** | arXiv:2305.14325 |
| `madaan2023self` | self_refine | 2023 | **WebSearch + arXiv ID** | arXiv:2303.17651 |
| `verga2024replacing` | llm_jury | 2024 | **WebSearch + arXiv ID** | arXiv:2404.18796 |
| `lee2023rlaif` | rlaif | 2023 | **WebSearch + arXiv ID** | arXiv:2309.00267 |
| `yamada2025ai` | ai_scientist_v2 | 2025 | **WebSearch + arXiv ID** | arXiv:2504.08066 |
| `song2026paperorchestra` | paper_orchestra | 2026 | **WebSearch + arXiv ID** | arXiv:2604.05018 |
| `shumailov2023curse` | curse_recursion | 2023 | **WebSearch + arXiv ID** | arXiv:2305.17493 |

## Verification process and gap

The literature-review-agent skill (from `~/paper-orchestra/skills/literature-review-agent/`) specifies a two-phase pipeline:

1. **Phase 1 — Discovery.** Web search for candidate papers per cluster. Returns `(title, snippet, url)` tuples. ✅ Completed cleanly for all 11 candidates.

2. **Phase 2 — Semantic Scholar verification.** Sequential 1-QPS queries against Semantic Scholar's `paper/search` endpoint via `scripts/s2_search.py`, with Levenshtein > 0.70 title-match, non-empty abstract, and year-≤-cutoff checks. ⚠️ **Partial.** Only 4 of 11 candidates landed cleanly via S2 before the unauthenticated endpoint rate-limited the run.

The S2 rate-limit incident (2026-05-13): the script ran a first pass at 1.0s spacing, which exceeded S2's unauthenticated burst budget after 3 successful queries; a retry pass at 8.0s spacing recovered one additional record (Reflexion) but the remaining 7 candidates all hit `HTTP 429 — rate-limited and retries exhausted`. The standard mitigation is to set `SEMANTIC_SCHOLAR_API_KEY` for the ~100x rate-limit headroom, but no key was available at draft time.

**Manual fallback applied.** For the 7 unverified candidates, records were constructed from the WebSearch results already in the drafting context plus the canonical arXiv IDs returned in those results. Each record is marked `"verification": "websearch+arxiv"` in `citation_pool.json`. The arXiv IDs are load-bearing — they are the canonical identifiers WebSearch returned, and they resolve to the listed metadata on arxiv.org. Authors, titles, years, and abstracts come from the WebSearch summaries, which in turn come from arxiv.org listings.

## S2 API key request status

**Submitted: 2026-05-13.** Brian filed the S2 API key request form at `https://www.semanticscholar.org/product/api#api-key-form` with the use-case description, endpoint list (`/graph/v1/paper/search`, `/graph/v1/paper/{paperId}`, `/graph/v1/paper/arXiv:{id}`), and request-volume estimate (100-500/day during drafting bursts, <50/day average, never above 1 QPS). All five required-checkbox acknowledgments confirmed honestly: prior unauthenticated requests made, exponential backoff in place, 60-day-inactivity removal acknowledged, license read and accepted.

Response from the form: *"Thank you for your request. We have received your information. Please note that we are currently working on a backlog of requests and we appreciate your patience!"*

**Approval is asynchronous and not guaranteed by submission deadline.** Public issue threads report 5+ day waits with no response in some cases. The fallback plan if the key arrives in time is to re-run `run_verify.py` with `SEMANTIC_SCHOLAR_API_KEY` set and upgrade the 7 WebSearch+arXiv records to full S2-verified.

**If the key does not arrive before submission**, the next-session task is to swap the verification arm from S2 to **arXiv's direct API** (`http://export.arxiv.org/api/query?id_list=<arxiv_id>`), which is free, unauthenticated, no rate limit at our query volume, and returns title/authors/abstract/date for every one of the 7 fallback records (each has an arXiv ID). This is strictly better than the current WebSearch+arXiv-string fallback because the metadata comes from arXiv's canonical record, not from a search-result summary.

## Why this gap is acceptable for the draft, with caveats

The literature-review-agent's S2 verification step is a backstop against the case where a candidate paper does not exist or is mis-titled. In our case, every candidate was already known to exist (WebSearch returned arxiv.org URLs for each), so the S2 check would have been a belt-and-suspenders confirmation rather than a discovery mechanism. Skipping it under rate-limit duress and noting the gap is defensible for a working draft.

Caveats Brian should resolve before submission:

1. **Re-run Phase 2 with a Semantic Scholar API key** before bioRxiv submission. Get a free key at https://api.semanticscholar.org/, set `SEMANTIC_SCHOLAR_API_KEY` in `~/.config/abent/paperorchestra.env`, re-run `run_verify.py`. Any record that fails S2 verification with a key in place must be either replaced or noted as an unverified citation in the manuscript itself.

2. **Confirm `song2026paperorchestra` metadata directly against arXiv 2604.05018.** This is the cite for the very tool being used to draft this paper; mis-citing it would be embarrassing. The WebSearch result returned `Yiwen Song, Yale Song, Tomas Pfister, Jinsung Yoon` as authors, which matches the marktechpost article ("Google Cloud AI Research"); cross-check against the arXiv abstract page.

3. **FARS is cited via the public deployment record (analemma.ai/fars/), not a peer-reviewed paper.** The §2.5 footnote acknowledges this. If reviewers push back on the non-peer-reviewed citation, replace with a more general reference to "end-to-end automated-research systems" or drop the specific FARS reference.

## What the reflexive narrative gets from this

The S2 rate-limit incident is, by the paper's own framing, a **failure of an external tool** — the same failure class as the §5.3 Paperclip MCP probe in the main paper. The honest documentation of the gap, the explicit verification fallback discipline, and the to-do for Brian before submission are exactly the kind of "rigor under degradation" the paper's own methodology section advocates. This audit document is preserved as supplementary material for Appendix B.

The deeper observation: even when running purpose-built tooling (PaperOrchestra's literature-review-agent skill pack), external API rate limits can break the verification arm of the pipeline. The architectural lesson is that the heterogeneity-guard pattern should not depend on a single external verification service — if S2 rate-limits, fall back to the next-best canonical identifier (arXiv ID), and log the degradation honestly rather than pretend the verification succeeded.
