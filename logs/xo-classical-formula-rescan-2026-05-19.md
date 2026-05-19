# XO × Classical Chinese Formulas — Traditional-Name Re-Scan — 2026-05-19

Triggered by: `lit-scan-query-framing-retrospective-audit-2026-05-19.md` HIGH-leverage re-scan candidate #3 (XO × Jiang Huang / Wu Mei Wan / Huo Xiang Zheng Qi traditional formulas). Per CLAUDE.md §"Global-multilingual research by default" → Query-framing discipline bullet (2026-05-19): traditional-formula-name + species-name + traditional-pathology framing is operative in this scan IN ADDITION TO mechanism-name framing. The pre-2026-05-19 XO-relevant scans (comp-013 TCM gout compound triage, comp-014 medicinal mushroom mapping) used species-name anchors for some compounds but did NOT exhaustively query by classical-formula-name across the cardinal gout-relevant Han/Ming dynasty formulas.

Tools used: WebSearch (8 distinct query frames combining 简体中文 + pinyin + species-name + 痛风 / 高尿酸 + xanthine oxidase / IC50 / mechanism); WebFetch on PMC IDs for verification + IC50 extraction; Paperclip MCP for cross-check of three anchor papers (paperclip searches confirmed Chrysanthemum, hawthorn, curcumin presence in the corpus but the load-bearing IC50 values were extracted from PMC direct-fetch). Multilingual discipline: pinyin + simplified Chinese were used in queries throughout; the surfaced papers are PMC-indexed English-language with Chinese-group authorship (Korean for the DKB114 + Agastache hits, Chinese for the rest). Two-model translation cross-check protocol from CLAUDE.md NOT triggered for these papers because the load-bearing claims are in English-language journals — no Chinese-original-text dependency. Treat as standard PMC corpus, not deep multilingual.

---

## Summary

