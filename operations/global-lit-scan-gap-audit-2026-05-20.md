---
title: "Global Literature Scan Gap Audit — Firewall + Native-Query Remediation"
date: 2026-05-20
status: active
tags: [operations, literature-scan, multilingual, cnki, wanfang, query-framing, firewall, audit]
related:
  - ../logs/lit-scan-query-framing-retrospective-audit-2026-05-19.md
  - ../wiki/etc/experiments/lib/agentic_lit_synthesis.py
  - ../CLAUDE.md
  - ../.claude/skills/new-comp-experiment/SKILL.md
---

# Global Literature Scan Gap Audit — Firewall + Native-Query Remediation

## Why This Exists

On 2026-05-20 we confirmed a second failure mode behind the already-documented multilingual coverage gap: Brian's firewall had been blocking China access, and hosted model fetches can egress from vendor infrastructure rather than Brian's laptop. That means prior "global" scans may have failed in two different ways:

1. **Network path failure:** Chinese academic domains were unreachable or intermittently blocked, so scans fell back to abstracts, PubMed-indexed English papers, or no full text.
2. **Query-framing failure:** English mechanism-name queries do not map cleanly to Chinese / Japanese / Korean corpora. Native corpus searches need native mechanism terms, species/common names, formula names, and traditional pathology framing.

The 2026-05-19 retrospective already diagnosed the query-framing side. This audit adds the firewall/network-path consequence and turns the combined diagnosis into a priority queue.

## Operational Fix Now in Shared Library

[`wiki/etc/experiments/lib/agentic_lit_synthesis.py`](../wiki/etc/experiments/lib/agentic_lit_synthesis.py) now carries three distinct pieces of discipline:

| Failure mode | Library support |
|---|---|
| Hosted model/web fetch exits from vendor servers and misses Brian's firewall allowlist | `local_curl_fetch()` uses laptop-local `curl` with an explicit East Asian academic allowlist and provenance sidecar. |
| Non-English source text needs cross-vendor translation | `translate_source_two_model()` runs two independent translations and preserves science-relevant disagreements inline. |
| English mechanism queries return false-zero results in non-English corpora | `build_language_native_query_plan()` and `audit_query_strategy_language_framing()` require native mechanism + species + formula + pathology frames for natural-product / traditional-medicine scans. |

The rule is not "translate English query into Chinese." The rule is: **query the corpus the way that corpus names the biology.**

## Priority Queue

### P0 — Highest Leverage / Most Likely Missing Load-Bearing Information

1. **comp-014 medicinal-mushroom Phase 5b deep dive**
   - Why: comp-014 explicitly queued CNKI / J-STAGE / KISS follow-ups; China/Japan/Korea source access is load-bearing for Ganoderma, Cordyceps, Trametes, Inonotus/Sanghuang, and GLPP cultivation/fractionation.
   - Native query anchors: `灵芝 多糖肽 分离纯化`, `菌草 灵芝 栽培`, `桑黄 黄嘌呤氧化酶`, `冬虫夏草 腺苷脱氨酶`, `霊芝 高尿酸血症`, `マイタケ グリフォラン 炎症`.
   - Expected wiki impact: medicinal-mushroom complement track, GLPP SOPs, NLRP3 exploit map, cordycepin/ADA pairing, quantification / cultivation SOPs.

2. **East Asian gout-genetics cohort scan**
   - Why: Q141K / HLA-B*58:01 / URAT1 W258X have the highest relevance in East Asian populations, and the wiki currently leans heavily on English-indexed cohort data.
   - Native query anchors: `ABCG2 Q141K 痛风`, `rs2231142 高尿酸血症`, `HLA-B*58:01 别嘌醇 严重皮肤不良反应`, `URAT1 W258X 日本 痛風`, `高尿酸血症 遗传 多态性`.
   - Expected wiki impact: gout-genetic-variants, ABCG2 modulators, genotype-informed supplement workflow, East Asian cohort/RCT design.

3. **TCM gout formula re-scan**
   - Why: comp-013 had partial formula/species anchoring, but the retrospective still found likely gaps around formula-level evidence and non-canonical components.
   - Native query anchors: `四妙散 高尿酸血症 URAT1`, `白虎加桂枝汤 痛风`, `土茯苓 高尿酸血症`, `姜黄 黄嘌呤氧化酶`, `乌梅丸 高尿酸血症`.
   - Expected wiki impact: TCM gout compound triage, H04, modality/chokepoint matrix, URAT1/XO/NLRP3 pages.

