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

## Relevance to Open Enzyme

Three plausible roles, listed by how concrete the integration is:

### 1. Manual research depth — immediately usable

For any specific question already in the wiki, Paperclip enables systematic full-text review where the existing MCP plugins can only return abstracts:

- **Uricase mutation landscape** — search + grep + map across PMC and arXiv to catalog published variants, hosts, catalytic parameters, immunogenicity. Currently scattered across `uricase.md`, `crispr-uricase.md`, `engineered-koji-protocol.md`.
- **NLRP3 inhibition mechanisms** — map across the NLRP3 corpus for dosing and efficacy data, complementing `nlrp3-exploit-map.md` and `nlrp3-inhibitor-screen.md`.
- **Koji / *A. oryzae* expression systems** — cross-reference food-science and synthetic-biology literature for promoter / cassette / yield data; expands `aspergillus-oryzae.md` and the Ward 1995 dual-cassette material in `koji-endgame-strain.md`.
- **Cross-domain queries** — e.g., grep for "uricase" + "food-grade" or "ABCG2" + "probiotic" across the full corpus to surface intersections that PubMed and Scholar fragment.

### 2. Sweep-daemon integration — open platform decision

The four-pass sweep daemon (Sonnet 4.6 → Gemini 2.5 Pro → Opus 4.7 → DeepSeek V4-Pro, see [open-source-platform.md](./open-source-platform.md)) currently operates only on the wiki itself. A Paperclip-augmented pass could query for new literature matching project keywords on each sweep and produce a "literature delta" surface — papers published since the last sweep that touch active research tracks, with cross-references to specific wiki pages.

This is a real architectural change to the sweep, not a tactical install — it adds an outward-facing input to a currently closed-corpus pipeline, with consequences for sweep runtime, OpenRouter token usage, signal-to-noise (literature deltas can be noisy), and whether the synthesis pass is responsible for triaging external findings vs. just propagating internal ones. Routed through `wiki/synthesis.md` as a Priority Action / Open Question rather than implemented inline. See triage note in synthesis.

### 3. Protein-engineering support — via arXiv coverage

arXiv inclusion brings the ML / computational biology literature into the same index as biomedical full text. Useful for keeping `bio-ai-tools.md` current — e.g., new protein language models, directed-evolution algorithms, or kidney-tropic siRNA delivery (the `modality-chokepoint-matrix.md` URAT1 vector) without bouncing between PubMed and arXiv.

## Recommendations

Concrete next steps, ordered by reversibility:

1. **Install the MCP.** One line, free, reversible. Available across the abent umbrella once installed, not just OE.
2. **Run a representative test query.** Suggested first probe: search "engineered uricase oral delivery", grep for "Saccharomyces" or "Aspergillus", map "summarize expression system, host, and catalytic activity for each variant." This both validates the tool and produces material the wiki may want.
3. **Triage sweep-integration in `synthesis.md`.** The literature-delta-sweep idea is the only recommendation here that affects platform architecture; everything else is tactical and can land inline.

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
