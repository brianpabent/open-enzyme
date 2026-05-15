---
title: Gout Kill Chain — Delivery Route Analysis
date: May 2026
tags:
  - gout
  - nlrp3
  - delivery-routes
  - pharmacokinetics
  - intra-articular
  - oral
  - subcutaneous
  - uricase
  - nanoparticles
  - drug-delivery
related:
  - nlrp3-exploit-map.md
  - nlrp3-inflammasome.md
  - uricase.md
  - gout-pathophysiology.md
  - gout-clinical-pipeline.md
  - complement-c5a-gout.md
  - delivery-route-matrix.md
  - compounding-pharmacy-track.md
  - chassis-pending-interventions.md
  - purine-degrading-bacteria.md
  - gsdmd-pore-delivery-paradox.md
  - uricase-abcg2-genotype-stratification-computational.md
sources:
  - "ACS Applied Nano Materials 2025 — gout nanocarrier systems review"
  - "Frontiers Pharmacology 2025 — drug delivery systems for gout"
  - "Inflammopharmacology 2025 — URAT1/GLUT9 delivery technologies"
  - "J Nanobiotechnology 2025 — Pickering emulsion uricase+catalase IA"
  - "PMC 2025 — hollow mesoporous silica nanomotors + uricase"
  - "Cell Reports Medicine 2025 (PULSE) — designer probiotic living drugs"
  - "Scientific Reports 2025 — Georgia State CRISPR uricase liver cells"
  - "bioRxiv Feb 2025 — caspase inhibitor delivery through GSDMD pores"
  - "ACS Omega 2025 — transdermal oxypurinol microneedle"
  - "PMC 2022 — transdermal colchicine microneedle, rat gout model"
  - "Trends Pharmacol Sci 2025 — targeting NLRP3 for inflammatory disease therapy"
status: published
---

# Gout Kill Chain — Delivery Route Analysis

A node-by-node pharmacological route analysis across all chokepoints in the gout/NLRP3 kill chain. Companion to [nlrp3-exploit-map.md](./nlrp3-exploit-map.md), which maps *what* to hit. This page maps *how to get there.*

**Companion matrix:** [`delivery-route-matrix.md`](./delivery-route-matrix.md) is the orthogonal-axis view (rows = compound classes, columns = delivery routes). Both pages are deliberately complementary — chokepoint-anchored vs compound-class-anchored. Cross-reference both when a finding could land in either grid.

**What this page adds:** The exploit map is rich in compounds but thin on delivery route reasoning. Mechanism match is necessary but not sufficient — a drug targeting a synovial macrophage enzyme that can only reach hepatocytes is a pharmacological dead end. Delivery route determines whether a compound's IC50 is biologically relevant at the target tissue.

**Guiding principle:** compartment matching. Ask "where does this target live?" before asking "how do we deliver?" A renal proximal-tubule transporter (URAT1) is unreachable by intra-articular injection. A synovial macrophage target is unreachable by inhaled drug. Compartment mismatch is the dominant reason a mechanistically-correct compound fails to work in vivo.

**Temporal axis:** The matrix below is largely time-static, but gout has at least three time regimes that gate route choice: (a) **flare onset** (0–6 hr) wants fast onset → sublingual / inhaled / IA; (b) **flare peak** (6–48 hr) wants sustained → IA hydrogel / SC depot; (c) **inter-flare chronic / lifetime prevention** wants once-daily oral or longer-cadence biologic / chassis-based. The right route for a given chokepoint depends on which clock you're on. Cells in the matrix should be read with this in mind even where it is not explicitly tagged.

---

## Route vocabulary

| Route | Abbreviation | Reaches | Typical context |
|---|---|---|---|
| Oral systemic | PO | Systemic circulation via GI absorption | Most small molecules, ULT drugs |
| Oral gut-lumen | PO-GL | GI tract lumen only (no systemic absorption intended) | Gut-lumen uricase, ABCG2 modulators |
| Intravenous | IV | Rapid systemic distribution | Biologics, pegloticase |
| Subcutaneous | SC | Slow systemic absorption via lymphatics | Biologics (anakinra, canakinumab) |
| Intra-articular | IA | Joint synovial fluid → synovial lining macrophages | Local flare management |
| Transdermal (passive) | TD | Skin + subcutaneous; limited systemic | ColciGel |
| Transdermal (microneedle) | TD-MN | Systemic via enhanced penetration | Active development for colchicine, oxypurinol |
| Intranasal | IN | Nasal mucosa, olfactory epithelium; small peptides can cross to CSF/systemic | KPV tripeptide |
| Oral microbiome | PO-MB | Gut lumen via live organism | PULSE probiotic, engineered yeast |
| GalNAc-siRNA / LNP | IV/SC → liver | Hepatocyte-tropic; via ASGPR for GalNAc, passive accumulation for LNP | Inclisiran class; emerging XDH/URAT1 siRNA |

---

## Kill chain node by node

### PRPS — De Novo Purine Biosynthesis (upstream of XO)

**Target compartment:** Liver (dominant flux), intestinal epithelium (significant), every rapidly-dividing cell.

**Clinically validated routes:**
- PO systemic — the only route used. No pharma-grade PRPS inhibitor in clinical development for gout. Eurycomanol (tongkat ali extract) reduces SUA 7–11% in oral RCT (n=105). (Clinical Trial — eurycomanol PO)

**Routes that fail and why:**
- IA: PRPS is hepatic/intestinal, not synovial. Delivering a PRPS inhibitor into the joint suppresses only local purine synthesis — the systemic urate load is unaffected.
- Inhaled/topical: same compartment mismatch.

**Open territory:**
- **GalNAc-siRNA for PRPS1 mRNA knockdown (hepatocyte-tropic):** The same delivery chemistry as inclisiran (GalNAc-PCSK9 siRNA, approved 2021) is structurally applicable to PRPS1 in liver. Quarterly dosing, liver-targeted, durable knockdown. No gout program exists. (Mechanistic Extrapolation — GalNAc-siRNA; freedom-to-operate open)
- **Gut-epithelium-targeted oral NP:** Upper GI enterocytes are high-flux purine synthesis sites. pH-triggered nanoparticles releasing in small intestine (pH 6–7), taken up by enterocytes without reaching systemic circulation — selective intestinal PRPS suppression without hepatic/hematologic toxicity risk. Not tested. (Mechanistic Extrapolation)

---

### XO — Xanthine Oxidase / Urate Production

**Target compartment:** Liver (dominant), intestinal epithelium. Hepatic XO generates ~80% of serum urate flux in humans.

**Clinically validated routes:**
- PO systemic — allopurinol (prodrug → oxypurinol), febuxostat (~85% oral bioavailability). All approved XO inhibitors are oral tablets. (Clinical Trial)

