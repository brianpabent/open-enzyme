# Pre-2026-05-19 Lit-Scan Query-Framing Retrospective Audit — 2026-05-19

Triggered by: Cluster M walkthrough query-framing discipline promotion (CLAUDE.md §"Global-multilingual research by default" → Query-framing discipline bullet, 2026-05-19, lines 263–269). Question: how much of the project's pre-2026-05-19 literature evidence base may be incomplete because lit scans used mechanism-name-only framing?

The rule under audit (CLAUDE.md line 263):

> Query by **traditional-formula-name + species-name + traditional-pathology-framing IN ADDITION TO mechanism-name** for non-Western-medicine compound discovery. Mechanism-name is the wrong starting point for non-Western literature.

Canonical worked example (comp-018 Phase 2, 2026-05-17): "C3 convertase inhibitor" misses *Houttuynia cordata* (鱼腥草 / どくだみ); "*Houttuynia cordata* anti-complementary" catches it.

---

## Summary

- **Three layers** of past literature work were audited: comp-NNN computational experiments (15+ with literature components), the daemon sweep pipeline (4 prompt templates + 39 prior Pass 2 synthesis logs), and the H-card hypothesis files (9 cards).
- **The query-framing gap is concentrated in two places**: (1) the upstream-complement domain (comp-018 Phase 1, the canonical exemplar — already corrected by Phase 2 / comp-020), and (2) the medicinal-mushroom compound mapping (comp-014 Phase 3 ChEMBL UniProt-join intersection — Phase 5 multilingual deep-dive deferred + East-Asian DBs unreachable). The TCM gout compound triage (comp-013) already used species + traditional-formula-name anchors (Si Miao San, Smilax glabra / Tu Fu Ling, Rheum officinale / Da Huang) — partial discipline was operative there.
- **Daemon sweep prompts encode the global-multilingual default but NOT the query-framing discipline.** Only the Pass 2 (synthesize) prompt mentions multilingual research at all; Pass 1 (propagate) and both Pass 3 (review) prompts are silent on language/discipline. This means all 39 pre-2026-05-19 Pass 2 syntheses operated without explicit query-framing-discipline guidance, though Pass 2 does have global-multilingual awareness.
- **Highest-leverage re-scan candidates** (in priority order): URAT1 × Si Miao San / Smilax glabra / Tu Fu Ling, XO × Jiang Huang (turmeric) × Huo Xiang Zheng Qi formulas, NLRP3 × Lingzhi spore powder + Yun Zhi (PSK/PSP), and Houttuynia × CP1 dual-mechanism (already queued separately for 2026-05-19). Lower-leverage but worth tagging: medicinal-mushroom × HDAC6 (Q141K-ABCG2 rescue), mushroom × Lp-PLA2, and Cordyceps × ADA (the ADA chokepoint was promoted via comp-014 Phase 5 — that promotion came from species-name reading, vindicating the rule).
- **Western-pharma-only domains do not need re-scanning under this rule.** comp-019 (ALLN-346/PRX-115 Q141K stratification), comp-017 (GTEx/HPA sex-dimorphism), comp-016 (T-axis ABCG2 evidence), comp-024 (complestatin BGC engineering), comp-027 (disulfiram dose modeling), and the engineering-side comp-NNN (comp-001/002/005/006/010/011/012/022/030/032/034) all operate in Western-pharma or sequence-engineering domains where the traditional-name framing is not load-bearing.

---

## Audited assets

- **comp-NNN experiment query-strategy files** (where present):
  - `wiki/etc/experiments/comp-013-tcm-gout-compound-triage/inputs/compounds.json` (lines 1–167) — TCM compounds with classical gout indication
  - `wiki/etc/experiments/comp-014-medicinal-mushroom-compound-mapping/inputs/data-sources.json` (lines 1–229) + `chokepoint-targets.json` (lines 1–202) + `phase-5-anchor-species.json` (lines 1–60+) — multi-DB breadth, chokepoint targets, anchor species
  - `wiki/etc/experiments/comp-018-upstream-complement-modulator-sweep/inputs/query-strategy.json` (lines 1–93) + `targets.json` (lines 1–124) — Phase 1 query macros (mechanism-name-only)
  - `wiki/etc/experiments/comp-018-upstream-complement-modulator-sweep/phase-2/phase-2-multilingual-findings.md` (lines 1–260) — Phase 2 correction with Houttuynia + canonical discipline statement (line 230)
  - `wiki/etc/experiments/comp-020-upstream-complement-verification-rerun/inputs/query-strategy.md` (lines 1–69) — brief-scrubbed re-run query strategy
  - `wiki/etc/experiments/comp-015-t-axis-adjuvant-urate-mapping/inputs/provenance.md` (lines 1–40) — cordycepin / eurycomanone / icariin / echinacoside identity sources
  - `wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/inputs/query_strategy.md` (lines 1–41) — Q141K + ALLN-346 keyword list
  - `wiki/etc/experiments/comp-016-t-abcg2-suppression-evidence-mining/inputs/provenance.md` (lines 1–23) — WebSearch query log
  - `wiki/etc/experiments/comp-017-intestinal-abcg2-sex-dimorphism-public-data-mining/inputs/provenance.md` (lines 1–30) — GTEx/HPA biobank-style scan
  - `wiki/etc/experiments/comp-024-complestatin-bgc-lbp-feasibility/inputs/provenance.md` (lines 1–30) — BGC engineering sources
  - `wiki/etc/experiments/comp-007-food-grade-hdaci-screen/inputs/candidates.json` (lines 1–50 sampled) — Western-food HDACi screen
