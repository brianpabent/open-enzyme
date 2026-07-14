---
title: "Sulforaphane lit scan — Track C (East Asian multilingual: Chinese / Japanese / Korean)"
date: 2026-07-14
scope: "SFN for gout / hyperuricemia / NLRP3 inflammation — zh/ja/ko corpus"
track: C
tags: [sulforaphane, hyperuricemia, gout, NLRP3, multilingual, east-asian, lit-scan]
---

# Track C — East Asian multilingual scan (sulforaphane × gout / hyperuricemia / NLRP3)

**Bottom line:** The strongest in-vivo SFN-gout evidence worldwide is East-Asian-authored. Two mouse gouty-inflammation studies (Korean) and one gut-microbiome/urate study (Chinese, Peking) are PubMed-indexed with English abstracts, so a naive PubMed-English scan *does* find them — but the Chinese-language corpus (via CQVIP) adds at least one mechanism angle absent from Western literature: SFN protecting **renal tubular epithelial cells from urate-induced ER-stress apoptosis** (IRE-1/JNK). The Japanese functional-food SFN base is large (132 J-STAGE records) but oriented to psychiatry/cancer/detox, **not** urate — a real absence, not a retrieval gap. Korean-only databases add nothing beyond the PubMed-indexed papers.

---

## 1. Retrieval-probe summary (which sources were reachable)

Full machine record: [`retrieval-probes.json`](./retrieval-probes.json).

| Source | Reachable? | Method | Note |
|---|---|---|---|
| **CQVIP** (cqvip.com/search) | ✅ **yes** | local curl | SSR HTML with full Chinese abstracts embedded in Nuxt payload. **Primary Chinese workhorse.** 204× 萝卜硫素, 58× 尿酸, 12× 高尿酸 in one result page. |
| **J-STAGE WebAPI** (api.jstage.jst.go.jp/searchapi, service=3) | ✅ yes | local curl | Structured Atom XML. 132 スルフォラファン records. Metadata only (no abstracts). |
| **CiNii** (cir.nii.ac.jp/opensearch/articles) | ✅ yes | local curl | JSON OpenSearch. **0 results** for every SFN × urate/gout combination. |
| **RISS** (riss.kr) | ✅ yes | local curl | HTML. 1 hit for 설포라판 요산 = a consumer nutrition guidebook, not research. |
| **PubMed** | ✅ yes | MCP | Catches East-Asian-authored English-abstract work. |
| CNKI (search.cnki.net, kns.cnki.net) | ❌ no | — | curl failed / anti-bot. **Unreachable from sandbox.** |
| Baidu Xueshu (xueshu.baidu.com) | ❌ no | — | Returns 百度安全验证 anti-bot page. Blocked. |
| WanFang (s.wanfangdata.com.cn) | ❌ no | — | Client-rendered SPA shell; results are XHR-loaded, absent from static HTML. |
| chinaxiv.org / KoreaScience | ❌ no | — | curl failed. |
| europepmc.org | ❌ no | — | Host not in local_curl allowlist (PubMed MCP covers the same index). |

**Plain statement on CNKI:** CNKI itself is unreachable from this sandbox (anti-bot). However, CQVIP indexes overlapping Chinese-journal + CNKI-conference content and *is* reachable — and it surfaced a CNKI conference DOI (`c.cnkihy.2022.033776`) directly. So the Chinese corpus is partially covered despite CNKI being down. WanFang would add breadth if driven through a headless browser; not attempted here.

---

## 2. Load-bearing sources

### A. UNIQUE to the Chinese corpus (not in PubMed English)

#### A1. Sulforaphane protects renal tubular epithelial cells (HK-2) from urate-induced apoptosis via ER-stress IRE-1/JNK inhibition
- **Native citation:** 萝卜硫素对尿酸诱导HK-2细胞凋亡及内质网应激IRE-1/JNK信号通路的影响 *(title reconstructed from abstract — precise title/journal source-read pending)*. Chinese Medical Association journal series, **DOI 10.3760/cma.j.cn431460-20190505-00032** (article ID dated 2019-05-05; CQVIP index hint ~2023).
  - English gloss: "Effect of sulforaphane on uric-acid-induced apoptosis of HK-2 cells and on activation of the endoplasmic-reticulum-stress IRE-1/JNK signaling pathway."
