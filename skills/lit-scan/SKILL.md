---
name: lit-scan
description: Run a literature/evidence-synthesis scan — search, curate, and synthesize primary sources into a cited findings artifact — as opposed to a computational experiment (comp-NNN). Use when a wiki question needs "what does the field say" rather than code producing deterministic outputs: a compound's evidence tier, a mechanism's support, a structure-activity relationship, a clinical-landscape read, or resolving a corpus-only-pushback via primary sources. Multilingual by default (Chinese CNKI/WanFang, Japanese J-STAGE, Korean KISS via local_curl_fetch) with two-model translation cross-check. Invoke when Brian says "run a lit scan", "do the work", "what does the literature say", or when a Pass-3 pushback rests only on corpus-absence. NOT for structure/sequence/simulation/docking — that is new-comp-experiment.
---

# lit-scan

A lit scan searches, curates, and synthesizes primary literature into a **cited findings artifact**. It is the counterpart to a `comp-NNN`: a comp runs **code that produces deterministic outputs** (structure / sequence / simulation / docking); a lit scan produces an **evidence synthesis**. Their risks — and therefore their guards — differ, so they are different artifact types with different homes.

## COMP vs lit-scan — which artifact is this?

| | lit-scan (this skill) | comp-NNN (`new-comp-experiment`) |
|---|---|---|
| **Work** | search → curate → synthesize literature | run code → deterministic output |
| **Output** | cited findings artifact | committed code/inputs/outputs |
| **Risk** | search-completeness, over-claim, translation nuance | model/code correctness |
| **Guard** | multilingual framing + two-model translation + primary-source grep-verify | full lifecycle adversarial-code-review gate |
| **Home** | `logs/<scope>-lit-scan-<date>.md` (+ `operations/<scope>-<date>/`) | `wiki/etc/experiments/comp-NNN/` |

**Decision:** if the question is "what does the literature say / does this claim hold / what's the evidence tier / what is the SAR" → lit-scan. If it needs an executable model (fold, ΔΔG, docking, kinetics, MD, sequence analysis) → comp. Do NOT wrap a lit scan in COMP clothing — the comp gate reviews executable code, not a literature sweep, and the mismatch produces a hollow "reproducible script" (the comp-018 failure). Full rule: `new-comp-experiment` SKILL.md §"COMP vs lit-scan".

## When to use

| Situation | Use? |
|---|---|
| Brian says "run a lit scan" / "do the work" / "what does the literature say" | Yes |
| A Pass-3 `Push back.` / `Rejected.` rests only on corpus-absence (world-claim not in the wiki) | Yes — the default is DO THE WORK |
| An evidence-tier verdict, SAR, or clinical-landscape read is needed before a wiki edit | Yes |
| The question needs an executable model (structure / docking / ΔΔG / kinetics / MD) | No — `new-comp-experiment` |
| A single fact needs one grep-verify against a known source | No — just verify it inline |

## Workflow

Use the shared library `wiki/etc/experiments/lib/agentic_lit_synthesis.py` (function cheatsheet in [`references/library-api.md`](references/library-api.md)). The Claude subagent running the scan **is Model A** in every two-model cross-check — OpenRouter only pays for Model B (`feedback_subagent_as_model_a.md`).

1. **Scope one question.** Name the load-bearing claims the scan must resolve (evidence tiers, dose numbers, mechanism directions, SAR rules). One scan → one decision.
2. **Workspace.** Create `operations/<scope>-<date>/` for intermediates (fetched sources, translations, query logs). The final artifact goes to `logs/`.
3. **Native-query plan — multilingual by default.** Build with `build_language_native_query_plan(...)`. **Query-framing discipline** (CLAUDE.md §Global-multilingual): query by traditional-formula-name + species-name + traditional-pathology-framing **in addition to** mechanism-name — mechanism-name-only seeding silently misses non-Western literature (canonical: "C3 convertase inhibitor" misses *Houttuynia*; "魚腥草 anti-complementary" catches it). Audit coverage with `audit_query_strategy_language_framing(...)`. Save queries to `inputs/query-strategy.json`.
4. **Fetch.** PubMed via `fetch_pubmed_snapshot(...)`. **East-Asian sources via `local_curl_fetch(...)` — MANDATORY, never fall back to hosted fetch** (hosted/browser fetch bot-blocks these hosts). But `local_curl` reliability **varies by host** (per the 2026-07-14 Houttuynia dogfood): **CQVIP returns genuine server-rendered full text — the most reliable zh host**; **WanFang** is often a JS/Nuxt shell (reached, but no static results); **Baidu Scholar** hits a CAPTCHA wall; **CNKI / ChinaXiv** can fail at the curl layer. So lead with **CQVIP + PubMed**; treat CNKI/WanFang/Baidu as best-effort. Do NOT mislabel a curl-layer bot-wall or CAPTCHA as a "language barrier" — report the exact failing host (canonical miss: 2026-07-13 chronic-tophus scan blamed a bot-wall on language).
5. **Translate (two-model cross-check).** For any non-English source producing a load-bearing claim, `translate_source_two_model(...)` — one Western-vendor, one Chinese-vendor model for Chinese sources — and surface disagreements as **inline annotations**, never silently pick a winner. Escalate disagreements that change an evidence tier / dose / mechanism with `[TRANSLATION-DISAGREEMENT]`. Full protocol: `wiki/etc/manual-literature-mining.md` §"Translation protocol".
6. **Grep-verify before writing.** Every load-bearing number gets verified against its primary source *before* it enters the artifact — the pre-commit verification gate (`manual-literature-mining.md` §"Pre-commit verification gate"). Drop or `[UNVERIFIED]`-tag anything you cannot anchor.
7. **Write + propagate.** Artifact → `logs/<scope>-lit-scan-<date>.md` (see [`references/library-api.md`](references/library-api.md) §"Artifact structure"). Then propagate load-bearing findings to the relevant wiki pages **with evidence-level tags** (Clinical Trial / Animal Model / In Vitro / Mechanistic Extrapolation) and inline provenance `(source: PMID/DOI)`. Cite non-English sources directly with original-language title + English gloss.

## Guards this skill enforces (all cross-referenced, not duplicated)

- **Multilingual by default** — CLAUDE.md §"Global-multilingual research by default". Language is not a barrier; reading a Chinese/Japanese paper is zero marginal cost.
- **`local_curl_fetch()` mandatory for East-Asian sources** — step 4 above.
- **Two-model translation cross-check + inline disagreement annotations** — `manual-literature-mining.md` §"Translation protocol".
- **Primary-source grep-verify gate** — `manual-literature-mining.md` §"Pre-commit verification gate".
- **Corpus-only-pushback → do the work** — a Pass-3 pushback resting only on "not in our corpus" is non-discovery, not refutation; the default is a primary-lit scan (`feedback_do_the_work_not_corpus_only.md`).
- **Do the work, don't cite our own corpus** — never resolve a world-claim by pointing at corpus-absence; go to primary sources (`feedback_do_the_work_not_corpus_only.md`).

## What this skill does NOT do

- **Executable modelling** — structure/sequence/simulation/docking/kinetics → `new-comp-experiment`.
- **The sweep daemon** — this skill produces a lit-scan artifact; the daemon synthesizes the corpus. Different flows.
- **Deciding evidence tiers Brian hasn't approved** — present the verdict; the tier judgment on load-bearing platform claims is Brian's.