- **comp-NNN wiki stub pages** (read for headline framing):
  - `wiki/upstream-complement-modulator-sweep-computational.md` (lines 1–102) — Phase 2 reframing
  - `wiki/upstream-complement-verification-rerun-computational.md` (lines 1–65) — brief-scrubbed re-run
  - `wiki/upstream-complement-assay-format-mapping-computational.md` (lines 1–66) — assay-format-focused, no lit-scan reframing
  - `wiki/tcm-gout-compound-triage-computational.md` (lines 1–63)
  - `wiki/medicinal-mushroom-compound-mapping-computational.md` (lines 1–125)
- **Sweep daemon prompt templates:**
  - `scripts/sweep-prompt-1-propagate.md` — grep'd for multilingual/query-framing keywords; **no hits**
  - `scripts/sweep-prompt-2-synthesize.md` (lines 1–226) — global-multilingual default explicitly invoked at line 5; query-framing discipline NOT encoded
  - `scripts/sweep-prompt-3-review.md` — grep'd; **no hits**
  - `scripts/sweep-prompt-3-review-gpt55.md` — grep'd; **no hits**
- **Pre-2026-05-19 daemon synthesis logs** sampled: 7 of 39 contain "multilingual / cnki / chinese / traditional" keywords; representative examples checked include `logs/v4-synthesis-2026-05-08-e842754.md` (the synthesis that proposed comp-018 itself, anchored on multilingual reasoning) and `logs/v4-synthesis-2026-05-16-3c1ca4b.md` (the carnosine convergence synthesis citing TCM track redundancy)
- **H-card hypothesis files** sampled: `wiki/hypotheses/H04-tcm-rigor-intersection.md` (line 54 already invokes global-multilingual gating); `wiki/hypotheses/H06-medicinal-mushroom-complement-track.md` (lit-scan-derived hypothesis emerging from comp-014 reasoning)

---

## Per-target diagnosis

### comp-013 (TCM gout compound triage)

- **Query framing used:** Species-name + traditional-formula-name + traditional-pathology framing was *already operative* — every compound entry in `inputs/compounds.json` includes a `tcm_source` field with simplified-Chinese + pinyin labels (Smilax glabra 土茯苓 / Tu Fu Ling for astilbin; Rheum officinale 大黄 / Da Huang for rhein and emodin; Lonicera japonica 金银花 / Jin Yin Hua for luteolin; Atractylodes 苍术 / Cang Zhu as a Si Miao San component for atractylenolide-I). The sources list cites Si Miao San systematic review (PMC5360963) and Smilax glabra primary studies. ChEMBL coverage gap was explicitly documented (5/9 TCM compounds had zero ChEMBL data) — exactly the gap the query-framing rule targets.
- **Compound class:** TCM compounds with classical gout indication (URAT1, ABCG2, XO, NLRP3 axes).
- **Gap diagnosis:** **Likely partial.** The pre-existing species-name + formula-name framing means the highest-leverage compounds were already on the list. But the comp-013 compound corpus is bounded by the 9-compound seed list — Si Miao San is recognized as a formula but individual non-canonical components (e.g., Achyranthes bidentata = Niu Xi alkaloids, Cyathula officinalis = Chuan Niu Xi saponins, Phellodendron amurense = Huang Bai berberine variants beyond simple berberine) were not separately spawned. Bai Hu Jia Gui Zhi Tang (the classical gout-indicated companion formula to Si Miao San) and Smilax-enhanced regional variations (e.g., Tu Fu Ling Tang) were NOT explicitly queried by formula-name.
- **Estimated leverage:** **MEDIUM.** Core compound list is well-covered; formula-completeness gap could surface 3–10 additional compound entries (Achyranthes saponins, Cyathula triterpenes, Phellodendron-derived phellodendrine, possibly Plantago seed iridoids beyond aucubin).
- **What might have been missed:** Achyranthes saponins (URAT1-active per CNKI), Phellodendron amurense secondary alkaloids beyond berberine, Bai Hu Tang formula-level evidence (gypsum + Anemarrhena + rice + licorice), Plantago seed broader iridoid panel (catalpol, geniposidic acid). Whether any of these would change the final triage verdicts is unclear without re-scan, but the comp-013 frame did the bulk of the species-anchoring already.

### comp-014 (medicinal mushroom compound mapping)

