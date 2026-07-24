# comp-020 — Per-Node Findings (Brief-Scrubbed Verification Re-Run)

**Independence statement:** This re-run was conducted without consulting comp-018 / comp-019 outputs. The compound list emerged organically from target-anchored literature mining via Paperclip MCP (PMC + bioRxiv full-text + abstracts), supplemented by targeted WebSearch for primary-literature claims (rosmarinic acid PubMed records, ChEMBL coverage spot-checks).

**Methodology:** for each upstream complement node, anchor queries → top results → grep verification of load-bearing IC50/CH50/AP50 values from primary-paper full text → flag assay format → record source language, evidence tier, and primary citation.

**Caveat:** The listed studies use different assay formats and conditions: CH50 (sheep erythrocyte, classical pathway), AP50 (rabbit erythrocyte, alternative pathway), Wieslab ELISA (terminal MAC deposition), C4-deposition assays (MASP-2 specific), and C3c ELISA (lectin-pathway specific). Their values are descriptive records, not interchangeable estimates of an operative gout-compartment potency. The current records do not isolate how much of each spread is caused by assay format, pathway context, serum dilution, material, laboratory, or another condition. See the cross-cutting heterogeneity log below.

---

## A. Initiation pathway — C1q (classical) / MBL-MASP (lectin) / AP tickover

### A.1 Direct C1q-cascade modulators (CP via C1q + downstream C2/C9)

| Compound | Class | CH50 (mM unless noted) | AP50 | Targets in cascade | Evidence tier | Source language | Primary citation |
|---|---|---|---|---|---|---|---|
| **(7S,8R)-Dihydrodehydrodiconiferyl alcohol** (Helicteres compound 5) | Plant lignan (benzofuran) | 0.009 ± 0.002 | 0.021 ± 0.003 | C1q, C2, C3, C9 | In vitro (sheep + rabbit erythrocyte hemolysis) | English (China-based authors) | Yin X, Lu Y, Cheng ZH, Chen DF. *Anti-Complementary Components of Helicteres angustifolia.* Molecules 21(11):1506 (2016). PMC6273495 L18 |
| **Machicendonal** (Helicteres compound 4) | Plant lignan (benzofuran) | 0.040 ± 0.009 | 0.105 ± 0.015 | C1q, C2, C3, C4, C5, C9 | In vitro (sheep + rabbit) | English (China-based) | Yin et al. 2016, PMC6273495 L18 |
| **Luteolin** | Plant flavone (3',4'-OH) | 0.19 ± 0.02 | 0.17 ± 0.04 | CP + AP (mechanism not target-mapped in this paper) | In vitro | English (China-based) | Zhang T, Chen DF. *Anticomplementary principles of a Chinese multiherb remedy for SARS.* J Ethnopharmacol 117(2):351-61 (2008). PMC7126446 L10 + Table 1 |
| **Quercitrin** | Plant flavonol glycoside | 0.53 ± 0.02 | 0.32 ± 0.04 | CP + AP | In vitro | English (China-based) | Zhang & Chen 2008, PMC7126446 |
| **Quercetin** | Plant flavonol | 0.50 ± 0.02 | 1.02 ± 0.03 | CP > AP | In vitro | English | Zhang & Chen 2008, PMC7126446 |
| **Rutin** | Plant flavonol glycoside | 0.58 ± 0.01 | 0.42 ± 0.04 | CP + AP | In vitro | English | Zhang & Chen 2008, PMC7126446 |
| **Hyperoside** | Plant flavonol glycoside | 1.72 ± 0.01 | 0.25 ± 0.02 | AP-selective | In vitro | English | Zhang & Chen 2008, PMC7126446 |
| **Apigenin** | Plant flavone | 3.40 ± 0.06 | 2.02 ± 0.21 | CP + AP, weak | In vitro | English | Zhang & Chen 2008, PMC7126446 |
| **Ginsenoside Rg3** | Plant triterpene saponin | not in matched-format paradigm | — | C1q reduction (mouse brain, depression model) | Animal model — chronic restraint depression mouse | English (China-based) | Yang D et al., PMC12594608 (2025) |

