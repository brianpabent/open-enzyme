# CFH Y402H × Dietary CP0 Blockade × Gout — Biobank Mining Report — 2026-05-19

Triggered by: `synthesis/queue/` 2026-05-17-connection-3 + experiment-2 (Cluster B4 walkthrough)
Target wiki: `gout-genetic-variants.md` (new CFH row); `complement-c5a-gout.md` §6.3 (mechanism update if warranted)

## Summary

- **The direct hypothesis (CFH Y402H × dietary CP0 blockade × gout) is empirically untested.** No published UK Biobank, All of Us, EPIC-Norfolk, or any other cohort analysis has crossed CFH genotype × dietary polyphenol/flavonoid intake × incident gout. Direct biobank scan (paperclip + UK Biobank Showcase web search) returns zero hits.
- **The closest published analog (CFH × diet × AMD) points the OPPOSITE direction from the OE stratification prediction.** Three independent cohorts (AREDS, NAT2, Klein 2008) report that CFH Y402H **risk-allele carriers do WORSE on antioxidant/zinc and DHA supplementation**, not better — with one paradoxical finding (Vavvas 2018 PNAS, AREDS GTG2: CFH high-risk + no ARMS2 risk had HR 2.9 for NV progression on AREDS formulation vs placebo, p=0.018). This is a substantial complication for the OE prediction. **Critical caveat:** these are zinc/antioxidant/DHA studies, mechanistically distinct from the comp-018 dietary CP0 candidates (rosmarinic acid C3-convertase inhibition, luteolin CH50/AP50, Houttuynia polysaccharide LBP/CP inhibition + NLRP3 suppression).
- **Mechanism evidence for the C5a-NLRP3-IL-1β chain in CFH Y402H carriers is partially established.** Hecker 2023 (PMID 37940657, n=153 healthy) shows CFH 402HH homozygotes have elevated CRP (38% in 3-10 mg/L range vs 10% YH carriers, p=0.037) and depressed CD4+ T cells. Volcik 2008 ARIC (PMID 18292760, n=15,792) shows CFH 402H × hypertension interaction for CHD and ischemic stroke (HRR 1.47 for stroke in 402HH whites). Both are consistent with chronic complement-priming-driven inflammation. Neither study extends to gout incidence or flare severity directly.
- **CFH Y402H allele frequency is more uniformly distributed across populations than the canonical "~30% European, ~7% East Asian" framing suggests.** gnomAD v4: European 39%, African 37%, South Asian 31%, East Asian 6%, Latino/Admixed 18%. The African frequency is comparable to European — relevant for the OE platform's reach assumptions. East Asian frequency is genuinely low (~5-6%), which biases the dietary CP0 stratification toward Western (European + African + South Asian) deployment.
- **Biobank feasibility is high in principle but blocked by access in practice.** UK Biobank Axiom array directly genotypes rs1061170 (resource 149601 SNP list), and gout ICD-10 M10.x outcomes + 24-hr dietary recall + Oxford WebQ dietary fields are all available. The cross-tabulation could be retrieved with an existing data application — but no published analysis has done so, and OE does not currently hold a UK Biobank application. A new application (~£3-9K access fee, ~6-12 months approval) is required to run the analysis directly; the alternative is propose-and-recruit-collaborator route via the existing UK Biobank gout-GWAS groups.

## Direct CFH × diet × gout analyses (the primary target)

**None found.** Three search surfaces, zero hits:

1. **Paperclip semantic + keyword** ("CFH Y402H gout serum urate", "CFH rs1061170 dietary polyphenol flavonoid", "complement factor H Y402H UK Biobank dietary"): 14 paperclip hits returned, all on AMD/CVD/AREDS — none on gout or hyperuricemia.
2. **WebSearch UK Biobank-specific**: returns Major UK Biobank gout × diet analyses (Yokose 2024 ultraprocessed food × gout, Choi 2024 dietary carbohydrates × gout, Major 2018 GCKR/ABCG2 × coffee × gout) but no CFH-stratified analysis. Yokose, Choi, and Major use the Tin 2019 gout PRS or specific transporter SNPs — never CFH.
3. **Multilingual (CNKI/J-STAGE proxy via paperclip Chinese-character search)**: 10 hits on TCM × hyperuricemia, none cross CFH genotype with diet or gout.