- **Query framing used:** Mixed. The chokepoint-target mapping (Phase 3) was **mechanism-name framed** — ChEMBL `activity.json` per chokepoint UniProt → InChIKey intersection across 24 chokepoint targets. The breadth-aggregation layer (Phase 2) was *species-agnostic* — LOTUS + NPAtlas + KNApSAcK pulled species-of-origin records without traditional-formula anchoring. The species-name layer was preserved in `phase-5-anchor-species.json` (Ganoderma lucidum 灵芝 / 霊芝 / Reishi; Cordyceps militaris + Ophiocordyceps sinensis 冬虫夏草; Hericium 猴头菇; Trametes versicolor 云芝 / Kawaratake; Inonotus obliquus 桦褐孔菌; 18 species total with TCM names + Japanese names) — but Phase 5 multilingual deep-dive **WAS QUEUED, NOT EXECUTED** (per the wiki stub `medicinal-mushroom-compound-mapping-computational.md` line 59: "Phase 5 — Multilingual literature deep-dive... Queued"). Additionally, three East-Asian DBs (NPASS, TCMSP, HIT) and SwissTargetPrediction were **unreachable from the sandbox** (data-sources.json line 74–81 + wiki stub lines 70–81) — the LOTUS-only breadth gap is documented but not yet closed.
- **Compound class:** Medicinal mushrooms (TCM + Kampo + Korean ethnomycology core class).
- **Gap diagnosis:** **Likely yes, significant.** Phase 3's headline finding — berkeleyamides A/D / *Penicillium* CASP1 IC50 330/610 nM — surfaced via **mechanism-name (CASP1 IC50) query through ChEMBL**, not via traditional-name anchor. The traditional Lingzhi 灵芝 / Reishi anti-inflammatory CNKI corpus, the Kampo Yun Zhi 云芝 (Trametes PSK/PSP) NLRP3-priming literature, and the Cordyceps cicadae PINK1-mitophagy thread (PMID 40334761, surfaced only in Phase 5 deep-read) all sit in non-PubMed-indexed Chinese-language databases that the comp-014 pipeline was structurally unable to reach. The ADA chokepoint promotion (chokepoint-targets.json lines 137–145) came from Phase 5 deep-read of GLPP polysaccharide-peptide (G. lucidum, PMID 36385640, 40.6% UA reduction in HUA mice) — this finding **WAS surfaced by species-name + Chinese-clinical-evidence reading**, demonstrating the query-framing discipline already operating where the pipeline could execute it.
- **Estimated leverage:** **HIGH.** comp-014 explicitly has Phase 5 multilingual deep-dive queued + East-Asian DB pull queued. The combined gap is exactly the discipline this rule names. A focused re-scan applying traditional-formula-name (e.g., 灵芝孢子粉 = Lingzhi spore powder; 云芝多糖肽 = PSP; 桑黄 = Sang Huang / Inonotus sanghuang specifically) + traditional-pathology framing (痹证 bi-zheng / blood-stasis / damp-heat) + Japanese Kampo names (Reishi as 霊芝; Maitake D-fraction as グリフォラン / グリフォーラン) is likely to surface ≥10 additional chokepoint-relevant compounds the Phase 3 ChEMBL intersection missed.
- **What might have been missed:** Sang Huang (Inonotus sanghuang) HUA evidence — the wiki anchors Inonotus obliquus 桦褐孔菌 / chaga but not the related I. sanghuang species canonical in Chinese clinical use; Maitake (Grifola frondosa) glucan NLRP3 priming with Japanese RCT evidence; Auricularia auricula-judae 木耳 anti-platelet / vessel-wall inflammation (Lp-PLA2 axis) per CNKI; Hericium erinaceus 猴头菇 amycenone gut-barrier evidence missed in the Phase 3 ChEMBL UniProt join.

### comp-018 Phase 1 (upstream complement modulator sweep) — **canonical gap exemplar**

