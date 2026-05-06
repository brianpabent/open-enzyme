---
title: "Phase 7-1b — Cordyceps militaris strain selection + cordycepin yield characterization"
date: 2026-05-06
experiment: comp-014
phase: 7-1b
related:
  - "../../wiki/medicinal-mushroom-complement-track.md"
  - "../PHASE-5-FINDINGS.md"
  - "phase-5-deepread-PMID41905012.md"
tags: [cordyceps-militaris, cordycepin, strain-selection, fermentation, lit-scan, multilingual-gap]
---

# Phase 7-1b — Cordyceps militaris strain × cordycepin yield scan

**Scope:** strain identity, yield-by-method, ADA substrate paradox, co-fermentation precedents, multilingual coverage gap.

**Source attribution:** All PubMed-derived findings cite PMID + DOI inline. Per PubMed MCP attribution requirement, full DOIs are linked at first mention.

---

## 1. Strain identity — named C. militaris strains with substantive characterization

The published C. militaris strain catalog is fragmented across Chinese (CGMCC, GDMCC), Korean (KCTC, KACC, mating-derived KSP/KYL), Taiwanese (BCRC, "Zhangzhou"), Japanese (NBRC, JCM), and Western (ATCC, NRRL) collections. Strain accession numbers rarely appear in the title/abstract — most papers reference an in-house number tied to a specific lab, and the authoritative deposit identifier is buried in M&M. Below is what surfaces as load-bearing in the cordycepin-yield literature:

| Strain | Origin / Accession | Yield (cited) | Method | Source |
|---|---|---|---|---|
| **GDMCC 5.270** | Guangdong Microbial Culture Collection (China) | 343 mg/L cordycepin in submerged culture with corn-steep-liquor hydrolysate (4.83× over no-CSLH control) | Submerged liquid + CSLH nitrogen | Chang et al. 2024 (PMID 38472926, [10.3390/foods13050813](https://doi.org/10.3390/foods13050813)) |
| **GYS60** | Mutant from wild C. militaris via multifunctional plasma mutagenesis (Beijing Polytechnic) | **7,883 mg/L (7.88 g/L)** — >20× over wild parent | Static liquid + plasma mutation | Zhang H et al. 2020 (PMID 33463932, [10.1615/IntJMedMushrooms.2020037153](https://doi.org/10.1615/IntJMedMushrooms.2020037153)) |
| **KSP8** | Korean mating-derived strain (sexual recombination); Pukyong Nat'l Univ. | "Significantly higher" cordycepin (numeric not in abstract; full text required) | Liquid culture | Kang N et al. 2017 ([PMC5395498](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5395498/)) |
| **KYL05** | Korean mutated strain | ~445 mg/L cordycepin with casein hydrolysate | Submerged | Lee SK et al. 2019 ([10.3390/biom9090461](https://doi.org/10.3390/biom9090461)) |
| **KN-1** | Chinese strain (Jiangsu Acad. Agri. Sci.) | 84% increase in fruiting-body cordycepin at 25°C vs control | Fruiting body, temperature-regulated | Shao J et al. 2026 (PMID 41745261, [10.3390/jof12020118](https://doi.org/10.3390/jof12020118)) |
| **"Zhangzhou" (FRE-Z)** | Wild Taiwanese strain | High cordycepin in brown-rice solid-state fermentation (FRE-Z) — direct numeric not in abstract; comparator strain "L" lower | Brown rice SSF | Wu HC et al. 2019 (PMID 31679300, [10.1615/IntJMedMushrooms.2019031138](https://doi.org/10.1615/IntJMedMushrooms.2019031138)) |
| **C. militaris H, L** (Da-Yeh Univ., Taiwan) | Two paired Taiwanese strains | Up to **25.07 mg/g** cordycepin in fruiting body on wheat + monosodium glutamate substrate | Solid grain SSF | Liang ZC et al. 2014 (PMID 25404221, [10.1615/intjmedmushrooms.v16.i6.60](https://doi.org/10.1615/intjmedmushrooms.v16.i6.60)) |
| **C. militaris (Da-Yeh)** | Taiwanese, undisclosed strain ID | **13.1 ± 0.36 mg/g** in germ rice fruiting body | Rice-varietal SSF | Liu ML et al. 2024 (PMID 38967211, [10.1615/IntJMedMushrooms.2024054150](https://doi.org/10.1615/IntJMedMushrooms.2024054150)) |
| **C. militaris (IoT-AAFRFS)** | Taiwanese (Da-Yeh / Chung Shan) | **1.44 g/L (103.2 mg/L/d)** at 5 L scale, hypoxic-induced | IoT-regulated submerged + CO₂ feedback | Chien TY et al. 2025 (PMID 39819523, [10.1615/IntJMedMushrooms.2024057399](https://doi.org/10.1615/IntJMedMushrooms.2024057399)) |
| **C. militaris (Sichuan Agri.)** | Chinese, in-house | 2,008 mg/L (1000 mL glass jar), liquid static | Optimized static liquid | Kang C et al. 2014 (PMID 25054182, [10.1155/2014/510627](https://doi.org/10.1155/2014/510627)) |
| **C. militaris (Nanjing Tech)** | In-house | Liquid fermentation, 69.2% boost from VeA overexpression + tea polyphenol cofeed | Submerged + genetic + chemical | Niu H et al. 2025 (PMID 41045993, [10.1016/j.biortech.2025.133438](https://doi.org/10.1016/j.biortech.2025.133438)) |
| **C. militaris (Nantong)** | In-house | 7.35 g/L static liquid culture (5 L fermenter) | Optimized static liquid | Tang J et al. 2014 (PMID 24117155, [10.1080/10826068.2013.833111](https://doi.org/10.1080/10826068.2013.833111)) |

**Heterologous chassis strains for comparison (engineered, not native C. militaris):**

| Chassis | Strain ID | Yield | Source |
|---|---|---|---|
| *Yarrowia lipolytica* | YlCor-18 | 4,362 mg/L (Cns1+Cns2 combinatorial) | Song Z et al. 2023 (PMID 36791366, [10.1021/acssynbio.2c00570](https://doi.org/10.1021/acssynbio.2c00570)) |
| *Y. lipolytica* | YL-CD3 | **4,780 mg/L** (lipid-droplet compartmentalization) | Duan XY et al. 2025 (PMID 40367369, [10.1021/acs.jafc.5c03654](https://doi.org/10.1021/acs.jafc.5c03654)) |
| *Pichia pastoris* | Pp29 | **8.11 g/L (10 L fed-batch)** — highest reported titer in any heterologous system | Zhao B et al. 2024 (PMID 39241814, [10.1016/j.biortech.2024.131446](https://doi.org/10.1016/j.biortech.2024.131446)) |
| **Aspergillus oryzae** (food-grade, GRAS, **direct relevance to OE koji track**) | A. oryzae + cns1/cns2 | **564.6 mg/L/d productivity** in submerged fermentation | Jeennor S et al. 2023 (PMID 38071331, [10.1186/s12934-023-02261-5](https://doi.org/10.1186/s12934-023-02261-5)) |
| *Saccharomyces cerevisiae* S288C | + ScCNS1/ScCNS2 | 137 mg/L fed-batch | Huo C et al. 2021 (PMID 34622640, [10.13345/j.cjb.200738](https://doi.org/10.13345/j.cjb.200738)) |

**Note on comp-014 koji track relevance:** the Jeennor 2023 *A. oryzae* result ([10.1186/s12934-023-02261-5](https://doi.org/10.1186/s12934-023-02261-5)) is **the highest-priority hit** for OE's koji thesis — cordycepin is already producible in food-grade A. oryzae at >500 mg/L/d via cns1+cns2 expression under constitutive promoters, on glucose. This converts cordycepin from a "co-fermentation Cordyceps × koji" question to a "single-organism engineered koji" question. Cross-link to comp-014 Phase 8 chassis triage.

---

## 2. Cordycepin yield by method — what's reproducible at scale

### Method-level yield landscape (native C. militaris only):

| Method | Typical range | Best reported | Notes |
|---|---|---|---|
| **Wild fruiting body** (uncultivated) | 0.3–1.0 mg/g dry | ~10 mg/g (atypical) | Hur 2008 ([10.4489/MYCO.2008.36.4.233](https://doi.org/10.4489/MYCO.2008.36.4.233)) — fruiting body 0.97% (9.7 mg/g), corpus 0.36% (3.6 mg/g) |
| **Solid-state fermentation, brown rice** | 1–10 mg/g substrate | 25 mg/g (W+Mg, Liang 2014) | Most reproducible per Park 2025 review (PMID 41097576, [10.3390/foods14193408](https://doi.org/10.3390/foods14193408)) |
| **Solid-state, mixed grains** | Higher than single-grain | 1.6–2.0 mg/g (Borde 2023, PMID 37930616, [10.1007/s42770-023-01169-x](https://doi.org/10.1007/s42770-023-01169-x)) | Rice + wheat + jowar + bajra + sugarcane bagasse |
| **Solid-state, edible insect substrate** | Variable | **34× higher than pupae** when grown on *Allomyrina dichotoma* (Korean rhinoceros beetle) — oleic acid as the key driver, upregulating cns1/cns2 transcription (Turk 2022, PMID 36338069, [10.3389/fmicb.2022.1017576](https://doi.org/10.3389/fmicb.2022.1017576)) | Direct transcriptional link to biosynthesis genes |
| **Liquid submerged, optimized media** | 0.3–2 g/L | **7.35 g/L** (Tang 2014); 7.88 g/L (Zhang H 2020 mutant GYS60) | Static culture is dominant format; air-supply matters |
| **Liquid + IoT/hypoxic regulation** | 1–1.5 g/L | 1.44 g/L (Chien 2025) | Productivity 103 mg/L/d at 5 L |
| **Submerged + insect-derived nitrogen** | Higher than peptone-only | 1.49 g/L (cottonseed + perilla oil, Kim CB et al. 2025, PMID 40549333, [10.1007/s42770-025-01713-x](https://doi.org/10.1007/s42770-025-01713-x)) | **DPRK-authored** (Kim Il Sung University, Pyongyang) — multilingual relevance |
| **Submerged + pupa powder / wheat bran** | 30% boost over peptone | 50% cost reduction (Luo 2018, PMID 30507305, [10.1080/10286020.2018.1539080](https://doi.org/10.1080/10286020.2018.1539080)) | Pupa powder = nitrogen source, also addresses Q3 ADA paradox |
| **Mating-derived hybrid strain** (sexual recombination) | High intra-strain variance | Significantly higher (Kang 2017 KSP8) | Korean approach to overcome culture degeneration |

**Most reproducible method per the Park 2025 review (the canonical synthesis):** brown rice solid-state for fruiting bodies remains dominant, but **liquid submerged is taking over industrially** because of shorter cycle (14–25 days vs 60–90 days), better oxygen control, and bioreactor scalability. The Park 2025 review explicitly identifies (i) absence of standardized cultivation protocols, (ii) incomplete metabolite-regulatory understanding, and (iii) scale-up barriers (oxygen transfer, foam, downstream) as the field's open gaps.

**Culture degeneration warning:** Shrestha et al. 2012 (PMC3408298) — single-ascospore progeny show declining fruiting-body productivity over generations. This is a recurring failure mode in commercial Cordyceps cultivation; the GYS60-style plasma mutagenesis approach and the KSP8-style mating recombination approach are both responses to this.

---

## 3. Adenosine deaminase substrate paradox — addressed in literature

Three papers directly address the cordycepin → 3'-deoxyinosine ADA deamination problem:

1. **Xia Y et al. 2017** (PMID 29056419, [10.1016/j.chembiol.2017.09.001](https://doi.org/10.1016/j.chembiol.2017.09.001)) — *the canonical paper.* Cordycepin and pentostatin are co-produced from a **single gene cluster** in C. militaris. PTN is the "safeguard molecule" — it inhibits ADA and protects cordycepin from deamination. ADA is derepressed only when cordycepin reaches self-toxic levels, allowing detoxification to 3'-deoxyinosine. **Key implication for OE:** if you grow C. militaris (or any heterologous chassis with the full cluster), you get cordycepin AND its built-in ADA inhibitor. This dramatically changes the in vivo bioavailability calculation — cordycepin from native cluster expression is co-delivered with PTN (a clinically validated FDA-approved ADA inhibitor used in hairy cell leukemia).

2. **Zhao X et al. 2018** (PMID 30454654, [10.1016/j.micres.2018.09.005](https://doi.org/10.1016/j.micres.2018.09.005)) — Cordyceps kyushuensis transcriptome/proteomics confirms the four-gene cluster (ck1–ck4) producing both cordycepin and pentostatin. Generalizes the Xia 2017 result across Cordyceps species.

3. **Karwowski 2025** (PMID 40871530, [10.3390/molecules30163377](https://doi.org/10.3390/molecules30163377)) — 8-oxo-cordycepin is **not a substrate for ADA**, suggesting an oxidative modification path that could deliver cordycepin pharmacology without the deamination liability. UV+RP-HPLC + DFTB computational evidence; in vitro and in vivo follow-up not yet done. Speculative but interesting for downstream H-card formation.

4. **Wang Y et al. 2014** (PMID 25404221, [10.1615/intjmedmushrooms.v16.i6.60](https://doi.org/10.1615/intjmedmushrooms.v16.i6.60)) — co-quantifies cordycepin, adenosine, AND mannitol across substrates, providing the C. militaris fingerprint required for fermentation-balance analysis. Adenosine present at 0.7–0.94 mg/g vs cordycepin 22–25 mg/g in fruiting bodies (cordycepin/adenosine ratio ~25–35× — consistent with active cluster expression and PTN-mediated ADA suppression).

5. **Wang Y et al. 2021** (PMID 34239513, [10.3389/fmicb.2021.698436](https://doi.org/10.3389/fmicb.2021.698436)) — hypoxic engineering with Vitreoscilla hemoglobin **inverts the adenosine/cordycepin ratio** (cordycepin drops to 9–15% of control while adenosine increases). Confirms the pathway is regulated by oxygen state and that ADA activity, cordycepin biosynthesis, and adenosine pool are tightly coupled.

**Bottom line on Q3:** the ADA paradox isn't actually a paradox in fungal cell context — C. militaris has solved it via the PTN safeguard. The deamination concern applies primarily to **purified cordycepin oral delivery without PTN**. Whole-mycelium / whole-fermentate preparations (which is what koji-track delivery would naturally be) carry both molecules in the native ratio. **This is a load-bearing finding** for comp-014 Phase 6's URAT1 thesis: ALLN-346-style oral delivery via fermentation extract preserves the PTN co-presence; injecting purified cordycepin does not.

---

## 4. Co-fermentation precedents — explicit GLPP+cordycepin search

### Astragalus × Cordyceps co-fermentation (the AMC-BFE precedent):
PubMed-indexed search for "Cordyceps militaris" AND "Astragalus" AND solid-state returns **zero hits** beyond the AMC-BFE paper (PMID 41905012) already in comp-014's Phase 5 deepread. This is *itself* a finding — AMC-BFE represents one of the very few PubMed-indexed C. militaris × medicinal-herb co-fermentation papers, and the underlying methodology probably has a much deeper Chinese-language patent / CNKI literature shadow.

### Cordyceps + ginseng (closest analog):
Zhao X et al. 2025 (PMID 41550597, [10.1016/j.jgr.2025.09.001](https://doi.org/10.1016/j.jgr.2025.09.001)) — *American ginseng + C. militaris* bidirectional solid-state fermentation. C. militaris β-glucosidase converts Rb1 → Rd → F2 → CK (rare ginsenoside CK rose from undetectable to 11.81 mg over 40 days). Cordycepin levels increased over time in the same vessel. **This is the strongest published GLPP-analog precedent** — same operating principle (Cordyceps secretes enzymes that bioconvert herb saponins/glycosides into rare aglycones; herb nutrients upregulate cordycepin biosynthesis) — applied to ginseng instead of Ganoderma.

### Cordyceps + herbal substrate generally (CMSSF):
Pi CC et al. 2024 (PMID 39604968, [10.1186/s12917-024-04338-8](https://doi.org/10.1186/s12917-024-04338-8)) — "C. militaris solid-state fermentation" (CMSSF) on undisclosed herbal substrate, shown to enhance pig immunity/antioxidant function. The Taguchi method optimization confirms commercial-scale CMSSF as an established platform. Multiple Korean / Taiwanese commercial operations use this format.

### Cordyceps + Bacillus subtilis (tandem):
Wu FC et al. 2013 (PMID 23796221, [10.1615/intjmedmushr.v15.i4.70](https://doi.org/10.1615/intjmedmushr.v15.i4.70)) — Bacillus subtilis natto first produces levan, then C. militaris is grown on the spent medium. Tandem (not simultaneous) co-culture; demonstrates that fermentation residues can serve as Cordyceps substrate.

### **Direct GLPP × cordycepin co-fermentation: zero PubMed hits.**
Searches for "Cordyceps militaris + Ganoderma lucidum" co-culture / co-fermentation return **no published precedent** in PubMed-indexed English literature. The Chrysostomou 2024 toxicology paper (PMC11558339) tests Ganoderma + Cordyceps mushroom powders **separately** in the same study but does not co-ferment them. The Phase 6 GLPP+cordycepin synergy hypothesis appears to be **genuinely novel** in PubMed-indexed literature.

**Caveats — this is the multilingual coverage gap:** Ganoderma and Cordyceps are *the* two flagship Chinese medicinal fungi. The probability that no Chinese-language paper has tested co-fermentation is essentially zero. A CNKI / Wanfang search is required before declaring novelty (see §5).

### Related precedent — synergistic platform validation:
- **Chitin + aged rice + C. militaris** (Guo A et al. 2025, PMID 40278135, [10.3390/jof11040315](https://doi.org/10.3390/jof11040315)) — chitin waste at ≤5% upregulates cordycepin and piplartine.
- **Tea polyphenols + VeA overexpression** (Niu 2025, PMID 41045993) — exogenous polyphenols + genetic intervention give 69.2% cordycepin boost. *Tea polyphenols share structural class with G. lucidum triterpenoids* (both polyphenolic, both pentose-phosphate-pathway-modulating). Provides indirect mechanistic prior for why GLPP + C. militaris co-fermentation could work.

---

## 5. Multilingual coverage gap — Phase 5b CNKI/KISS/J-STAGE follow-ups queued

Cordyceps research is ~60–70% Chinese-language by paper volume (CNKI + Wanfang) and ~10–15% Korean (KISS, RISS). PubMed-indexed English literature substantially under-represents the actual field. Specific gaps:

### 5b-Q1: Direct GLPP × cordycepin co-fermentation (highest priority)
- **CNKI search terms:** 灵芝 灵芝多糖 蛹虫草 共培养 / 灵芝 蛹虫草 双菌发酵 / 灵芝 蛹虫草 协同
  - English gloss: "Ganoderma lucidum polysaccharide × Cordyceps militaris co-culture / dual-fungus fermentation / synergistic"
- **Hypothesis to falsify:** that no Chinese-language precedent exists. If 2+ papers found, the comp-014 Phase 6 GLPP+cordycepin hypothesis converts from "novel" to "validated and refined." If zero, the novelty claim survives the multilingual filter.
- **Why this is load-bearing:** the Phase 6 synergy hypothesis is one of the cheapest experimental items in the comp-014 queue. Whether it is novel or already tested in Chinese literature changes the experimental design priority — if validated, deep-read those papers and skip to the next-step refinement; if novel, design clean fermentation.

### 5b-Q2: Strain accession map (high priority)
- **CGMCC, CCTCC** (China) — query CNKI for systematic strain comparisons. Specific accessions like CGMCC 3.4622, CCTCC AF 95015 surface only in M&M sections, not abstracts.
- **KCTC, KACC** (Korea) — KISS/RISS for systematic strain-yield comparisons. The KSP8 paper (Kang 2017) and KYL05 paper (Lee 2019) are likely the tip of a much larger KSP/KYL/KACC strain catalog.
- **NBRC, JCM** (Japan) — J-STAGE for any cordycepin-yield characterization. Japan has a substantial Cordyceps culinary/commercial industry but lower research volume vs China/Korea.

### 5b-Q3: Silkworm-pupae cultivation (medium priority)
- The Wang Y 2021 paper (PMID 34239513) documents that silkworm-pupae substrate produces **higher cordycepin than rice or broth** because of hypoxic pupa hemocoel + unique nutrient profile, but the published English literature on silkworm-pupae cultivation is thin. **CNKI/J-STAGE** are likely to have substantial primary-cultivation literature.
- **CNKI:** 蚕蛹 虫草 培养 / 蚕蛹 蛹虫草 发酵
- **J-STAGE:** カイコ 冬虫夏草 培養 (silkworm × cordyceps × cultivation)

### 5b-Q4: Pentostatin co-production / ADA escape
- The Xia 2017 paper (PMID 29056419) is the canonical PTN safeguard finding. Chinese-language follow-up (CNKI: 喷司他丁 蛹虫草 / 腺苷脱氨酶 抑制 蛹虫草) likely has substantial PTN-quantification and clinical-relevance work.
- DPRK paper (Kim CB et al. 2025, PMID 40549333) demonstrates the field is also active in non-PRC East Asia. Kim Il Sung University publishes regularly to Western journals — this corner of the field is more accessible than expected.

### 5b-Q5: Korean industrial strain selection
- The KSP and KYL strain series + commercial Mushtech / King's Ground Biotech operations all suggest a substantial Korean-language literature on strain-improvement methodology that hasn't surfaced in English-only PubMed scans.
- **KISS:** 동충하초 균주 선발 / 동충하초 코디세핀 수율
- **RISS:** Korean theses (PhD dissertations) on Cordyceps strain breeding likely contain unpublished yield numbers.

### 5b-Q6: TCM × cordycepin clinical evidence (gout-relevant)
- Comp-014 Phase 6 PURSUE'd cordycepin on URAT1 modulation evidence (PMID 29422889 — mouse SUA 337→203 µmol/L). The PRC clinical literature on Cordyceps × hyperuricemia × gout is **substantial** and almost entirely in Chinese.
- **CNKI:** 蛹虫草 高尿酸血症 / 蛹虫草 痛风 / 虫草素 尿酸 — likely yields 5–20+ small-cohort RCTs that PubMed never sees.

---

## Phase 5b CNKI/KISS/J-STAGE follow-ups — explicit queue

Hand off the following multilingual queries to the next subagent (with translation protocol per Open Enzyme CLAUDE.md §"Translation protocol — two-model independent cross-check"):

| ID | Source | Query (original language) | Priority | Why |
|---|---|---|---|---|
| **5b-1** | CNKI | 灵芝多糖 蛹虫草 共培养 / 灵芝 蛹虫草 双菌发酵 | **HIGH** | Direct test of Phase 6 GLPP+cordycepin novelty claim |
| **5b-2** | KISS / RISS | 동충하초 균주 KSP / KYL 코디세핀 | HIGH | KSP/KYL strain catalog, mating-derived hybrid yields |
| **5b-3** | CNKI | 蛹虫草 痛风 / 蛹虫草 高尿酸血症 / 虫草素 尿酸 | HIGH | Chinese clinical-cohort gout evidence — comp-014 Phase 6 URAT1 evidence depth |
| **5b-4** | CNKI | 蚕蛹 虫草 培养 / 蚕蛹 蛹虫草 发酵 | MED | Silkworm-pupae cultivation; commercial-scale yield numbers |
| **5b-5** | CNKI | 喷司他丁 蛹虫草 / 腺苷脱氨酶 抑制 蛹虫草 | MED | PTN safeguard — Chinese follow-up to Xia 2017 |
| **5b-6** | J-STAGE | カイコ 冬虫夏草 培養 / 冬虫夏草 コルジセピン | MED | Japanese silkworm cultivation tradition |
| **5b-7** | CNKI | 蛹虫草 菌种 CGMCC 选育 高产 | LOW (broad) | Strain accession × yield baseline map |

Translation protocol reminder: use Claude (or Gemini) + DeepSeek (or Qwen) for two-vendor parallel translation, sentence-level disagreement annotations. Tag any load-bearing yield numbers, mechanism claims, or evidence-tier hedging language with `[TRANSLATION-DISAGREEMENT]` if models differ.

---

## Cross-references back into the OE wiki

- `wiki/medicinal-mushroom-complement-track.md` — Phase 7 scope page; cordycepin track section needs strain-table propagation
- `wiki/synthesis.md` — append Phase 7-1b finding card under comp-014 entries
- `experiments/comp-014-medicinal-mushroom-compound-mapping/PHASE-5-FINDINGS.md` — link from URAT1 / cordycepin section
- `experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/phase-5-deepread-PMID41905012.md` — AMC-BFE cross-link for co-fermentation §4
- Open Enzyme koji track (root `index.md`, `wiki/engineered-koji-protocol.md` if present) — propagate the **Jeennor 2023 A. oryzae cns1+cns2 result (564 mg/L/d)** as a major cross-track finding. Cordycepin is producible directly in food-grade A. oryzae — major chassis-decision implication.

---

## Evidence-level summary (per OE CLAUDE.md §5)

- All yield numbers cited from published peer-reviewed papers — **In Vitro / Bioprocess** evidence tier.
- Strain catalog: deposited and cited but not independently re-cultured by OE — **Mechanistic Extrapolation** for any specific strain choice.
- ADA paradox resolution (Xia 2017 PTN safeguard cluster): **In Vitro + Genetic** evidence; high confidence.
- GLPP+cordycepin novelty claim: **Negative-result Mechanistic Extrapolation** — absence of PubMed-indexed precedent does not establish novelty until CNKI/KISS multilingual scans clear the gap. Hold the "novel" tag pending 5b-1.
- Heterologous chassis yields (A. oryzae, Y. lipolytica, P. pastoris): cited from peer-reviewed papers; strain-specific reproducibility requires independent verification.

---

## Citations (PubMed attribution per MCP requirement)

All findings above derived from PubMed and Paperclip (PMC) full-text searches. Per the PubMed MCP attribution requirement, DOIs are linked inline at first mention. Full citation list:

1. Chang Y et al. *Foods* 2024. [10.3390/foods13050813](https://doi.org/10.3390/foods13050813) (PMID 38472926)
2. Zhang H et al. *Int J Med Mushrooms* 2020. [10.1615/IntJMedMushrooms.2020037153](https://doi.org/10.1615/IntJMedMushrooms.2020037153) (PMID 33463932)
3. Chien TY et al. *Int J Med Mushrooms* 2025. [10.1615/IntJMedMushrooms.2024057399](https://doi.org/10.1615/IntJMedMushrooms.2024057399) (PMID 39819523)
4. Song Z et al. *ACS Synth Biol* 2023. [10.1021/acssynbio.2c00570](https://doi.org/10.1021/acssynbio.2c00570) (PMID 36791366)
5. Zhao B et al. *Bioresour Technol* 2024. [10.1016/j.biortech.2024.131446](https://doi.org/10.1016/j.biortech.2024.131446) (PMID 39241814)
6. Jeennor S et al. *Microb Cell Fact* 2023. [10.1186/s12934-023-02261-5](https://doi.org/10.1186/s12934-023-02261-5) (PMID 38071331)
7. Cai X et al. *Bioprocess Biosyst Eng* 2021. [10.1007/s00449-021-02611-w](https://doi.org/10.1007/s00449-021-02611-w) (PMID 34268619)
8. Wu HC et al. *Int J Med Mushrooms* 2019. [10.1615/IntJMedMushrooms.2019031138](https://doi.org/10.1615/IntJMedMushrooms.2019031138) (PMID 31679300)
9. Duan XY et al. *J Agric Food Chem* 2025. [10.1021/acs.jafc.5c03654](https://doi.org/10.1021/acs.jafc.5c03654) (PMID 40367369)
10. Wang Y et al. *Front Microbiol* 2021. [10.3389/fmicb.2021.698436](https://doi.org/10.3389/fmicb.2021.698436) (PMID 34239513)
11. Liang ZC et al. *Int J Med Mushrooms* 2014. [10.1615/intjmedmushrooms.v16.i6.60](https://doi.org/10.1615/intjmedmushrooms.v16.i6.60) (PMID 25404221)
12. Luo QY et al. *J Asian Nat Prod Res* 2018. [10.1080/10286020.2018.1539080](https://doi.org/10.1080/10286020.2018.1539080) (PMID 30507305)
13. Tang J et al. *Prep Biochem Biotechnol* 2014. [10.1080/10826068.2013.833111](https://doi.org/10.1080/10826068.2013.833111) (PMID 24117155)
14. Wang L et al. *Bioengineering (Basel)* 2022. [10.3390/bioengineering9020069](https://doi.org/10.3390/bioengineering9020069) (PMID 35200422)
15. Lin LT et al. *J Food Drug Anal* 2017. [10.1016/j.jfda.2016.11.021](https://doi.org/10.1016/j.jfda.2016.11.021) (PMID 29389548)
16. Kang C et al. *ScientificWorldJournal* 2014. [10.1155/2014/510627](https://doi.org/10.1155/2014/510627) (PMID 25054182)
17. Kim CB et al. *Braz J Microbiol* 2025. [10.1007/s42770-025-01713-x](https://doi.org/10.1007/s42770-025-01713-x) (PMID 40549333)
18. Kunhorm P et al. *Appl Microbiol Biotechnol* 2019. [10.1007/s00253-019-09623-3](https://doi.org/10.1007/s00253-019-09623-3) (PMID 30648190)
19. Huo C et al. *Sheng Wu Gong Cheng Xue Bao* 2021. [10.13345/j.cjb.200738](https://doi.org/10.13345/j.cjb.200738) (PMID 34622640) — *Chinese-language*
20. Niu H et al. *Bioresour Technol* 2025. [10.1016/j.biortech.2025.133438](https://doi.org/10.1016/j.biortech.2025.133438) (PMID 41045993)
21. Park HJ. *Foods* 2025. [10.3390/foods14193408](https://doi.org/10.3390/foods14193408) (PMID 41097576) — review
22. Borde M, Singh SK. *Braz J Microbiol* 2023. [10.1007/s42770-023-01169-x](https://doi.org/10.1007/s42770-023-01169-x) (PMID 37930616)
23. Pi CC et al. *BMC Vet Res* 2024. [10.1186/s12917-024-04338-8](https://doi.org/10.1186/s12917-024-04338-8) (PMID 39604968)
24. Liu ML et al. *Int J Med Mushrooms* 2024. [10.1615/IntJMedMushrooms.2024054150](https://doi.org/10.1615/IntJMedMushrooms.2024054150) (PMID 38967211)
25. Zhao X et al. *J Ginseng Res* 2025. [10.1016/j.jgr.2025.09.001](https://doi.org/10.1016/j.jgr.2025.09.001) (PMID 41550597)
26. Wu FC et al. *Int J Med Mushrooms* 2013. [10.1615/intjmedmushr.v15.i4.70](https://doi.org/10.1615/intjmedmushr.v15.i4.70) (PMID 23796221)
27. Krishna KV et al. *Mol Biotechnol* 2024. [10.1007/s12033-024-01154-1](https://doi.org/10.1007/s12033-024-01154-1) (PMID 38658470) — review
28. Zhao X et al. *Microbiol Res* 2018. [10.1016/j.micres.2018.09.005](https://doi.org/10.1016/j.micres.2018.09.005) (PMID 30454654)
29. Xia Y et al. *Cell Chem Biol* 2017. [10.1016/j.chembiol.2017.09.001](https://doi.org/10.1016/j.chembiol.2017.09.001) (PMID 29056419) — **canonical PTN safeguard**
30. Shao J et al. *J Fungi (Basel)* 2026. [10.3390/jof12020118](https://doi.org/10.3390/jof12020118) (PMID 41745261)
31. Chen B et al. *Toxins (Basel)* 2020. [10.3390/toxins12060410](https://doi.org/10.3390/toxins12060410) (PMID 32575649) — review, mycotoxin safety
32. Karwowski BT. *Molecules* 2025. [10.3390/molecules30163377](https://doi.org/10.3390/molecules30163377) (PMID 40871530)
33. Zheng ZL et al. *Mycobiology* 2015. [10.5941/MYCO.2015.43.1.37](https://doi.org/10.5941/MYCO.2015.43.1.37) (PMID 25892913)
34. Ha SY et al. *Lett Appl Microbiol* 2021. [10.1111/lam.13598](https://doi.org/10.1111/lam.13598) (PMID 34758116)
35. Kim JR et al. *Pest Manag Sci* 2002. [10.1002/ps.508](https://doi.org/10.1002/ps.508) (PMID 12146173)
36. Oh J et al. *J Microbiol* 2018. [10.1007/s12275-019-8486-z](https://doi.org/10.1007/s12275-019-8486-z) (PMID 30594983)
37. Hur H. *Mycobiology* 2008. [10.4489/MYCO.2008.36.4.233](https://doi.org/10.4489/MYCO.2008.36.4.233) (PMID 23997632)
38. Oh J et al. *J Microbiol Biotechnol* 2019. [10.4014/jmb.1904.04004](https://doi.org/10.4014/jmb.1904.04004) (PMID 31336431)
39. Turk A et al. *Front Microbiol* 2022. [10.3389/fmicb.2022.1017576](https://doi.org/10.3389/fmicb.2022.1017576) (PMID 36338069)
40. Kang N et al. *Mycobiology* 2017. PMC5395498 — KSP8 mating-derived strain
41. Lee SK et al. *Biomolecules* 2019. [10.3390/biom9090461](https://doi.org/10.3390/biom9090461) — KYL05 mutant
42. Shrestha B et al. *Mycobiology* 2012. PMC3408298 — fruiting body progeny degeneration
43. Guo A et al. *J Fungi (Basel)* 2025. [10.3390/jof11040315](https://doi.org/10.3390/jof11040315) (PMID 40278135)