**Routes that fail and why:**
- IA: XO is hepatic/intestinal. Synovial macrophages have negligible XO activity — the urate driving crystal formation is systemically derived. IA XO inhibition is mechanistically incoherent.
- Inhaled: XO not expressed in lung at levels relevant to gout.

**Open territory:**
- **Transdermal oxypurinol via microneedle array:** Oxypurinol (the active XO-inhibiting metabolite of allopurinol) has a 13–18-hour half-life vs. allopurinol's 1–1.6 hours. ~30% of patients have suboptimal first-pass conversion. A 2025 ACS Omega study demonstrated sustained transdermal plasma levels of oxypurinol via thermosensitive gel + polymeric solid microneedles in rats — bypassing first-pass conversion bottleneck. No human microneedle data yet. (Animal Model — rat; Mechanistic Extrapolation for human)
- **GalNAc-siRNA / LNP for XDH mRNA knockdown:** XDH encodes both XO and xanthine dehydrogenase. Liver-tropic GalNAc-siRNA or LNP delivery of XDH-targeting siRNA would achieve the same endpoint as allopurinol/febuxostat with quarterly dosing. No gout program; closest analogue is inclisiran. (Mechanistic Extrapolation)
- **ColciGel precedent:** Topical colchicine gel (FDA-approved) establishes that transdermal gout-drug delivery is pharmaceutically feasible — a delivery-route proof that benefits the entire transdermal class.

---

### Renal URAT1 / GLUT9 — Renal Urate Reabsorption

**Target compartment:** Proximal tubule lumen (URAT1 on apical membrane), proximal tubule cell basolateral exit (GLUT9/SLC2A9). Drug must reach renal filtrate via systemic circulation → glomerular filtration → tubular fluid.

**Clinically validated routes:**
- PO systemic — probenecid, lesinurad, AR882 (pozdeutinurad, Phase 3 REDUCE 1 & 2), dotinurad, benzbromarone. All oral. The proximal tubule lumen is naturally a distribution endpoint for filtered drugs — oral → systemic → renal filtration is mechanistically correct. (Clinical Trial)

**Routes that fail and why:**
- IA: URAT1 is a renal transporter. No URAT1 expression in synovium. Intra-articular delivery of a URAT1 inhibitor reaches the wrong tissue entirely.
- Inhaled/intranasal/topical: systemic exposure required to reach renal tubule lumen via filtration; none of these routes provide meaningful renal tubular concentration.

**Open territory:**
- **Kidney-tropic siRNA for URAT1 mRNA knockdown:** The OE wiki documents `sirna-urat1-modality.md` — kidney-tropic siRNA using folate-receptor or megalin-receptor targeting (not GalNAc, which is liver-tropic). A 2025 *Inflammopharmacology* paper maps liposomes and sustained-release devices as URAT1/GLUT9 delivery technologies under investigation. No human trial. (Mechanistic Extrapolation)
- **GLUT9 as co-target — the understudied locus:** GLUT9 (SLC2A9) has the largest per-allele effect on serum urate of any GWAS locus — greater than URAT1. No clinical GLUT9 inhibitor program exists despite its genetics being stronger. An oral GLUT9 inhibitor faces the same delivery requirements as URAT1 inhibitors. The target exists; the drug does not. (Mechanistic Extrapolation)

---

### Intestinal ABCG2 — Gut Urate Secretion

**Target compartment:** Apical membrane of intestinal epithelial cells (duodenum/jejunum). Secretes uric acid from enterocytes into gut lumen. Accounts for ~1/3 of total urate excretion. Q141K loss-of-function variant is the #1 gout-risk GWAS locus.

**Clinically validated routes:**
- PO dietary/prebiotic: butyrate (from fermentable fiber → SCFAs) activates PPARγ → ABCG2 upregulation. DASH diet RCT: 0.25–0.73 mg/dL SUA reduction. Inulin-enriched diets elevate SCFA-producing bacteria and ABCG2 expression. (Clinical Trial — dietary; Animal Model + In Vitro — ABCG2 mechanism)
- PO probiotic: engineered probiotics upregulating colonic ABCG2 reduced SUA >60% in animal models (ScienceDirect 2025). (Animal Model)
- Note: all approved ABCG2-targeting drugs inhibit it (for cancer MDR reversal). ABCG2 enhancement is pharmacologically uncompeted.

**Routes that fail and why:**
- Systemic IV/SC: systemic ABCG2 enhancers would also modulate ABCG2 in liver and kidney, potentially disrupting drug disposition via ABCG2's role as a promiscuous efflux transporter. Compartment-contamination problem.
- IA: ABCG2 not expressed at relevant levels in synovium.

**Open territory:**
- **Gut-restricted ABCG2 enhancers — no drug exists:** An oral compound acting exclusively in intestinal lumen without systemic absorption would upregulate intestinal ABCG2 while sparing hepatic/renal ABCG2. Analogous strategy to colesevelam (gut-restricted bile acid sequestrant). No such molecule exists for ABCG2. (Mechanistic Extrapolation — novel drug class)
- **Q141K trafficking rescue via HDAC inhibition:** HDAC inhibitors partially rescue Q141K ABCG2 from ER retention to apical membrane (In Vitro). Oral butyrate may have dual mechanism: PPARγ induction + Q141K rescue. Not studied in gout specifically. (In Vitro)
- **Gut-lumen uricase + ABCG2-upregulating probiotic as a two-stage combination:** Stage 1 — probiotic upregulates ABCG2 → more urate secreted into gut lumen. Stage 2 — uricase-expressing probiotic degrades that secreted urate → serum urate drawn down by combined flux. PULSE (E. coli Nissle expressing uricase) and the 2025 ABCG2-probiotic paper describe the two halves separately. The combination has not been tested. This is a two-stage gut-lumen clearance architecture with no clinical precedent. (Mechanistic Extrapolation — combination not tested)
- **Purine-degrading bacteria (PDB) — now covered in [purine-degrading-bacteria.md](./purine-degrading-bacteria.md):** A conserved gene cluster in gut Bacillota (Lachnospiraceae and related) converts urate to SCFAs (butyrate + acetate) via the 2,8-dioxopurine pathway. Antibiotic depletion raises incident gout 30% (Stanford n=14K cohort, HR 1.30). Engineered EcN expressing the gene cluster reduces plasma UA −63% in hyperuricemic mice (CBT2.0). SCFA outputs compound the mechanism via butyrate → ABCG2 upregulation + XO inhibition. No clinical trial exists. (Animal Model + Human Retrospective Cohort + Mechanistic Extrapolation)

---

### Uricase — Uric Acid Degradation / Crystal Dissolution