**Provenance for the empirical absence:** the closest gout-genetics × diet UK Biobank paper is Yokose 2024 (Rheumatology, [academic.oup.com/rheumatology/article/63/1/165/7147894](https://academic.oup.com/rheumatology/article/63/1/165/7147894)), which constructs a gout PRS from Tin 2019 loci (351 loci, none of which are CFH — CFH is below GWAS significance for gout per Tin 2019 PMID 31578528). This is consistent with `complement-c5a-gout.md` §6.1 — complement-pathway sub-signals are not detected in gout GWAS at current sample sizes because urate-transporter loci dominate.

The absence is a finding: the prediction has not been falsified, but it also has zero direct empirical support and one strongly negative analog (Vavvas 2018, see next section).

## Closest analogs (CFH × diet × AMD/cardio, or CFH × gout without diet)

### CFH × diet × AMD — three landmark studies, conflicting directions

| Study | Cohort, n | Intervention | CFH Y402H × intervention finding | Direction relative to OE prediction |
|---|---|---|---|---|
| **Klein 2008** (Ophthalmology, PMID 18423869) | AREDS, n=876 | Antioxidants + zinc 80 mg/day vs placebo | CFH non-risk allele carriers benefited from supplementation; risk-allele carriers did NOT | **Opposite** of OE prediction |
| **Awh 2013 / Awh 2015** (Ophthalmology, PMID 23972322 / 25200399) | AREDS, n=989 | AREDS formulation | CFH high-risk + no ARMS2 risk (GTG2) had paradoxically WORSE outcomes on AREDS treatment; CFH low-risk + ARMS2 high-risk (GTG3) benefited | **Opposite** of OE prediction |
| **Vavvas 2018** (PNAS, PMID 29311295) | AREDS expanded set, n=802; validation n=299 | AREDS formulation (zinc 80 mg + antioxidants) | Confirms Awh + Klein: GTG2 (high CFH, no ARMS2) HR 2.9 (p=0.018) for NV-AMD progression ON treatment vs placebo. GTG3 (low CFH, high ARMS2) HR 0.50 (p=0.008) — benefit. Bootstrap-validated. | **Opposite** of OE prediction |
| **Merle 2015 NAT2** (PLoS ONE, PMID 26132079) | n=250 neovascular AMD patients | 280 mg DHA/day × 3 years | Significant CFH × DHA interaction (p=0.01). Protective effect of DHA only in CFH 402YY (non-risk homozygous): CNV 38.2% placebo vs 16.7% DHA. CFH 402CC (risk homozygous): CNV 23.1% placebo vs 39.5% DHA — DHA may have HARMED risk-allele carriers. | **Opposite** of OE prediction |
| **Reynolds 2013** (cited in NAT2): omega-3 PUFA dietary intake × AMD | n~1,500 AMD cases | Dietary recall | Protective effect of dietary DHA on geographic atrophy in CFH 402YY only | **Opposite** of OE prediction |
| **Chew 2014 AREDS Report #38** (Ophthalmology, PMID 24974817) | AREDS, n=1,237 | AREDS formulation | NO significant CFH/ARMS2 × treatment interaction detected | Null — contradicts Klein/Awh/Vavvas |

**Why the AMD analog points the wrong way (mechanism analysis).** Vavvas 2018 attributes the paradoxical AREDS × CFH-risk worsening to **zinc-induced complement activation in CFH-risk allotypes**: zinc oligomerizes/inactivates C3 at physiological concentrations, but CFH 402H allotype binds CRP poorly, preventing the CRP-bridged C3b-CFH inactivation pathway. In effect, zinc supplementation pushes complement activation up in CFH risk-allele carriers because their CFH cannot leverage zinc-dependent inactivation. The DHA story is different — DHA reduces CRP and inflammation broadly, but Merle 2015 speculates CFH-risk-allele complement dysregulation may overwhelm the DHA effect at the retinal site.

**Implication for the OE CP0 prediction.** The OE-predicted CP0 intervention is mechanistically distinct from zinc/antioxidants/DHA:

- **Rosmarinic acid** directly inhibits C3 convertase (Englberger 1988, PMID 3198307; IC50 5-10 µM optimal) — physically prevents C3b/C3a/C5 convertase assembly. Mechanism does not require CFH-mediated inactivation.
- **Luteolin** inhibits CP+AP convertases (Zhang & Chen 2008, PMID 18400428; CH50 190 µM / AP50 170 µM) — also CFH-bypass mechanism.
- **Houttuynia cordata polysaccharide** inhibits lectin/classical pathway (Lu 2017 PMID 29404287; CH50 79-318 µg/mL) AND suppresses NLRP3 inflammasome (Li 2025 PMC12254813) — two mechanisms, both CFH-bypass.

If CP0 blockade works by **bypassing** CFH (preventing C3 convertase formation upstream of where Y402H matters), then **CFH Y402H carriers should still benefit** — the dietary intervention provides the regulation their CFH cannot. This is mechanistically distinct from zinc/AREDS, which works **through** complement regulation that requires functional CFH.

However: the AMD evidence is sobering. Three independent cohorts found CFH risk-allele carriers do worse on three different dietary complement-relevant interventions. The mechanism distinction above is a hypothesis, not a demonstrated dissociation. The OE prediction should be re-stated as "mechanistically plausible but empirically untested; one related literature points the opposite direction."

### CFH × gout (no diet stratification)

Direct CFH × gout association evidence: **none in published gout GWAS** (Tin 2019, Major 2018, Kawamura 2019 UK Biobank n=150,542). CFH variants do not reach genome-wide significance in any gout GWAS.

Indirect mechanism evidence:

- **Hecker 2023** (Front Immunol, PMID 37940657, n=153 healthy + 84 dry AMD + 143 nvAMD): CFH 402HH carriers have elevated CRP (38% in 3-10 mg/L vs 10% YH, p=0.037) and lower CD4+ T cells with aging. CRP elevation is upstream of classical complement priming on MSU crystals (`complement-c5a-gout.md` §5).
- **Volcik 2008 ARIC** (PMID 18292760, n=15,792): CFH 402HH × hypertension → HRR 1.47 for ischemic stroke; HRR 1.19-1.28 for CHD in hypertensive 402H carriers. White subgroup only; null in African Americans. Consistent with complement-amplified inflammation in CFH-impaired individuals on top of pre-existing inflammatory risk.

Neither extends to gout incidence or flare severity directly, but both are consistent with the priming-gradient framework in `complement-c5a-gout.md` §6.3.

## CFH Y402H allele frequency anchors

Updated from dbSNP/ALFA/gnomAD v4/1000Genomes/TOPMED (2026 access; primary source: ncbi.nlm.nih.gov/snp/rs1061170 population frequency aggregator):

| Population | C-allele (Y402H risk) frequency | T-allele (non-risk) frequency | Source |
|---|---|---|---|
| **European (ALFA)** | 0.376 | 0.624 | ALFA aggregator |
| **European (gnomAD v4 exomes)** | 0.386 | 0.614 | gnomAD v4 |
| **European (1000G)** | 0.362 | 0.638 | 1000 Genomes Phase 3 |
| **African (ALFA)** | 0.346 | 0.654 | ALFA aggregator |
| **African (gnomAD v4 exomes)** | 0.370 | 0.630 | gnomAD v4 |
| **African (1000G)** | 0.362 | 0.638 | 1000 Genomes Phase 3 |
| **East Asian (ALFA)** | 0.042 | 0.958 | ALFA aggregator |
| **East Asian (gnomAD v4)** | 0.060 | 0.940 | gnomAD v4 |
| **East Asian (1000G)** | 0.049 | 0.951 | 1000 Genomes Phase 3 |
| **South Asian (ALFA)** | 0.297 | 0.703 | ALFA aggregator |
| **South Asian (gnomAD v4)** | 0.306 | 0.694 | gnomAD v4 |
| **Latino/Admixed (ALFA "Lat Am 1")** | 0.322 | 0.678 | ALFA aggregator |
| **Latino/Admixed (gnomAD v4 "American")** | 0.176 | 0.824 | gnomAD v4 |
| **Global (gnomAD v4 exomes)** | 0.364 | 0.636 | gnomAD v4 |

**Three operational corrections** to the canonical wiki framing ("~30-50% European, ~7% East Asian"):

1. **European C-allele frequency is ~36-39%, not 30-50%.** The "30-50%" range in the wiki appears to conflate AMD-case C-allele frequencies (enriched ~50-55% in NAT2 cohort, Merle 2015) with general-population frequencies (~36-39% per gnomAD/ALFA). The 30-50% number should be replaced with "~36-39% in unselected Europeans; up to ~50-55% in clinical AMD cases due to ascertainment bias."
2. **African C-allele frequency is ~35-37%, comparable to European.** The wiki and synthesis-queue framing implicitly treats CFH Y402H as a Western-deployment issue. This is wrong. African-ancestry carriers are roughly as common as European carriers, and the Volcik 2008 ARIC finding (CFH 402H cardiovascular signal absent in African Americans) suggests population-specific effect-direction differences worth flagging separately.
3. **East Asian C-allele frequency is genuinely ~5-6%.** This is the only confirmed-low frequency anchor and biases any CFH-stratified dietary CP0 trial AWAY from East Asian deployment. The OE platform's natural deployment target is the Q141K-rich East Asian gout cohort (per `abcg2-modulators.md` §6); the CFH-stratification axis is structurally a different cohort.

The mechanistic homozygosity rate (CC) at 36% allele frequency is roughly 13% of the population (0.36² = 0.13). At 30% (more conservative end), CC homozygotes are 9%. This is consistent with the CFH Y402H × AMD literature reporting ~10-15% CC homozygous in Caucasian samples.

## Dietary polyphenol → complement-inhibition mechanism evidence

Effect-size anchors per `upstream-complement-modulator-sweep-computational.md` (comp-018) and `comp-020-verification` lineage:

| Compound | Mechanism + target | Effect size | Source | Evidence tier |
|---|---|---|---|---|
| **Rosmarinic acid** | C3 convertase inhibition | IC50 **5-10 µM optimal** in early assay; **137-182 µM in alternate assay formats** | Englberger 1988 (PMID 3198307); Cimanga 1999, Mu 2013 (alternate-assay range) | **In Vitro**, low-bound abstract-tier per the comp-021 verification gate (see `upstream-complement-modulator-sweep-computational.md` ⚠️ assay-format spread caveat) |
| **Rosmarinic acid (in vivo)** | C3-convertase target; whole-animal complement-driven inflammation models | Three independent precedents: rat CVF lung injury (Englberger 1988); rat ADPKD Pkd1-/- (paper TBD); classical paw oedema | comp-018 cross-reference | **Animal Model** |
| **Luteolin** | CP + AP convertase inhibition | CH50 0.19 mM (190 µM) / AP50 0.17 mM (170 µM) | Zhang & Chen 2008 (PMID 18400428) | **In Vitro** |
| **Houttuynia cordata polysaccharide (HCP)** | Lectin + classical pathway inhibition | CH50 **79-318 µg/mL** across crude + purified fractions | Lu 2017 (PMID 29404287); Cheng 2013; Xu 2015 (Chen Daofeng group, 3+ papers) | **In Vitro + Animal Model** |
| **HCP (NLRP3 axis)** | NLRP3 inflammasome suppression in gut-lung axis | H1N1+MRSA coinfection model: improved survival, reduced lung NLRP3 activation | Li 2025 (PMC12254813) | **Animal Model** |
| **Houttuynia cordata (clinical-tier dosing)** | Traditional dietary intake (魚腥草, 어성초, どくだみ); 9-30 g dried herb/day in TCM dosing | No CP-pathway-specific RCT | Cao 2003 traditional dosing references | **Mechanistic Extrapolation** (clinical → CP) |

**Dietary plausibility anchors:**

- Rosmarinic acid sources (rosemary, lemon balm, spearmint, salvia, mentha) are FDA GRAS. Dietary RA intake from a "Mediterranean herb-heavy" eating pattern reaches ~10-50 mg/day. Plasma RA after oral dosing peaks at ~50-200 ng/mL (~0.14-0.55 µM) — at the low end of the disputed Englberger IC50 range. **Whether plasma RA reaches C3-convertase-inhibitory concentrations in vivo is the comp-021 verification gate.**
- Luteolin sources (parsley, thyme, celery, chamomile, broccoli, peppers) — dietary intake ~1-3 mg/day in Western diets, up to ~10 mg/day in Mediterranean. Plasma luteolin peaks at low µM range — well below the Zhang & Chen 2008 CH50/AP50.
- Houttuynia cordata is a culinary herb in southern China, Korea, Japan, Vietnam (eaten fresh or as tea). Traditional clinical dosing 9-30 g/day. No CP-pathway-specific human RCT.

**The honest framing for the OE prediction:** dietary RA + luteolin from a Mediterranean-herb-heavy pattern is mechanistically plausible to reduce CP0 priming, but the plasma-concentration-vs-IC50 gap is real and unresolved (comp-021 is the gating verification). Houttuynia at traditional dietary doses has the strongest mechanism stack (CP + LBP + NLRP3) but is culturally non-Western, which collides with the European/African deployment target above.

## Biobank query feasibility

### UK Biobank — high in principle, blocked by access

**Required data fields (all confirmed available):**

| Field | UK Biobank field/resource | Status |
|---|---|---|
| CFH rs1061170 genotype | Axiom array (resource 149600 BiLEVE / 149601 main); directly typed | Available, n~500,000 |
| Gout outcome | ICD-10 M10.x (HES inpatient + primary care if linked); ULT prescription (Field 20003); 2019 pain questionnaire gout module | Available; recent gout GWAS (med_8325123770db, Wrigley 2020) confirm extraction protocol |
| 24-hr dietary recall | Oxford WebQ (Field 100020-100090 series), 5 administrations × ~210K participants | Available, but only ~211K have ≥1 recall, ~70K have ≥4 |
| Total polyphenol intake | Not a built-in field; derived via Phenol-Explorer database mapping on Oxford WebQ items | Derivable (precedent: Liu 2024 Adv Nutr [pubmed.ncbi.nlm.nih.gov/38740187/]) |
| Flavonoid subclass intake | Derivable via USDA Flavonoid Database mapping on FFQ items | Derivable (precedent: Bondonno 2025 Nature Food, Wood 2024 J Nutr lung/asthma) |
| Rosmarinic acid intake | Not directly recorded; requires Phenol-Explorer mapping on rosemary/sage/oregano/thyme/mint frequency | Derivable but lossy (FFQ herb specificity limited) |

**The technical query (what the analysis would do):**

```
SELECT * FROM ukb_participants WHERE
  rs1061170_genotype IN ('CC', 'CT', 'TT')
  AND has_dietary_recall = TRUE
  AND age_at_recruitment >= 40
  AND ancestry_eur = TRUE  -- and stratified replication in AFR + SAS
CROSS-TABULATED BY:
  total_polyphenol_intake_tertile (or flavonoid intake tertile)
OUTCOME:
  incident_gout_M10x within follow-up window
  serum_urate at baseline (Field 30880)
  CRP at baseline (Field 30710) -- mechanism marker
COVARIATES:
  age, sex, BMI, eGFR, diuretic use, alcohol, ABCG2 Q141K (rs2231142), GLUT9 (rs734553), SLC22A12 (rs121907892)
```

Powering estimate: at gout incidence ~3.2% over ~12-year follow-up in UK Biobank (Yokose 2024), and assuming a CFH × polyphenol interaction effect size similar to the AREDS × CFH AMD interaction (HR 2-3 between extremes), the cross-tabulation is well-powered in the EUR subcohort (~170K with rs1061170 + dietary recall + gout outcome). The AFR subcohort (~6K with all fields) is underpowered for interaction detection but adequate for direction-confirmation.

**The blocker:** OE does not currently hold a UK Biobank data application. Standard application fee is £3,000-9,000; approval typically 6-12 months; data refresh schedule is quarterly. This is not a "subagent + existing biobank data, $0, 1 hour" experiment as the synthesis-queue item-2 framed it. **The honest cost framing is £3-9K + 6-12 months access lag, OR ~3 months collaborator-recruitment lag (e.g., the Merriman group at Otago, Major group at Auckland, Choi group at Massachusetts General, all active UK Biobank gout-genetics groups; some published on `complement-c5a-gout.md`-relevant axes already).**

### All of Us Research Program — feasible, smaller relevant N

- AoU Researcher Workbench provides whole-genome sequence (so rs1061170 is directly available) and EHR-derived gout diagnoses + ASA-24 dietary recall.
- Active gout cohort size as of 2025 is ~12-15K (Wallace 2024 estimate) — smaller than UK Biobank's ~30-50K gout cases, but with better African American and Hispanic/Latino representation. The African-American subgroup is particularly relevant given the CFH C-allele frequency parity with Europeans noted above.
- No published CFH × diet × gout AoU analysis.
- Access requires AoU Researcher Workbench credentialing (free, ~2-4 weeks) — lower friction than UK Biobank.

### EPIC-Norfolk — feasible, niche

- EPIC-Norfolk has detailed FFQ + 7-day food diary on ~25K participants, plus genotyping on a subset (~7K with HumanCoreExome array; rs1061170 imputable).
- Gout outcomes via HES linkage; cases ~1,500 — underpowered for interaction analysis but adequate for direction confirmation in a meta-context.
- Access via the EPIC-Norfolk data access committee, no fee, ~3-6 months.

### Best-fit operational recommendation

**The "no new wet-lab, $0" framing in the synthesis-queue is wrong.** The empirically honest recommendation:

1. **Stage 1 (free, ~2 weeks):** Document the empirical-absence finding and the AMD-analog opposite-direction caveat in `complement-c5a-gout.md` §6.3 and add the CFH row to `gout-genetic-variants.md`. This is the immediate wiki update.
2. **Stage 2 (~3 months, $0 OE cost):** Reach out to the Merriman group (Otago) or the Major/Wrigley group at Auckland (active UK Biobank gout GWAS authors) with a one-page collaboration proposal. Both groups already have UK Biobank applications and gout-extraction pipelines. OE contributes the mechanism framing + comp-018 dietary-CP0 hypothesis; collaborator runs the cross-tabulation in their existing application. Output: a co-authored short report.
3. **Stage 3 (only if Stage 2 doesn't materialize, ~6-12 months + £3-9K):** OE files a UK Biobank application as primary applicant, focused narrowly on the CFH × dietary CP0 × gout question.
4. **Stage 4 (parallel, ~2-4 weeks access):** AoU Researcher Workbench credentialing + initial scoping query on the smaller AoU cohort. Useful as a hypothesis-direction check before committing to UKB.

## Proposed wiki updates

### Update 1 — Add CFH row to `gout-genetic-variants.md` (Category — needs to be created, "Complement regulation")

Insert after Category 4 (NLRP3/IL-1β axis), as a new Category 5 "Complement regulators":

```markdown
## Category 5 — Complement regulators

The complement cascade is the upstream priming signal for the NLRP3 inflammasome on MSU crystals (per [`complement-c5a-gout.md`](./complement-c5a-gout.md) — chokepoint 0). Inherited variation in complement regulators that controls alternative-pathway amplification on non-host surfaces (which MSU crystals functionally are) is mechanistically positioned to modify gout flare severity, even if it has not surfaced in published gout GWAS at current sample sizes (a known sample-size + endpoint-power gap per `complement-c5a-gout.md` §6.1).

| Variant | Gene (chr) | Cascade step | Effect direction | Allele frequency | Evidence tier | OE-platform implication | Canonical wiki page |
|---|---|---|---|---|---|---|---|
| **rs1061170 (p.Tyr402His, Y402H)** | CFH (chr1q31.3) | Alternative-pathway regulation; fluid-phase + host-surface decay-accelerating cofactor for Factor I | Reduces CFH ability to bind C-reactive protein and host glycosaminoglycans; reduces inactivation of surface-deposited C3b → ↑ alternative-pathway amplification → ↑ C5a generation | **C-allele (Y402H risk): European ~36-39%, African ~35-37%, South Asian ~30%, East Asian ~5-6%, Latino ~18-32%** (gnomAD v4 / ALFA / 1000 Genomes). Frequency in AMD case cohorts ~50-55% (ascertainment-enriched, not general-population). | **Clinical Trial** (AMD outcomes only — Hageman 2005 PMID 15870199, Klein 2005 PMID 15761122, Edwards 2005 PMID 15761121, Haines 2005 PMID 15761120). **Mechanistic Extrapolation** for gout — no published gout GWAS signal at genome-wide significance (consistent with `complement-c5a-gout.md` §6.1 explaining the sample-size/endpoint gap); supportive intermediate-phenotype evidence: Hecker 2023 (PMID 37940657, n=153) CFH 402HH → elevated CRP (38% in 3-10 mg/L vs 10% YH carriers, p=0.037) + depressed CD4+ T cells with aging; Volcik 2008 ARIC (PMID 18292760, n=15,792) → CFH 402H × hypertension HRR 1.47 ischemic stroke in whites, null in African Americans. | **Untested in gout; the genotype-stratified dietary CP0 prediction is empirically open.** Predicted (Mechanistic Extrapolation): CFH Y402H carriers should benefit MORE from dietary CP0 blockade (rosmarinic acid C3 convertase inhibition per comp-018, luteolin CH50/AP50, Houttuynia polysaccharide multi-target) than wild-type carriers — same logic as Q141K × butyrate. **⚠️ Counter-evidence from AMD analog:** Klein 2008 / Awh 2013 / Vavvas 2018 (PMID 29311295) AREDS and Merle 2015 NAT2 (PMID 26132079) consistently find CFH risk-allele carriers do WORSE on zinc/antioxidant/DHA — opposite direction. Mechanism distinction (zinc/AREDS work *through* CFH-mediated complement regulation; comp-018 candidates work by *bypassing* CFH at upstream C3 convertase) may explain why the OE prediction could still hold, but the AMD analog is sobering and the prediction must be flagged as empirically untested and one-analog-negative until biobank cross-tabulation runs. Biobank feasibility: technically straightforward in UK Biobank (rs1061170 on Axiom array, gout M10.x outcomes, Oxford WebQ dietary recall; precedent published) but blocked by data-application access; collaboration with existing gout-GWAS groups (Merriman/Otago, Major-Wrigley/Auckland) is the cheapest path. See [`logs/cfh-y402h-dietary-cp0-biobank-mining-2026-05-19.md`](../logs/cfh-y402h-dietary-cp0-biobank-mining-2026-05-19.md) for the full mining report. | [complement-c5a-gout.md](./complement-c5a-gout.md) §6.3, [upstream-complement-modulator-sweep-computational.md](./upstream-complement-modulator-sweep-computational.md) |
```

### Update 2 — Expand `complement-c5a-gout.md` §6.3

Replace the existing single paragraph in §6.3 with:

```markdown
### 6.3 Factor H (CFH) variants

**CFH Y402H (rs1061170, p.Tyr402His)** is the canonical common variant dysregulating alternative-pathway complement amplification. The risk C-allele has frequency ~36-39% in Europeans, ~35-37% in Africans, ~30% in South Asians, ~5-6% in East Asians, and ~18-32% in Latino/Admixed populations (gnomAD v4 / ALFA / 1000 Genomes 2026 access; corrects the earlier "~30-50% European, ~7% East Asian" framing which conflated AMD-case ascertainment with population frequencies). The variant reduces CFH's ability to bind C-reactive protein and host glycosaminoglycans, weakening inactivation of surface-deposited C3b — predicted to amplify alternative-pathway C5a generation on MSU crystals, producing more vigorous flares.

**No published gout-association data** connect CFH variants to gout risk, severity, or flare frequency. This is the canonical complement-genetics gap, consistent with §6.1 — published gout GWAS (Tin 2019, Major 2018, Kawamura 2019 UK Biobank n=150,542) do not detect complement-pathway sub-signals at genome-wide significance, plausibly because (1) urate-transporter signals dominate gout GWAS effect-size distributions, (2) flare-severity endpoints are less well-powered than hyperuricemia endpoints, and (3) the complement-priming axis acts conditionally on MSU crystallization rather than as an unconditional gout-risk modifier.

**Supportive intermediate-phenotype evidence:**

- **Hecker 2023** (Front Immunol, PMID 37940657, n=153 healthy + 84 dry AMD + 143 neovascular AMD): CFH 402HH homozygotes had elevated baseline CRP (38% of healthy 402HH in the 3-10 mg/L range vs 10% in 402YH carriers, p=0.037) and depressed CD4+ T-cell proportions with aging. CRP elevation is upstream of classical complement priming on MSU crystals (per §5).
- **Volcik 2008 ARIC** (PMID 18292760, n=15,792): CFH 402H × hypertension interaction → HRR 1.47 (95% CI 1.05-2.05) for ischemic stroke in white 402HH; HRR 1.19-1.28 for CHD in hypertensive 402H carriers. Effect absent in African Americans, suggesting population-specific effect-direction differences. Consistent with the priming-gradient framework.

**The dietary-CP0 stratification prediction (added 2026-05-19, untested):** the comp-018 / comp-020 dietary CP0 candidates (rosmarinic acid C3 convertase inhibition, luteolin CH50/AP50, Houttuynia cordata polysaccharide multi-target) are mechanistically positioned to **bypass** the CFH-mediated complement-regulation axis (they prevent C3 convertase assembly upstream of where Y402H matters), suggesting CFH Y402H carriers should benefit MORE from dietary CP0 blockade than wild-type carriers — the same stratification logic as ABCG2 Q141K × butyrate per [`abcg2-modulators.md` §6](./abcg2-modulators.md).

**⚠️ Counter-evidence from CFH × diet × AMD analog (added 2026-05-19):** three independent published analyses point the opposite direction.

- **Klein 2008 / Awh 2013 / Vavvas 2018** (PMID 18423869 / 23972322 / 29311295; AREDS n=989/802 with bootstrap validation n=412): CFH high-risk + no ARMS2 risk genotype group (GTG2) had **paradoxically increased** progression to neovascular AMD on AREDS formulation (zinc 80 mg + antioxidants) vs placebo (HR 2.9, p=0.018). CFH low-risk + ARMS2 high-risk (GTG3) benefited (HR 0.50, p=0.008).
- **Merle 2015 NAT2** (PLoS ONE PMID 26132079, n=250): CFH × DHA-supplementation interaction p=0.01. DHA was protective only in CFH 402YY (non-risk homozygous; CNV 38.2% placebo vs 16.7% DHA, p=0.008); CFH 402CC homozygotes had numerically MORE CNV on DHA (23.1% placebo vs 39.5% DHA).
- **Chew 2014 AREDS Report #38** (PMID 24974817, n=1,237): null result — no significant CFH × treatment interaction. The literature is heterogeneous.

The mechanism interpretation that may rescue the OE prediction: AREDS-zinc and DHA work *through* complement regulation that requires functional CFH (Vavvas 2018 attributes the GTG2 paradox to zinc-induced complement inactivation requiring CFH-CRP bridging, which CFH 402H performs poorly). Rosmarinic acid / luteolin / Houttuynia work by *direct* convertase inhibition or polysaccharide-mediated CP/LBP blockade — neither requires functional CFH. The dissociation is mechanistically plausible but empirically untested.

**Biobank feasibility:** the cross-tabulation (UK Biobank CFH rs1061170 × dietary polyphenol intake × incident gout M10.x) is technically straightforward — rs1061170 is on the standard Axiom array (resource 149601); gout outcomes + Oxford WebQ dietary recall + Phenol-Explorer-derived polyphenol intake are all standard fields with published precedent (Yokose 2024 Rheumatology for gout × diet UKB methodology; Bondonno 2025 Nature Food for flavonoid-diversity × outcome UKB methodology). OE does not currently hold a UK Biobank application; the practical paths are (a) collaboration with existing gout-GWAS groups (Merriman/Otago, Major-Wrigley/Auckland, Choi/MGH) who already have UKB access and gout-extraction pipelines, ~3-month timeline, $0 OE cost; (b) AoU Researcher Workbench credentialing for a parallel direction-check in a smaller cohort with better African-American representation, ~2-4 weeks; (c) primary UKB application, ~6-12 months + £3-9K. Full mining report: [`logs/cfh-y402h-dietary-cp0-biobank-mining-2026-05-19.md`](../logs/cfh-y402h-dietary-cp0-biobank-mining-2026-05-19.md).

**Open research priorities (per §11 also):**

1. CFH Y402H × dietary CP0 blockade × incident gout — biobank cross-tabulation as above.
2. CFH Y402H × flare severity at first-presentation gout — chart-review study in tertiary rheumatology cohorts where genotyping + flare-severity grading + DAS-style scoring exist.
3. CFH Y402H × serum C5a / sC5b-9 during flare phase — biomarker biobank substudy nested in any prospective gout cohort.
4. African-ancestry-specific complement-pathway × gout work — the CFH C-allele frequency parity with Europeans + the Volcik 2008 ARIC null-in-AfricanAmericans finding together mark a population-specific question that the predominantly-European AMD literature has not answered.
```

### Update 3 — Add a single line under `complement-c5a-gout.md` §11 "Open research questions" item 5

Replace the existing line 749:
```
5. **Factor H variants and gout severity** — cross-reference AMD-CFH-genotyped biobanks with gout ICD codes and flare frequency. Database-only study.
```
with:
```
5. **Factor H variants and gout severity** — UK Biobank / All of Us cross-tabulation of CFH rs1061170 × dietary polyphenol intake × incident gout M10.x. Status (2026-05-19): empirically untested; biobank feasibility documented in `logs/cfh-y402h-dietary-cp0-biobank-mining-2026-05-19.md`; closest analog (CFH × diet × AMD) points the opposite direction, mechanistic dissociation hypothesis (CP0 candidates bypass CFH-dependent regulation) is plausible but unverified. Operational path: collaboration with existing UKB gout-genetics groups, not solo OE application.
```

## Limitations

- **No UK Biobank or AoU primary access.** All UK Biobank statements are derived from public Showcase metadata + published methodology in adjacent gout × diet UKB studies (Yokose 2024, Choi 2024, Major 2018). No direct query was run.
- **Paperclip semantic search has a known coverage gap on Chinese-language non-PubMed-indexed sources.** The CNKI / WanFang / J-STAGE direct-search surface is not available in this session. The multilingual CFH × diet × gout absence in Chinese-language sources is inferred from paperclip's Chinese-character search returning only TCM × hyperuricemia papers and the absence of CFH × dietary work in the comp-018 multilingual sweep — but a dedicated CNKI search would be a more definitive negative.
- **The mechanism-dissociation hypothesis (CP0 candidates bypass CFH-dependent regulation, therefore the OE prediction direction may hold despite the AMD analog opposite direction) is a mechanistic claim, not an empirically demonstrated dissociation.** It is the cleanest current explanation for why the AMD analog might not generalize, but it should be flagged explicitly as untested.
- **CFH Y402H allele frequencies in admixed populations (Latino/Hispanic, African American) have substantial cohort-to-cohort variability** (ALFA "Lat Am 1" 32% vs gnomAD v4 "American" 18%) reflecting different ancestry-component proportions. Stratification by genetic-ancestry proportion rather than self-report would be required for clean African-American or Hispanic effect-size estimates.
- **The rosmarinic acid plasma-vs-IC50 gap** (per the comp-021 verification gate noted in `upstream-complement-modulator-sweep-computational.md`) is not addressed by any biobank query and constrains the operational interpretation of any positive biobank finding. Even a clean CFH × dietary RA × gout interaction signal would be subject to the assay-format spread caveat at the mechanism layer.
- **Bidirectional confounding is plausible.** CFH Y402H is associated with cardiovascular risk + CRP elevation + AMD — all of which correlate with dietary patterns and gout risk through non-complement routes. A clean interaction signal would require careful adjustment for confounding by overall dietary quality, BMI, and CKD/eGFR (since CFH 402H × hypertension is real per Volcik 2008).

## Citation provenance summary

| Load-bearing claim | Primary source | PMID / Identifier | Verification status |
|---|---|---|---|
| CFH 402HH → elevated CRP (38% in 3-10 mg/L vs 10% YH, p=0.037, n=153 healthy) | Hecker et al., Front Immunol 2023 | PMID 37940657 (PMC10632322) | WebFetch verified from PMC abstract + methods |
| CFH 402H × hypertension → ischemic stroke HRR 1.47 in whites | Volcik et al., ARIC 2008 | PMID 18292760 (PMC2674647) | WebFetch verified from PMC |
| Vavvas 2018 GTG2 (CFH high-risk + no ARMS2) NV-AMD HR 2.9 on AREDS, p=0.018 | Vavvas et al., PNAS 2018 | PMID 29311295 (PMC5789949) | Paperclip content.lines verified L46 |
| Vavvas 2018 GTG3 (CFH low-risk + high ARMS2) NV-AMD HR 0.50 on AREDS, p=0.008 | Vavvas et al., PNAS 2018 | PMID 29311295 (PMC5789949) | Paperclip content.lines verified L46 |
| Merle 2015 NAT2 CFH × DHA interaction p=0.01; CFH 402YY DHA-protective (CNV 38.2% placebo vs 16.7% DHA, p=0.008) | Merle et al., PLoS ONE 2015 | PMID 26132079 (PMC4489493) | Paperclip content.lines verified L18, L62, L65 |
| Klein 2008 CFH non-risk allele → benefit from AREDS antioxidant+zinc | Klein et al., Ophthalmology 2008 | PMID 18423869 | Cited via Merle 2015 ref [31]; not full-text verified |
| Awh 2013 CFH+ARMS2 genotype-treatment interaction in AREDS | Awh et al., Ophthalmology 2013 | PMID 23972322 | Cited via Merle 2015 ref [33] and Vavvas 2018 ref [12]; not full-text verified |
| Chew 2014 AREDS Report #38 null finding | Chew et al., Ophthalmology 2014 | PMID 24974817 | Cited via Merle 2015 ref [38] and Vavvas 2018 ref [14]; not full-text verified |
| CFH Y402H rs1061170 European C-allele 0.376 (ALFA) / 0.386 (gnomAD v4 exomes) | dbSNP / ALFA / gnomAD v4 | rs1061170 | WebFetch verified from ncbi.nlm.nih.gov/snp/rs1061170 |
| CFH Y402H rs1061170 East Asian C-allele 0.042-0.060 | dbSNP / ALFA / gnomAD v4 / 1000G | rs1061170 | WebFetch verified |
| CFH Y402H rs1061170 African C-allele 0.346-0.370 | dbSNP / ALFA / gnomAD v4 / 1000G | rs1061170 | WebFetch verified |
| Rosmarinic acid C3 convertase IC50 5-10 µM optimal | Englberger et al., Int J Immunopharmacol 1988 | PMID 3198307 | Inherited from comp-018, abstract-tier per the ⚠️ assay-format spread caveat in `upstream-complement-modulator-sweep-computational.md` — comp-021 verification gate pending |
| Rosmarinic acid C3 convertase IC50 137-182 µM (alternate assays) | Cimanga 1999; Mu 2013 | PMID 10501230; PMID 23659550 | Inherited from comp-018, abstract-tier |
| Luteolin CH50 190 µM / AP50 170 µM | Zhang & Chen, J Ethnopharmacol 2008 | PMID 18400428 | Inherited from comp-018 |
| Houttuynia cordata polysaccharide CH50 79-318 µg/mL | Lu et al., Acta Pharm Sin B 2017; Cheng 2013; Xu 2015 | PMID 29404287; multi-anchor | Inherited from comp-018 Phase 2 |
| Houttuynia cordata polysaccharide → NLRP3 inflammasome suppression in coinfection model | Li et al., Int J Biol Macromol 2025 | PMC12254813 | Paperclip abstract verified |
| Tin 2019 gout GWAS (351 loci, no CFH at GWS) | Tin et al., Nat Genet 2019 | PMID 31578528 | Cited in `gout-genetic-variants.md` sources |
| Yokose 2024 UK Biobank ultraprocessed food × gout PRS | Yokose et al., Rheumatology 2024 | DOI 10.1093/rheumatology/kead455 | WebSearch verified |
| UK Biobank Axiom array directly types rs1061170 (resource 149601) | UK Biobank Showcase Resource 149601 | community.ukbiobank.ac.uk | WebSearch verified |
| Di Scipio 2026 UK Biobank G×D PGS → incident gout signal | Di Scipio et al., medRxiv 2026 | DOI 10.64898/2026.04.13.26350340 | Paperclip abstract verified; CFH-specific extraction not possible (paper content unavailable in slab service this session) |

**Pre-commit grep-verify gate status (per CLAUDE.md Rule 4):** the load-bearing numbers in this report — CFH 402HH CRP 38% vs 10% (p=0.037), Vavvas GTG2 HR 2.9 / GTG3 HR 0.50, Merle NAT2 38.2/16.7 CNV percentages, allele frequencies — were verified directly against source files (paperclip content.lines or WebFetch from PMC/NCBI) at the time of writing. The Englberger 1988 rosmarinic acid IC50 number is inherited from comp-018 with its existing abstract-tier caveat (the comp-021 verification gate is the formal resolution path). The Klein 2008 / Awh 2013 / Chew 2014 findings are presented as cited via Merle 2015 and Vavvas 2018 (not direct full-text verified this session) — flagged in the table above.
