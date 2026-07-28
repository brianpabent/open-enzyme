# comp-020 — Per-Node Findings (Brief-Scrubbed Verification Re-Run)

**Independence defect:** Direct comp-018 / comp-019 output files were not
consulted, but the brief supplied named comparators, prior exclusions, and an
empty-class conclusion. This artifact is not an independent confirmation.

> **Artifact-wide quarantine boundary:** Every table, number, absence note,
> coverage label, and interpretation below is retained only as a historical
> source lead. None is current authority for a threshold-qualified hit,
> potency rank, target attribution, cross-assay comparison, coverage rate,
> systematic or exhaustive absence, gout-compartment activity, dietary
> efficacy, CFH independence, genotype response, or platform priority. Reuse
> requires fresh primary-source verification at the exact material, assay,
> unit, and evidence tier.

**Historical methodology:** for each upstream complement node, anchor queries
were followed by result inspection and partial grep verification. The run did
not retain a complete primary-source receipt for every value.

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
| **TFPI1-derived peptide** (engineered MASP-2 inhibitor) | Protein engineering | High potency vs MASP-2 (Ki sub-nM range) | Direct enzymatic + ischemia-reperfusion model | MASP-2-selective | Animal model | English | Szakács D et al. JBC 2019, PMC6527154 |

The oligosaccharide and polysaccharide values describe different exact materials in the cited assays. They do not establish a class-wide or cross-material priority.

### A.3 Complement-fixation polysaccharides (immunomodulatory; effect direction context-dependent)

| Compound | Class | ICH50 (μg/mL) | Note | Citation |
|---|---|---|---|---|
| **Ligusticum chuanxiong LCP-I-I** | Pectic polysaccharide (HG + RG-I + AG-I/II) | 26.3 ± 2.2 | Comparable to BP-II positive control 25.5 | Zou YF et al. PMC6155779 (2017) |

This fixation record does not establish the direction or compartment of a gout
effect. Treat it only as an assay lead until an exact-material MSU/complement
experiment measures C5a and downstream injury directly.

---

## B. Convertases — C3 convertase / C5 convertase

### B.1 C3 convertase

| Compound | Class | IC50 | Assay | Target | Evidence tier | Source | Primary citation |
|---|---|---|---|---|---|---|---|
| **Rosmarinic-acid records** | Plant phenolic acid (Lamiaceae/Boraginaceae) | Values withheld pending primary-full-text verification | Search snippets named C3b-deposition, hemolysis, and C5-convertase records | Exact target attribution unresolved here | Historical source lead | English | Sahu 1999 PMID 10353266; Englberger 1988 PMID 3198307; Peake 1991 PMID 1761351 |
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

The historical Factor B/D queries and nearby sulfated-polysaccharide records
are retained as search leads only. They do not establish a natural-product
empty class, direct active-site mechanism, or current database state.

### C.2 Factor H upregulation (positive-direction intervention)

This was scoped in the brief as "upregulating Factor H is positive intervention." Surveyed corpus surfaced:

| Compound | Mechanism | Effect | Evidence tier | Citation |
|---|---|---|---|---|
| **Factor H mini-construct (mHDM-FH)** | Engineered protein, NOT a natural product | Functional substitution | Animal model | Kamala O et al. PMC8696033 (2021) |
| **Thrombospondin-1 (TSP-1)** | Endogenous human protein; not a "compound" but acts synergistically with Factor H | Synergistic AP inhibition | Animal model + in vitro | Konwar S et al. bioRxiv 2024-07-31 |
| **Native Factor H protein supplementation** | Endogenous; engineering thread | Direct AP regulation | Clinical (autosomal disease compensation literature) | Kopp A et al. PMC4030870; Sándor N et al. PMC10894998 |

**Historical search boundary:** The retained queries neither pin a complete source
snapshot nor support a current non-retrieval or class-absence claim for
small-molecule or natural-product Factor H upregulators. The named endogenous
regulators above may seed a new source-pinned search; they do not establish that
other modulator classes are absent.

### C.3 Factor I / Properdin / Clusterin

The historical Factor I, properdin, and clusterin queries are recorded only as
seeds for a fresh source-pinned search. They do not support a current
non-retrieval or class-absence claim.

**Properdin safety conjecture:** A historical record associated low plasma
properdin with cardiovascular mortality in a different disease context (Louwe
et al., PMC12074774). It does not establish that a properdin-directed
intervention causes cardiovascular harm. Verify the primary cohort and test
mechanism-specific safety before treating this as a constraint.

---

## D. Membrane regulators — DAF / CD55 / CD59 / CR1

The historical CD55, CD59, and CR1 queries retained examples from cancer
biology, endogenous transcriptional regulation, and viral receptor biology.
Because the run retained no complete source snapshot, those queries do not
support a current non-retrieval or coverage-gap conclusion. Re-execute a
source-pinned search before using them to choose between expression and
engineering approaches.

---

## E. C5 / C5aR1 axis (residual coverage)