**Reference record:** Zhang & Chen 2008 reported heparin sodium salt in the same experimental paradigm. Molecular-weight conversion is not used here because heparin is heterogeneous and a mass-to-molar comparison would create false precision. The tabulated values remain material- and assay-specific observations, not a cross-compound rank.

### A.2 Lectin pathway — MASP-2 / MBL-MASP

| Compound | Class | IC50 | Assay | Target | Evidence tier | Source | Primary citation |
|---|---|---|---|---|---|---|---|
| **Heparin (unfractionated)** | Sulfated GAG (FDA-approved drug) | 2 μg/mL (LP) / 39 μg/mL (CP) / 76 μg/mL (AP) | WieLISA (LP/CP/AP) at 1:100 serum dilution | MASP-2 (LP) + C1q (CP) + AP serine proteases | In vitro | English (Netherlands group) | Talsma DT et al. *MASP-2 Is a Heparin-Binding Protease.* Front Immunol 11:732 (2020). PMC7212410 L45 |
| **Heparin tetrasaccharide** (4-mer) | Sulfated GAG fragment | 21 μg/mL (LP), no CP/AP inhibition at tested concentrations | WieLISA | MASP-2-selective | In vitro | English | Talsma 2020, PMC7212410 |
| **Heparin hexasaccharide** | Sulfated GAG fragment | 4 μg/mL (LP), LP-selective | WieLISA | MASP-2 | In vitro | English | Talsma 2020 |
| **Heparin octasaccharide** | Sulfated GAG fragment | 3 μg/mL (LP), LP-selective | WieLISA | MASP-2 | In vitro | English | Talsma 2020 |
| **Bupleurum smithii** crude polysaccharide (BPs) | Plant pectic polysaccharide | LP IC50 1.057 mg/mL (C3c ELISA), CH50 0.34 mg/mL, AP50 0.081 mg/mL | C3c ELISA + hemolysis | C1s, C3, C4 (per prior work cited in PMC4629277 L46) | In vitro | English (China-based) | Wu M, Li H, Zhang YY, Chen DF. *C3c-based ELISA for Bupleurum polysaccharides.* Acta Pharm Sin B (2015). PMC4629277 |
| **Bupleurum chinense** crude polysaccharide (BCPs) | Plant pectic polysaccharide | LP IC50 0.098 mg/mL, CH50 0.35 mg/mL, AP50 0.337 mg/mL | C3c ELISA + hemolysis | C1q, C2, C5, C9 (per PMC4629277 L46) | In vitro | English (China-based) | Wu et al. 2015, PMC4629277 |
| **Suramin** | Synthetic polysulfonated naphthylurea (FDA-approved trypanosomiasis drug) | LP IC50 not stated as μM but operates on LP per PMC4629277 | Hemolysis + C3c ELISA | CP and LP | Pre-clinical (FDA-approved for off-label complement use) | English | PMC4629277 — used as positive control |
| **TFPI1-derived peptide** (engineered MASP-2 inhibitor) | Protein engineering | High potency vs MASP-2 (Ki sub-nM range) | Direct enzymatic + ischemia-reperfusion model | MASP-2-selective | Animal model | English | Szakács D et al. JBC 2019, PMC6527154 |

The oligosaccharide and polysaccharide values describe different exact materials in the cited assays. They do not establish a class-wide or cross-material priority.

### A.3 Complement-fixation polysaccharides (immunomodulatory; effect direction context-dependent)

| Compound | Class | ICH50 (μg/mL) | Note | Citation |
|---|---|---|---|---|
| **Ligusticum chuanxiong LCP-I-I** | Pectic polysaccharide (HG + RG-I + AG-I/II) | 26.3 ± 2.2 | Comparable to BP-II positive control 25.5 | Zou YF et al. PMC6155779 (2017) |

