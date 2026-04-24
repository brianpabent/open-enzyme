---
title: "TNFSF14 (LIGHT) as a Gout Target"
date: 2026-04-24
tags: ["tnfsf14", "light", "gout", "nlrp3", "nf-kb", "il-6", "biomarker", "chokepoint-1b", "cerc-002", "avalo"]
related:
  - nlrp3-exploit-map.md
  - nlrp3-inflammasome.md
  - gout-clinical-pipeline.md
  - gout-pathophysiology.md
  - supplements-stack.md
  - nlrp3-inhibitor-screen.md
sources:
  - "Ea et al. Ann Rheum Dis 2024;83(7):945-956 (PMID: 38373842)"
  - "Perlin et al. J Clin Invest 2022;132(3):e153173 (PMID: 34871182)"
  - "Perlin et al. mSphere 2020;5(4):e00699-20 (PMID: 32817460)"
  - "Zhong et al. J Cell Mol Med 2020;24(20):11936-11948 (PMID: 32881263)"
  - "Hosokawa et al. Mol Nutr Food Res 2010;54 Suppl 2:S151-8 (PMID: 20461739)"
  - "Huang et al. Eur Rev Med Pharmacol Sci 2024;28(1):107-117 (PMID: 38235898)"
  - "Ishida et al. J Rheumatol 2008;35(6):960-8 (PMID: 18412315)"
  - "Kang et al. Arthritis Rheum 2007;56(4):1106-17 (PMID: 17393389)"
  - "Krause et al. Gastroenterology 2014;146(7):1752-62 (PMID: 24560868)"
  - "Giles et al. Front Immunol 2018;9:2585 (PMID: 30524422)"
  - "Mousa et al. Front Immunol 2025;16:1657071 (PMID: 41030453)"
  - "Herrero-Cervera et al. Diabetologia 2019;62(11):2143-2157 (PMID: 31388695)"
  - "Zuccala et al. J Genet Genomics 2021;48(6):497-507 (PMID: 34353742)"
---

# TNFSF14 (LIGHT) as a Gout Target

TNFSF14 — also known as LIGHT (homologous to lymphotoxins, inducible, competes with HSV glycoprotein D for HVEM) — is a TNF-superfamily cytokine produced by activated monocytes, macrophages, neutrophils, B cells, and T cells. Ea et al. 2024 identified it as the second-highest fold-change inflammatory biomarker in gout flare, after IL-6, across two independent cohorts. Ex vivo blockade of TNFSF14 reduced LPS+MSU-induced cytokine response. This page synthesizes the evidence for TNFSF14 as a gout-relevant therapeutic target and its placement in the NLRP3 chokepoint framework.

## 1. The seed finding (Clinical + In Vitro)

Ea et al. *Ann Rheum Dis* 2024 (PMID: 38373842) used the Olink 92-protein inflammation panel on the prospective GOUTROS cohort, sampling at three timepoints: T1 (flare), T2 (intercritical), T3 (after reaching serum urate target under urate-lowering therapy). Validation in an independent cohort (OLT1177-05 — the dapansutrile Phase 2a patients, T1 and T2 only).

- 21 proteins differentially expressed across phases
- Four elevated at flare vs. intercritical in both cohorts: IL-6, CSF1 (M-CSF), VEGF-A, **TNFSF14**
- IL-6 and TNFSF14 showed the highest fold change at T1
- TNFSF14 was **produced at the inflamed joint** (local myeloid source, not systemic spillover alone)
- Recombinant TNFSF14 **enhanced LPS+MSU ex vivo cytokine production**; **anti-TNFSF14 blockade reduced it**
- *TNFSF14* SNPs modulated myeloid cytokine output — genetic dose-response

Sample sizes and exact statistical thresholds are in the full text (not retrievable via PMC at the time of this audit — retrieve the PDF for Pass-2 quantitative extraction).

## 2. Mechanism: a parallel NF-κB amplifier, not a new sensor

No PubMed paper links TNFSF14 directly to NLRP3 assembly, ASC speck formation, caspase-1 cleavage, or gasdermin D pore formation (zero hits on "TNFSF14 NLRP3 inflammasome" or "TNFSF14 inflammasome"). TNFSF14 is not a CP2 / CP3 / CP4 / CP6 exploit.

TNFSF14 instead binds two receptors:

- **HVEM (TNFRSF14)** — on lymphocytes and myeloid cells; also binds BTLA (inhibitory) and CD160
- **LTβR (lymphotoxin β receptor)** — on stromal cells, synoviocytes, myeloid cells, epithelium; also binds LTα1β2