**Target compartments:** (a) Systemic/vascular — degrading circulating urate. (b) Gut lumen — degrading secreted urate. (c) Intra-articular — dissolving MSU crystal deposits directly in joint.

**Computational prior:** [`comp-019` (gut-lumen uricase × ABCG2 genotype flux model)](./uricase-abcg2-genotype-stratification-computational.md) predicts the SUA reduction band for the gut-lumen sink mechanism: −0.5 to −1.0 mg/dL in typical (non-CKD) gout cohorts, with WT/WT showing the LARGEST predicted ΔSUA (−0.83 mg/dL at 25 mg/day mid-dose, 90% CI −1.13 to −0.57) and Q141K homozygotes the smallest (−0.50 mg/dL). The Q141K-positive subset gains a synergy bonus from butyrate-mediated trafficking rescue — see [`purine-degrading-bacteria.md` §"Q141K + PDB-butyrate + HDAC"](./purine-degrading-bacteria.md). The mechanism is multiplicative on residual ABCG2 capacity; the gut-lumen sink works ACROSS genotypes.

**Clinically validated routes:**
- **IV systemic (pegylated):** Pegloticase (Krystexxa), rasburicase. Near-zero serum urate within hours. Anti-drug antibody formation limits durability in ~40–60%; methotrexate co-dosing (SEL-212/pegadricase strategy) partially resolves immunogenicity. PRX-115 Phase 2 RELEASE trial active (Dec 2025, N=150). (Clinical Trial — IV pegloticase/rasburicase)
- **PO gut-lumen (ALLN-346):** Enteric-coated engineered *C. utilis* uricase. Phase 1 completed without safety signals; Phase 2a pivotal trial terminated September 2022 (not for safety reasons). Mechanism valid — exploits ABCG2-mediated intestinal urate secretion as concentration sink. No currently active oral uricase program. (Clinical Trial Phase 1/2a — oral gut-lumen)
- **PO probiotic (PULSE):** *E. coli* Nissle 1917 expressing uricase with HucR UA-responsive biosensor (dynamically regulates expression based on luminal urate). Validated in Cell Reports Medicine 2025 in humanized microbiome mouse model. Not in human trials. (Animal Model)

**Routes that fail and why:**
- Inhaled/intranasal: no therapeutic urate elimination pathway exists in the airway for gout. Uric acid is not secreted into airways at clinically significant flux.
- Topical skin: sweat contains trace urate; topical uricase degrades surface urate only. No systemic benefit.
- SC: SC delivery of a large protein antigen (uricase ~135 kDa homotetramer) places enzyme directly in subcutaneous tissue where sensitization occurs without the oral tolerance advantage. IV provides faster PK/PD and standard monitoring protocol. No SC uricase program in development.

**Open territory:**
- **Oral Qβ bacteriophage capsid nanoparticle uricase:** Ancestral uricase encapsulated in Qβ VLP (virus-like particle) delivered orally reduced hyperuricemia in XO-knockout mice (Biomacromolecules 2023, PMID 37126604). VLP capsids provide protease protection superior to enteric coating alone and present different immunogenic epitopes than naked enzyme. First oral nanoparticle uricase with animal-model efficacy. (Animal Model)
- **Intra-articular Pickering emulsion cascade bioreactor:** A 2025 *J Nanobiotechnology* paper describes uricase + catalase spatially co-confined at an oil-water interface (Pickering emulsion), delivered intra-articularly to dissolve MSU crystals while neutralizing H₂O₂ byproduct in situ. The H₂O₂ problem — uricase generates H₂O₂ alongside allantoin, which can drive oxidative damage — is solved by the co-confined catalase. (Animal Model — preclinical IA delivery)
- **Intra-articular self-propelled nanomotors (uricase + ionic diffusiophoresis):** A 2025 PMC paper (hollow mesoporous silica nanomotors) demonstrated uricase-loaded nanomotors that migrate toward MSU crystals within the joint cavity driven by their own enzymatic activity (ionic diffusiophoresis from urate → allantoin conversion). Active crystal-seeking, not passive diffusion. (Animal Model — preclinical)
- **Cell membrane-coated liposomal uricase (immune evasion):** M2 macrophage membrane + exosome membrane-coated liposome encapsulating uricase: ~91.9% enzyme activity retention after 1 hour of trypsin exposure; anti-inflammatory synovial macrophage targeting in gouty arthritis models (Frontiers Pharmacology 2025). M2 membrane coating co-delivers anti-inflammatory polarization signals. (Animal Model)
- **RBC membrane-coated nanoparticle uricase (Biomimetic Bioreactor):** Uricase in red blood cell membrane-coated nanoparticles — autologous-membrane self-tolerance reduces immunogenicity without PEGylation. Extended half-life (PMC 2025). (Animal Model)
- **CRISPR/LNP hepatic gene restoration (long-horizon curative):** Georgia State 2025 (*Scientific Reports*) demonstrated CRISPR insertion of ancestral uricase at the AAVS1 safe-harbor locus in Huh-7 liver cells, normalizing urate and blocking fructose-driven lipogenesis. LNP delivery of the CRISPR cassette to hepatocytes is the stated next step; animal studies pending. Not enzyme replacement — gene restoration. Timeline 5–10+ years to human trial but the direction is established. (In Vitro human cells — CRISPR; Mechanistic Extrapolation — LNP delivery in vivo)

> **Key intra-articular gap:** No clinical IA uricase program exists. The Pickering bioreactor and nanomotor approaches together solve the two primary obstacles (H₂O₂ toxicity + crystal access) at the preclinical level. This is genuine open territory.

---

### MSU Crystal — Phagocyte Uptake Inhibition

**Target compartment:** Synovial fluid / joint space. The intervention point is the surface of MSU crystals before macrophage/neutrophil uptake.

**Clinically validated routes:**
- None. No clinical drug specifically targets crystal phagocytosis. Colchicine indirectly reduces phagocytic capacity (CP3 tubulin disruption). CD44 is the primary phagocytic receptor for MSU — no CD44-blocking drug is approved for gout.

**Routes that fail and why:**
- Systemic IV/SC anti-CD44 mAb: CD44 is ubiquitously expressed (wound healing, bacterial defense, tissue homeostasis). Systemic CD44 blockade is too broad.
- PO systemic crystal-coating agents: crystal surfaces in joint are a local physical target. Systemic drug dilutes before reaching joint at crystal-surface-adsorption-effective concentrations.

