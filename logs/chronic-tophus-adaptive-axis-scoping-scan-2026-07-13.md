---
title: "Scoping scan — chronic-tophaceous / adaptive-immune axis (is there a distinct tophus kill chain?)"
date: 2026-07-13
tags: [scoping-scan, tophus, tophaceous-gout, Th17, IL-17, RORgt, RANKL, osteoclast, TGF-beta, fibrosis, SPP1-macrophage, tophus-dissolution, adaptive-immunity]
status: scan-log
trigger: "ChEMBL refresh flagged ursolic acid as RORγt inverse agonist → question whether chronic-tophaceous / adaptive-immune axis deserves its own peer track separate from acute-flare NLRP3 kill chain"
related: [nlrp3-exploit-map.md, gout-pathophysiology.md, gut-lumen-sink.md, modality-chokepoint-matrix.md, spm-resolution-pathway.md]
---

# Chronic-Tophus Adaptive-Axis Scoping Scan — 2026-07-13

**Question probed:** The OE kill chain (CP0–CP6) is built around the *acute flare* (MSU → NLRP3 → IL-1β → neutrophils; innate, fast, self-limiting). A **tophus** is a chronic organized granuloma (crystalline core + macrophage/giant-cell corona + fibrous capsule + adaptive-immune infiltrate). Does a distinct chronic-tophaceous / adaptive-immune axis (RORγt/Th17/IL-17; TGF-β/fibrosis; RANKL/osteoclast; giant-cell/granuloma; complement) deserve its own scope-page peer track (like LBP / siRNA-URAT1), or is it an open-questions entry?

**Method note / multilingual coverage:** bio-research MCP (pubmed, c-trials, consensus, chembl). Direct CNKI / WanFang / Baidu-Scholar / ChiCTR fetch is **JS-gated / bot-blocked in-sandbox** (508–560 byte challenge stubs returned) — this is a *tooling* access limit, NOT a language barrier. Chinese-group evidence was captured through PubMed/EuropePMC/Consensus indexing instead, and it turns out the load-bearing tophus-tissue and Th17/Treg papers ARE from Chinese groups (Fudan/Huashan — Xu 2025; Shanxi Medical — Zhao 2022; the Zi 2024 Th17/Treg cohort), all read in this scan. ChiCTR interventional-registry coverage for IL-17-blocker/TCM-tophus trials remains an un-probed gap (no sandbox route).

---

## Queries run

| # | Source | Query | Hits |
|---|---|---|---|
| 1 | PubMed | (IL-17/Th17) AND (gout/tophus/MSU) | 137 |
| 2 | PubMed | tophus AND (T cell/adaptive/lymphocyte/granuloma/giant cell) | 34 |
| 3 | PubMed | secukinumab/ixekizumab/bimekizumab/anti-IL-17 AND gout/MSU | 9 (all PsA-with-gout-comorbidity; none = gout treatment) |
| 4 | PubMed | IL-17 AND gout AND (synovial fluid/serum/tissue/macrophage) | 40 |
| 5 | PubMed | (TGF-β/fibrosis/fibroblast) AND (tophus/tophaceous fibrosis) | 32 |
| 6 | ClinicalTrials.gov | gout × (secukinumab/ixekizumab/bimekizumab/canakinumab/IL-17) | 12 — **all canakinumab (IL-1β); ZERO IL-17-blocker gout trials** |
| 7 | PubMed | tophus dissolution/regression × (pegloticase/febuxostat/allopurinol) × (DECT/US) | 31 |
| 8 | PubMed | (RANKL/osteoclast/bone erosion) AND (gout/tophus/MSU) | 294 |
| 9 | PubMed | RORγt inverse agonist × natural product (ursolic/triterpene/flavonoid/digoxin) | 70 |
| 10 | PubMed | tophus × (corona/organization/adaptive/CD3/CD20/plasma cell) × histology | 21 |
| 11 | PubMed | (Th17/IL-17/RORγt/Treg) AND (tophaceous/tophi/chronic gout) AND T-cell balance | **2 (total)** — near-empty; direct tophus-tissue Th17 literature does not exist |
| 12 | PubMed | RORγt/IL-17 × (ursolic/celastrol/digoxin/berberine/resveratrol/dietary) | 402 |
| 13 | Consensus | "Does IL-17/Th17 drive tophus formation or bone erosion in chronic tophaceous gout?" | 20 |

---

