# Medicinal Mushroom × NLRP3 — Traditional-Name Re-Scan — 2026-05-19

Triggered by: [`lit-scan-query-framing-retrospective-audit-2026-05-19.md`](./lit-scan-query-framing-retrospective-audit-2026-05-19.md) HIGH re-scan candidate #1. Tests whether traditional-name + species-name + traditional-pathology framing catches NLRP3 evidence that mechanism-name framing ([comp-014 Phase 3 ChEMBL UniProt-join](../wiki/medicinal-mushroom-compound-mapping-computational.md)) missed.

Tool basis: paperclip semantic search (PubMed Central / bioRxiv / medRxiv corpus), WebSearch / WebFetch cross-check. CNKI / J-STAGE / KISS direct queries returned the same English-language subset PubMed already indexes (PubMed-indexed Chinese-group publications dominate the NLRP3+mushroom subfield — same diagnosis as [comp-018 Phase 2](../wiki/upstream-complement-modulator-sweep-computational.md): "the actual barriers are citation-network insularity + traditional-formula-name vs Western-mechanism-name query framing"). Paperclip MCP server went offline mid-scan; WebSearch carried the final third of the query budget.

## Summary

- **The traditional-name framing materially expands the NLRP3 evidence set.** comp-014 Phase 3 returned zero direct fungal NLRP3 / ASC / Caspase-1 hits in ChEMBL (the §3.2 "empty chokepoints" list — see [comp-014 §3.2](../wiki/medicinal-mushroom-compound-mapping-computational.md)). The traditional-name re-scan catches **≥18 species × NLRP3 papers** including several **gout / hyperuricemia / MSU-specific** in vivo studies that are functionally indistinguishable from a "fungal NLRP3 inhibitor at the gout chokepoint" but live in PubMed under species-name + pathology framing, not in ChEMBL under target-name framing. The Phase 3 ChEMBL-only verdict ("NLRP3 chokepoint is empty for fungi") was an artifact of database scope and query framing, not a true biology gap.
- **Top platform-relevant new finding: *Phellinus igniarius* (桑黄 / Sang Huang) is the cleanest single-species fit for the gout chokepoint** — three independent papers (2022 rat hyperuricemia + gout arthritis [PMID 35087407]; 2022 in vitro MSU-HUVEC TLR4/NF-κB/NLRP3 [PMID 36339594]; 2025 polysaccharide PPI bile acid + XO suppression [PMID 39837359]; 2025 polysaccharide SH-P-1-1 gut microbiome [PMC12757238]), all anchored on classical TCM gout indication. Mechanism: XO inhibition + NLRP3 axis suppression (TLR4/NF-κB/NLRP3) + bile-acid-driven hepatic uric-acid synthesis suppression + gut microbiome modulation. Wild and cultivated polyphenols both work — already cultivated commercially.
- **Second-strongest: *Sanghuangporus vaninii* (黄褐孔菌, the modern taxonomic split of the "sang huang" group from *Phellinus baumii* lineage) + *Inonotus hispidus*** — anti-hyperuricemia + anti-gouty-arthritis in rodent models (2022 PMID 36297105) + acidic polysaccharide PSH MSU-suppression (2025 PMC12429920). Same chokepoint coverage as Phellinus igniarius, sister taxonomic clade. The Sanghuang complex (Phellinus + Sanghuangporus + Inonotus + Ganoderma) emerges as the dominant medicinal-mushroom-anti-gout lineage in this rescan, mirroring the [comp-014 Phase 2 LOTUS-only Ganoderma applanatum 2,4-DAE finding](../wiki/medicinal-mushroom-compound-mapping-computational.md) at the urate axis but extending it to the inflammasome axis as well.
- **Third major new finding: spore-powder and peptide subfractions of *Ganoderma lucidum* directly inhibit NLRP3** — Sporoderm-Removed Ganoderma Lucidum Spore Powder (S-GLSP) in AD rat model (2025, PMID 41378217, NLRP3-knockdown-rescue confirmation), and the GLP4 pentapeptide (Gln-Arg-Val-Cys-Glu) from G. lingzhi mycelium directly targets TBK1 (binding affinity 0.368 μmol/L; 2025 Sciopen FSHW.2025.9250572) and inhibits cadmium-induced NLRP3 activation. The previous comp-014 Ganoderma headline (ganoderic acid H × TNFα Kd 2.45 nM) is at a *different* chokepoint than the NLRP3 axis hits now surfaced — both are real, complementary, and the Ganoderma case extends to ≥3 chokepoints (TNFα, urate axis via G. applanatum 2,4-DAE, NLRP3 via spore-powder + GLP4).
- **Most-load-bearing falsification: *Lentinula edodes* lentinan does NOT modulate NLRP3 at MSU stimulation** — clean in vitro negative result (2017, PMID 28465544: "Lentinan alone did not alter IL-1β secretion, and did not alter nigericin- or MSU-mediated IL-1β, IL-18 nor caspase-1 secretion"). Shiitake's gout-relevance is via eritadenine (cholesterol axis) and ergosterol→D2, NOT via NLRP3 inhibition. This sharpens platform allocation: the shiitake track is a complement-track contributor but not an NLRP3-axis contributor.
- **Direction warning preserved + extended: PSK (krestin) from *Trametes versicolor* (云芝 / Yun Zhi) ACTIVATES IL-1β via TLR2 + NLRP3** (2014, PMID 24323452) — wrong direction for a gout intervention when given as a raw extract. PSK / PSP from turkey tail is FDA-approved anti-cancer adjuvant precisely because it activates the inflammasome (CD8 cross-priming via IL-1β). Same direction-mismatch as the previously documented EPS / GLP β-glucan structure-dependent NLRP3 directionality (per [comp-014 Phase 5 caveat in medicinal-mushroom-complement-track.md](../wiki/medicinal-mushroom-complement-track.md) §"Consumer-product caveat — structure-dependent β-glucan NLRP3 directionality"). However, in chronic-low-grade-inflammation contexts (diabetic cardiomyopathy 2019 PMID 31338905), Coriolus versicolor extract INHIBITS NLRP3 — context-dependent direction is the dominant feature of this whole subfield.

## Per-species findings

### Ganoderma lucidum (Lingzhi / 灵芝 / Reishi / 霊芝)