These cause complement *fixation* (consumption of complement at tissue sites away from inflammatory targets) — interpretive caution: in a gout context, fixation away from MSU sites could reduce or amplify C5a generation depending on tissue distribution. Flagged for further mechanism work.

---

## B. Convertases — C3 convertase / C5 convertase

### B.1 C3 convertase

| Compound | Class | IC50 | Assay | Target | Evidence tier | Source | Primary citation |
|---|---|---|---|---|---|---|---|
| **Rosmarinic acid** | Plant phenolic acid (Lamiaceae/Boraginaceae) | **34 μM** (C3b covalent attachment to cells); 180 μM CP hemolysis; 160 μM AP hemolysis | Cell-based C3b deposition + classical/alternative hemolytic | Covalently modifies activated C3b → blocks C5 convertase formation; primarily C5 convertase | In vitro + 3 in vivo models | English | Sahu A et al. *Inhibition of complement by covalent attachment of rosmarinic acid to activated C3b.* Biochem Pharmacol 57(12):1439-46 (1999). PMID 10353266. Also Englberger W et al. Int J Immunopharmacol 10(7):729-37 (1988). PMID 3198307. Also Peake PW et al. Int J Immunopharmacol 13(7):853-7 (1991). PMID 1761351 |
| **C5 convertase regulation by rosmarinic acid** | — | **1500 μM** for C5 convertase direct inhibition | Cell-based | C5 convertase | In vitro | English | Sahu 1999, PMID 10353266 |
| **Compstatin family** (C3-binding peptide) | Engineered cyclic peptide derived from phage display, NOT a natural product but FDA-approved adjacent (pegcetacoplan = compstatin derivative) | sub-μM (peptide engineering) | Direct C3 binding | C3 (blocks both C3 and C5 convertase formation) | Clinical (pegcetacoplan = Empaveli FDA 2021) | English | Mohan RR et al. PMC5082644; Gorham RD et al. PMC4306506 |

### B.2 C5 convertase

The surveyed Sahu 1999 record directly names C5-convertase inhibition by rosmarinic acid. This search observation is not a universal absence claim about other natural compounds and does not establish operative potency.

---

## C. Soluble factors

### C.1 Factor B / Factor D (alternative pathway)

| Compound | Class | IC50 / Ki | Target | Evidence tier | Citation |
|---|---|---|---|---|---|
| **Iptacopan (LNP023)** | Synthetic small-molecule; approved for PNH/IgAN as Fabhalta | sub-nM Factor B Ki | Factor B | Clinical (FDA 2023) | Schubart A et al. PMC6475383 (2019); Tang Z et al. PMC11124358 (2024) |
| **Danicopan (ACH-4471)** | Synthetic Factor D inhibitor | sub-μM | Factor D | Clinical | Risitano AM et al. PMC8634185 (2020) |
| **MY008211A** | Synthetic small-molecule | clinical | Factor B/D class | Clinical | Ye L et al. medRxiv 2026 |
| **Vemircopan** | Synthetic Factor D inhibitor | sub-μM | Factor D | Phase trial | Schubart 2022 review PMC10092480 |

**Natural-product Factor B/D direct-inhibition class:** corpus surveyed surfaced **no** characterized natural-product factor B or factor D direct enzymatic inhibitor with in vivo evidence. The closest hits are sulfated polysaccharides (heparin, fucoidan, dextran sulfate) which broadly inhibit AP including factor B/D function via electrostatic competition with substrate, not via direct active-site binding.

### C.2 Factor H upregulation (positive-direction intervention)

This was scoped in the brief as "upregulating Factor H is positive intervention." Surveyed corpus surfaced:

| Compound | Mechanism | Effect | Evidence tier | Citation |
|---|---|---|---|---|
| **Factor H mini-construct (mHDM-FH)** | Engineered protein, NOT a natural product | Functional substitution | Animal model | Kamala O et al. PMC8696033 (2021) |
| **Thrombospondin-1 (TSP-1)** | Endogenous human protein; not a "compound" but acts synergistically with Factor H | Synergistic AP inhibition | Animal model + in vitro | Konwar S et al. bioRxiv 2024-07-31 |
| **Native Factor H protein supplementation** | Endogenous; engineering thread | Direct AP regulation | Clinical (autosomal disease compensation literature) | Kopp A et al. PMC4030870; Sándor N et al. PMC10894998 |

**Natural-product Factor H upregulator class:** the surveyed corpus did NOT surface a small-molecule or natural-product compound with documented Factor H expression-upregulation activity in matched assay format. Factor H promoter modulation is dominated by endogenous regulators (NF-κB, IFNγ-responsive elements) rather than dietary or natural-product compounds in the literature scanned. **Flagged as a coverage gap.**

### C.3 Factor I / Properdin / Clusterin

Corpus did NOT surface natural-product compounds with documented direct modulation of Factor I, properdin, or clusterin at IC50/Ki tier evidence.

**Properdin caution:** Properdin downregulation is NOT universally desirable. Low plasma properdin associates with increased CV mortality in carotid atherosclerosis (Louwe MC et al. PMC12074774, 2025). Compounds that broadly suppress AP convertase function via properdin destabilization may have adverse cardiovascular signal in long-term use. Flagged.

---

## D. Membrane regulators — DAF / CD55 / CD59 / CR1

The surveyed corpus did NOT surface natural-product or dietary compounds with characterized expression-upregulation activity on CD55, CD59, or CR1 with comparable IC50/EC50 metric. CD55-related natural-compound literature focuses on (1) cancer biology contexts where high CD55 is detrimental and downregulation is studied, (2) endogenous transcription factor regulation (KLF4, An FQ et al. PMC10884306), (3) viral exploitation of CD55 by enteroviruses. **Coverage gap; this is the engineering-thread (comp-012, H05) territory, not the natural-product thread.**

---

## E. C5 / C5aR1 axis (residual coverage)

Per brief: "Direct natural-product C5aR1 antagonist class confirmed empty by comp-014 + validation-experiments §1.21." This re-run did NOT re-execute the C5aR1 scan; confirmed by ruling out via comp-014 cross-reference per brief instructions. **Avacopan is the synthetic FDA-approved C5aR1 antagonist; not fermentable.**

The C5 axis ENGINEERING surface (anti-C5 antibodies eculizumab, ravulizumab; anti-C5a antibodies vilobelimab) is well-mapped in `wiki/complement-c5a-gout.md`; not re-done here.

---

## F. Marine compounds — sulfated polysaccharides

| Compound | Source | IC50 (CP, μg/mL) | Assay | Target | Evidence tier | Citation |
|---|---|---|---|---|---|---|
| **Sulfated galactofucan SJW-3** | *Saccharina japonica* (brown algae) | 3.11 | CP hemolysis | CP (broad) | In vitro | Jin W et al. PMC4728500 (2015) |
| **Crude fucoidan ANW** | *Ascophyllum nodosum* | 0.98 | CP hemolysis | CP | In vitro | Jin 2015 |
| **SJS** (acid-extracted *S. japonica*) | Brown algae | 4.51 | CP hemolysis | CP | In vitro | Jin 2015 |
| **HFW** | *Hizikia fusiforme* | 5.51 | CP hemolysis | CP | In vitro | Jin 2015 |
| **SJW** | *Saccharina japonica* | 7.26 | CP hemolysis | CP | In vitro | Jin 2015 |
| **HFS** | *Hizikia fusiforme* (acid-extract) | 24.65 | CP hemolysis | CP | In vitro | Jin 2015 |
| **Sea cucumber polysaccharide (SC)** | *Acaudina molpadioides* (marine invertebrate) | similar to ANW (~1 μg/mL range) | CP hemolysis | CP | In vitro | Jin 2015 |