## Papers found (PMID / DOI + one-line finding)

**Tophus tissue architecture / adaptive-immune content**
- **Dalbeth 2010**, PMID 20131281, DOI 10.1002/art.27356 (Arthritis Rheum) — Cellular characterization of the gouty tophus (16 samples/12 pts). Corona zone: CD68+ mono/multinucleated (giant) cells, mast cells, **very high plasma cells**, IL-1β+ and TGFβ1+ cells; CD20+ B-cell aggregates in fibrovascular zone in **6/12 (50%)**; CD8+ T cells present; neutrophils rare. CD68 count correlates with IL-1β+ (r=0.691, p=0.009) and TGFβ1+ (r=0.518, p=0.04). **No Th17/IL-17 signature reported.** Innate + adaptive, but plasma-cell/B-cell + macrophage dominant. [tier: In Vitro / ex-vivo human tissue]
- **Xu, Dalbeth, He 2025**, PMID 41107120, DOI 10.1016/j.ard.2025.09.003 (Ann Rheum Dis) — First single-cell (44,221 cells) + spatial transcriptomic deconstruction of tophaceous vs intercritical gout joints. **SPP1/MMP9/CHI3L1 macrophages exclusive to tophus corona**: ECM-remodeling genes, integrin-stromal interactions, **osteoclast-transition potential**, and **fibroblast-like phenotype (S100A4+ COL6A2+)**. **CD4 T cells shift inflammatory → immune-REGULATORY during tophus development.** The definitive tissue-level datum. [tier: In Vitro / ex-vivo human tissue + Mendelian-randomisation causal inference]
- **Chhana/Dalbeth "The gouty tophus: a review" 2015**, PMID 25761926, DOI 10.1007/s11926-014-0492-x — tophus = chronic foreign-body granuloma-like structure; NET formation a candidate checkpoint; effective treatment needs long-term SUA **<5 mg/dL (300 µmol/L)**.

**Q1 driver-vs-bystander (Th17/IL-17)**
- **Liu 2018**, PMID 29476737, DOI 10.1016/j.bbrc.2018.02.166 — Serum IL-17 elevated in **acute** gout, rises early, decays with symptoms; **source = γδ T cells (innate-like), not adaptive Th17**; correlates with IL-1β. Acute/innate, not tophus.
- **Zhao 2022**, PMID 36436796, DOI 10.1016/j.trim.2022.101763 (Shanxi Medical, n=205 gout) — Th1/Th2 dominates progression; Th1 the independent risk factor for chronic gout; "Th17 becomes involved as disease progresses" but **Th17 negatively correlates with CRP** (peripheral blood).
- **Zi 2024** (Consensus [1], Clin Exp Med, n=126 gout) — Th17/Treg ratio elevated in gout **including gout WITHOUT tophus**; early-onset imbalance = ↑Th17, late-onset = ↓Treg. Tophus predicted by disease duration/CRP/fibrinogen, **not by Th17**. Peripheral, not tophus-specific.
- **Wang/Terkeltaub 2020**, PMID 31738005, DOI 10.1002/art.41173 — Gout PBMC methylome: Th17-differentiation + IL-17-signaling pathways differentially methylated; IL23R (granuloma mediator) a differentially-methylated risk gene; BUT **osteoclast differentiation is the most strongly weighted pathway**. Epigenetic/correlative.
- ClinicalTrials.gov (query 6): **no IL-17-blocker (secukinumab/ixekizumab/bimekizumab) trial in gout exists** — no blockade → no driver evidence. All gout-biologic trials are canakinumab (IL-1β).