- **Query framing used:** **Mechanism-name-only.** The eight Phase 1 search macros in `inputs/query-strategy.json` lines 42–90 are all mechanism-anchored: `"complement C3 convertase" AND (inhibit* OR antagonist) AND (natural OR plant OR herbal OR flavonoid OR triterpene OR saponin OR polysaccharide OR fungal OR mushroom)`, `"complement system" AND "rosmarinic acid"`, `(berberine OR quercetin OR luteolin OR baicalein OR EGCG OR curcumin) AND complement AND (C3 OR convertase) AND IC50`, etc. The multilingual sources list (CNKI / WanFang / J-STAGE / KISS) was documented as "Phase 1 sample read; full ingestion deferred to Phase 2 if hits warrant" (query-strategy.json lines 24–40). The query framing was bounded by Western pharma mechanism vocabulary.
- **Compound class:** Natural-product complement modulators (small-molecule + polysaccharide + triterpene). Heavy overlap with TCM materia medica + Japanese Kampo + Tibetan medicine.
- **Gap diagnosis:** **Yes, demonstrated.** Phase 2 (2026-05-17) ran the corrected discipline and surfaced *Houttuynia cordata* as new tier-1 — the Chen Daofeng (Fudan) group had been publishing English-language papers on this for ≥14 years, but the mechanism-name query missed them because the Chen group anchors their papers on the species-name + traditional anti-complementary terminology, not on "C3 convertase inhibitor." Phase 2 also surfaced Tibetan medicine candidates (Myricaria wardii, Juniperus pingii), Korean Pharmacology Society candidates (Styrax japonica norlignans), Yamada/Kiyohara (Kitasato) Kampo polysaccharide thread covering Glycyrrhiza, Angelica acutiloba, Scutellaria barbata/baicalensis, Panax ginseng leaf, Viola yedoensis, Amomum tsao-ko, Malva verticillata, Imperata cylindrica, Rabdosia japonica, Artemisia princeps. **Phase 1 missed all of these via mechanism-name framing alone.**
- **Estimated leverage:** **HIGHEST.** This IS the canonical case — already corrected by Phase 2. No further re-scan needed for the complement-modulator domain; the Phase 2 work IS the corrected re-scan. **Operational lesson** (canonical statement at `phase-2-multilingual-findings.md` line 230): "the operational discipline is to query by traditional-medicine-formula-name + species-name in addition to mechanism-name. A 'C3 convertase inhibitor' query misses Houttuynia; a 'Houttuynia cordata anti-complementary' query catches it."
- **What might have been missed:** Already cataloged above — 13 additional compound entries surfaced by Phase 2.

### comp-020 (upstream complement verification rerun)

- **Query framing used:** `inputs/query-strategy.md` lines 8–9 explicitly enumerate "fungal, plant (phenolic / flavonoid / terpenoid / polysaccharide / lignan / alkaloid), bacterial, marine, dietary, FDA-approved, TCM, Kampo, Ayurvedic — all with equal initial weight" and "Multilingual default: PubMed + CNKI + WanFang + J-STAGE + KISS / RISS where queries support it" — but the per-node anchor queries (lines 14–20) still use mechanism-name framing: `"<node-name>" AND ("inhibitor" OR "antagonist" OR "modulator" OR "natural product" OR "extract")`. The compound-class breadth was applied but the *query pattern itself* was mechanism-name primary.
- **Compound class:** Same as comp-018 — natural-product complement modulators.
- **Gap diagnosis:** **Partial.** comp-020 is the brief-scrubbed verification re-run; it caught the rosmarinic acid over-promotion AND surfaced Helicteres benzofuran lignans as a tied tier-1 candidate. But it ran BEFORE the comp-018 Phase 2 finding that named the discipline. Houttuynia was not yet on its radar. The comp-020 query pattern is essentially comp-018 Phase 1 with breadth widened — same mechanism-name anchor.
- **Estimated leverage:** **LOW for re-scan.** The comp-018 Phase 2 work is the corrected version; comp-020 doesn't need a separate re-run unless the discipline gets refined further.
- **What might have been missed:** Houttuynia would have been missed by comp-020 too — confirmed by Phase 2 finding (Houttuynia was new in Phase 2, not present in comp-020 outputs).

### comp-029 / comp-021 (upstream complement assay format mapping)

Note: the user task brief named this as "comp-029" but the actual computational page is the assay-format mapping at comp-021 (`wiki/upstream-complement-assay-format-mapping-computational.md`). comp-029 is the combined CP0 systems model (`wiki/combined-cp0-systems-model-computational.md`). I audited comp-021 (assay-format mapping) since that was the intent based on description.

- **Query framing used:** N/A — comp-021 is **assay-format-focused**, not lit-scan-framed. It mines published IC50 values from comp-020's compound set across 6 canonical assay formats. No new query macros run.
- **Compound class:** Same as comp-018/020; inherits whatever scope they produced.
- **Gap diagnosis:** **Inherits the upstream gap.** comp-021 explicitly notes (wiki page line 58): "This run did not execute new CNKI / WanFang / J-STAGE direct queries; comp-020's partial-execution disclosure (§4.3) applies."
- **Estimated leverage:** **LOW** as a standalone re-scan target. It updates automatically if the upstream comp-018/020 compound list expands.

### comp-015 (T-axis adjuvant urate mapping)

- **Query framing used:** Species-name + traditional-name anchor was **already operative** — the four compounds (cordycepin / Cordyceps militaris; eurycomanone / Eurycoma longifolia; icariin / Epimedium; echinacoside / Cistanche) are all TCM / Ayurvedic-adjacent species-anchored. Bioavailability evidence pulled from species-anchored PK papers.
- **Compound class:** Adjuvant compounds modulating the androgen-urate axis; overlap with traditional aphrodisiac/tonic compounds.
- **Gap diagnosis:** **Likely no.** Compound selection was already species-anchored.
- **Estimated leverage:** **LOW.** Possibly minor — could check if additional Cistanche / Epimedium constituents beyond echinacoside/icariin (e.g., other Cistanche phenylethanoid glycosides like acteoside / verbascoside) have T-axis evidence in Chinese literature.