These marine-polysaccharide values are descriptive records for the exact materials and assay reported by Jin 2015. They do not establish oral exposure, safety, material equivalence, or a priority order.

**Activator (negative finding):** **Floridoside** from *Mastocarpus stellatus* (red alga) is a potent CP **activator** — recruits IgM to drive CP. Inverse hit, included for completeness; not a CP0 candidate. (Courtois A et al. PMC2579733)

---

## G. Fungal metabolites

Per brief: "comp-014 catalogued ~6,800 fungal compounds with target activity. You can build on it for fungal sub-pass; don't redo the breadth scan."

The independent scan of "fungal complement inhibitor" / "Monascus complement" / "fumagillin complement" / "K76" surfaced no novel fungal natural product with documented direct complement-cascade IC50 in the matched paradigm. The Husakova & Patakova 2025 Monascus pigments review (PMC11877510) shows antioxidant/antimicrobial activity but not complement-cascade activity. Aspergillus-derived fumagillin targets MetAP2, not complement. Confirms comp-014's structural-gap finding for fungi at the C5aR1 node and extends it: no characterized fungal natural product directly inhibits any of the named upstream complement nodes in the surveyed corpus.

**Flagged as a coverage finding.** comp-014 verdict (zero direct fungal C5aR1 antagonists) is here independently extended: fungal natural products are systematically absent from upstream complement modulator literature with characterized IC50.

---

## H. Bacterial metabolites

Survey of bacterial-metabolite anticomplement activity surfaced:
- *E. coli* K5 polysaccharide (chemically O-sulfated) — non-natural-form, requires synthetic sulfation to gain activity
- *Klebsiella pneumoniae* over-cleaves C5 to evade MAC formation — pathogen-evasion biology, not therapeutic
- Gut commensal SCFA (butyrate/propionate) — well-characterized HDAC inhibitors per comp-007, but NOT documented direct upstream complement modulators

**Coverage gap on natural bacterial-metabolite direct upstream complement modulators.**

---

## I. Node-level source inventory

The tables above preserve records by complement node, material, assay, and primary source. They are an inventory, not a ranking surface. Factor B, Factor D, Factor H, CD55, CD59, and CR1 natural-product queries returned no directly characterized candidate in the searched corpus; that bounded search result is a coverage gap, not evidence that the class is universally empty.

---

## J. Assay-format heterogeneity log

For compounds with reported IC50 spanning >5× across the literature:

### Rosmarinic acid

| Assay | IC50 | Source |
|---|---|---|
| Cell-based C3b covalent attachment | 34 μM | Sahu 1999 |
| Classical pathway hemolysis (human serum) | 180 μM | Sahu 1999 |
| Alternative pathway hemolysis (human serum) | 160 μM | Sahu 1999 |
| Direct C5 convertase enzymatic | 1500 μM | Sahu 1999 |

**Descriptive range: 34 → 1500 μM = 44× across the listed assay records.** The covalent-C3b mechanism makes assay-step dependence plausible, but these records also differ in assay context and do not isolate format as the cause of the spread. No value is an operative gout-compartment potency. A matched-material, matched-condition replication across prespecified formats must determine whether the spread follows cascade step, laboratory context, or both.

### Heparin

| Assay | IC50 | Source |
|---|---|---|
| LP via WieLISA (1:100 serum dilution) | 2 μg/mL | Talsma 2020 |
| CP via WieLISA | 39 μg/mL | Talsma 2020 |
| AP via WieLISA (1:50 serum, 200 μg/mL ceiling) | 76 μg/mL | Talsma 2020 |
| C4 cleavage MASP-mediated | 102 μg/mL | Talsma 2020 |
| Sheep-erythrocyte CH50 (Zhang & Chen paradigm) | 38.5 μg/mL | Zhang & Chen 2008 |