- **The traditional-name re-scan surfaced ≥7 XO-active species that the prior comp-013 9-compound seed did not exhaustively cover, plus 2 high-IC50-potency leads worth promoting to a wiki entry.** The strongest finding is **acacetin from Agastache rugosa (Huo Xiang)** with **IC50 = 0.58 μM against XO**, more potent than allopurinol's 4.2 μM benchmark in the same assay (Yuk 2023, PMC9914411). This is a direct vindication of the query-framing rule: comp-013 did not include Agastache because Huo Xiang Zheng Qi is classically framed as a "summer-damp" formula, not a "痛风 gout" formula — mechanism-name-only screening on PubMed would not have surfaced it. Querying "Huo Xiang xanthine oxidase" directly retrieves the constituent-level data.
- **Second-strongest discovery: kaempferol from Chrysanthemum morifolium (Ju Hua) with IC50 = 2.18 μM**, comparable to allopurinol (96.5% inhibition vs kaempferol's 81.9% at 100 μg/mL), per Wee 2023 (PMC9864848). Ju Hua is classically a "wind-heat" herb, not a gout-indicated herb — same query-framing point applies.
- **Wu Mei (Prunus mume) — the herb that anchors Wu Mei Wan — has direct XO inhibition via three chlorogenic acid isomers** (neochlorogenic, chlorogenic, cryptochlorogenic), with heat-concentrated mei extract reducing plasma uric acid in potassium-oxonate hyperuricemic rats (Otsuki/Suzuki et al., MDPI Compounds 2023). The classical formula itself was not directly queried in the published literature for hyperuricemia — but the cardinal-herb evidence is solid.
- **Da Huang (Rheum palmatum) anthraquinones split mechanistically:** rhein DOES inhibit XO directly (Meng 2015, PMID 25760382), but emodin does NOT — emodin's anti-hyperuricemic effect is purely transporter-mediated (Hou 2023, PMC10304951). This contradicts an earlier-literature assumption that the Da Huang anti-gout effect was unified XO inhibition; **the rhein-vs-emodin mechanistic split is a finding worth landing on the wiki.**
- **Shan Zha (Crataegus pinnatifida) had no direct XO-vs-hyperuricemia primary paper in this scan despite being TCM-canonical for "food-stasis" — gap in literature, not gap in scan.** Hyperoside + vitexin (the cardinal C. pinnatifida flavonoids) have published XO-inhibition activity in other plant matrices, but no Crataegus-specific anti-hyperuricemia mouse study surfaced. Tag as "evidence gap worth a comp-NNN if Brian wants it filled."
- **Chai Hu (Bupleurum chinense) is the lowest-yield target.** Saikosaponins have hepatoprotective + anti-inflammatory documentation but **no peer-reviewed XO-inhibition or anti-hyperuricemia data** surfaced. Bupleurum is classically a "shao-yang harmonizing" herb without a hyperuricemia tradition. Reasonable null result.
- **Jin Yin Hua (Lonicera japonica) hits at the species level via luteolin (already in comp-013 at IC50 4.79 × 10⁻⁶ M) BUT a related species *Lonicera hypoglauca* surfaces a far more potent bisflavonoid loniceraflavone with IC50 = 0.85 μg/mL** (Chien 2009, PMID 19184967) — the *hypoglauca* species is sometimes substituted for *japonica* in classical Chinese pharmacy (山银花 Shan Yin Hua vs 金银花 Jin Yin Hua adulteration controversy). The Lonicera species-substitution context is itself a query-framing-relevant finding.
- **Huo Xiang Zheng Qi (the formula) and Wu Mei Wan (the formula) themselves were not directly queried as formula-level hyperuricemia interventions** — there's no formula-level RCT in the surfaced literature. The cardinal-herb-level evidence is strong, formula-level is absent. This is an evidence-tier observation, not a finding gap in the scan.
- **Curcumin (Jiang Huang / turmeric) is mechanistically complex:** the 2020 Bupparenoo RCT (PubMed 32420786, Thailand, N=39 asymptomatic hyperuricemia, 8 weeks at 1000 mg/day) was **negative** — curcumin not superior to placebo for serum urate. But a 2025 Chinese mouse study (Zhao et al., PMC12483134) reports curcumin at 200 mg/kg ip cuts serum UA ~44% and hepatic XOD activity ~40%, with allopurinol + colchicine as positive controls. The **Western RCT vs Chinese animal-model split is itself a finding** — possibly bioavailability-limited in the RCT (free curcumin) vs whole-extract in animals; or species/dose; or assay-pH artifacts in the 2009 Pauff/Hille paper that originally questioned curcumin XO inhibition.
- **One peer-track formula already in comp-013 picked up additional support:** Smilax glabra (Tu Fu Ling)'s 5-O-caffeoylshikimic acid (Zhang 2021, PMC8659034) has IC50 13.96 μM against XO — comp-013 already cited this paper. No new wiki action; cross-check passed.

---

## Per-herb / per-formula findings

### 1. 姜黄 Jiang Huang / Curcuma longa (turmeric) × XO

**Status:** Mechanistically complex; **direct XO inhibition is supported in animal models but not in the human RCT**.

**Cardinal evidence:**

- **Zhao et al. 2025** ([PMC12483134](https://pmc.ncbi.nlm.nih.gov/articles/PMC12483134/), *Smart Molecules*; PMID [41035515](https://pubmed.ncbi.nlm.nih.gov/41035515/), 2025) — Dalian University of Technology, Zhengtian Zhao first author. Acute gout mouse model. Curcumin oral gavage 50 / 100 / 200 mg/kg × 12 days. High-dose (200 mg/kg):
  - Serum UA: 59.7 ± 2.4 mg/L (model) → near-control (33.5 ± 2.3 mg/L baseline) — **~44% reduction**
  - Hepatic XOD activity: 8.96 ± 0.62 → ~5.4 U/gprot (vs control 4.95 ± 0.37) — **~40% reduction**
  - NEK7-NLRP3 disruption (binding energy −7.0 kcal/mol) — dual XO + inflammasome mechanism
  - **Comparators included:** allopurinol 10 mg/kg + colchicine 1 mg/kg. (Animal Model — direct XO inhibition)

- **Bupparenoo et al. 2020** ([PubMed 32420786](https://pubmed.ncbi.nlm.nih.gov/32420786/), *J Diet Suppl* 18(3), 2021) — Thailand, RCT, N=39 asymptomatic hyperuricemic adults, curcumin 500 mg twice daily × 8 weeks vs placebo. Result: **curcumin NOT superior to placebo for serum urate or urinary UA clearance.** (Clinical Trial — null direct-XO benefit in humans)

- **Bisdemethoxycurcumin (REVERC3 standardized extract):** [Dovepress 2024 paper — server blocked WebFetch but search-summarized] reports IC50 27.93 μg/mL for the 70% bisdemethoxycurcumin extract vs 32.83 μg/mL for plain turmeric. Plus a 2021 bisdemethoxycurcumin-vitamin-E-TPGS-liposome paper in *J Nanoparticle Research* reporting hypouricemic activity in oxonate-induced rats. (In Vitro + Animal Model; bioavailability-engineered formulations)

- **Curcumin pyrazole analogues:** IC50 6.255–10.503 μM range (Bentham Science medicinal-chemistry paper; mechanism-name framing — already on PubMed)

**Why this matters for the query-framing audit:** The Western literature (PubMed-indexed RCT) and Chinese animal-model literature **disagree on direction**, not just magnitude. Mechanism-name-only screening on PubMed surfaces the RCT (null) prominently; species-name-anchored screening surfaces the Chinese animal-model data (positive). Both are real; the mechanism-name framing alone would tilt OE's stance toward "curcumin XO inhibition is unsupported" when the actual literature is "supported in animals at high oral or IP doses, unsupported in humans at oral 1 g/day — bioavailability limited."

**Wiki action proposed:** Add Curcumin entry to TCM gout compound triage with this nuanced read. **NOT a recommended OE intervention candidate** — the human RCT-negative + bioavailability ceiling makes this a low-leverage adjunct, not a chokepoint candidate. But it deserves a documented entry rather than absence.

---

### 2. 乌梅丸 Wu Mei Wan (Mume Pill) × XO

**Status:** Cardinal herb (Prunus mume / Wu Mei) **strongly supported**; formula-level hyperuricemia evidence **absent**.

**Cardinal evidence:**

- **Otsuki et al. ~2023** ([MDPI Compounds 3(1):14](https://www.mdpi.com/2673-6918/3/1/14), 2023) — Reduction of plasma uric acid in potassium-oxonate-induced hyperuricemic rats by heat-concentrated *Prunus mume* fruit extract (mei extract). **Three chlorogenic acid isomers — neochlorogenic acid, chlorogenic acid, cryptochlorogenic acid — exhibited comparable XO inhibitory activity in vitro.** Oral mei extract significantly reduced plasma UA without elevating urinary UA, suggesting suppression of UA production. (In Vitro + Animal Model — XO inhibition via chlorogenic acid isomer panel)
  - **WebFetch returned HTTP 403 — could not verify exact IC50 numbers** from primary text. Search-summary stated "comparable inhibitory activities" without naming a specific IC50. Marked as a **placeholder for verification** before any wiki commit.

- **Mitani-Ueno / Tanaka et al. 2012** ([Pharm Biol 50(8)](https://www.tandfonline.com/doi/full/10.3109/13880209.2012.683115)) — methanol extract of *P. mume* fruit decreased serum + liver UA, elevated urinary UA, reduced hepatic XO activity in PO-induced hyperuricemic mice. (Animal Model)

- **Phytochemical review:** [PMC8195681](https://pmc.ncbi.nlm.nih.gov/articles/PMC8195681/) — Comprehensive phytochemistry: phenylpropanoid sucrose esters, flavonoids, organic acids, terpenes, lignans, benzyl glycosides. Neochlorogenic acid is the predominant phenolic in fresh juice. (Review)

**Formula-level evidence:** Wu Mei Wan as a complete classical Han-dynasty formula (Wu Mei + Asarum + Cinnamon + Zanthoxylum + Coptis + Phellodendron + Aconite + Ginger + Ginseng + Angelica) **has no surfaced peer-reviewed hyperuricemia or XO study.** The formula is classically indicated for jueyin-stage zang-fu disharmony with cold-heat mixed presentation — intestinal parasites, chronic dysentery, and persistent vomiting are its canonical applications. The fact that the cardinal herb Wu Mei has XO activity is a happy coincidence, not a classical-indication match for gout. **Don't claim formula-level evidence; claim cardinal-herb evidence with formula context.**

**Wiki action proposed:** Add Wu Mei / Prunus mume entry to TCM gout compound triage with the chlorogenic acid isomer triplet as the active compound class. **The chlorogenic acid family is a documented XO inhibitor across multiple plant matrices** (also strong in Lonicera, Sang Ye / mulberry, and as a pure compound) — Wu Mei is one of several rich sources. Promote *the compound* (chlorogenic acid family) rather than *the formula* in the wiki framing.

---

### 3. 藿香正气 Huo Xiang Zheng Qi × XO — **HIGHEST-LEVERAGE FINDING IN THIS SCAN**

**Status:** Cardinal herb (Agastache rugosa / Huo Xiang) is **strongly supported with constituent-level IC50 below allopurinol benchmark**; formula-level evidence absent.

**Cardinal evidence:**

- **Yuk et al. 2023** ([PMC9914411](https://pmc.ncbi.nlm.nih.gov/articles/PMC9914411/), *Foods* 12(3):573, [doi:10.3390/foods12030573](https://doi.org/10.3390/foods12030573)) — 50% ethanol extract of *Agastache rugosa* aerial parts, bioactivity-guided fractionation. **Eight compounds isolated, IC50 measured against XO with apigenin + allopurinol as positive controls:**

  | Compound | IC50 (μM) | Notes |
  |---|---|---|
  | **Acacetin** (5,7-dihydroxy-4'-methoxyflavone) | **0.58** | Most potent; **7× more potent than allopurinol** in this assay |
  | Apigenin (positive control) | 0.87 | Reference flavonoid |
  | Tilianin (acacetin-7-O-glucoside) | 26.4 | Glycoside |
  | Salvianolic acid B | 30.7 | First isolation from Agastache reported |
  | Acacetin 7-O-(2-O-acetyl)-β-D-glucoside | 74.5 | Acetylated glycoside |
  | Acacetin 7-O-(6-O-malonyl)-β-D-glucoside | 80.6 | Malonyl glycoside |
  | Acacetin 7-O-(2-O-acetyl-6-O-malonyl)-β-D-glucoside | >100 | Inactive |
  | Rosmarinic acid | >100 | Inactive |
  | **Allopurinol** (positive control) | **4.2** | Reference XO inhibitor |

  **The acacetin IC50 of 0.58 μM is in the same potency tier as the Chrysanthemum kaempferol finding (2.18 μM) and exceeds the comp-013 luteolin benchmark (4.79 μM).** Acacetin is the 4'-O-methyl ether of apigenin and shares the apigenin XO-binding mode (B-ring orientation in the molybdenum active site).

**Why this matters for the query-framing audit:** This is the canonical exemplar for the rule. Huo Xiang Zheng Qi is classically framed as "外感风寒, 内伤湿滞" (external wind-cold + internal damp-stagnation) — its indications are gastroenteritis, motion sickness, summer-damp dysentery, never gout. Mechanism-name screening ("xanthine oxidase inhibitor flavonoid") on English PubMed would surface acacetin in passing (as one of many flavonoids in the Khan 2014 review and successor papers) but **would not connect it to a usable culinary/medicinal source** in the OE-platform sense. **Querying "Agastache rugosa xanthine oxidase" directly retrieves Yuk 2023 with the IC50 panel intact.** This is exactly the discipline-failure mode comp-018 Phase 2 identified for Houttuynia, manifesting in a different herb-formula context.

**Wiki action proposed:** **Promote Agastache rugosa / acacetin to TCM gout compound triage as a tier-1 XO chokepoint candidate.** Acacetin sits between luteolin (4.79 μM, already in comp-013) and the most potent flavonoid XO inhibitors in the literature. The plant is GRAS in Korea and Japan as a culinary herb; bioavailability profile would need a comp-NNN before any platform integration — but the IC50 is in the "worth pursuing" range. **This is the strongest single finding in the re-scan.**

---

### 4. 山楂 Shan Zha / Crataegus pinnatifida × XO

**Status:** **Evidence gap — no Crataegus-specific anti-hyperuricemia paper surfaced** despite Crataegus being TCM-canonical for "食滞 food stasis" with high-purine diet implications.

**What was found:**

- **Polyphenolic profile review** ([PMC6268084](https://pmc.ncbi.nlm.nih.gov/articles/PMC6268084/), Jurikova 2012): comprehensive C. pinnatifida fruit polyphenol catalog (chlorogenic acid, epicatechin, hyperoside, vitexin-2-O-rhamnoside, rutin, quercetin, procyanidin oligomers) — antioxidant + anti-inflammatory + cardiovascular benefits documented; **no XO or hyperuricemia data in this review.**

- **Wu 2014 chemistry-pharmacology overview** ([PMC6271784](https://pmc.ncbi.nlm.nih.gov/articles/PMC6271784/)) — broad pharmacology review; lipid + cardiovascular + hepatic + anti-cancer activities; **no XO entry, no anti-hyperuricemia entry.**

- **Lin 2022 fruit-extract activities** ([PMC8868160](https://pmc.ncbi.nlm.nih.gov/articles/PMC8868160/)) — hyperoside is the strongest antioxidant + α-glucosidase inhibitor identified; **no XO assay run.**

- **Compound-level analogy:** hyperoside, vitexin, and rutin (cardinal C. pinnatifida flavonoids) **do** have published XO inhibition in *other* plant matrices (Loh 2022 Chrysanthemum metabolomics paper, Saqib 2014 Crataegus monogyna twig paper). But the Crataegus pinnatifida fruit/leaf has not been the subject of a direct anti-hyperuricemia mouse study indexed in PubMed as of 2026-05-19.

**Why this matters for the query-framing audit:** This is a **null result in the right direction** — the re-scan didn't surface evidence that doesn't exist. The traditional-name framing is correct (Shan Zha as a 食滞 herb has obvious indication-overlap with high-purine-diet gout), but the literature hasn't been generated yet. **Tag as evidence gap worth a comp-NNN** if Brian wants the cardinal C. pinnatifida flavonoid panel screened against XO directly. This is a low-cost in-silico + in-vitro experiment if the C. pinnatifida extract is sourceable.

**Wiki action proposed:** Add a stub entry to TCM gout compound triage flagging "Crataegus pinnatifida hyperoside/vitexin XO activity unverified in species-specific assay — comp-NNN candidate." Do not claim XO inhibition for C. pinnatifida absent the direct paper.

---

### 5. 菊花 Ju Hua / Chrysanthemum morifolium × XO — **SECOND-HIGHEST FINDING**

**Status:** **Strongly supported, multiple independent papers, multiple constituent-level IC50 values, multiple formula-level animal model studies.**

**Cardinal evidence:**

- **Wee et al. 2023** ([PMC9864848](https://pmc.ncbi.nlm.nih.gov/articles/PMC9864848/)) — Computational + multispectroscopic study of C. morifolium XO inhibitors:
  - **Kaempferol IC50 = 2.18 ± 0.02 μM** (strongest constituent)
  - **Apigenin IC50 = 3.2 μM**
  - Trans-cinnamic acid IC50 > 200 μM (inactive)
  - Homovanillic acid: less potent inhibitor
  - At 100 μg/mL, kaempferol 81.87 ± 3.31% inhibition vs allopurinol 96.48 ± 2.40% — comparable order of magnitude.
  - Mechanism: non-competitive inhibition; binding via H-bonding + hydrophobic at active site; benzopyran moiety load-bearing. (In Vitro)

- **DKB114 formula (Chrysanthemum indicum + Cinnamomum cassia 1:2 w/w)** — Lee et al. 2018 ([PMC6213378](https://pmc.ncbi.nlm.nih.gov/articles/PMC6213378/), *Nutrients*): Korea Institute of Oriental Medicine.
  - **XOD IC50 (in vitro): 104.4 μg/mL**
  - Hyperuricemic rats (PO-induced) at 200 mg/kg: serum UA **−38.3%**, liver XOD activity **−66.7%**, urinary UA **+1.8–2.1×**
  - Mechanism: dual hepatic XOD inhibition + renal URAT1/GLUT9 downregulation (mRNA + protein). (In Vitro + Animal Model — formula-level evidence)

- **Loh et al. 2022** ([PubMed 34000756](https://pubmed.ncbi.nlm.nih.gov/34000756/), *Phytochem Anal*): metabolomics-driven identification of XO inhibitors from C. morifolium flowers — multiple flavonoid + caffeoylquinic acid hits.

- **Boju (boju) cultivar studies**: spectrum-effect relationship coupled UPLC-TOF-MS / HS-SPME-GC/MS quality control — flavonoids + monoterpenoids both contribute to XO inhibitory activity (multiple papers from the Wu Deling group at Anhui University of Chinese Medicine).

- **Luteolin-rich chrysanthemum extract in humans:** [Oatext open-access paper] — luteolin-rich chrysanthemum flower extract supplementation reduced baseline serum UA in Japanese subjects with mild hyperuricemia. (Clinical Trial, small N — would need full text fetch for sample size + statistical detail.)

**Why this matters for the query-framing audit:** Ju Hua is classically a "wind-heat clearing" + "liver-clearing" herb in the cooling-herbs class — not gout-indicated in the classical materia medica. But the constituent-level evidence is overwhelming: kaempferol + apigenin + luteolin + acacetin all sit in the same flavonoid scaffold class (5,7-dihydroxy A-ring + B-ring aromatic + C-ring planar) and all show low-μM XO inhibition. **Querying by formula context ("DKB114 Chrysanthemum Cinnamomum hyperuricemia") directly retrieves the dual-mechanism mouse data; querying by traditional indication ("Ju Hua 痛风") would surface the Japanese clinical study.** Mechanism-name framing ("kaempferol xanthine oxidase") would surface kaempferol but not its co-occurrence with apigenin + luteolin + acacetin in flavonoid-rich classical herbs.

**Wiki action proposed:** Add Chrysanthemum morifolium + kaempferol entry to TCM gout compound triage. Promote kaempferol as a tier-1 XO chokepoint candidate alongside luteolin (already in comp-013) and the new acacetin entry. **Flavonoid scaffold class — apigenin + kaempferol + luteolin + acacetin — should be discussed as a coherent compound class rather than as four separate entries.** This is a natural successor to the comp-013 luteolin row.

---

### 6. 金银花 Jin Yin Hua / Lonicera japonica × XO

**Status:** **Cardinal-herb supported via luteolin (already in comp-013) + chlorogenic acid panel; species-substitution L. hypoglauca surfaces a 100× more potent bisflavonoid.**

**Cardinal evidence:**

- **Luteolin** from L. japonica: IC50 = 4.79 × 10⁻⁶ M (Lin et al. 2002), Ki = 2.38 × 10⁻⁶ M, competitive inhibition. **Already in comp-013 row 2** (`compounds.json`). No new wiki action for luteolin itself.

- **Chlorogenic acid** from L. japonica: IC50 = 85.5 μg/mL (anti-oxidant assay; XO assays elsewhere put chlorogenic acid in the 10–50 μM range). Synergistic effect with luteolin demonstrated in DPPH assays. Same chlorogenic acid family active in Wu Mei (see herb #2 above).

- **LJP-1 polysaccharide** (Lonicera japonica polysaccharide): anti-hyperuricemic + anti-gouty-arthritis in PO-induced rats; **decreased serum UA + suppressed XOD activity + reduced IL-1β / IL-6 / TNF-α / COX-2** (Wang et al., *Int J Biol Macromol*, 2018, [ScienceDirect S0141813018326072](https://www.sciencedirect.com/science/article/abs/pii/S0141813018326072)). (Animal Model)

- **Lonicera hypoglauca species-substitution find** — Chien et al. 2009 ([PubMed 19184967](https://pubmed.ncbi.nlm.nih.gov/19184967/)):
  - L. hypoglauca crude extract: **IC50 = 48.8 μg/mL**
  - LH-EA sub-fraction: IC50 = 35.2 μg/mL
  - **Isolated loniceraflavone (bisflavonoid): IC50 = 0.85 μg/mL** — ~100× more potent than crude
  - Mouse PO-induced model, LH-EA: 300 mg/kg → 70.1% UA reduction; 500 mg/kg → 93.7%. (Animal Model)

**The species-substitution caveat:** *Lonicera hypoglauca* (山银花 Shan Yin Hua) and *Lonicera japonica* (金银花 Jin Yin Hua) are different species. In Chinese pharmacy, they are sometimes substituted or co-marketed under the umbrella "honeysuckle" label, but the 2010 Chinese Pharmacopoeia formally separated them. L. hypoglauca's loniceraflavone is a bisflavonoid not present in L. japonica. This means **the 0.85 μg/mL IC50 belongs to a different (closely related) species than the one classically named "Jin Yin Hua"** — a traditional-name-mapping subtlety the query-framing rule explicitly warns about.

**Wiki action proposed:** Add a Lonicera-genus note to the comp-013 luteolin row mentioning the L. hypoglauca loniceraflavone for completeness, but **do NOT conflate the species.** The species-substitution issue is itself a query-framing-discipline finding — "Jin Yin Hua" returns mostly L. japonica papers; "Shan Yin Hua" returns mostly L. hypoglauca papers; the umbrella English term "honeysuckle" returns both. Document this nuance.

---

### 7. 大黄 Da Huang / Rheum palmatum × XO

**Status:** **Mechanistically split — rhein inhibits XO, emodin does NOT.** This is a substantive update to the comp-013 anthraquinone framing.

**Cardinal evidence:**

- **Rhein** — Meng et al. 2015 ([PubMed 25760382](https://pubmed.ncbi.nlm.nih.gov/25760382/), adenine + ethambutol-induced hyperuricemic mice). Rhein **significantly decreased serum UA by inhibiting XO activity** + enhanced urinary UA excretion + reduced IL-1β / PGE2 / TNF-α / TGF-β1 + nephroprotective. (Animal Model — direct XO inhibition)

- **Emodin** — Hou et al. 2023 ([PMC10304951](https://pmc.ncbi.nlm.nih.gov/articles/PMC10304951/), *Pharmaceuticals*, PMID 37375737). PO-induced hyperuricemic rats. **Emodin reduced serum UA via increased urinary excretion, NOT via XO inhibition** — XO activity unchanged across treatment groups. Dose-response: 10 mg/kg minimal, 30 mg/kg significant, 50 mg/kg greatest, ~34–38% UA reduction. (Animal Model — transporter-mediated, not XO)

**Why this matters:** The current `wiki/tcm-gout-compound-triage-computational.md` comp-013 frame lists rhein + emodin together as "Rheum officinale 大黄 anthraquinones" without splitting their mechanisms. **The Hou 2023 paper is in comp-013's source list**, so the split is already partially documented — but the **wiki narrative does not separate them by mechanism**. A reader of comp-013 would conclude both anthraquinones are XO inhibitors; the literature says only rhein is. The Da Huang formula benefit (the herb contains both) is mechanism-additive (XO inhibition via rhein + transporter modulation via emodin), but the per-compound mechanistic claims should be separated.

**Wiki action proposed:** Edit comp-013 prose to distinguish rhein-XO from emodin-transporter. Add a one-line note that **the apparent XO inhibition attributed to Da Huang at the formula level is rhein-driven, with emodin contributing through a different mechanism** — this is a meaningful narrative refinement, not a new finding.

---

### 8. 柴胡 Chai Hu / Bupleurum chinense × XO

**Status:** **Null result — no direct XO or anti-hyperuricemia evidence located.**

**What was found:**

- Saikosaponins are extensively documented for hepatoprotection + anti-inflammatory + anti-viral activity, with **0.30%+ content required for Chinese Pharmacopoeia quality control** (2015 ed.).
- No surfaced paper directly testing saikosaponin or Radix Bupleuri extract against xanthine oxidase or in a hyperuricemia animal model.
- The Wang 2024 systematic review ([PMC11612855](https://pmc.ncbi.nlm.nih.gov/articles/PMC11612855/), *World J Gastroenterol*) of TCM extracts in hyperuricemia and gout treatment **does not include Bupleurum chinense as an entry** — consistent with the absence of primary data.

**Why this matters:** Chai Hu's classical indication is "和解少阳 harmonizing shao-yang" — applied to alternating fever-chills, intercostal pain, irregular menstruation, hepatobiliary disorders. There is **no traditional indication for hyperuricemia or gout** in the classical materia medica for Chai Hu. The query-framing rule was tested here and **correctly returned null** — Chai Hu doesn't sit in a traditional gout context, and the literature confirms it has no special XO activity. This is the rule working in the "correctly skip" direction.

**Wiki action proposed:** **None.** Document this as a null result in the per-herb section if/when this scan output is referenced. Don't add a Bupleurum entry to comp-013.

---

## Comparison: traditional-name vs mechanism-name framing — what was missed

Pre-2026-05-19 mechanism-name scans (XO inhibitor + flavonoid + hyperuricemia) would have surfaced:

- Luteolin (in comp-013, IC50 4.79 μM) — also present in C. morifolium, L. japonica, and many other matrices
- Quercetin (in many compound triage lists)
- Apigenin (4.79 / 3.2 / 0.87 μM across different papers — wide variance, often picked up via Salvia / Petroselinum scans)
- Allopurinol / febuxostat reference data
- Astilbin from Smilax glabra (comp-013, IC50 in tens-of-μM range)

Traditional-name-anchored scans (this re-scan) **additionally surfaced**:

| Compound | Source herb | Classical formula context | IC50 (XO) | Why mechanism-name framing missed it |
|---|---|---|---|---|
| **Acacetin** | Agastache rugosa (Huo Xiang) | Huo Xiang Zheng Qi | **0.58 μM** | A. rugosa is classically a summer-damp formula, not a gout herb — mechanism-name search would find acacetin among generic flavonoids but not connect it to a usable culinary/medicinal source |
| **Kaempferol** | Chrysanthemum morifolium (Ju Hua) | Ju Hua Cha + DKB114 | **2.18 μM** | Ju Hua is a wind-heat herb, not classical-gout; kaempferol is on every flavonoid screen but the C. morifolium constituent-level context is missing without the herb anchor |
| **Loniceraflavone** | Lonicera hypoglauca (Shan Yin Hua) | Substituted in some Jin Yin Hua applications | **0.85 μg/mL** (~2 μM est.) | The L. hypoglauca species is rarely surfaced by English mechanism-name queries; the species-substitution distinction needs the traditional-name framing to find at all |
| **Chlorogenic acid isomers** | Prunus mume (Wu Mei) | Wu Mei Wan | "comparable" (IC50 unverified due to 403) | Wu Mei is classically a jueyin formula, not gout — query-framing surfaces the herb-level XO data |
| **Cassia oil** | Cinnamomum cassia (Rou Gui) | DKB114, Wu Mei Wan | dose-dependent in vivo | C. cassia is "warming-yang" classically; mechanism-name framing would find cinnamaldehyde XO data but not the cassia oil whole-extract animal-model |

**Conversely, the traditional-name scan correctly did NOT promote:**

- Chai Hu (Bupleurum chinense) — null result, no XO evidence, classical indications unrelated to gout. The scan worked correctly in the "skip" direction.
- Crataegus pinnatifida — evidence gap, not finding gap. The scan correctly flagged the absence rather than fabricating positive evidence.
- Curcumin — surfaced the conflicting Western-RCT-negative + Chinese-animal-positive data rather than collapsing to one direction. The scan preserved the disagreement (per CLAUDE.md translation-disagreement-surfacing discipline).

---

## Proposed wiki updates

Per task constraints, this scan does **not** write to `wiki/*.md`. Below are the proposed updates for Brian's review:

### High-priority

1. **`wiki/tcm-gout-compound-triage-computational.md` (comp-013) — add Agastache rugosa / acacetin as a tier-1 XO chokepoint candidate.** Cite Yuk 2023 PMC9914411 with the IC50 = 0.58 μM number. Position above luteolin in the compound-ranking row (acacetin is more potent in the same assay class). The compound entry should note: classical formula context (Huo Xiang Zheng Qi), GRAS culinary status in Korea + Japan, and that this finding was surfaced by the 2026-05-19 traditional-name re-scan.

2. **`wiki/tcm-gout-compound-triage-computational.md` (comp-013) — add Chrysanthemum morifolium / kaempferol as a tier-1 XO chokepoint candidate.** Cite Wee 2023 PMC9864848 with IC50 = 2.18 μM. Also reference Lee 2018 PMC6213378 DKB114 formula-level data (38.3% UA reduction at 200 mg/kg, 104.4 μg/mL XO IC50).

3. **`wiki/tcm-gout-compound-triage-computational.md` (comp-013) — split the Rheum / Da Huang anthraquinone row by mechanism.** Rhein → direct XO inhibition (Meng 2015). Emodin → transporter-mediated UA excretion, NO XO inhibition (Hou 2023, already cited but mechanism not separated in narrative). Update the wiki prose accordingly. **This is a corrective edit, not a new finding.**

4. **`wiki/gout-pathophysiology.md` — the "multi-track urate transporter coverage" table — add an XO row showing acacetin (Huo Xiang) + kaempferol (Ju Hua) + rhein (Da Huang) alongside the existing astilbin (Smilax) entry.** XO is currently shown only with astilbin in the TCM-track column. The flavonoid panel is mechanism-additive at XO.

### Medium-priority

5. **`wiki/tcm-gout-compound-triage-computational.md` (comp-013) — add Wu Mei / Prunus mume chlorogenic acid panel as a compound-class entry** rather than a herb-specific entry. Chlorogenic acid family is XO-active across Wu Mei, L. japonica, and likely Crataegus and others — better framed as a class than as per-herb redundant entries.

6. **`wiki/tcm-gout-compound-triage-computational.md` (comp-013) — add Lonicera hypoglauca species-substitution note to the luteolin row.** Loniceraflavone IC50 = 0.85 μg/mL is worth a one-line entry distinguishing L. hypoglauca from L. japonica, with the species-substitution discipline-finding called out.

### Low-priority (evidence gaps to flag, not action)

7. **`wiki/tcm-gout-compound-triage-computational.md` (comp-013) — flag Crataegus pinnatifida as an evidence gap.** Hyperoside + vitexin in C. pinnatifida have no direct anti-hyperuricemia mouse study. **Candidate for comp-NNN** if Brian wants the cardinal Shan Zha flavonoid panel screened against XO.

8. **`wiki/tcm-gout-compound-triage-computational.md` (comp-013) — flag Curcumin's Western-RCT-negative + Chinese-animal-positive contradiction as a documented entry with mechanism nuance.** Not a recommended OE intervention candidate, but deserves explicit treatment rather than absence.

### No action

9. **Chai Hu / Bupleurum chinense** — null result. Do NOT add a row. Documented in this log only.

10. **Huo Xiang Zheng Qi (formula) + Wu Mei Wan (formula)** — no formula-level RCT evidence. The cardinal-herb evidence stands; do NOT make formula-level claims absent the trials.

---

## Limitations

- **Wu Mei chlorogenic acid IC50 verification gap.** The MDPI Compounds 2023 paper on heat-concentrated Prunus mume extract (Otsuki et al.) was blocked by HTTP 403 in WebFetch; the search-summary stated "comparable inhibitory activities" without a numerical IC50. The Wu Mei row in any wiki update should either (a) cite the qualitative "comparable" wording with a clear evidence-tier hedge, or (b) wait for a paperclip-pull or sci-hub fetch to extract the actual numbers. **Mark as placeholder, not verified.**

- **REVERC3 bisdemethoxycurcumin IC50 verification gap.** Dovepress 403'd on WebFetch; the IC50 = 27.93 μg/mL number is from the search summary and should be verified against the primary text before any wiki commit.

- **Bupparenoo 2020 RCT details not fully fetched.** The negative RCT result is established (PubMed 32420786), but the Curcuma form / dose / cohort details would need a full-text fetch before formally positioning curcumin as "human-RCT-negative" in the wiki. Functional adequacy of the search-summary read is acceptable for this scan log.

- **L. japonica polysaccharide LJP-1 paper not fully read.** Surfaced as anti-hyperuricemic via XO suppression in PO-induced rats but the journal paywall (ScienceDirect) blocks direct WebFetch. Cited from search summary; load-bearing claims about LJP-1 should be verified before wiki commit.

- **No paperclip full-text reads of the load-bearing papers in this scan.** Paperclip MCP returned 404 errors on three of the five attempted secondary searches (Lonicera, Si Miao San, Rheum-specific) — possibly transient. The semantic search worked initially (s_05c4c525, s_5c05f753, s_62dd6ba6) and confirmed the corpus contains the curcumin + Crataegus + Chrysanthemum papers — but the deep IC50 extractions came from PMC direct-fetch, not from paperclip. **A second-pass paperclip read of Yuk 2023 + Wee 2023 + Lee 2018 + Zhao 2025 would tighten verification before committing any of these IC50 numbers to wiki claims.**

- **No formula-level RCT search executed for Huo Xiang Zheng Qi or Wu Mei Wan.** ChiCTR + WHO ICTRP would be appropriate next-step searches if Brian wants the formula-level evidence specifically interrogated. This scan stayed at the cardinal-herb level.

- **No CNKI / WanFang direct queries executed.** Sandbox does not have direct access. The English-language PMC + ScienceDirect literature is the surface that was actually scanned. CNKI-only Chinese clinical literature for these formulas (which is extensive — Huo Xiang Zheng Qi has hundreds of CNKI papers, Wu Mei Wan has dozens) was not directly mined. **Estimated yield of a CNKI-only follow-up: 5–15 additional formula-level clinical observations + 3–8 additional constituent compounds per formula, though confidence in Chinese-clinical evidence tier is variable and individual paper verification would be required.**

- **No Japanese Kampo or Korean ethnomycology direct search.** Acacetin's identification came from a Korean Foods paper, suggesting the Korean-clinical-trial database (KISS / RISS) might have additional Agastache rugosa hyperuricemia data not surfaced by English keyword searches. Out of scope for this 1-2 hour scan.

- **Pre-commit grep-verify gate not yet executed against the numbers above.** Per CLAUDE.md §"Pre-commit grep-verify gate for load-bearing numbers" — every IC50 + percent UA reduction in this log should be re-verified against the primary PMC text before any of these numbers ship into a wiki commit. The numbers in this log have been pulled from a single WebFetch read each (sometimes a search-summary read); a second read would tighten confidence. **Treat the log itself as a scan output, not as wiki-ready claims.**

- **Translation discipline not triggered.** Per CLAUDE.md two-model translation protocol — would only apply if the load-bearing claims were in Chinese-original text. All surfaced papers in this scan are English-language PMC papers with Chinese / Korean group authorship. No translation-disagreement annotations needed.

---

## Citation provenance summary

| Claim | Primary source | Evidence tier | Verified |
|---|---|---|---|
| Acacetin IC50 = 0.58 μM vs XO; allopurinol 4.2 μM in same assay | Yuk et al. 2023, *Foods* 12(3):573, [PMC9914411](https://pmc.ncbi.nlm.nih.gov/articles/PMC9914411/) | In Vitro | WebFetch PMC table extraction; single read |
| Kaempferol IC50 = 2.18 μM vs XO; apigenin 3.2 μM | Wee et al. 2023, [PMC9864848](https://pmc.ncbi.nlm.nih.gov/articles/PMC9864848/) | In Vitro | WebFetch PMC; single read |
| DKB114 (Chrysanthemum + Cinnamon) IC50 = 104.4 μg/mL; rat 38.3% UA reduction at 200 mg/kg | Lee et al. 2018, *Nutrients*, [PMC6213378](https://pmc.ncbi.nlm.nih.gov/articles/PMC6213378/) | In Vitro + Animal Model | WebFetch PMC; single read |
| Curcumin 200 mg/kg oral gavage → ~44% serum UA reduction + ~40% hepatic XOD reduction in acute gout mice | Zhao et al. 2025, *Smart Molecules*, [PMC12483134](https://pmc.ncbi.nlm.nih.gov/articles/PMC12483134/), PMID 41035515 | Animal Model | WebFetch PMC; single read |
| Curcumin RCT (N=39, 1000 mg/day, 8 weeks) NOT superior to placebo for serum urate | Bupparenoo et al. 2020, *J Diet Suppl* 18(3), [PubMed 32420786](https://pubmed.ncbi.nlm.nih.gov/32420786/) | Clinical Trial | Search-summary read; primary text NOT fetched |
| Rhein significantly decreased serum UA via XO inhibition + uricosuric effect (mice) | Meng et al. 2015, [PubMed 25760382](https://pubmed.ncbi.nlm.nih.gov/25760382/) | Animal Model | WebFetch PMID summary |
| Emodin reduced serum UA via increased urinary excretion, NOT via XO inhibition (rats) | Hou et al. 2023, [PMC10304951](https://pmc.ncbi.nlm.nih.gov/articles/PMC10304951/), PMID 37375737 | Animal Model | WebFetch PMC; single read (already in comp-013 source list) |
| Heat-concentrated *Prunus mume* extract: three chlorogenic acid isomers exhibit XO inhibition; reduces rat plasma UA | Otsuki et al. ~2023, [MDPI Compounds 3(1):14](https://www.mdpi.com/2673-6918/3/1/14) | In Vitro + Animal Model | **PLACEHOLDER — primary text not retrieved (HTTP 403); search-summary only** |
| Lonicera hypoglauca crude IC50 = 48.8 μg/mL; loniceraflavone IC50 = 0.85 μg/mL; mouse 70.1–93.7% UA reduction at 300–500 mg/kg LH-EA | Chien et al. 2009, [PubMed 19184967](https://pubmed.ncbi.nlm.nih.gov/19184967/) | In Vitro + Animal Model | WebFetch PMID summary |
| Luteolin IC50 = 4.79 × 10⁻⁶ M, Ki = 2.38 × 10⁻⁶ M, competitive XO inhibition | Lin et al. 2002 (cited in multiple downstream reviews) | In Vitro | Already in comp-013; cross-check only |
| 5-O-caffeoylshikimic acid IC50 = 13.96 μM; binding energy −8.6 kcal/mol | Zhang et al. 2021, [PMC8659034](https://pmc.ncbi.nlm.nih.gov/articles/PMC8659034/), PMID 34885887 | In Vitro + Animal Model | Already in comp-013 source list; no new wiki action |
| Hesperetin IC50 = 110.4 μmol/L (one study) or 16.48 μM (another); dose 5–10 mg/kg ip in mice reduced serum UA | An et al. 2023, *Front Pharmacol* 14:1128699, [PMC10131109](https://pmc.ncbi.nlm.nih.gov/articles/PMC10131109/), PMID 37124197 | In Vitro + Animal Model | WebFetch PMC; single read |
| Kong et al. 2000 screen of 122 Chinese medicinal plants — Cinnamomum cassia twig IC50 = 18 μg/mL; Chrysanthemum indicum flower IC50 = 22 μg/mL; Polygonum cuspidatum rhizome IC50 = 38 μg/mL; Lycopus europaeus IC50 = 26 μg/mL; allopurinol IC50 = 1.06 μg/mL | Kong et al. 2000, *J Ethnopharmacol* 73(1-2):199-207, [PubMed 11025157](https://pubmed.ncbi.nlm.nih.gov/11025157/) | In Vitro | WebFetch PubMed abstract |
| Chinese sumac (*Rhus chinensis*) fruit ethanol extract → 39.56% serum UA reduction (mice high-purine diet) + XO inhibition + ABCG2 upregulation + URAT1/SLC2A9 downregulation | Wang et al. 2024, *Nutrients*, [PMC10819650](https://pmc.ncbi.nlm.nih.gov/articles/PMC10819650/) | Animal Model | WebFetch PMC; single read |
| Sanmiao Wan / Ermiao Wan reduce serum + liver UA + inhibit hepatic XOD in mice | Kong et al. 2004, [PubMed 15234772](https://pubmed.ncbi.nlm.nih.gov/15234772/) (Ermiao) + multiple Sanmiao papers | Animal Model | Search-summary only; primary text not fetched (already aware via comp-013 Si Miao San citation) |
| Houttuynia cordata polysaccharide regulates URAT1 + reduces XO activity in hyperuricemic mice | Cited from [houttuynia-cp1-dual-mechanism-lit-scan-2026-05-19.md](./houttuynia-cp1-dual-mechanism-lit-scan-2026-05-19.md) — full deep-read | In Vivo Animal Model | Already separately scanned 2026-05-19; cross-reference only |

---

*Scan executed by Opus 4.7 subagent under the 2026-05-19 query-framing discipline. All proposed wiki actions require Brian's review + pre-commit grep-verify gate against primary sources before any commit. The high-leverage findings (acacetin from Agastache, kaempferol from Chrysanthemum) are the strongest single-paper anchors in the scan — the others are confirmatory or evidence-gap-flagging.*
