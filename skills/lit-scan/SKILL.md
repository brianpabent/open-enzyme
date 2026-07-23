---
name: lit-scan
description: 'Run a literature/evidence-synthesis scan — search, curate, and synthesize primary sources into canonical wiki updates plus a compact method receipt — as opposed to a computational experiment (comp-NNN). Use when a wiki question needs "what does the field say" rather than code producing deterministic outputs: a compound''s evidence tier, a mechanism''s support, a structure-activity relationship, a clinical-landscape read, or resolving a corpus-only-pushback via primary sources. Multilingual by default (Chinese CNKI/WanFang, Japanese J-STAGE, Korean KISS via local_curl_fetch) with two-model translation cross-check. Invoke when Brian says "run a lit scan", "do the work", "what does the literature say", or when a Pass-3 pushback rests only on corpus-absence. NOT for structure/sequence/simulation/docking — that is new-comp-experiment.'
---

# lit-scan

A lit scan searches, curates, and synthesizes primary literature into a **cited canonical evidence update**. It is the counterpart to a `comp-NNN`: a comp runs **code that produces deterministic outputs** (structure / sequence / simulation / docking); a lit scan produces an **evidence synthesis**. Their risks — and therefore their guards — differ. The wiki retains the current synthesis; a transient workspace supports the scan; Git retains its history.

## COMP vs lit-scan — which artifact is this?

| | lit-scan (this skill) | comp-NNN (`new-comp-experiment`) |
|---|---|---|
| **Work** | search → curate → synthesize literature | run code → deterministic output |
| **Output** | cited canonical wiki update + compact method receipt | committed code/inputs/outputs |
| **Risk** | search-completeness, over-claim, translation nuance | model/code correctness |
| **Guard** | multilingual framing + two-model translation + primary-source grep-verify | full lifecycle adversarial-code-review gate |
| **Home** | canonical `wiki/` page(s) + `logs/lit-scans/<scope>-<date>.json`; transient `operations/<scope>-<date>/` workspace | `wiki/etc/experiments/comp-NNN/` |

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
2. **Workspace.** Create `operations/<scope>-<date>/` for uncommitted intermediates (fetched sources, translations, query logs). This directory is disposable working state, not a repository artifact. Plan a compact method receipt at `logs/lit-scans/<scope>-<date>.json`.
3. **Native-query plan — multilingual by default.** Build with `build_language_native_query_plan(...)`. **Query-framing discipline** (CLAUDE.md §Global-multilingual): query by traditional-formula-name + species-name + traditional-pathology-framing **in addition to** mechanism-name — mechanism-name-only seeding silently misses non-Western literature (canonical: "C3 convertase inhibitor" misses *Houttuynia*; "魚腥草 anti-complementary" catches it). Audit coverage with `audit_query_strategy_language_framing(...)`. Save queries to `inputs/query-strategy.json`.
4. **Fetch.** PubMed via `fetch_pubmed_snapshot(...)`. **East-Asian sources via `local_curl_fetch(...)` — MANDATORY, never fall back to hosted fetch** (hosted/browser fetch bot-blocks these hosts). But `local_curl` reliability **varies by host** (per the 2026-07-14 Houttuynia dogfood): **CQVIP returns genuine server-rendered full text — the most reliable zh host**; **WanFang** is often a JS/Nuxt shell (reached, but no static results); **Baidu Scholar** hits a CAPTCHA wall; **CNKI / ChinaXiv** can fail at the curl layer. So lead with **CQVIP + PubMed**; treat CNKI/WanFang/Baidu as best-effort. Do NOT mislabel a curl-layer bot-wall or CAPTCHA as a "language barrier" — report the exact failing host (canonical miss: 2026-07-13 chronic-tophus scan blamed a bot-wall on language).
5. **Translate (two-model cross-check).** For any non-English source producing a load-bearing claim, `translate_source_two_model(...)` — one Western-vendor, one Chinese-vendor model for Chinese sources — and surface disagreements as **inline annotations**, never silently pick a winner. Escalate disagreements that change an evidence tier / dose / mechanism with `[TRANSLATION-DISAGREEMENT]`. Full protocol: `wiki/etc/manual-literature-mining.md` §"Translation protocol".
6. **Grep-verify before writing.** Every load-bearing number gets verified against its primary source *before* it enters the artifact — the pre-commit verification gate (`manual-literature-mining.md` §"Pre-commit verification gate"). Drop or `[UNVERIFIED]`-tag anything you cannot anchor.
7. **Write in place.** Update the canonical evidence page(s) directly using the structure in [`references/library-api.md`](references/library-api.md) §"Canonical evidence update". Use evidence-level tags (Clinical Trial / Animal Model / In Vitro / Mechanistic Extrapolation) and inline provenance `(source: PMID/DOI)`. A focused page must lead with the gout weakness, then evidence, source, delivery, exposure constraints, and falsification; cross-track comparisons belong only in portfolio comparison surfaces. Cite non-English sources directly with original-language title + English gloss. Dependents get only the local decision delta and a link.
   - Audit claims and ideas separately. Correct unsupported factual wording, but do not delete a useful connection merely because the scan found no direct study. If its premises remain grounded, preserve it as a compact **Research Conjecture** on the mechanism-owning page: evidence-tagged premises, explicit unsupported leap, upside, and a discriminating observation. “No study found in this bounded search” is not falsification.
8. **Record method, then clean up.** Write and validate the compact receipt described in [`references/library-api.md`](references/library-api.md) §"Method receipt". It must retain the exact queries, sources/databases attempted, result counts, fetch/translation failures, source identifiers considered, translation disagreements, verification status, limitations, and canonical pages changed. It must not duplicate the findings narrative or verdict from the wiki. Run `python3 scripts/check-lit-scan-receipt.py logs/lit-scans/<scope>-<date>.json`, then delete the transient workspace. Do not commit fetched documents, model transcripts, or a second prose synthesis under `logs/` or `operations/`.

## Guards this skill enforces (all cross-referenced, not duplicated)

- **Multilingual by default** — CLAUDE.md §"Global-multilingual research by default". Language is not a barrier; reading a Chinese/Japanese paper is zero marginal cost.
- **`local_curl_fetch()` mandatory for East-Asian sources** — step 4 above.
- **Two-model translation cross-check + inline disagreement annotations** — `manual-literature-mining.md` §"Translation protocol".
- **Primary-source grep-verify gate** — `manual-literature-mining.md` §"Pre-commit verification gate".
- **Compact reproducibility receipt** — exact search coverage and faults go in `logs/lit-scans/*.json`; scientific findings live only in canonical wiki pages. Receipts are excluded from full-corpus synthesis.
- **Corpus-only-pushback → do the work** — a Pass-3 pushback resting only on "not in our corpus" is non-discovery, not refutation; the default is a primary-lit scan (`feedback_do_the_work_not_corpus_only.md`).
- **Do the work, don't cite our own corpus** — never resolve a world-claim by pointing at corpus-absence; go to primary sources (`feedback_do_the_work_not_corpus_only.md`).
- **Claim/conjecture separation** — Research Conjecture is an epistemic status, not an evidence tier. A bounded search can weaken a premise or bound a gap; absence of a direct hit alone does not kill a grounded lead.

## What this skill does NOT do

- **Executable modelling** — structure/sequence/simulation/docking/kinetics → `new-comp-experiment`.
- **The sweep daemon** — this skill updates current evidence in the corpus; the daemon searches the complete corpus for novel connections. Different flows.
- **Deciding evidence tiers Brian hasn't approved** — present the verdict; the tier judgment on load-bearing platform claims is Brian's.