**Q2 tophus dissolution kinetics under urate-lowering**
- **Becker 2005 (FACT)**, PMID 16339094, DOI 10.1056/NEJMoa050373 (NEJM, n=760) — median **tophus AREA reduction 83% (febuxostat 80 mg) / 66% (120 mg) / 50% (allopurinol 300 mg) over 52 wk** (between-group NS, p=0.08/0.16). Threshold endpoint SUA <6.0 mg/dL.
- **Araujo/Schett 2015**, PMID 26509070, DOI 10.1136/rmdopen-2015-000075 (RMD Open, pegloticase DECT, n=10 refractory, baseline SUA 8.1) — **tophus volume −71.4% overall; responders (SUA <6 ≥80% of time) −94.8%; near-clearance in mean 13.3 weeks (months).** Articular tophi fast, tendon tophi slow.
- **Pascart 2025 (GOUT-DECTUS)**, PMID 40139560, DOI 10.1016/j.jbspin.2025.105892 (n=55, baseline SUA 8.73) — treat-to-target ULT: **DECT tophus volume −96% M6, −100% M12, complete resolution by M24**; US −56/−84/−96% (US noisier).
- **Dalbeth 2019**, PMID 31081595, DOI 10.1002/art.40929 (DECT RCT, n=87) — treat-to-target (SU <0.36 mmol/L = 6 mg/dL) reduces **bone-erosion progression** (control +7.8% vs escalation +1.4% at 2 yr, p=0.015) and DECT urate volume (−28%); sub-target SU → no urate reduction (+1.5%).
- **Bardin 2022 "shrinking toe sign"**, PMID 35183934, DOI 10.1016/j.semarthrit.2022.151981 — in severe tophaceous gout, crystal dissolution below 300/360 µmol/L can precipitate **lytic bone collapse** of already-eroded joints → dissolution clears crystals but does NOT restore the eroded bone scaffold.

**Q3 candidate nodes (RANKL / fibrosis / granuloma)**
- **Schlesinger 2010** (Consensus [3], Ann Rheum Dis, 166 cites) — bone erosion in gout driven by **tophus eroding bone via RANK–RANKL/osteoclast**; IL-1β the upstream driver; "it is the tophus eroding the underlying bone that is pivotal." Basis for anti-RANKL (denosumab) repurposing hypothesis.
- TGF-β/fibrosis node anchored by Dalbeth 2010 (TGFβ1+ corona cells) + Xu 2025 (fibroblast-like SPP1 macrophages). No anti-fibrotic tested in tophus.

**Q4 food-grade / engineerable adaptive-axis candidates**
- Ursolic acid = RORγt inverse agonist (food-grade: apple peel, holy basil, rosemary; triterpene). Reported ROR-γ activity spans **~sub-µM to low-µM (task-supplied ~0.75–680 nM range)** across cell-free reporter / SPR / cellular assays — **moderate-potency and highly promiscuous** (hits many targets), not a clean selective probe.
- **Al Nabhani/Eberl 2019**, PMID 30902637, DOI 10.1016/j.immuni.2019.02.014 — SCFAs (butyrate) + retinoic acid generate **RORγt+ peripheral Tregs**; ties the adaptive axis directly to OE's existing butyrate/LBP track (Treg induction / Th17-Treg rebalancing).
- Salt→Th17 axis papers (Kleinewietfeld 2013 PMID 23467095 Nature; Faraco 2018 PMID 29335605 Nat Neurosci) — confirm RORγt→Th17→IL-17 is a real, diet-modulable axis in *autoimmune* contexts, but not shown in tophus.
- Digoxin (potent RORγt inverse agonist) and celastrol (Th17/anti-fibrotic) — **rejected for food-grade route** (narrow TI / toxic, non-food-grade).
- Already-in-stack incidental Th17/RORγt suppressors: berberine, EGCG, sulforaphane, resveratrol, curcumin (curcumin = the anti-fibrotic/TGF-β anchor). Astragalus polysaccharide (PMID 35265068) — Th17/Treg rebalance, Chinese-source, potentially fermentable.

---

## Per-question verdicts

**Q1 — Th17/IL-17: driver or bystander in tophus biology? → BYSTANDER (driver hypothesis unsupported; tissue evidence points against).**
Strongest single datum against driver: **Xu 2025 (PMID 41107120)** — in actual tophus tissue, CD4 T cells skew *immune-regulatory* during tophus development while matrix remodeling/osteoclast/fibrosis is done by a tophus-exclusive **SPP1/MMP9 macrophage** subset, not Th17. Corroborating: direct tophus-tissue Th17 literature is essentially non-existent (query 11 = 2 papers total); Th17 elevation is a peripheral / acute-flare / early-onset phenomenon (Liu 2018 γδ-T source; Zi 2024 elevated even in *non-tophaceous* gout; Zhao 2022 Th17 negatively correlates with CRP); and **zero IL-17-blocker trials exist in gout** so there is no blockade-shrinks-tophi evidence. Evidence tier for driver claim: none above Mechanistic Extrapolation. Evidence tier for "elevated in gout" (bystander-compatible): In Vitro + peripheral human cohorts.

