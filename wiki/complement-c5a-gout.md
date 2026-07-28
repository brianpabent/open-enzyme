---
title: "Complement C5a as an NLRP3 Priming Route in Gout (CP0)"
date: 2026-04-24
tags:
  - complement
  - c5a
  - c5ar1
  - c5ar2
  - c3a
  - membrane-attack-complex
  - gout
  - nlrp3
  - priming
  - chokepoint-0
  - avacopan
  - vilobelimab
  - zilucoplan
  - eculizumab
  - iptacopan
  - msu
related:
  - nlrp3-exploit-map.md
  - nlrp3-inflammasome.md
  - gout-pathophysiology.md
  - gout-deep-dive.md
  - gout-clinical-pipeline.md
  - tnfsf14-gout-target.md
  - etc/open-enzyme-vision.md
  - spm-resolution-pathway.md
  - supplements-stack.md
  - self-experiment-protocol.md
  - open-questions.md
sources:
  - "Cumpelik A, Ankli B, Zecher D, Schifferli JA. Ann Rheum Dis 2016;75(6):1236-45 (PMID: 26245757)"
  - "Khameneh HJ, Ho AWS, Laudisi F, et al. Front Pharmacol 2017;8:10 (PMID: 28167912)"
  - "An LL, Mehta P, Xu L, et al. Eur J Immunol 2014;44(12):3669-79 (PMID: 25229885)"
  - "Wessig AK, Hoffmeister L, Klingberg A, et al. Sci Rep 2022;12(1):4483 (PMID: 35296708)"
  - "Russell IJ, Mansen C, Kolb LM, Kolb WP. Clin Immunol Immunopathol 1982;24(2):239-50 (PMID: 6749358)"
  - "Doherty M, Richards N, Hornby J, Powell R. Ann Rheum Dis 1988;47(3):190-7 (PMID: 2833185)"
  - "Jayne DRW, Merkel PA, Schall TJ, Bekker P. N Engl J Med 2021;384(7):599-609 (PMID: 33596356)"
  - "Liu H, Kim HR, Deepak RNVK, et al. Nat Struct Mol Biol 2018;25(6):472-481 (PMID: 29867214)"
  - "Vlaar APJ, Witzenrath M, van Paassen P, et al. Lancet Respir Med 2022;10(12):1137-1146 (PMID: 36087611)"
  - "Howard JF Jr, Bresch S, Genge A, et al. Lancet Neurol 2023;22(5):395-406 (PMID: 37059508)"
  - "Avacopan (Tavneos) FDA approval label, 2021 (ANCA-associated vasculitis)"
  - "Zaninelli TH, Fattori V, Verri WA Jr. Expert Opin Ther Targets 2023;27(8):751-766 (PMID: 37651647)"
  - "Schauer C, Janko C, Munoz LE, et al. Nat Med 2014;20(5):511-7 (PMID: 24784231)"
  - "Takeda J, Miyata T, Kawagoe K, et al. Cell 1993;73(4):703-11 (PMID: 8500164)"
  - "Laine M, Jarva H, Seitsonen S, et al. J Immunol 2007;178(6):3831-6 (PMID: 17339482)"
  - "Schaumberg DA, Christen WG, Kozlowski P, et al. Arch Ophthalmol 2006;124(11):1530-5 (PMID: 16723442)"
  - "Sahu A, Rawal N, Pangburn MK. Biochem Pharmacol 1999;57(12):1439-46 (PMID: 10353266)"
  - "Zhang T, Chen DF. J Ethnopharmacol 2008;117(2):351-361 (PMID: 18400428; PMC7126446)"
  - "Lu Y, Liu X, Liang X, et al. Acta Pharm Sin B 2018;8(2):218-227 (PMID: 29719782; PMC5925397)"
  - "Yin X, Huang A, Zhang S, et al. Molecules 2016;21(11):1506 (PMID: 27834928; PMC6273495)"
status: published
---

# Complement C5a as a Gout NLRP3 Priming Route

**Chokepoint 0** in the [NLRP3 exploit map](./nlrp3-exploit-map.md). MSU-associated complement activation and C5aR1 signaling provide a demonstrated route into inflammasome priming in human-cell and animal systems. Whether this route dominates other priming inputs across human gout flares is unresolved.

> **Current CP0 status:** The retained legacy searches are not a reproducible
> census and support no direct-natural-product C5aR1 retrieval or absence claim.
> Upstream complement candidates exist at C3 convertase and pathway-entry nodes.
> A direct functional screen is the shortest route to test exact C5aR1 leads.
>
> **Engineered-regulator status:** [comp-012](./daf-cd55-scr14-truncated-computational.md) supplies a sequence-filter/pLDDT proxy for truncated DAF SCR1-4 (aa 35–285), not a protease-risk result. Expression, eight-disulfide folding, processing stability, retained regulatory activity, and access to the relevant complement compartment require wet-lab validation under [§1.25](./validation-experiments.md).
>
> **Dietary-regulator status:** Rosmarinic acid, luteolin, *Houttuynia cordata* polysaccharides, and related upstream candidates have mechanism evidence but large assay-format, structure, exposure, and translation uncertainties. They are research leads, not recommendations.
>
> Falsification card: [H05 — DAF SCR1-4 CP0 thesis](./hypotheses/H05-daf-scr14-cp0-thesis.md).

**Scope:** mechanism primer (complement cascade → crystal activation → C5a → priming), receptor biology (C5aR1 / C5aR2 / C3aR), cell-type effects in gout flares, genetics, the full therapeutic landscape (approved drugs, research compounds, natural products), combination biology versus LPS priming, portfolio implications, clinical biomarkers, and open research questions.

---

## 1. Complement Cascade Primer

Complement is the soluble effector arm of innate immunity — a self-assembling proteolytic cascade of ~30 proteins that opsonizes pathogens, recruits phagocytes, and lyses membranes. It is old (evolved before adaptive immunity), fast (seconds-to-minutes kinetics), and dangerously promiscuous when mis-regulated. Gout exploits it.

> **Reactome graph anchor:** Reactome already models the canonical complement machinery: `R-HSA-166658` Complement cascade, `R-HSA-173623` classical antibody-mediated complement activation, `R-HSA-173736` alternative complement activation, `R-HSA-166665` terminal pathway of complement, `R-HSA-375395` C5a receptor binding C5a, `R-HSA-9957423` C5AR1 antagonist binding, and `R-HSA-977371` Factor I inactivation of Factor H-bound C3b. The gout-specific claim on this page is narrower: MSU/CRP/IgM surfaces drive this machinery in the joint. That disease-context edge remains anchored to the primary gout/complement literature rather than Reactome itself. (Pathway anchor; source: `reference/generated/reactome/2026-06-01-open-enzyme-audit/`)

### Three activation pathways, one convergence point

```text
Classical         Lectin           Alternative
  |                 |                  |
  C1q binds        MBL binds         "Tick-over" +
  IgM/IgG          carbohydrates     surface C3b
  or charged       (fungal mannose,  deposition
  surfaces         bacterial)
  |                 |                  |
  C1r/s             MASP-1/2           Factor B +
  |                 |                  Factor D
  ▼                 ▼                  ▼
  C4 + C2 → C4b2a (classical/lectin C3 convertase)
                      \      |      /
                       \     |     /
                   C3b deposits, amplifies via
                   alternative pathway (C3bBb)
                              |
                              ▼
                    C5 convertase (C4b2a3b or C3bBbC3b)
                              |
                ┌─────────────┼─────────────┐
                ▼             ▼             ▼
              C5a            C5b ──► C5b-9 (MAC)
         (anaphylatoxin)         (pore on target membrane)

        Opsonization:    C3b, iC3b
        Anaphylatoxins:  C3a, C5a
        Lytic effector:  C5b-9 (MAC)
```