**Open territory:**
- **IA cationic nanoparticles for crystal surface coating:** Amphiphilic or cationic nanoparticles delivered intra-articularly adsorb to MSU crystal surfaces, blocking CD44/TLR recognition. Effectively creates "stealth crystals" that cannot trigger CP0/CP1 priming. Crystal surface modification is established in other contexts (kidney stone prevention, biofilm disruption) but not studied for gout. (Mechanistic Extrapolation)
- **Serum albumin crystal coating as a physiological precedent:** Albumin naturally coats MSU crystals and reduces their inflammatory potential. Gout flares are more common with low albumin states (cachexia, fasting). An albumin-derived crystal-coating peptide for IA delivery is speculative but mechanistically grounded. (Mechanistic Extrapolation)
- **Liposome "decoy" competition for phagocyte attention:** Unilamellar liposomes can be phagocytosed preferentially over MSU crystals in dose-dependent competition (In Vitro). IA injection of decoy liposomes saturating macrophage phagocytic capacity before MSU crystal encounter is not tested in vivo. (In Vitro)

---

### CP0 — Complement C5a Priming

**Target compartment:** Systemic macrophages/monocytes (circulating and tissue-resident) that traffic to the joint; C5a generated in joint space but also systemically.

**Clinically validated routes:**
- PO systemic: Avacopan (Tavneos), 30 mg BID, FDA-approved oral C5aR1 antagonist for ANCA vasculitis; 64–129-hour half-life. No gout trial registered as of May 2026. Mechanism is directly applicable. (Clinical Trial — ANCA; Mechanistic Extrapolation — gout)
- IV: Eculizumab (anti-C5 mAb), zilucoplan (anti-C5 peptide, MG). Not tested in gout.

**Routes that fail and why:**
- IA: C5a is generated both in joint space and systemically. IA C5aR1 blockade covers only joint-local C5a — circulating monocytes primed systemically and trafficking to the joint are unaffected. Incomplete coverage at this node.
- Inhaled: C5aR1 in lung is the target for pulmonary complement diseases. Wrong compartment for gout.

**Open territory:**
- **Avacopan gout repurposing — lowest-friction pharma-grade CP0 access:** Oral, generic pathway approaching, established safety profile, 64–129-hour half-life (near-once-daily dosing). An investigator-initiated flare trial with avacopan requires no formulation work. This is the single most accessible pharma-grade CP0 intervention. (Clinical Trial for ANCA; gap = no gout trial)
- **DAF/CD55 SCR1-4 gut-lumen delivery via engineered koji:** The OE stack's H05 hypothesis — truncated DAF/CD55 secreted by koji into gut lumen to intercept mucosal complement activation upstream of systemic C5a. Three wet-lab unknowns remain. If validated, the first food-grade CP0 intervention with no pharma analogue. (Mechanistic Extrapolation; see `wiki/hypotheses/H05-daf-scr14-cp0-thesis.md`)

> **Platform gap:** The OE wiki notes zero confirmed fermentable C5aR1 antagonists in ChEMBL or PubMed (as of comp-014 screen, 6,798 compounds). Avacopan repurposing is the near-term bridge; DAF/CD55 koji is the long-horizon food-grade path.

---

### CP1 — NF-κB Priming (Transcriptional Signal 1)

**Target compartment:** Macrophages and monocytes throughout the body (tissue-resident + circulating). NF-κB priming is a systemic event establishing the "primed" state before the crystal triggers activation.

**Clinically validated routes:**
- PO systemic: vast majority of CP1 compounds are oral (berberine, curcumin, sulforaphane, EGCG, quercetin, resveratrol, KPV/PepT1 substrates). Appropriate — NF-κB operates systemically. (Clinical Trial — berberine, some curcumin formulations; Animal Model + In Vitro — most natural compounds)
- SC/IV: CERC-002 (anti-TNFSF14/LIGHT mAb), Phase 2 signal in COVID ARDS; no gout trial. TNFα inhibitors (SC) target upstream NF-κB activators.

**Routes that fail and why:**
- IA NF-κB inhibitors during active flare: NF-κB priming establishes the macrophage's ready state before the crystal encounter — it's a systemic, time-preceding process. Delivering NF-κB inhibitors intra-articularly after the flare starts is closing the barn door post-facto. Correct timing is systemic/chronic suppression, not acute local delivery.
- Inhaled corticosteroids: suppress NF-κB in airway; do not reach joint macrophages at therapeutic concentrations for gout.

**Open territory:**
- **Nasal KPV (tripeptide) for CP1 — PK rationale:** KPV and GHK-Cu are PepT1 substrates — the intestinal oligopeptide transporter delivers tripeptides into enterocytes and portal circulation without protease destruction. Oral KPV provides gut-mucosal macrophage access for CP1 suppression. Nasal KPV (200–500 mcg/day, in the current OE protocol) crosses nasal mucosa and olfactory epithelium. These are two distinct delivery routes for the same tripeptide accessing different macrophage compartments. Pharmacokinetic characterization of each route's contribution to systemic CP1 suppression does not exist. (Mechanistic Extrapolation — PK; In Vitro — KPV mechanism)
- **Gut microbiome LPS as systemic NF-κB primer:** Berberine's dual mechanism (direct NF-κB inhibition + reduction of LPS-producing gram-negative bacteria) means it delivers an "upstream source block" by reshaping the gut microbiome. Systemic LPS from gram-negative gut dysbiosis is Signal 1 for chronic macrophage NF-κB priming. Treating the microbiome as the NF-κB primer is an underappreciated delivery concept — the "drug" is the microbial ecosystem state. (Animal Model + Clinical Trial — berberine in SIBO/IBD; Mechanistic Extrapolation — LPS-NF-κB in gout priming)
- **TNFSF14/HVEM blockade — no oral option:** CERC-002 is SC/IV only. Natural compounds with in vitro TNFSF14/HVEM modulation activity (EGCG, TF3 theaflavins) are the only oral-route CP1a candidates; in vivo HVEM receptor modulation has not been characterized for these compounds. (In Vitro — EGCG/TF3; Mechanistic Extrapolation — gout-specific)

---

### CP2 — NLRP3 Activation (K⁺ Efflux / Lysosomal Rupture / ROS)

**Target compartment:** Cytoplasm of synovial macrophages and recruited monocytes. NLRP3 assembly is intracellular.

**Clinically validated routes:**
- PO systemic: BHB (exogenous ketone esters or ketogenic diet), oridonin, tranilast (oral, approved in Japan/South Korea), hydroxychloroquine (lysosomal stabilization), dapansutrile Phase 2a (100–2000 mg/day oral). The pharmaceutical NLRP3 inhibitor class is uniformly oral. (Clinical Trial — tranilast; Phase 2a — dapansutrile; Animal Model + In Vitro — most others)
- IV: Exogenous BHB IV infusion — pharmacologically established in ICU settings; not gout-specific.

**Routes that fail and why:**
- Inhaled NLRP3 inhibitors: NLRP3 in lung macrophages is the relevant target for ARDS, not gout. Inhaled MCC950/dapansutrile class would suppress pulmonary NLRP3 without meaningful synovial macrophage concentrations for gout.