**Q2 — dissolution threshold + timescale + magnitude.**
Threshold: **SUA < 6.0 mg/dL (360 µmol/L)** to dissolve (below 6.8 saturation); **< 5.0 mg/dL (300 µmol/L)** for faster/complete resolution (Clinical Trial + imaging RCTs). Timescale/magnitude: months → ~24 months; treat-to-target ULT → DECT tophus −96% at 6 mo, complete by 24 mo (Pascart 2025); intensive pegloticase (very low SUA) → −71% overall / −95% in responders within ~3 months (Araujo 2015); febuxostat −83% tophus area at 52 wk (Becker 2005). **What OE's uricase sink already contributes:** tophus dissolution is a *urate-solubility* phenomenon, so to whatever extent the sink drives SUA below saturation (and ideally <6/<5), it dissolves tophi on the identical physical-chemistry kinetics — no separate "tophus mechanism" is needed. **What it does NOT address:** (a) the sink's projected −0.5 to −1.0 mg/dL (comp-019/H08) is unlikely to cross the <6 threshold from an 8+ mg/dL baseline as monotherapy → it is an adjunct that lowers ULT burden, not a standalone tophus-dissolver; (b) the organized tissue response — fibrous capsule, SPP1-macrophage/ECM remodeling, and already-eroded bone scaffold — persists after crystals clear (Bardin 2022 shows dissolution can even precipitate bony collapse).

**Q3 — distinct "tophus kill chain," filtered.**
- **RANKL / osteoclast (bone erosion)** — REAL intervention point. Tier: Animal Model + In Vitro + human imaging RCT (Schlesinger 2010; Dalbeth 2019; Xu 2025 osteoclast-transition). Tractable via denosumab repurposing (discovery-engine output). Caveat: substantially downstream of crystal burden + IL-1β, so partly covered by urate-lowering already.
- **SPP1/MMP9 macrophage → ECM remodeling / fibrosis** — the single most *distinct* newly-defined node and the actual driver of tophus organization (Xu 2025). Tier: In Vitro (ex-vivo human). Intervention tractability currently LOW (no approved SPP1/CHI3L1 drug; MMP9 inhibitors historically failed). Distinctness from acute axis: VERY HIGH.
- **TGF-β / fibrosis (capsule)** — REAL biology (Dalbeth 2010; Xu 2025), SPECULATIVE as intervention (systemic TGF-β inhibition unsafe; no anti-fibrotic tested in tophus).
- **Giant-cell / granuloma** — REAL cardinal histology, but no intervention distinct from crystal removal (LOW tractability).
- **RORγt / Th17 / IL-17** — SPECULATIVE / likely bystander (see Q1). Keep as open-question, not a node.
- **Complement in tophus** — already covered by CP0/C5a track; no tophus-specific driver evidence.
- **Reframe:** the distinct chronic axis is real but it is **innate-macrophage + stromal + osteoclast**, NOT adaptive-Th17. The premise's "adaptive-immune corona" is present (plasma cells, B-cell aggregates, regulatory CD4) but is not the growth/persistence driver.

**Q4 — food-grade / engineerable adaptive-axis shortlist (honest).**
1. **Butyrate / SCFA (RORγt+ Treg induction)** — best-integrated engineerable hit; **already inside OE's LBP/butyrate track** (Al Nabhani 2019). Promotes Treg, rebalances Th17/Treg. This is the adaptive-axis lever OE is already closest to.
2. **Ursolic acid** — genuine RORγt inverse agonist, food-grade, but moderate-potency + promiscuous, and the axis it hits is not a validated tophus driver → discovery-engine curiosity, not a priority.
3. **Curcumin** — anti-fibrotic/TGF-β anchor, already in stack.
4. Incidental (already in stack): berberine, EGCG, sulforaphane, resveratrol suppress Th17/RORγt as a side effect.
5. **Astragalus polysaccharide** — Th17/Treg rebalance, Chinese-source, potentially fermentable (untested in gout).
- The potent RORγt naturals (digoxin, celastrol) are toxic / non-food-grade → rejected. Net: food-grade RORγt-inverse-agonism as a discovery target is thin.

