---
title: comp-039 — CFH-dependence mechanism-dissociation of upstream-CP0 candidates
date: 2026-05-21
status: complete (first pass; left uncommitted for Brian's walkthrough review)
---

# comp-039 — CFH-dependence mechanism-dissociation of dietary upstream-CP0 candidates

## Scope

For each top OE candidate from [comp-018](../../wiki/upstream-complement-modulator-sweep-computational.md) and [comp-020](../../wiki/upstream-complement-verification-rerun-computational.md) — rosmarinic acid, luteolin, *Houttuynia cordata* polysaccharide (HCP/HCPM/CHCP), *Helicteres* benzofuran lignans — produce a CFH-dependence classification (CFH-dependent / CFH-independent / mixed) with structural justification, and generate a per-candidate genotype × candidate interaction prediction table that the UK Biobank collaboration (Merriman/Otago, Major-Wrigley/Auckland, Choi/MGH) can test.

The hypothesis under test (from [`complement-c5a-gout.md`](../../wiki/complement-c5a-gout.md) §6.3, added 2026-05-19): the comp-018 / comp-020 dietary candidates inhibit complement *upstream of* where CFH acts (preventing C3 convertase assembly), so Y402H carriers should benefit *more*, not less. The AMD-paradox counter-evidence (Klein 2008 / Awh 2013 / Vavvas 2018 AREDS; Merle 2015 DHA) is hypothesized to apply only to interventions that work *through* CFH-CRP-bridging.

## Candidates

| Candidate | Source | Key reference |
|---|---|---|
| Rosmarinic acid | rosemary, lemon balm, perilla | Sahu 1999 PMID 10353266 (C3b thioester covalent attachment, IC50 34 μM) |
| Luteolin | celery, parsley, chamomile | Zhang 2008 PMID 18400428 / PMC7126446 (CH50 0.19 mM, AP50 0.17 mM) |
| Houttuynia cordata polysaccharide (HCP/HCPM/CHCP) | fish-mint / 鱼腥草 / どくだみ / diếp cá | Lu 2018 PMID 29719782 / PMC5925397 (C3+C4 depletion-rescue mapping) |
| Helicteres benzofuran lignans | *Helicteres angustifolia* (tropical Sterculiaceae) | Yin 2016 PMID 27834928 / PMC6273495 (CH50 9/40 μM, C1q+C2+C3+C4+C9 targeting) |

## Status

| Step | Status |
|---|---|
| Background corpus read (gout-genetic-variants Category 5, complement-c5a-gout §6.3, comp-018, comp-020, biobank log) | Complete |
| UniProt P08603 (CFH) Sushi-domain structural lookup — Sushi 7 = aa 387-444 grep-verified | Complete |
| Per-candidate multi-frame query plan built | Complete (audit `needs_revision` only because isolated compounds have no traditional formula — expected and recorded as provenance) |
| Retrieval probes (East Asian academic sources reachability) | Complete (81/84 ok across 4 candidates) |
| PubMed snapshot for Western mechanism queries | Complete (rosmarinic 13 records, luteolin 6, Houttuynia 12, Helicteres 7) |
| Primary-source full-text reads (Model A — Claude Opus 4.7) | Complete (PMC7126446 luteolin, PMC6273495 Helicteres, PMC5925397 Lu 2018 Houttuynia, PMC7127486 Xu 2015 Houttuynia, PubMed abstracts for Sahu/Englberger/Peake/Tian) |
| Two-model cross-check (Model B = DeepSeek `deepseek/deepseek-chat-v3` via OpenRouter) | Complete (all 4 candidates) |
| Two-model annotated cross-check markdowns | Complete |
| comp-039 wiki page authored | Complete |
| `computational-experiments.md` index updated | Complete |
| Git commit | **Not done — brief instructs leave dirty for Brian's review** |

## Artifacts

### Inputs

- [`inputs/per-candidate-query-plan.json`](./inputs/per-candidate-query-plan.json) — multi-frame query plans per candidate, with `audit_query_strategy_language_framing` verdict per candidate (verdict = `needs_revision` for all four only because isolated compounds have no traditional-formula frame — expected and recorded as provenance, not a real gap)
- [`inputs/build_query_plan.py`](./inputs/build_query_plan.py) — query plan builder
- [`inputs/run_retrieval.py`](./inputs/run_retrieval.py) — PubMed snapshot + East Asian reachability probe driver
- [`inputs/run_deepseek_counterread.py`](./inputs/run_deepseek_counterread.py) — Model B (DeepSeek) counter-read driver, OpenRouter via curl to bypass Python 3.13 cert-bundle issue

### Outputs

- [`outputs/retrieval-probes.json`](./outputs/retrieval-probes.json) — East Asian source reachability per query (81/84 ok)
- [`outputs/<candidate>-pubmed-snapshot.json`](./outputs/) — Western-frame PubMed snapshot per candidate
- [`outputs/<candidate>-source-read-2026-05-21.md`](./outputs/) — Model A (Claude Opus 4.7) primary-source reads per candidate
- [`outputs/<candidate>-deepseek-counterread-2026-05-21.json`](./outputs/) — Model B (DeepSeek) independent counter-reads per candidate
- [`outputs/<candidate>-two-model-annotated-2026-05-21.md`](./outputs/) — annotated cross-check markdowns with `[TRANSLATION-DISAGREEMENT]` inline annotations
- [`outputs/retrieval-probes-raw/`](./outputs/retrieval-probes-raw/) — raw HTML + provenance JSON for East Asian source probes

## Key findings (TL;DR — see [comp-039 wiki page](../../wiki/cfh-mechanism-dissociation-cp0-candidates-computational.md) for full analysis)

| Candidate | CFH-dependence | Confidence | Model A Y402H direction | Model B Y402H direction |
|---|---|---|---|---|
| Rosmarinic acid | CFH-independent | High | negative (effect ≥ in carriers) | null |
| Luteolin | CFH-independent | Medium | negative (effect ≥ in carriers, with multi-mode confound) | null |
| HCP / HCPM / CHCP | CFH-independent | High | negative, possibly notably greater (dual CP0+CP1) | null |
| Helicteres benzofuran lignans | CFH-independent | Medium (replication-bounded) | negative (wide uncertainty bands; non-dietary) | null |

**Consensus:** all four CFH-independent. **Two-model disagreement on Y402H direction:** Model A predicts negative (Y402H baseline severity amplifies absolute effect size); Model B predicts null (mechanism independence implies genotype indifference). Both reject the AMD-paradox direction. UKB cross-tab needs to pre-specify falsification thresholds for both negative and null directions.

## Decisions

- **Operations workspace shape:** modeled on [`operations/global-lit-scan-p0-remediation-2026-05-20/`](../global-lit-scan-p0-remediation-2026-05-20/) — `inputs/` for query plans + driver scripts, `outputs/` for source reads + counter-reads + annotated cross-checks + raw probe HTML, README at the workspace root with status table + artifact index.
- **Model B vendor choice:** DeepSeek (Chinese-vendor, native-Chinese training depth) chosen for all four candidates per CLAUDE.md §"Translation protocol" — even though only Houttuynia + Helicteres have Chinese-language source material, the cross-vendor heterogeneity guard benefits the rosmarinic-acid and luteolin reads too.
- **Wiki page status:** authored at [`wiki/cfh-mechanism-dissociation-cp0-candidates-computational.md`](../../wiki/cfh-mechanism-dissociation-cp0-candidates-computational.md). [`gout-genetic-variants.md`](../../wiki/gout-genetic-variants.md) Category 5 CFH row and [`complement-c5a-gout.md`](../../wiki/complement-c5a-gout.md) §6.3 are NOT edited until Brian reviews — per the brief.
- **No commit/push:** per the brief, all artifacts left in dirty working tree for Brian's review.

## Cross-references

- [comp-039 interpretive wiki page](../../wiki/cfh-mechanism-dissociation-cp0-candidates-computational.md)
- [comp-018 — upstream-complement modulator sweep](../../wiki/upstream-complement-modulator-sweep-computational.md)
- [comp-020 — upstream-complement verification rerun](../../wiki/upstream-complement-verification-rerun-computational.md)
- [`gout-genetic-variants.md`](../../wiki/gout-genetic-variants.md) Category 5 CFH row (canonical; comp-039 informs but does not edit)
- [`complement-c5a-gout.md`](../../wiki/complement-c5a-gout.md) §6.3 (canonical; comp-039 informs but does not edit)
- [`logs/cfh-y402h-dietary-cp0-biobank-mining-2026-05-19.md`](../../logs/cfh-y402h-dietary-cp0-biobank-mining-2026-05-19.md) — biobank feasibility analysis
