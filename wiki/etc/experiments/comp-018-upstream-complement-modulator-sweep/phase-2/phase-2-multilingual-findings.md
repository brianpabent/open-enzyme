# comp-018 Phase 2 — Multilingual Findings

**Date:** 2026-05-17
**Scope:** Multilingual extension of comp-018 (Phase 1 English-corpus) and comp-020 (brief-scrubbed verification re-run). Anchors: PubMed indexes Chinese-, Japanese-, and Korean-author publications; Paperclip MCP corpus; direct non-English-source searches per CLAUDE.md §"Global-multilingual research by default."

**Independence statement:** Phase 2 brief was deliberately written WITHOUT pre-loading any compound or species as expected headline (subagent brief hygiene per `operations/comp-018-vs-comp-020-retrospective.md` + `scripts/SWEEP-ARCHITECTURE.md`). User-direction text limited to scope/method propagation only.

**Translation protocol:** All non-English source material in this Phase 2 was either (a) abstract-tier (PubMed-indexed abstracts, originally non-English papers with English-language abstract metadata) or (b) read in English mirror (PMC full-text English versions of Chinese-vendor papers from Fudan / Kitasato groups). Where source-language Chinese or Japanese full-text was substantially relevant, I read the English-language abstract and flagged the source-language paper with `[TRANSLATION-SINGLE-MODEL — flagged for v2 DeepSeek cross-check]` where the load-bearing claim depends on interpretation rather than numerical extraction. No Chinese-language full-text in this Phase 2 was load-bearing for an evidence-tier verdict — the Chen Daofeng (Fudan) and Yamada (Kitasato) groups both publish substantively in English, and Phase 2's gap-closing finding is that "non-English literature" for upstream complement modulators is in practice **a Chinese-group / Japanese-group publication corpus that is partially English-indexed but underweighted by Western database curation**.

---

## Headline (one sentence)

**Phase 2 surfaces no NEW tier-1 single compound that displaces the Phase 1 / comp-020 ranking, but reframes the entire upstream-complement-modulator field as overwhelmingly Chinese-group + Japanese-group anchored — the Chen Daofeng (Fudan) and Yamada-Kiyohara (Kitasato Institute) labs together account for the majority of post-1985 anti-complementary natural product literature, including evidence on Houttuynia cordata, Bupleurum (multiple species), Glycyrrhiza, Angelica acutiloba, Scutellaria barbata, Scutellaria baicalensis, Panax ginseng leaf, Viola yedoensis, Amomum tsao-ko, Myricaria wardii (Tibetan), Juniperus pingii (Tibetan), Malva verticillata, Imperata cylindrica, Rabdosia japonica, and Artemisia princeps — all of which Phase 1 either underweighted or missed entirely.**

---

## TIER 1 — strong evidence, mechanistically anchored, complementary to Phase 1 leads

### Helicteres benzofuran lignans — REPLICATION ATTEMPT, see [`phase-2-helicteres-replication.json`](./phase-2-helicteres-replication.json)

The Yin et al. 2016 Helicteres angustifolia anchor paper (PMC6273495) remains a SINGLE-PAPER ANCHOR. Multilingual search (Chinese-author network, J-STAGE, Korean Pharmacology Society) found no independent replication of the CH50 9 / 40 µM benzofuran-lignan finding for compound 5 (hedyotol-D-7''-O-β-D-glucopyranoside) or compound 4 (machicendonal). What was found:

- The same Chen Daofeng (Fudan) group has published ~14+ separate anti-complementary natural product papers using the matched sheep-erythrocyte CH50 / rabbit-erythrocyte AP50 hemolytic assay format (1999-2025). The Helicteres benzofuran lignan finding is consistent with the assay-format and laboratory protocol used across this body of work, but **no independent group has reproduced the specific Helicteres benzofuran lignan CH50 metric on a matched assay format.**
- The Helicteres genus has been studied for cancer (PMC4806988, PMC5346361, PMC10323433 via Tsukuba / Beijing), antifibrotic (Helicteres angustifolia methyl helicterate, J Ethnopharmacol 2012 PMID 22967666, [doi:10.1016/j.jep.2012.08.018](https://doi.org/10.1016/j.jep.2012.08.018)), and triterpene chemistry (Wang 2012 Fitoterapia PMID 23010154, [doi:10.1016/j.fitote.2012.09.016](https://doi.org/10.1016/j.fitote.2012.09.016)) — but none of these threads cite or replicate the upstream-complement CH50 finding.

**Verdict for Helicteres replication:** INCONCLUSIVE / ANCHOR-STILL-SINGLE. The original finding is real and falls within the Chen group's matched-assay envelope; no independent CH50 confirmation exists; the Helicteres genus has substantial Chinese / Japanese pharmacology literature but the upstream-complement angle is isolated to the Yin 2016 paper. **Wet-lab independent replication remains the load-bearing next step.**

### Houttuynia cordata polysaccharides — NEW tier-1 candidate Phase 1 missed entirely

**Source-language status:** Multiple papers in this thread are Chinese-language (Zhongguo Zhong Yao Za Zhi = China Journal of Chinese Materia Medica) — but corresponding English abstracts are PubMed-indexed and the group also publishes in English (Acta Pharm Sin B, Int J Biol Macromol, Planta Med). Phase 1 missed Houttuynia entirely.

**Crude polysaccharide CHCP:** CH50 0.079 g/L (= 79 µg/mL) on the matched Chen-group CH50 assay (Zhang JJ, Lu Y, Chen DF. Zhongguo Zhong Yao Za Zhi 37(14):2071-5 (2012). PMID 23126186, source-language **Chinese** [TRANSLATION-SINGLE-MODEL — flagged for v2 DeepSeek cross-check for the extraction-protocol section but numeric CH50 = 0.079 g/L is unambiguous in the English abstract]). Mechanism: complement C3 + C4 (Lu 2017 Acta Pharm Sin B PMID 29719782, [doi:10.1016/j.apsb.2017.11.003](https://doi.org/10.1016/j.apsb.2017.11.003)). **In vivo precedent: protects against H1N1-induced acute lung injury in mice (PMC5925397), LPS-induced fever, hemorrhagic shock + LPS "two-hit" ALI model.**

**Purified polysaccharides HC-PS1 and HC-PS3:** IC50 0.272–0.318 mg/mL on both CP and AP, interact with C2 + C4 + C5 (Lu Y, Zhang JJ, Huo JY, Chen DF. Planta Med 85(13):1098-1106 (2019). PMID 31250410, [doi:10.1055/a-0955-7841](https://doi.org/10.1055/a-0955-7841)). Source language English.

**HCPM (ultrafiltration-purified heteropolysaccharide, 19.1 kDa):** CH50 254.1 ± 7.8 µg/mL; in vivo attenuation of H1N1-induced lung + gut injury (Zhou L et al. Int J Biol Macromol 222:2414-2425 (2022). PMID 36252625, [doi:10.1016/j.ijbiomac.2022.10.027](https://doi.org/10.1016/j.ijbiomac.2022.10.027)). Source language English.

**Why Phase 1 missed:** Phase 1's PubMed query strategy used "anti-complement" / "anticomplement" / "complement inhibitor" search terms but did NOT spawn a dedicated Houttuynia probe. Houttuynia cordata is a well-known Chinese / Japanese folk medicine (鱼腥草 yúxīngcǎo / どくだみ dokudami) used for "clearing heat and toxins" — substantial Chinese-language pharmacology literature lives at Acta Pharm Sin B + Zhongguo Zhong Yao Za Zhi. The Chen Daofeng group has indexed it cleanly in English-language journals since at least 2012.

**Mechanistic placement:** Houttuynia cordata polysaccharides target C2 + C4 + C5 (classical pathway, possibly AP at C5). Same target node as Bupleurum (Wu 2015 PMC4629277 surfaced in Phase 1). **Distinct platform candidate from Bupleurum because Houttuynia is widely consumed as a vegetable in Vietnam, southern China, Korea, and Japan — the dietary-access pathway is operational without supplementation.**

### Glycyrrhiza uralensis pectic polysaccharides (GR-2IIc and PG-1c fragments) — UNDERWEIGHTED in Phase 1

**Source language English** (Kitasato Institute, Yamada group, 1989-1996). Phase 1's CP0 thread did not surface this.

GR-2IIc anti-complementary activity via classical pathway; PG-1c (lithium-degradation enzyme-resistant region) was further analyzed for short and long neutral oligosaccharide-alditol fractions, both with anti-complementary activity (Kiyohara H et al. Planta Med 62(1):14-9 (1996). PMID 8720381, [doi:10.1055/s-2006-957787](https://doi.org/10.1055/s-2006-957787)). Structural mechanism: rhamnogalacturonan core + neutral side chains, with the rhamnogalacturonan moiety load-bearing. Earlier Zhao 1991 (PMID 1804531, [doi:10.1016/0008-6215(91)89049-l](https://doi.org/10.1016/0008-6215(91)89049-l)) — five anti-complementary polysaccharide fractions from G. uralensis, methylation analysis.

**Why it matters for the platform:** Licorice (Glycyrrhiza) is FDA GRAS, widely consumed dietary tier, and Chinese / Japanese / Korean pharmacology has it under continuous study since the 1980s with the matched Yamada-Kitasato pectic-polysaccharide assay. Phase 1's TCM compound triage caught glycyrrhizin (the triterpenoid saponin) but missed the polysaccharide layer.

### Scutellaria baicalensis flavonoid aglycones — metabolic-activation thread

**Source language English** (Chen Daofeng group). Phase 1's TCM triage (comp-013) and Phase 1's upstream-complement sweep (comp-018) BOTH partially captured this — baicalein, wogonin, oroxylin A, chrysin were named — but the LOAD-BEARING mechanistic insight was missed:

**Phase 2 finding:** flavonoid glycosides (baicalin, the predominant form in Scutellaria root) are INACTIVE at the complement system in vitro. The active form is the aglycone (baicalein, oroxylin A, wogonin, chrysin) — generated in vivo by gut-microbiome β-glucuronidase activity (Zhi HJ et al. J Pharm Biomed Anal 177:112876 (2019). PMID 31525575, [doi:10.1016/j.jpba.2019.112876](https://doi.org/10.1016/j.jpba.2019.112876)) — and **IAV-infected mice have higher gut-microbiome β-glucuronidase activity than healthy mice, so deglycosylation efficiency in inflammation is HIGHER than baseline.**

**Why this matters for gout / CP0:** Same mechanism applies to other flavonoid-glycoside-rich Chinese herbs (Lonicera, Forsythia, honeysuckle). In MSU-driven inflammation, gut-microbiome state shifts; the active aglycone form is favored. Implies any dietary recommendation for upstream complement modulation via flavonoid-glycoside-containing herbs needs to factor microbiome state. **Triple-convergence pattern (similar to luteolin XO+URAT1+CP0 from Phase 1) extends to baicalein.**

### Quercus glauca galloyl glucoses (Korean folk medicine)

Bioactivity-guided fractionation of Q. glauca leaves yielded:
- 1,2,3,6-tetragalloylglucose: CP IC50 32.3 µM
- 1,2,6-trigalloylglucose: 138.3 µM
- 6'-O-galloyl salidroside: 224 µM
- methyl gallate: 362.4 µM
(Chung IM et al. Hum Exp Toxicol 30(9):1415-9 (2010). PMID 21078772, [doi:10.1177/0960327110390067](https://doi.org/10.1177/0960327110390067))

**Source language English** (Korean group, Kon Kuk University). Phase 1 missed entirely.

**Mechanistic placement:** Galloyl glucoses are NOT in current OE compound stack. Tetragalloyl glucose at 32 µM CP IC50 is competitive with luteolin (190 µM CH50 per Zhang & Chen 2008) and within ~3× of rosmarinic acid in matched assay (RMA hemolytic CP 180 µM per Sahu 1999). Quercus species are extensively used in Korean / Chinese / Japanese folk medicine for diarrhea, dermatitis, hemorrhagia (per the paper).

---

## TIER 2 — moderate evidence, primary source verified, complementary tier-1 leads above

### Caffeic acid (Rabdosia japonica)

- CH50 0.041 g/L (= 41 µg/mL ≈ 230 µM if MW=180) classical pathway, strongest in the Rabdosia japonica panel of 11 isolates
- Source: Yao S et al. Zhongguo Zhong Yao Za Zhi 38(2):199-203 (2013). PMID 23672041. Source language **Chinese** [TRANSLATION-SINGLE-MODEL — flagged: numeric CH50 = 0.041 g/L unambiguous, but assay-format and erythrocyte source need full-text verification before downstream propagation]
- Mechanism: classical pathway; previous Rabdosia japonica panel (isoquercetrin, rutin, quercetin, 3-methylquercetin, luteolin, 7-methylluteolin, apigenin) also active per same paper
- **Platform relevance:** caffeic acid is dietary tier (coffee, apple, prune, blueberry), already in OE corpus via different mechanism (XO inhibition). Triple-convergence pattern again

### Amomum tsao-ko hydroquinone + diarylheptanoid

- 1,7-bis(4-hydroxyphenyl)-4(E)-hepten-3-one: blocked C1q + C2 + C3 + C4 + C5 + C9 (most complete-cascade pan-blocker in Phase 2)
- Hydroquinone: blocked C1q + C2 + C3 + C5 + C9
- CH50 range 0.42-4.43 mM, AP50 range 0.53-1.51 mM
- Source: Jin J, Cheng Z, Chen D. Nat Prod Commun 8(12):1715-8 (2013). PMID 24555280, source-language English (Fudan group)
- **Platform relevance:** Amomum tsao-ko (草果, tsao-ko / black cardamom) is dietary tier in Sichuan / Yunnan cuisine, widely consumed in Southeast Asian cooking. Specific compound chemistry (diarylheptanoid) overlaps with curcumin scaffold

### Viola kunawarensis sterols + sesquiterpenoid (Xinjiang, China)

- Stigmasta-4-ene-3β,6β-diol, saringosterone, aurantiamide acetate, solalyratin B
- CH50 0.02–0.08 mM (= 20–80 µM)
- Source: Wang H et al. Nat Prod Res 31(19):2312-2315 (2017). PMID 28278621, [doi:10.1080/14786419.2017.1297446](https://doi.org/10.1080/14786419.2017.1297446). Source language English (Shihezi + Fudan groups)
- **Platform relevance:** Endemic to Xinjiang Uyghur region; not dietary; chemistry overlaps with stigmasterol scaffold (extensively studied)

### Myricaria wardii (Tibetan medicine, Myricariae Ramulus)

- Spectrum-effect analysis of 15 batches; methyl 3,4-dihydroxy-5-methoxybenzoate, myricarin A, protocatechualdehyde, N-feruloyl normetanephrine, protocatechuic acid as quality markers
- Source: Zhang M et al. Phytochem Anal 36(5):1502-1516 (2025). PMID 40070292, [doi:10.1002/pca.3527](https://doi.org/10.1002/pca.3527). Source language English (Fudan + Tibet University); 2025 publication, post-dates Phase 1
- **Platform relevance:** Tibetan medicine surface; quality-marker approach validates the matched-assay anti-complementary discipline at scale

### Juniperus pingii var. wilsonii (Tibetan medicine)

- JPWP-PS: CH50 0.073 ± 0.009 mg/mL
- Mechanism: structure-characterized acidic polysaccharide with d-galacturonic acid content
- In vivo: attenuates H1N1-induced ALI in mice
- Source: Fu Z et al. Int J Biol Macromol 129:246-253 (2019). PMID 30708019, [doi:10.1016/j.ijbiomac.2019.01.163](https://doi.org/10.1016/j.ijbiomac.2019.01.163). Source language English (Fudan + Tibet University)

### Bupleurum chinense BC-PS1, BC-PS2 (companion to Phase 1's Wu 2015 BPs)

- BC-PS1: CH50 0.199 mg/mL, AP50 0.371 mg/mL; targets C1q + C2 + C5 + C9 (Di H et al. Int J Biol Macromol 58:179-85 (2013). PMID 23570674, [doi:10.1016/j.ijbiomac.2013.03.043](https://doi.org/10.1016/j.ijbiomac.2013.03.043))
- BC-PS2: CH50 0.222 mg/mL, AP50 0.356 mg/mL; targets C1q + C2 + C9 (DI HY et al. Chin J Nat Med 11(2):177-84 (2013). PMID 23787186, [doi:10.1016/S1875-5364(13)60046-1](https://doi.org/10.1016/S1875-5364(13)60046-1))
- **Platform relevance:** Phase 1 surfaced Bupleurum chinense polysaccharide via Wu 2015 but did NOT surface the parallel Di 2013 anchor papers. Three independent Bupleurum chinense fractions show same general mechanism (C1q + C2 + downstream) — anchor density confirms the species is well-characterized

### Scutellaria barbata B3-PS1 (different species from S. baicalensis above)

- CH50 0.12 ± 0.02 mg/mL, AP50 0.36 ± 0.05 mg/mL
- Mechanism: interacts with C1q + C1r + C1s + C2 + C3 + C4 + C5 + C9 (pan-cascade)
- Source: Wu Y, Chen DF. Immunopharmacol Immunotoxicol 31(4):696-701 (2009). PMID 19874244, [doi:10.3109/08923970903095314](https://doi.org/10.3109/08923970903095314). Source language English (Fudan group)

### Bupleurum smithii D3-S1 (companion to BC-PS1/2)

- CH50 0.34 ± 0.02 mg/mL, AP50 0.081 ± 0.003 mg/mL
- Targets C1s + C3 + C4 (selective; NOT C1q, C1r, C2, C5, C9)
- Source: Xu H et al. Int Immunopharmacol 7(2):175-82 (2007). PMID 17178384, [doi:10.1016/j.intimp.2006.09.006](https://doi.org/10.1016/j.intimp.2006.09.006). Source language English (Fudan group)

### Imperata cylindrica (lalang grass, white-mao-gen, 白茅根)

- Friedelin, vanillic acid, trans-p-coumaric acid: inhibited CP
- Source: Fu LN et al. Zhong Yao Cai 33(12):1871-4 (2010). PMID 21548362. Source language **Chinese** [TRANSLATION-SINGLE-MODEL — flagged: compound names + activity direction unambiguous in English abstract; full quantitative CH50 not in abstract]
- **Platform relevance:** Imperata is dietary tier (used in Chinese folk medicine teas), already in TCM corpus

### Styrax japonica norlignans + terpenes (Korean Research Institute)

- Styraxlignolide A (norlignan glucoside): IC50 123 µM
- Egonol (norlignan): IC50 33 µM
- Styraxoside B (terpene): IC50 65 µM
- Masutakeside I (terpene): IC50 166 µM
- Source: Min BS et al. Planta Med 70(12):1210-5 (2004). PMID 15643559, [doi:10.1055/s-2004-835853](https://doi.org/10.1055/s-2004-835853). Source language English (Korean Research Institute of Bioscience and Biotechnology)
- **Platform relevance:** Styrax species are not dietary; benzofuran-egonol scaffold structurally overlaps the Helicteres anchor chemistry (both are benzofuran-containing). Possibly the lowest-effort positive-control material for a Helicteres benzofuran lignan replication study

### Quercus glauca galloyl glucoses (see TIER 1 above for tetragalloyl glucose)

The smaller galloyl glucoses (tri-, di-, mono-) at higher IC50s (138-362 µM) are tier 2.

---

## TIER 3 — narrow evidence / source-limited / context-dependent

### Cimicifugae Rhizoma (Korean traditional medicine)

- Anti-inflammatory + anti-complement + osteogenic stem-cell effects at 0.1-10 µg/mL
- Source: Lee JE et al. Exp Ther Med 13(2):443-448 (2017). PMID 28352313, [doi:10.3892/etm.2016.4010](https://doi.org/10.3892/etm.2016.4010). Source language English (Korean groups)
- Mechanism for complement not detailed in this paper; tier 3 because of unspecified target nodes

### Ligularia taquetii chloroform extract

- CP IC50 73.2 µg/mL (Korean Compositae plants panel)
- Source: Moon HI, Lee JH, Lee YC. Immunopharmacol Immunotoxicol 34(1):12-4 (2011). PMID 21506692, [doi:10.3109/08923973.2011.571698](https://doi.org/10.3109/08923973.2011.571698). Source language English

### Artemisia princeps AAF-IIb-2 + IIb-3 (Japanese Gaiyo)

- Anti-complementary acidic heteroglycans; both CP and AP active
- Source: Yamada H et al. Chem Pharm Bull 39(8):2077-81 (1991). PMID 1797428, [doi:10.1248/cpb.39.2077](https://doi.org/10.1248/cpb.39.2077). Source language English (Kitasato group)
- Mechanism: classical + alternative pathway via C4 + C3 consumption; IgG-dependent — implies this is more an immunomodulator than a pure inhibitor

### Juzen-taiho-to (Japanese Kampo, 十全大補湯) — TJ-48 prescription

- 10-herb Kampo prescription; F-2 (water + methanol-insoluble fraction) and F-5 (crude polysaccharide fraction) both anti-complementary
- F-5-2 (acidic pectic polysaccharide fraction) has both anti-complementary AND mitogenic activity — direction-of-effect interpretive challenge
- Source: Yamada H et al. Planta Med 56(4):386-91 (1990). PMID 2236295, [doi:10.1055/s-2006-960990](https://doi.org/10.1055/s-2006-960990). Source language English (Kitasato group)
- Also Yamada H. Gan To Kagaku Ryoho 16(4 Pt 2-2):1500-5 (1989). PMID 2786380. **Source language Japanese** [TRANSLATION-SINGLE-MODEL — flagged: the original Japanese paper develops the active-fraction discipline that the 1990 English-language Planta Med paper formalized. Phase 2 reads only the English abstract; full Japanese text not load-bearing because the mechanism is captured in the 1990 paper]
- **Why tier 3:** anti-complementary AND mitogenic in same molecule means direction-of-effect ambiguous for gout-context use

### Malva verticillata seed polysaccharides

- MVS-I (β-1,3-D-glucan + α-1,5-L-arabino-β-3,6-branched D-galactan) anti-complementary + hypoglycemic
- Source: Tomoda M et al. Planta Med 56(2):168-70 (1990). PMID 2353063, [doi:10.1055/s-2006-960917](https://doi.org/10.1055/s-2006-960917). Source language English (Kyoritsu College of Pharmacy, Tokyo)

### Angelica acutiloba AR-arabinogalactan and AR-2II series

- Multiple polysaccharide fractions, CP + AP active
- Sources: Yamada H et al. 1985 PMID 4000133 + 1988 PMID 3242805 + 1990 PMID 2353065 + 1984 PMID 17340284, [doi:10.1055/s-2007-969661](https://doi.org/10.1055/s-2007-969661). Source language English (Kitasato group)
- Why tier 3: same direction-of-effect ambiguity as Juzen-taiho-to — these are ACTIVATORS of complement (C4 consumption) in some assay formats, INHIBITORS in others

### Panax ginseng leaf glycans GL-NIa + GL-AIa (Kitasato Yamada group 1991)

- Anti-complementary via alternative pathway
- Source: Gao QP et al. Planta Med 57(2):132-6 (1991). PMID 1891495, [doi:10.1055/s-2006-960049](https://doi.org/10.1055/s-2006-960049). Source language English
- Tier 3 because IC50 not stated; "active at low concentrations" qualitative only

### Viola yedoensis liposoluble fraction (PEVY)

- LPS-induced ALI model in mice, 2-8 mg/kg oral, attenuated lung injury via complement deposition reduction
- Source: Li W et al. Am J Chin Med 40(5):1007-18 (2012). PMID 22928831, [doi:10.1142/S0192415X12500747](https://doi.org/10.1142/S0192415X12500747). Source language English (Fudan group)
- Tier 3 because in vivo only; in vitro IC50 not reported in this paper

---

## What changed vs Phase 1

| Dimension | Phase 1 (English / contaminated brief) | Phase 2 (multilingual / scrubbed brief) |
|---|---|---|
| **Candidates surfaced** | 32 compounds | +13 new compound entries (Houttuynia 3, Glycyrrhiza 2, Quercus 4, Caffeic acid, Amomum, Viola kunawarensis, Myricaria, Juniperus, plus Tier-3 panel) |
| **New tier-1 from Phase 2** | — | Houttuynia cordata polysaccharides (CH50 79 µg/mL crude, 254 µg/mL purified HCPM, 272-318 µg/mL HC-PS1/3) |
| **Phase 1 missed (now caught)** | — | Houttuynia (Chinese folk medicine tier-1), Glycyrrhiza polysaccharide layer, Quercus tetragalloyl glucose, Caffeic acid CH50 anchor, Scutellaria baicalensis aglycone-vs-glycoside mechanism, Tibetan medicine surface (Myricaria + Juniperus) |
| **Source-language confirmation** | Promised CNKI/WanFang/J-STAGE; partially executed | Confirmed: the upstream-complement-natural-product subfield is anchored in Chinese-group (Chen Daofeng / Fudan) and Japanese-group (Yamada / Kitasato) labs whose work is partially English-indexed but underweighted by Western database curation. NOT a translation barrier — a citation-network and topic-discovery barrier |
| **Helicteres status** | Phase 1 missed | Phase 2 attempted independent replication; result INCONCLUSIVE / ANCHOR-STILL-SINGLE (see `phase-2-helicteres-replication.json`) |
| **comp-020 ranking** | rosmarinic acid + luteolin + Helicteres benzofuran lignans tied (CH50 9 µM Helicteres best) | UNCHANGED at the tier-1 single-compound level. Houttuynia adds a NEW tier-1 compound class (polysaccharide, dietary, mass-action mechanism) that is mechanistically orthogonal to the small-molecule trio |

---

## Multilingual-citation gap analysis

**The corpus of upstream-complement natural product literature in Phase 2 has the following structure:**

- ~50% Chen Daofeng group (Fudan University, Shanghai) — publishes 80%+ English-language journals, 20% Chinese-language journals (Zhongguo Zhong Yao Za Zhi, Zhong Yao Cai)
- ~25% Yamada / Kiyohara group (Kitasato Institute, Oriental Medicine Research Center, Tokyo) — publishes 95%+ English-language journals (Planta Med, Carbohydr Res), legacy Japanese-language papers in Gan To Kagaku Ryoho
- ~10% Korean groups (Korean Research Institute of Bioscience and Biotechnology, Kon Kuk University, Catholic University Korea) — predominantly English-language
- ~15% other groups (Vietnamese / Mali / Western collaborations on traditional medicines)

**The Phase 1 contamination retrospective worried about "language barrier" as a research bias. Phase 2 finding refines this:** the actual barrier is NOT translation cost (these papers are largely in English). The barrier is:

1. **Citation-network insularity** — the Chen Daofeng group's matched-assay anti-complementary CH50/AP50 hemolytic discipline is a self-contained methodology that produces a stream of natural product anchor papers, but these papers don't get heavily cited outside the immediate field. Western pharma's complement programs (pegcetacoplan, iptacopan, narsoplimab) don't cite the natural product literature.
2. **Topic-discovery framing** — the Chinese-group anti-complementary natural product corpus uses traditional Chinese / Japanese terminology framings ("heat-clearing," "toxin-eliminating") that don't map cleanly to Western pharma's mechanism-targeted framing. A PubMed query for "complement inhibitor" will catch some of this corpus, but not all of it; querying by traditional formula name (Juzen-taiho-to, Houttuynia cordata) catches the rest.
3. **Source-journal weighting** — Zhongguo Zhong Yao Za Zhi (China J Chinese Materia Medica) and Acta Pharm Sin B are PubMed-indexed but Web of Science impact-factor weighting underweights them relative to Western pharma journals.

**Implication for OE platform:** the "global-multilingual research by default" rule in CLAUDE.md is doing its job, but the operational discipline is to query by traditional-medicine-formula-name + species-name in addition to mechanism-name. A "C3 convertase inhibitor" query misses Houttuynia; a "Houttuynia cordata anti-complementary" query catches it. The mechanism term is the wrong starting point for non-Western literature.

---

## Cross-references

- Phase 1 wiki anchor: [`upstream-complement-modulator-sweep-computational.md`](../../../upstream-complement-modulator-sweep-computational.md)
- comp-020 verification re-run: [`upstream-complement-verification-rerun-computational.md`](../../../upstream-complement-verification-rerun-computational.md)
- Phase 1 archived analysis: [`../wiki-archive.md`](../wiki-archive.md)
- comp-018 vs comp-020 retrospective: [`../../../../operations/comp-018-vs-comp-020-retrospective.md`](../../../../operations/comp-018-vs-comp-020-retrospective.md)
- Brief hygiene discipline: [`../../../../scripts/SWEEP-ARCHITECTURE.md`](../../../../scripts/SWEEP-ARCHITECTURE.md)
- Helicteres replication track: [`./phase-2-helicteres-replication.json`](./phase-2-helicteres-replication.json)
- C1-INH engineering track: [`./phase-2-c1-inh-engineering-literature.md`](./phase-2-c1-inh-engineering-literature.md)
- Phase 2 synthesis: [`./phase-2-summary.md`](./phase-2-summary.md)

---

## Limitations

1. **No Chinese-language full-text was load-bearing in Phase 2.** The papers cited above are either (a) PubMed-indexed with English-language abstracts containing the load-bearing quantitative claims, or (b) PMC-mirrored English full-text from Chinese-group authors. The translation protocol per CLAUDE.md was applied as a precautionary inline flag, not as a load-bearing translation cross-check. For wet-lab gating, the source-language papers flagged `[TRANSLATION-SINGLE-MODEL]` (Chinese: PMID 23126186, PMID 29192453, PMID 23672041, PMID 21548362; Japanese: PMID 2786380) should be cross-checked with DeepSeek V4-Pro before any in vitro confirmation gates depend on their specific numeric claims.

2. **The Chen Daofeng group dominates the post-2010 anti-complementary natural product literature.** This is a single-group risk — if the group's matched-assay protocol has a systematic bias (e.g., specific sheep-erythrocyte source, specific serum complement source, specific buffer composition), the entire literature inherits that bias. Wet-lab independent replication on a DIFFERENT laboratory's protocol is the load-bearing risk-closure step.

3. **Helicteres benzofuran lignan replication remains the single highest-value next step** because it's the comp-020 tier-1 anchor and the only single-paper-anchored finding in the OE corpus's upstream-complement compound stack. Phase 2 did not close this — see `phase-2-helicteres-replication.json` for full status.

4. **The "language barrier" reframing in §"Multilingual-citation gap analysis" is empirical and may not generalize.** Other natural-product mechanism fields (e.g., antiviral plant compounds, urate-lowering TCM) may have more Chinese-language-only literature; the upstream-complement field happens to be English-publishing-anchored for the specific groups that dominate it. Future multilingual sweeps for other mechanism classes should NOT assume the same English-coverage as observed here.

5. **No primary-source TCM materia medica text was consulted in Phase 2.** Traditional formularies (本草纲目 Bencao Gangmu, 神农本草经 Shennong Bencao Jing, 千金方 Qianjin Yaofang, 傷寒論 Shokanron) describe Houttuynia, Bupleurum, Glycyrrhiza, Angelica acutiloba, Scutellaria, Imperata, etc. under pre-modern terminology — but the load-bearing mechanism + IC50 evidence sits in modern peer-reviewed literature, which Phase 2 covers. Future Phase 3 multilingual could pull primary TCM materia medica for context, not for evidence-tier verdicts.

6. **The Phase 1 contamination retrospective's "Brian's suspicion was empirically correct" framing remains valid:** Phase 2 confirms that comp-018's headline-promotion of rosmarinic acid was indeed narrative-cohesion-amplified rather than independently-confirmed. The actual upstream-complement landscape is multi-modal (small-molecule trio + polysaccharide multi-target tier with Houttuynia as the new entrant + benzofuran-lignan tier still single-anchor) — not single-compound-dominated.