### comp-019 (gut-lumen uricase × ABCG2 genotype stratification)

- **Query framing used:** Mechanism-name + product-name framed (Q141K / rs2231142 / ALLN-346 / PRX-115 / ABCG2 dysfunction / Mendelian randomization / Ichida-Matsuo functional classification). One ChiCTR query was attempted (`query_strategy.md` line 14) explicitly to surface China-registered oral uricase trials in Asian Q141K-enriched cohorts.
- **Compound class:** Western pharmaceutical uricase + Western biobank ABCG2 data.
- **Gap diagnosis:** **Likely no.** This is engineered-protein PK/PD + biobank stratification work — the traditional-name framing does not apply.
- **Estimated leverage:** **LOW.** Possibly worth a minor follow-up: are there ChiCTR-registered uricase trials in hyperuricemic Asian cohorts that PubMed missed? But the absence of pre-stratified Q141K data in the canonical trials is already documented as "does not exist."

### comp-016 / comp-017 (T-axis ABCG2 evidence mining + intestinal ABCG2 sex dimorphism)

- **Query framing used:** WebSearch-style English-language pharma terminology (testosterone / DHT / androgen / ABCG2 / BCRP / Caco-2 / GTEx / HPA). Both runs documented sandbox blocking on PMC + portal access.
- **Compound class:** Western pharmacology + biobank.
- **Gap diagnosis:** **Likely no.** Sex-hormone × transporter expression sits in Western pharma context; traditional-name framing not load-bearing.
- **Estimated leverage:** **LOW.** Not a re-scan candidate.

### comp-024 (complestatin BGC × LBP feasibility)

- **Query framing used:** Genomic / BGC architecture queries (MIBiG BGC0000326, *Streptomyces lavendulae*, NRPS module structure, heterologous-expression precedent).
- **Compound class:** Bacterial NRPS-derived cyclic peptide (Western pharma natural-product chemistry context — actinomycete-derived).
- **Gap diagnosis:** **Likely no.** Complestatin is Western-discovered Actinomycetota chemistry; no traditional-medicine analog corpus.
- **Estimated leverage:** **LOW.**

### comp-027 (disulfiram dose modeling)

- **Compound class:** FDA-approved Western drug (Antabuse) repurposed for CASP1/NRF2 axes.
- **Gap diagnosis:** **Likely no.** Western pharma drug; traditional-name framing not applicable.
- **Estimated leverage:** **LOW.**

### comp-007 (food-grade HDACi screen)

- **Query framing used:** Mechanism-name (HDAC inhibitor) + Western-dietary food-source anchoring (butyrate / sulforaphane / allyl mercaptan / quercetin / EGCG etc.).
- **Compound class:** Western-dietary + GRAS-classified small molecules.
- **Gap diagnosis:** **Possibly partial.** The HDAC inhibitor literature has significant Chinese-language coverage for compounds like Astragalus polysaccharides, Sang Huang melanin, Lingzhi triterpenoids — but comp-007's explicit scope was "food-grade dietary GRAS" not "traditional natural-product." If the scope were widened to include TCM-grade compounds, traditional-name queries could surface additional HDACi candidates.
- **Estimated leverage:** **LOW–MEDIUM.** Out of scope for comp-007 as designed; could be a separate comp-NNN if Q141K-ABCG2 rescue via HDAC6 wants TCM-grade chaperone candidates.

### comp-004 (supplement ABCG2 antagonism)

- **Compound class:** Western OTC supplements (mostly).
- **Gap diagnosis:** **Likely no for primary scope.** Supplement scope was deliberately Western OTC.
- **Estimated leverage:** **LOW.**

### Engineering-side comp-NNN (comp-001/002/005/006/010/011/012/022/030/032/034 + comp-008/009/033/035/036)

- **Compound class:** Sequence engineering, protease stability, cassette compatibility, mRNA/LNP, intra-articular formulation, siRNA target selection.
- **Gap diagnosis:** **No.** No literature-search component where traditional-name framing applies.
- **Estimated leverage:** **NONE.**

### Sweep daemon prompts (Pass 1 / 2 / 3 templates)