**Routes that are plausible but underexplored:**
- **IA NLRP3 inhibitor with sustained-release depot:** NLRP3 assembles in synovial lining macrophages accessible from the joint space — IA delivery is mechanistically coherent (unlike nodes with distant target compartments). Challenge: small molecules clear from joint fluid in ~1–4 hours. A pH-responsive hydrogel depot (crosslinked hyaluronate, PLGA microspheres) releasing MCC950/oridonin-class inhibitor over 5–7 days per injection would maintain therapeutic NLRP3 suppression in synovial macrophages. A 2025 ScienceDirect paper demonstrates Gas6-loaded microsphere IA delivery in MSU models; a 2025 Trends Pharmacol Sci review cites IV and direct injection as the routes being explored for NLRP3 inhibitor nanoparticles — no gout-specific IA program in either. (Animal Model — IA colchicine nanoemulsion PMID 34032545; Mechanistic Extrapolation — IA sustained-release NLRP3 inhibitor)
- **Monocyte membrane-coated dual NP (mMc@DNCs) — RA precedent:** Co-delivery of MCC950 + dexamethasone in monocyte membrane-coated nanocrystals; IV injection; monocyte membrane enables active targeting to inflamed synovium via VCAM-1/ICAM-1 leukocyte trafficking. Published in RA context; directly applicable to gout. (Animal Model — RA; Mechanistic Extrapolation — gout translation)
- **BHB ester vs. salt for acute flare-abort:** R-BHB ethyl ester achieves serum BHB 1–2 mM within 30 min orally; D-BHB salts achieve similar but lower peak with slower kinetics. For flare-abort use (ketone supplement at flare onset for rapid NLRP3 suppression), the ester form may be pharmacokinetically superior. Not compared in gout context. An n=1 serum-BHB-at-flare-onset experiment (ester vs. salt) is within Brian's self-experiment framework. (Mechanistic Extrapolation — comparative PK in gout)

---

### CP3 — ASC Speck Assembly / Microtubule Transport

**Target compartment:** Cytoplasm of macrophages and neutrophils. ASC transport from mitochondria to ER-localized NLRP3 is microtubule-mediated.

**Clinically validated routes:**
- PO systemic: colchicine (AGREE trial, low-dose 1.2 + 0.6 mg regimen validated). Multi-mechanism: CP3 ASC transport block + CP2 P2X7 pore block + CP6a neutrophil tubulin disruption. (Clinical Trial — AGREE trial)
- IV colchicine: historically used; narrow therapeutic index + severe extravasation toxicity; essentially abandoned.

**Routes that fail and why:**
- Topical colchicine (passive transdermal — ColciGel): achieves local skin/subcutaneous concentrations with limited systemic exposure. Does not reach synovial macrophages at CP3-effective concentrations. ColciGel's mechanism is likely peripheral nerve/local tissue anti-inflammatory rather than NLRP3 pathway disruption. Indicated for pain relief, not inflammasome suppression.
- Inhaled colchicine: systemic distribution required to reach synovial macrophages. Inhaled delivery concentrates in lung.