**Descriptive range: 2 → 102 μg/mL = 50× across the listed records.** Talsma 2020 directly supports pathway-specific inhibition and MASP-2 binding/inhibition for the tested heparin materials. The records do not isolate how much of the numerical spread is caused by assay format, pathway context, serum dilution, material, laboratory, or another condition; none supplies an operative gout-compartment potency. A matched-material, matched-condition panel is required before attributing the spread or using it for experimental routing.

### Luteolin

Surveyed Zhang & Chen 2008 paper reports CH50 0.19 mM, AP50 0.17 mM. CNKI / WanFang searches (via WebSearch redirect) did not surface additional luteolin anti-complement IC50 in the matched paradigm, though luteolin is widely studied for other anti-inflammatory targets. Limited heterogeneity data in surveyed corpus — flagged as a Phase 2 follow-up: a focused CNKI / WanFang search in Chinese for 木犀草素 + 补体 (luteolin + complement) is the indicated next step.

---

## K. Multilingual coverage analysis

| Source language | Hits surfaced | Novel hits not in English | Notes |
|---|---|---|---|
| English (China-based authors, English-language journals: Mol Pharmacol, J Ethnopharmacol, Molecules, Int Immunopharmacol) | All structured CH50/AP50/IC50 data above | — | Most TCM-derived complement work IS published in English-language journals by Chinese groups (Daofeng Chen group at Fudan; Quanbin Zhang group at OUC). |
| Chinese (CNKI / WanFang direct query) | Targeted searches via WebSearch did not return primary-paper IC50 numbers in the time budget | UNKNOWN — could be additional luteolin/quercetin/Bupleurum work in Chinese-only journals | **Phase 2 follow-up:** dedicated CNKI/WanFang query for 补体抑制 + flavonoids/lignans/polysaccharides |
| Japanese (J-STAGE) | Sho-saiko-to (TJ-9) Kampo paper PMC2276037 surfaced with IL-12 modulation; not direct complement | Unclear — Kampo formulary likely contains anti-complement data | **Phase 2 follow-up:** dedicated J-STAGE query for 補体 + 漢方 + Kampo formulas |
| Other (Korean KISS, Russian eLIBRARY) | Not surveyed in time budget | — | Phase 2 follow-up |

**Honest finding:** the surveyed Western/English-language literature ALREADY contains substantial TCM-derived natural-product complement-modulator data — Daofeng Chen's group at Fudan publishes the canonical TCM anti-complement work in English (Mol Pharmacol, J Ethnopharmacol). The "Western-research bias" risk in this specific subfield is *partially* mitigated by the fact that the leading group publishes in English. However, the assumption is tested only at a coarse level — Kampo formulary work and CNKI-only Chinese-language work were NOT systematically scanned in this re-run's time budget. **Phase 2 follow-up flagged.**

---

## L. ChEMBL coverage gap analysis

Survey of compounds for ChEMBL anti-complement records:

| Compound | ChEMBL ID search via PubChem cross-ref | ChEMBL anticomplement assay coverage | Comments |
|---|---|---|---|
| Luteolin | CHEMBL156 | Multiple records; HMG-CoA, MAPK, sirtuin, but no direct C1q/C3/CH50 assay records | Gap |
| Quercetin | CHEMBL50 | Hundreds of records; multiple kinases and oxidoreductases; no direct complement-pathway IC50 records as primary endpoint | Gap |
| Rutin | CHEMBL222302 | Records present but no direct complement-cascade IC50 assays | Gap |
| Rosmarinic acid | CHEMBL165102 | Records present; no direct C3 convertase IC50 record despite published 1988/1991/1999 papers (PMID 3198307, 1761351, 10353266) | **Significant gap** — published in primary literature for 30+ years but absent from ChEMBL anticomplement curation |
| Helicteres lignans (machicendonal, dihydrodehydrodiconiferyl alcohol) | Not in ChEMBL | No records | Total absence |
| Bupleurum polysaccharides BPs/BCPs | Not in ChEMBL (polysaccharides are systematically absent from ChEMBL by design) | None | Structural gap |
| Marine fucoidans (SJW, SJS, HFW, ANW) | Not in ChEMBL | None | Structural gap |
| Heparin | Multiple ChEMBL records (clinical drug) | Anticoagulation primary; complement-inhibition secondary | Anticomplement records present but secondary annotation |
| Iptacopan | CHEMBL5314125 | Factor B records present | Covered |
| Danicopan | CHEMBL4794868 | Factor D records present | Covered |
| Compstatin | CHEMBL2105656 | C3 records present | Covered |

