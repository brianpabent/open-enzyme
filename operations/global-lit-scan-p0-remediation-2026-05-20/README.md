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
| P0-1 | Medicinal mushroom / comp-014 Phase 5b rescue scan | Query plan adequate; J-STAGE exact `霊芝 高尿酸血症` probe weak; WanFang reachable but SPA extraction unresolved; CNKI search blocked | Re-run through WanFang extraction or authenticated/browser CNKI path before treating as negative |
| P0-2 | East Asian gout genetics: ABCG2 Q141K, HLA-B*58:01, URAT1/W258X | Query plan adequate; J-STAGE local-curl route has strong immediate yield | Run first deep dive here |
| P0-3 | TCM gout formula re-scan | Query plan adequate; WanFang reachable but SPA extraction unresolved; CNKI search blocked; Baidu captcha | Needs China-source access workaround before evidence update |
| P0-4 | NLRP3 x Lingzhi/Yun Zhi/Maitake immunomodulation | Query plan adequate; J-STAGE returns fungal beta-glucan immunology reviews; RISS route reachable | Run after P0-2, with explicit "not gout-specific yet" guardrail |

## Artifacts

- [`inputs/p0-1-medicinal-mushroom-phase-5b-query-plan.json`](./inputs/p0-1-medicinal-mushroom-phase-5b-query-plan.json)
- [`inputs/p0-2-east-asian-gout-genetics-query-plan.json`](./inputs/p0-2-east-asian-gout-genetics-query-plan.json)
- [`inputs/p0-3-tcm-gout-formula-rescan-query-plan.json`](./inputs/p0-3-tcm-gout-formula-rescan-query-plan.json)
- [`inputs/p0-4-nlrp3-mushroom-immunomodulation-query-plan.json`](./inputs/p0-4-nlrp3-mushroom-immunomodulation-query-plan.json)
- [`outputs/retrieval-probes.json`](./outputs/retrieval-probes.json) - source reachability probes via local curl.
- [`outputs/jstage-extracted-results.json`](./outputs/jstage-extracted-results.json) - parsed J-STAGE search/article metadata from the successful probes.
- `outputs/retrieval-probes-raw/` - raw HTML/provenance files. Provenance records when a fetch used local curl and whether insecure TLS was required.

## Retrieval Findings

**J-STAGE works via local curl.** The P0-2 probe `URAT1 W258X 痛風` returned `4,903件中 1-20の結果を表示しています` and included directly relevant urate-transporter/gout genetics records, including:

- `URAT1/SLC22A12遺伝子の機能消失型変異が血清尿酸値および痛風・高尿酸血症の発症に与える影響` ([J-STAGE](https://www.jstage.jst.go.jp/article/gnam/41/1/41_143/_article/-char/ja), DOI `10.6032/gnam.41.143`)
- `腎性低尿酸血症3例における尿酸トランスポーター(URAT1)遺伝子異常の解析` ([J-STAGE](https://www.jstage.jst.go.jp/article/gnam1999/28/2/28_115/_article/-char/ja), DOI `10.6032/gnam1999.28.2_115`)

**P0-4 has useful mechanism background but not yet gout-specific evidence.** The `マイタケ グリフォラン 炎症` probe returned fungal beta-glucan structure/innate-immunity reviews, including `真菌βグルカンと生体防御` ([J-STAGE](https://www.jstage.jst.go.jp/article/yakushi/141/5/141_20-00245/_article/-char/ja), DOI `10.1248/yakushi.20-00245`). Treat these as immunology/background leads until a gout, urate, NLRP3, or MSU-linked source is found.

**WanFang is reachable but not yet extractable.** Local curl returns HTTP 200 for WanFang search pages, but the fetched HTML appears to be an application shell and does not contain query terms or result records. Next remediation is an API/browser extraction path, not more static curl.

**CNKI search is still not solved.** `kns.cnki.net` search URLs fail TLS hostname validation through normal curl and return HTTP 418 even when retried with explicit insecure TLS. Provenance files capture this. `allow_insecure_tls` exists only to document and test that specific failure mode; it is not a scientific-data retrieval success path.

**Baidu/Baidu Scholar is not usable through simple curl.** Baidu redirects to `百度安全验证` captcha pages. Treat Baidu as manual/browser-only unless a compliant API/source route is identified.

## Decision

Run P0-2 first. It has a working retrieval path, directly relevant native-language hits, and likely affects the OE gout genetics / trial-stratification understanding more immediately than the mushroom and TCM scans. Use two independent model readings for any Japanese source text that changes a scientific conclusion, and annotate translation disagreements inline rather than collapsing them.