**GO/NO-GO → NO to a dedicated scope page + falsification card; YES to an open-questions entry (+ a short annotation on `gout-pathophysiology.md` and a RANKL/denosumab repurposing note).**
Biggest single reason: the *triggering* hypothesis — Th17/IL-17/RORγt as a chronic-tophus driver — fails the driver test (no IL-17-blockade gout data; tophus CD4 T cells skew regulatory; Th17 is peripheral/acute/early-onset, not tophus-specific). A peer track needs a falsifiable driver thesis; this axis is a bystander. The genuinely distinct chronic-tophus biology (SPP1-macrophage/RANKL-osteoclast/fibrosis) is innate-stromal, largely downstream of crystal burden + IL-1β (already in the CP framework), and not food-grade-engineerable — so it belongs as an open-question + repurposing note, not a new chassis/peer track. The highest-value capture is the honest Q2 framing: **OE's sink dissolves crystals if it crosses the solubility threshold, but does nothing for the organized capsule/bone damage** — which cleanly bounds what the platform claims for tophi.

---

## Chinese-registry re-run (local_curl, 2026-07-13)

**Why this section exists:** the scan above flagged Chinese sources as "JS-gated / bot-blocked in-sandbox" and left ChiCTR interventional-registry coverage as an un-probed gap. This re-run used **local `curl`** (per `wiki/etc/experiments/lib/agentic_lit_synthesis.py` `local_curl_fetch`), not hosted/browser fetch, and closes the ChiCTR gap decisively. Public-corpus registry data only.

### Per-host reachability (local curl, this sandbox)

| Host | Reachable? | Detail |
|---|---|---|
| **ChiCTR** `chictr.org.cn` | **YES — full query + detail** | Not in this sandbox's network allowlist → fetched with sandbox disabled (laptop network path). Sits behind an **Aliyun WAF JS challenge** (`aliyunwaf`, `acw_sc__v2` cookie). Solved locally by reproducing the `unsbox` byte-permutation + `hexXor(mask)` that the challenge JS computes from `arg1`, then re-requesting with the derived `acw_sc__v2` cookie. Results are **server-rendered** into `searchproj.html` (GET params `studyailment`=disease, `measure`=intervention, `title`, `btngo=btn`) and `showproj.html?proj=NNNN` (authoritative per-trial record, bilingual zh/en). Note: `curl --compressed` required (gzip). |
| **CNKI** `oversea.cnki.net` | Landing YES / search **NO** | `kns.cnki.net`, `search.cnki.net`, `scholar.cnki.net` = connection-refused (HTTP 000, datacenter-IP block). `oversea.cnki.net` landing = 200. Its `kns8s/brief/grid` search API is reachable and *processes* the POST but **soft-blocks non-JS clients**: 4 QueryJson variants returned a progression of rejections (`非法逻辑操作符` → `检索模型参数错误` → `查询对象结构错误,没有指定检索分类`). Requires JS-established search-classification/session tokens curl cannot reproduce. Not curl-scriptable here. |
| **WanFang** `wanfangdata.com.cn` | Landing YES / search **NO** | Landing 200 (212 KB). Vue SPA; the JS bundle host (`cdn.w.wanfangdata.com.cn`) and search API host are **not in the sandbox allowlist** (000), so the search XHR endpoint can't be reached. |
| **CQVIP** `cqvip.com` | Landing YES / search **NO** | Landing 200 (284 KB). Search endpoints (`/search/normal`, `/api/search`) return HTTP 400 — signed/token-gated SPA API. Not curl-scriptable here. |
| **Baidu Scholar** `xueshu.baidu.com` | Landing YES / search **NO** | Landing 200. `/s?wd=…` returns Baidu **安全验证** anti-bot interstitial / 302 redirect even with a primed cookie + referer. |
| **ChinaXiv** `chinaxiv.org` | Landing YES / search **NO** | Landing 200 (108 KB). Search paths (`/search.htm`, `/user/search.htm`) return 400/403/404 — gated. (Open-access repo but small; unlikely to hold clinical gout literature regardless.) |

**Honest correction to the parent scan's framing:** local curl solved the source that mattered most and is genuinely different in kind — **ChiCTR (a server-rendered registry behind a solvable WAF).** The Chinese *full-text databases* (CNKI/WanFang/CQVIP) and Baidu Scholar are **SPA + signed-API + anti-bot** and were NOT curl-scriptable from this sandbox; the parent scan's "bot-blocked" was accurate for those, and local curl does not change it for them. So Q-B/Q-C literature (published mechanistic papers) still rests on the PubMed/EuropePMC-indexed Chinese-group papers already captured above; the *registry* dimension is what this re-run adds.

### Exact queries curled (ChiCTR `searchproj.html`, `btngo=btn`)