Downstream signaling activates **canonical NF-κB, non-canonical NF-κB (NIK/RelB), JNK/AP-1, and p38 MAPK** — the same transcription factors that generate pro-IL-1β and NLRP3 transcripts during classical LPS/DAMP priming. This places TNFSF14 squarely within **CP1 (priming)**, as a myeloid-autocrine / paracrine amplifier loop layered on top of LPS/TLR4 and DAMP/NLR priming.

- Zhong et al. 2020 *J Cell Mol Med* (PMID: 32881263): LIGHT → **TLR4-MyD88-NF-κB** axis in sepsis-associated AKI. LIGHT KO attenuates LPS injury; HVEM-Fc and LTβR-Fc rescue wild-type mice. (Animal Model + In Vitro.)
- Lai et al. 2023 *Mediators Inflamm* (PMID: 36654880): TLR3 agonist poly(I:C) induces LIGHT via NF-κB; LIGHT then amplifies NF-κB further. Classic feed-forward. Soluble HVEM ameliorates liver injury. (Animal Model.)
- Herrero-Cervera et al. *Diabetologia* 2019 (PMID: 31388695): LIGHT-deficient mice on high-fat/high-cholesterol diet have improved glucose tolerance, less hepatic steatosis, reduced systemic TNF-α and IL-6, fewer F4/80+CD11c+ pro-inflammatory adipose macrophages. (Animal Model.)

## 3. Gout-relevant cell types express both receptors

- **Fibroblast-like synoviocytes (FLS):** Ishida et al. 2008 (PMID: 18412315) — FLS from RA synovium express HVEM and LTβR; LIGHT stimulation drives MMP-9/12, IL-8, MCP-1, MIP-1α, ICAM-1 via **LTβR (not HVEM)** and NF-κB. LIGHT synovial-fluid levels are elevated in RA vs. OA. Mechanistic extrapolation to gouty synovitis: MSU deposits activate the same synovial tissue, and the same ligand–receptor system is present.
- **Osteoclastogenesis:** Ishida et al. 2008 *Immunology* (PMID: 19019090) — LIGHT promotes osteoclast differentiation from CD14+ monocytes co-cultured with synovial nurse-like cells, synergizing with RANKL. Relevant to long-term joint damage in chronic tophaceous gout.
- **B cells + monocytes:** Kang et al. 2007 *Arthritis Rheum* (PMID: 17393389) — in RA, LIGHT is upregulated on CD20+ B cells and monocytes. Produced centrally by both innate and adaptive arms.
- **Myeloid cells in colitis:** Krause et al. 2014 *Gastroenterology* (PMID: 24560868); Giles et al. 2018 *Front Immunol* (PMID: 30524422) — LIGHT signaling through **LTβR** drives both inflammation and resolution context-dependently. Full KO worsens colitis. **This is a caution flag for total-body blockade.**
- **Psoriatic keratinocytes:** Ye et al. 2026 (PMID: 41684072) — HaCaT cells express HVEM and LTβR; LIGHT drives IL-6, IL-8, PGI2, PTGS2 via JNK/AP-1-HVEM-LIGHT pathway. Extends the cell-type reach.

## 4. Therapeutic landscape

### Clinical

- **CERC-002 (Avalo Therapeutics, formerly Cerecor):** humanized anti-LIGHT mAb. Phase 2 RCT in COVID-19 ARDS (NCT04412057, N=83), *J Clin Invest* 2022 (PMID: 34871182). 83.9% (CERC-002) vs. 64.5% (placebo) alive and respiratory-failure-free at day 28 (p=0.044); mortality 7.7% vs. 14.3%. **Clinical Trial — positive Phase 2 in a different indication.** No gout trial on record. Avalo has pursued CERC-002 in additional indications including pyoderma gangrenosum, GvHD, and IBD. Joosten's Radboud group co-authored Ea 2024 *and* the dapansutrile Phase 2a — they have the gout cohorts and the relationship with the NLRP3-ARDS clinical world.
- **Historical LTβR fusion protein:** baminercept (Biogen) — LTβR-Fc, tested in RA (did not meet primary endpoint) and Sjögren's. Programs paused. Preclinical utility still demonstrated (Zhong 2020 with LTβR-Fc rescue).

### Natural compounds with published direct TNFSF14 activity

