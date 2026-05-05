---
title: Paperclip (GXL) — Agent-Native Scientific Literature MCP
date: 2026-05-05
tags: [tools, mcp, literature, sweep-daemon, infrastructure]
related: [bio-ai-tools.md, open-source-platform.md]
sources:
  - "James Zou (Stanford / Chan-Zuckerberg / Together Compute) — pinned tweet announcement, May 2026"
  - "https://gxl.ai/blog/paperclip/"
  - "https://gxl.ai/blog/adding-arxiv-and-abstracts/"
  - "https://paperclip.gxl.ai/"
---

# Paperclip (GXL) — Agent-Native Scientific Literature MCP

## What it is

[Paperclip](https://paperclip.gxl.ai/) is an MCP server (and CLI) for scientific literature, built by [GXL (Generative Expert Labs)](https://gxl.ai/), a Stanford-adjacent group connected to James Zou's lab. Unlike PubMed or Google Scholar — which return links and stop — Paperclip exposes papers to an LLM as a structured filesystem: search, grep, cat, map, and SQL operations chain through a stateful `results_id`, so an agent can narrow a corpus iteratively over many turns without re-searching.

Naming caveat: there is an unrelated product (paperclip.ing / paperclipai) for AI agent orchestration. Not the same tool. The literature one is **paperclip.gxl.ai**, made by **GXL**.

## Corpus

| Source | Coverage | Type |
|---|---|---|
| PubMed Central | ~5M+ | Full text, biomedical, open access |
| arXiv | ~3M | Full text, ML / math / quant-bio / physics / CS |
| bioRxiv + medRxiv | ~3M+ | Full text, preprints |
| OpenAlex | ~150M+ | Abstracts + structured metadata only |

Total: ~11M full-text papers + ~150M abstracts. Coverage caveats: PMC has embargo periods for some journals; only open-access full text is indexed. Abstract-only coverage means you can map the landscape but not grep within the body for non-OA papers.

## Commands

| Command | Function |
|---|---|
| `search` | Hybrid (BM25 + vector embedding) search; returns 1–2 sentence TL;DRs |
| `grep` | Regex / keyword search within full text. Vendor claim: 36–294× faster than raw grep on the 8M+ paper index — unverified |
| `cat` | Reads structured paper text (sections, tables, figures) |
| `map` | Applies a prompt across a result set — the synthesis primitive |
| `ask-image` | Multimodal query against figures and images |
| `sql` | Read-only SQL over metadata table; 15s timeout, 200-row limit |
| `--from <results_id>` | Chains operations against a previous result set |

The `--from` chaining is the load-bearing piece — every search produces a cloud-stored `results_id`, and subsequent grep / map / cat operations can target it. An agent can search broadly, narrow by grep, synthesize via map, then drill into specific papers without losing the working set.

## Setup

```
claude mcp add --transport http paperclip https://paperclip.gxl.ai/mcp
```

Or in `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "paperclip": { "url": "https://paperclip.gxl.ai/mcp" }
  }
}
```

The hosted MCP at `paperclip.gxl.ai/mcp` is currently free and does not appear to require an API key. Pricing tiers have not been announced. As a Stanford / Together Compute-adjacent project this may remain free for research use, but plan for the possibility of usage limits.

## Comparison to PubMed and Google Scholar

| Dimension | PubMed | Google Scholar | Paperclip |
|---|---|---|---|
| Primary user | Humans (web UI) | Humans (web UI) | LLM agents (and humans via CLI) |
| Corpus | ~36M citations, biomedical | Broad multidisciplinary | 11M full-text + 150M abstracts, bio + ML + preprints |
| Searches within full text | No (links to it) | No (links to it) | Yes |
| Stateful chaining | No | No | Yes (`--from`) |
| Native API for agents | Limited (NCBI E-utilities) | None official | MCP-native |
| Synthesis primitive | Manual | Manual | `map` |
| Multimodal (figures) | No | No | Yes (`ask-image`) |

**When to still use PubMed:** MeSH-vocabulary searches, citation tracking by PMID, peer-reviewed-only filtering. (Paperclip does not appear to support MeSH; preprints and OA full text are mixed in by default.)

**Where Paperclip is differentiated:** searching *within* papers, cross-domain queries that span biomedical + ML, multi-paper synthesis via `map`, and any agent-driven workflow.

The OE [bio-ai-tools.md](./bio-ai-tools.md) page already lists the Anthropic life-sciences MCP marketplace (PubMed, bioRxiv, ChEMBL, Open Targets, ClinicalTrials.gov) as Phase 0 core. Paperclip is complementary, not a replacement: the marketplace plugins are best-in-class for their specific sources (PubMed's MeSH index, ChEMBL's bioactivity tables); Paperclip wins on full-text search and cross-source synthesis.

## Reliability — 2026-05-05 verification test

A first end-to-end test (uricase variant landscape + *A. oryzae* expression evidence) surfaced a **systematic hallucination pattern in the `map` operator** that significantly changes the trust model for this MCP. Documenting here so future Paperclip sessions inherit the correct guardrails.

### Trust ranking by tool

| Tool | Reliability | Notes |
|---|---|---|
| `search` | **High** | Returns real PMC / bioRxiv / arXiv records with accurate IDs and titles. Verified by spot-checking against `meta.json` and external lookups. |
| `cat /papers/<id>/meta.json` | **High** | Authoritative paper metadata — title, abstract, authors, journal, PMID, DOI. Use as ground truth for abstract-level claims. |
| `grep PATTERN /papers/<id>/...` | **High** | Returns real text from indexed paper bodies. Use to verify any quantitative claim before propagation. |
| `cat /papers/<id>/content.lines` | **High** | Real full-text. Same trust level as grep. |
| `map --from <id> "extract X"` | **LOW — hallucinates quantitative data and misattributes organisms** | Lighter "reader" model behind `map` substitutes plausible-looking domain values when full text doesn't directly support the requested field. Treat outputs as hypothesis-generation, not evidence. |
| `reduce --from <map-id> ...` | **Compounding risk** (model-on-model) | If the underlying `map` is wrong, `reduce` consolidates wrong claims into a confident-looking summary. |

### Concrete examples from the 2026-05-05 test

All of these were caught by grep-verifying body text or reading the actual abstract via `meta.json` after `map` returned the structured field. None of these are subtle — they're load-bearing identity errors.

| Paper | Abstract / body says | `map` returned |
|---|---|---|
| PMC9773812 (Najjari 2022, PASylated UOX) | ***A. flavus* UOX**, K<sub>m</sub> 52.61 µM | ***A. globiformis*** uricase variant (S284G, K304R), K<sub>m</sub> 0.007 mM (~7,500× off) |
| PMC4881585 (Xie 2016, chimeric uricase) | **Porcine**-human exon-replacement chimera | ***P. chrysogenum***-human exon chimera (different organism entirely) |
| PMC10561068 (Yan 2023, *Arthrobacter* CSAJ-16) | Optimal **T 20°C**, K<sub>m</sub> **0.048 mM** (Lineweaver-Burk, body L40) | Optimal T 40°C, K<sub>m</sub> 0.015 mM |
| PMC12106716 (Rahbar 2025, A. flavus disulfide design) | **Pure computational paper** — frustration mapping + RMSF + tunnel analysis, no wet-lab | Invented Tm 64.9 → 70.3°C, K<sub>m</sub>/k<sub>cat</sub> measurements as if wet-lab data existed; named non-existent S173C/L221C mutation pair (real predicted pairs are A6-C290 and S119-C220) |

These are not transcription errors. They are confabulations — plausible-looking values and organism names that would pass a casual review but are not in the underlying full text.

### Probable mechanism

Paperclip's `map` operator runs a lightweight per-paper extraction model. When asked for specific quantitative or identity fields the model can't ground in the indexed text, it appears to substitute domain-plausible values rather than emit "not reported." This is a known failure mode for small models forced into structured-output tasks they can't actually support.

### Verification discipline for any future Paperclip session

1. **Use `search` and `grep` as primary evidence.** Treat `map` outputs as a sketch of where to look, not as data.
2. **Grep-verify every load-bearing number** against the paper body before letting it into the wiki. If grep can't find it, it didn't come from the paper.
3. **Anchor identity claims (organism, gene, host, year) to `meta.json`.** Abstracts in `meta.json` are clean — use them as the source of truth for organism / engineering-approach claims.
4. **Never propagate `reduce` summaries directly.** If the underlying `map` was bad, `reduce` will confidently consolidate the bad claims.
5. **Computational vs. wet-lab status must be checked from the abstract or methods section.** `map` does not reliably distinguish these.

The corpus and the deterministic tools are good. The model-mediated synthesis layer is not yet trustworthy for content destined for the wiki.

## Relevance to Open Enzyme

Three plausible roles, listed by how concrete the integration is:

### 1. Manual research depth — immediately usable

For any specific question already in the wiki, Paperclip enables systematic full-text review where the existing MCP plugins can only return abstracts:

- **Uricase mutation landscape** — search + grep + map across PMC and arXiv to catalog published variants, hosts, catalytic parameters, immunogenicity. Currently scattered across `uricase.md`, `crispr-uricase.md`, `engineered-koji-protocol.md`.
- **NLRP3 inhibition mechanisms** — map across the NLRP3 corpus for dosing and efficacy data, complementing `nlrp3-exploit-map.md` and `nlrp3-inhibitor-screen.md`.
- **Koji / *A. oryzae* expression systems** — cross-reference food-science and synthetic-biology literature for promoter / cassette / yield data; expands `aspergillus-oryzae.md` and the Ward 1995 dual-cassette material in `koji-endgame-strain.md`.
- **Cross-domain queries** — e.g., grep for "uricase" + "food-grade" or "ABCG2" + "probiotic" across the full corpus to surface intersections that PubMed and Scholar fragment.

### 2. Sweep-daemon integration — DECIDED 2026-05-05: do not integrate

**Decision: do not wire Paperclip into the four-pass sweep daemon.** The reliability finding above (`map` operator hallucinations) is disqualifying for any architecture that lands Paperclip-derived content into the wiki without a human in the loop.

The original framing — Paperclip-augmented pass producing a "literature delta" surface for the synthesis stage — assumed the synthesis primitive (`map`) could be trusted to faithfully extract per-paper findings. The 2026-05-05 verification test invalidated that assumption: `map` produced load-bearing identity errors (wrong organisms, wrong gene names, fabricated kinetic numbers) on multiple papers in a single session. Wiring this into the sweep would inject a structured external hallucination source into a corpus designed for PhD-grade rigor, exactly the failure mode the multi-model synthesis architecture in [open-source-platform.md](./open-source-platform.md) is meant to guard against.

The reopen condition: if GXL ships a verified upgrade of the `map` reader model and we re-run the verification test (uricase variant landscape is a clean repeatable probe; ~12 papers, multiple known-correct ground truths via abstract + grep) and it passes cleanly, revisit. Until then Paperclip remains a manual-research-only tool, used interactively with verification discipline, never embedded in an automated pipeline.

The original "open platform decision" entry in `synthesis.md` should be closed as resolved on the same date with this same outcome.

### 3. Protein-engineering support — via arXiv coverage

arXiv inclusion brings the ML / computational biology literature into the same index as biomedical full text. Useful for keeping `bio-ai-tools.md` current — e.g., new protein language models, directed-evolution algorithms, or kidney-tropic siRNA delivery (the `modality-chokepoint-matrix.md` URAT1 vector) without bouncing between PubMed and arXiv.

## Recommendations

Updated 2026-05-05 after the verification test:

1. **Install the MCP.** Done. Available across the abent umbrella, not just OE.
2. **Use Paperclip as a manual research tool only**, with the verification discipline above. Never propagate `map` or `reduce` outputs into the wiki unverified — anchor every quantitative claim in a `grep` or abstract `meta.json` cross-check.
3. **Do not integrate Paperclip into the sweep daemon.** See §"Sweep-daemon integration — DECIDED" above for rationale and reopen condition.
4. **Report the `map` hallucination pattern to GXL.** Bug report drafted 2026-05-05 (see session log); contains reproducible examples with paper IDs and what abstract says vs. what `map` returned.

## Watch list

- **Pricing changes** — if GXL adds paid tiers, evaluate whether sweep-driven query volume justifies the cost.
- **Public repo** — `github.com/GXL-ai/paperclip` (per James Zou's announcement) for feature requests, especially around `map` improvements and citation-graph traversal.
- **PMC embargo lag** — Paperclip can only index what's openly available; recent high-impact papers in non-OA journals will be abstract-only.
- **Rate limits** — untested for sustained automated query volume.

## Sources

- [James Zou — Paperclip announcement](https://x.com/james_y_zou/status/2042333880947261832)
- [James Zou — MCP setup instructions](https://x.com/james_y_zou/status/2042333882247462998)
- [GXL Blog — Paperclip CLI for scientific literature](https://gxl.ai/blog/paperclip/)
- [GXL Blog — Adding arXiv and 150M+ abstracts](https://gxl.ai/blog/adding-arxiv-and-abstracts/)
- [Paperclip main page](https://paperclip.gxl.ai/)
- [GXL — Generative Expert Labs](https://gxl.ai/)