- **Pass 1 (`sweep-prompt-1-propagate.md`):** No multilingual / query-framing language. Pass 1 is single-page propagation, less affected — its role is propagating findings within a known wiki corpus, not literature discovery.
- **Pass 2 (`sweep-prompt-2-synthesize.md`):** Global-multilingual default explicitly invoked at line 5 ("Read CLAUDE.md first... the global-multilingual research default rule"). **Query-framing discipline NOT encoded** — Pass 2 has awareness that non-English-source angles can surface new connections, but no operational guidance on traditional-formula-name + species-name + traditional-pathology framing as a query pattern. Pass 2 reading the corpus is doing synthesis over already-ingested content, not doing primary lit-scan — but a query-framing-aware Pass 2 would flag when an existing wiki page's evidence base appears mechanism-name-only and recommend a re-scan.
- **Pass 3 (both review prompts):** No multilingual or query-framing language. Pass 3 critiques Pass 2 findings, not raw literature.
- **Implication:** Pass 2 syntheses across 39 pre-2026-05-19 logs operated with global-multilingual awareness but without the operational query-framing discipline. The `logs/v4-synthesis-2026-05-08-e842754.md` is the canonical example where Pass 2 reasoning ABOUT the multilingual gap (proposing comp-018 itself) was good but the operational guidance that would have prevented comp-018 Phase 1's mechanism-name framing was absent.

### Pre-2026-05-19 sweep cycle logs (v3-* / v4-*)

- Sampled 7 of 39 logs containing multilingual/chinese/traditional keywords (counts: `logs/v4-synthesis-2026-04-25-a280c0d.md`: 2 hits, `logs/v4-synthesis-2026-04-25-622d2e2.md`: 2, `logs/v4-synthesis-2026-04-25-b5c9116.md`: 1, `logs/v4-synthesis-2026-05-05-d6b4210.md`: 6, `logs/v4-synthesis-2026-05-08-e842754.md`: 6, `logs/v4-synthesis-2026-05-16-91acf49.md`: 6).
- The 2026-05-08 log (which proposed comp-018) explicitly framed the opportunity as "Run the Fungal Complement-Modulator Multilingual Sweep (comp-018) using Paperclip + PubMed + CNKI/J-STAGE to exhaustively map natural-product hits at upstream complement nodes" — multilingual awareness was operative, but the actual comp-018 implementation reverted to mechanism-name framing because the Pass-2-spawned brief did not include the discipline operationally.
- Diagnosis: Pass 2 syntheses were aware of multilingual opportunity but did NOT consistently translate it into operational query-framing guidance for downstream comp-NNN briefs. This is the meta-gap.

---

## Ranked re-scan candidates

### HIGH leverage (re-scan strongly recommended)

1. **NLRP3 × Lingzhi 灵芝 spore-powder + Yun Zhi 云芝 (Trametes PSK/PSP) + Maitake グリフォラン anti-inflammatory mechanism.** Re-scan prompt: "灵芝孢子粉 anti-inflammatory mechanism NLRP3 / IL-1β" + "云芝多糖肽 PSP PSK NLRP3 priming β-glucan" + "舞茸 / マイタケ Maitake D-fraction NLRP3 inflammasome." Anchors: comp-014's `phase-5-anchor-species.json` Ganoderma + Trametes versicolor + Grifola frondosa rows. Expected yield: ≥5 NLRP3-priming polysaccharide candidates not currently in `wiki/nlrp3-exploit-map.md` or `wiki/medicinal-mushroom-compound-mapping-computational.md` Phase 3 ChEMBL intersection.

2. **URAT1 × Si Miao San 四妙散 / Bai Hu Jia Gui Zhi Tang 白虎加桂枝汤 / Smilax glabra 土茯苓 formula-level evidence.** Re-scan prompt: "四妙散 hyperuricemia URAT1" + "白虎加桂枝汤 痛风" + "土茯苓 / Tu Fu Ling 高尿酸血症." Anchors: comp-013's compound list (Si Miao San is named but components not exhaustively queried by formula-name; Bai Hu Tang variants not queried). Expected yield: Achyranthes saponins, Cyathula triterpenes, Phellodendron non-berberine alkaloids, Plantago iridoid panel beyond aucubin (3–10 additional compound entries).

3. **XO × Jiang Huang 姜黄 (turmeric curcuminoids) + Wu Mei Wan 乌梅丸 + Huo Xiang Zheng Qi 藿香正气 traditional formulas.** Re-scan prompt: "姜黄 / Jiang Huang xanthine oxidase 痛风" + "curcuminoid demethoxycurcumin XO" + "乌梅丸 hyperuricemia." Anchors: comp-013 luteolin XO 550 nM benchmark; XO chokepoint in modality-chokepoint-matrix.md. Expected yield: at least demethoxycurcumin + bisdemethoxycurcumin XO data (Chinese-clinical literature reports IC50 in the 1–10 μM range); possibly Wu Mei (Prunus mume) organic acid XO data.

4. **Mushroom × HDAC6 (Q141K-ABCG2 rescue chaperone candidates).** Re-scan prompt: "灵芝三萜 ganoderic acid HDAC6 / HDAC inhibitor" + "桑黄 Sang Huang HDAC histone deacetylase" + Korean ethnomycology HDAC inhibitor surveys. Anchors: comp-007 food-grade HDACi compound list (Western-dietary scope); comp-014 Phase 3 found HDAC6 was not a top fungal-compound chokepoint hit via ChEMBL, but Phase 5 deep-read identified no HDAC6 candidates either — gap may be query-framing rather than absence.

