# `agentic_lit_synthesis.py` — API cheatsheet + artifact structure

Shared library: `wiki/etc/experiments/lib/agentic_lit_synthesis.py`. stdlib-based; OpenRouter secrets from the repo-root `.env` (gitignored) via `load_root_dotenv(start)`. Import it from a scan script run at repo root, or call functions from a subagent.

## Query planning

```python
build_language_native_query_plan(
    scope, mechanisms=None, species=None, formulas=None, pathologies=None,
    languages=("zh", "ja", "ko"), western_queries=None,
    natural_product_scope=True, required_frames=None,
) -> query_strategy   # dict; save to inputs/query-strategy.json
```
Builds a multilingual query plan across **four frames** — mechanism-name, species-name (+ original-language), traditional-formula, traditional-pathology. Pass `mechanisms=`, `species=`, `formulas=`, `pathologies=` to seed each frame. Set `natural_product_scope=False` for pure Western pharma/synthetic-chemistry scope (skips the traditional frames; document why in the artifact).

```python
native_terms(language, mechanisms=None, pathologies=None) -> list   # original-language term expansion
audit_query_strategy_language_framing(query_strategy, languages=("zh","ja","ko")) -> report
```
`audit_...` verifies the plan actually covers each language + frame — run it before fetching so you catch a Western-only plan before it biases the scan.

## Fetching

```python
fetch_pubmed_snapshot(query_strategy, retmax_per_query=10, pause_seconds=0.34) -> records
pubmed_search(query, retmax=10, mindate=None, maxdate=None) -> pmids
pubmed_fetch_records(pmids) -> records
```
```python
local_curl_fetch(url, output_dir, allowed_suffixes=None, timeout_seconds=90, allow_insecure_tls=False) -> path|None
host_allowed_for_local_curl(hostname, allowed_suffixes=None) -> bool
```
**`local_curl_fetch` is MANDATORY for East-Asian sources** (CNKI / WanFang / ChiCTR / CQVIP / ChinaXiv / Baidu Scholar / J-STAGE / CiNii / KISS / RISS). Those hosts are in the sandbox network allowlist and reachable only via the local `curl` binary — hosted/browser fetch bot-blocks. `host_allowed_for_local_curl` gates the URL against the whitelisted suffixes.

## Translation (two-model cross-check)

```python
translation_models_for_language(config, language) -> (model_a, model_b)   # different vendors
translate_source_two_model(client, source_text, language, source_id, config, output_dir, target_language="English") -> annotated
counterread_source_single_model(...) -> read   # cheaper single-model pass when a full cross-check isn't warranted
```
The Claude subagent running the scan **is Model A** — `translate_source_two_model` only pays OpenRouter for Model B (`memory/feedback_subagent_as_model_a.md`). Surface disagreements as inline annotations; tag tier/dose/mechanism-changing ones `[TRANSLATION-DISAGREEMENT]`. Full protocol: `wiki/etc/manual-literature-mining.md` §"Translation protocol".

## Model client + config

```python
OpenRouterClient(...).chat(model, messages, temperature=0.2, max_tokens=4096) -> text
role_model(config, role) -> model_id      # role → model routing from config
load_root_dotenv(start); read_json(path); write_json(path, data); safe_filename(text)
```

---

## Artifact structure (`logs/<scope>-lit-scan-<date>.md`)

Follow the shape of recent scans (e.g. `logs/cbd-vs-flavonoid-gut-degradation-lit-scan-2026-07-13.md`):

```markdown
---
title/date/tags frontmatter
---

# <the one question the scan answers>

## Load-bearing findings (per compound / per claim)
### <item>
- finding + evidence-level tag + (source: PMID/DOI)

## Verdict table
| item | verdict | evidence tier | key source |

## Biggest evidence gap
<what the literature does NOT resolve — the honest limitation>

## Queries run
<the multilingual query plan actually executed, per frame + language>

## Primary sources (PMID / DOI)
<full citation list; non-English sources with original-language title + English gloss>
```

**Workspace:** intermediates (fetched sources, per-source translations, `query-strategy.json`) live in `operations/<scope>-<date>/`; only the synthesized artifact + its primary-source list land in `logs/`. Propagate load-bearing findings from the artifact to the canonical wiki pages with evidence tiers — the scan is the working record, the wiki is the corpus.