4. **NLRP3 × Lingzhi / Yun Zhi / Maitake immunomodulation**
   - Why: comp-014 and the 2026-05-19 retrospective both flag that ChEMBL/PubMed mechanism-name coverage undercounts polysaccharide / spore-powder evidence.
   - Native query anchors: `灵芝孢子粉 NLRP3 炎症小体`, `云芝多糖肽 NLRP3`, `舞茸 グリフォラン NLRP3`, `PSK インフラマソーム`.
   - Expected wiki impact: NLRP3 exploit map, medicinal mushroom complement track, mushroom extract SOP prioritization.

### P1 — Important, But Less Likely To Flip Near-Term Decisions

5. **Houttuynia / Tibetan complement-modulator protocol deepening**
   - Why: the mechanism gap was already corrected by comp-018 Phase 2, but CNKI/WanFang may hold extraction, QC, and industrial-process details.
   - Native query anchors: `鱼腥草 抗补体 多糖`, `鱼腥草 C3转化酶`, Tibetan species names from comp-018 Phase 2.
   - Expected wiki impact: upstream complement modulator pages and Houttuynia CP1/CP0 follow-up protocols.

6. **Cordyceps × ADA / mitophagy deepening**
   - Why: ADA became a first-class chokepoint through species-name reading; Chinese/Korean/Japanese corpora may refine cordycepin + pentostatin + Cordyceps cicadae mechanism.
   - Native query anchors: `蛹虫草 腺苷脱氨酶`, `虫草素 ADA`, `冬虫夏草 线粒体自噬`, `Cordyceps cicadae PINK1`.
   - Expected wiki impact: cordycepin route, ADA-challenge validation experiments, medicinal-mushroom track.

7. **Mushroom × HDAC / HDAC6 Q141K rescue candidates**
   - Why: comp-007 was intentionally Western-food-grade; TCM-grade mushroom compounds could matter if Q141K rescue expands beyond GRAS-first candidates.
   - Native query anchors: `灵芝三萜 HDAC6`, `桑黄 组蛋白去乙酰化酶`, `蘑菇 HDAC 抑制剂`.
   - Expected wiki impact: food-grade HDACi screen follow-up, ABCG2 Q141K rescue, chassis-pending interventions.

### P2 — Track, But Do Not Spend First

8. **T-axis adjuvant Chinese primary literature**
   - Why: comp-015 flagged no Chinese-language primary literature access for icariin / echinacoside / cordycepin related mechanisms.
   - Expected wiki impact: T-axis adjuvant mapping; likely refinement rather than platform flip.

9. **Testosterone × intestinal ABCG2 multilingual re-check**
   - Why: comp-016 flagged CNKI/J-STAGE/KISS as not executed, but this field is likely Western pharma-DMPK dominated.
   - Expected wiki impact: low to medium.

10. **Western pharma / engineering comp-NNN re-checks**
   - Why: sequence engineering, mRNA, LNP, disulfiram, and ALLN-346/PRX-115 analyses are not likely to be changed by traditional-language query frames.
   - Expected wiki impact: low.

## Audit Protocol For Each Re-Scan

1. Build an `inputs/query-strategy.json` with `build_language_native_query_plan()`.
2. Run `audit_query_strategy_language_framing()` and fail/warn if native frames are missing.
3. Fetch Chinese / East Asian source pages using `local_curl_fetch()` when domains are firewall-sensitive.
4. For non-English full text, run `translate_source_two_model()` with one native-language-strong model where possible.
5. Promote only grep/source-verified load-bearing claims into wiki pages; annotate translation disagreements inline when they affect science.

## Canonical Sources For This Audit

- [`logs/lit-scan-query-framing-retrospective-audit-2026-05-19.md`](../logs/lit-scan-query-framing-retrospective-audit-2026-05-19.md) — original query-framing retrospective and priority list.
- [`CLAUDE.md` §Global-multilingual research by default](../CLAUDE.md) — repo-wide rule.
- [`.claude/skills/new-comp-experiment/SKILL.md`](../.claude/skills/new-comp-experiment/SKILL.md) — comp-NNN query-strategy discipline.
- [`wiki/etc/experiments/lib/agentic_lit_synthesis.py`](../wiki/etc/experiments/lib/agentic_lit_synthesis.py) — shared helper that now encodes network-path, translation, and native-query guardrails.
