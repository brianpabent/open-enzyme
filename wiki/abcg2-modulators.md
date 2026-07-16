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

This page maps the pharmacological levers on ABCG2 in the gut: what suppresses it (closing the gate), what induces it (opening the gate), what specifically rescues the common gout-associated ABCG2 variant Q141K, and where the existing supplement stack accidentally fights the gut-lumen-sink mechanism.

The landscape was characterized through PubMed scans on 2026-04-26 with primary-source verification. Evidence tiers are tagged inline.

---

## Two distinct modulation modes — keep them separate

### Inflammation is not directionally uniform across tissues

ABCG2 and NLRP3 should not be treated as independent “good transporter / bad
inflammasome” targets. Direct intestinal-cell work links NLRP3 signaling, PDZK1, and ABCG2,
while gout studies also support compensatory intestinal ABCG2 responses during systemic
urate stress. The direction may depend on cell type, stimulus, timing, and inhibitor.
(In Vitro + Animal Model; human therapeutic consequence unknown.)

Every lead NLRP3 inhibitor intended for combination with a gut-lumen sink should therefore
be screened for total and surface ABCG2 plus functional urate flux in polarized intestinal
cells. See [validation experiment 1.35](./validation-experiments.md#135-enterocyte-nlrp3pdzk1abcg2-tissue-paradox-assay)
and the [multihop gout program](./gout-multihop-research-program.md).

Most ABCG2 literature conflates two mechanisms with opposite implications for the gut-lumen-sink hypothesis. Read every claim with this distinction in mind:

| Mode | What it does | Implication for gut sink |
|---|---|---|
| **Functional inhibition** | Compound binds existing ABCG2 protein and blocks its pumping action. The pump is present but occupied. | **Bad.** Even if there is plenty of ABCG2 in the apical membrane, urate cannot be effluxed into the lumen. Studied heavily in oncology because tumor ABCG2 effluxes chemotherapy drugs. |
| **Transcriptional modulation** | Compound changes how much ABCG2 protein is produced (via nuclear receptors PPARγ, PXR, AhR, Nrf2, or via NFIB and other transcription factors). | **Inducers are good** — more pump = more urate efflux capacity. **Suppressors are bad** — fewer pumps regardless of activity. |

**The same compound can do both, in opposite directions, dose-dependent.** Quercetin is a textbook case: at low μM cytosolic concentrations it is a competitive substrate/inhibitor (functional inhibition), but in some chronic-dosing animal studies it appears to upregulate ABCG2 mRNA (transcriptional induction). Net effect at a given dose is the integrated result, often poorly characterized in the gut-lumen context specifically.

**Q141K trafficking rescue** is a third, distinct mode discussed in §6 — relevant only to carriers of the Q141K polymorphism but mechanistically different from both functional inhibition and transcriptional induction.

> **Quantitative correction (2026-07-13):** [comp-044](./gut-lumen-uricase-physiologic-regime-computational.md) invalidated comp-019's ΔSUA and genotype ordering. Increasing functional ABCG2 can plausibly supply more substrate to a luminal sink, but the magnitude and genotype interaction are unmeasured. The earlier “triple-mechanism” PDB-butyrate claim is also reopened because Basseville did not test PDB-derived butyrate and CBT2.0 carbon fate is unresolved; see [purine-degrading bacteria](./purine-degrading-bacteria.md) and validation experiments [1.14](./validation-experiments.md#114-additive-abcg2-suppression-by-androgens-tnf-butyrate-rescue-lactoferrin-synergy) and [1.37](./validation-experiments.md#137-cbt20-carbon-fate-and-pdb-self-niche-test).

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

This refinement separates supported wild-type induction from Q141K rescue. Pharmacologic HDAC-inhibitor rescue of Q141K is established in vitro, but direct rescue by butyrate is not; no patient group can yet be said to benefit from both butyrate mechanisms.

---

## Suppressors of intestinal ABCG2

What is making the gate leaky in the typical gout patient:

### 1. Sex-dimorphic intestinal ABCG2 — covered in [`androgen-urate-axis.md`](./androgen-urate-axis.md)

**[REFRAMED 2026-05-07 per [comp-016 evidence-mining](./t-abcg2-suppression-evidence-mining-computational.md).]** Earlier framing here described "AR-mediated transcriptional repression of ABCG2 in gut and kidney." The comp-016 17-study primary-literature scan found **zero** primary studies demonstrating direct androgen-driven suppression of intestinal ABCG2 in vivo. No published ChIP-seq locates a classical androgen response element on the ABCG2 promoter. The closest mechanistic anchor (Jeong 2015 LNCaP, PMID 25615818) is an indirect CREB/CRTC2 axis in **prostate cancer cells**, not intestinal epithelium. One in vitro study (Klyushova 2023 Caco-2) shows testosterone INCREASES ABCG2 via PXR/FXR — opposite direction to the prior framing. MacLean 2008 (PMID 18378562) found NO sex difference in healthy rat intestinal ABCG2 across all four segments.

**Updated framing** [refined post-[comp-017](./intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md) full-text re-read 2026-05-07]: Intestinal ABCG2 is sex-dimorphic in a urate-relevant way (Hoque 2020 Nat Commun PMID 32488095 — male Q140K mice show **78% Western-jejunum / 88% combined Western+IHC** intestinal ABCG2 protein loss + severe hyperuricemia; female Q140K mice protected), but the mechanistic driver is **estradiol POSITIVE on the female side via PI3K/Akt** (Yu 2021 Nutr Metab PMID 34144706, In Vitro + Animal Model — **at strong-pharmacological E2 tier (100 µM, 5–6 orders above physiological); magnitude at physiological E2 unestablished per comp-017**), not androgen NEGATIVE on the male side. The male-female asymptote difference at healthy baseline is empirically near-null (MacLean 2008, replicated by Tubic-Grozdanis 2020) and only emerges under disease state (e.g., Q141K-positive gout patients per Hoque 2020) or strong-pharmacological perturbation. The renal arm of the androgen-urate axis IS partially supported (Hosoyamada/Takiue 2010 PMID 20589576: T → URAT1 mRNA in mouse kidney; **NEW per comp-017 full-text re-read: T → URAT1 protein UNCHANGED in non-orchiectomized animals; the actual protein-level renal drivers are Smct1 protein induction + GLUT9 attenuation**) — but this is renal, not intestinal.

**Klyushova 2023 nuance** [post-[comp-017](./intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md) full-text re-read]: ALL three sex hormones (T, E2, P) at all three concentrations (1, 10, 100 µM — lowest active 30–100× above physiological free T) INCREASE Caco-2 ABCG2 via PXR/FXR. This is a **xenobiotic-sensor response, not hormone-receptor-specific**. The "T INDUCES not suppresses" framing direction is correct; the mechanism is xenobiotic-tier promiscuous induction.

**Clinical-cohort anchoring** (cohort-level, mechanism-not-isolated-to-intestine): Sakamoto 2018 (PMID 30557349) reports −0.66 mg/dL serum UA at 6 months ADT (n=150 ADT vs 339 surgery); Yahyaoui 2008 PMID 18349066 confirms FtM cross-sex T administration raises serum UA + decreases FEUA over 2 years. These are real and clinically meaningful but consistent with URAT1 mRNA + Smct1 protein + GLUT9 attenuation (renal mechanism) being the dominant transporter axis affected; they do NOT distinguish the intestinal ABCG2 mechanism. (Clinical — observational, not RCT.)

For SERMs (e.g., clomid): the androgen-driver effect on **renal transporters** propagates as in TRT (clomid raises endogenous T → renal mRNA + Smct1 protein + GLUT9 attenuation); the **intestinal ABCG2** arm of the prior framing is not directly supported by primary literature and should be considered open. The H07 hypothesis ([`hypotheses/H07-clomid-intestinal-er-antagonism.md`](./hypotheses/H07-clomid-intestinal-er-antagonism.md)) proposes clomiphene's intestinal-ER antagonism as the mechanism; sub-claim 2 (clomiphene tissue-specificity at the gut) remains the open core untested by comp-017. (Mechanistic Extrapolation, supported by single-arm clinical observation; intestinal compartment uncertain.)

### 2. Inflammation / TNFα

Ferrer-Picón et al. 2020, *Inflammatory Bowel Diseases* ([DOI](https://doi.org/10.1093/ibd/izz119), PMID 31211831). Patient-derived intestinal organoids (d-EpOCs) treated with TNFα showed **suppressed SLC16A1 (MCT1), ABCG2, and GPR43**, mimicking the expression profile of active IBD biopsies. Critically, IBD-derived organoids were *not* intrinsically less responsive to butyrate — TNFα was the proximal blocker.

**Implication:** chronic low-grade inflammation (Hashimoto's, food sensitivities, IBS, active IBD) produces the same gut ABCG2 suppression that high androgens do, by a parallel mechanism. **In Vitro + clinical biopsy correlation.** Both axes can act simultaneously and additively.

**Lactoferrin as a TNFα-mediated ABCG2 rescue candidate.** Habib et al. 2023 (PMID 37926296; Animal Model) and older Håversen et al. monocyte/macrophage studies document that oral/parenteral lactoferrin suppresses systemic TNFα. The composed mechanism — koji-derived lactoferrin → ↓ local TNFα drive → relief of TNFα suppression of intestinal ABCG2 → ↑ luminal urate substrate → ↑ effective co-expressed uricase activity — is **Speculative** (three Animal Model / In Vitro links, no published experiment in this combined geometry), but it positions lactoferrin as a potential substrate-supply synergist for the gut-lumen-sink platform, not merely a parallel NLRP3 modulator. The direct test is the lactoferrin rescue arm in [`validation-experiments.md §1.14`](./validation-experiments.md#114-additive-abcg2-suppression-by-androgens-tnf-butyrate-rescue-lactoferrin-synergy) — a Caco-2 transwell experiment comparing lactoferrin basolateral rescue vs. butyrate PPARγ-mediated rescue at the worst-case (high TNFα) condition. Full mechanistic write-up in [`lactoferrin.md §4.7`](./lactoferrin.md). (source: lactoferrin.md, koji-endgame-strain.md)

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

***Alistipes indistinctus* / Hippuric acid (PPARγ — microbiome axis)**
- **Mechanism:** *A. indistinctus* produces hippuric acid via aromatic amino acid catabolism. Hippuric acid enhances PPARγ binding to the ABCG2 promoter AND promotes ABCG2 localization to brush border membranes via PDZK1 (a PDZ-domain scaffold that retains ABCG2 at the apical membrane).
- **Anchoring evidence:** *A. indistinctus* gavage decreased serum urate to baseline in mouse models; *A. indistinctus* is depleted in hyperuricemia subjects. (Animal Model + Human Observational — Xu et al. 2024, Cell Host & Microbe 32(3):366-381.e9, PMID 38412863; last author: Yan Liu, Sun Yat-sen Univ.)
- **Practical lever:** *A. indistinctus* is not commercially available as a probiotic. Dietary hippuric acid precursor routes: (1) polyphenol-rich foods (tea, berries, citrus) → gut catabolism → hippuric acid, OR (2) **direct dietary benzoic acid → hepatic glycine conjugation → hippuric acid (no bacterial mediation needed).** Cranberries are unusually high in natural benzoic acid; cranberry juice reliably elevates urinary hippuric acid (the basis of cranberry-UTI lore). A 4-week unsweetened cranberry juice n=1 (~8 oz/day) before/after panel is the cheapest test of whether the hippuric-acid → ABCG2 mechanism moves serum urate at dietary doses, **independent of needing to colonize *A. indistinctus*.** ~$20 cost. (Mechanistic Extrapolation for cranberry route; Animal Model + Human Observational for the hippuric acid mechanism itself.)
- **OE relevance:** This is a second candidate PPARγ → ABCG2 axis, distinct from the strain-specific PDB/carbon-fate hypothesis. Their combined effect is unknown. Test each exposure and ABCG2 response separately before testing a combination. See [purine-degrading-bacteria.md](./purine-degrading-bacteria.md).

**Indole-3-carbinol / DIM (AhR)**
- **Mechanism:** AhR activation; gut-AhR is highly active because the receptor evolved partly to sense gut microbial metabolites.
- **Anchoring evidence:** **In Vitro + Animal Model.** Cruciferous-vegetable consumption epidemiologically associated with lower UA, though mechanism may be multifactorial.
- **Tissue selectivity:** good (gut-enterocyte enrichment of AhR), though hepatic AhR is also active.
- **Caveat:** DIM at high doses (>200 mg/day) has hepatotoxicity case reports. Stay at dietary or moderate-supplement levels.

**Probiotic delivery of AhR-active microbes**
- **Mechanism:** specific *Lactobacillus reuteri* strains, *L. plantarum*, and others produce indole-3-aldehyde (a potent AhR agonist) from dietary tryptophan.
- **Evidence:** **Mechanistic Extrapolation.** Direct urate endpoint untested for probiotic strain selection. Worth investigating.

***Poria cocos* / *Wolfiporia cocos* (茯苓 Fu Ling) — mechanism unidentified, in-vivo evidence robust**
- **Mechanism:** Empirically uncharacterized. Could be transcriptional (PPARγ / HNF4α / AhR / Nrf2 — none tested), chaperone-class trafficking rescue (analogous to UDCA / TUDCA per comp-032), or class I HDAC inhibition (no HDAC isoform was tested). The unidentified mechanism is itself the highest-leverage open question.
- **Anchoring evidence:** Sun et al. 2021, *Front Pharmacol* (PMID 33651969). Hyperuricemic mouse model. Both ethanol and water extracts significantly elevated intestinal ABCG2 mRNA + protein. Water extract effect magnitude **exceeded benzbromarone positive control** (p < 0.01). Concurrent UA-lowering via XO inhibition + renal protection. **Animal Model.**
- **Five computationally predicted bioactives** (PubChem CIDs 267, 277, 13824, 15730, 5759) docked to ABCG2; in vitro validation not yet performed. Pachymic acid mentioned only as HPLC reference standard, not implicated as active agent.
- **Traditional context:** Poria cocos is a canonical ingredient of Si Miao San (the gout-indicated TCM formula already surveyed by comp-013) and Wu Ling San (the canonical urinary-tract / fluid-metabolism formula). Per comp-013's `inputs/compounds.json`, Poria cocos was implicitly included via the Si Miao San source citation but NOT separately spawned as a compound source — exactly the formula-completeness gap flagged in the 2026-05-19 query-framing retrospective audit.
- **Practical lever:** Poria cocos extract is widely available as a TCM supplement (5-15g daily of decoction or 1-3g of standardized extract is the canonical dose range). Mechanism uncertainty makes off-label dosing for ABCG2 induction premature.
- **Tissue selectivity:** Not characterized.
- **Next move:** Caco-2 transwell assay (sister to §1.14 butyrate dose-response arm) — pachymic acid + polyporenic acid C + dehydroeburicoic acid panel against ABCG2 expression + Q141K trafficking. Marginal cost <$2K on existing infrastructure. **High platform-relevance: closes the mechanism question on a TCM-grade compound that already has robust in-vivo HUA evidence.**

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

**Implication for the gut-lumen-sink hypothesis:**

Butyrate is an HDAC inhibitor and can induce wild-type ABCG2 through PPARγ. For Q141K-positive patients, two distinct hypotheses must not be conflated:

1. **PPARγ-mediated induction** of any wild-type allele (most Q141K carriers are heterozygous)
2. **Proposed HDI-mediated trafficking rescue** of the Q141K variant, not yet demonstrated for butyrate

The first route has supporting evidence; the second is mechanistic extrapolation from other HDAC inhibitors. Whether Q141K carriers respond more strongly to fiber is therefore an open test, not an established genotype-specific lever.

A pharmacogenomic-stratified study could test the differential-response hypothesis, but serum UA alone would not identify the mechanism; exposure, surface trafficking, and functional urate flux are required.

**Attribution and concentration caveat (corrected 2026-07-13):** Basseville 2012 established pharmacological/chemical-chaperone rescue of Q141K ABCG2, not direct rescue by 1–5 mM butyrate. Butyrate is a proposed food-grade HDAC-directed test compound. Its ability to reproduce Q141K surface trafficking and functional urate efflux—and the epithelial exposure required—must be established directly in validation §1.14 before any in-vivo rescue claim.

**Genotype-source framing — clinical, not consumer.** The trial must generate its own genotype data at enrollment via a CLIA-certified clinical PCR assay for rs2231142 (Quest, LabCorp, or equivalent single-SNP genotyping; ~$40–80 per patient at clinical-lab pricing). Consumer-grade genotype exports (23andMe, Ancestry, etc.) are explicitly excluded as the data source — not as a personal-preference call but for trial-design rigor: reproducibility, documented assay performance, sample-chain-of-custody, and CLIA-grade QA are all preconditions for a publishable pharmacogenomic stratification. The trial framing is therefore agnostic at recruitment (no presumed prior genotype knowledge); patients are screened, genotyped on-site, and assigned to arms by the trial's own assay.

**Population-frequency caveat for trial design.** Q141K allele frequency varies substantially by ancestry. A pharmacogenomic fiber trial should pre-specify population and power genotype strata, but it must test rather than assume a Q141K-specific butyrate response or allele-dose scaling.

On-site clinical genotyping is still required for a publishable stratified study. Sample size must be calculated from pilot data rather than the earlier assumed Q141K-conditional effect.

### Pharmacological-chaperone route — orthogonal small-molecule rescue (added 2026-05-16)

Pharmacologic HDAC-inhibitor rescue is one demonstrated in-vitro strategy for Q141K; butyrate is only a candidate within that strategy. A distinct hypothesis is a **pharmacological chaperone** that binds and stabilizes the misfolded protein. CFTR correctors provide class precedent, but no validated ABCG2 Q141K candidate exists.

This route is mechanistically orthogonal to the butyrate / HDAC track: a chaperone restores native folding *directly*, without needing microbiome-mediated HDAC inhibition or PPARγ-mediated transcriptional induction of a wild-type allele. Implications:

- Works in Q141K homozygotes (no wild-type allele to induce — HDI rescue still applies, but PPARγ induction does not).
- Independent of gut-microbiome state (no dependence on fiber intake, SCFA production capacity, or PDB colonization).
- Daily-pill modality via compounding pharmacy if a hit is found among FDA-approved molecules (off-label / 503A) — see [`compounding-pharmacy-track.md`](./compounding-pharmacy-track.md).
- Stacks additively with the HDI rescue (different mechanism, same target outcome).

The full chassis-pending entry is at [`chassis-pending-interventions.md` §7 "Pharmacological chaperones for ABCG2 Q141K folding rescue"](./chassis-pending-interventions.md). The cheapest first move — AlphaFold Q141K structure + virtual screen of FDA-approved molecules — was run as [comp-032](./abcg2-q141k-chaperone-screen-computational.md) (2026-05-16) and then **superseded by [comp-047](./abcg2-q141k-chaperone-rescreen-computational.md) (2026-07-14, real AutoDock Vina docking) → INCONCLUSIVE.** comp-032's GREEN was a descriptor/class-prior heuristic whose positive-control validation was tautological (comp-review 2026-07-13); when comp-047 re-ran the screen with real docking and no class prior, the CFTR-corrector positive controls **failed to earn rank** (0/4). **The list below is comp-032's prior-ranked hypotheses — NOT validated wet-lab priorities, NOT empirically supported chaperone candidates.** It is retained only as a hypothesis-generation starting point for a folding-ΔΔG or wet-lab study; do not act on it as a ranking:

1. **Lumacaftor** (Tier 2, CFTR corrector) — strongest mechanistic prior; same ABC superfamily; on-patent for CF (Vertex), navigate patent landscape for off-label 503A
2. **Tafamidis** (Tier 2, TTR tetramer stabilizer) — aromatic-acid stabilizer at hydrophobic interface; misfolded-state selective
3. **Ursodiol / UDCA** (**Tier 1**, bile acid chaperone) — broad ER-stress chaperone via ATF6/Hsp70; F508del-CFTR rescue precedent; off-patent USP/NF monograph
4. **Diflunisal** (**Tier 1, lowest-friction first call** — off-patent NSAID with USP/NF monograph + off-label ATTR-stabilization precedent) — anionic at pH 7.4, strongest electrostatic match for Q141K +1 pocket
5. **TUDCA** (Tier 2, bile acid chaperone) — CNS-penetrant; F508del-CFTR + ALS-clinical-trial precedent

**The Q141K folding-rescue *route* remains an open hypothesis, but neither comp-032 nor comp-047 supplies a validated candidate — so no compounding-pharmacy conversation is warranted yet.** Rigid-receptor docking cannot discriminate chaperones here (mechanism mismatch: a chaperone works by stabilizing a folding intermediate / raising ΔTm, which docking to a static structure can't see). The real next move is a folding-ΔΔG calculation (MD / Rosetta on the Q141K mutant) or, more decisively, a wet-lab Q141K trafficking-rescue assay in a Caco-2 Q141K-transfected line (sister to the §1.14 butyrate dose-response arm — same Caco-2 infrastructure) paired with basolateral→apical urate flux and an ABCG2-inhibition counterscreen. Any compounding-pharmacy partner conversation is gated behind that wet-lab result (per comp-review 2026-07-13).

---

## The substrate-supply chokepoint — the sink and the Q141K rescue are one question

Everything on this page treats ABCG2 modulation as a lever. It is worth naming *why* that lever is load-bearing: the [gut-lumen uricase sink](./gut-lumen-sink.md) can only degrade urate that ABCG2 delivers to the lumen. **The sink's substrate supply is this pump's output.** So the Q141K rescue axis and the gut-lumen-sink thesis are not two parallel tracks — they share one bottleneck. Q141K throttles apical ABCG2 trafficking, so in a Q141K carrier the pump that fuels the sink is throttled, and the platform's core question collapses to one: does the engineered strain's uricase output exceed the Q141K-limited ABCG2 flux, or is the transporter the rate-limiter?

If transporter supply proves rate-limiting, WT induction and Q141K rescue become separate engineering questions. The shared wet-lab resolver is [`validation-experiments.md` §1.14](./validation-experiments.md); no rescue layer is load-bearing until that assay establishes functional urate flux.

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

Several compounds in [`supplements-stack.md`](./supplements-stack.md) are functional ABCG2 inhibitors at typical supplement doses, even though they were added for anti-NLRP3 or anti-inflammatory reasons. **In androgen-dominant contexts, the stack may work pharmacologically against the gut-lumen-sink mechanism.**

Documented functional ABCG2 inhibitors at supplement-relevant doses:

| Compound | Inhibition tier | Source |
|---|---|---|
| Curcumin | Established BCRP/ABCG2 inhibitor in vitro (Ki ~5–10 μM) — **and confirmed in vivo**: oral curcumin acts as a selective intestinal BCRP inhibitor in cynomolgus monkeys ([Karibe 2018, PMID 29358184](https://doi.org/10.1124/dmd.117.078931)). Despite curcumin's chemical instability, functional gut inhibition survives in a live primate — the **strongest** case in this table (caveat: substrates were sulfasalazine/rosuvastatin, **not urate**). | In vitro (multiple labs) + **Animal Model in vivo (primate)** |
| Quercetin | Substrate/inhibitor at low μM (functional); transcriptional upregulation in chronic dosing (mixed). Net effect on gut sink: probably negative acutely. | Pharmacology + nutritional biochemistry literature |
| EGCG | Functional BCRP inhibitor in pharmacology assays. Yu et al. 2024 (*Food Funct*, PMID 38757391) showed mouse PO-induced hyperuricemic model net-favorable effect on ABCG2/URAT1/GLUT9 expression at the tissue level — direction opposite to the in vitro inhibition story. Net clinical effect on gut sink: unresolved. | Mixed: pharmacology in vitro vs. animal model in vivo |
| Genistein / soy isoflavones | Established BCRP substrate-inhibitor. Dietary intake from natto/miso is much smaller than supplement doses. | Pharmacology literature |

**The EGCG paradox is not a one-off — it is a candidate tea-polyphenol class pattern (added 2026-06-01).** The EGCG in-vitro-inhibition / in-vivo-favorable split (above) is mirrored by its black-tea cousin: **theaflavins** are ABCG2/BCRP *substrates* in vitro (not inhibitors) yet *up-regulate* ABCG2 at the gene level in hyperuricemic mice while lowering serum urate (Tai et al. 2020, *J Funct Foods* 66:103803, attributed to Nrf2/HO-1 — see [`theaflavins.md` §2](./theaflavins.md)). Two independent tea polyphenols thus show the same pattern: acute pharmacological inhibition in a dish, net-favorable ABCG2 phenotype in a live animal. The unifying hypothesis is **hormetic, Nrf2-driven transcriptional up-regulation under chronic exposure** — the same mechanism by which [sulforaphane](./supplements-stack.md) (a corpus-documented ABCG2 *inducer*) works. This places EGCG and theaflavins provisionally in the Nrf2-inducer bucket rather than the net-inhibitor bucket, *for chronic dietary exposure*. **This remains a hypothesis, not a resolution** (per the open question below): the in vivo data are rodent and transcript-level, the Nrf2 mechanism is inferred, and the acute inhibition is real at high concentrated-extract doses (hence the high-dose stratification rows below). The dose-and-chronicity axis is the load-bearing variable — dietary tea plausibly favorable, mega-dose extract plausibly the opposite.

**Risk-tier stratification** (propagated from `supplements-stack.md` §"Stack-level contradictions" 2026-04-27; updated framing 2026-05-05):

| User profile | ABCG2 status | Risk tier | Practical implication |
|---|---|---|---|
| Q141K homozygote + androgen-suppressed (TRT / SERM / AAS) + high-dose flavonoid (>500 mg quercetin OR >600 mg EGCG OR >500 mg curcumin) | Triple-hit suppressed | **Highest research concern** | Treat transporter capacity as a prospective vulnerability and control high-dose inhibitor exposure in experiments. Do not infer that fiber or butyrate rescues Q141K; no wild-type allele remains for the supported WT-induction route. |
| Q141K heterozygote OR androgen-dominant (high-T, no SERM) + supplement-grade flavonoid | One axis suppressed + acute pharmacological inhibition | **High concern** | Meaningful gut-sink narrowing during the dose window. Time inhibitor flavonoids away from urate spikes (post-fructose meals, peri-flare). Acceptable with UA monitoring. |
| Wild-type ABCG2 + supplement-grade flavonoid | Pharmacological inhibition only | **Moderate concern** | Net effect dose- and chronicity-dependent. Watch UA trajectory after introduction; down-titrate if UA rises. |
| Any genotype + dietary-level flavonoid (onions, tea, turmeric, fermented soy at normal food portions) | Sub-Ki gut concentrations | **Minimal concern** | No restriction. Food-level intake is unlikely to be clinically significant for the gut sink. |

Stratification matters because a blanket "avoid quercetin" message undermines compliance for the largest cohort (wild-type genotype, dietary intake) where the risk is essentially zero. The clinically meaningful signal concentrates in androgen-suppressed Q141K-positive readers at supplement-grade doses.

**Practical inference for high-T or Q141K-positive patients:** avoid high-dose curcumin and quercetin acutely when the gut sink matters most (post-meal urate spikes, fructose challenges, etc.). Dietary-level intake of these compounds (turmeric in food, onions, tea) is unlikely to be problematic; supplement-grade doses are the concern.

This also surfaces a research-level open question: how much of the "non-responder" rate in nutraceutical gout RCTs is explained by ABCG2-inhibitor co-supplementation rather than by per-compound efficacy failure?

### Gut-luminal metabolic stability resolves the CBD-vs-flavonoid inconsistency (added 2026-07-13)

The corpus contained an unstated contradiction: [`cannabinoids-terpenes.md`](./cannabinoids-terpenes.md) argues that CBD's poor oral bioavailability does **not** yield a high functional gut-luminal concentration, while the flavonoid ABCG2-inhibitor warning above rests on the opposite premise (poor absorption ⇒ high, functionally relevant luminal concentration). Both can be true — the discriminating variable is **gut-luminal metabolic stability × gut segment × in-vivo net direction**. A 2026-07-13 multilingual literature scan ([`logs/cbd-vs-flavonoid-gut-degradation-lit-scan-2026-07-13.md`](../logs/cbd-vs-flavonoid-gut-degradation-lit-scan-2026-07-13.md)) resolved each compound — the upshot is **stratify per compound, not one class rule**:

| Compound | Gut-luminal fate | Premise (poor absorption ⇒ real gut-ABCG2 inhibition) | Bucket |
|---|---|---|---|
| **Curcumin** | Chemically unstable, colonic biotransformation — **but** functional inhibition demonstrated in a live primate ([Karibe 2018, PMID 29358184](https://doi.org/10.1124/dmd.117.078931)) | **HOLDS — strongest case** | Inhibitor (in vivo-confirmed) |
| **Quercetin** | Dietary = glycosides → obligate bacterial deglycosylation + C-ring fission; genuine low-µM BCRP inhibitor in the **proximal** small intestine right after a dose, but catabolized before the colon ([Rechner 2004, PMID 14744633](https://doi.org/10.1016/j.freeradbiomed.2003.10.008); Di Pede 2020) | **PARTIAL** — holds proximally/acutely, overstated for colonic/sustained concentration | Inhibitor (proximal-gut window only) |
| **EGCG** | Unstable at intestinal pH → gallocatechin + gallic acid; ring-fissioned by microbiota; net-**favorable** ABCG2/URAT1/GLUT9 phenotype in vivo ([Yu 2024, PMID 38757391](https://doi.org/10.1039/d3fo05606f)) | **MOST OVERSTATED** — parent doesn't persist; in vivo net-favorable | Move to **Nrf2-inducer bucket** (with theaflavins) |
| **CBD** | Not degraded by colonic microbes as previously stated — actual fate is **lipid/fecal sequestration + gastric-acid lability + host metabolism**; and CBD is not an ABCG2 inhibitor anyway (target P2X7/NLRP3) | N/A — never an ABCG2-inhibitor story | Neither |

**The class warning does not stand as written — it needs per-compound stratification.** Curcumin earns the strongest warning (in vivo primate); quercetin is a real but *proximal-gut-only* inhibitor; EGCG likely belongs with the favorable Nrf2 inducers (consistent with the theaflavins reclassification, §"The EGCG paradox is not a one-off" above). The CBD "gets degraded" logic generalizes cleanly to EGCG, partly to quercetin, and **not** to curcumin (the counterexample).

**Load-bearing evidence gap:** no study measures the actual **free luminal concentration** of any of these compounds, segment-resolved along the gut after a realistic dose, against **urate** efflux via intestinal ABCG2 (Karibe used drug substrates; the EGCG in vivo data measure transporter *expression*, not acute luminal inhibition). So `[free compound]_lumen` vs `Ki(ABCG2-for-urate)` per gut segment remains unmeasured for all four — the quantity every warning above ultimately depends on. (source: CBD-vs-flavonoid gut-degradation lit scan 2026-07-13; per-compound PMIDs in the scan log.)

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

**Reconciliation:** in advanced CKD, reduced renal clearance dominates the UA balance. Even if gut ABCG2 is upregulated, the systemic UA pool is dominated by impaired filtration. The Juraschek/DASH effect was in non-CKD adults—the gut-sink lever has more room to matter when renal function is intact. CKD is a confounding context for this mechanism.

---

## Engineering implications

### For the engineered koji (uricase + lactoferrin endgame strain)

Three potential additions to the koji configuration that would couple substrate supply (ABCG2 induction) with substrate degradation (uricase):

1. **Glucoraphanin co-production.** *A. oryzae* can be cultured on cruciferous substrates (or engineered to produce glucoraphanin from glucose precursors). Glucoraphanin is the sulforaphane precursor; gut myrosinase from cruciferous-resident bacteria converts it to active sulforaphane. Co-delivery of uricase + glucoraphanin would pair "degrade urate in lumen" with "induce more urate transport into lumen" in a single product. **Speculative — synthetic biology feasibility not yet assessed for this specific coupling.**

2. **Resistant-starch-rich substrate.** The koji rice itself is the substrate. Engineering or selecting rice strains with higher resistant-starch content → more colonic butyrate → more PPARγ drive on ABCG2. The protein/enzyme delivery vehicle becomes a fiber-delivery vehicle simultaneously. **Mechanistically plausible; needs quantification of incremental SCFA yield from engineered vs. wild-type substrate.**

3. **Tryptophan-pathway probiotic co-strain.** *L. reuteri* or similar AhR-agonist-producing strain co-formulated with the engineered *S. boulardii* or *S. cerevisiae* uricase strain. Each contributes a different mechanism to the gut sink. **Speculative — strain compatibility under fermentation conditions and survival post-ingestion not yet established.**

### For an engineered LBP peer track (commercial-pharmaceutical chassis)

The supported LBP rationale is sustained local butyrate for PPARγ-mediated wild-type ABCG2 induction. Direct Q141K trafficking rescue by butyrate is an unvalidated extension and cannot make the route genotype-agnostic. Oral and LBP delivery also require measured colonic and epithelial exposure.

**An engineered colonically resident butyrate producer is a testable bioavailability hypothesis, not a solved delivery system.** *Faecalibacterium prausnitzii* is one candidate chassis because it natively produces butyrate in the colon, but the route requires a workable engineering toolkit plus measured colonization density, butyrate titer, dosing durability, and epithelial exposure. No quarterly-capsule or continuous-crypt-exposure claim is established.

This is a **commercial-pharmaceutical research track**, not a home-fermentation route: an obligate-anaerobe product would require anaerobic manufacturing, stabilization, and an LBP regulatory path. See [`engineered-lbp-chassis.md`](./engineered-lbp-chassis.md). Patient-population claims remain premature, especially for Q141K, until direct rescue and delivery are demonstrated.

### For the supplements stack catalog

Per-compound stack-interaction fields including ABCG2 status should be a required field for any new compound considered for [`supplements-stack.md`](./supplements-stack.md). The four functional inhibitors documented above are the current contradiction set; new entries that meet that pharmacology profile should carry a counter-indication note for high-T or Q141K-positive readers.

---

## Open research questions

1. **Q141K × fiber differential response.** Open: does fermentable fiber change functional ABCG2 urate flux differently by genotype? A stratified study must measure exposure and transporter function; it cannot assume direct butyrate rescue of Q141K.

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