- **Evidence level:** In Vitro (human HK-2 proximal tubular cell line).
- **Administered:** pure **sulforaphane** (萝卜硫素), 10 / 20 / 40 μM, co-incubated 24 h with uric acid (200 mg/L).
- **Model/population:** HK-2 cells; uric-acid (200 mg/L, 24 h) injury model. Groups: control / UA / UA+SFN low-mid-high.
- **Verified key result:** UA alone ↓ viability, ↑ apoptosis, ↑ Cleaved caspase-3, Cleaved caspase-12, BiP/GRP78, IRE-1, JNK (all P<0.05). SFN dose-dependently reversed all of these (↑ viability, ↓ apoptosis, ↓ all five proteins; P<0.05). **Conclusion:** SFN reduces tubular-cell apoptosis by inhibiting ER-stress IRE-1/JNK activation.
- **Two-model annotation (load-bearing claims):** Model A = this agent (in-context read of the Chinese abstract); Model B = DeepSeek-chat via OpenRouter counterread ([`counterreads.json`](./counterreads.json)).
  - Dose/route/markers/statistics: **full agreement**, no disagreement. Both read 200 mg/L UA, 10/20/40 μM SFN, 24 h, caspase-3/caspase-12/BiP-GRP78/IRE-1/JNK, all P<0.05.
  - Mechanism verb: {Model A: "inhibits activation of the ER-stress IRE-1/JNK pathway" | Model B: "inhibiting the activation of the endoplasmic reticulum stress IRE-1/JNK signaling pathway"} — agree (Chinese 抑制…活化). No `[TRANSLATION-DISAGREEMENT]`.

#### A2. Sulforaphane (as glucoraphanin + myrosinase) lowers serum urate mainly via excretion — urine-metabolomics study in hyperuricemic rats
- **Native citation:** CNKI conference paper, **DOI 10.26914/c.cnkihy.2022.033776** (2022). Peking-University-style oxonate+yeast HUA model. (Almost certainly the conference companion of PMID 36371056 — same group, same model, same Nrf2/gut-axis thesis; see B1.)
  - English gloss: "Intervention effect and mechanism of sulforaphane on hyperuricemic rats based on urine metabolomics."
- **Evidence level:** Animal Model (male SD rats, n=40, 4 groups).
- **Administered:** ⚠️ **not pure SFN** — the "sulforaphane group" was dosed **10 mg/kg·bw glucoraphanin (萝卜硫苷) + myrosinase (黑芥子酶)**, i.e. the glucosinolate precursor plus its activating enzyme for in-situ SFN generation. Allopurinol arm = 10 mg/kg·bw.
- **Verified key result:** vs HUA group, the SFN(precursor) group ↓ SUA, SCr, UCr (P<0.05); ↓ ALT/AST, ↑ A/G, ↓ TC. 7 key pathways / 5 marker metabolites (4-hydroxyproline & proline ↓; succinate & α-ketoglutarate ↑; threonate ↑). **Conclusion: SFN lowers urate chiefly by promoting uric-acid EXCRETION**, plus enhanced antioxidant/anti-inflammatory capacity and improved energy metabolism.
- **Two-model annotation:** Model B (DeepSeek) counterread confirms the **glucoraphanin+myrosinase** dosing (not pure SFN) and the **excretion-dominant** mechanism verbatim — full agreement on the load-bearing dose-form and mechanism claims. No disagreement.

### B. East-Asian-authored, PubMed-indexed (English abstract)

Per PubMed. Attribution: *Based on articles retrieved from PubMed.*

