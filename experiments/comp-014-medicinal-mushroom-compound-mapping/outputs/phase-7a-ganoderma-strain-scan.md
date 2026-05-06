---
title: "comp-014 Phase 7a — Ganoderma lucidum strain selection + GLPP cultivation lit scan"
date: 2026-05-06
phase: 7-1a (medicinal mushroom complement track — strain selection)
parent: medicinal-mushroom-complement-track.md
scope: Ganoderma lucidum strain identity, GLPP yield/composition by strain, cultivation method, taxonomic verification, multilingual coverage gap
---

# Phase 7a — *Ganoderma lucidum* strain scan for GLPP track

## Bottom line up front

1. The 40.6%-UA-reduction GLPP material from PMID 36385640 (the paper that anchors the Phase 7 track) was produced by the **Lin Zhibin / Lin Shuqian / Lin Dongmei lab** at the **National Engineering Research Center of JUNCAO Technology, Fujian Agriculture and Forestry University (Fuzhou)**, using **Juncao-grass-substrate-cultivated *G. lucidum*** (≈30 papers from this group, 2007–2026). Strain identity is not numbered in the open-access papers — strain code is held internally by Fuzhou Institute of Green Valley Bio-Pharm Technology (the lab's industrial spin-out). Reproducing the 40.6% UA effect *as written* requires either (a) acquiring strain material directly from the Lin lab / Green Valley or (b) accepting strain-substitution risk and re-validating yield + bioactivity.
2. Most commercial "*G. lucidum*" supplements are actually **G. lingzhi** (Wu, Cao & Dai 2012). Reishi is a species *complex*, not a single species; the names "G. lucidum," "G. lingzhi," "G. sichuanense," and "G. sinense" overlap in commerce. **DNA mis-ID rate is high enough that ITS authentication is non-optional** for any reproducibility claim.
3. The cleanest documented, reproducible cultivation method for GLPP is **liquid submerged fermentation on defined natural media** (sucrose + corn flour + potato extract, or starch + wheat bran), followed by ethanol precipitation and DEAE-Sepharose / Sephacryl chromatography. Yields cluster around **30-60 mg polysaccharide / g dry mycelium** under optimized conditions. Solid-state Juncao cultivation is the Lin lab's preferred mode for the mouse-model GLPP material specifically.
4. Multiple GLPP "fractions" have been characterized, and **they are not the same compound.** GL-PP (MW 37,121) and GL-PP2 (MW 31,130) differ in molecular weight, polysaccharide:peptide ratio, and monosaccharide composition (PMID 37852403, PMID 36385640). The 40.6% UA paper used "GLPP" without specifying which sub-fraction — closer reading of the methods section is needed before any wet-lab follow-up.
5. Chinese-language and Japanese-language literature is genuinely indispensable here. Strain catalog numbers (CGMCC, ACCC, KCTC), Juncao protocol details, and the Chinese commercial cultivar landscape (DT, GL-1, Hu-Nong-1, etc.) are absent or barely indexed in PubMed. **Phase 5b CNKI/J-STAGE dive is queued at the end of this document.**

---

## 1. Strain identity — which named *Ganoderma lucidum* strains have substantive published characterization?

### 1.1 Western-published strains with characterized GLPP yield

According to PubMed, only a small set of named G. lucidum / G. lingzhi strains appear with substantive English-language pharmacology + cultivation characterization:

| Strain | Source / accession | Published characterization | Notes |
|---|---|---|---|
| **Lin lab "Juncao-substrate G. lucidum"** | National Engineering Research Center of JUNCAO Technology, Fujian Agriculture and Forestry University (Fuzhou); industrial production via Fuzhou Institute of Green Valley Bio-Pharm Technology | ~30 PubMed papers 2007-2026: GLPP / GL-PP / GL-PP2 isolation, MW, monosaccharide ratios, peptide composition; in vivo HUA (PMID 36385640), nephrotoxicity protection (PMID 41539637, 37852403, 37841924), RA (PMID 37586160), NAFLD (PMID 30196282), reproductive toxicity (PMID 39200097), tumor metastasis (PMID 34305583) | **Highest-evidence strain in the Phase 7 corpus.** Internal strain code not stated in open-access papers; institutional strain (not deposited in CGMCC under a public number that I could confirm). The "grass-cultured" framing refers to the Juncao protocol (Z. Lin's invention; substrate is Juncao grass, *Pennisetum* hybrid). |
| **G. lucidum M9720** | Mycelia bvba (Belgium) | Hennicke et al. 2016 (PMID 27044336) — confirmed as **true G. lucidum sensu stricto** by ITS + β-tubulin + morphology; **lower triterpenic acid content** than M9724 (which is G. lingzhi) | The only commercially-sold strain with confirmed European G. lucidum identity. Useful as the "negative control" / less-bitter reference in any comparative cultivation study. |
| **G. lingzhi M9724** | Mycelia bvba (Belgium) | Hennicke et al. 2016 (PMID 27044336) — confirmed as **G. lingzhi** by ITS + β-tubulin; high triterpenic acid content (bitter ethanol extract) | Likely closer to the "real" Chinese commercial reishi than M9720; commercially available in Europe. |
| **GD strain** + **Du996** | Yangtze Normal University (Chongqing) liquid fermentation study | Luo et al. 2025 (PMID 39717915) — 56.97 mg/g and 53.22 mg/g mycelial polysaccharide respectively under optimized submerged conditions; 20-strain comparison across 9 Ganoderma species | **The single best published strain-comparison study for liquid-fermentation polysaccharide yield.** GD is not deposited in a Western strain bank; Du996 is presumably a Du-family accession (Du280, Du1320 also tested for antioxidant activity). |
| **GLP1-GLP6** (six unspecified strains) | Beijing Technology and Business University + Yunnan Baiyao Group | Zhang et al. 2022 (PMID 35993963) — six G. lucidum mycelial polysaccharides compared for anti-inflammatory + antioxidant activity. **GLP1 had the highest comprehensive score**; GLP1-I (low-MW, β-glycosidic, fractionated by DEAE-52) was the most active subfraction. | Strain identifiers withheld in the published paper. Useful as proof-of-principle that strain choice meaningfully shifts polysaccharide bioactivity, with magnitude on the order of 2-3× across strains. |
| **G. lucidum strain S3** + **"sweet G. lucidum"** + **"G. lucidum of Shinshu"** | Liu et al. 2016 (PMID 30204370, Chinese-language) | Laccase activity + polysaccharide content compared across Ganoderma species; G. gibbosum (NOT G. lucidum) had highest laccase | Polysaccharide content not the primary endpoint; cited here for strain nomenclature reference. |

**What's NOT in PubMed but referenced in the corpus:**

- "Chinese commercial cultivars" routinely cited by name in CNKI papers but not in PubMed: **DT, JN, GL-1, Hu-Nong-1 (沪农1号), Su-Zhi (苏芝), Han-Nong, Te-Te-1, Te-Te-2, Han-Han-2, Nan-tong**. These are the actual strains being cultivated at industrial scale in China for the consumer supplement market. Identifying which of these has published GLPP characterization is the core Phase 5b CNKI deliverable.
- Korean strains (KCTC accessions) and Japanese strains (e.g., Mycoscience Co. cultivars, often called "Ling-shi" or "Mannentake") — not surfaced by PubMed search; J-STAGE has the underlying body of work.
- Genome-sequenced reference: **G. lucidum strain G.260125-1** (Chen et al. 2012, *Nat Commun* — the Lingzhi reference genome). The sequenced genome is widely cited but the strain itself isn't typically used for downstream pharmacology.

### 1.2 Strain-identity issue: the "G. lucidum" label is ~always wrong

Per multiple authoritative analyses (PMID 33180770, 30061872, 27044336, 28798349, 26300957):

- **Loyd et al. 2018 (PMID 30061872):** 20 manufactured products + 17 grow-your-own kits sold as "G. lucidum"; **93% were G. lingzhi**, none were *true* G. lucidum sensu stricto. Some kits also contained G. sessile, G. resinaceum, G. multipileum (non-medicinal Ganoderma species).
- **Gunnels et al. 2020 (PMID 33180770):** 7 store-bought "G. lucidum" supplements from independent suppliers; **100% G. lingzhi** by ITS phylogeny.
- **Wu et al. 2017 (PMID 28798349):** 19 US-purchased G. lucidum supplements analyzed for triterpene + polysaccharide profile; **only 26.3% were consistent with their labeled bioactive content** by saccharide mapping (chemistry-side validation, not just DNA).
- **Hennicke et al. 2016 (PMID 27044336):** of two commercial European strains, M9720 = true G. lucidum, M9724 = G. lingzhi — biochemically and morphologically distinct (notably, **G. lingzhi has substantially more triterpenic acids**).
- **Liao et al. 2015 (PMID 26300957):** ITS2 distinguishes "Chizhi" (red lingzhi, G. lucidum/lingzhi) from "Zizhi" (purple lingzhi, G. sinense); Chinese-cultivated G. lucidum/lingzhi is genetically distinct from European G. lucidum.

**Implication for Open Enzyme:** any Phase 7 protocol that says "use commercial reishi" without specifying ITS-verified G. lingzhi will produce non-reproducible results. The protocol must either (a) require ITS authentication on the source strain or (b) source from Mycelia bvba M9724 / a CGMCC-deposited G. lingzhi accession with published ITS.

---

## 2. GLPP yield + composition by strain

### 2.1 Multiple GLPP fractions exist — they are not interchangeable

The literature uses "GLPP" loosely. What's actually been characterized:

| Fraction | MW | Polysaccharide:peptide ratio | Monosaccharide composition | Source |
|---|---|---|---|---|
| **GL-PP** (Lin lab, 2018 paper) | **42,635 Da** | 88.70 : 11.30 | L-arabinose : D-mannose : D-glucose = **1.329 : 0.372 : 2.953**; 17 amino acids | PMID 29541200 (glioma U251 cells) |
| **GL-PP** (Lin lab, 2023 paper) | **37,121 Da** | 76.39 : 16.35 | xylose : mannose : glucose = **4.83 : 1 : 7.03** | PMID 37852403 (proteinuric nephropathy) |
| **GL-PP2** (Lin lab, 2023 paper) | **31,130 Da** | 64.14 : 17.73 | xylose : mannose : glucose = **2.35 : 1 : 9.38** | PMID 37852403 (same paper) |
| **GLPP** (Lin lab, 2022 HUA paper) | not stated in abstract; previous Lin lab papers reference ~520 kDa for the high-MW fraction | not stated | not stated | PMID 36385640 — **the Phase 7 anchor paper.** Methods section needs deep-read to confirm which sub-fraction was used. |
| **FYGL** ("Fudan-Yueyang-Ganoderma lucidum") | not specified | 17 : 77 protein:polyglycan; 78% glucose in polysaccharide | aspartic acid, glycine, glutamic acid, alanine, serine, threonine dominant | PMID 22453054 (PTP1B inhibitor; db/db diabetes) — **different lab (Fudan), different fraction**, different bioactivity. Often confused with GLPP in citation chains. |
| **GLP1-GLP6** (Zhang 2022) | varies by strain | not reported | not reported | PMID 35993963 — strain comparison; GLP1 best, GLP1-I subfraction had β-glycosidic linkage |

**The 520 kDa figure** referenced in the Phase 7 scope page (`medicinal-mushroom-complement-track.md`) for GLPP from PMID 36385640 — this is **higher than the 31-43 kDa range characterized in the Lin lab's own follow-up papers** (PMIDs 29541200, 37852403). Possibilities:
- (a) The 520 kDa value refers to the *crude* polysaccharide-peptide complex before fractionation, and GL-PP / GL-PP2 are subfractions.
- (b) Different extraction protocols yield different MW distributions in different papers (the Lin lab's protocol has evolved).
- (c) The Phase 6 triage may have pulled the 520 kDa figure from a different paper than 36385640 — this should be re-verified. **comp-014 Phase 5 deep-read of 36385640 lives at `/experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/phase-5-deepread-PMID36385640.md`** — re-check whether 520 kDa was confirmed from the actual methods section or assumed from secondary references.

### 2.2 Cross-strain yield comparison (the closest study to what we want)

**Luo et al. 2025 (PMID 39717915, *Int J Med Mushrooms*)** — 20 Ganoderma strains across 9 species, optimized submerged liquid fermentation:
- Best-yielding strains: **GD (56.97 mg/g)** and **Du996 (53.22 mg/g)** mycelial polysaccharide.
- Average across G. sichuanense and G. lucidum strains: ~35 mg/g.
- No significant difference between cultivated and wild strains (a useful negative result for the strain-source question).
- Optimized medium: soluble starch 25 g/L, wheat bran 3 g/L, KH₂PO₄ 4.5 g/L, pH 4.0, 27°C, 90 rpm, 11 days.
- Antioxidant ranking: Du1320, Du280, GD top three for DPPH; GSD top for ABTS; GD top for hydroxyl radical.

This is the **best-published strain-comparison study for liquid-fermentation polysaccharide yield** I could find in PubMed-indexed English literature. It's recent (2025) and from a Chinese institution (Yangtze Normal University, Chongqing) — strain identifiers GD/Du996/Du1320 are presumably the Du-lab's internal accessions; deposited identifier (CGMCC etc.) not surfaced.

### 2.3 Strain-comparison study #2 — six-strain mycelial polysaccharide bioactivity

**Zhang et al. 2022 (PMID 35993963, *Int J Med Mushrooms*)** — six G. lucidum strains (GLP1-GLP6 mycelial polysaccharides), Beijing Technology and Business University + Yunnan Baiyao Group:
- Anti-inflammatory + antioxidant scoring: **GLP1 > all others** (significant range across strains).
- GLP1 fractionated → GLP1-I (β-glycosidic, low-MW) had distinct structure from GLP1-II.
- Strain identifiers withheld; this is a methodology / proof-of-strain-effect paper, not a strain-cataloging paper.

**Bottom line on strain × yield:** there is **clear evidence that strain choice matters** at the 2-3× level for both polysaccharide yield and bioactivity, but the specific high-yielding strains in Western-indexed literature are all coded with internal lab IDs (GD, Du996, GLP1) rather than deposited public-bank accessions. Reproducing the published yields requires either (a) acquiring strain material from the publishing lab or (b) running the strain comparison de novo with whatever G. lingzhi accession the contributor can source.

---

## 3. Cultivation method — liquid mycelium fermentation vs Juncao solid-state vs hardwood log

### 3.1 Liquid submerged fermentation (defined-medium, scalable)

**Most published yield data uses this method.** Standard protocol pattern across the corpus:

- **Optimized media** (multiple papers converge on similar ranges):
  - Carbon: starch 15-25 g/L, sucrose 25 g/L, or glucose 50 g/L
  - Nitrogen: wheat bran 3 g/L, NH₄Cl 0.375 g/L, peptone, or yeast extract
  - Mineral: KH₂PO₄ 4.5 g/L, CaCl₂ 0.75 g/L, MgSO₄ trace
  - Optional: corn flour 7 g/L, potato extract 300 g/L (Zheng 2026, PMID 41610097)
  - pH: 4.0-6.0
  - Temperature: 27-30°C
  - Agitation: 90-150 rpm
  - Duration: 6-11 days

- **Yield ranges:**
  - Mycelial dry biomass: 5-15 g/L (depending on strain + reactor type)
  - Mycelial polysaccharide: 30-60 mg/g dry mycelium (Luo 2025, Zhang 2022)
  - Exopolysaccharide (EPS, secreted into broth): 0.2-0.74 g/L (Liu 2018 PMID 30263843, Tikhomirova 2024 PMID 39572077)
  - Triterpenoids in mycelia: ~20-32 mg/g (Zheng 2026, PMID 41610097)

- **Reproducibility verdict:** **High.** Multiple labs across China, Russia, Malaysia, Indonesia have reported similar yield ranges with similar media. This is the cleanest cultivation method for an Open Enzyme reproducibility protocol — assumes contributor has access to a 1-3 L bioreactor (or even a 250-mL shake flask, per Zheng 2026's optimized natural medium protocol).

- **Solid-seed inoculum trick** (Liu & Zhang 2018, PMID 30263843): pre-grow on wheat-bran fine powder solid medium, transfer solid seed to liquid culture → **EPS yield 0.74 g/L vs 0.47 g/L for liquid-pellet inoculum** (a 1.6× improvement). Stable for 6 months at storage. Worth incorporating into the SOP if reproducibility is the goal.

### 3.2 Juncao solid-state cultivation (the Lin lab method — the GLPP-for-HUA paper's source)

Juncao technology = a **1986 Chinese invention** by **Lin Zhanxi** (Fujian Agriculture and Forestry University) for cultivating edible/medicinal mushrooms on hybrid grass substrate (*Pennisetum* genus, sugarcane-relatives) instead of hardwood. Juncao = "grass for mushrooms" (菌草). The approach replaces wood substrates with grass, dramatically lowering input costs and enabling mushroom cultivation in regions without forestry resources.

For *G. lucidum* specifically:
- Substrate: dried, chopped Juncao grass (often blended with corn cob, cottonseed hull, or rice bran).
- The Lin lab papers consistently cite "**grass-cultured G. lucidum**" or "Juncao-substrate G. lucidum" as their source material.
- After cultivation, the **fruiting body** is harvested (not just mycelium); GLPP is extracted from the fruiting body via hot-water decoction → ethanol precipitation → DEAE-Sepharose / Sephacryl chromatography.
- A spent-substrate side-stream ("Juncao G. lucidum residue") is increasingly characterized as a feed additive (PMIDs 41933526, 39457856, 39322164 — broiler / duck / poultry studies, all from Fujian Agriculture and Forestry University, all from the Lin / Jin labs).

**Key open question for Phase 5b:** the actual Juncao + G. lucidum cultivation SOP (substrate prep, sterilization, inoculation density, fruiting trigger) is in the Chinese-language Juncao technology manuals (李占熙, 林占熺 et al.) and in CNKI-indexed papers from the Fujian Agriculture and Forestry group. **PubMed has the pharmacology end of this work; it does not have the cultivation SOP.**

**Reproducibility verdict:** **Medium-low for non-Chinese contributors.** Juncao grass is not commercially available in the West. Substituting hardwood log / sawdust block changes the substrate and likely shifts compound profile. If Phase 7 wants to faithfully reproduce the 40.6% UA effect from PMID 36385640, this is a significant constraint.

### 3.3 Hardwood log / sawdust block (Western consumer-kit cultivation)

This is the dominant cultivation method in Western consumer + commercial reishi production:
- Substrate: oak / maple / poplar sawdust + wheat bran + gypsum (typical 70:20:10 ratio); pasteurized or autoclaved; bagged in spawn bags.
- Inoculation: with G. lingzhi (or, less commonly, G. tsugae / G. lucidum sensu stricto for "European reishi") spawn.
- Fruiting: 4-12 weeks; antler vs conk morphology depends on CO₂ levels.
- Fruiting body harvested; ground; extracted as above.

**Yield/quality vs Juncao:** very few rigorous comparative studies. One signal point: Hennicke 2016 (PMID 27044336) found G. lingzhi (M9724) had substantially higher triterpenic acid content than G. lucidum sensu stricto (M9720) when both were cultivated under identical conditions, suggesting **strain identity dominates substrate effects** for triterpene content. Whether this also holds for polysaccharide yield is unclear from PubMed-indexed work.

**Reproducibility verdict:** **High for the cultivation method itself** (consumer kits are widely available, protocols are standardized). **Low for matching the Lin lab's specific GLPP material** without confirming the substrate effect.

### 3.4 Fruiting body vs mycelium — different compounds

A persistent source of confusion in the supplement industry:
- **Mycelium-on-grain** products (mostly grain by mass): polysaccharides come predominantly from the grain (β-glucan from oat / rice cell walls), not from the fungus. Wu 2017 (PMID 28798349) flagged this as a major quality issue in US supplements.
- **Mycelium from liquid fermentation**: clean; mycelial polysaccharide content reproducibly 30-60 mg/g (per Luo 2025).
- **Fruiting body**: distinct compound profile from mycelium — **fruiting body has higher triterpenoid content** (Hennicke 2016); polysaccharide content varies by tissue (cap vs stipe).
- **Spores / spore powder**: yet another distinct fraction; cracked-shell spore powder is a separate commercial product.

The Lin lab's GLPP material is from **fruiting body**, not mycelium. Liquid-fermentation mycelium-derived polysaccharide is a different material with potentially different bioactivity. **Phase 5 deep-read of PMID 36385640 should confirm which (fruiting body vs mycelium) was used in the 40.6% UA study.**

---

## 4. Species mis-identification — prevalence and authentication methods

### 4.1 Prevalence of mis-ID in commercial supplements

Five independent studies converge on a **very high mis-ID rate**:

| Study | Sample size | "G. lucidum" mis-ID rate | Method |
|---|---|---|---|
| Wu et al. 2017 (PMID 28798349) | 19 US supplements | **74% (14/19) failed chemistry-based label verification** | Triterpene + polysaccharide saccharide mapping |
| Loyd et al. 2018 (PMID 30061872) | 20 manufactured + 17 GYO kits | **93% of manufactured "G. lucidum" were G. lingzhi**; 0% were true G. lucidum sensu stricto | ITS + tef1-α + Illumina MiSeq |
| Gunnels et al. 2020 (PMID 33180770) | 7 supplements | **100% G. lingzhi (none true G. lucidum)** | ITS Sanger + RAxML/MrBayes phylogeny |
| Hennicke et al. 2016 (PMID 27044336) | 2 European commercial strains | 1/2 (M9724) was G. lingzhi despite labeled "G. lucidum" | ITS + β-tubulin + UPLC-MS triterpene profile |
| Liao et al. 2015 (PMID 26300957) | 33 wild + commercial samples | Distinguished G. lucidum, G. sinense, G. sichuanense, G. tsugae; Chinese cultivar G. lucidum is genetically distinct from European | ITS2 + RNA secondary structure |

**Synthesis:** **virtually no commercial "G. lucidum" supplement is actually G. lucidum sensu stricto.** Most are G. lingzhi (the actually-medicinal Asian species, sometimes called true reishi). A meaningful fraction are species substitutions (G. sessile, G. resinaceum, G. multipileum, G. applanatum). For Phase 7, this means:

1. The "*Ganoderma lucidum*" label in PMID 36385640 and other GLPP-related papers **should be read as G. lingzhi** by default. The Lin lab's GLPP material is almost certainly from G. lingzhi.
2. Any Open Enzyme protocol that says "obtain G. lucidum" without specifying ITS verification will produce a different organism than the literature describes.
3. The **G. lucidum vs G. lingzhi distinction is biochemically meaningful** (G. lingzhi has higher triterpenic acid content; potentially higher polysaccharide yield, though this isn't conclusively demonstrated). Sourcing matters.

### 4.2 Recommended authentication protocol for Phase 7

Based on the corpus, the protocol for Open Enzyme contributors:

1. **Source strain:** require either (a) Mycelia bvba M9724 (commercially available, ITS-verified G. lingzhi), (b) a CGMCC-deposited G. lingzhi accession with publicly available ITS sequence, or (c) a contributor-collected sample with **mandatory ITS sequencing before use** (the Cao et al. 2012 *Ganoderma*-specific primers G-ITS-F1 / G-ITS-R2, validated by Gunnels 2020, are the cheapest path — ~$20-40/sample at most academic core facilities).
2. **Sequence comparison:** BLAST against NCBI nr/nt; require top hit to be G. lingzhi at >99% identity; reject if top hit is any other Ganoderma species (especially G. lucidum sensu stricto from European clade B).
3. **Confirm with secondary marker** (tef1-α or β-tubulin) for any contributor wanting to publish reproducibility data; sufficient for downstream verification by reviewers.
4. **Document strain provenance in the SOP output** — every Open Enzyme cultivation log should record: source strain ID, supplier, ITS GenBank accession (if newly sequenced), and which clade (A=lingzhi, B=lucidum sensu stricto) it falls in.

This is a meaningful but tractable infrastructure ask — closer to "always run a control" than "build new capability."

---

## 5. Multilingual coverage gap — Chinese / Japanese / Korean primary literature

Per Open Enzyme/CLAUDE.md global-multilingual-research rule: **the Western-PubMed view is severely incomplete for this domain.** Specific gaps:

### 5.1 What's missing from PubMed but exists in Chinese-language literature

- **Industrial cultivar catalog.** Chinese commercial G. lingzhi cultivars are routinely cited in CNKI / Wanfang papers by name (DT, JN, GL-1, Hu-Nong-1, Su-Zhi, Han-Nong, Te-Te series, etc.). Yield characterization, cultivation conditions, regional adaptation data — almost entirely in Chinese. PubMed surfaces ~3-5 of these by name; the actual industry uses 30+.
- **CGMCC / ACCC strain bank deposit data.** Chinese national microorganism strain collections (China General Microbiological Culture Collection Center; Agricultural Culture Collection of China) hold hundreds of G. lingzhi accessions with associated cultivation + bioactivity data. Public catalogs are in Chinese.
- **The Juncao cultivation manual literature.** Lin Zhanxi's body of work on Juncao technology (~30 years, hundreds of papers) is mostly Chinese-language, in journals like 食用菌学报 (*Acta Edulis Fungi*), 中国食用菌 (*Edible Fungi of China*), 福建农林大学学报 (*Journal of Fujian Agriculture and Forestry University*).
- **Regional cultivar pharmacology.** Substantial CNKI literature on regional G. lingzhi cultivars × bioactivity (immunomodulation, anti-tumor, blood-pressure, blood-sugar) using 4-6 regional cultivars in parallel; almost none is indexed in PubMed.

### 5.2 What's missing from PubMed but exists in Japanese-language literature

- **Reishi (霊芝, レイシ) traditional medicine pharmacopoeia data.** Kampo-formula context for G. lucidum / G. lingzhi use (often combined with other herbs); Japanese clinical data on cancer adjuvant use; quality standards from Japan Reishi Association (日本霊芝協会).
- **Mycoscience Co. + commercial Japanese strain characterization.** Japanese commercial reishi cultivars (often labeled by farm or supplier rather than scientific strain ID); spore-shell-cracking technology was developed in Japan and the methodology refinement is in J-STAGE.
- **Mannentake (万年茸) spore oil / sporoderm-broken spore powder literature.** A distinct Japanese product line; characterization papers in CiNii.

### 5.3 What's missing from PubMed but exists in Korean-language literature

- **Yeongji (영지) strain collection in KCTC** (Korean Collection for Type Cultures); regional cultivars adapted to Korean climate.
- **Korean ginseng × reishi formulation studies** (a meaningful body of work in KISS / RISS); not Open-Enzyme-relevant for gout but relevant to broader medicinal-mushroom-complement track.

---

## Phase 5b CNKI / J-STAGE / KCI follow-ups queued

Specific papers / search strategies the contributor or future Open Enzyme work should pursue (no institutional CNKI access in this turn — these are queued for when access is available, or for a Chinese-vendor-LLM-translated shallow scan that may be tractable now):

### Highest priority — would directly close gaps in the Phase 7 deliverable

1. **Lin Zhanxi (林占熺) Juncao G. lucidum cultivation SOP.** CNKI search: `菌草 灵芝 栽培` (Juncao Lingzhi cultivation). Expected hits: substrate preparation ratios (Juncao grass : corn cob : rice bran), sterilization protocols, inoculation density, fruiting trigger conditions, harvest timing. Likely available as a chapter in 林占熺 Juncao technology monograph. **This is the missing reproducibility piece for replicating PMID 36385640's source material.**
2. **Lin Zhibin (林志彬) lab's GLPP fractionation methods paper(s) in Chinese journals.** PubMed has the pharmacology; CNKI may have the underlying chemistry. Search: `灵芝多糖肽 GLPP 分离纯化` (GLPP isolation purification). Expected: hot-water extraction conditions, ethanol precipitation cuts, DEAE-Sepharose elution gradient, MW determination by gel filtration. Critical for confirming whether PMID 36385640's "GLPP" = GL-PP, GL-PP2, or the high-MW (520 kDa?) crude fraction.
3. **Chinese commercial cultivar comparison study.** CNKI search: `灵芝 品种 比较 多糖` (Lingzhi variety comparison polysaccharide). Likely papers comparing 6-10 Chinese commercial cultivars (DT, JN, Hu-Nong-1, etc.) on polysaccharide yield, triterpene content, cultivation cycle length. This is the "industrial cultivar landscape" doc that's missing from PubMed.

### Medium priority — strain bank verification + secondary characterization

4. **CGMCC + ACCC G. lingzhi accession catalog.** Search CGMCC database directly (http://www.cgmcc.net/english/) for "Ganoderma lingzhi" — strain numbers, deposit dates, depositing institution. Specifically look for any deposit traceable to the Lin lab / Fuzhou Institute of Green Valley Bio-Pharm Technology — that would close the strain-identity loop on PMID 36385640.
5. **G. lingzhi vs G. sinense (Zizhi) clinical comparison.** ChiCTR (http://www.chictr.org.cn/) search for "灵芝" + "紫芝" + "高尿酸" (lingzhi + zizhi + hyperuricemia). G. sinense is sometimes used interchangeably with G. lingzhi in Chinese supplements but is a distinct species; clinical comparison data may exist.
6. **J-STAGE Reishi clinical literature.** J-STAGE search: `霊芝 高尿酸血症` (reishi hyperuricemia). Japanese clinical or animal-model data on G. lingzhi for hyperuricemia, separate from the Chinese literature.

### Lower priority — broader corpus

7. **CNKI Pleurotus ostreatus ergothioneine cultivar comparison** (relevant to comp-014 ergothioneine route, distinct from this Ganoderma scan).
8. **CNKI Cordyceps militaris liquid fermentation cordycepin yield** (relevant to comp-014 cordycepin route, distinct from this scan).

### Specific paper IDs flagged as worth chasing

These are paper *concepts* — exact CNKI IDs need a CNKI session to retrieve:
- 林占熺 + 灵芝 + 菌草栽培 (Lin Zhanxi + Lingzhi + Juncao cultivation) — likely 5-10 indexed papers
- 林志彬 + 灵芝多糖肽 (Lin Zhibin + Ganoderma polysaccharide-peptide) — likely 15-30 papers covering pre-PubMed-era chemistry
- 林树钱 + 灵芝 (Lin Shuqian + Lingzhi) — Fuzhou Institute of Green Valley spinout's cultivation work
- 包海鹰 + 灵芝 + 多糖 (Bao Haiying + Lingzhi + polysaccharide) — Jilin Agricultural University, separate Chinese strain comparison group

---

## Priority strain shortlist for Phase 7 follow-up cultivation work

Synthesizing across questions 1-5, the Open-Enzyme-tractable strain options for any Phase 7 wet-lab follow-up:

| Rank | Strain | Why | Caveat |
|---|---|---|---|
| 1 | **Mycelia bvba M9724 (G. lingzhi)** | Commercially available, ITS-verified G. lingzhi, biochemically characterized triterpene profile, European supplier (no China-import friction) | Not the exact Lin lab strain; ~2-3× yield variability vs published GD/Du996 expected |
| 2 | **CGMCC-deposited G. lingzhi accession (any) with ITS/tef1-α published** | Public deposit, traceable, Chinese-source matches ancestral cultivar lineage | Phase 5b CNKI dive needed to identify which accessions have published characterization |
| 3 | **GD strain (Yangtze Normal U)** or **Du996** | Highest published mycelial polysaccharide yield (PMID 39717915, 56-57 mg/g) | Not deposited in public bank; would require collaboration with Chongqing lab |
| 4 | **Lin lab Juncao-strain (PMID 36385640 source)** | The actual strain behind the 40.6% UA result | Would require collaboration with Fuzhou lab + Juncao substrate access |
| 5 | **Contributor-sourced consumer-kit reishi + ITS authentication** | Lowest cost; tractable for any contributor anywhere | High variance in actual species (often G. lingzhi but sometimes G. multipileum / G. sessile); yield + bioactivity will diverge from any specific paper |

---

## Cross-references

- Parent scope page: [`medicinal-mushroom-complement-track.md`](../../../wiki/medicinal-mushroom-complement-track.md)
- comp-014 Phase 5 deep-read of the GLPP-HUA paper: [`phase-5-deepread-PMID36385640.md`](./phase-5-deepread-PMID36385640.md)
- comp-014 parent computational page: [`medicinal-mushroom-compound-mapping-computational.md`](../../../wiki/medicinal-mushroom-compound-mapping-computational.md)
- comp-014 anchor list (Phase 4): [`phase-4-ranked-candidates.md`](./phase-4-ranked-candidates.md)
- Open Enzyme global multilingual research rule: top-level CLAUDE.md §"Global-multilingual research by default"

## Citations (PubMed)

According to PubMed, the following articles were used in this scan:

**GLPP characterization (Lin lab + Fudan + others):**
- Hou Z et al. 2026 (PMID 41539637) [DOI](https://doi.org/10.1016/j.jep.2026.121210) — GL-PP / GL-PP2 cisplatin nephroprotection
- Zhang H et al. 2024 (PMID 39200097) [DOI](https://doi.org/10.3390/biomedicines12081632) — GLPP cyclophosphamide reproductive injury
- Fang H et al. 2023 (PMID 37852403) [DOI](https://doi.org/10.1016/j.ijbiomac.2023.127336) — GL-PP vs GL-PP2 proteinuric nephropathy (key MW + composition reference)
- Fang H et al. 2023 (PMID 37841924) [DOI](https://doi.org/10.3389/fphar.2023.1287908) — GL-PP doxorubicin nephropathy ("grass-cultured")
- Meng M et al. 2023 (PMID 37586160) [DOI](https://doi.org/10.1016/j.phymed.2023.155010) — GLPP rheumatoid arthritis
- Xie J et al. 2023 (PMID 37305093) [DOI](https://doi.org/10.3389/fnut.2023.1179749) — GLPP immune dysfunction
- **Lin S et al. 2022 (PMID 36385640) [DOI](https://doi.org/10.1039/d2fo02431d) — GLPP HUA 40.6% UA reduction (the Phase 7 anchor paper)**
- Xian H et al. 2021 (PMID 34305583) [DOI](https://doi.org/10.3389/fphar.2021.650216) — GL-PP melanoma metastasis
- Zhong D et al. 2018 (PMID 30196282) [DOI](https://doi.org/10.1159/000493297) — GLPP NAFLD
- Wang C et al. 2018 (PMID 29541200) [DOI](https://doi.org/10.3892/ol.2018.7823) — GL-PP grass-cultured glioma U251 (key MW reference)
- Zhong D et al. 2015 (PMID 26603550) [DOI](https://doi.org/10.1038/srep16910) — GLPP renal ischemia reperfusion
- Cao QZ et al. 2007 (PMID 18087562) — Gl-PP lung carcinoma invasion (Chinese-language paper, no DOI in record)
- Wang CD et al. 2012 (PMID 22453054) [DOI](https://doi.org/10.1017/S0007114512000153) — FYGL (Fudan-Yueyang-Ganoderma lucidum) PTP1B db/db diabetes

**Strain comparison + yield:**
- Luo S et al. 2025 (PMID 39717915) [DOI](https://doi.org/10.1615/IntJMedMushrooms.2024056392) — 20-strain submerged fermentation comparison (GD, Du996 best)
- Zhang J et al. 2022 (PMID 35993963) [DOI](https://doi.org/10.1615/IntJMedMushrooms.2022044274) — six-strain GLP1-GLP6 mycelial polysaccharide comparison
- Liu Y et al. 2016 (PMID 30204370) — Ganoderma species laccase + polysaccharide (Chinese-language, no DOI)
- Xie C et al. 2020 (PMID 32865920) [DOI](https://doi.org/10.1615/IntJMedMushrooms.2020035042) — fermentation broth vs fruiting body bioactivity
- Liu SR & Zhang WR 2018 (PMID 30263843) [DOI](https://doi.org/10.1007/s10068-018-0343-z) — solid-seed inoculum hyperproduction
- Tikhomirova T et al. 2024 (PMID 39572077) [DOI](https://doi.org/10.1093/lambio/ovae115) — bioreactor scale-up + RSM
- Zheng S et al. 2026 (PMID 41610097) [DOI](https://doi.org/10.1371/journal.pone.0337539) — natural-medium submerged fermentation optimization

**Authentication / species verification:**
- Loyd AL et al. 2018 (PMID 30061872) [DOI](https://doi.org/10.3389/fmicb.2018.01557) — 93% mis-ID rate, "Mushroom of Immortality" study
- Gunnels T et al. 2020 (PMID 33180770) [DOI](https://doi.org/10.1371/journal.pone.0236774) — ITS barcoding 100% G. lingzhi mis-ID
- Hennicke F et al. 2016 (PMID 27044336) [DOI](https://doi.org/10.1016/j.phytochem.2016.03.012) — M9720 (G. lucidum) vs M9724 (G. lingzhi) biochemistry
- Wu DT et al. 2017 (PMID 28798349) [DOI](https://doi.org/10.1038/s41598-017-06336-3) — 26.3% chemistry-verified rate in US supplements
- Liao B et al. 2015 (PMID 26300957) [DOI](https://doi.org/10.1186/s13020-015-0056-7) — ITS2 Chinese vs European G. lucidum
- Khan MA et al. 2016 (PMID 27706590) [DOI](https://doi.org/10.4238/gmr.15038536) — SCAR markers for Ganoderma authentication
- Fu JJ et al. 2015 (PMID 26125765) [DOI](https://doi.org/10.4238/2015.May.25.19) — RAPD-SCAR Ganoderma species
- Fu CM et al. 2009 (PMID 18942087) [DOI](https://doi.org/10.1002/bmc.1111) — HPLC fingerprint for Ganoderma differentiation

**Juncao substrate cultivation context:**
- Cai ZX et al. 2026 (PMID 41933526) [DOI](https://doi.org/10.1016/j.psj.2026.106822) — Juncao G. lucidum residue in duck feed
- Gao YY et al. 2024 (PMID 39457856) [DOI](https://doi.org/10.3390/ani14202926) — Juncao G. lucidum residue in broiler feed (immune/intestinal)
- Gao YY et al. 2024 (PMID 39322164) [DOI](https://doi.org/10.1016/j.ijbiomac.2024.135918) — Juncao G. lucidum residue in broiler (lipid/antioxidant)
