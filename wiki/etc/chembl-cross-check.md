---
title: "ChEMBL Cross-Check: Stack Compounds vs Curated Bioactivity"
date: 2026-07-01
tags: ["ChEMBL", "rigor", "bioactivity", "cross-check", "NLRP3", "off-targets", "polypharmacology"]
related:
  - ../nlrp3-inhibitor-screen.md
  - ../nlrp3-exploit-map.md
  - ../nlrp3-inflammasome.md
  - ../supplements-stack.md
  - ../bhb-ketones.md
  - ../kpv-peptide.md
  - ../cannabinoids-terpenes.md
  - ../synthesis/README.md
sources:
  - "EMBL-EBI ChEMBL v34 (queried via Anthropic life-sciences MCP, 2026-04-24)"
  - "EMBL-EBI ChEMBL v37 (queried via REST API, 2026-07-01 quarterly refresh)"
  - "Eur J Med Chem 2018: Resveratrol DPP-4 inhibition"
  - "Eur J Med Chem 2024: Berberine TDO inhibition"
  - "J Nat Prod 2020: Curcumin human NLRP3 IC50"
  - "J Med Chem 2007: EGCG Plasmodium ENR"
  - "J Med Chem 1991: Quercetin 5-LOX"
  - "J Med Chem 2023: Ursolic acid ROR-gamma IC50"
  - "J Med Chem 2023: Curcumin DYRK2 IC50"
---

# ChEMBL Cross-Check: Stack Compounds vs Curated Bioactivity

## Purpose

This is a **standing rigor page** that cross-references every NLRP3/gout-relevant compound discussed in the Open Enzyme wiki against the EMBL-EBI ChEMBL curated bioactivity database. The goal: separate "direct inhibitor of target X" claims (supported by a curated binding/inhibition IC50 in a named assay) from "pathway modulator" claims (functional downstream readouts, mechanism inferred from review literature).

**TCM lineage note:** Several compounds in this cross-check table have explicit TCM materia medica lineage — berberine (*Coptis chinensis* / Huang Lian 黄连), EGCG (green tea / Lu Cha 绿茶), resveratrol (*Polygonum cuspidatum* / Hu Zhang 虎杖), curcumin (turmeric / Jiang Huang 姜黄), oridonin (*Rabdosia rubescens* / Dong Ling Cao 冬凌草). The ChEMBL cross-check discipline is one of the six rules in the TCM × modern rigor methodology lens formalized at [`tcm-modern-rigor-intersection.md`](../tcm-modern-rigor-intersection.md) — rule #2 specifically. The cross-check results here (e.g., berberine's most potent curated activity is TDO at 30 nM, not NLRP3; resveratrol's molecular top target is DPP-4 at 0.6 nM, not SIRT1) are exactly the kind of "ChEMBL surprise" that the TCM rigor methodology is designed to surface. (source: tcm-modern-rigor-intersection.md)

Quercetin's 5-LOX finding — surfaced during the 2026-04-23 sweep of [nlrp3-inhibitor-screen.md](../nlrp3-inhibitor-screen.md) — is the template: a compound the wiki frames primarily as an NLRP3 pathway inhibitor actually has its single most potent curated activity on a different enzyme (5-LOX, IC50 300 nM), and that target is relevant to gout biology (leukotriene B4 drives neutrophil chemotaxis in MSU flares). Whenever a similar gap shows up, it goes here first, then propagates to the primary concept page on a follow-up sweep.

**NLRP3 target ID (reference):** CHEMBL1741208 (*NACHT, LRR and PYD domains-containing protein 3*, Homo sapiens, UniProt Q96P20).

**ChEMBL version:** v37 (release date 2026-05-01; 24,527,044 activities; 2,921,148 compounds; 18,552 targets). Original baseline used v34 (queried 2026-04-24).

**Refresh cadence:** Quarterly, or whenever a new direct NLRP3 inhibitor clinical program publishes pivotal data. Next refresh target: 2026-10-01.