**ChEMBL coverage gap finding (matches comp-013 / comp-014 pattern):** ChEMBL anticomplement assay curation is structurally biased toward **synthetic small-molecule clinical-stage compounds** (iptacopan, danicopan, compstatin derivatives) and **absent for**:

1. Plant flavonoids/lignans with documented anti-complement IC50 in primary literature (rosmarinic acid is the canonical example — 30+ year primary-literature record, ChEMBL does not curate the C3-convertase IC50)
2. Polysaccharides as a structural class (Bupleurum, marine fucoidans, heparin oligosaccharides — systematically absent from ChEMBL by design, since polysaccharide structure ≠ small-molecule SMILES)
3. Natural-product hits from non-Western lit
4. Most pre-2000 publications

**Operational implication:** any computational triage on upstream-complement compounds that uses ChEMBL as the primary IC50 source will systematically miss the natural-product class. The ChEMBL coverage gap is even more severe here than for the gout-relevant transporter chokepoints (URAT1, ABCG2) per comp-013's TCM coverage observation.

n compounds surveyed in this re-run with documented anticomplement IC50: ~25
n with corresponding ChEMBL anticomplement-curated record: ~5 (synthetic clinical drugs only)
n absent from ChEMBL entirely as a chemical entity: ~10 (polysaccharides + lignans + several flavonoid glycosides)

Coverage rate: ~20%. Significantly below ChEMBL's coverage rate for kinases or GPCRs (typical >70% for clinical-stage compounds).

---

## M. Translation-disagreement summary

Only one source in this re-run was non-English (PMC7126446 — Zhang & Chen 2008, J Ethnopharmacol, English journal but China-based authors using TCM materia medica references). The IC50/CH50/AP50 numerical data are reported directly in the English text; no translation step required.

CNKI / WanFang queries did not return primary-paper full-text in the time budget for translation cross-check. **Translation-disagreement summary: not applicable to this re-run's data; deferred to Phase 2.**

If the Phase 2 CNKI/WanFang follow-up surfaces primary-language IC50 papers (e.g., 补体经典途径抑制 luteolin numerical data), the two-model cross-check protocol (Claude Anthropic + DeepSeek per CLAUDE.md §Translation protocol) applies.

---

## N. Discriminating follow-ups

This artifact does not choose a candidate. Candidate selection must come from an independently verified evidence home, exact-material availability, compartment plausibility, safety, and a prespecified decision.

Useful next observations include:

1. Independently replicate the Yin 2016 *Helicteres* result with matched compound identity, stocks, assay conditions, and controls before translational routing.
2. Test one qualified rosmarinic-acid material in an MSU-associated complement assay while measuring material recovery and C5a or C5b-9. This asks whether the cited C3b mechanism is active in the proposed system; it does not presume gut exposure.
3. Repeat one exact material across preregistered complement formats under harmonized conditions before attributing cross-paper numerical variation to assay format.
4. Run dedicated CNKI/WanFang and J-STAGE searches using compound, species, formula, and traditional-pathology frames; apply the two-model translation protocol to load-bearing non-English findings.

The re-run does not establish oral bioavailability, a gout-compartment concentration, engineering route, cross-class rank, or replacement for the independent CD55 engineering track.