> **QUARANTINED — DO NOT CITE:** The brief supplied an empty-class conclusion
> from comp-014 and a named avacopan comparator. This run did not re-execute
> that search, so it supplies no C5aR1 class-absence or independent-confirmation
> result.

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

These marine-polysaccharide values are descriptive records for the exact materials and assay reported by Jin 2015. They do not establish oral exposure, safety, material equivalence, or a priority order.

**Activator (negative finding):** **Floridoside** from *Mastocarpus stellatus* (red alga) is a potent CP **activator** — recruits IgM to drive CP. Inverse hit, included for completeness; not a CP0 candidate. (Courtois A et al. PMC2579733)

---

## G. Fungal metabolites

The brief supplied a prior fungal-catalog conclusion and instructed the run not
to repeat the breadth scan. That contamination prevents an independent
replication claim.

The historical queries `"fungal complement inhibitor"`, `"Monascus complement"`, `"fumagillin complement"`, and `"K76"` did not yield a new fungal direct-complement record in this scan. The search was incomplete and lacks an immutable result snapshot, so it supports no current systematic-absence or exhaustive-class conclusion.

> **QUARANTINED — DO NOT CITE:** ~~comp-014 verdict (zero direct fungal C5aR1 antagonists) is here independently extended: fungal natural products are systematically absent from upstream complement modulator literature with characterized IC50.~~ The scan did not justify this claim.

---

## H. Bacterial metabolites

Historical bacterial-metabolite search notes:
- *E. coli* K5 polysaccharide (chemically O-sulfated) — non-natural-form, requires synthetic sulfation to gain activity
- *Klebsiella pneumoniae* over-cleaves C5 to evade MAC formation — pathogen-evasion biology, not therapeutic
- Gut commensal SCFA (butyrate/propionate) — well-characterized HDAC inhibitors per comp-007, but NOT documented direct upstream complement modulators

These notes do not establish a coverage gap or class absence.

---

## I. Node-level source inventory

The tables above preserve historical records by complement node, material,
assay, and cited source. They are not a ranking surface. The recorded queries
for Factor B, Factor D, Factor H, CD55, CD59, and CR1 lack immutable result
snapshots and therefore supply no current non-retrieval or coverage-gap claim.

---

## J. Assay-format heterogeneity log

The historical run attempted cross-record comparisons, but the records differ
in material, assay, pathway, and verification status. The derived range
multipliers are retired.

### Rosmarinic acid and heparin

The former 44× rosmarinic-acid and 50× heparin summaries combined
non-interchangeable records and, for some values, incomplete verification.
Neither multiplier is current evidence. A new analysis must first verify exact
materials and values from primary full text, then prespecify a matched panel
before interpreting any difference.

### Luteolin

Surveyed Zhang & Chen 2008 paper reports CH50 0.19 mM and AP50
0.17 mM. The retained CNKI/WanFang redirect attempts are not a source-pinned
database census and support no non-retrieval claim. A fresh direct search in
Chinese for 木犀草素 + 补体 (luteolin + complement), with exact queries and
results preserved in a compact receipt, is the indicated next step.

---

## K. Historical multilingual search-method note — quarantined

The historical rerun attempted English-language surfaces and limited Chinese
and Japanese discovery queries; Korean and Russian surfaces were not
systematically searched. The retained artifacts do not bind an exhaustive
query set, reproducible result census, or complete source-verification record.
They therefore support no language-coverage rate, regional-literature
comparison, bias-mitigation finding, or non-retrieval claim. A future
multilingual scan must preserve exact queries, surfaces attempted, counts,
failures, translations, and primary-source verification in a compact
literature-search receipt.

---

## L. ChEMBL identifier notes — quarantined

> **Quarantine boundary:** This historical spot-check retained neither a reproducible query census nor an immutable ChEMBL snapshot. It may seed a fresh database query, but it cannot support a coverage rate, systematic-absence claim, structural-bias verdict, or comparison with another target class.

Historical identifier notes: luteolin `CHEMBL156`, quercetin `CHEMBL50`, rutin
`CHEMBL222302`, rosmarinic acid `CHEMBL165102`, iptacopan `CHEMBL5314125`,
danicopan `CHEMBL4794868`, and compstatin `CHEMBL2105656`. These identifiers
must be rechecked before use. The retained artifact makes no statement about
which assays or materials ChEMBL currently contains.

> **QUARANTINED — DO NOT CITE:** ~~Coverage rate: ~20%. Significantly below ChEMBL's coverage rate for kinases or GPCRs (typical >70% for clinical-stage compounds).~~ Neither rate was established by a source-pinned census.

---

## M. Translation-disagreement summary

No non-English primary full text was used. Zhang and Chen 2008 (PMC7126446) is an English-language article despite China-based authorship and traditional-medicine references. No translation cross-check was triggered.

Chinese, Japanese, Korean, Russian, and other relevant regional searches were incomplete, so this artifact supports no multilingual-coverage or bias-mitigation inference. **Translation-disagreement summary: not applicable to this re-run's retained data; multilingual retrieval remained incomplete.**

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