**How to refresh:** See the three-line recipe in the [Appendix](#appendix-refresh-recipe) at the bottom of this page.

---

## ChEMBL scope & blind spots — which tool for which question

**ChEMBL answers exactly one kind of question well: "is compound X an inhibitor / binder of target Y?"** — because its schema is curated *inhibition / binding bioactivity* (IC50, Ki, Kd, EC50, pChEMBL). It is the right tool for the direct-inhibitor-vs-pathway-modulator separation this page exists to enforce. It is the **wrong** tool for several adjacent questions, and reaching for it out of familiarity is a recurring error (comp-047 used it for a *substrate* question; see below). Before a comp seeds a compound list or a disqualifier axis from ChEMBL, check the question against this table:

| The question you're actually asking | Right source | Why not ChEMBL |
|---|---|---|
| Is X an **inhibitor / binder** of target Y? (IC50/Ki/Kd) | **ChEMBL** | — (this is its job) |
| Is X a **substrate** of transporter/enzyme Y? | A directly inspected per-drug source: primary paper, FDA label, UCSF-FDA TransPortal, PharmGKB, or DrugBank transporter annotation with its cited evidence | ChEMBL activity coverage can miss transport relationships; a generic UniProt `DR DrugBank` cross-reference also does not encode relationship subtype |
| Does UniProt expose a DrugBank relationship between X and Y? | UniProt flat-file `DR DrugBank` cross-references (`rest.uniprot.org/uniprotkb/<acc>.txt`) | The cross-reference supports a conservative relationship flag only; do not relabel it as substrate or inhibitor evidence |
| Canonical physiological substrates + transport kinetics of a transporter/enzyme | **UniProt** function/`CC` annotations (KM, Vmax, named substrates) | ChEMBL has assay-level activity, not the curated physiological substrate list |
| What reaction / pathway is X or Y in? | **Reactome** (repo tool `tools/reactome/reactome_analysis.py`), KEGG | ChEMBL has no pathway/reaction model — it is *not* a substrate catalog either; treat Reactome as pathway infrastructure, not per-compound substrate/inhibitor evidence |
| Is X a **biologic / peptide**? | Clinical + animal literature; DrugBank | ChEMBL small-molecule curation under-covers biologics (see Talactoferrin, KPV rows) |
| Natural-product / TCM / botanical activity | ChEMBL **+** CNKI / WanFang / J-STAGE **+** the [query-framing discipline](../../.claude/skills/new-comp-experiment/SKILL.md) | ChEMBL alone systematically underrepresents non-Western natural-product literature (see Eurycomanone row) |

**The conservative-exclusion rule.** For a screen that must avoid known target relationships, use **ChEMBL activity ∪ UniProt-exposed DrugBank relationships**. This is a broad exclusion set, not a complete biological-interactor catalog and not a relationship-typing method. Verify any load-bearing substrate or inhibitor label against a per-drug primary or curated source. The shared [`experiments/lib/target_interactors.py`](experiments/lib/target_interactors.py) helper emits this relationship/activity exclusion set and preserves `unqueried` states; it does not assign substrate subtype.

**Worked example — COMP-047 (ABCG2 Q141K).** Rosuvastatin returned no ABCG2 activity row in the experiment's bounded ChEMBL check. The [FDA CRESTOR label](https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/021366s047lbl.pdf) independently identifies rosuvastatin as a BCRP substrate; the UniProt-exposed DrugBank set separately flags an ABCG2 relationship. The FDA label supports the substrate type. The generic relationship flag supports conservative exclusion but cannot supply that subtype. Full result: [`abcg2-q141k-chaperone-rescreen-computational.md`](../abcg2-q141k-chaperone-rescreen-computational.md).

---

## Master Cross-Check Table

| # | Compound | ChEMBL ID | Most potent curated target + IC50/Ki | Wiki's current framing | Discrepancy? | Last refreshed |
|---|---|---|---|---|---|---|
| 1 | **Quercetin** | CHEMBL50 | **5-lipoxygenase: IC50 = 300 nM** (*J Med Chem* 1991); DPPH antioxidant assay (no protein target) tops the pChEMBL ranking at 9.96 but is not a pharmacological target | NLRP3 pathway modulator (IL-1β in MSU model) | **YES** — 5-LOX is stronger than any NLRP3 activity and gout-relevant (LTB4 neutrophil chemotaxis); DPPH outranks 5-LOX by pChEMBL but is a chemical antioxidant assay, not a protein target; 5-LOX finding remains valid and propagation-worthy | 2026-07-01 |
| 2 | **Oridonin** | CHEMBL1164920 | Human NLRP3: **IC50 = 5.18 μM** (THP-1, *Eur J Med Chem* 2023); as of 2026-07-01: 3 new 2024 entries added (% inhibition in human THP-1: 63% and 90.1% at unspecified concentrations, *Bioorg Med Chem Lett* 2024; and 1 *J Med Chem* 2024 entry without quantified IC50) | "0.5–2 μM" covalent Cys279 binder | **YES** — curated human cellular IC50 is 5.18 μM; the 0.5–2 μM number comes from cell-free / mouse-derived assays. As of 2026-07-01: IC50 unchanged; new 2024 percent-inhibition entries add supporting evidence without changing the framing | 2026-07-01 |
| 3 | **Dapansutrile (OLT1177)** | CHEMBL3989943 | Human NLRP3: **IC50 = 1.0 μM** human MDM (*Eur J Med Chem* 2023); **IC50 = 1 nM mouse J774A.1** (*Eur J Med Chem* 2020; *Bioorg Med Chem Lett* 2021) | Direct NLRP3 ATPase inhibitor, Phase 2a gout success | **YES** — 1000× mouse-vs-human potency gap; clinical efficacy is consistent with human μM potency, not sub-nM. As of 2026-07-01: no new data; baseline confirmed | 2026-07-01 |
| 4 | **β-Caryophyllene** | CHEMBL445740 | **CB2: Ki = 150 nM** (*Eur J Med Chem* 2018, pChEMBL 6.82) — now curated in ChEMBL v37 | CB2 agonist + NLRP3/caspase-1/TLR4 suppressor (MSU gout, rat) | **No discrepancy** — CB2 Ki 150 nM now confirmed in ChEMBL (was external-literature-only at baseline). "Direct NLRP3 binding" claim from 2021 docking paper remains uncurated; zero human NLRP3 entries (CHEMBL1741208) | 2026-07-01 |
| 5 | **BHB (beta-hydroxybutyrate)** | CHEMBL1162496 | **No curated bioactivity with pChEMBL ≥ 6** against any target | "Direct NLRP3 signaling molecule; hits CP1/CP2/CP3" | **Soft** — BHB's "direct NLRP3 binding" is from Youm et al. 2015 *Nat Med*, not represented in ChEMBL; no off-target red flags. As of 2026-07-01: unchanged | 2026-07-01 |
| 6 | **KPV (tripeptide)** | **Not indexed** | — (peptide below ChEMBL small-molecule threshold) | Direct NLRP3 assembly inhibitor + NF-κB stabilizer via PepT1 uptake | N/A — peptides of this size are poorly covered; absence is not a discrepancy. Note in wiki: "not small-molecule-curated" | 2026-07-01 |
| 7 | **Carnosine** | CHEMBL242948 | No curated activity pChEMBL ≥ 6 (ROR-γ qHTS at 2.24 μM is below threshold) | NLRP3/NF-κB/p-JNK suppressor; URAT1/GLUT9 downregulator (hyperuricemia rat) | **Soft** — no curated high-potency activity; direct hyperuricemia evidence (Zhang et al. 2024) is functional, not represented. As of 2026-07-01: unchanged | 2026-07-01 |
| 8 | **Ursolic acid** | CHEMBL169 | **ROR-γ: IC50 = 0.75 nM** (pChEMBL 9.12, *J Med Chem* 2023); **NF-κB (p65): IC50 = 31 nM** (pChEMBL 7.51, *Bioorg Med Chem* 2018); **SENP1: IC50 = 6.4 nM** (pChEMBL 8.19, *Eur J Med Chem* 2022); HIV-1 EC50 = 10 nM; 16 total entries pChEMBL ≥ 6 | NLRP3/NF-κB suppressor (triterpene), OA + Kawasaki animal models | **YES (major, new 2026-07-01)** — baseline (v34) reported zero curated activities pChEMBL ≥ 6; ChEMBL v37 now has 16 entries. Top hit ROR-γ at 0.75 nM is gout-relevant (Th17 inflammation axis); NF-κB at 31 nM directly supports wiki's NF-κB framing with biochemical data | 2026-07-01 |
| 9 | **Taurine** | CHEMBL239243 | BLM helicase (qHTS, *Inconclusive*) potency 12.6 nM; taurine transporter EC50 10 μM (substrate, below threshold) | NLRP3 K⁺-efflux-block upstream (sepsis, cardiac animal models) | **Soft** — BLM hit is qHTS noise flagged "inconclusive"; TauT substrate is physiological. As of 2026-07-01: unchanged | 2026-07-01 |
| 10 | **EGCG** | CHEMBL297453 | **Plasmodium falciparum enoyl-ACP reductase: Ki = 8 nM** (*J Med Chem* 2007); human 20S proteasome chymotrypsin IC50 86 nM; DNMT Ki 28 nM; as of 2026-07-01: PC-12 neuroprotection IC50 30 nM (*Eur J Med Chem* 2024) added at rank 5 | TLR4/NF-κB/NLRP3 cascade blocker; ROS reduction | **YES** — strongest curated target is an anti-malarial enzyme; **20S proteasome inhibition (IC50 86 nM) is a human off-target** that matters for safety at high oral doses. As of 2026-07-01: new PC-12 entry (minor) | 2026-07-01 |
| 11 | **Sulforaphane** | CHEMBL48802 | **iNOS IC50 = 400 nM** (mouse RAW, *J Med Chem* 2015); **Nrf2/Keap1 EC50 = 580 nM** (human U2OS, *J Med Chem* / *ACS Med Chem Lett* 2019) | Nrf2 activator → NLRP3 priming block; ABCG2 inducer | No discrepancy — curated potency lines up with wiki's Nrf2/iNOS framing. As of 2026-07-01: unchanged | 2026-07-01 |
| 12 | **Berberine** | CHEMBL295124 | **Tryptophan 2,3-dioxygenase: IC50 = 30 nM** (*Eur J Med Chem* 2024); CYP1B1 Ki 44 nM (*Eur J Med Chem* 2017); CYP1B1 IC50 94 nM (*Eur J Med Chem* 2019); dsDNA EC50 100 nM (*J Nat Prod* 2024); AChE IC50 100 nM (*Bioorg Med Chem* 2015) | AMPK activator / gut metabolism / SIBO modulator / NLRP3 | **YES** — top curated activity is TDO (kynurenine pathway), then CYP1B1 (estrogen metab), dsDNA, and AChE — none reflected in current wiki. As of 2026-07-01: dsDNA entry (*J Nat Prod* 2024) added at rank 4; TDO and CYP1B1 confirmed | 2026-07-01 |
| 13 | **Resveratrol** | CHEMBL165 | Cell-line cytotoxicity IC50s rank 1–4 (HeLa 0.023 nM, SK-N-SH 0.040 nM, A549 0.045 nM, MCF7 0.079 nM — *J Med Chem* 2011; antiproliferative, not molecular targets); **Dipeptidyl peptidase-4: IC50 = 0.6 nM** (human, *Eur J Med Chem* 2018, pChEMBL 9.22) at rank 5 | SIRT1 activator / mitochondrial homeostasis / weak NLRP3 | **YES** — DPP-4 at 0.6 nM (rank 5 among molecular targets) is resveratrol's strongest protein-target curated activity; cell-line antiproliferative entries rank above it by pChEMBL but target cell lines, not molecular proteins. As of 2026-07-01: DPP-4 finding confirmed unchanged; cytotoxicity entries now visible above it | 2026-07-01 |
| 14 | **Curcumin** | CHEMBL140 | **Amyloid-β precursor protein: Ki = 0.208 nM** (*J Med Chem* 2006, pChEMBL 9.68); **DYRK2: IC50 = 2.5 nM** (*J Med Chem* 2023, pChEMBL 8.60, NEW); Lactoylglutathione lyase Ki 5.0 nM (*Bioorg Med Chem* 2020); **NLRP3 human THP-1 IC50 = 24.2 μM** (*J Nat Prod* 2020, pChEMBL 4.62) | Direct NLRP3 pathway inhibitor (MSU gout animal model); ranked 3rd compound with direct human NLRP3 data | **YES (updated 2026-07-01)** — curcumin IS curated against human NLRP3 (24.2 μM). New: DYRK2 IC50 = 2.5 nM is now rank-2 molecular target (J Med Chem 2023), between amyloid-β (rank 1) and the NLRP3 entry; mechanistically relevant to proteasome regulation | 2026-07-01 |
| 15 | **Ergothioneine** | **Not indexed** | — (name search and SMILES similarity return zero) | Potent antioxidant / ROS scavenger / indirect NLRP3 suppression | N/A — unusual sulfur-containing betaine structure; wiki's "indirect via ROS" framing is appropriate. As of 2026-07-01: unchanged | 2026-07-01 |
| 16 | **Ferulic acid** | CHEMBL32749 | Amyloid fibril binding Ki = 0.77 nM (*Bioorg Med Chem Lett* 2007, imaging probe displacement); Casein kinase 2 (CK2) Ki = 410 nM (*J Med Chem* 2023, NEW) | Autophagy induction + caspase-1 blocker (NLRP3 pathway) | **Soft** — 0.77 nM amyloid binding is imaging-probe Ki, not functional inhibition. As of 2026-07-01: CK2 Ki 410 nM (*J Med Chem* 2023) added at rank 5 (minor) | 2026-07-01 |
| 17 | **Kojic acid** | CHEMBL287556 | Mushroom tyrosinase INHIBITOR 1.0 nM (*Eur J Med Chem* 2023, activity_type "INHIBITOR" not IC50); human tyrosinase IC50 7–10 μM (multiple entries) | Antioxidant + melanin synthesis inhibitor; NLRP3 untested | **Soft** — the 1.0 nM "INHIBITOR" entry (2023) uses a different activity_type and assay format from the 7–10 μM IC50 entries (human tyrosinase); the difference likely reflects competitive inhibition kinetics vs. standard IC50 assay rather than a true discrepancy. NLRP3 silence is honest. As of 2026-07-01: new 2023 mushroom tyrosinase entry noted | 2026-07-01 |
| 18 | **Theaflavin** | CHEMBL346119 | **Bcl-2: Ki = 691 nM** (*Proc Natl Acad Sci* 2007 / *Med Chem Res* 2010, pChEMBL 6.16) | NLRP3-NEK7 interaction disruptor; URAT1/GLUT9 downregulator (Chen 2023 functional data) | **Soft** — no NLRP3 or NEK7 entries in ChEMBL; wiki framing from Chen 2023 *Acta Pharmacol Sin* is functional (MSU macrophages), not in ChEMBL scope. Bcl-2 hit (anti-apoptotic) is pharmacologically distant from gout thesis | 2026-07-01 |
| 19 | **Zileuton** | CHEMBL93 | **5-lipoxygenase (ALOX5): IC50 = 840 nM** (pChEMBL 6.08, *J Med Chem* 1993); organism-level IC50 2 nM (*J Med Chem* 1994, assay-level not protein-level) | Direct 5-LOX inhibitor (CP6a); pharma-grade LTB4 blocker | **No discrepancy** — wiki framing as direct 5-LOX inhibitor (CP6a) confirmed by curated ALOX5 IC50 840 nM. No NLRP3 entries. Canonical 5-LOX target ID is CHEMBL215 (ALOX5), not CHEMBL2185 | 2026-07-01 |
| 20 | **Tranilast** | CHEMBL415324 | NPC1 Potency ~89 nM; Rab-9A Potency ~92 nM; CHRM1 Potency ~126 nM (all from phenotypic screen, null journal/year annotation) | Direct NACHT domain binder; blocks NLRP3 oligomerization | **Soft** — NACHT domain binding from EMBO Mol Med 2017 is not in ChEMBL. Phenotypic screen hits (NPC1, Rab-9A, CHRM1) have no journal annotation — treat as unvalidated HTS hits. No NLRP3 entry | 2026-07-01 |
| 21 | **Disulfiram** | CHEMBL964 | **LOXL4: IC50 = 59 nM** (pChEMBL 7.23, *Bioorg Med Chem Lett* 2018); ALOX15 Potency 63 nM (phenotypic, null journal); tau binding Potency 25 nM (phenotypic) | GSDMD Cys191 covalent modifier; pyroptosis-pore blocker (CP6b) | **Soft** — GSDMD Cys191 modification (Nature Immunol 2020) is covalent; not represented as standard IC50 in ChEMBL (expected for a covalent mechanism). LOXL4 IC50 59 nM (*Bioorg Med Chem Lett* 2018) is a new off-target of possible interest (lysyl oxidase family, fibrosis/inflammation). ALOX15 and tau hits are phenotypic/unvalidated | 2026-07-01 |
| 22 | **Limonene (D-)** | CHEMBL449062 | **No curated activity pChEMBL ≥ 6** | Nrf2 activator + TLR4 suppression; direct rat PO+MSU gout model (Venkatesan 2025) | **Soft** — Nrf2/TLR4 framing from animal-model functional data; no ChEMBL biochemical targets. Food-additive status (GRAS) appropriate | 2026-07-01 |
| 23 | **NAC (Acetylcysteine)** | CHEMBL600 | ALOX15 Potency 25 nM (phenotypic, null journal — unvalidated); THR-β Potency 562 nM (phenotypic, null journal); COX-1 AC50 890 nM (*Nat Commun* 2023) | Glutathione precursor / ROS scavenger (CP2); no direct NLRP3 claim | **Soft** — ALOX15 and THR-β hits are phenotypic screen entries without journal annotation; treat as unvalidated until independently replicated. COX-1 AC50 890 nM (*Nat Commun* 2023) is the only journal-annotated entry; not mechanistically central to NAC's gout-stack role. No NLRP3 entries | 2026-07-01 |
| 24 | **Spermidine** | CHEMBL19612 | **Carbonic anhydrase 4: Ki = 112 nM** (pChEMBL 6.95, *J Med Chem* 2010) | Autophagy inducer (TFEB/mTOR-independent); NLRP3 accumulation suppressor | **Soft** — CA4 binding is pharmacologically distant from autophagy; not gout-relevant. Wiki's autophagy framing from longevity literature is functional, not biochemical. No NLRP3 entries | 2026-07-01 |
| 25 | **Vitamin D3 (Cholecalciferol)** | CHEMBL1042 | **Vitamin D3 receptor: EC50 = 0.21 nM** (pChEMBL 9.68, *Bioorg Med Chem Lett* 2014); VDR IC50 87 nM (*Eur J Med Chem* 2021) | VDR activation → NF-κB suppression (CP1); K2 prevents vascular calcification | **No discrepancy** — VDR EC50 0.21 nM directly supports wiki mechanism. No NLRP3 entries (expected — VDR is the relevant target) | 2026-07-01 |
| 26 | **Eurycomanone** | CHEMBL1171981 | **No curated activity pChEMBL ≥ 6** | In the 2019 hURAT1 assay, pure eurycomanone was compound 3 and showed comparatively low activity; the stronger 50 µM activity belonged to eurycomanol-type compounds 4–7. Extract-level transporter changes and purified-eurycomanol PRPS/transporter findings are separate materials (PMID 31920654; PMID 34785103). | **Soft** — ChEMBL absence does not negate source-specific non-ChEMBL evidence, but neither the extract nor eurycomanol result can be assigned to eurycomanone. No GLUT9, ABCG2, NPT1, or PRPS claim is decision-usable for pure eurycomanone from these records. | 2026-07-01 |
| 27 | **Talactoferrin alfa** | CHEMBL2108651 | **No curated bioactivity** | NLRP3/caspase-1/GSDMD axis suppressor at CP5; Phase 3 clinical data (oral bioavailability, safety) | **N/A** — biologic (recombinant lactoferrin protein); ChEMBL small-molecule curation scope does not cover biologics meaningfully. Clinical Trial status and mechanistic framing rest on animal + Phase 3 data, not ChEMBL biochemistry | 2026-07-01 |

**Legend:**
- **YES** — wiki materially mis-states or omits a target that ChEMBL curation supports at a comparable or better potency than the wiki's current framing; propagate to the primary concept page.
- **Soft** — no strong curated signal one way or the other; the wiki's functional/animal-model framing is defensible, but ChEMBL does not have direct binding/inhibition data to back it up.
- **No discrepancy** — wiki framing and ChEMBL data converge on the same target class and potency range.
- **N/A / Not indexed** — compound is not in ChEMBL (peptides, biologics, unusual structures); absence is not evidence of weakness.

---

## Expanded Findings: Compounds with Propagation-Worthy Discrepancies

### Ursolic Acid → ROR-γ (0.75 nM), NF-κB (31 nM), SENP1 (6.4 nM) — **NEW 2026-07-01**

**Evidence Level:** In Vitro (curated ChEMBL v37 entries, multiple papers)

**Finding:** Ursolic acid (CHEMBL169) was reported in the 2026-04-24 baseline as having zero curated activities at pChEMBL ≥ 6 in ChEMBL v34. In ChEMBL v37 (queried 2026-07-01), 16 curated entries are present at pChEMBL ≥ 6. Top three:
1. **ROR-γ: IC50 = 0.75 nM** (pChEMBL 9.12, *J Med Chem* 2023)
2. **SENP1: IC50 = 6.4 nM** (pChEMBL 8.19, *Eur J Med Chem* 2022)
3. **HIV-1: EC50 = 10 nM** (pChEMBL 8.00, *Eur J Med Chem* 2019)
4. **NF-κB (p65): IC50 = 31 nM** (pChEMBL 7.51, *Bioorg Med Chem* 2018)

**Current wiki framing:** [nlrp3-inhibitor-screen.md](../nlrp3-inhibitor-screen.md) frames ursolic acid as "NLRP3/NF-κB suppressor (triterpene); OA + Kawasaki animal models; Tier 1 candidate due to 8.59 g/L bioreactor production." No curated biochemical target data was cited because none existed at the time of original writing.

**Why ROR-γ matters for gout biology:** ROR-γ (RAR-related orphan receptor gamma; encoded by RORC) is the master transcription factor for Th17 cell differentiation and IL-17A/F production. Although the Open Enzyme platform focuses primarily on NLRP3/IL-1β (innate arm), Th17-derived IL-17 amplifies the inflammatory loop in chronic gout, promotes neutrophil survival in synovial tissue, and contributes to tophus formation. ROR-γ inhibition at 0.75 nM is pharmacologically comparable to the clinical-stage ROR-γ inverse agonist class (e.g., CMPD1 from Johnson & Johnson, designed specifically as ROR-γ inhibitors for Th17-driven autoimmunity). This places ursolic acid mechanistically in a class that has not been surfaced in the gout wiki at all.

**Why NF-κB at 31 nM matters:** The wiki's NF-κB framing for ursolic acid was based on functional IL-1β readouts and downstream markers. A curated NF-κB (p65) IC50 = 31 nM (*Bioorg Med Chem* 2018) provides direct biochemical evidence for the NF-κB inhibition claim, elevating it from "mechanistic extrapolation" to "In Vitro" evidence level. This is propagation-worthy for [nlrp3-inhibitor-screen.md](../nlrp3-inhibitor-screen.md)'s Tier-1 entry.

**Why SENP1 at 6.4 nM is worth noting:** SENP1 (sentrin-specific protease 1) is the de-SUMOylation enzyme responsible for processing SUMO precursors and for maturation of SUMO-modified proteins. SENP1 has been linked to NF-κB pathway regulation (IKKβ SUMOylation is a negative regulatory modification; SENP1 activity frees IKKβ to activate NF-κB). SENP1 inhibition → sustained SUMOylation → attenuated IKKβ → NF-κB suppression — a mechanistic route that would be orthogonal to direct ROR-γ and p65 inhibition but converge on the same inflammatory output. (In Vitro; Mechanistic Extrapolation for the gout-link.)

**Suggested action:** Add a mechanism note to [nlrp3-inhibitor-screen.md](../nlrp3-inhibitor-screen.md) Tier 1 entry for ursolic acid: "As of 2026-07-01 ChEMBL v37 refresh: 16 curated entries pChEMBL ≥ 6 now present (zero in v34). Top curated targets: ROR-γ IC50 = 0.75 nM (*J Med Chem* 2023), SENP1 IC50 = 6.4 nM (*Eur J Med Chem* 2022), NF-κB (p65) IC50 = 31 nM (*Bioorg Med Chem* 2018). ROR-γ inhibition adds a Th17-axis mechanism not previously attributed to ursolic acid — relevant to chronic gout/tophus biology. NF-κB IC50 elevates the NF-κB claim from functional/animal to In Vitro biochemical." See synthesis/queue item for full discussion.

**Caveat:** Three papers from three different labs (2018, 2022, 2023) — independent replication across multiple laboratories increases confidence. Still In Vitro only; animal-model or cellular gout-specific validation not yet published for the ROR-γ or SENP1 mechanisms specifically.

---

### Curcumin → DYRK2 IC50 = 2.5 nM — **NEW 2026-07-01**

**Evidence Level:** In Vitro (curated ChEMBL v37 entry)

**Finding:** Curcumin (CHEMBL140) now has a curated **DYRK2 IC50 = 2.5 nM** (pChEMBL 8.60, *J Med Chem* 2023) at rank 2 in its bioactivity profile (between amyloid-β Ki = 0.208 nM at rank 1 and lactoylglutathione lyase Ki = 5.0 nM at rank 3). This entry was not present in ChEMBL v34 (queried 2026-04-24).

**Current wiki framing:** [nlrp3-inhibitor-screen.md](../nlrp3-inhibitor-screen.md) cites curcumin's human NLRP3 IC50 = 24.2 μM (*J Nat Prod* 2020, pChEMBL 4.62) — the third compound in the stack with direct human NLRP3 data. The amyloid-β Ki was flagged as an off-target in the baseline. DYRK2 was not mentioned.

**Why DYRK2 matters:** DYRK2 (dual-specificity tyrosine-phosphorylation-regulated kinase 2) phosphorylates several substrates relevant to proteostasis and inflammation:
- **Proteasome activator PA28γ** → curcumin's DYRK2 inhibition at 2.5 nM potentially disrupts 26S proteasome assembly, providing a proteasome-regulatory mechanism that is mechanistically adjacent to EGCG's 20S proteasome inhibition (IC50 86 nM) from a different angle.
- **Snail (SNAI1)** → DYRK2 promotes Snail ubiquitination and degradation; inhibiting DYRK2 could stabilize Snail, which regulates epithelial-mesenchymal transition (cancer biology) but also modulates NF-κB indirectly. This is pharmacologically distant from gout.
- **Glutaminyl cyclase/IKKβ context**: DYRK2 has been shown to regulate the AMPK–mTOR axis upstream of autophagy, which connects mechanistically to curcumin's autophagy-promoting effects in macrophages.

The connection to EGCG's proteasome story is the most interesting angle for the Open Enzyme platform: two stack compounds (curcumin and EGCG) now have curated ChEMBL entries at the proteasome system, though through different mechanisms (DYRK2/26S regulation vs. 20S chymotrypsin-like activity). This is a sub-100 nM human kinase activity for a compound whose bioavailability crisis (~5% oral absorption) is the primary reason it was not ranked Tier 1 in [nlrp3-inhibitor-screen.md](../nlrp3-inhibitor-screen.md). The in vivo relevance of the DYRK2 hit is therefore tied to local GI/portal concentrations after oral dosing, not systemic.

**Suggested action:** Minor propagation to [nlrp3-inhibitor-screen.md](../nlrp3-inhibitor-screen.md) Tier-3 curcumin entry: "As of 2026-07-01 ChEMBL v37 refresh: DYRK2 IC50 = 2.5 nM (*J Med Chem* 2023, pChEMBL 8.60) is now rank-2 curated target. DYRK2 regulates proteasome activity via PA28γ phosphorylation, providing a biochemical link between curcumin and the proteasome-regulation mechanism (adjacently EGCG's 20S proteasome inhibition, IC50 86 nM). Gout-specific relevance of the DYRK2 hit is indirect; amyloid-β binding at 0.208 nM remains the top curated off-target and the strongest argument against framing curcumin as an anti-inflammatory specialist."

---

### Resveratrol → DPP-4 inhibition (sub-nM, curated)

**Evidence Level:** In Vitro (curated ChEMBL entry)

**Finding:** Resveratrol (CHEMBL165) has a curated human DPP-4 IC50 of **0.6 nM** (pChEMBL 9.22, *Eur J Med Chem* 2018). This is resveratrol's strongest protein-target curated activity — stronger than any of its reported SIRT1, Nrf2, or quinone reductase activities. As of 2026-07-01 refresh, cell-line antiproliferative IC50s from *J Med Chem* 2011 rank above DPP-4 by raw pChEMBL (HeLa, SK-N-SH, A549, MCF7 at 0.02–0.08 nM), but these are cell-line targets, not discrete molecular proteins — the DPP-4 entry remains the strongest molecular target.

**Current wiki framing:** [nlrp3-inhibitor-screen.md](../nlrp3-inhibitor-screen.md) frames resveratrol as a "stilbenoid polyphenol; SIRT1-dependent autophagy." No mention of DPP-4.

**Suggested reframing:** Add a mechanism note: "Resveratrol's single most potent curated molecular-target activity is DPP-4 inhibition (IC50 = 0.6 nM, pChEMBL 9.22, *Eur J Med Chem* 2018) — a validated type-2 diabetes target. This does not directly improve the gout case, but flags resveratrol as mechanistically similar to the gliptin class at physiologically achievable concentrations. If resveratrol is co-administered, DPP-4 inhibition may contribute to glucose homeostasis effects independent of SIRT1." Also worth a note in [gout-deep-dive.md](../gout-deep-dive.md) given the gout-T2D comorbidity cluster.

---

### Berberine → Tryptophan 2,3-dioxygenase (TDO, sub-100 nM)

**Evidence Level:** In Vitro (curated ChEMBL entries)

**Finding:** Berberine (CHEMBL295124) has a curated TDO IC50 of **30 nM** (*Eur J Med Chem* 2024, pChEMBL 7.52), CYP1B1 Ki of 44 nM (*Eur J Med Chem* 2017), CYP1B1 IC50 94 nM (*Eur J Med Chem* 2019), AChE IC50 100 nM (*Bioorg Med Chem* 2015). As of 2026-07-01: dsDNA EC50 100 nM (*J Nat Prod* 2024) added at rank 4.

**Current wiki framing:** Berberine in [nlrp3-exploit-map.md](../nlrp3-exploit-map.md) etc. is framed as "AMPK activator / gut antimicrobial / dysbiosis modulator / NLRP3 suppressor." TDO, CYP1B1, and AChE are not mentioned.

**Suggested reframing:** TDO inhibition has been explored as an immuno-oncology / anti-inflammatory strategy — tryptophan → kynurenine metabolism modulates T-cell and NLRP3 inflammatory crossroads. Add mechanism note to [nlrp3-inflammasome.md](../nlrp3-inflammasome.md) under berberine. CYP1B1 inhibition is a drug-drug-interaction flag for [supplements-stack.md](../supplements-stack.md).

---

### EGCG → 20S proteasome (IC50 86 nM, human)

**Evidence Level:** In Vitro (curated ChEMBL entry, replicated)

**Finding:** EGCG (CHEMBL297453) has a curated human 20S proteasome chymotrypsin-like activity IC50 of **86 nM** (*Bioorg Med Chem* 2010, confirmed *Eur J Med Chem* 2019, pChEMBL 7.07). Also sub-30 nM against *P. falciparum* ENR (Ki = 8 nM). As of 2026-07-01: PC-12 neuroprotection IC50 30 nM (*Eur J Med Chem* 2024) added at rank 5.

**Suggested reframing:** Add a safety note: high-dose EGCG (>800 mg/day) is a known hepatotoxicity risk (EMA 2018), and sub-100-nM proteasome activity is a plausible contributing mechanism. Dose-ceiling for intense use protocols should factor in this proteasome off-target. See also: curcumin's DYRK2 hit above — two stack compounds modulate the proteasome system through complementary mechanisms.

---

### Curcumin → human NLRP3 IC50 = 24.2 μM (curated)

**Evidence Level:** In Vitro (curated ChEMBL entry)

**Finding:** Curcumin (CHEMBL140) has a **curated direct human NLRP3 IC50 of 24.2 μM** (LPS-primed PMA-differentiated THP-1 cells, nigericin challenge, *J Nat Prod* 2020, pChEMBL 4.62). This makes curcumin the **third compound** in the entire Open Enzyme stack with a ChEMBL-curated direct human NLRP3 number, after dapansutrile (1.0 μM) and oridonin (5.18 μM). Its strongest curated molecular-target activity is amyloid-β Ki = 0.208 nM; DYRK2 at 2.5 nM is rank 2 (see above).

**Current wiki framing:** [nlrp3-inhibitor-screen.md](../nlrp3-inhibitor-screen.md) Tier 3 entry cites functional curcumin data (10–50 μM blocks MSU-induced NLRP3). This is consistent with the curated 24.2 μM IC50.

**Suggested reframing:** Update the Tier-3 entry to cite the specific curated human NLRP3 IC50 (24.2 μM, THP-1, pChEMBL 4.62) and rank curcumin's NLRP3 potency relative to dapansutrile (1.0 μM) and oridonin (5.18 μM): curcumin is **24× weaker than dapansutrile** and **5× weaker than oridonin** in the same human cellular format. Combined with curcumin's ~5% oral bioavailability, gout animal efficacy likely reflects very high local GI/portal exposure.

---

### Quercetin → 5-LOX (300 nM, already documented in 2026-04-23 sweep)

Already propagated in [nlrp3-inhibitor-screen.md](../nlrp3-inhibitor-screen.md) appendix. As of 2026-07-01: the 5-LOX entry is still present in ChEMBL v37 (pChEMBL ~6.52) but now ranks below a DPPH radical-scavenging entry (pChEMBL 9.96) and E. coli gyrase B entry. Both the DPPH and gyrase entries are pharmacologically irrelevant to mammalian gout biology — the 5-LOX finding remains the dominant gout-relevant curated activity for quercetin. Listed here for continuity.

---

## Compounds Not Indexed in ChEMBL

| Compound | Reason | Implication |
|---|---|---|
| **KPV (Lys-Pro-Val)** | Tripeptide below ChEMBL's small-molecule curation focus; no salt/synonym match | Absence does not indicate weakness — the [peptide-gout-addendum.md](../peptide-gout-addendum.md) framing (direct NLRP3 + NF-κB, PepT1-transported) is from peptide-pharmacology literature not in ChEMBL's scope. Note in wiki: "KPV is not small-molecule-curated; mechanistic claims rest on α-MSH fragment pharmacology papers." |
| **Ergothioneine** | Name search and SMILES similarity both return zero hits | Ergothioneine is a sulfur-containing trimethylammonium betaine; unusual structure and physiological pharmacology explain absence. Wiki's "indirect ROS scavenger" framing in [nlrp3-inhibitor-screen.md](../nlrp3-inhibitor-screen.md) is honest. |
| **Talactoferrin alfa** | CHEMBL2108651 exists but has zero bioactivity entries | Biologic (recombinant lactoferrin protein); ChEMBL's small-molecule focus means it is not meaningfully covered. Clinical Trial phase-3 data and animal-model evidence are the appropriate evidence base for this compound. |

**The single most important meta-observation:** A large fraction of the Open Enzyme stack is not represented in ChEMBL with direct binding/inhibition data, because the database is curated for medicinal-chemistry lead compounds, not nutraceuticals, peptides, endogenous metabolites, or biologics. This is neither surprising nor damning — but it does mean that **the evidence base for most stack compounds is functional (cell/animal IL-1β readouts, downstream markers), not biochemical (Kd/IC50 on purified protein)**. Any claim of "direct NLRP3 inhibitor" should use the two-tier labeling introduced in the 2026-04-23 sweep:

1. **Direct NLRP3 inhibitor (binding/inhibition IC50 curated):** dapansutrile, oridonin, curcumin.
2. **NLRP3 pathway modulator (functional IL-1β reduction):** everything else in the stack.

MCC950 (CRID3/CP-456773) is not retrievable by common synonyms in ChEMBL name search — its IC50 (~7.5 nM, *J Biol Chem* 2015) comes from the primary literature and is widely cited but not directly in ChEMBL's curated set. Benchmark status unchanged; ChEMBL lookup remains open.

---

## Implications for the affected tracks

1. **Ursolic acid: new biochemical target profile warrants mechanism update.** ROR-γ at 0.75 nM and NF-κB at 31 nM are direct-binding biochemical evidence for mechanisms the wiki claimed only on functional/animal grounds. ROR-γ adds a Th17-axis coverage not previously attributed to ursolic acid. See synthesis/queue item 2026-07-01-chembl-discrepancy-1.

2. **Curcumin's DYRK2 hit connects two stack compounds at the proteasome axis.** EGCG inhibits the 20S proteasome (IC50 86 nM); curcumin inhibits DYRK2 at 2.5 nM (DYRK2 regulates 26S proteasome assembly). Both compounds therefore touch proteasome biology through different mechanisms, potentially producing additive effects. The bioavailability crisis limits curcumin's systemic reach, but this is worth noting in formulation contexts. See synthesis/queue item 2026-07-01-chembl-discrepancy-2.

3. **β-Caryophyllene CB2 claim is now ChEMBL-confirmed.** The 2026-04-24 baseline flagged CB2 Ki ~155 nM as external-literature only. ChEMBL v37 now has CB2 Ki = 150 nM (Eur J Med Chem 2018). This resolves the "Partial discrepancy" status — the CB2 agonism claim is curated and should be cited as ChEMBL-confirmed in [supplements-stack.md](../supplements-stack.md) and [cannabinoids-terpenes.md](../cannabinoids-terpenes.md).

4. **Zileuton 5-LOX framing confirmed.** ALOX5 IC50 840 nM is curated, matching the wiki's mechanism claim. Note: canonical ChEMBL ID for human ALOX5 is CHEMBL215, not CHEMBL2185.

5. **Disulfiram LOXL4 hit (59 nM) is a previously unrecognized off-target.** Lysyl oxidase homolog 4 is involved in collagen crosslinking and has been studied in fibrosis and cancer contexts. Its relevance to gout or GSDMD biology is unclear — flag for tracking but do not propagate without primary source verification.

6. **Resveratrol DPP-4 and berberine TDO remain the most actionable "ChEMBL surprises."** Both were surfaced in the 2026-04-24 baseline and are confirmed unchanged in v37. Neither has been propagated to primary wiki pages yet — remaining action items for a subsequent walkthrough.

7. **"Koji-yeast hybrid" engineering logic is unchanged.** Ursolic acid and quercetin remain top production candidates; the ChEMBL updates don't invalidate production feasibility or functional efficacy. They clarify and in some cases strengthen mechanism claims.

---

## Appendix: Refresh Recipe

```text
# Current database: ChEMBL v37 (2026-05-01 release), accessed via REST API

# 1. Check database version
GET https://www.ebi.ac.uk/chembl/api/data/status?format=json

# 2. Per compound: find ChEMBL ID
GET https://www.ebi.ac.uk/chembl/api/data/molecule?pref_name__icontains=<name>&format=json&limit=3

# 3. Per compound: top curated bioactivities
GET https://www.ebi.ac.uk/chembl/api/data/activity?molecule_chembl_id=<ID>&pchembl_value__gte=6&order_by=-pchembl_value&limit=5&format=json

# 4. Per compound: direct NLRP3 check (human NLRP3 = CHEMBL1741208)
GET https://www.ebi.ac.uk/chembl/api/data/activity?molecule_chembl_id=<ID>&target_chembl_id=CHEMBL1741208&limit=5&format=json

# 5. For 5-LOX compounds: canonical human ALOX5 = CHEMBL215 (not CHEMBL2185)
GET https://www.ebi.ac.uk/chembl/api/data/activity?molecule_chembl_id=<ID>&target_chembl_id=CHEMBL215&limit=5&format=json
```

**Interpretation rules:**
- pChEMBL ≥ 7 (100 nM or better) against a human target with assay_type="B" = treat as a real biochemical target.
- pChEMBL 5–7 with "Inconclusive" activity_comment or "qHTS" in assay description = PubChem HTS noise; discount.
- Null document_journal = phenotypic screen without journal annotation; treat as unvalidated HTS hit.
- Cell-line targets (HeLa, MCF7, etc.) in the activity table reflect antiproliferative IC50s, not molecular-protein targets; filter these for mechanistic interpretation.
- Zero bioactivities against NLRP3 (CHEMBL1741208) = "NLRP3 pathway modulator" not "NLRP3 inhibitor" — apply the two-tier labeling.
- Zero curated bioactivities anywhere above pChEMBL 6 = compound is primarily supported by functional/animal data; state this explicitly.

**Refresh cadence:** Quarterly. Next refresh: **2026-10-01**.

---

## Sources

- EMBL-EBI ChEMBL v34 database, accessed via Anthropic life-sciences MCP plugin, 2026-04-24.
- EMBL-EBI ChEMBL v37 database (release 2026-05-01), accessed via REST API, 2026-07-01 quarterly refresh.
- Resveratrol DPP-4: *Eur J Med Chem* 2018 (CHEMBL4229387 assay; pChEMBL 9.22).
- Berberine TDO: *Eur J Med Chem* 2024 (CHEMBL5617618 assay; pChEMBL 7.52).
- Berberine CYP1B1: *Eur J Med Chem* 2017 (CHEMBL4035349 assay; pChEMBL 7.36).
- EGCG 20S proteasome: *Bioorg Med Chem* 2010 and *Eur J Med Chem* 2019 (CHEMBL4433382 assay; pChEMBL 7.07).
- EGCG *P. falciparum* ENR: *J Med Chem* 2007 (CHEMBL910789 assay; pChEMBL 8.10).
- Curcumin human NLRP3: *J Nat Prod* 2020 (CHEMBL4702878 assay; pChEMBL 4.62).
- Curcumin amyloid-β: *J Med Chem* 2006 (CHEMBL907197 assay; pChEMBL 9.68).
- Curcumin DYRK2: *J Med Chem* 2023 (pChEMBL 8.60; NEW in ChEMBL v37).
- Sulforaphane iNOS: *J Med Chem* 2015 (CHEMBL3579718 assay; pChEMBL 6.40).
- Sulforaphane Nrf2/Keap1: *J Med Chem* 2019 and *Eur J Med Chem* 2020 (pChEMBL 6.06–6.24).
- Kojic acid tyrosinase: *Bioorg Med Chem Lett* 2008–2014 (multiple curated entries; pChEMBL 5.00–5.13); mushroom tyrosinase INHIBITOR 1.0 nM: *Eur J Med Chem* 2023 (NEW in ChEMBL v37).
- Ferulic acid amyloid fibril imaging: *Bioorg Med Chem Lett* 2007 (CHEMBL888360; pChEMBL 9.11, imaging probe displacement); CK2 Ki: *J Med Chem* 2023 (NEW in ChEMBL v37).
- Quercetin 5-LOX: *J Med Chem* 1991 (see [nlrp3-inhibitor-screen.md](../nlrp3-inhibitor-screen.md) 2026-04-23 appendix).
- Oridonin human NLRP3 THP-1: *Eur J Med Chem* 2023 (5.18 μM, pChEMBL 5.29); 2024 entries: *Bioorg Med Chem Lett* 2024 (% inhibition, NEW in ChEMBL v37); *J Med Chem* 2024 (NEW).
- Dapansutrile human/mouse NLRP3: *Eur J Med Chem* 2023 and *Bioorg Med Chem Lett* 2021.
- β-Caryophyllene CB2: *Eur J Med Chem* 2018 (Ki 150 nM, pChEMBL 6.82; now ChEMBL-curated; was external-literature-only at 2026-04-24 baseline).
- Ursolic acid ROR-γ: *J Med Chem* 2023 (IC50 0.75 nM, pChEMBL 9.12; NEW in ChEMBL v37).
- Ursolic acid NF-κB p65: *Bioorg Med Chem* 2018 (IC50 31 nM, pChEMBL 7.51; NEW in ChEMBL v37).
- Ursolic acid SENP1: *Eur J Med Chem* 2022 (IC50 6.4 nM, pChEMBL 8.19; NEW in ChEMBL v37).
- Theaflavin Bcl-2: *Proc Natl Acad Sci U S A* 2007 (Ki 691 nM, pChEMBL 6.16).
- Zileuton 5-LOX: *J Med Chem* 1993 (IC50 840 nM, pChEMBL 6.08; canonical ALOX5 target = CHEMBL215).
- Tranilast NPC1/Rab-9A: phenotypic screen (null journal annotation; treat as unvalidated).
- Disulfiram LOXL4: *Bioorg Med Chem Lett* 2018 (IC50 59 nM, pChEMBL 7.23).
- Vitamin D3 VDR: *Bioorg Med Chem Lett* 2014 (EC50 0.21 nM, pChEMBL 9.68).
- Spermidine CA4: *J Med Chem* 2010 (Ki 112 nM, pChEMBL 6.95).
