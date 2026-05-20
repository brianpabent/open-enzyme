---
title: Global lit scan P0 remediation
date: 2026-05-20
status: active
---

# Global lit scan P0 remediation

This folder is the first remediation pass after discovering two coupled failure modes in prior global literature scans:

1. China-focused sources were often not reachable through hosted model/browser fetch paths because those requests egressed from vendor infrastructure rather than Brian's whitelisted laptop network.
2. Non-English searches were sometimes framed as direct translations of Western mechanism queries instead of using native-language species, formula, and traditional-pathology terms.

The goal here is not to write new wiki claims yet. This pass creates query plans, proves which source routes actually work from the local network, and identifies the first scans worth running deeply with the two-model translation protocol.

## P0 Worklist

| Item | Question | Current status | Next action |
|---|---|---|---|
| P0-1 | Medicinal mushroom / comp-014 Phase 5b rescue scan | CNKI Overseas rerun and abstract-level two-model read complete; Cordyceps militaris and Sanghuang/Phellinus are the strongest recovered urate leads | Retrieve/read full text for priority Cordyceps and Sanghuang/Phellinus records before wiki evidence update |
| P0-2 | East Asian gout genetics: ABCG2 Q141K, HLA-B*58:01, URAT1/W258X | Query plan adequate; J-STAGE local-curl route has strong immediate yield; CNKI Overseas route corrected | Run first deep dive here |
| P0-3 | TCM gout formula re-scan | Query plan adequate; WanFang reachable but SPA extraction unresolved; CNKI Overseas route corrected; Baidu captcha | Needs CNKI/WanFang result extraction before evidence update |
| P0-4 | NLRP3 x Lingzhi/Yun Zhi/Maitake immunomodulation | Query plan adequate; J-STAGE returns fungal beta-glucan immunology reviews; RISS route reachable; CNKI Overseas route corrected | Run after P0-2, with explicit "not gout-specific yet" guardrail |

## Artifacts

- [`inputs/p0-1-medicinal-mushroom-phase-5b-query-plan.json`](./inputs/p0-1-medicinal-mushroom-phase-5b-query-plan.json)
- [`inputs/p0-2-east-asian-gout-genetics-query-plan.json`](./inputs/p0-2-east-asian-gout-genetics-query-plan.json)
- [`inputs/p0-3-tcm-gout-formula-rescan-query-plan.json`](./inputs/p0-3-tcm-gout-formula-rescan-query-plan.json)
- [`inputs/p0-4-nlrp3-mushroom-immunomodulation-query-plan.json`](./inputs/p0-4-nlrp3-mushroom-immunomodulation-query-plan.json)
- [`outputs/retrieval-probes.json`](./outputs/retrieval-probes.json) - source reachability probes via local curl.
- [`outputs/jstage-extracted-results.json`](./outputs/jstage-extracted-results.json) - parsed J-STAGE search/article metadata from the successful probes.
- [`outputs/cnki-oversea-route-correction.json`](./outputs/cnki-oversea-route-correction.json) - corrected CNKI Overseas route probes after `kns.cnki.net` / `www.cnki.net` cert mismatch diagnosis.
- [`outputs/p0-1-cnki-overseas-rerun-2026-05-20.json`](./outputs/p0-1-cnki-overseas-rerun-2026-05-20.json) - focused P0-1 CNKI Overseas query counts and top result records.
- [`outputs/p0-1-cnki-lead-articles-2026-05-20.json`](./outputs/p0-1-cnki-lead-articles-2026-05-20.json) - fetched article-page provenance for high-signal P0-1 lead records.
- [`outputs/p0-1-cnki-rerun-summary-2026-05-20.md`](./outputs/p0-1-cnki-rerun-summary-2026-05-20.md) - human-readable P0-1 rerun summary and next-read list.
- [`outputs/p0-1-cnki-lead-abstract-records-2026-05-20.json`](./outputs/p0-1-cnki-lead-abstract-records-2026-05-20.json) - parsed abstract/keyword records for the nine highest-priority CNKI leads.
- [`outputs/p0-1-cnki-deepseek-counterread-2026-05-20.json`](./outputs/p0-1-cnki-deepseek-counterread-2026-05-20.json) - native-Chinese DeepSeek counter-read over the parsed abstract records.
- [`outputs/p0-1-cnki-two-model-source-read-2026-05-20.md`](./outputs/p0-1-cnki-two-model-source-read-2026-05-20.md) - Codex/GPT-5.5 plus DeepSeek conservative source-read summary.
- [`outputs/p0-1-cordyceps-biotech-source-read-2026-05-20.md`](./outputs/p0-1-cordyceps-biotech-source-read-2026-05-20.md) - publisher-page read of the priority *C. militaris* water-extract rat paper; promotes this one from abstract lead to Animal Model wiki-update candidate.
- [`outputs/p0-1-cordyceps-biotech-deepseek-counterread-2026-05-20.json`](./outputs/p0-1-cordyceps-biotech-deepseek-counterread-2026-05-20.json) - native-Chinese counter-read for the publisher-page source facts.
- `outputs/retrieval-probes-raw/` - raw HTML/provenance files. Provenance records when a fetch used local curl and whether insecure TLS was required.