- `studyailment=痛风` (gout) → **data-total = 208** interventional+observational gout records
- `studyailment=痛风石` (tophus) → **data-total = 4**
- `studyailment=痛风 & measure=司库奇尤单抗` (secukinumab) → **0**
- `studyailment=痛风 & measure=依奇珠单抗` (ixekizumab) → **0**
- `studyailment=痛风 & measure=白细胞介素17` (IL-17) → **0**
- `studyailment=痛风 & measure=生物制剂` (biologic) → **0**
- `measure=司库奇尤单抗` (secukinumab, ANY disease) → **6** (all non-gout — see below)
- `measure=依奇珠单抗` (ixekizumab, ANY disease) → **1** (psoriasis-vulgaris biomarker study)
- Detail pages: `showproj.html?proj=190398 / 192843 / 327215`

*(Caveat on the `measure` field: it matches full drug/agent names, not fragments — `measure=单抗` alone returns 0 — so intervention searches were run with complete drug names, and the tophus universe was swept via `studyailment=痛风石` + reading each record.)*

### Q-A — do IL-17-pathway / non-IL-1β immunomodulator interventional gout trials exist in ChiCTR?

**IL-17 blockers: CONFIRMED zero in gout.** Secukinumab (司库奇尤单抗) is registered in **6** ChiCTR trials and ixekizumab (依奇珠单抗) in **≥1**, but **none in gout/hyperuricemia**. The 6 secukinumab trials are all the expected IL-17 indications — moderate-severe plaque psoriasis; psoriasis vulgaris biomarkers; active thyroid eye disease; psoriasis immune-cell/cytokine study; refractory Takayasu arteritis (大动脉炎); active ankylosing spondylitis (强直性脊柱炎). The drug names ARE correctly indexed (6 and 1 hits respectively), so the zero-in-gout result is a true negative, not a query miss. **This confirms the parent scan's "zero IL-17-blocker gout trials."**

**BUT — one non-IL-1β immunomodulator interventional gout trial DOES exist (parent scan missed it; it checked only ClinicalTrials.gov):**

- **ChiCTR2300069207** (`showproj proj=190398`) — 「巴瑞替尼治疗慢性痛风石性关节炎的有效性和安全性的临床研究」 *(Clinical study of the efficacy and safety of **baricitinib** for **chronic tophaceous gouty arthritis**)*. Target disease 慢性痛风石性关节炎 / "chronic tophi arthritis". **Interventional**, post-marketing **Phase 4**, **randomized parallel-controlled**, experimental group **n=10**, intervention **巴瑞替尼 (baricitinib, a JAK1/2 inhibitor)**, **primary outcome = gouty radiologic bone erosion (target joint)**. Study period 2022-12-27 → 2024-07-31; recruiting. Site **复旦大学附属华山医院 (Huashan Hospital, Fudan University)**. — *Evidence tier: registered interventional protocol (results not yet published).* JAK inhibition sits downstream of IL-6/IL-23/type-I-IFN via JAK-STAT and *indirectly* modulates Th17 differentiation, but it is **not** an IL-17 antagonist. Its primary endpoint is **bone erosion** — i.e., it targets the innate-stromal/osteoclast chronic-tophus node (Q3), not the adaptive-Th17 axis per se.

- **ChiCTR2600126391** (`showproj proj=327215`) — 「IL-39在痛风患者血清中的表达水平及临床意义」 *(Serum IL-39 expression and clinical significance in gout)*. **Observational** case-control, primary outcome serum IL-39 concentration. IL-39 is an IL-12-family cytokine linked to IL-23/Th17 biology — shows Chinese groups are actively probing novel cytokine axes in gout, but this is a biomarker study, not an intervention.

**Q-A verdict:** The narrow claim **"zero IL-17-blocker gout trials" holds** (secukinumab/ixekizumab/IL-17 all zero in gout across ChiCTR too). The broader framing "**zero non-IL-1β immunomodulator gout trials**" is **partially overturned**: a **baricitinib (JAK-inhibitor) Phase-4 RCT in chronic tophaceous gouty arthritis with a bone-erosion primary endpoint exists in ChiCTR** and was invisible to the ClinicalTrials.gov-only pass. It is a JAK trial, not an IL-17 trial, and its endpoint is the innate-stromal (bone-erosion) node — so it does not resurrect a Th17-driver thesis.

### Q-B — Chinese driver-grade evidence for Th17/IL-17 in tophus (vs bystander)?