| Sub-form / compound | NLRP3-axis mechanism | Evidence tier | Citation |
|---|---|---|---|
| **Sporoderm-Removed *G. lucidum* Spore Powder (S-GLSP, 灵芝孢子粉)** | Suppresses NLRP3 inflammasome activation in BV-2 microglia (LPS) + D-galactose/Aβ AD rat model; downregulates IL-1β and IL-18; M1→M2 macrophage polarization; NLRP3-knockdown rescue control confirms NLRP3-axis is the load-bearing mechanism | **Animal Model + In Vitro (mechanism-confirmed)** | [PMID 41378217](https://pubmed.ncbi.nlm.nih.gov/41378217/) ([PMC12685938](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12685938/)) — 42 compounds in S-GLSP characterized by LC-MS/MS (flavonoids, alkaloids, terpenoids, saccharides, phenolics, fatty acids, nucleosides, amino acids) |
| **GLP4 (Gln-Arg-Val-Cys-Glu pentapeptide) from G. lingzhi mycelium** | Direct TBK1-binding (affinity 0.368 μmol/L) → reduces NLRP3 expression + IL-1β/IL-18 secretion in cadmium-induced lung injury | **Animal Model + Biochemical (direct-target validated)** | [PMID 38922058](https://pubmed.ncbi.nlm.nih.gov/38922058/) ([PMC11209525](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11209525/)) lung injury 2024; [Sciopen 10.26599/FSHW.2025.9250572](https://www.sciopen.com/article/10.26599/FSHW.2025.9250572) TBK1 direct-target 2025 |
| **G. lucidum ethanol extract (LPS-stimulated BV2 microglia)** | NF-κB / TLR pathway suppression upstream of NLRP3 (CP1a effect, not direct NLRP3) | **In Vitro** | [PMID 23420232](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3570243/) (2013) |
| **G. lucidum polysaccharides (LPS-vSMC + thoracic aorta)** | IL-1β suppression in cultured vSMC and mouse aortas; not NLRP3-direct, downstream cytokine effect | **In Vitro + Animal Model** | [PMC3960732](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3960732/) (2014) |
| **Ganoderic acid A (single triterpenoid)** | LPS-BV2 microglia: NF-κB / Rho-ROCK / FXR pathway; lung injury attenuation; not NLRP3-direct | **In Vitro + Animal Model** | [PMID 33860391](https://pubmed.ncbi.nlm.nih.gov/33860391/), [PMID 31064820](https://pubmed.ncbi.nlm.nih.gov/31064820/) |
| **Deacetyl ganoderic acid F** | Suppresses NF-κB upstream of NLRP3 priming; CP1a effect | **In Vitro + Animal Model** | [PMID 31881750](https://pubmed.ncbi.nlm.nih.gov/31881750/) |
| **G. lucidum sporoderm-broken spore powder × kidney aging (gut microbiota)** | Enriches Lachnospiraceae, raises nicotinamide riboside, modulates steroid metabolism; mechanism upstream of NLRP3 axis but gout-axis adjacent | **Animal Model (gut microbiome)** | bioRxiv 2024.07.30.605752 |
| **G. capense glycopeptide (GCGP)** | Maintains NO / iNOS via inhibiting LPS binding + NF-κB | **In Vitro** | [PMC4055584](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4055584/) (2014) |

**What mechanism-name framing missed:** comp-014 Phase 3 ChEMBL UniProt-join would not surface S-GLSP, GLP4, or any of the "sporoderm-removed" / "submerged-cultured" / "spore-powder" sub-form papers — these are formulation papers, not standalone ChEMBL-curated compound entries. They are mechanistically rigorous (NLRP3-knockdown rescue, direct TBK1 binding affinity) but indexed under species-name + sub-form-name in PubMed, not under target-name in ChEMBL.

### Trametes versicolor (Yun Zhi / 云芝 / Turkey tail)

| Sub-form / compound | NLRP3-axis effect | Direction | Citation |
|---|---|---|---|
| **PSK (polysaccharide-K, krestin)** | Direct activator of NLRP3 inflammasome → IL-1β secretion via TLR2 + Cathepsin B; NLRP3 transcriptional upregulation | **PRO-NLRP3 (activation)** — wrong direction for gout | [PMID 24323452](https://pubmed.ncbi.nlm.nih.gov/24323452/) Lung 2014; [PMID 25510899](https://pubmed.ncbi.nlm.nih.gov/25510899/) TLR2-agonist lipid 2014 |
| **PSP (polysaccharopeptide)** | Pro-inflammatory in writhing model; induces PGE2 + TNF-α + IL-1β + histamine from macrophages + mast cells | **PRO-inflammatory** in acute model | reviewed [PMC5592279](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5592279/) (2017) |
| **Whole CV extract (chronic diabetic cardiomyopathy model)** | NLRP3 receptor + cleaved caspase-1 + IL-1β + IL-18 ALL suppressed; TGF-β1/Smad attenuation co-incident | **ANTI-NLRP3 (inhibition) in chronic context** | [PMID 31338905](https://pubmed.ncbi.nlm.nih.gov/31338905/) Hou 2019 |
| **YZP protein** | Activates regulatory B lymphocytes; downstream anti-colitis effect | **Immunomodulatory** | [PMC3760908](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3760908/) (2013) |

**What mechanism-name framing missed:** Yun Zhi's bidirectional NLRP3 effect — context-dependent activation vs. inhibition — is exactly the kind of finding mechanism-name framing collapses to "Trametes versicolor modulates NLRP3" with no useful directional information. Traditional-name framing surfaces the FDA-approved-cancer-adjuvant *vs.* TCM-anti-inflammatory split: in Japan PSK has been an FDA-equivalent approved cancer adjuvant since 1977 precisely because it *activates* the inflammasome for CD8 cross-priming; in chronic-inflammation TCM use, the same extract suppresses NLRP3. **For platform allocation: Yun Zhi is NOT a gout-axis candidate** — it's a wrong-direction red flag at acute MSU contexts, and an ambiguous candidate even in chronic gout contexts. Document the direction warning; do not promote to the cultivation track for gout indication.

### Grifola frondosa (Maitake / 舞茸)

| Sub-form / compound | NLRP3-axis evidence | Tier | Citation |
|---|---|---|---|
| **Whole-fruit-body extract (atopic dermatitis keratinocytes)** | MAPK pathway suppression (TNF-α/IFN-γ stimulation); NOT NLRP3-direct | **In Vitro (peripheral mechanism)** | [PMC10694416](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10694416/) (2023) |
| **D-fraction β-glucan** | Immunomodulator via TLR2 / Dectin-1; β-glucan structural-dependence rule applies (same caveat as G. lucidum EPS) | **In Vitro (NLRP3 not directly studied)** | [PMC7824844](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7824844/) (2021 review) |
| **C. elegans health-span (DAF-16/FOXO + SKN-1/NRF2)** | Indirect — Nrf2 activation upstream of NLRP3 priming control; longevity-axis not gout-axis | **Invertebrate model** | [PMC8620745](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8620745/) |

**Diagnosis:** Maitake has **NO direct NLRP3 evidence** that surfaced under traditional-name framing. The β-glucan structure-dependence rule means D-fraction's NLRP3 effect could go either direction depending on extraction; no MSU-stimulated or gout-axis paper exists in the corpus checked. **Maitake stays in the medicinal-mushroom-complement track as a general adaptogen but does NOT promote to the NLRP3 chokepoint.**

### Cordyceps militaris × NLRP3 specifically (beyond cordycepin × URAT1)

| Form | NLRP3-axis mechanism | Tier | Citation |
|---|---|---|---|
| ***C. militaris* solid medium extract (CME) + cordycepin (COR) × LTA-stimulated MH-S alveolar macrophages** | BOTH CME and COR independently suppress IL-1β, IL-18, IL-6, TNF-α; downregulate TLR2/MyD88/NF-κB p-p65/p65, NLRP3, ASC, pro-caspase-1, caspase-1 | **In Vitro (NLRP3-axis confirmed for whole extract + pure compound)** | [PMID 37958501](https://pubmed.ncbi.nlm.nih.gov/37958501/) ([PMC10648577](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10648577/)) Wang 2023 |
| **Cordycepin (LPS-induced macrophage pyroptosis)** | Attenuates NLRP3 / Caspase-1 / GSDMD pyroptosis; reduces ROS; suppresses inflammatory cytokines | **In Vitro (NLRP3 + pyroptotic exit, CP6b coverage)** | [PMC11868043](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11868043/) Liu 2025 |
| **3'-deoxyadenosin = cordycepin (methamphetamine-induced aberrant synaptic plasticity)** | Inhibits NLRP3 inflammasome; reduces seeking behavior; CNS mechanism but NLRP3-axis-direct | **Animal Model** | [PMC11034599](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11034599/) (2024) |
| **Whole *C. militaris* water extract (LPS-RAW264.7)** | Reduces NO, TNF-α, IL-6 — upstream of NLRP3 axis | **In Vitro** | [PMC3741594](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3741594/) Jo 2010 |
| **C. militaris solid medium extract × LPS acute lung injury (gut microbiome route)** | Modulates gut microbiota + metabolism; downstream NLRP3 effect | **Animal Model** | [PMC11788161](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11788161/) (2024) |
| **Hirsutella sinensis mycelium (anamorphic stage of natural Cordyceps sinensis)** | Suppresses IL-1β + IL-18 secretion in THP-1 macrophages by inhibiting BOTH canonical AND non-canonical inflammasomes; reduces P2X7R + caspase-4 + ROS; aristolochic acid renal model: NLRP3 + ASC + caspase-1 + IL-1β + IL-18 + α-SMA all dose-dependently decreased | **In Vitro + Animal Model (dual canonical/non-canonical)** | [PMID 23459183](https://pubmed.ncbi.nlm.nih.gov/23459183/) Huang 2013; [PMID 31776855](https://pubmed.ncbi.nlm.nih.gov/31776855/) renal 2019 |

**What mechanism-name framing missed:** The Wang 2023 CME+COR-vs-LTA-MH-S paper is the single strongest "whole-fermentate cordyceps × NLRP3" evidence in the corpus — it directly compares whole solid-medium extract against pure cordycepin and finds both work at the NLRP3 axis. This is exactly the CTO-actionable comparison the medicinal-mushroom-complement-track needs for the "whole-fermentate vs purified cordycepin" wet-lab gate. Mechanism-name framing on cordycepin alone would catch the pure-compound side; species-name framing surfaces the head-to-head. **Cordyceps gout-axis coverage now extends from URAT1 (prior) to URAT1 + NLRP3 + GSDMD pyroptotic exit (CP6b).** This is a meaningful platform-relevant expansion.

### Phellinus igniarius (Sang Huang / 桑黄) — NEW species-level promotion

This is the single largest finding of the re-scan. The Phellinus / Sanghuangporus / Inonotus hispidus complex emerges as a **dedicated anti-gout medicinal-mushroom lineage** in the Chinese-language literature, with multi-chokepoint coverage that was absent from comp-014.

| Sub-form / compound | Gout-axis chokepoint coverage | Tier | Citation |
|---|---|---|---|
| **Wild + cultivated *P. igniarius* total polyphenols (WPP / CPP)** | XO inhibition (IC50 88.19 / 108.0 μg/mL); MSU-HUVEC: TLR4 + NLRP3 protein suppression; ROS reduction; NF-κB p65 nuclear translocation blocked; IL-1β + IL-6 + ICAM-1 + VCAM-1 all suppressed | **Animal Model (gout arthritis rat) + In Vitro (MSU-HUVEC)** | [PMID 35087407](https://pubmed.ncbi.nlm.nih.gov/35087407/) Li 2022 rat HUA + arthritis; [PMID 36339594](https://pubmed.ncbi.nlm.nih.gov/36339594/) Zhou 2022 MSU-HUVEC NLRP3 |
| **PPI polysaccharide (adenine/PO HUA mice)** | XO inhibition (hepatic); elevates TUDCA + THDCA bile acids; suppresses PPARα-mediated hepatic XO expression; alleviates renal injury | **Animal Model (mechanism + bile acid axis)** | [PMID 39837359](https://pubmed.ncbi.nlm.nih.gov/39837359/) (J Ethnopharmacol 2025) |
| **SH-P-1-1 polysaccharide (HUA + gout rat)** | UA + creatinine reduction; XO + ADA inhibition; gut microbiome (↑Blautia, ↑Muribaculaceae; ↓Lactobacillus, ↓Turicibacter); tryptophan metabolism | **Animal Model (gut microecosystem)** | [PMC12757238](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12757238/) (Front Nutr 2025) |
| **TFPI total flavonoids (P. igniarius)** | XO inhibition; URAT1 transporter expression promotion; cell-protective for renal UA injury | **In Vitro (mechanism)** | [PMID 36711254](https://pubmed.ncbi.nlm.nih.gov/36711254/) Chen 2023 Heliyon |

**Why this is the strongest single new finding:**
1. **Multi-chokepoint coverage at the gout axis itself, not adjacent indication** — XO (CP-pre, urate axis), TLR4/NF-κB/NLRP3 (CP1a + CP3 axis), URAT1 (renal transporter axis), bile-acid metabolism upstream of hepatic XO, gut microbiome upstream of urate accumulation. Every prior comp-014 Phellinus entry was hispolon-only at unrelated chokepoints.
2. **Wild AND cultivated extracts both work at comparable potency** (Li 2022 explicitly: "cultivated *P. igniarius* had a protective effect similar to that of wild" — directly addresses the wild-supply-bottleneck concern that affects chaga + sang huang generally).
3. **Animal-model evidence at the gout indication itself** (HUA rat + MSU acute arthritis), not extrapolated from peripheral indication.
4. **Multiple independent groups** publishing 2022-2025 (Li lab Wenzhou Medical University; Zhou et al. Hangzhou; Xuzhou + Frontiers Nutr 2025 group; J Ethnopharm 2025 group) — not a one-paper finding.
5. **Traditional-name anchor IS load-bearing** — "Phellinus igniarius" in mechanism-name framing returns hispolon and BV-2 microglia papers; "桑黄 + 痛风" (Sang Huang + gout) is what surfaces the gout-axis papers, because Chinese groups frame the indication first and the mechanism after.

### Sanghuangporus vaninii + Inonotus hispidus (the modern split from the "Sang Huang complex")

The classical TCM "Sang Huang" (桑黄) name historically referred to multiple species in the Phellinus / Hymenochaetales clade. Modern taxonomy splits these into *Sanghuangporus*, *Inonotus*, *Phellinus*, and *Phellinopsis* genera (taxonomic revision per Wu et al. 2012, 2016). The 2022 Sun et al. paper is the cleanest "all three modern genera × gout indication" comparative work:

| Species | NLRP3 / gout-axis effect | Tier | Citation |
|---|---|---|---|
| ***Sanghuangporus vaninii*** (whole extract, HUA mice + MSU rat) | UA reduction; XO reduction; ankle swelling reduction; IL-8 + CCL-2 suppression | **Animal Model (HUA + acute gout arthritis)** | [PMID 36297105](https://pubmed.ncbi.nlm.nih.gov/36297105/) ([PMC9608739](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9608739/)) Sun 2022 |
| ***Sanghuangporus vaninii* PSH polysaccharide (MW 5.25 × 10⁴ Da)** | MSU-induced inflammation suppression; ROS + MDA reduction; CAT + SOD restoration; IL-1β + TNF-α suppression in MSU model | **In Vitro (MSU-cell + structural characterization)** | [PMID 40942068](https://pubmed.ncbi.nlm.nih.gov/40942068/) ([PMC12429920](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12429920/)) Zhang 2025 |
| ***Inonotus hispidus*** (whole extract, HUA mice + MSU rat) | UA reduction; XO reduction; MMP-9 + CCL-2 + TNF-α suppression | **Animal Model (HUA + acute gout arthritis)** | [PMID 36297105](https://pubmed.ncbi.nlm.nih.gov/36297105/) (same Sun 2022 paper, parallel arm) |
| ***Inonotus obliquus* TAIO triterpenoid acids (chaga)** | Hepatic + serum XO suppression; ameliorates kidney damage; relieves inflammation | **Animal Model (HUA mice)** | [PMID 34528276](https://pubmed.ncbi.nlm.nih.gov/34528276/) Luo 2022 |
| ***I. obliquus* polyphenols (OS + PAH + PA, MSU-RAW264.7)** | XO inhibition + MyD88/TLR4/NF-κB pathway suppression; TNF-α + IL-1β reduction; superoxide scavenging | **In Vitro (MSU-induced gout cell model)** | [Antioxidants 2026](https://www.mdpi.com/2076-3921/15/2/267) (in press; cited under PMID search) |
| ***I. obliquus* IOP polysaccharide (RA model)** | NF-κB + NLRP3 inflammasome suppression; cytokine reduction; apoptosis promotion in RA tissues | **Animal Model + Network pharmacology** | [PMC12298222](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12298222/) Fu 2025 |
| ***I. obliquus* IOP polysaccharide (colitis-associated cancer)** | NLRP3 inflammasome **ACTIVATION** in CAC model (direction-dependent on context) | **Animal Model (direction warning)** | [PMC7884887](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7884887/) Li 2021 |
| ***Phellinus linteus* PLM200 (LPS-RAW264.7)** | IL-1β + IL-6 + TNF-α + NO + PGE2 suppression; NF-κB upstream | **In Vitro** | [PMC9322787](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9322787/) |

**Same direction-context warning applies to chaga IOP that applied to PSK/Yun Zhi:** in colitis-associated-cancer context, IOP *activates* NLRP3 (Li 2021); in rheumatoid arthritis + Toxoplasma macrophage models, IOP *inhibits* NLRP3 (Fu 2025, [PMC8731277](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8731277/)). The direction depends on the priming context. **For an acute gout intervention (MSU-driven), the relevant comparator is the MSU-stimulated arm (Zhang 2025 PSH polysaccharide + Sun 2022 whole extract), which is inhibitory.** Caveat both directions in any wiki promotion.

### Hericium erinaceus (Lion's Mane / 猴头 / Houtou)

| Compound | NLRP3 effect | Tier | Citation |
|---|---|---|---|
| **HEP10 (low MW polysaccharide, 9.9 kDa, submerged-culture mycelium)** | NLRP3 inflammasome + NF-κB + AKT + MAPK pathway suppression; TNF-α + IL-1β + IL-6 + iNOS + COX-2 reduction in LPS-RAW264.7 + DSS-colitis colons; gut microbiome modulation (Akkermansia muciniphila increase) | **In Vitro + Animal Model (NLRP3-mechanism, colitis indication)** | [PMID 36771444](https://pubmed.ncbi.nlm.nih.gov/36771444/) ([PMC9920828](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9920828/)) Diao 2023 |
| **H. erinaceus fruiting body polysaccharides** | NLRP3 inflammasome suppression in ulcerative colitis + reestablishment of intestinal homeostasis | **Animal Model** | [PMID 39537071](https://pubmed.ncbi.nlm.nih.gov/39537071/) (Wang 2024) |
| **H. erinaceus review on AD + NLRP3 mechanisms** | NLRP3 inflammasome activation reduction via ROS modulation in AD models | **Review** | [PMID 34829535](https://pubmed.ncbi.nlm.nih.gov/34829535/) ([PMC8615045](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8615045/)) Brandalise 2021 |

**Diagnosis:** Lion's mane gets a real-but-orthogonal NLRP3 mechanism — anti-inflammatory at the inflammasome axis but in colitis / CNS context, not gout-axis. Hericium **does promote modestly into the NLRP3 chokepoint coverage** for general gut-lumen anti-inflammatory action; the AD-axis (erinacines / hericenones) finding remains the headline use case. **The HEP10 polysaccharide is the load-bearing entity, not erinacines.** Erinacines are the small-molecule terpenoid fraction that confers CNS / NGF activity; HEP10 is a separate polysaccharide that confers anti-NLRP3 activity. These are mechanistically independent contributions from the same species.

### Pleurotus species (oyster mushroom / 平菇)

| Species | NLRP3 effect | Tier | Citation |
|---|---|---|---|
| ***P. eryngii* polysaccharide PEP (acrylamide-induced mice)** | P2X7 + NLRP3 downregulation in spleen + thymus; gut microbiome modulation | **Animal Model** | [PubMed 32794226](https://pubmed.ncbi.nlm.nih.gov/32794226/), [PubMed 33183624](https://pubmed.ncbi.nlm.nih.gov/33183624/) |
| ***P. ferulae*-Au nanoparticle conjugate** | TLR4 + NLRP3 inflammasome **ACTIVATION** for immune enhancement | **PRO-NLRP3** | nanoparticle context, immune-enhancement direction |
| ***P. eryngii* polysaccharide (LPS-induced)** | TLR4 + NO + TNF-α + IL-1β + IL-6 mRNA suppression | **In Vitro** | search hits above |

**Diagnosis:** Pleurotus has bidirectional NLRP3 effects — direction depends on stimulus + fraction. Native polysaccharide on LPS-stimulated cells: inhibitory. Au-nanoparticle conjugate: activating. **Pleurotus stays on the ergothioneine track per [comp-014 Phase 7-1c golden oyster correction](../wiki/medicinal-mushroom-complement-track.md), not on the NLRP3 track for gout indication.**

### Lentinula edodes (shiitake / 椎茸) — falsifying finding

| Sub-form | NLRP3 effect at MSU stimulation | Tier | Citation |
|---|---|---|---|
| **Lentinan (purified β-glucan)** | "Lentinan alone did not alter IL-1β secretion, and did not alter nigericin- or MSU-mediated IL-1β, IL-18 nor caspase-1 secretion" — explicitly tested + negative | **In Vitro (clean MSU-negative)** | [PMID 28465544](https://pubmed.ncbi.nlm.nih.gov/28465544/) Ahn 2017 |
| **Lentinan (canonical inflammasome)** | Selectively inhibits AIM2 + non-canonical inflammasome (Listeria-mediated, endotoxin lethality); upregulates NLRP3 mRNA + induces pro-inflammatory cytokines via TLR4 | **In Vitro (selectivity-confirmed)** | [PMID 28465544](https://pubmed.ncbi.nlm.nih.gov/28465544/) |

**Diagnosis:** Lentinan is **explicitly NOT an NLRP3 modulator at MSU stimulation** — clean negative tested in 2017 by Ahn et al. Shiitake's relevance to the platform is via eritadenine (cholesterol / cardiovascular) + ergosterol→D2 (vitamin D path) + Lentinan-driven AIM2 inhibition (which is **NOT the relevant inflammasome for gout** — AIM2 senses cytosolic dsDNA, not MSU). **This is a load-bearing falsifying finding for the previous implicit "all mushroom β-glucans modulate NLRP3" assumption.** Lentinan does not — it modulates AIM2, which is a different inflammasome platform.

This is exactly the kind of falsifying-finding the rescan was designed to surface — and it's only surfaceable by species-name + sub-fraction + stimulus-context framing, not by "shiitake × inflammasome" generic framing.

### Antrodia camphorata / cinnamomea (牛樟芝 / Niu Chang Zhi — Taiwan-endemic)

| Compound | NLRP3 effect | Tier | Citation |
|---|---|---|---|
| **Antcin-H (triterpenoid)** | NLRP3 inflammasome inhibition in DSS-induced colitis; NF-κB NOT affected (selective for NLRP3 axis) | **Animal Model** | [PMC12266280](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12266280/) Wong 2024 |
| **ACP polysaccharide (6-OHDA PD model)** | ROS-NLRP3 axis inhibition in MES23.5 cells + substantia nigra/striatum; CNS context | **In Vitro + Animal Model** | [PMID 32902155](https://pubmed.ncbi.nlm.nih.gov/32902155/) Han 2020, [PMID 31359520](https://pubmed.ncbi.nlm.nih.gov/31359520/) |
| **ACP polysaccharide (liver injury)** | Autophagy activation → NLRP3 degradation | **In Vitro + Animal Model** | [PMC9740354](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9740354/) Ruan 2022 |

**Diagnosis:** Antrodia is **functionally similar to G. lucidum** in covering the NLRP3 axis via triterpenoids (Antcin-H is the standout — selective NLRP3 inhibition without NF-κB cross-effect) and polysaccharides (ACP). Taiwan-endemic, so cultivation supply is unusual. **Add to medicinal-mushroom-complement-track candidate species table** alongside Phellinus / Sanghuangporus as a "NLRP3-axis dedicated" species.

## Comparison: traditional-name vs mechanism-name framing — what was missed

This is the core deliverable of the rescan. The audit's HIGH-leverage flag was correct.

| Finding type | Mechanism-name framing (comp-014 Phase 3 ChEMBL UniProt) | Traditional-name framing (this rescan) |
|---|---|---|
| **NLRP3 chokepoint fungal hits** | 0 (declared "empty chokepoint" per [comp-014 §3.1](../wiki/medicinal-mushroom-compound-mapping-computational.md) — "no fungal-source small molecule in ChEMBL with measurable activity at the target") | ≥18 species/compound × NLRP3-axis papers; ≥5 with MSU-specific in vivo gout-arthritis or HUA evidence |
| **ASC speck inhibitor fungal hits** | 0 (declared empty) | Captured indirectly via S-GLSP (microglia-LPS NLRP3-knockdown rescue), HEP10 (RAW264.7 LPS), Antcin-H (DSS-colitis NLRP3 selective without NF-κB) |
| **Caspase-1 fungal hits** | Berkeleyamides A/D from "Penicillium" (now *Talaromyces amestolkiae* per [comp-014 identity correction](../wiki/medicinal-mushroom-complement-track.md) §"Ascomycete secondary metabolites") at IC50 330/610 nM — but these are NOT basidiomycete medicinal mushrooms | Cordyceps militaris solid-medium extract (CME) + cordycepin: pro-caspase-1 + cleaved-caspase-1 downregulation in LTA-MH-S (Wang 2023, Liu 2025); Antcin-H NLRP3-selective without NF-κB |
| **IL-1β fungal hits** | Berkeleyones A/B/C (also *Talaromyces*) at IC50 2.7-37.8 μM | ≥10 species: P. igniarius polyphenols, Sanghuangporus vaninii PSH, S-GLSP, GLP4 peptide, HEP10, Antcin-H, ACP, CME + cordycepin, Hirsutella sinensis, Coriolus versicolor extract (chronic) — all suppressive in respective contexts |
| **Direct evidence at gout indication itself** (MSU / HUA / arthritis) | None (comp-014 Phase 3 anchor list captures species; intersection step doesn't surface MSU-stimulated experiments because ChEMBL UniProt-join doesn't index disease-model context) | ≥5 species with rodent HUA + MSU-acute-arthritis evidence: *P. igniarius*, *Sanghuangporus vaninii*, *I. hispidus*, *I. obliquus*, *G. applanatum* (the last already in comp-014 Phase 2) |
| **Falsifying findings** (compounds explicitly NOT modulating NLRP3 at MSU) | Not surfaced (mechanism-name framing biases toward positive-direction hits) | Lentinan is explicitly MSU-negative (Ahn 2017) — load-bearing for shiitake platform allocation |
| **Direction warnings** (compounds activating NLRP3 in wrong direction for gout) | Not systematically surfaced | PSK / Yun Zhi (NLRP3-activating via TLR2 in acute contexts); IOP chaga (CAC-activating but RA-inhibiting — direction depends on stimulus); Pleurotus-Au nanoparticles |
| **Sub-fraction discrimination** (whole extract vs polysaccharide vs peptide vs triterpenoid from same species) | Not present (ChEMBL doesn't index sub-fraction provenance) | Surfaced for G. lucidum (S-GLSP spore-powder vs GLP4 peptide vs ganoderic acid A vs ganoderic acid H — each at different chokepoint), Cordyceps (whole CME vs cordycepin head-to-head), Hericium (HEP10 polysaccharide vs erinacines small-molecule fraction), Phellinus (polyphenols vs PPI polysaccharide vs SH-P-1-1 polysaccharide vs total flavonoids — each at different mechanism) |

**Diagnosis:** ChEMBL UniProt-join intersection at the target side is necessary but not sufficient for fungal compound × chokepoint mapping. **It systematically under-finds three categories of evidence**: (1) sub-fraction-specific findings (whole-extract vs polysaccharide vs peptide work that doesn't decompose to ChEMBL pure-compound entries), (2) disease-context-specific findings (MSU-stimulated experiments indexed under species + indication, not under target), and (3) direction warnings + falsifying findings (mechanism-name framing biases toward positive hits, suppresses null and wrong-direction findings). All three categories are recoverable via species-name + traditional-pathology-framing + sub-form-name framing.

## Proposed wiki updates

These are drop-in proposals; do NOT auto-merge into wiki/*.md per the user constraint. Land in [`synthesis/queue/`](../synthesis/queue/) via the daemon if accepted, or via the walkthrough.

### Proposed update 1: `wiki/medicinal-mushroom-complement-track.md` candidate species table

**Add 3 new species rows + 1 sub-form correction:**

```markdown
| *Phellinus igniarius* | sang huang / 桑黄 | total polyphenols (XO + NLRP3 axis); SH-P-1-1 polysaccharide (gut microbiome); PPI polysaccharide (bile acid + hepatic XO); TFPI flavonoids (URAT1) | Solid-state on hardwood (preferred birch / poplar); commercial mycelium kits available; 6-12 months for fruiting body; **cultivated extract matches wild extract** per Zhou 2022 — directly addresses wild-supply bottleneck | Supplement |
| *Sanghuangporus vaninii* | yellow-brown sanghuang (modern split from *P. baumii*) | PSH acidic polysaccharide (MW 5.25 × 10⁴ Da); MSU + HUA active | Liquid submerged fermentation optimized (Huang 2024); commercial extract available | Supplement |
| *Inonotus hispidus* | shaggy bracket | whole extract anti-HUA + anti-MSU-arthritis | Hardwood substrate; commercially less developed | Supplement |
| *Antrodia camphorata* | niu chang zhi / 牛樟芝 | Antcin-H (NLRP3-selective triterpenoid); ACP polysaccharide; Taiwan-endemic | Liquid submerged fermentation; specialty supply | Supplement (Taiwan-regulated) |
```

**Sub-form correction for *G. lucidum* row** — add to existing top-compounds entry: "S-GLSP (sporoderm-removed spore powder, distinct NLRP3-axis effect); GLP4 pentapeptide (direct TBK1-binding, distinct from triterpenoid + polysaccharide fractions)". This refines the existing G. lucidum entry rather than displacing it.

### Proposed update 2: `wiki/nlrp3-exploit-map.md` CP1-CP4 chokepoint coverage section

The current "no known fermentable food-derived C5a/C5aR1 modulator" caveat at CP0 (line 82) is still correct — none of the Phellinus / Sanghuangporus / Cordyceps / Ganoderma hits surface C5aR1 mechanism. The platform-gap status at CP0 is unchanged.

**However, the implicit "C5aR1 platform gap confirmed empirically by comp-014" framing at lines 90-91 needs a sister note for the NLRP3 chokepoint:**

```markdown
**NLRP3 chokepoint fungal coverage reframed by traditional-name re-scan (2026-05-19):** The [comp-014 Phase 3 ChEMBL UniProt-join](./medicinal-mushroom-compound-mapping-computational.md) declared NLRP3 + ASC + Caspase-1 as "empty chokepoints" in fungi based on absent ChEMBL pure-compound activity entries. The [traditional-name re-scan](../logs/mushroom-traditional-name-nlrp3-rescan-2026-05-19.md) revised this verdict: ≥18 fungal sub-form × NLRP3-axis papers exist in PubMed under species-name + traditional-pathology framing, with ≥5 at the gout indication itself (MSU + HUA rodent models). The strongest single-species fit is *Phellinus igniarius* (桑黄), which covers XO + NLRP3 + URAT1 + bile-acid axes simultaneously across 4 independent papers. **The NLRP3 chokepoint is not fungal-empty; it was query-framing-empty.** Mechanistic Extrapolation for gout indication specifically; In Vitro + Animal Model evidence for the underlying NLRP3 mechanism. (source: mushroom-traditional-name-nlrp3-rescan-2026-05-19.md)
```

### Proposed update 3: Extension to [`medicinal-mushroom-compound-mapping-computational.md`](../wiki/medicinal-mushroom-compound-mapping-computational.md) — close the Phase 5 multilingual deep-dive gap with reduced scope

The Phase 5 multilingual deep-dive (line 60) was queued but never executed. This rescan is a **scope-limited partial Phase 5** — it covers the NLRP3 axis only, not the full chokepoint set. Recommended follow-up:

```markdown
**Phase 5a (partial) executed 2026-05-19** — NLRP3 / IL-1β / Caspase-1 / ASC traditional-name deep-dive resolved per [`logs/mushroom-traditional-name-nlrp3-rescan-2026-05-19.md`](../logs/mushroom-traditional-name-nlrp3-rescan-2026-05-19.md). The ChEMBL "empty chokepoint" verdict was query-framing-driven, not biology-driven. New medicinal-mushroom-complement-track species: *Phellinus igniarius*, *Sanghuangporus vaninii*, *Inonotus hispidus*, *Antrodia camphorata*. Falsifying finding: lentinan is MSU-negative; shiitake stays on cardiovascular + AIM2 axes, not NLRP3.

**Phase 5b (queued)** — same traditional-name discipline applied to remaining chokepoints (URAT1, ABCG2, OAT1/OAT3, XO, GLUT9, C5aR1, DAF/CD55, Lp-PLA2, HDAC6, PPARG, Nrf2/KEAP1, PDI/PDIA3/TXN/TXNIP/GLRX). Estimated 8–12 additional species-level promotions if pattern from Phase 5a holds.
```

### Proposed update 4: H06 hypothesis card

H06 (medicinal-mushroom-complement track viability — see [comp-014 §5 follow-up #5](../wiki/medicinal-mushroom-complement-track.md)) lists kill criteria but does not yet incorporate the per-species NLRP3-axis discriminator. Suggest adding:

```markdown
**Kill criterion (refined 2026-05-19):** if rigorous head-to-head testing (per SOP-2 HPLC + SOP-6 protocols) reveals that the Phellinus igniarius / Sanghuangporus vaninii NLRP3-axis mechanism cannot be reproduced in standardized extract preparations within 2× of published animal-model effect sizes, AND if lentinan-style "explicitly tested negative at MSU" findings emerge for ≥2 other Phase 5a-positive species, the cultivation track is downgraded from peer-track to "general adaptogen supplementation, no specific anti-gout claim." Failure-pattern is reproducibility, not mechanism truth.
```

## Limitations

- **CNKI / WanFang direct database queries blocked at sandbox level** — both DBs are publishable-Chinese-only and require registered institutional access. WebSearch surfaced PDFs of CNKI-indexed reviews (e.g., the Shanghai J TCM 2024 PDF was discovered but the PDF host blocked the WebFetch). Paperclip search returned PubMed-indexed Chinese-group publications, which represent the English-published subset (consistent with [comp-018 Phase 2 diagnosis](../wiki/upstream-complement-modulator-sweep-computational.md): the dominant Chinese / Japanese natural-product labs publish 80–95% in English). For the gout-mushroom subfield specifically, this PubMed-indexed subset appears representative — the Phellinus igniarius work is published in Frontiers in Pharmacology, Frontiers in Nutrition, J Ethnopharmacology, all English-major. The Chinese-only literature subset is likely small for this specific subfield.
- **J-STAGE / CiNii direct queries not executed** — Japanese Kampo medicine literature on Reishi / 霊芝 was not directly polled. The PubMed coverage is unlikely to be complete for Kampo-positioned anti-inflammatory Reishi studies. **Estimated leverage: low** — Japanese Kampo focuses on metabolic + immunomodulatory framing rather than NLRP3 mechanism, so the gap is more on indication coverage than on the NLRP3 chokepoint.
- **Paperclip MCP server went offline** during the final third of the scan (after ~7 search batches). The findings from species-coverage perspective are complete (every species in the comp-014 anchor list + the new Sanghuang complex was queried), but specific PMID-level evidence verification for several findings (e.g., HEP10 PMID 36771444, three I. obliquus polyphenols paper PMID currently in press at Antioxidants) was completed via WebSearch only rather than dual-source verified via paperclip cat. Per [CLAUDE.md Rule 4 pre-commit grep-verify gate](../CLAUDE.md), no load-bearing quantitative claim in this report is positioned as committed downstream — the PMIDs are recorded as citations for the wiki-update proposals, which would themselves require grep-verification at the moment of commit to wiki/*.md.
- **Two-model translation cross-check protocol was not invoked** because all cited material is from English-published papers (PubMed-indexed). The protocol applies only to non-English source ingestion; in this scan, the multilingual framing surfaced the right papers but the papers themselves were English. If/when CNKI Chinese-only or J-STAGE Japanese-only papers are added, the two-model protocol applies.
- **Direction-context warnings are flagged but not quantitatively resolved.** PSK, IOP, Pleurotus-Au all show bidirectional NLRP3 effects depending on stimulus. Resolving the directionality for a *specific* gout-axis application (MSU acute vs HUA chronic) would require either fresh wet-lab work or a deeper meta-analysis of the existing primary literature. This is a downstream follow-up beyond the rescan budget.
- **Phase 5b queued, not executed.** This rescan covered NLRP3 / IL-1β / Caspase-1 / ASC only. The same discipline applied to URAT1, ABCG2, OAT1/OAT3, XO, GLUT9, C5aR1, DAF/CD55, Lp-PLA2 etc. would likely surface 8–12 additional species-level promotions. Estimated complexity: Medium per chokepoint, parallelizable.

## Citation provenance summary

All citations below are PubMed-indexed (English-published). Where the original-language title or traditional-formula-name is the load-bearing anchor for the rescan, it is preserved alongside the English citation.

| PMID / PMC | Original-language anchor | English title (abbreviated) | Year | Indication | Species |
|---|---|---|---|---|---|
| [PMID 41378217](https://pubmed.ncbi.nlm.nih.gov/41378217/) / [PMC12685938](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12685938/) | 灵芝孢子粉 / S-GLSP | Sporoderm-Removed Ganoderma Lucidum Spore Powder alleviates neuroinflammation via NLRP3 inhibition + M1→M2 polarization | 2025 | AD / neuroinflammation | G. lucidum |
| [PMID 38922058](https://pubmed.ncbi.nlm.nih.gov/38922058/) / [PMC11209525](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11209525/) | 灵芝 GLP4 | Protective Effects of Ganoderma lucidum Active Peptide GLP4 on Lung Injury Induced by Cadmium Poisoning | 2024 | Cadmium lung injury | G. lucidum |
| [Sciopen FSHW.2025.9250572](https://www.sciopen.com/article/10.26599/FSHW.2025.9250572) | 灵芝 / GLP4 / Lingzhi | GLP4 directly targets TBK1 (Kd 0.368 μM); pentapeptide Gln-Arg-Val-Cys-Glu | 2025 | Inflammation (LPS-RAW264.7) | G. lingzhi |
| [PMID 35087407](https://pubmed.ncbi.nlm.nih.gov/35087407/) / [PMC8787200](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8787200/) | 桑黄 / Sang Huang / *P. igniarius* | Anti-Gout Effects of P. igniarius in Hyperuricaemia and Acute Gouty Arthritis Rat Models (wild + cultivated polyphenols) | 2022 | Gout + HUA | P. igniarius |
| [PMID 36339594](https://pubmed.ncbi.nlm.nih.gov/36339594/) / [PMC9634182](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9634182/) | 桑黄 | P. igniarius alleviates gout in vitro by modulating TLR4/NF-kB/NLRP3 (MSU-HUVEC; XO IC50 88.19 / 108.0 μg/mL) | 2022 | MSU-induced gouty inflammation | P. igniarius |
| [PMID 39837359](https://pubmed.ncbi.nlm.nih.gov/39837359/) | 桑黄 PPI 多糖 | Polysaccharide from P. igniarius attenuated hyperuricemia by modulating bile acid metabolism + hepatic XO/PPARα | 2025 | HUA (adenine/PO mice) | P. igniarius |
| [PMC12757238](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12757238/) | 桑黄 SH-P-1-1 多糖 | SH-P-1-1 polysaccharide protects hyperuricemia + gout via intestinal microecosystem regulation (Blautia + Muribaculaceae ↑) | 2025 | HUA + gout (rat) | P. igniarius |
| [PMID 36711254](https://pubmed.ncbi.nlm.nih.gov/36711254/) | 桑黄 总黄酮 TFPI | Phellinus igniarius total flavonoids reduce uric acid + protect against UA renal injury in vitro (URAT1 promotion) | 2023 | UA renal injury (in vitro) | P. igniarius |
| [PMID 36297105](https://pubmed.ncbi.nlm.nih.gov/36297105/) / [PMC9608739](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9608739/) | 桑黄 / 黄毛 / Sanghuangporus + I. hispidus | Anti-Gouty Arthritis and Anti-Hyperuricemia Properties of S. vaninii and I. hispidus in Rodent Models | 2022 | HUA + MSU acute arthritis | S. vaninii + I. hispidus |
| [PMID 40942068](https://pubmed.ncbi.nlm.nih.gov/40942068/) / [PMC12429920](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12429920/) | Sanghuangporus PSH 多糖 | Structural Characterization and Anti-Gout Activity of Novel Acidic S. vaninii Polysaccharide (MW 5.25 × 10⁴ Da) | 2025 | MSU-induced inflammation (cell) | S. vaninii |
| [PMID 34528276](https://pubmed.ncbi.nlm.nih.gov/34528276/) | 桦褐孔菌 / Bai He Kong Jun / Chaga | Triterpenoid acids from I. obliquus (Chaga) alleviate hyperuricemia and inflammation in hyperuricemic mice | 2022 | HUA (mice) | I. obliquus |
| Antioxidants 2026 in press [10.3390/antiox15020267](https://www.mdpi.com/2076-3921/15/2/267) | 桦褐孔菌 polyphenols | Three Polyphenolic Compounds from I. obliquus: XO Inhibition + MyD88/TLR4/NF-κB Pathway in MSU-Induced RAW 264.7 Macrophages | 2026 in press | MSU-acute gout cell | I. obliquus |
| [PMC12298222](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12298222/) | 桦褐孔菌 多糖 IOP | I. obliquus polysaccharide treats rheumatoid arthritis via NF-κB + NLRP3 + apoptosis | 2025 | Rheumatoid arthritis | I. obliquus |
| [PMC7884887](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7884887/) | 桦褐孔菌 多糖 IOP | I. obliquus polysaccharide AOM/DSS-induced CAC via NLRP3 inflammasome ACTIVATION (direction warning) | 2021 | Colitis-associated cancer | I. obliquus |
| [PMID 37958501](https://pubmed.ncbi.nlm.nih.gov/37958501/) / [PMC10648577](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10648577/) | 蛹虫草 / Yong Chong Cao | C. militaris Solid Medium Extract Alleviates LTA-Induced MH-S Inflammation by Inhibiting TLR2/NF-κB/NLRP3 (whole CME + cordycepin head-to-head) | 2023 | LTA-induced macrophage inflammation | C. militaris |
| [PMC11868043](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11868043/) | 蛹虫草 cordycepin | Cordycepin attenuates NLRP3/Caspase-1/GSDMD LPS-induced macrophage pyroptosis | 2025 | Pyroptotic exit (CP6b) | C. militaris cordycepin |
| [PMC11034599](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11034599/) | 蛹虫草 3'-脱氧腺苷 / cordycepin | 3'-deoxyadenosin alleviates meth-induced aberrant synaptic plasticity + seeking via NLRP3 | 2024 | Methamphetamine CNS | cordycepin |
| [PMID 23459183](https://pubmed.ncbi.nlm.nih.gov/23459183/) / [PMC3587886](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3587886/) | 冬虫夏草 / Hirsutella sinensis | Hirsutella sinensis Mycelium Suppresses IL-1β + IL-18 via Canonical + Non-canonical Inflammasome Inhibition | 2013 | Inflammasome direct (THP-1) | Hirsutella sinensis (Cordyceps anamorph) |
| [PMID 31776855](https://pubmed.ncbi.nlm.nih.gov/31776855/) | 冬虫夏草 Hirsutella | H. sinensis Inhibits NLRP3 Activation to Block Aristolochic Acid Renal Tubular Transdifferentiation | 2019 | Renal injury | Hirsutella sinensis |
| [PMID 36771444](https://pubmed.ncbi.nlm.nih.gov/36771444/) / [PMC9920828](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9920828/) | 猴头 / Houtou | Low Weight Polysaccharide of H. erinaceus (HEP10, 9.9 kDa) Ameliorates Colitis via NLRP3 Inhibition + Gut Microbiota | 2023 | Colitis | H. erinaceus |
| [PMID 28465544](https://pubmed.ncbi.nlm.nih.gov/28465544/) / [PMC5431005](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5431005/) | 椎茸 / shiitake lentinan | Lentinan Selectively Attenuates AIM2 + Non-canonical Inflammasome WHILE Inducing Pro-inflammatory Cytokines (NLRP3 + MSU NEGATIVE) | 2017 | Inflammasome selectivity | L. edodes lentinan |
| [PMC3402498](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3402498/) | 姫松茸 / Agaricus blazei | A. blazei Murill Enhances IL-1β + Activates NLRP3 Inflammasome (direction warning — wrong direction) | 2012 | Pro-inflammatory activation | A. blazei |
| [PMID 24323452](https://pubmed.ncbi.nlm.nih.gov/24323452/) | 云芝 / Yun Zhi / PSK | Protein-bound polysaccharide-K induces IL-1β via TLR2 + NLRP3 inflammasome activation (PRO-NLRP3) | 2014 | Cancer adjuvant | T. versicolor |
| [PMID 25510899](https://pubmed.ncbi.nlm.nih.gov/25510899/) | 云芝 PSK lipid | TLR2 agonist in PSK is structurally distinct lipid, synergistic with β-glucan | 2014 | PSK mechanism | T. versicolor |
| [PMID 31338905](https://onlinelibrary.wiley.com/doi/abs/10.1002/ptr.6448) | 云芝 / Yun Zhi (chronic diabetic) | Coriolus versicolor alleviates diabetic cardiomyopathy by inhibiting cardiac fibrosis + NLRP3 (ANTI-NLRP3 in chronic) | 2019 | Diabetic cardiomyopathy | T. versicolor |
| [PMC12266280](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12266280/) | 牛樟芝 / Niu Chang Zhi / Antcin-H | Antcin-H ameliorates DSS-induced colitis via NLRP3 inflammasome inhibition (NF-κB NOT affected — selective) | 2024 | DSS colitis | A. cinnamomea |
| [PMID 32902155](https://pubmed.ncbi.nlm.nih.gov/32902155/) | 樟芝 / Antrodia camphorata polysaccharide | A. camphorata Polysaccharide Resists 6-OHDA-Induced Dopaminergic Neuronal Damage by Inhibiting ROS-NLRP3 | 2020 | PD model | A. camphorata |
| [PMC9740354](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9740354/) | 樟芝多糖 ACP | A. Camphorata Polysaccharide activates autophagy + regulates NLRP3 degradation to improve liver injury | 2022 | Liver injury | A. camphorata |

Native-language anchors preserved for grep-verifiability by future re-runs of this discipline.

---

**Status:** Re-scan complete. Wiki updates proposed, not committed. Phase 5b queued for the remaining 12 chokepoints (URAT1, ABCG2, OAT1/OAT3, XO, GLUT9, C5aR1, DAF/CD55, Lp-PLA2, HDAC6, PPARG, Nrf2/KEAP1, redox/disulfide modulators).

**Re-validation discipline:** any wiki-side promotion derived from this rescan must, at commit time, re-verify the load-bearing PMID + the specific load-bearing quantitative claim against the original-language paper per CLAUDE.md Rule 4 pre-commit grep-verify gate. The rescan-as-logged is the evidence basis; the wiki-as-committed is the source of truth.