5. **Houttuynia × CP1 dual-mechanism + Tibetan medicine (Myricaria + Juniperus) complement modulation deepening.** Already queued — `logs/houttuynia-cp1-dual-mechanism-lit-scan-2026-05-19.md` exists in 2026-05-19 sweep. Lower priority for ADDITIONAL re-scan because the most recent walkthrough already actioned this.

### MEDIUM leverage

6. **comp-014 Phase 5 multilingual deep-dive execution.** Already queued in the comp-014 phase plan (`medicinal-mushroom-compound-mapping-computational.md` line 59). The discipline rule promotion is the right moment to fire this. Expected yield: ≥10 additional fungal compound × chokepoint hits across the 18 anchor species, with strongest gain on TXNIP / NRF2 / PINK1 axes that current ChEMBL intersection underweights.

7. **comp-014 East-Asian DB re-pull (NPASS / TCMSP / HIT / BATMAN-TCM-2) from non-sandboxed environment.** Documented as Phase 2 gap; the LOTUS-only breadth is structurally Western-skewed. Expected yield: 3–5K additional fungal compound entries not in LOTUS / NPAtlas / KNApSAcK.

8. **Cordyceps × ADA chokepoint deepening.** ADA was promoted to first-class chokepoint via comp-014 Phase 5 (chokepoint-targets.json lines 137–145, anchor PMID 36385640 GLPP 40.6% UA reduction). The promotion came from species-name reading; deepening should include Cordyceps cicadae (PMID 40334761 PRELIMINARY chokepoint), Cordyceps militaris, Ophiocordyceps sinensis Chinese-clinical literature on ADA / mitophagy.

9. **Mushroom × Lp-PLA2 (Brian-relevant vessel-wall biomarker).** Lp-PLA2 was named in comp-014 `chokepoint-targets.json` as "unmapped territory." Re-scan: "木耳 / mu er Auricularia auricula-judae anti-platelet vessel inflammation" + Yamada/Kiyohara Kampo polysaccharide Lp-PLA2 data. Lower priority than NLRP3/URAT1/XO but Brian-relevant.

### LOW leverage (Western pharma / biobank / engineering domains)

10. comp-019 (Q141K ALLN-346/PRX-115) — minor possible ChiCTR re-check.
11. comp-007 (food-grade HDACi) — TCM-grade HDACi as a separate comp-NNN if the chassis-pending-interventions thread wants TCM-grade chaperone candidates.
12. comp-016/017 (T-axis biobank) — no traditional-name angle.
13. comp-024 (complestatin BGC) — actinomycete Western pharma context.
14. comp-027 (disulfiram dose modeling) — Western pharma drug.
15. comp-004 (Western OTC supplements) — out of scope by design.

---

## Process improvements queued

### Encode the discipline in sweep daemon prompts

- **Pass 2 prompt update needed.** `scripts/sweep-prompt-2-synthesize.md` already invokes "global-multilingual research default" at line 5. Add a query-framing-discipline note alongside it: when Pass 2 surfaces a finding in a non-Western-medicine compound class (TCM / Kampo / Ayurvedic / medicinal mushroom / classical-formula-anchored evidence), flag whether the underlying corpus pages appear to have been built from mechanism-name-only queries. Recommend a re-scan with traditional-name framing as a suggested action.
- **Pass 1 prompt update (lower priority).** Pass 1 is propagation, not discovery — but if a propagated finding lands on a wiki page that's mechanism-name-only, Pass 1 could flag it for sweep walkthrough attention.
- **Pass 3 prompt update.** Pass 3 review could include a "is this finding's evidence base potentially mechanism-name-biased?" check as one of its critique categories.

### Encode the discipline in new-comp-NNN scaffolding

- The `.claude/skills/new-comp-experiment` skill (already invoked when Brian asks "could we model this computationally?") should add a query-framing checklist item to its subagent brief template: **"If the compound class includes TCM / Kampo / Ayurvedic / medicinal mushroom / non-Western traditional-medicine compounds, the query strategy MUST include traditional-formula-name + species-name + traditional-pathology framing alongside mechanism-name queries."**
- The `inputs/query-strategy.json` template should have a required field documenting which traditional-name anchors were used (or explicitly noting "not applicable — Western pharma compound class") to make the discipline auditable.

### Encode in subagent brief hygiene

- The "subagent brief hygiene" discipline already in CLAUDE.md (Rule 4 sister discipline) should add: when composing a literature-scan subagent brief, the brief MUST include the query-framing discipline alongside the pre-commit grep-verify gate. Both gates close different failure modes; the new query-framing gate closes the upstream framing gap, the existing grep-verify gate closes the inside-output verification gap.

### Add to manual-literature-mining.md