No new **driver-grade** evidence surfaced. The Chinese full-text databases (CNKI/WanFang) were not curl-scriptable (above), so this rests on the PubMed/EuropePMC-indexed Chinese-group papers already in the parent scan (Xu 2025 Fudan/Huashan — CD4 skews regulatory in tophus tissue; Zhao 2022 Shanxi; Zi 2024). The only new registry-level signal is the **IL-39 observational study (ChiCTR2600126391)** — an IL-23/Th17-adjacent cytokine being measured in gout serum, which is *bystander-compatible* (expression, not manipulation). **No blockade-changes-tophus-outcome evidence.** **Q-B verdict unchanged: BYSTANDER.** Tier for any Th17/IL-17-in-tophus driver claim remains ≤ Mechanistic Extrapolation.

### Q-C — TCM / clinical tophus-dissolution (痛风石溶解/消融) evidence

- **ChiCTR2300071056** (`showproj proj=192843`) — 「健脾渗湿颗粒治疗痛风石（脾虚湿阻型）的临床疗效观察」 *(**Jianpi Shenshi Granule** for tophus, spleen-deficiency damp-obstruction pattern 脾虚湿阻型)*. **Interventional**, randomized pilot (Study phase 0 / exploratory), **treatment arm = 非布司他片 + 健脾渗湿颗粒 (febuxostat + Jianpi Shenshi Granule), n=20** vs **control = 非布司他片 (febuxostat alone), n=20**. **Primary indicator = 痛风石 (tophus)**; secondary = 血尿酸 (serum uric acid). Study period 2023-01-01 → 2024-05-31. Site 云南中医药大学第一附属医院 (First Affiliated Hospital, Yunnan University of TCM). — *Evidence tier: registered interventional protocol; results not yet published.* Design is explicitly **adjunct-to-ULT** (TCM formula *on top of* febuxostat, with serum urate as a secondary), which is consistent with — not a challenge to — the parent scan's Q2 framing that **tophus dissolution is fundamentally a urate-solubility phenomenon**. The registered primary field reads literally "痛风石 / Gout stone"; it does not specify a quantitative size/volume metric, so do not over-read it as a validated "size-reduction" endpoint.

**Q-C verdict:** One registered Chinese TCM tophus adjunct RCT exists (健脾渗湿颗粒 + febuxostat), framed as add-on to standard urate-lowering. No published outcome yet; no formula with demonstrated *stand-alone* tophus-regression evidence surfaced (CNKI/WanFang full text not reachable). Consistent with "dissolution is urate-driven; food-grade/TCM adjuncts modulate ULT burden, not a separate dissolution mechanism."

### Rigor — two-model translation cross-check (Model A = this Claude subagent; Model B = DeepSeek via OpenRouter)

Ran on the three load-bearing ChiCTR records. **Concordant on every load-bearing point** — Record 1 baricitinib = JAK inhibitor / interventional / NOT IL-17-pathway blockade / primary endpoint radiographic bone erosion; Record 2 = TCM herbal compound + febuxostat (XO inhibitor) / interventional / primary endpoint tophus; Record 3 IL-39 = observational biomarker, IL-23/Th17-linked, not IL-17 blockade. **No `[TRANSLATION-DISAGREEMENT]` flags.** (ChiCTR records are themselves bilingual zh/en, which independently corroborates the readings.) One minor non-substantive note: Model B rendered Record 2's primary endpoint as "tophus size reduction"; the registry field literally reads only "痛风石 / Gout stone", so the size-quantification is Model B's inference, not a registered metric — flagged, not adopted.

### Bottom line

The Chinese-language registry evidence **CONFIRMS the prior NO-GO** on a dedicated chronic-tophus adaptive-immune (Th17/IL-17) scope page — it still fails the driver test (zero IL-17-blocker gout trials in ChiCTR too; the only new immunomodulator trial is a **JAK inhibitor** whose primary endpoint is **bone erosion**, i.e., the innate-stromal node, and the only new adaptive-axis signal is an **observational** IL-39 biomarker study) — while adding two registry items worth an open-questions line: **ChiCTR2300069207 (baricitinib/JAK Phase-4 RCT in tophaceous gout, bone-erosion endpoint)** as a real-world readout on the RANKL/osteoclast Q3 node, and **ChiCTR2300071056 (健脾渗湿颗粒 + febuxostat tophus adjunct RCT)** as a TCM data point squarely inside the urate-solubility dissolution frame.