#### B1. SFN reprograms gut microbiome/metabolome to ameliorate hyperuricemia (Chinese, Peking)
- Wang R, Halimulati M, ... Zhang Z. *J Adv Res* 2022;52:19-28. [DOI](https://doi.org/10.1016/j.jare.2022.11.003) (PMID 36371056).
- **Animal Model.** Oxonate+yeast HUA rats; SFN vs allopurinol, 6 wk oral. SFN ↓ urate by **decreasing urate synthesis AND increasing renal urate excretion**; identified succinate & oxoglutarate as host–microbiome co-metabolites; renoprotection via **epigenetic modification of Nrf2** × gut-microbiota interaction.

#### B2. Oral SFN suppresses NLRP3 inflammasome, alleviates acute gouty inflammation (Korean)
- Yang G, Yeon SH, ... Lee JY (Catholic Univ. of Korea). *Rheumatology (Oxford)* 2018;57(4):727-736. [DOI](https://doi.org/10.1093/rheumatology/kex499) (PMID 29340626).
- **Animal Model.** Two MSU-crystal gout models (footpad + air pouch). Oral SFN ↓ swelling & neutrophil recruitment; ↓ caspase-1(p10) & IL-1β; suppressed NLRP3 activation by MSU, ATP, nigericin **but not poly(dA:dT)** — ROS-independent; suggests SFN acts directly on the NLRP3 complex.

#### B3. SFN attenuates NLRP3 and NLRC4 (not AIM2) inflammasomes; MSU peritonitis (Korean)
- Lee J, Ahn H, ... Lee GS (Kangwon / Chungnam / Pusan / Chungbuk Nat'l Univ.). *Cell Immunol* 2016;306-307:53-60. [DOI](https://doi.org/10.1016/j.cellimm.2016.07.007) (PMID 27423466).
- **In Vitro + Animal Model.** SFN blocks NLRP3 & NLRC4 assembly and NLRP3-gene/pro-IL-1β priming; ↓ IL-1β in MSU-induced peritonitis; ↓ mitochondrial ROS. AIM2 unaffected.

*(Western anchor, for mechanism completeness — not East Asian: Greaney AJ et al., NIH, J Leukoc Biol 2015;99(1):189-99, [DOI](https://doi.org/10.1189/jlb.3A0415-155RR), PMID 26269198 — SFN inhibits NLRP1/NLRP3/NLRC4/AIM2 via an **Nrf2-INDEPENDENT** mechanism; acute-gout peritonitis model. Note this directly qualifies the "Nrf2 epigenetic" framing in B1: the anti-inflammasome action is at least partly Nrf2-independent.)*

---

## 3. "Unique to East Asian corpus" callout — findings NOT present in Western literature

1. **Renal-tubular ER-stress / IRE-1/JNK protective axis (A1, Chinese, CQVIP).** Western SFN-gout literature is almost entirely macrophage/NLRP3-centric. The Chinese corpus adds a **urate-nephropathy / kidney-protection** angle: SFN dose-dependently rescues human proximal-tubular cells from urate-induced ER-stress apoptosis (BiP/GRP78, IRE-1, JNK, caspase-12). This is a distinct organ target (kidney parenchyma, not joint macrophages) and a distinct pathway (UPR/ER-stress, not inflammasome). Not found in the PubMed-English set.

2. **In-situ SFN generation via glucoraphanin + myrosinase dosing (A2, Chinese).** The Peking group's in-vivo "SFN" arm actually delivered the **precursor glucoraphanin plus myrosinase**, not preformed SFN — an enzyme-activated delivery format. **Directly relevant to Open Enzyme's thesis:** an engineered enzyme (myrosinase) converting a stable dietary precursor to the active agent in the gut lumen is the same architecture as OE's koji/uricase gut-delivery model. Worth flagging as a delivery-format precedent.

3. **Mechanism framing centers EXCRETION, not just inflammation.** Both Chinese sources emphasize **uric-acid excretion / renal handling** (A2: "mainly through promoting excretion"; B1: "increasing renal urate excretion") — aligning with OE's ABCG2 / gut-and-kidney excretion thesis more than the Western NLRP3-inflammation framing does.

4. **Japanese absence is real, not a retrieval artifact.** 132 J-STAGE + 70 CiNii スルフォラファン records, but **zero** intersect uric acid / gout / hyperuricemia (CiNii returned 0 for every SFN×urate combination; J-STAGE title matches were generic 炎症/immunology, psychiatry, cancer, detox). The large Japanese functional-food SFN base has **not** been pointed at hyperuricemia. This is a genuine white space, not a language barrier.

---

## 4. Non-promotion caveats (discovery-positive, source-read pending)

- **A1 (HK-2 ER-stress):** abstract fully read + cross-checked (Model A + Model B agree). Precise **journal name and publication year not yet confirmed** from a full-text/landing page (CMA DOI cn431460; article ID 2019-05-05, index hint 2023). Finding is solid; bibliographic metadata is pending a landing-page read. **Discovery-positive, full-text source-read pending.**
- **A2 (HUA metabolomics):** CNKI conference abstract read + cross-checked. Treated as the conference companion of B1 (PMID 36371056) on strong circumstantial grounds (same model, group, thesis) but **that linkage is inferred, not confirmed**.
- CNKI / WanFang not directly searchable from the sandbox — a headless-browser pass on those two would likely add more Chinese-language SFN×hyperuricemia records (candidate follow-up).

## 5. Provenance
- Query plan: [`inputs/sulforaphane-query-plan.json`](../inputs/sulforaphane-query-plan.json)
- Raw retrieval bodies: [`outputs/retrieval-probes-raw/`](./retrieval-probes-raw/)
- Extracted Chinese abstracts: [`outputs/cqvip-abstracts.json`](./cqvip-abstracts.json)
- Model-B counterreads (DeepSeek): [`outputs/counterreads.json`](./counterreads.json)
- PubMed data retrieved via MCP; DOIs linked inline above.