- `wiki/etc/manual-literature-mining.md` is the canonical operational doc for lit-scan discipline. Add a §"Query framing for non-Western compound classes" section codifying the rule with the Houttuynia case + the URAT1/XO/NLRP3 generalizations. Brian's walkthrough action — promoted manually since this audit doesn't modify wiki/*.

---

## Limitations

- **Not all 32 comp-NNN folders inspected at depth.** I sampled the ones with explicit literature-scan components (comp-013, 014, 015, 016, 017, 018, 019, 020, 021, 024, 027, 007, 004) and inferred low-leverage for the engineering-side ones from their wiki stubs and folder structure without deep-reading every `inputs/*.md` file. If any engineering comp-NNN secretly has a hidden traditional-medicine compound thread, this audit missed it.
- **Pass 1 / Pass 3 prompt templates inspected via grep only.** I confirmed they contain no `multilingual / cnki / wanfang / j-stage / traditional` keywords but didn't read them line-by-line. A more thorough audit might find indirect references.
- **Daemon synthesis logs sampled, not exhaustively read.** I sampled 7 of 39 v4 logs (the ones with multilingual keyword hits) and read two in detail. The other 32 may contain subtle query-framing references I missed.
- **Pre-comp-013 wiki pages not deeply audited for lit-scan provenance.** Some wiki pages (e.g., `wiki/tcm-modern-rigor-intersection.md`, `wiki/medicinal-mushroom-complement-track.md`, `wiki/nlrp3-exploit-map.md`) were built from lit scans whose provenance is mixed between Brian's manual reading and comp-NNN outputs. Whether those pages' underlying scans used the discipline is not always recoverable from the wiki text.
- **No actual re-scans run.** This audit is diagnostic; no re-scan candidates were verified by actually running them. The leverage estimates are based on framing-gap analysis + comp-018 Phase 2 empirical precedent, not on counterfactual evidence.
- **DeepSeek V4-Pro / Qwen translation cross-check coverage of past scans not audited.** The 2026-05-19 CLAUDE.md rule includes a two-model translation protocol; whether past comp-018 Phase 2 + comp-014 Phase 5 multilingual reads followed it correctly is a separate audit question.

---

## Citation provenance summary

Load-bearing claims in this audit trace to specific files + line numbers:

| Claim | Source |
|---|---|
| CLAUDE.md query-framing rule canonical statement (2026-05-19 addition) | `CLAUDE.md` lines 263–269 |
| comp-018 Phase 1 mechanism-name-only query macros | `wiki/etc/experiments/comp-018-upstream-complement-modulator-sweep/inputs/query-strategy.json` lines 42–90 |
| comp-018 Phase 2 canonical discipline statement | `wiki/etc/experiments/comp-018-upstream-complement-modulator-sweep/phase-2/phase-2-multilingual-findings.md` line 230 |
| Phase 2 Houttuynia missed-by-Phase-1 anchor | `wiki/upstream-complement-modulator-sweep-computational.md` lines 76–77, 91 |
| comp-020 query pattern (mechanism-name primary) | `wiki/etc/experiments/comp-020-upstream-complement-verification-rerun/inputs/query-strategy.md` lines 14–20 |
| comp-013 species-name + formula-name framing already operative | `wiki/etc/experiments/comp-013-tcm-gout-compound-triage/inputs/compounds.json` lines 6–11, 22–36, 53–101, 121–135, 137–151 |
| comp-014 Phase 5 multilingual deep-dive QUEUED, not executed | `wiki/medicinal-mushroom-compound-mapping-computational.md` line 59 (Phase 5 row) |
| comp-014 East-Asian DB unreachable (NPASS/TCMSP/HIT) | `wiki/medicinal-mushroom-compound-mapping-computational.md` lines 70–81; `wiki/etc/experiments/comp-014-medicinal-mushroom-compound-mapping/inputs/data-sources.json` lines 73–110 |
| comp-014 Phase 5 anchor-species traditional-name list (18 species with TCM + Japanese + Korean names) | `wiki/etc/experiments/comp-014-medicinal-mushroom-compound-mapping/inputs/phase-5-anchor-species.json` lines 6–60 |
| comp-014 ADA chokepoint promotion via species-name reading | `wiki/etc/experiments/comp-014-medicinal-mushroom-compound-mapping/inputs/chokepoint-targets.json` lines 137–145 |
| Pass 2 sweep prompt global-multilingual default; no query-framing | `scripts/sweep-prompt-2-synthesize.md` line 5 (only multilingual hit across all four prompt templates) |
| 2026-05-08 daemon log proposing comp-018 with multilingual framing | `logs/v4-synthesis-2026-05-08-e842754.md` lines 32–36, 90 |
| comp-019 query strategy (mechanism + product name, Western pharma scope) | `wiki/etc/experiments/comp-019-gut-lumen-uricase-abcg2-genotype-stratification/inputs/query_strategy.md` lines 17–41 |
| comp-015 species-anchored compound identity | `wiki/etc/experiments/comp-015-t-axis-adjuvant-urate-mapping/inputs/provenance.md` lines 22–37 |
| H04 already names global-multilingual gating | `wiki/hypotheses/H04-tcm-rigor-intersection.md` line 54 |