- **Classical pathway.** Triggered by C1q binding to IgM or clustered IgG Fc on a target surface, or by direct binding to charged surfaces (including MSU crystals — see §2). C1q binding activates C1r and C1s, which cleave C4 and C2 to form the C4b2a C3 convertase.
- **Lectin pathway.** Triggered by mannose-binding lectin (MBL) or ficolins recognizing microbial carbohydrate patterns, activating MASP-1 and MASP-2 (analogs of C1r/s). Converges on the same C4b2a convertase.
- **Alternative pathway.** Constitutively idling via spontaneous "tick-over" hydrolysis of C3 → C3(H₂O), which binds Factor B; Factor D cleaves B → Ba + Bb; C3(H₂O)Bb is a fluid-phase C3 convertase. If C3b deposits on a non-protected surface, it recruits Factor B → Bb and forms the surface-bound C3bBb convertase, creating a positive-feedback amplification loop. This is the pathway that iptacopan blocks.

All three converge on **C3 convertases** that cleave C3 → C3a (anaphylatoxin, diffuses away) + C3b (opsonin, deposits). When enough C3b accumulates on a surface, a **C5 convertase** assembles (C4b2a3b classical/lectin, C3bBbC3b alternative) and cleaves C5 → **C5a** (anaphylatoxin) + **C5b** (nucleus of the membrane attack complex).

### Downstream effectors

- **C3a, C5a — anaphylatoxins.** Small proteolytic fragments of C3 and C5. They bind C3aR, C5aR1, and, for C5a, C5aR2. C5a is a strong neutrophil chemoattractant and activator; exact potency depends on receptor, cell system, species, and assay.
- **C5b-9 — Membrane Attack Complex (MAC).** C5b nucleates assembly of C6, C7, C8, and multiple C9 molecules into a transmembrane pore. On pathogens and (erroneously) host cells, MAC causes osmotic lysis. At sublytic concentrations (insufficient pore density for lysis), MAC on leukocytes and stromal cells drives calcium influx, NF-κB activation, inflammasome priming, and cytokine release. Sublytic MAC is increasingly recognized as an inflammatory driver in its own right.

### Regulators — why healthy tissue does not lyse itself

Complement activation would destroy host cells were it not tightly regulated at every step:

| Regulator | Site | Action |
|-----------|------|--------|
| **C1-INH** | Fluid phase | Dissociates C1r/C1s and MASPs from C1q/MBL |
| **Factor H (CFH)** | Fluid phase + surface (host sialic acid / GAGs) | Cofactor for Factor I cleavage of C3b → iC3b; accelerates decay of C3bBb |
| **Factor I** | Fluid phase | Protease that cleaves C3b and C4b with appropriate cofactor |
| **DAF (CD55)** | Host cell surface | Accelerates decay of both C3 and C5 convertases |
| **MCP (CD46)** | Host cell surface | Cofactor for Factor I cleavage of C3b/C4b on host cells |
| **CD59 (protectin)** | Host cell surface | Blocks C9 polymerization → prevents MAC pore formation |
| **C4BP** | Fluid phase | Regulates classical C4b2a convertase |

PNH usually begins with an acquired somatic *PIGA* mutation in a hematopoietic stem-cell clone. Loss of GPI-anchor biosynthesis then removes multiple GPI-anchored proteins from descendant blood cells, including CD55 and CD59; their absence makes erythrocytes vulnerable to complement-mediated hemolysis (PMID 8500164; **Human molecular evidence**). Factor H deficiency causes atypical hemolytic uremic syndrome (aHUS) and is strongly associated with age-related macular degeneration (AMD). These systemic complement-dysregulation diseases supplied clinical precedents for complement-targeted drugs. Gout instead presents a candidate local-overactivation problem, so their treatment results do not select a gout target, product, or exposure.

### Kinetics and half-lives — relevant for measurement and drug design

- **C5a** is generated rapidly after complement activation. In serum, carboxypeptidase N removes the C-terminal arginine to form **C5a-desArg**, which has different receptor potency and persistence. Assays may conflate the forms, so a biomarker record must specify analyte and matrix before it is compared with tissue signaling.
- **C3a** is also clipped by CPN to C3a-desArg (ASP, acylation-stimulating protein), which loses anaphylatoxin activity but retains metabolic signaling via C5L2/C5aR2. This is one reason C5aR2 biology is confusing — it binds both C5a and C3a-desArg.
- **C5b-9 (MAC)** is slower to assemble (~minutes) but persists on membranes for hours once inserted. Soluble sC5b-9 (shed from membranes) is a stable plasma biomarker of MAC activation.

(Evidence level: In Vitro — standard complement biochemistry, well-established since the 1970s-80s.)

---

## 2. MSU Crystal → Complement Activation

Monosodium urate crystals are exceptional among danger signals: they activate complement **directly and potently**, without requiring PAMPs, antibodies, or adjuvants. This is the foundational observation on which CP0 rests.

### 2.1 The 1982 seed paper