**Open territory:**
- **Transdermal colchicine via microneedle array (systemic, not passive):** A 2022 PMC study (PMID 36101018) demonstrated dissolvable microneedle arrays for colchicine in a rat gout model — achieving therapeutic plasma levels and reducing joint inflammation. A 2024 Drug Delivery and Translational Research paper used ethosomes + dissolving microneedle patch for co-delivery of colchicine + iguratimod. Active microneedle-assisted transdermal delivery achieves systemic concentrations while eliminating GI side effects (colchicine's dose-limiting GI toxicity is the primary adherence problem). Pre-clinical/Phase 1 development area. (Animal Model — rat; early-stage for human)
- **IA colchicine nanoemulsion:** PMID 34032545 demonstrated colchicine-loaded nanoemulsion for IA delivery with biodistribution showing prolonged joint retention vs. free drug. Direct delivery to inflamed joint space eliminates systemic distribution and toxicity while targeting the exact tissue where CP3 operates. Preclinical only. (Animal Model — preclinical)
- **IC100 anti-ASC antibody (SC/IV):** Zyngeria's IC100 directly targets the ASC PYD domain, blocking polymerization. Biologic — SC or IV delivery only. Validates ASC as a druggable target independent of colchicine's tubulin mechanism. (Mechanistic Extrapolation — gout-specific; note no known active gout trial)

---

### CP4 — Caspase-1 Activation

**Target compartment:** Intracellular, within macrophage cytoplasm. The ASC speck platform activates caspase-1 by proximity-induced autocleavage.

**Clinically validated routes:**
- PO prodrug: VX-765 (belnacasan) → VRT-043198 (caspase-1 inhibitor). Reached Phase 2a in epilepsy (well-tolerated); clinical development paused. Not trialed in gout. (Clinical Trial — epilepsy safety data; Mechanistic Extrapolation — gout)
- No approved caspase-1 inhibitor for any indication.

**Routes that fail and why:**
- IA delivery of peptidic caspase-1 inhibitors (Z-YVAD-FMK class): these inhibitors have poor cell membrane permeability due to size and charge — IA delivery puts them in the joint fluid but they cannot cross the macrophage plasma membrane to reach intracellular caspase-1. Small, lipophilic caspase-1 inhibitors (VX-765 class) can reach the intracellular target from the joint space; large peptidic inhibitors cannot.

**Open territory:**
- **GSDMD pore-mediated delivery of membrane-impermeant caspase inhibitors (2025 bioRxiv preprint):** A February 2025 bioRxiv preprint demonstrates that once GSDMD pores form (10–20 nm diameter), they serve as delivery conduits — membrane-impermeant caspase inhibitors passively enter GSDMD-pore-expressing pyroptotic cells more efficiently than normal cells. Paradoxical: the inflammatory cell's own exit pores become the drug delivery portal. This creates a therapeutic window at the intersection of CP4 and CP6b: as pyroptosis initiates (CP6b, GSDMD pores open), those pores enhance delivery of caspase inhibitors that close the CP4 executioner. No drug development program has exploited this in any disease, including gout. (In Vitro — preprint; Mechanistic Extrapolation — gout translation)
- **Oral VX-765 for gout — zero trials in 28 years of mechanism availability:** Caspase-1 is the final executioner of the gout cascade (cleaves pro-IL-1β, pro-IL-18, GSDMD simultaneously). VX-765 has human Phase 2a safety data. No gout trials registered on ClinicalTrials.gov as of May 2026. Identical gap structure to zileuton at CP6a and disulfiram at CP6b — mechanistically-obvious repurposing candidates missed when discovering and treating research communities don't overlap. **Compounding pharmacy track candidate** — VX-765 is research-compound class (not FDA-approved for any indication), so compounding access is more constrained than for FDA-approved zileuton/disulfiram; tracked under [`compounding-pharmacy-track.md`](./compounding-pharmacy-track.md) as a Tier 3 candidate pending API availability audit.

---

### CP5a — IL-1β / IL-18 Receptor Blockade

**Target compartment:** IL-1R1 on neutrophils, endothelial cells, synoviocytes. After IL-1β is released into the joint, it binds IL-1R1 on these cells to amplify the flare.

**Clinically validated routes:**
- SC: Anakinra (100 mg SC daily, 4–6 hour half-life — short), canakinumab (150 mg SC Q8 weeks for gout, FDA-approved August 2023, 26-day half-life), rilonacept (SC, IL-1 trap, not FDA-approved for gout). (Clinical Trial — anakinra off-label; Clinical Trial — canakinumab FDA-approved gout 2023)
- IV: High-dose anakinra in ICU. Not gout standard.
- IA anakinra: small case series for acute gout flare — delivers high local concentrations without systemic immunosuppression. No large RCT. (Mechanistic Extrapolation with small case series)

**Routes that fail and why:**
- PO biologics (anakinra/canakinumab oral): GI proteases destroy recombinant proteins. Small-molecule IL-1R1 antagonists would solve this but none are approved.
- Inhaled: IL-1 signaling in gout is synovial/neutrophil compartment, not pulmonary.

**Open territory:**
- **IA anakinra depot (sustained-release microsphere):** Single IA injection of PLGA microsphere-encapsulated anakinra providing 5–7 days of sustained IL-1R1 blockade in the joint. Addresses the short-half-life problem (anakinra's 4–6 hours requires daily SC injection) and the systemic immunosuppression concern. PLGA IA delivery is established for dexamethasone; anakinra formulation for this format has not been reported. (Mechanistic Extrapolation — IA sustained-release platform for biologics). Note: anakinra (~17 kDa, ~4 nm) falls in the GSDMD pore size-permissive range — see [`gsdmd-pore-delivery-paradox.md`](./gsdmd-pore-delivery-paradox.md) §"Implication for OE biologics" for the size-selectivity table; IA anakinra during active pyroptosis would gain enhanced intracellular access via pore self-delivery.
- **Inhaled mRNA-IL-1RA pulse for acute flare:** LNP-formulated mRNA encoding IL-1 receptor antagonist (anakinra-equivalent), delivered via pulmonary inhaler. Transient expression matches the short flare window (12–72 hours). Pulmonary surface area (~70 m²) maximizes uptake; mRNA-LNP delivery for pulmonary indications is mature (CF, RSV, asthma research programs). Eliminates SC injection requirement for flare management; potentially cost-competitive with $300K/yr canakinumab. Tracked in [`chassis-pending-interventions.md` §4](./chassis-pending-interventions.md) — chassis pending (synthetic mRNA + LNP + inhaler device, commercial pharma + clinical partner). (Mechanistic Extrapolation — no clinical program)
- **Oral anti-IL-1β nanobody:** Nanobodies (VHH ~12–15 kDa) are far more acid- and protease-stable than full mAbs. Oral nanobody delivery for IBD demonstrated in mice. An oral anti-IL-1β nanobody for gout would eliminate SC injection requirement for flare management. No gout program. (Animal Model — oral nanobody IBD precedent; Mechanistic Extrapolation — gout translation)
- **Canakinumab + gut-lumen uricase combination — ULT initiation flare window:** Canakinumab's 26-day half-life covers the peak flare-risk window during ULT initiation (crystal dissolution mobilization). A combination trial — canakinumab SC (flare-abort) + oral/probiotic uricase (serum urate reduction) — that co-targets the flare amplification (CP5a) and crystal burden upstream simultaneously does not exist. (Mechanistic Extrapolation — combination design)

---

### CP5b — Active Resolution via ALX/FPR2 (SPMs)

**Target compartment:** ALX/FPR2 receptor on neutrophils and macrophages — commands neutrophil withdrawal and M1→M2 macrophage polarization switch. Distinct mechanism from IL-1 receptor blockade — resolution is not "suppress inflammation" but "command cessation."

**Clinically validated routes:**
- PO (precursor): High-dose EPA/DHA omega-3 (3–4 g/day) — endogenous biosynthesis of RvE1, RvD series. No gout-specific flare-shortening RCT with this combination. (Mechanistic Extrapolation for gout; Clinical Trial — cardiovascular omega-3 safety/efficacy)
- Topical: RX-10045 (resolvin E1 analog) Phase 2 for dry eye disease — establishes that stable SPM analogs are pharmacologically deliverable topically. (Clinical Trial — dry eye; Mechanistic Extrapolation — joint delivery)
- IA: RvD1 intrathecal + IP in mouse gout model reduced joint IL-1β, ASC specks, CGRP (PMID 35716378). Preclinical. (Animal Model)

**Routes that fail and why:**
- PO direct SPMs (not precursors): SPMs have plasma half-lives of minutes — destroyed by GI oxidation and first-pass metabolism before reaching joint macrophages. Supplements labeled "SPM Active" (Metagenics) provide 17-HDHA and 18-HEPE (precursors), not SPMs themselves.
- Inhaled SPMs for gout: resolving pulmonary inflammation is the indicated use; gout is a joint disease. Inhaled SPMs do not reach knee/MTP joint at therapeutic concentration.

**Open territory:**
- **IA stable SPM analog:** A chemically modified resolvin or protectin analog (modified at metabolically vulnerable positions) delivered IA at flare onset could actively command resolution from within the joint. No clinical program. The topical resolvin E1 analog proof-of-concept (dry eye, Phase 2) demonstrates that stable SPM analogs are chemically achievable. (Mechanistic Extrapolation — IA route; no human trial)
- **Low-dose aspirin + EPA combination for AT-SPM generation:** Low-dose aspirin redirects COX-2 to produce aspirin-triggered 15-epi-LXA4 and AT-RvD series — these are active-resolution mediators (not COX-2 inhibitors). The mechanism is "trigger resolution," not "reduce inflammation." Combining low-dose aspirin + EPA (3–4 g/day) to shift the joint toward active resolution via AT-SPM generation is the most accessible pharmacologically-supported CP5b combination. No gout flare trial exists. (Mechanistic Extrapolation — combination in gout)
- **Lactoferrin as the only fermentable CP5b modulator in the OE stack:** Lactoferrin's indirect ALX/FPR2 modulation via multiple pathways makes it the OE platform's only food-grade CPsb option. Validated for expression in A. awamori and P. pastoris. See [nlrp3-exploit-map.md](./nlrp3-exploit-map.md).

---

### CP6a — 5-LOX / LTB4 / Neutrophil Amplification Loop

**Target compartment:** ALOX5 (5-LOX) in neutrophils recruited to the joint space, and in synovial mast cells/macrophages. LTB4 drives BLT1-mediated neutrophil chemoattraction.

**Clinically validated routes:**
- PO systemic: Zileuton (Zyflo/Zyflo CR), FDA-approved oral 5-LOX inhibitor for asthma since 1996. Direct mechanism match for CP6a. Zero gout trials registered. (Clinical Trial — asthma; Mechanistic Extrapolation — gout)
- PO supplements: quercetin (300 nM 5-LOX IC50 in ChEMBL), AKBA from boswellia (~2.7 μM cellular IC50, allosteric 5-LOX binding site distinct from active site). (In Vitro — IC50 data)

**Routes that fail and why:**
- Inhaled zileuton: 5-LOX inhibition for asthma/COPD is the pulmonary application. For gout, the neutrophil amplification loop operates in the knee/MTP joint space. Inhaled zileuton suppresses pulmonary LTB4 without meaningfully affecting the joint neutrophil amplification.
- IA 5-LOX inhibitor (small molecule): mechanistically plausible — 5-LOX operates in neutrophils that are IN the joint space. Challenge is rapid small-molecule clearance from joint fluid (1–4 hour half-life). IA sustained-release 5-LOX inhibition not studied for gout.

**Open territory:**
- **Zileuton for acute gout flare — 28-year opportunity gap:** A generic, oral, FDA-approved drug with direct CP6a mechanism that has never been trialed in gout. A physician-initiated retrospective analysis of asthma patients also taking colchicine for gout, or a small investigator-initiated trial, requires no formulation work. The absence of any such report after 28 years of zileuton availability suggests the immunology/asthma research community and rheumatology community simply haven't intersected around this compound. (Clinical Trial — asthma safety; gap = zero gout evidence). **Compounding pharmacy track candidate:** zileuton fits the cleavage rule (small-molecule + FDA-approved + off-patent → compoundable), pending bulk API availability audit — see [`compounding-pharmacy-track.md`](./compounding-pharmacy-track.md).
- **BLT1 receptor antagonist (oral, one step downstream of 5-LOX):** BLT1 is the LTB4 receptor on neutrophils. BLT1 antagonists (LY293111, BIIL 260) tested in asthma and RA with modest results; no gout trial. BLT1 blockade is complementary to 5-LOX inhibition — same pathway, different target, non-overlapping resistance profile. (Animal Model + early clinical — asthma/RA; Mechanistic Extrapolation — gout)
- **EPA + quercetin + AKBA triple 5-LOX interference — non-redundant stacking:** EPA competes with arachidonic acid for 5-LOX substrate (redirects toward RvE1); quercetin inhibits the catalytic site (~300 nM IC50); AKBA inhibits allosterically at a distinct site (~2.7 μM IC50). Three non-overlapping mechanisms on the same enzyme. This combination has not been tested in any gout model. (In Vitro — IC50 data for each; Mechanistic Extrapolation — combination in gout)

---

### CP6b — Gasdermin D / Pyroptotic Exit

**Target compartment:** GSDMD N-terminal fragment, specifically Cys191 (human) / Cys192 (mouse), in pyroptotic macrophage plasma membrane.

**Clinically validated routes:**
- PO systemic: Disulfiram (FDA-approved for alcohol use disorder, generic ~$30/month) — covalently modifies GSDMD Cys191. Dimethyl fumarate/DMF (Tecfidera, FDA-approved for MS) — succinates GSDMD Cys191. Both oral, both with established long-term safety data. Neither approved for gout; no gout trials registered. (Clinical Trial — approved indications; Mechanistic Extrapolation — gout)
- No IV/SC GSDMD inhibitor in clinical use.

**Routes that fail and why:**
- IA disulfiram/DMF: both are cysteine-reactive electrophiles that covalently modify any accessible cysteine residue. IA delivery into joint space would expose them to other Cys-containing proteins (collagens, synovial proteins) promiscuously — a higher off-target burden than systemic oral delivery where hepatic first-pass partially controls reactivity profile.
- GSDMD-targeted biologics: GSDMD is intracellular. Antibody delivery to intracellular targets requires endosomal escape chemistry or specialized conjugates; no such program in development for gout.

**Open territory:**
- **Disulfiram for gout — the recognized but untried window:** Disulfiram's GSDMD Cys191 mechanism was published in Nature Immunology 2020. Five years later, no published case series of disulfiram co-administration for refractory gout management. Identical pattern to zileuton — mechanistically-obvious repurposing candidate, treating and discovering communities non-overlapping. $30/month generic. (Clinical Trial — approved indication; gap = zero gout evidence). **Compounding pharmacy track — highest-priority candidate:** disulfiram is the lead candidate in [`compounding-pharmacy-track.md`](./compounding-pharmacy-track.md) (FDA-approved for AUD, off-patent, bulk API available, comp-027 dose-modeling queued).
- **GSDMD pore self-delivery paradox (2025 bioRxiv preprint) — dual relevance at CP4 and CP6b:** See CP4 note above. GSDMD pores (10–20 nm) serve as delivery conduits for membrane-impermeant inhibitors back into the pyroptotic cell — including GSDMD-derived blocking peptides (Ac-FLTD-CMK, PNAS 2018) that cannot normally cross intact plasma membranes. Once the pore opens, it enables delivery of compounds that close it. This paradox is unaddressed in gout pharmacology and in drug delivery literature generally. (In Vitro — preprint Feb 2025; Mechanistic Extrapolation)
- **Lactoferrin CP6b via mitophagy pathway:** Lactoferrin induces PINK1/Parkin + FUNDC1/BNIP3/NIX mitophagy, clearing damaged mitochondria before they trigger GSDMD cleavage. Mechanistically upstream of Cys191 chemistry — prevents GSDMD cleavage rather than blocking the cleaved fragment's pore formation. **Source paper Shan et al. 2026 (PMID 41524100, Food & Function) is a *radiation-induced intestinal injury (RIII)* model, NOT a gout model**; the PINK1/Parkin + FUNDC1/BNIP3/NIX mitophagy → NLRP3/caspase-1/GSDMD pyroptosis suppression mechanism is what transfers to gout (Mechanistic Extrapolation). Delivery route: oral kojied lactoferrin. The only fermentable food-grade CP6b option in the OE stack. (Animal Model + In Vitro for the RIII paper itself; Mechanistic Extrapolation for gout translation.)
- **DMF gout trial — the low-friction alternative to disulfiram:** DMF (generic, oral, FDA-approved) succinates GSDMD Cys191 via a distinct chemistry from disulfiram's dithiocarbamate mechanism. DMF also activates Nrf2/HO-1 (anti-oxidant) and has lower hepatotoxicity profile than disulfiram. An investigator-initiated DMF gout flare management case series faces no regulatory barriers.

---

## Cross-cutting findings

### 1. Intra-articular delivery as a systematic gap

Nearly every node from CP2 through CP6b has a mechanistically coherent IA delivery rationale — the synovial lining macrophages are physically accessible from the joint space. Yet the IA pharmacology of these nodes is almost entirely in animal models or not tested at all. The convergence of:
- Ultrasound-guided IA injection (rheumatology standard of care)
- pH-responsive sustained-release hydrogel depots
- Cell-membrane-coated NPs targeting synovial macrophages via leukocyte trafficking (VCAM-1/ICAM-1)
- Co-delivery of multiple payloads in a single formulation

...creates an IA combination platform that doesn't exist. A single IA injection combining an NLRP3 inhibitor (CP2), anakinra/IL-1Ra (CP5a), and an SPM analog (CP5b) could simultaneously block three nodes from within the joint. This is a research architecture, not a drug — but no lab has framed it this way.

### 2. The GSDMD pore self-delivery paradox

The most structurally novel finding from this survey: GSDMD pores (10–20 nm diameter) serve as delivery conduits for membrane-impermeant caspase inhibitors and GSDMD-blocking peptides into the pyroptotic cell (bioRxiv February 2025). The inflammatory cell's own exit pore becomes the drug delivery portal. The CP4/CP6b overlap is the most concentrated opportunity — once GSDMD pores open (CP6b), they provide enhanced access for caspase-1 inhibitors (CP4) that normally cannot cross intact plasma membranes. No program in any disease. No gout pharmacologist has described this. The preprint is from 2025 and the delivery implication appears not to have been noticed by the gout field.

### 3. Three generic repurposing candidates with zero gout trials

Three mechanistically-correct, FDA-approved, oral, generic drugs have never been trialed for gout flare management:

| Drug | Node | Mechanism | Approved for | Generic price | Gout trials |
|---|---|---|---|---|---|
| Zileuton (Zyflo) | CP6a | 5-LOX inhibition → ↓LTB4 | Asthma (1996) | ~$30–100/month | Zero |
| VX-765 (belnacasan) | CP4 | Caspase-1 inhibition | Phase 2a epilepsy | Research compound | Zero |
| Disulfiram (Antabuse) | CP6b | GSDMD Cys191 covalent modification | Alcohol use disorder (1951) | ~$30/month | Zero |

Zileuton and disulfiram are available over-the-counter or via standard prescription without clinical trial infrastructure. A physician managing a patient on both zileuton (for asthma) and colchicine (for gout) has generated real-world data on this question — that data simply hasn't been collected or published.

### 4. Gut-lumen two-stage combination

Combining ABCG2-upregulating probiotic (Stage 1: more urate secreted into gut lumen) with gut-lumen uricase expression (Stage 2: degrade the secreted urate) creates a two-stage clearance platform. The 2025 ABCG2-probiotic paper and PULSE paper describe the two halves separately. In principle, combining these in a single engineered organism or a co-administered pair generates additive serum urate reduction — each stage individually reduces SUA; together they close a positive feedback loop. Not tested as a combination in any model.

### 5. Purine-degrading bacteria (PDB) — now covered in [purine-degrading-bacteria.md](./purine-degrading-bacteria.md)

The 2,8-dioxopurine pathway: conserved 8-gene cluster in *Bacillota* gut bacteria converts urate anaerobically to butyrate + acetate. Depleted in gout patients (70% lower gene cluster abundance in early hyperuricemia). Clindamycin (anaerobic-targeting) raises incident gout 30% vs. Bactrim (HR 1.30, Stanford n=14K cohort). Engineered EcN with the gene cluster (CBT2.0) reduced plasma UA −63% in hyperuricemic mice. SCFA compounding: butyrate → ABCG2 upregulation + XO inhibition + NLRP3 dampening — three downstream effects on top of direct urate degradation. No clinical trial. Selenium cofactor requirement creates a potential dietary lever (DOPDH is selenium-dependent; deficiency may phenocopy PDB depletion even with intact bacterial abundance).

---

## Summary table

| Kill chain node | Best clinical route | Most underexplored route | Key gap |
|---|---|---|---|
| PRPS | PO systemic | GalNAc-siRNA (liver) | No pharma-grade PRPS inhibitor for gout |
| XO | PO systemic | Transdermal microneedle (oxypurinol) | No GalNAc-siRNA XDH program |
| URAT1/GLUT9 | PO systemic | Kidney-tropic siRNA | GLUT9 has no drug despite strongest GWAS effect |
| Intestinal ABCG2 | PO gut/dietary | Gut-restricted ABCG2 enhancer | No pharmacological ABCG2 enhancer exists |
| Uricase | IV systemic | IA nanomotor/Pickering bioreactor | No clinical IA uricase program |
| MSU phagocyte uptake | None (IA only makes sense) | IA crystal-coating NP | No clinical crystal surface modification |
| CP0 — C5a | PO (avacopan, no gout trial) | DAF/CD55 koji (food-grade) | Zero gout trials with avacopan |
| CP1 — NF-κB | PO systemic | Gut microbiome LPS block | TNFSF14 has no oral antagonist |
| CP2 — NLRP3 activation | PO systemic | IA sustained-release depot | Monocyte-membrane NP not translated to gout |
| CP3 — ASC speck | PO colchicine | IA colchicine NP / transdermal MN | GI side effects remain dose-limiting |
| CP4 — Caspase-1 | PO (VX-765 — no gout trial) | GSDMD pore self-delivery | Zero gout trials with VX-765 |
| CP5a — IL-1β | SC (canakinumab, anakinra) | IA anakinra depot | No single-injection IA IL-1Ra format |
| CP5b — SPM resolution | PO precursor (EPA/DHA) | IA stable SPM analog | No stable SPM analog in gout trials |
| CP6a — 5-LOX/LTB4 | PO (zileuton — no gout trial) | Triple stacking (EPA+quercetin+AKBA) | 28 years of zero gout trials with zileuton |
| CP6b — GSDMD | PO (disulfiram — no gout trial) | GSDMD pore self-delivery | Zero gout trials with disulfiram or DMF |

---

*Delivery route reasoning reviewed against: [nlrp3-exploit-map.md](./nlrp3-exploit-map.md), [gout-pathophysiology.md](./gout-pathophysiology.md), [gout-clinical-pipeline.md](./gout-clinical-pipeline.md), [uricase.md](./uricase.md), [complement-c5a-gout.md](./complement-c5a-gout.md), [peptide-gout-addendum.md](./peptide-gout-addendum.md). Web research May 2026.*