## Retrieval Findings

**J-STAGE works via local curl.** The P0-2 probe `URAT1 W258X 痛風` returned `4,903件中 1-20の結果を表示しています` and included directly relevant urate-transporter/gout genetics records, including:

- `URAT1/SLC22A12遺伝子の機能消失型変異が血清尿酸値および痛風・高尿酸血症の発症に与える影響` ([J-STAGE](https://www.jstage.jst.go.jp/article/gnam/41/1/41_143/_article/-char/ja), DOI `10.6032/gnam.41.143`)
- `腎性低尿酸血症3例における尿酸トランスポーター(URAT1)遺伝子異常の解析` ([J-STAGE](https://www.jstage.jst.go.jp/article/gnam1999/28/2/28_115/_article/-char/ja), DOI `10.6032/gnam1999.28.2_115`)

**P0-4 has useful mechanism background but not yet gout-specific evidence.** The `マイタケ グリフォラン 炎症` probe returned fungal beta-glucan structure/innate-immunity reviews, including `真菌βグルカンと生体防御` ([J-STAGE](https://www.jstage.jst.go.jp/article/yakushi/141/5/141_20-00245/_article/-char/ja), DOI `10.1248/yakushi.20-00245`). Treat these as immunology/background leads until a gout, urate, NLRP3, or MSU-linked source is found.

**WanFang is reachable but not yet extractable.** Local curl returns HTTP 200 for WanFang search pages, but the fetched HTML appears to be an application shell and does not contain query terms or result records. Next remediation is an API/browser extraction path, not more static curl.

**CNKI route corrected.** The original `kns.cnki.net` / `www.cnki.net` probes were the wrong path from this network: those hosts CNAME through `oversea.cnki.net.eo.dnse2.com` and present a non-CNKI `*.cdn.myqcloud.com` certificate, then return HTTP 418 when TLS verification is bypassed. The valid-cert entrypoint is [`https://cnki.net/index/`](https://cnki.net/index/), whose page source points search to `https://oversea.cnki.net/kns8s/defaultresult/index?kw=...`. Re-running the four CNKI probes through `oversea.cnki.net` returns HTTP 200 and includes the query terms in the HTML. Result records are still loaded into `#ModuleSearchResult` via JavaScript/API, so the remaining task is result extraction, not domain reachability.

**CNKI AI may be a useful triage surface, not a citable source.** CNKI Overseas advertises [`CNKI AI`](https://oversea.cnki.net/index/second/cnkiai/en/homepage.html) as an AI research tool over CNKI's 380 million-paper corpus, with multilingual Q&A/translation, traceable answers, paper snapshots, citation generation, and a `Try It Now` entrypoint at `https://ai.oversea.cnki.net/inds/aigc?sysid=4&lang=en`. This is operationally noteworthy because it may expose a CNKI-native discovery path for Chinese literature that ordinary static curl does not. Treat it as a lead generator only: any CNKI AI answer must be traced back to original CNKI records/full text and then read with the two-model translation protocol before it can affect wiki evidence tiers.

**P0-1 CNKI rerun is now positive.** The corrected CNKI route plus direct `/kns8s/brief/grid` extraction recovered meaningful medicinal-mushroom urate leads. Focused query counts included `灵芝 多糖肽 分离纯化` (39), `灵芝 高尿酸血症` (7), `桑黄 高尿酸血症` (28), `桑黄 黄嘌呤氧化酶` (10), `蛹虫草 高尿酸血症` (12), and cultivation/substrate queries `菌草 灵芝 栽培` (95) / `菌草 灵芝 多糖` (86). A Codex/GPT-5.5 plus DeepSeek abstract-level read ranks Cordyceps militaris first, Sanghuang/Phellinus second, and Ganoderma third for follow-up. Treat this as a discovery-positive result that needs full-text reading, not as a final evidence-tier change.

**CNKI full text is not yet script-retrievable from curl.** Article detail pages expose HTML/PDF/CAJ order links, but local curl against those order endpoints redirects to CNKI Overseas login pages. The P0-1 two-model pass is therefore an abstract-level source read. Any wiki evidence-tier update still requires full text, preferably obtained through browser/manual CNKI access or another legitimate full-text route, then read with two independent models.

**Baidu/Baidu Scholar is not usable through simple curl.** Baidu redirects to `百度安全验证` captcha pages. Treat Baidu as manual/browser-only unless a compliant API/source route is identified.

## Decision

Run P0-2 first. It has a working retrieval path, directly relevant native-language hits, and likely affects the OE gout genetics / trial-stratification understanding more immediately than the mushroom and TCM scans. Use two independent model readings for any Japanese source text that changes a scientific conclusion, and annotate translation disagreements inline rather than collapsing them.
