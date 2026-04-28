---
title: "ABCG2 Modulators — Pharmacological Levers on the Gut Urate Sink"
date: 2026-04-26
tags:
  - abcg2
  - bcrp
  - urate-transport
  - gut-lumen-sink
  - ppar-gamma
  - nrf2
  - ahr
  - hdac-inhibitor
  - butyrate
  - scfa
  - q141k
  - polymorphism
  - androgen-axis
  - tnf-alpha
  - tissue-selectivity
related:
  - gut-lumen-sink.md
  - androgen-urate-axis.md
  - gout-pathophysiology.md
  - supplements-stack.md
  - engineered-koji-protocol.md
  - lactoferrin.md
sources:
  - Gorczyca & Aleksunes 2020 (PMID 32077332)
  - Rzeczycki et al. 2025 (PMID 41465322)
  - Xie et al. 2020 (PMID 32555444)
  - Basseville et al. 2012 (PMID 22472121)
  - Saranko et al. 2013 (PMID 23800412)
  - Ferrer-Picón et al. 2020 (PMID 31211831)
  - Li et al. 2023 (PMID 36948133)
  - Juraschek et al. 2021 (PMID 33615722)
  - He et al. 2021 (PMID 34491388)
  - Wathanavasin et al. 2025 (PMID 39998074)
---

# ABCG2 Modulators — Pharmacological Levers on the Gut Urate Sink

Gut ABCG2 is the apical-membrane efflux transporter that moves urate from blood into the intestinal lumen, accounting for ~30% of daily urate elimination. The engineered-uricase platform's "gut-lumen sink" thesis (see [`gut-lumen-sink.md`](./gut-lumen-sink.md)) requires the substrate (luminal urate) to be there before the enzyme can act. ABCG2 is the gate that controls substrate supply.

This page maps the pharmacological levers on ABCG2 in the gut: what suppresses it (closing the gate), what induces it (opening the gate), what specifically rescues the most common gout-causing ABCG2 variant (Q141K), and where the existing supplement stack accidentally fights the platform thesis.

The landscape was characterized through PubMed scans on 2026-04-26 with primary-source verification. Evidence tiers are tagged inline.

---

## Two distinct modulation modes — keep them separate

Most ABCG2 literature conflates two mechanisms with opposite implications for the platform thesis. Read every claim with this distinction in mind:

| Mode | What it does | Implication for gut sink |
|---|---|---|
| **Functional inhibition** | Compound binds existing ABCG2 protein and blocks its pumping action. The pump is present but occupied. | **Bad.** Even if there is plenty of ABCG2 in the apical membrane, urate cannot be effluxed into the lumen. Studied heavily in oncology because tumor ABCG2 effluxes chemotherapy drugs. |
| **Transcriptional modulation** | Compound changes how much ABCG2 protein is produced (via nuclear receptors PPARγ, PXR, AhR, Nrf2, or via NFIB and other transcription factors). | **Inducers are good** — more pump = more urate efflux capacity. **Suppressors are bad** — fewer pumps regardless of activity. |

**The same compound can do both, in opposite directions, dose-dependent.** Quercetin is a textbook case: at low μM cytosolic concentrations it is a competitive substrate/inhibitor (functional inhibition), but in some chronic-dosing animal studies it appears to upregulate ABCG2 mRNA (transcriptional induction). Net effect at a given dose is the integrated result, often poorly characterized in the gut-lumen context specifically.

**Q141K trafficking rescue** is a third, distinct mode discussed in §6 — relevant only to carriers of the Q141K polymorphism but mechanistically different from both functional inhibition and transcriptional induction.

---

## The transcriptional regulation map

The most authoritative review of ABCG2/BCRP transcriptional regulation across tissues and species is Gorczyca & Aleksunes 2020, *Expert Opinion on Drug Metabolism & Toxicology* (PMID 32077332). Per that review, the major nuclear-receptor and transcription-factor regulators of ABCG2 are:

| Pathway | Inducer signal | Tissue distribution | Gut selectivity |
|---|---|---|---|
| **PPARγ** | Endogenous: omega-3 metabolites, prostaglandin J2 derivatives. Pharmacologic: pioglitazone, fenofibrate (weak). Microbiome-derived: SCFAs, especially butyrate (Xie et al. 2020). | Adipose-dominant; substantial in gut, liver. | Moderate — also in adipose and liver. |
| **AhR (aryl hydrocarbon receptor)** | Indole-3-carbinol & DIM (cruciferous), tryptophan-derived AhR ligands from gut microbes (kynurenine, indole-3-aldehyde from *Lactobacillus*), some flavonoids. | Highest expression in barrier tissues (gut, skin, lung). | **Strong gut enrichment.** |
| **Nrf2 / Keap1** | Sulforaphane (broccoli sprouts), curcumin (mixed effects — see contradiction note in §8), DMF (drug). | Broad expression. | Moderate — also in liver, kidney, BBB. |
| **PXR** | Rifampicin, hyperforin (St. John's wort), some statins. | Gut, liver, **also BBB**. | **Worst tissue selectivity** — induces BBB ABCG2 too, which compromises CNS drug penetration. |
| **HNF4α** | Bile acids (FXR cross-talk), short-chain fatty acids via complex regulatory cross-talk. | **Gut-enterocyte-specific** in adult tissue. | **Best tissue selectivity for the gut sink thesis.** |
| **NFIB** (Nuclear Factor I B) | Endogenous expression varies by tissue and genotype (rs28379954). | Broad. | Less characterized; Solbakk 2025 (PMID 40554316) showed NFIB overexpression in Caco-2 enterocytes suppresses ABCG2 by 25–30%. |

(All Mechanistic Extrapolation + In Vitro / Animal Model unless specifically tagged as Clinical.)

**Key correction relative to first-pass deep dive:** The original framing of "butyrate → HDAC inhibition → ABCG2 induction via HNF4α" was incomplete. Per Xie et al. 2020 (*Acta Pharmacologica Sinica*, PMID 32555444; [DOI](https://doi.org/10.1038/s41401-020-0402-x)), butyrate has **two independent effects** on intestinal transporters:

- **HDAC inhibition** → P-gp (ABCB1) downregulation via NF-κB / p65 — a separate phenomenon affecting drug-efflux pumps, not directly relevant to urate.
- **PPARγ activation** → BCRP / ABCG2 induction — the urate-relevant effect.

Xie et al. specifically tested HDAC inhibitors (vorinostat, valproate) and TNF-α / NF-κB pathway disruption. None affected BCRP protein expression. PPARγ antagonist GW9662 abolished butyrate's BCRP induction. Butyrate's effect on the gut urate sink is therefore PPARγ-mediated, not HDAC-mediated, in wild-type ABCG2 carriers.

This refinement matters because it untangles the wild-type induction mechanism from the Q141K rescue mechanism (§6), which IS HDAC-mediated and operates independently. Brian-pattern Q141K-positive gout patients (estimable as ~30–50% of the population per published GWAS) would benefit from butyrate via *both* mechanisms simultaneously, on different alleles.

---

## Suppressors of intestinal ABCG2

What is making the gate leaky in the typical gout patient:

### 1. Androgens (T, DHT) — covered in [`androgen-urate-axis.md`](./androgen-urate-axis.md)

AR-mediated transcriptional repression of ABCG2 in gut and kidney. **Mechanistic Extrapolation + Animal Model** (rodent renal expression studies; primate physiology supports gut homology). Clinically anchored by ~0.3–0.8 mg/dL serum UA rise on physiological-replacement TRT, larger at supraphysiological doses (Clinical, observational + small RCTs).

For SERMs (e.g., clomid) the androgen-driver effect is the same as exogenous TRT: clomid raises endogenous T → URAT1 up + ABCG2 down. (Mechanistic Extrapolation, supported by single-arm clinical observation.)

### 2. Inflammation / TNFα

Ferrer-Picón et al. 2020, *Inflammatory Bowel Diseases* ([DOI](https://doi.org/10.1093/ibd/izz119), PMID 31211831). Patient-derived intestinal organoids (d-EpOCs) treated with TNFα showed **suppressed SLC16A1 (MCT1), ABCG2, and GPR43**, mimicking the expression profile of active IBD biopsies. Critically, IBD-derived organoids were *not* intrinsically less responsive to butyrate — TNFα was the proximal blocker.

**Implication:** chronic low-grade inflammation (Hashimoto's, food sensitivities, IBS, active IBD) produces the same gut ABCG2 suppression that high androgens do, by a parallel mechanism. **In Vitro + clinical biopsy correlation.** Both axes can act simultaneously and additively.

### 3. NFIB upregulation

Solbakk et al. 2025, *Drug Metabolism and Disposition* ([DOI](https://doi.org/10.1016/j.dmd.2025.100100), PMID 40554316). NFIB overexpression in Caco-2 enterocytes suppressed ABCG2 by 25–30%. In humans, the rs28379954 T>C NFIB variant causes increased clozapine dose requirements consistent with reduced intestinal efflux. **In Vitro + pharmacogenomic correlation.**

This is a less-studied lever than the others; clinical relevance for urate is unestablished but mechanistically plausible.

### 4. Statins (mixed)

Some statin isoforms suppress ABCG2 expression, contributing to the well-documented modest UA rise on statin therapy (~0.1–0.3 mg/dL). **Clinical observation + Mechanistic Extrapolation.** Effect varies by statin (rosuvastatin > atorvastatin > pravastatin per limited data).

### 5. Western diet / low fiber

Low fiber → low colonic SCFA production → low PPARγ drive → baseline-suppressed ABCG2. Confounds with the "gout patients eat poorly" stereotype, but the proposed mechanism here is the gut ABCG2 axis specifically, not just purine intake. **Mechanistic Extrapolation; clinical evidence in §9.**

---

## Inducers of intestinal ABCG2

Ranked roughly by evidence + safety + tissue selectivity:

### Tier 1 — Strong evidence + good safety

**Butyrate (via fermentable fiber → colonic SCFA production)**
- **Mechanism:** PPARγ activation in enterocytes (Xie et al. 2020; In Vitro + Animal Model)
- **Anchoring evidence:** Animal model — sodium butyrate in HUA mouse model decreased serum UA AND restored intestinal ABCG2 expression (Li et al. 2023, *Biomedicine & Pharmacotherapy*, [DOI](https://doi.org/10.1016/j.biopha.2023.114568), PMID 36948133). **Animal Model** with direct gout-relevant endpoint.
- **Practical lever:** Fermentable fiber (resistant starch, inulin, GOS, beta-glucan) — **not** direct butyrate supplementation, which reaches the gut poorly. Aim ≥25–30 g fiber/day, with deliberate fermentable types in the mix.
- **Effect size in humans:** ~0.25 mg/dL UA reduction on DASH diet, up to 0.73 mg/dL in baseline UA ≥8 mg/dL (§9, Juraschek 2021).
- **Tissue selectivity:** good — colonic butyrate is largely consumed by colonocytes before significant systemic distribution.

**Sulforaphane (Nrf2)**
- **Mechanism:** Nrf2 activation in enterocytes
- **Anchoring evidence:** clinical safety established; broccoli-sprout extracts standardized; animal models show ABCG2 upregulation. **In Vitro + Animal Model + clinical safety data.** Direct UA endpoint not established.
- **Practical lever:** Standardized broccoli-sprout extract (10–60 mg sulforaphane glucosinolate equivalent/day) or fresh broccoli sprouts (~50 g daily provides similar dose).
- **Tissue selectivity:** moderate — also induces Nrf2 in liver and BBB. The BBB effect is a small concern for someone on lipophilic CNS-active drugs that depend on BBB ABCG2 for safety margins (rare in practice).

### Tier 2 — Solid mechanism, modest evidence

**Indole-3-carbinol / DIM (AhR)**
- **Mechanism:** AhR activation; gut-AhR is highly active because the receptor evolved partly to sense gut microbial metabolites.
- **Anchoring evidence:** **In Vitro + Animal Model.** Cruciferous-vegetable consumption epidemiologically associated with lower UA, though mechanism may be multifactorial.
- **Tissue selectivity:** good (gut-enterocyte enrichment of AhR), though hepatic AhR is also active.
- **Caveat:** DIM at high doses (>200 mg/day) has hepatotoxicity case reports. Stay at dietary or moderate-supplement levels.

**Probiotic delivery of AhR-active microbes**
- **Mechanism:** specific *Lactobacillus reuteri* strains, *L. plantarum*, and others produce indole-3-aldehyde (a potent AhR agonist) from dietary tryptophan.
- **Evidence:** **Mechanistic Extrapolation.** Direct urate endpoint untested for probiotic strain selection. Worth investigating.

### Tier 3 — Pharmacological-grade levers

**Fenofibrate (PPARα/γ + direct uricosuric effect)**
- **Mechanism:** PPARγ activation contributes to gut ABCG2 induction; the larger effect is direct URAT1 inhibition (uricosuric, lowers serum UA via increased renal excretion).
- **Anchoring evidence:** Clinical trials show fenofibrate lowers serum UA ~10–15% in patients with mixed dyslipidemia/hyperuricemia. **Clinical Trial.**
- **Caveat:** This is a drug, not a supplement. Requires prescription and monitoring (LFTs, creatinine, drug interactions including warfarin).

**Pioglitazone (PPARγ)**
- **Mechanism:** strong PPARγ agonist.
- **Anchoring evidence:** **Clinical Trial** for type 2 diabetes; ABCG2 induction is a downstream effect. Modest UA-lowering effect documented.
- **Caveat:** Weight gain, fluid retention, modest bladder cancer signal. Not appropriate for non-diabetic gout patients on cost/risk grounds alone.

### Tier 4 — Avoid for primary tissue-selectivity reasons

**Rifampicin (PXR)**
- Induces ABCG2 in gut + liver + BBB. The BBB induction compromises the protective drug-efflux function (potentially increases neurotoxic drug penetration). Antibiotic use only — not a chronic urate strategy.

---

## The Q141K rescue mechanism — a separate axis

The Q141K (rs2231142, p.Gln141Lys) ABCG2 polymorphism is the single largest genetic risk factor for hyperuricemia and gout (odds ratio ~2–3 across populations). Per Saranko et al. 2013, *Biochemical and Biophysical Research Communications* ([DOI](https://doi.org/10.1016/j.bbrc.2013.06.054), PMID 23800412):

- Q141K has a "mild processing defect" — protein folds imperfectly in the nucleotide-binding domain
- Mistrafficked: significant fraction is retained in the aggresome (perinuclear protein-aggregation compartment) instead of reaching the apical membrane
- Reduced ATPase activity (~50% of wild-type)
- Defect is **rescuable by low temperature** in cell culture, indicating it is a folding/trafficking defect, not loss of catalytic core. **In Vitro.**

Basseville et al. 2012, *Cancer Research* ([DOI](https://doi.org/10.1158/0008-5472.CAN-11-2008), PMID 22472121) demonstrated:

- HDAC inhibitors (vorinostat, romidepsin, others tested) **rescue Q141K trafficking from aggresome to plasma membrane**
- HDIs restore wild-type-equivalent ABCG2 expression and substrate-efflux activity in Q141K cells
- Mechanism is via altered microtubule motor protein expression (kinesins/dyneins involved in protein trafficking), not direct chromatin opening at the ABCG2 locus
- **In Vitro.** No human RCT in Q141K-positive gout patients yet.

**Implication for the platform thesis:**

Butyrate is an HDAC inhibitor at colonic concentrations achievable through fermentable fiber. For Q141K-positive gout patients, butyrate hits **two independent targets** on ABCG2:

1. **PPARγ-mediated induction** of any wild-type allele (most Q141K carriers are heterozygous)
2. **HDI-mediated trafficking rescue** of the Q141K variant

This is mechanistically a stronger lever in Q141K carriers than wild-type carriers. Predicted but untested: **Q141K + fiber → larger UA reduction than wild-type + fiber.**

A pharmacogenomic-stratified RCT of fermentable fiber (or sodium butyrate enteric capsules) on serum UA, stratified by Q141K genotype, would either confirm or falsify this prediction. Cost-effective experiment for the platform's "differential responder" question.

**Genotype-source framing — clinical, not consumer.** The trial must generate its own genotype data at enrollment via a CLIA-certified clinical PCR assay for rs2231142 (Quest, LabCorp, or equivalent single-SNP genotyping; ~$40–80 per patient at clinical-lab pricing). Consumer-grade genotype exports (23andMe, Ancestry, etc.) are explicitly excluded as the data source — not as a personal-preference call but for trial-design rigor: reproducibility, documented assay performance, sample-chain-of-custody, and CLIA-grade QA are all preconditions for a publishable pharmacogenomic stratification. The trial framing is therefore agnostic at recruitment (no presumed prior genotype knowledge); patients are screened, genotyped on-site, and assigned to arms by the trial's own assay.

**Population-frequency caveat for trial design.** Q141K allele frequency varies substantially by ancestry — published GWAS report ~30–50% in East Asian gout cohorts but only ~10–15% in European-ancestry cohorts (some series lower). The "30–50% of gout patients" figure is correct for an East-Asian-majority cohort but overstates the carrier fraction in a European-American sample. A pharmacogenomic fiber trial should pre-specify population and powering — and, given that Q141K homozygotes are predicted to show the largest effect size, including a homozygous arm (where feasible) gives the cleanest signal-to-noise even at modest n. This framing is not "fiber for everyone with gout" — it's **dual-action butyrate as a personalized intervention for Q141K-positive gout patients, with effect size scaling by allele dose**.

The clinical-genotyping cost is also self-justifying against the alternative non-stratified design. In a European-ancestry cohort with carrier frequency ~10–15%, a non-stratified RCT looking for the same Q141K-conditional effect size would need roughly 3× the n to power the differential response (the Q141K-positive subset's signal is diluted by the wild-type majority). At ~$40–80/patient, on-site genotyping that lets the trial run with ~120 enriched patients instead of ~360 unstratified is a clear win — and is anyway required to identify Q141K homozygotes (~5–25% of carriers depending on population) for the homozygous arm. See [`androgen-urate-axis.md`](./androgen-urate-axis.md) for the male-demographic ceiling that interacts with this stratification, and [`supplements-stack.md`](./supplements-stack.md) for ABCG2-inhibitor counter-indications that should be exclusion criteria at enrollment.

---

## Tissue selectivity matters

ABCG2 is expressed at multiple barrier sites with different physiological roles:

| Tissue | ABCG2 role | Inducing it does what? |
|---|---|---|
| Intestinal apical membrane | Effluxes urate, drugs, xenobiotics into gut lumen | **Good for urate platform** |
| Renal proximal tubule | Effluxes urate from cell into urine | Good for urate (parallel renal sink) |
| Blood-brain barrier | Effluxes drugs out of brain (protective) | **Bad** — reduces CNS penetration of e.g. statins, some psychotropics, some antibiotics |
| Placenta | Effluxes drugs from fetal circulation | Clinically irrelevant for adult gout |
| Hepatic canalicular membrane | Effluxes substrates into bile | Mixed — affects drug clearance kinetics |

**Pick gut-selective inducers, not pan-tissue ones.** The HNF4α and PPARγ axes are relatively gut-enriched (PPARγ also adipose/liver but minimal BBB). PXR is the worst — gut/liver/BBB simultaneously, so rifampicin is a no-go for chronic use.

A patient on chronic CNS-active medication (e.g., SSRIs, antipsychotics, anti-epileptics) should be cautious about pan-tissue ABCG2 inducers — measurable drug-level changes can result.

---

## The supplements-stack contradiction

Several compounds in [`supplements-stack.md`](./supplements-stack.md) are functional ABCG2 inhibitors at typical supplement doses, even though they were added for anti-NLRP3 or anti-inflammatory reasons. **For male gout patients on TRT or supraphysiological clomid (the highest-leverage demographic), the stack may be working pharmacologically against the platform thesis.**

Documented functional ABCG2 inhibitors at supplement-relevant doses:

| Compound | Inhibition tier | Source |
|---|---|---|
| Curcumin | Established BCRP/ABCG2 inhibitor in vitro (Ki ~5–10 μM). At 500–1000 mg supplement doses, gut-lumen concentrations easily reach this. | Pharmacology literature, multiple in vitro studies |
| Quercetin | Substrate/inhibitor at low μM (functional); transcriptional upregulation in chronic dosing (mixed). Net effect on gut sink: probably negative acutely. | Pharmacology + nutritional biochemistry literature |
| EGCG | Functional BCRP inhibitor in pharmacology assays. Yu et al. 2024 (*Food Funct*, PMID 38757391) showed mouse PO-induced hyperuricemic model net-favorable effect on ABCG2/URAT1/GLUT9 expression at the tissue level — direction opposite to the in vitro inhibition story. Net clinical effect on gut sink: unresolved. | Mixed: pharmacology in vitro vs. animal model in vivo |
| Genistein / soy isoflavones | Established BCRP substrate-inhibitor. Dietary intake from natto/miso is much smaller than supplement doses. | Pharmacology literature |

**Practical inference for high-T or Q141K-positive patients:** avoid high-dose curcumin and quercetin acutely when the gut sink matters most (post-meal urate spikes, fructose challenges, etc.). Dietary-level intake of these compounds (turmeric in food, onions, tea) is unlikely to be problematic; supplement-grade doses are the concern.

This also surfaces a research-level open question: how much of the "non-responder" rate in nutraceutical gout RCTs is explained by ABCG2-inhibitor co-supplementation rather than by per-compound efficacy failure?

---

## Human clinical evidence — what the RCTs actually show

**Dose-anchoring** is essential because in vitro and animal effect sizes don't always translate.

### Non-CKD adults — fiber/DASH effect is real but modest

Juraschek et al. 2021, *Arthritis & Rheumatology* ([DOI](https://doi.org/10.1002/art.41614), PMID 33615722): secondary analysis of the DASH feeding study, n=327 adults with mild-to-moderate hypertension.

- DASH diet (high fiber + low-fat dairy): mean serum UA reduction **0.25 mg/dL** vs. control (p=0.004)
- Fruit-and-Vegetables diet alone: 0.17 mg/dL reduction (p=0.051, borderline)
- **Effect dose-dependent on baseline UA severity:**
  - UA <5: 0.08 mg/dL reduction
  - UA 5–5.9: 0.12
  - UA 6–6.9: 0.42
  - UA 7–7.9: 0.44
  - UA ≥8: **0.73 mg/dL** reduction (P-trend = 0.04)

**Clinical Trial.** This is gold-standard evidence. The effect is small but reproducible and dose-dependent on baseline severity, which is exactly the pattern expected from a mechanism that opens the gut sink against a variable starting load.

### CKD/dialysis — mixed; meta-analysis says null for UA specifically

He et al. 2021, *European Journal of Nutrition* ([DOI](https://doi.org/10.1007/s00394-021-02669-y), PMID 34491388): randomized crossover trial of inulin-type prebiotics in 16 peritoneal dialysis patients, 12 weeks.

- Serum UA reduced ~10% in prebiotic phase vs. placebo (p=0.047)
- Mechanism attributed to enhanced fecal UA degradation (microbial uricolysis), not increased renal excretion
- Microbiota changes: enrichment of purine-degrading species (*Anaerostipes caccae*, *Clostridium* species)

**Clinical Trial** (small, single-center).

Khosroshahi et al. 2019, *Nutrition & Metabolism* ([DOI](https://doi.org/10.1186/s12986-019-0343-x), PMID 30911321): RCT of resistant starch in 44 maintenance hemodialysis patients, 8 weeks. Reduced creatinine and uric acid (p<0.05). Reduced p-cresol. Smaller study, supportive.

**But** Wathanavasin et al. 2025, *Toxins* ([DOI](https://doi.org/10.3390/toxins17020057), PMID 39998074) — meta-analysis of 21 RCTs and 700 CKD patients on dietary fiber (6–50 g/day, ≥4 weeks):

- Significant reductions: **p-cresyl sulfate, indoxyl sulfate, BUN, IL-6, TNFα**
- **No significant reduction in serum uric acid** (or TMAO, hs-CRP)

**Clinical Trial — Meta-Analysis.** Across the broader CKD literature, fiber lowers other uremic toxins and inflammation but the UA signal does not survive aggregation.

**Reconciliation:** in advanced CKD, reduced renal clearance dominates the UA balance. Even if gut ABCG2 is upregulated, the systemic UA pool is dominated by impaired filtration. The Juraschek/DASH effect was in non-CKD adults — the gut-sink lever has room to matter when renal function is intact. The platform thesis applies to non-CKD gout patients first; CKD is a confounding context.

---

## Engineering implications

### For the engineered koji (uricase + lactoferrin endgame strain)

Three potential additions to the koji platform that would couple substrate-supply (ABCG2 induction) with substrate-degradation (uricase):

1. **Glucoraphanin co-production.** *A. oryzae* can be cultured on cruciferous substrates (or engineered to produce glucoraphanin from glucose precursors). Glucoraphanin is the sulforaphane precursor; gut myrosinase from cruciferous-resident bacteria converts it to active sulforaphane. Co-delivery of uricase + glucoraphanin would pair "degrade urate in lumen" with "induce more urate transport into lumen" in a single product. **Speculative — synthetic biology feasibility not yet assessed for this specific coupling.**

2. **Resistant-starch-rich substrate.** The koji rice itself is the substrate. Engineering or selecting rice strains with higher resistant-starch content → more colonic butyrate → more PPARγ drive on ABCG2. The protein/enzyme delivery vehicle becomes a fiber-delivery vehicle simultaneously. **Mechanistically plausible; needs quantification of incremental SCFA yield from engineered vs. wild-type substrate.**

3. **Tryptophan-pathway probiotic co-strain.** *L. reuteri* or similar AhR-agonist-producing strain co-formulated with the engineered *S. boulardii* or *S. cerevisiae* uricase strain. Each contributes a different mechanism to the gut sink. **Speculative — strain compatibility under fermentation conditions and survival post-ingestion not yet established.**

### For the supplements stack catalog

Per-compound stack-interaction fields including ABCG2 status should be a required field for any new compound considered for [`supplements-stack.md`](./supplements-stack.md). The four functional inhibitors documented above are the current contradiction set; new entries that meet that pharmacology profile should carry a counter-indication note for high-T or Q141K-positive readers.

---

## Open research questions

1. **Q141K × fiber differential response.** Predicted but untested: Q141K-positive gout patients should show larger UA reduction with fermentable fiber than wild-type-positive patients, because butyrate hits both PPARγ-induction and HDI-rescue. A pharmacogenomic-stratified RCT (n ~120, baseline UA ≥7 mg/dL, stratified Q141K hetero/wild-type by on-site CLIA-grade rs2231142 PCR genotyping at enrollment — see §6 for genotype-source rationale, 12-week inulin or equivalent) would resolve this. Estimated cost: $150K, 6 months. High platform-relevance.

2. **Tissue-selective PPARγ agonists.** Pharmacology question: are there PPARγ agonists with gut-enrichment selectivity (sparing adipose, liver, BBB)? Selective PPARγ modulators (SPPARMs) are an active drug-development area; some have differential tissue activity. Worth a desk review.

3. **Engineered koji + glucoraphanin co-production.** Synthetic biology desk review: is co-expression of glucoraphanin biosynthetic pathway feasible in *A. oryzae*? The plant pathway involves several enzymes; whether a fungal host can support it is open.

4. **EGCG net effect on the gut sink.** Yu 2024 (PMID 38757391) shows favorable in vivo phenotype despite EGCG being a known functional ABCG2 inhibitor in vitro. Resolution requires direct in vivo measurement of gut ABCG2 protein/function before and after EGCG dosing in a relevant model.

5. **Inflammation-suppression overlap with androgen suppression.** TNFα and androgens act independently on ABCG2 expression. For patients with both high T and chronic inflammation (e.g., Hashimoto's), is the suppression additive or saturating? Animal model question; can be tested with TNFα + DHT co-treatment vs. either alone.

6. **Stack-level audit of nutraceutical gout RCT non-responders.** Hypothesis: a measurable fraction of the ~30% non-responder rate in fiber/polyphenol gout RCTs is explained by ABCG2-inhibitor co-supplementation in those participants. Tractable as a meta-analytic question if the RCTs reported concomitant supplement use (often they do).

---

## Provenance and citation tier

All claims tagged with evidence level: **Clinical Trial / Animal Model / In Vitro / Mechanistic Extrapolation**. Primary sources for the most actionable claims:

- **Transcriptional regulation map:** Gorczyca & Aleksunes 2020 ([DOI](https://doi.org/10.1080/17425255.2020.1732348), PMID 32077332) — review of TF-mediated BCRP regulation across tissues.
- **Microbiome-transporter axis:** Rzeczycki et al. 2025 ([DOI](https://doi.org/10.3390/ijms262411897), PMID 41465322) — recent review specifically on gut microbiota → intestinal drug transporters via SCFAs / bile acids / indole metabolites.
- **PPARγ as the wild-type ABCG2 induction mechanism:** Xie et al. 2020 ([DOI](https://doi.org/10.1038/s41401-020-0402-x), PMID 32555444) — primary study, rat in vivo + Caco-2 in vitro.
- **Q141K trafficking defect:** Saranko et al. 2013 ([DOI](https://doi.org/10.1016/j.bbrc.2013.06.054), PMID 23800412).
- **HDI rescue of Q141K:** Basseville et al. 2012 ([DOI](https://doi.org/10.1158/0008-5472.CAN-11-2008), PMID 22472121).
- **TNFα suppression of intestinal ABCG2:** Ferrer-Picón et al. 2020 ([DOI](https://doi.org/10.1093/ibd/izz119), PMID 31211831).
- **Animal model gout efficacy:** Li et al. 2023 ([DOI](https://doi.org/10.1016/j.biopha.2023.114568), PMID 36948133).
- **Human RCT — DASH/fiber:** Juraschek et al. 2021 ([DOI](https://doi.org/10.1002/art.41614), PMID 33615722).
- **Human RCT — inulin in CKD (positive):** He et al. 2021 ([DOI](https://doi.org/10.1007/s00394-021-02669-y), PMID 34491388).
- **Meta-analysis — fiber in CKD (UA null):** Wathanavasin et al. 2025 ([DOI](https://doi.org/10.3390/toxins17020057), PMID 39998074).
- **NFIB regulation:** Solbakk et al. 2025 ([DOI](https://doi.org/10.1016/j.dmd.2025.100100), PMID 40554316).

Information retrieved via PubMed on 2026-04-26.