According to PubMed, Russell, Mansen, Kolb, and Kolb ([*Clin Immunol Immunopathol* 1982;24(2):239-50](https://doi.org/10.1016/0090-1229(82)90235-5), PMID 6749358) demonstrated that **MSU crystals directly activate human C5 by assembling a C5 convertase on the crystal surface**. Using purified human complement components, they showed that MSU crystals:

- Bound C3b and sustained alternative-pathway C5 convertase assembly (C3bBbC3b) on the crystal surface
- Generated the chemotactic fragment (later named C5a) in a C5-dependent manner
- Did not require antibody for activation, though classical-pathway engagement occurred when antibody was present

This was the first demonstration that a sterile crystalline danger signal could engage complement convertases on its own surface. The authors connected this to the known chemotactic / neutrophil-attracting activity of synovial fluid from acute gouty joints.

### 2.2 Classical pathway — IgM and CRP drive most of it

According to PubMed, the 2022 Wessig et al. paper ([*Sci Rep* 2022;12(1):4483](https://doi.org/10.1038/s41598-022-08311-z), PMID 35296708) dissected the molecular recognition events. Key findings:

- **Wessig et al. reported natural IgM binding to MSU crystals in the human samples they tested.** This is compatible with constitutive polyreactive “natural antibody,” but the experiment does not justify a universal claim about every healthy person or fetus.
- **CRP (C-reactive protein) binds MSU crystals** and fixes active C1 complex more efficiently than IgM does.
- **In serum depleted of both IgM and CRP, MSU complement activation is negligible.** IgM and CRP are **both** required to efficiently drive classical-pathway C1 activation on MSU surfaces.
- **CRP is more efficient than IgM at generating C5a** (the most pro-inflammatory anaphylatoxin), suggesting non-redundant functions — CRP binding may orient C1 to favor downstream C5 convertase assembly.
- **CRP does not bind the related CPPD (calcium pyrophosphate dihydrate) crystals of pseudogout, but IgM does.** This differential recognition helps explain why pseudogout and gout have subtly different complement signatures (Doherty 1988, below).

**Mechanistic implication for gout:** In the acute flare, the patient's baseline CRP (elevated in hyperuricemia, metabolic syndrome, and aging) plus constitutive IgM binds crystals → C1q → C4b2a classical convertase → C3b deposition → alternative-pathway amplification (C3bBb) → C5 convertase → C5a. The classical pathway initiates; the alternative pathway amplifies.

(Evidence level: In Vitro — purified serum + complement-depleted sera; IgM/CRP reconstitution experiments.)

### 2.3 Alternative pathway — surface amplification

MSU crystal surfaces also permit direct alternative-pathway engagement independent of IgM/CRP. Spontaneous fluid-phase C3 tick-over continuously deposits trace C3b; on MSU crystals, C3b is not efficiently inactivated by Factor H/I because MSU lacks the host-surface sialic acid and GAG patterns that recruit Factor H. The result is a positive-feedback amplification loop: more C3bBb convertase → more C3b → more convertase. This is the same logic that makes the alternative pathway dangerous on any non-host surface (bacteria, biomaterials, artificial membranes).

### 2.4 Doherty 1988 — in vivo evidence from patient synovial fluid

According to PubMed, Doherty et al. ([*Ann Rheum Dis* 1988;47(3):190-7](https://doi.org/10.1136/ard.47.3.190), PMID 2833185) measured C3 degradation products (C3dg/d, indicative of local C3 activation) in 288 synovial fluid samples across RA, OA, chronic pyrophosphate arthropathy, and **acute pseudogout**. Key finding for this page: **every acute pseudogout sample had strikingly elevated synovial fluid C3dg/d** (mean 61 units/mL, range 16-126), with local activation confirmed by plasma-to-synovial-fluid discordance. The acute pseudogout signal was similar in magnitude to active RA. Chronic pyrophosphate arthropathy (non-flaring) had much lower C3dg/d. This is **Human Observational evidence in CPPD**, not MSU gout. Russell 1982 separately supplies **In Vitro MSU evidence**; transferring the joint-level CPPD observation to gout is a **Mechanistic Extrapolation**. The present sources do not establish a matched human-gout synovial C3a/C5a/sC5b-9 dataset.

(Evidence level: **Human Observational** — CPPD synovial-fluid biomarker study.)

### 2.5 C5a generation timeline in murine MSU peritonitis

According to PubMed, Cumpelik et al. ([*Ann Rheum Dis* 2016;75(6):1236-45](https://doi.org/10.1136/annrheumdis-2015-207338), PMID 26245757) used a murine MSU peritonitis model with wild-type and mice reported by the paper as C5aR⁻/⁻ to track the kinetics:

- MSU injection → **C5a detectable in peritoneal lavage within 30-60 minutes**
- C5a precedes and is required for NLRP3-dependent IL-1β release
- Genetic loss of the receptor reported as C5aR markedly reduced IL-1β and neutrophil influx in that model
- Neutrophil-derived phosphatidylserine-positive microvesicles (PMN-Ecto) accumulate over hours and *terminate* C5a-mediated priming — an endogenous resolution brake via MerTK engagement

The rapid complement response is compatible with early flare biology. That timing does not exclude pre-existing or concurrent transcriptional priming through TLR4, TNFSF14, or other inputs.

### 2.6 Relative contribution of initiation and amplification

In the Wessig 2022 MSU-surface system, natural antibodies and CRP supported classical-pathway initiation, while the alternative pathway could amplify deposited C3b. How these contributions vary across human joints, flare stages, and patient phenotypes is not established. Factor-H variation and baseline inflammatory state are testable modifiers, not demonstrated gout stratifiers.

---

## 3. C5a, C3a, and MAC — Functional Roles in Gout

The anaphylatoxins and MAC are not interchangeable. C5a has the clearest direct priming evidence in the cited MSU systems; the relative human-gout contributions of C3a and MAC remain incompletely measured.

### 3.1 C5a — a demonstrated priming signal

According to PubMed, An et al. ([*Eur J Immunol* 2014;44(12):3669-79](https://doi.org/10.1002/eji.201444560), PMID 25229885) — **the direct mechanistic study of C5a + MSU in human monocytes**. This paper complements Khameneh 2017 (murine) and should be cited alongside it as the human-cell counterpart. Key findings in human whole blood and primary monocytes:

- In the study's defined **In Vitro** human whole-blood system, C5aR1 perturbation indicated a large C5a contribution to the measured MSU-induced cytokine/chemokine response; this does not establish dominance across human gout flares
- C5a alone induces pro-IL-1β and IL-1β in human primary monocytes
- C5a + MSU is **synergistic for IL-1β**, not merely additive
- C5a priming is caspase-1-dependent, K⁺-efflux-dependent, Ca²⁺-mobilization-dependent, and cathepsin B-dependent
- Authors propose C5a as a therapeutic target **in combination with IL-1β antagonists** for gout

According to PubMed, Khameneh et al. ([*Front Pharmacol* 2017;8:10](https://doi.org/10.3389/fphar.2017.00010), PMID 28167912) — murine MSU peritonitis:

- C5a, not C3a, potentiates IL-1β/IL-1α release from LPS-primed, MSU-exposed peritoneal macrophages and human monocytic cells
- MSU-induced C5a mediates murine neutrophil recruitment and joint-local IL-1β production
- **C5aR antagonism ameliorates MSU peritonitis** — pharmacologic validation
- Mechanism: C5a increases NLRP3 inflammasome activation via **ROS** production, **not** via transcriptional upregulation of inflammasome components. This is the non-transcriptional priming axis — the defining feature of CP0 distinct from CP1a (NF-κB transcriptional priming).

**Putting these two papers together — the CP0 story:**

1. MSU crystals directly activate complement on their surface (Russell 1982, Wessig 2022)
2. C5a is generated within minutes, before any NF-κB transcriptional program can ramp up (Cumpelik 2016)
3. C5a binds C5aR1 on tissue-resident macrophages and infiltrating neutrophils (An 2014, Khameneh 2017)
4. C5aR1 signaling was associated with increased cellular ROS and greater NLRP3 output in the tested macrophage system; Khameneh 2017 did not identify the ROS-generating enzyme
5. Primed NLRP3 now responds to the crystal itself (K⁺ efflux, lysosomal rupture, mtROS — CP2) to assemble the inflammasome and release IL-1β (An 2014; the full cascade)

The mechanistic implication is narrower: **C5a can provide a rapid, non-transcriptional priming route in the tested systems.** This explains a route by which complement can contribute early in a flare; it does not show that LPS/TLR4 or other priming inputs are absent or clinically subordinate.

### 3.2 C3a — the supporting actor

C3a binds C3aR (also a GPCR, Gi-coupled, on mast cells, basophils, macrophages, and some neurons). In the Khameneh 2017 experiments, **C3a did not potentiate IL-1β release from MSU-exposed cells** — only C5a did. That result distinguishes C5a from C3a in the tested system; it does not establish their relative contributions in every human flare. C3a has reported roles in:

- **Mast cell degranulation** — C3a is a more potent mast cell activator than C5a in some assays; mast cells are present in synovium and contribute to early flare histamine/tryptase release
- **Basophil activation** — systemic
- **Regulatory T cell biology** — C3a/C3aR signaling influences Treg function in non-gout contexts
- **Metabolic signaling via C3a-desArg / ASP** on C5L2

For gout specifically, C3a is a possible additional signal whose magnitude relative to C5a has not been established in matched human-flare samples.

### 3.3 C5b-9 (Membrane Attack Complex) — sublytic amplifier

Sublytic MAC deposition on leukocytes and synoviocytes drives:

- Calcium influx through the pore
- NF-κB activation (inflammatory transcriptional program)
- NLRP3 priming (some literature implicates sublytic MAC as a Signal 1 in its own right)
- Cytokine release (IL-1β, IL-6, IL-8)
- On synoviocytes: **MMP release** (tissue destruction in chronic gout / tophaceous joints)

The MAC contribution in gout has been under-studied. A matched comparison of C5a and sC5b-9 in human flare samples is needed. **Mechanistic Extrapolation:** C5 blockade removes both C5a and MAC generation, whereas C5aR1 antagonism isolates one receptor arm; paired perturbations could separate those effects in a gout-relevant assay.

### 3.4 Missing human comparison

The page does not have a source-verified, matched human-gout dataset that compares C3a, C5a, and sC5b-9 across the same synovial-fluid and plasma samples. Cross-study concentration ranges are not interchangeable because pre-analytics, matrices, timing, and assays differ. The discriminating observation is a paired flare study with cold-chain-controlled split-product measurements and matched clinical timing.

---

## 4. Receptor Biology

### 4.1 C5aR1 (CD88) — the main effector receptor

**Gene:** C5AR1 (HGNC:1338, chromosome 19q13.3-q13.4). **Protein:** 350 aa, 7-transmembrane class A GPCR (rhodopsin family, anaphylatoxin receptor subfamily IPR002234). **ChEMBL target:** [CHEMBL2373](https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2373) (SINGLE PROTEIN, Homo sapiens, UniProt P21730).

**Expression:** Neutrophils (high), monocytes/macrophages, mast cells, basophils, eosinophils, dendritic cells, hepatocytes, lung and renal epithelium, astrocytes/microglia, vascular endothelium (low but inducible), fibroblast-like synoviocytes, osteoclast precursors. Essentially every innate immune cell and many stromal cells.

**G-protein coupling:** Primarily **Gαi** (inhibits cAMP, activates PI3K/AKT, ERK1/2) and **Gαq/11** (activates PLCβ → IP3 + DAG → calcium mobilization + PKC). The calcium flux and ERK activation are the dominant signals; cAMP inhibition is less critical.

**Downstream of C5aR1 engagement (the full signaling tree):**

- **Cellular ROS increase** — Khameneh 2017 measured a C5a-associated H2DCFDA signal and greater NLRP3 output; it did not attribute that signal to NOX2 or another ROS-generating enzyme
- **Calcium mobilization** via PLCβ — feeds into Ca²⁺-dependent NLRP3 activation
- **ERK1/2 MAPK** — amplifies inflammatory transcription
- **PI3K/AKT** — survival and chemotactic signaling
- **Actin remodeling** → chemotaxis along a C5a concentration gradient
- **Degranulation** (neutrophils release MPO, elastase, lactoferrin)
- **Upregulation of adhesion molecules** (Mac-1/CD11b on neutrophils; P-selectin/ICAM-1 on endothelium)

**β-arrestin recruitment** follows agonism and contributes to receptor
internalization and desensitization. Ligand-specific signaling bias is
assay-dependent and should not be converted into a safety explanation without
a matched pharmacology and clinical source.

**Structural biology.** According to PubMed, Liu et al. ([*Nat Struct Mol Biol* 2018;25(6):472-481](https://doi.org/10.1038/s41594-018-0067-z), PMID 29867214) solved crystal structures of human C5aR1 in ternary complex with **PMX-53** (orthosteric peptide antagonist) and with **avacopan** or **NDT-9513727** (non-peptide allosteric antagonists). Key findings:

- PMX-53 binds the **orthosteric pocket** where C5a's C-terminus normally docks — direct competition
- **Avacopan and NDT-9513727 bind allosterically** in different poses from
  orthosteric PMX-53.
- The structures establish orthosteric and allosteric C5aR1 druggability; exact
  contact maps must remain ligand-specific.

Known PDB structures: 5O9H, 6C1Q, 6C1R, 7Y64-7Y67, 8GO8, 8GOO, 8HK5, 8I0N, 8I0Z, 8IA2, 8JZP, 8JZZ.

**Gout-relevant polymorphisms.** The source set reviewed for this page did not provide a source-pinned gout association for C5AR1, C5AR2, or C3AR1. That bounded result is not a universal GWAS absence and does not predict effect size or phenotype. A reproducible search must define the GWAS catalog, ancestry, phenotype, variant/gene window, query, and retrieval date before a genetics experiment is prioritized.

### 4.2 C5aR2 (C5L2) — the enigmatic second receptor

**Gene:** C5AR2 (HGNC:4527, chromosome 19q13.32 — adjacent to C5AR1). **Protein:** 337 aa, 7-transmembrane topology but with two substitutions (DRY → DLC motif) that prevent canonical G-protein coupling. **ChEMBL target:** [CHEMBL3713] (within the CHEMBL4523605 heterodimer record).

**Ligands reported in the receptor literature include C5a, C5a-desArg, and C3a-desArg / ASP.** Relative affinity and signaling direction vary with assay and context; this page does not use an affinity ordering as a gout premise.

**Signaling:** Non-G-protein-coupled; engages β-arrestin and scaffolds. Literature is split on whether C5aR2 is:

1. A **decoy receptor** that sequesters C5a and dampens C5aR1 signaling (pro-resolution)
2. A **pro-inflammatory signaling receptor** in its own right, driving distinct cytokine programs
3. A **modulator** of C5aR1 signaling via heterodimerization (both receptors physically associate on the plasma membrane)

In gout specifically, C5aR2's role has not been dissected. **For CP0 experimental design, this is an open branch.** A C5aR1-selective perturbation leaves C5aR2 unperturbed, whereas ligand- or C5-level perturbation changes both receptor arms. A matched comparison can therefore test whether a residual C5a-dependent signal remains after C5aR1 blockade without presuming the direction of C5aR2 signaling.

### 4.3 C3aR — the C3a receptor

**Gene:** C3AR1. **Protein:** 482 aa, 7-TM class A GPCR, Gαi-coupled, with long extracellular loops. **Expression:** Mast cells (high), basophils, eosinophils, neutrophils, monocytes/macrophages (moderate), brain microglia and astrocytes, adipocytes.

**Gout relevance:** Weaker than C5aR1 per the Khameneh 2017 data (no IL-1β potentiation by C3a). Possibly relevant via mast-cell histamine/tryptase release in early flare vascular permeability.

**Clinical targeting:** SB 290157 and other C3aR tools are research comparators whose exact selectivity and off-target behavior must be taken from the primary assay. Regulatory or development status is outside this mechanism claim and requires a dated primary-record refresh.

### 4.4 Structural implications for drug design

Liu 2018 demonstrates two separable C5aR1 intervention geometries:
orthosteric peptide antagonism and ligand-specific non-peptide allosteric
antagonism. That structural result supports designing matched receptor assays;
it does not by itself establish selectivity, resistance risk, oral exposure, or
clinical safety for a new molecule.

**Natural-product implication:** The bounded legacy searches retained on this project contain pathway-level natural-product assays but no validated direct natural-product C5aR1 antagonist. They were not an exhaustive or source-pinned census and cannot establish how thoroughly the broader field has searched this target. A direct functional screen therefore remains an open discovery experiment (§9.4), not a response to a proven field-wide absence.

---

## 5. Cell Biology of C5a in a Gout Flare

C5a does not act on one cell type — it orchestrates the early-flare cellular storm through coordinated effects on myeloid cells, endothelium, and stroma.

### 5.1 Neutrophil chemotaxis — the first wave

C5a is a strong neutrophil chemoattractant; its concentration-response and relative potency depend on the assay and biological context. In a gout flare:

1. MSU crystals in the joint activate complement (minutes)
2. C5a diffuses into local microvasculature (diffusion-limited, ~minutes)
3. Endothelium responds to C5a (see §5.4) — upregulates P-selectin, ICAM-1
4. Circulating neutrophils tether, roll, adhere on activated endothelium
5. Neutrophils transmigrate into the synovium, following the C5a gradient to the crystal-rich tissue
6. Once in the tissue, neutrophils encounter crystal directly — phagocytose, activate their own NLRP3 (crystal engulfment → lysosomal rupture → K⁺ efflux → CP2)
7. Activated neutrophils release more C5a (via serine proteases acting on C5) and IL-8 — amplification loop

This route can contribute to the rapid neutrophil-rich infiltrate in gout. C5aR1- and C5-level perturbations are therefore useful mechanistic tests; no cited evidence shows that either aborts a human gout flare.

### 5.2 Macrophage priming — the CP0 mechanism

An 2014 and Khameneh 2017 show that C5a can act through C5aR1 and ROS to increase MSU-associated inflammasome output in their human-cell and murine systems. Resting macrophages require an adequate priming state for a robust response, but those studies do not establish that complement supplies that priming in every context or that C5a is necessary across human flares.

### 5.3 Non-myeloid compartments remain open

The current gout-specific source set does not establish how much C5aR1 signaling in synoviocytes, endothelium, mast cells, platelets, or osteoclast-lineage cells contributes to flare initiation or chronic joint damage. Preserve these as separate questions rather than importing detailed mechanisms from rheumatoid arthritis, vascular inflammation, or other contexts.

The cheapest useful gate is a compartment-matched perturbation: expose the relevant human cell system to MSU-conditioned complement or defined C5a, compare C5aR1-, ligand-, and C5-level controls, and measure target-proximal signaling before downstream cytokines, permeability, adhesion, or resorption. A positive result would establish only the tested cell system and exposure.

---

## 6. Genetics and Clinical Heterogeneity

This section records only source-pinned observations and explicitly labeled
experiment ideas; it is not a census of complement genetics in gout.

### 6.1 C5 polymorphisms

This page has no source-pinned, dated genetics scan that can support a *C5*–gout absence claim. Before genotype-stratified work is proposed, search records must identify the catalog and primary studies, ancestry, phenotype, query, coverage window, and retrieval date. Variant effects reported in rheumatoid arthritis or another autoimmune phenotype would not by themselves establish gout risk, flare severity, or response direction.

### 6.2 C5AR1 / C5AR2 / C3AR1 polymorphisms

This page has no source-pinned, dated genetics scan for C5AR1, C5AR2, or
C3AR1. It therefore makes no gout-association or absence claim for those genes.
Variant effects reported in other diseases do not establish a gout-risk or
response direction.

### 6.3 Factor H (CFH) variants

**CFH Y402H (rs1061170, p.Tyr402His)** is an AMD-risk variant
(PMID 16723442; **Human Observational**) with source-specific effects on CFH–CRP
binding (PMID 17339482; **In Vitro + Human-derived protein**). Those records do
not establish gout risk, flare severity, MSU response, or a
candidate-treatment interaction. Population frequency and ancestry effects
require a source-pinned extract before cohort design.

> **Research conjecture — candidate activity under impaired CFH**{ .research-conjecture-label }
>
> **Grounded premises:** CFH regulates alternative-pathway amplification; Y402H changes CFH interactions in non-gout systems (**Human Observational + In Vitro**; source: [CFH evidence boundary](./gout-genetic-variants.md)). Rosmarinic acid, luteolin, exact *Houttuynia* fractions, and exact *Helicteres* lignans have candidate-specific complement-assay evidence at other measured nodes (**In Vitro**; source: [candidate synthesis](./cfh-mechanism-dissociation-cp0-candidates.md)).
>
> **Novel leap:** One or more exact candidates may retain activity when CFH function is absent or impaired. No direct evidence tests this in MSU-activated, CFH-controlled serum, and no Y402H response direction is established.
>
> **Why it matters:** A retained effect would identify a route that does not collapse when Factor-H regulation is weakened.
>
> **Discriminating observation:** Compare each exact material in CFH-replete, CFH-depleted, and CFH-restored serum activated by MSU, with proximal C3, C5a, recovery, and assay-interference controls.

The [CFH-dependence hypotheses page](./cfh-mechanism-dissociation-cp0-candidates.md) preserves the candidate-level reasoning:

- Sahu 1999 reports rosmarinic-acid attachment to activated C3b and a 34 μM half-maximal concentration for inhibiting covalent C3b attachment to cells. **[In Vitro; PubMed-abstract verified, full primary text unresolved]**
- Zhang 2008 reports luteolin activity in both CP and AP hemolysis formats. **[In Vitro; full-text verified]** Similar whole-pathway values do not localize its target or exclude CFH involvement.
- Lu 2018 maps exact CHCP activity mainly to C3 and C4, with partial C5 involvement. **[In Vitro; full-text verified]** Related *Houttuynia* fractions and animal records do not make the fractions interchangeable.
- Yin 2016 maps two exact *Helicteres* compounds to several complement nodes. **[In Vitro; full-text verified, single-paper anchor]** Independent matched-material replication is required.

These records make retained activity plausible for one or more candidates. **[Mechanistic Extrapolation]** They do not establish net CFH independence in MSU-activated serum, a carrier-specific benefit, or a genotype-response direction.

The discriminating experiment is candidate-by-candidate testing in CFH-replete, CFH-depleted, and CFH-restored serum activated by MSU crystals, with proximal C3 and C5a readouts plus assay-interference controls. A population genotype-by-diet analysis would test the recorded dietary proxy in that cohort; it cannot establish or retire an exact biochemical mechanism because identity, dose, absorption, and operative-compartment exposure are not matched.

### 6.4 Gout phenotype heterogeneity — does complement differ by subtype?

Clinical phenotypes of gout that might have distinct complement profiles:

| Phenotype | Hypothesized complement difference | Testable how |
|-----------|------------------------------------|--------------|
| Acute intermittent vs. chronic tophaceous | Tophaceous has chronic low-grade complement activation; acute has cyclic spikes | Serum C3/C4/sC5b-9 longitudinal |
| CKD-associated vs. idiopathic | CKD patients have higher baseline CRP → more classical-pathway priming on crystals | Pre-flare CRP; in-flare C5a generation |
| Metabolic syndrome vs. lean | MetSyn patients have higher baseline complement activation; LPS translocation also contributes | Fecal calprotectin + serum LBP + C5a |
| Post-menopausal women vs. men | Sex hormones affect complement (estrogen slightly suppresses); women have later and different gout | Sex-stratified complement biomarker study |
| Pegloticase responders vs. non-responders (ADA-driven failure) | Non-responders develop immune complexes → additional complement activation → worse flares | C3a / sC5b-9 around infusions |

These rows are **Research Conjectures**, not a literature census. Each would
require a source-pinned cohort review before protocol design; the table is a
set of possible stratification variables for paired flare sampling.

---

## 7. Pharmacological comparators for the complement hypothesis

The evidence assembled in this section does not establish gout efficacy for a complement-directed product. These agents are useful as exact pharmacologic comparators because they perturb different parts of the cascade and can separate C5aR1, C5a, terminal-C5, and alternative-pathway-amplification hypotheses.

| Comparator | Perturbation | Human evidence outside gout | What it could discriminate in a gout-relevant experiment | Principal boundary |
|---|---|---|---|---|
| **Avacopan** | C5aR1 allosteric antagonism | **Clinical Trial:** ADVOCATE in ANCA-associated vasculitis (Jayne 2021, PMID 33596356) | Receptor-mediated C5a signaling while leaving C5aR2 and MAC intact | Gout efficacy is not established by the current source set; refresh registries before making an absence claim |
| **Vilobelimab** | C5a neutralization | **Clinical Trial:** PANAMO in severe COVID-19 (Vlaar 2022, PMID 36087611) | C5a signaling through both receptors while preserving C5b/MAC | Different disease and IV modality |
| **Zilucoplan, eculizumab, ravulizumab** | C5 blockade | **Clinical Trial / regulatory evidence** in non-gout complement-mediated diseases | Combined removal of C5a and MAC | Infection risk, route, and no gout efficacy evidence |
| **Iptacopan** | Factor B inhibition | **Clinical Trial / regulatory evidence** in non-gout complement-mediated diseases | Contribution of alternative-pathway amplification while classical/lectin initiation remains | Does not isolate the initiating route; no gout efficacy evidence |
| **PMX-53 / PMX-205** | Research C5aR1 antagonists | **In Vitro / Animal Model** | Positive-control perturbations for receptor-level assays | Not clinical gout interventions |

The useful comparison is mechanistic, not a cross-drug winner table. A matched MSU-activated human-serum or whole-blood experiment should measure C5a, sC5b-9, and IL-1β under receptor-, ligand-, C5-, and Factor-B-level perturbation. That would show which complement arm is carrying the signal in the tested system without turning evidence from other diseases into a treatment recommendation.

---

## 8. Combination Biology — C5a vs. LPS vs. TNFSF14 Priming

A central unresolved question is how much C5a contributes relative to LPS/TLR4, TNFSF14, and other priming inputs in human flares.

### 8.1 Why the question matters

Three experimental models remain live: C5a carries most of the measured priming signal under a defined condition; C5a and transcriptional inputs contribute nonredundantly; or the inputs compensate for one another. Current evidence does not select among these models in human flares.

### 8.2 What the literature shows

- **An 2014** (PMID 25229885) — C5a potentiated MSU-associated IL-1β in human whole blood and primary monocytes in the tested systems
- **Khameneh 2017** (PMID 28167912) — separate C5ar1⁻/⁻ and C5aR-antagonist arms reduced MSU-associated inflammatory readouts in the tested peritonitis model: genetic loss reduced IL-1β and neutrophil recruitment, while antagonist pretreatment reduced neutrophil and monocyte recruitment. This supports C5aR involvement without establishing a human-gout effect size.
- **Cumpelik 2016** (PMID 26245757) — Neutrophil-derived PMN-Ecto suppressed C5a-mediated priming in the tested system, establishing an endogenous brake on that route

Together, these studies establish C5a as a consequential route in their human-cell and animal systems. They do not show that C5a is necessary, sufficient, or dominant across human gout flares, and they do not demote LPS/TLR4 models to artifacts.

> **Research conjecture — priming-route dependence may vary across gout-flare contexts**{ .research-conjecture-label }
>
> **Grounded premises:** C5a can prime MSU-associated inflammasome output through C5aR1 and ROS in human-cell and murine systems **[In Vitro + Animal Model]** ([An 2014](https://doi.org/10.1002/eji.201444560); [Khameneh 2017](https://doi.org/10.3389/fphar.2017.00010)). TLR4/LPS and TNFSF14 can provide transcriptional priming in other gout-relevant systems **[In Vitro + Human Observational]** ([TNFSF14 evidence](./tnfsf14-gout-target.md)).
>
> **Novel leap:** The relative contribution of these routes may differ by patient state or flare phase. No direct evidence supports that comparative human-flare claim.
>
> **Why it matters:** Route dependence would change which perturbation is most informative in a defined experimental context without declaring a universal target winner.
>
> **Discriminating observation:** In matched human whole-blood, synovial-fluid, or primary-cell systems, cross receptor-, ligand-, and transcriptional-priming perturbations and measure C5a, ROS, pro-IL-1β, mature IL-1β, and viability over time.

### 8.3 Cross-system translation

Cross-system records differ in species, cell system, stimulus, endpoint, and protocol, so numerical differences do not isolate species effects. Translation work must control receptor pharmacology, complement source, trigger surface, and antagonist cross-reactivity rather than transfer a rodent effect size directly.

The Khameneh 2017 result is mechanistically supportive but not a clinical prediction. A matched human gout-relevant study is required before clinical inference; avacopan is one possible receptor-level comparator.

---

## 9. CP0 coverage gap

### 9.1 Direct coverage

The current named natural-product candidates have pathway-level evidence but no
source-verified direct C5aR1 result on this page. This is a claim about the
attached evidence, not about all published or unpublished chemistry. Synthetic
small molecules, constrained peptides, antibodies, and engineered complement
regulators provide assay comparators, while an unbiased human-C5aR1 functional
screen keeps natural-product discovery open.

### 9.2 Indirect urate-lowering effect

A successful uricase intervention could reduce the MSU substrate for future complement activation, but it does not directly inhibit CP0 during an active flare. The relative timing of urate lowering, crystal burden, and complement signaling requires its own clinical evidence.

### 9.3 Portfolio implication

Direct CP0 blockade, upstream crystal removal, and downstream inflammatory suppression are separate intervention classes. Avacopan provides human C5aR1 pharmacology outside gout; DAF, C1-INH, dietary convertase modulators, uricase tracks, and downstream suppressors each retain their own evidence and delivery gates. None is treated as mandatory for the others to proceed.

### 9.4 Research opportunity — screen natural products against C5aR1

Because the bounded legacy records do not answer whether exact natural products directly antagonize human C5aR1 (§4.4), a functional screen using β-arrestin recruitment, calcium flux, or receptor-binding displacement could test the open class. Candidate selection may use pathway-level evidence only as a sampling strategy, not as target attribution:

- **Quercetin, luteolin, apigenin** (flavonoids with broad anti-inflammatory activity; some reported complement inhibition in CH50 assays but no C5aR1-specific data)
- **EGCG** (polyphenol; modulates NF-κB, already in stack; any C5aR1 affinity unknown)
- **Ursolic acid** (triterpenoid; broad anti-inflammatory; unknown at C5aR1)
- **Curcumin** (known NF-κB inhibitor; C5aR1 unknown)
- **Resveratrol, pterostilbene** (SIRT1 activators; C5aR1 unknown)
- **Berberine** (isoquinoline alkaloid; known microbiome modulator; C5aR1 unknown)
Advance any reproducible hit only after concentration-response replication, orthogonal receptor attribution, counterscreens for cytotoxicity and assay interference, and an exposure assessment for the exact compound. A null plate would close only the tested compounds and assay conditions.

### 9.5 Compartment-aware combination conjectures

> **Research conjecture — layered complement blockade**{ .research-conjecture-label }
>
> **Grounded premises:** Rosmarinic acid has assay-specific C3b-directed evidence (**In Vitro; PMID 10353266; full primary text unresolved**). DAF SCR1-4 and C1-INH act at different complement-control steps, but their proposed engineered configurations have not cleared identity, folding, stability, activity, or access gates (**Mechanistic Extrapolation**; source: [DAF hypothesis](./hypotheses/H05-daf-scr14-cp0-thesis.md) and [C1-INH evidence](./c1-inh-protease-stability-ecn-computational.md)).
>
> **Novel leap:** Two exact, independently active materials at different cascade steps might produce a larger or more robust effect than either alone. No direct evidence tests rosmarinic acid + DAF, C1-INH + DAF, or C1-INH + rosmarinic acid.
>
> **Why it matters:** A true layered effect could exploit incomplete blockade or pathway redundancy without making any single track the project.
>
> **Discriminating observation:** First qualify each exact arm alone. Then run vehicle, arm A, arm B, and combination in the same MSU-activated complement system with prespecified additivity/interaction criteria, recovery, and assay-interference controls.

The experiment above tests biochemical compatibility in the chosen system. It does not establish delivery. Intestinal complement modulation and systemic/joint MSU modulation are separate compartment hypotheses; a gut-local result cannot support joint efficacy without a measured causal bridge. The current evidence homes are the [legacy rosmarinic-acid inventory](./upstream-complement-verification-rerun-computational.md), [H05 for DAF](./hypotheses/H05-daf-scr14-cp0-thesis.md), and the [C1-INH configuration page](./c1-inh-protease-stability-ecn-computational.md).

---

## 10. Natural-Product Modulators — What the Literature Actually Shows

### 10.1 Bounded C5aR1 database search

The legacy ChEMBL notes retain neither an exact query nor an immutable database
snapshot. They support no current retrieval, non-retrieval, coverage-rate, or
class-absence claim. Run and preserve a fresh query receipt if database
curation is needed; use a direct functional screen to answer the biological
question.

### 10.2 Flavonoids and broad complement assays

Quercetin, EGCG, resveratrol, baicalein/baicalin, curcumin, luteolin, and related polyphenols appear in broad complement-pathway literature. These records use different materials and CH50/AP50 or other pathway-level assays rather than direct C5aR1 function. Reverify each exact observation before reuse; do not combine them into a potency range, class effect, dietary exposure claim, or receptor-target conclusion.

### 10.3 Omega-3 / SPM — indirect effects

Exact RvD1 and MaR1 changed MSU inflammation in mouse systems through distinct reported routes, while RvD2 has adjacent macrophage and zymosan evidence (see [SPM resolution](./spm-resolution-pathway.md)). EPA and DHA are precursors, not delivered equivalents of those mediators. The reviewed SPM records do not establish direct C5aR1 antagonism, C5a neutralization, or a CP0 effect; any complement–resolution connection remains a separate interaction experiment.

### 10.4 Vitamin D

VDR activation has been reported to change complement-component expression in some cell systems, and vitamin D studies report inflammatory-marker associations outside a direct C5aR1 assay. Whether either observation changes MSU-associated complement activation is unresolved; test it as an indirect pathway hypothesis, not as direct CP0 blockade.

### 10.5 Traditional medicine candidates

Traditional formulations and source materials may contain upstream-complement or C5aR1-relevant chemistry, but formula-level gout phenotypes do not identify the responsible compound or complement node. Exact materials require mechanism-matched fractionation or functional screening before target attribution.

### 10.6 Honest summary

**The present natural-product evidence does not establish direct C5aR1 antagonism.** Avacopan and PMX-53 provide pharmacological comparators, not a reason to close other chemical space. The next useful move is the direct functional screen in §9.4, followed by exact-material, selectivity, exposure, and delivery gates for any hit.

---

## 11. Biomarker experiment

A prospective flare study should collect matched baseline and flare-phase samples and measure total complement components alongside activation products such as C5a, sC5b-9, and pathway-specific fragments. Pre-analytics must be prespecified because complement can continue activating after collection and create artifactual split products.

Wessig 2022 makes CRP a plausible experimental modifier of MSU-surface complement activation. Whether baseline hsCRP stratifies complement output or flare severity in gout is unknown. The decision-relevant result is a within-cohort relationship among CRP, complement activation products, flare timing, and clinical phenotype—not a single reference-range comparison.

These are research readouts, not clinical decision rules.

---

## 12. Open Research Questions

1. **How much does C5a contribute relative to other priming inputs in human flares?** Use matched human whole-blood and synovial-fluid systems with MSU ± C5aR1 blockade ± TLR4/TNFSF14 perturbation; measure C5a, sC5b-9, IL-1β, and cell recruitment.
2. **Which complement level carries the gout-relevant signal?** Compare receptor-, C5a-, terminal-C5-, and Factor-B-level perturbations in the same MSU system. Pharmacological agents in §7 are comparators, not treatment recommendations.
3. **Can a natural product directly antagonize C5aR1?** Screen exact materials in a receptor-functional assay, then confirm selectivity, recovery, and exposure before any gout interpretation.
4. **Does CFH function change an exact candidate's activity?** Run the matched CFH-replete/depleted/restored experiment in §6.3. A genotype/exposure cohort result cannot substitute for the biochemical test.
5. **Do C5a and MAC track differently in human gout?** Collect paired, cold-chain-controlled plasma and synovial-fluid samples across flare timing.
6. **Does CRP modify MSU-associated complement output?** Test CRP as an experimental variable before treating it as a patient stratifier.
7. **Are intestinal and joint complement hypotheses causally connected?** Measure gut-local complement effects and systemic/joint effects separately. A gut-luminal signal advances only the intestinal hypothesis unless a gut-to-joint causal bridge is demonstrated.
8. **Can engineered complement regulators reach and function in the intended compartment?** Qualify each exact payload–chassis–route configuration for identity, folding, stability, activity, recovery, and access before testing combinations.

---

## 13. Sources (Annotated Bibliography)

### Core mechanism

1. Russell IJ, Mansen C, Kolb LM, Kolb WP. "Activation of the fifth component of human complement (C5) induced by monosodium urate crystals: C5 convertase assembly on the crystal surface." *Clin Immunol Immunopathol* 1982;24(2):239-50. [DOI: 10.1016/0090-1229(82)90235-5](https://doi.org/10.1016/0090-1229(82)90235-5). PMID: 6749358. **The 1982 seed paper demonstrating direct C5 convertase assembly on MSU surfaces.**

2. Doherty M, Richards N, Hornby J, Powell R. "Relation between synovial fluid C3 degradation products and local joint inflammation in rheumatoid arthritis, osteoarthritis, and crystal associated arthropathy." *Ann Rheum Dis* 1988;47(3):190-7. [DOI: 10.1136/ard.47.3.190](https://doi.org/10.1136/ard.47.3.190). PMID: 2833185. **288-sample synovial fluid study; acute pseudogout has strikingly elevated C3 activation.**

3. An LL, Mehta P, Xu L, Turman S, Reimer T, Naiman B, Connor J, Sanjuan M, Kolbeck R, Fung M. "Complement C5a potentiates uric acid crystal-induced IL-1β production." *Eur J Immunol* 2014;44(12):3669-79. [DOI: 10.1002/eji.201444560](https://doi.org/10.1002/eji.201444560). PMID: 25229885. **Human whole-blood and monocyte study; C5a + MSU is synergistic for IL-1β via C5aR1, K⁺ efflux, Ca²⁺, cathepsin B.**

4. Cumpelik A, Ankli B, Zecher D, Schifferli JA. "Neutrophil microvesicles resolve gout by inhibiting C5a-mediated priming of the inflammasome." *Ann Rheum Dis* 2016;75(6):1236-45. [DOI: 10.1136/annrheumdis-2015-207338](https://doi.org/10.1136/annrheumdis-2015-207338). PMID: 26245757. **C5a-mediated priming in the tested system; PMN-Ecto / MerTK as an endogenous resolution brake.**

5. Khameneh HJ, Ho AWS, Laudisi F, Derks H, Kandasamy M, Sivasankar B, Teng GG, Mortellaro A. "C5a Regulates IL-1β Production and Leukocyte Recruitment in a Murine Model of Monosodium Urate Crystal-Induced Peritonitis." *Front Pharmacol* 2017;8:10. [DOI: 10.3389/fphar.2017.00010](https://doi.org/10.3389/fphar.2017.00010). PMID: 28167912. **Murine validation; C5a via ROS, not transcription; C5aR antagonism ameliorates peritonitis.**

6. Wessig AK, Hoffmeister L, Klingberg A, Alberts A, Pich A, Brand K, Witte T, Neumann K. "Natural antibodies and CRP drive anaphylatoxin production by urate crystals." *Sci Rep* 2022;12(1):4483. [DOI: 10.1038/s41598-022-08311-z](https://doi.org/10.1038/s41598-022-08311-z). PMID: 35296708. **IgM and CRP both supported efficient classical-pathway MSU activation in the tested serum experiments; CRP generated more C5a than IgM under those assay conditions.**

### Receptor structure and function

7. Liu H, Kim HR, Deepak RNVK, Wang L, Chung KY, Fan H, Wei Z, Zhang C. "Orthosteric and allosteric action of the C5a receptor antagonists." *Nat Struct Mol Biol* 2018;25(6):472-481. [DOI: 10.1038/s41594-018-0067-z](https://doi.org/10.1038/s41594-018-0067-z). PMID: 29867214. **C5aR1 crystal structures with PMX-53 (orthosteric) + avacopan (allosteric); orthosteric / allosteric dual-site druggability.**

### Clinical and therapeutic

8. Jayne DRW, Merkel PA, Schall TJ, Bekker P (for the ADVOCATE Study Group). "Avacopan for the Treatment of ANCA-Associated Vasculitis." *N Engl J Med* 2021;384(7):599-609. [DOI: 10.1056/NEJMoa2023386](https://doi.org/10.1056/NEJMoa2023386). PMID: 33596356. **Phase 3 ADVOCATE trial; basis for FDA 2021 approval.**

9. Vlaar APJ, Witzenrath M, van Paassen P, et al. "Anti-C5a antibody (vilobelimab) therapy for critically ill, invasively mechanically ventilated patients with COVID-19 (PANAMO): a multicentre, double-blind, randomised, placebo-controlled, phase 3 trial." *Lancet Respir Med* 2022;10(12):1137-1146. [DOI: 10.1016/S2213-2600(22)00297-1](https://doi.org/10.1016/S2213-2600(22)00297-1). PMID: 36087611. **Vilobelimab Phase 3; basis for FDA EUA 2023.**

10. Vlaar APJ, de Bruin S, Busch M, et al. "Anti-C5a antibody IFX-1 (vilobelimab) treatment versus best supportive care for patients with severe COVID-19 (PANAMO): an exploratory, open-label, phase 2 randomised controlled trial." *Lancet Rheumatol* 2020;2(12):e764-e773. [DOI: 10.1016/S2665-9913(20)30341-6](https://doi.org/10.1016/S2665-9913(20)30341-6). PMID: 33015643.

11. Lim EHT, Vlaar APJ, de Bruin S, et al. "Pharmacokinetic analysis of vilobelimab, anaphylatoxin C5a and antidrug antibodies in PANAMO: a phase 3 study in critically ill, invasively mechanically ventilated COVID-19 patients." *Intensive Care Med Exp* 2023;11(1):37. [DOI: 10.1186/s40635-023-00520-8](https://doi.org/10.1186/s40635-023-00520-8). PMID: 37332066. **Clinical pharmacokinetic and biomarker record in severe COVID-19; not gout.**

12. Howard JF Jr, Bresch S, Genge A, et al. "Safety and efficacy of zilucoplan in patients with generalised myasthenia gravis (RAISE): a randomised, double-blind, placebo-controlled, phase 3 study." *Lancet Neurol* 2023;22(5):395-406. [DOI: 10.1016/S1474-4422(23)00080-7](https://doi.org/10.1016/S1474-4422(23)00080-7). PMID: 37059508. **RAISE Phase 3; FDA 2023 approval.**

13. de la Borderie G, Chimits D, Boroojerdi B, et al. "Maintenance of zilucoplan efficacy in patients with generalised myasthenia gravis up to 24 weeks: a model-informed analysis." *Ther Adv Neurol Disord* 2024;17:17562864241279125. [DOI: 10.1177/17562864241279125](https://doi.org/10.1177/17562864241279125). PMID: 39314260. **Efficacy durability through 24 weeks.**

### Gout context and pipeline

14. Zaninelli TH, Fattori V, Verri WA Jr. "Harnessing lipid mediators and immune cells to treat gouty arthritis." *Expert Opin Ther Targets* 2023;27(8):751-766. [DOI: 10.1080/14728222.2023.2247559](https://doi.org/10.1080/14728222.2023.2247559). PMID: 37651647. **Review naming complement arm as an under-exploited gout target.**

15. Schauer C, Janko C, Munoz LE, et al. "Aggregated neutrophil extracellular traps limit inflammation by degrading cytokines and chemokines." *Nat Med* 2014;20(5):511-7. [DOI: 10.1038/nm.3547](https://doi.org/10.1038/nm.3547). PMID: 24784231. **NET degradation of C5a and IL-1β as endogenous resolution mechanism; relevant to CP6a.**

### Natural antibody / CRP connection

16. (Wessig 2022 — see entry 6; central to the classical-pathway initiation story.)

### CFH and candidate-specific premises

17. Schaumberg DA, Christen WG, Kozlowski P, Miller DT, Ridker PM, Zee RYL. "A prospective assessment of the Y402H variant in complement factor H, genetic variants in C-reactive protein, and risk of age-related macular degeneration." *Arch Ophthalmol* 2006;124(11):1530-1535. PMID: 16723442. **Human observational AMD evidence; not gout.**

18. Laine M, Jarva H, Seitsonen S, et al. "Y402H polymorphism of complement factor H affects binding affinity to C-reactive protein." *J Immunol* 2007;178(6):3831-3836. [DOI: 10.4049/jimmunol.178.6.3831](https://doi.org/10.4049/jimmunol.178.6.3831). PMID: 17339482. **Variant-specific CFH–CRP binding evidence; not an MSU response experiment.**

19. Sahu A, Rawal N, Pangburn MK. "Inhibition of complement by covalent attachment of rosmarinic acid to activated C3b." *Biochem Pharmacol* 1999;57(12):1439-1446. PMID: 10353266. **In Vitro C3b-directed premise; full primary text remains unresolved in this corpus.**

Additional exact-material records used only for the candidate-specific premises in §6.3:

- Zhang T, Chen DF. *J Ethnopharmacol* 2008;117(2):351-361. PMID: 18400428; PMC7126446. **In Vitro whole-pathway premise for exact luteolin material.**
- Lu Y, Liu X, Liang X, et al. *Acta Pharm Sin B* 2018;8(2):218-227. PMID: 29719782; PMC5925397. **In Vitro depletion/rescue mapping for exact CHCP material.**
- Yin X, Huang A, Zhang S, et al. *Molecules* 2016;21(11):1506. PMID: 27834928; PMC6273495. **In Vitro node-mapping premise; single-paper anchor.**

### Regulatory labels (non-PubMed primary sources)

20. Avacopan (Tavneos) FDA label. Amgen / ChemoCentryx. Approval October 2021 for ANCA-associated vasculitis. [FDA label](https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/214487s000lbl.pdf).

21. Vilobelimab (Gohibic) FDA EUA. InflaRx. EUA April 2023 for severe COVID-19. [FDA EUA letter](https://www.fda.gov/media/166788/download).

22. Zilucoplan (Zilbrysq) FDA label. UCB. Approval October 2023 for generalized myasthenia gravis.

23. Eculizumab (Soliris) FDA label. Alexion / AstraZeneca. First approved March 2007 for PNH. [FDA label](https://www.accessdata.fda.gov/drugsatfda_docs/label/2020/125166s431lbl.pdf).

24. Ravulizumab (Ultomiris) FDA label. Alexion / AstraZeneca. First approved December 2018 for PNH.

25. Iptacopan (Fabhalta) FDA label. Novartis. First approved December 2023 for PNH; IgA nephropathy and C3 glomerulopathy approvals 2024. [FDA label](https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/218276s000lbl.pdf).

### ChEMBL cross-references

- C5aR1 target: [CHEMBL2373](https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2373) (UniProt P21730)
- C5aR2 subunit within complex [CHEMBL4523605]
- Avacopan: [CHEMBL3989871](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL3989871) (first approval 2021, oral)
- Vilobelimab: [CHEMBL2109636](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL2109636)
- Zilucoplan: [CHEMBL4298207](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL4298207) / [CHEMBL5315048](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL5315048) (sodium salt, approved 2023)
- Eculizumab: [CHEMBL1201828](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL1201828) (first approval 2007, IV)
- Ravulizumab: [CHEMBL3989986](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL3989986) (first approval 2018, IV)
- Iptacopan: [CHEMBL4594448](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL4594448) / [CHEMBL5095401](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL5095401) (HCl salt, first approval 2023, oral)
- PMX-53: CHEMBL62201 (IC50 60 nM on human PMN C5aR1 radioligand binding, pChEMBL 7.22, *J Med Chem* 1999)

---

*This page is part of the Open Enzyme research library. Phase 0 — Research and Design. No claims in this document constitute medical advice. All therapeutic discussion is research-stage and, where applicable, off-label.*