- **EGCG, ECG, theaflavin-3,3'-digallate (green and black tea polyphenols):** Hosokawa et al. 2010 *Mol Nutr Food Res* (PMID: 20461739) — suppress TNFSF14-induced IL-6 in human gingival fibroblasts; block TNFSF14-driven ERK/JNK/NF-κB activation; **downregulate TNFSF14 receptor expression** on target cells. In Vitro. This is the only published direct-modulation data for any compound currently in the Open Enzyme supplement stack. Upgrades EGCG's chokepoint profile from CP1/CP4/CP5 to CP1b-direct + CP1/CP4/CP5.
- **DHA (omega-3):** Huang et al. 2024 (PMID: 38235898) — Mendelian-randomization evidence that DHA levels negatively associate with circulating TNFSF14 (OR 0.933, p=0.022); TNFSF14 positively associates with atopic dermatitis risk. **Human genetic / Mechanistic Extrapolation.** Suggests systemic DHA intake lowers serum LIGHT.
- **Vitamin D:** Faienza et al. 2023 (PMID: 36917420) — inverse correlation of serum LIGHT with 25(OH)D in Prader-Willi. Observational / correlational. Mechanistic Extrapolation.
- **Liraglutide (GLP-1):** Grannes et al. 2024 (PMID: 38685051) — significantly reduces circulating LIGHT after 16 weeks of treatment in obese/T2D vs. matched-weight-loss lifestyle controls. Clinical Trial. Not in the stack but relevant for metabolic-gout comorbidity.

### No direct TNFSF14 data for

Curcumin, resveratrol, berberine, sulforaphane, oridonin, andrographolide, parthenolide, quercetin, spermidine, trehalose, MitoQ, NAC, colchicine, BHB, KPV, BPC-157, TB-500. All are plausible indirect modulators (via NF-κB suppression, which would reduce *TNFSF14* transcription and LIGHT-driven NF-κB output simultaneously), but published direct data are absent. This is a testable screening gap.

## 5. Genetics

Zuccala et al. 2021 *J Genet Genomics* (PMID: 34353742) — fine-mapping in Italian multiple sclerosis shows the intronic SNP **rs1077667** is the primary MS-associated TNFSF14 variant, with the risk allele driving reduced *TNFSF14* mRNA in blood cells but increased LIGHT+ myeloid DCs. Relevant as proof that TNFSF14 expression is under polymorphic control in humans and that reduced expression is disease-relevant. The Ea paper's SNP observations in gout flare are consistent with this functional genetics.

## 6. Placement in the NLRP3 Exploit Map

TNFSF14 is added to **Chokepoint 1 as sub-branch CP1b** — a myeloid amplifier loop alongside CP1a (LPS/DAMP/TLR priming). It does **not** justify a new CP0 (there is nothing upstream of CP1a that TNFSF14 attacks), nor a fully parallel cascade (its signaling collapses into NF-κB, the existing CP1 target).

Accessible intervention ranking:

1. **EGCG (stack)** — in vitro direct receptor and IL-6 suppression. Cheap, already in stack.
2. **DHA/EPA omega-3 (stack)** — human-genetic association with lower LIGHT.
3. **CERC-002** — phase-2-positive in ARDS; requires investigator-initiated trial or compassionate use to reach a gout patient. Not realistic for the current phase of Open Enzyme.
4. **Screen the rest of the stack against TNFSF14-driven IL-6 in a simple HGF or THP-1 assay** — low cost, high information value. Any NF-κB blocker that also suppresses TNFSF14-driven output picks up a free CP1b justification.

## 7. Safety caveat

LIGHT has dual pro-inflammatory and resolution roles. Krause 2014 (PMID: 24560868) and Giles 2018 (PMID: 30524422) show LIGHT-null mice have **worse** DSS colitis — LIGHT is required for resolution of intestinal inflammation. Mousa 2025 review (PMID: 41030453) frames this as dual-receptor biology: HVEM engagement can be regulatory (via BTLA), LTβR engagement is the pro-inflammatory/pro-fibrotic arm. Implication: total systemic TNFSF14 blockade may trade gout-flare suppression for impaired gut/colitis resolution. Episodic flare-phase blockade or receptor-selective (LTβR-biased) inhibition is the safer design space.

## 8. Open questions / next actions

- Retrieve the Ea 2024 PDF and extract N per cohort, statistical thresholds, and the myeloid cell subset identified as the joint-local TNFSF14 source.
- Screen the existing Open Enzyme supplement stack against TNFSF14-driven IL-6 in a human macrophage (THP-1) or synoviocyte assay. One plate, 10 compounds, clear readout.
- Contact Joosten / Radboud group (already connected via dapansutrile Phase 2a sample set) — they have the cohort infrastructure to test CERC-002 or any upstream compound against gout flare cytokines.
- Update [nlrp3-exploit-map.md](./nlrp3-exploit-map.md), [nlrp3-inflammasome.md](./nlrp3-inflammasome.md), [gout-pathophysiology.md](./gout-pathophysiology.md), [supplements-stack.md](./supplements-stack.md) (EGCG/omega-3 CP1b annotation), and [GRAPH.md](./GRAPH.md) (new TNFSF14 → HVEM/LTβR → NF-κB → priming edges).
