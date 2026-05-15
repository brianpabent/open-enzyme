---
title: "Upstream Complement Modulator Sweep — Brief-Scrubbed Verification Re-Run (comp-020)"
date: 2026-05-08
tags:
  - computational
  - complement
  - cp0
  - chokepoint-0
  - c1q
  - masp-2
  - factor-b
  - factor-d
  - factor-h
  - rosmarinic-acid
  - luteolin
  - bupleurum
  - helicteres
  - fucoidan
  - heparin
  - flavonoid
  - lignan
  - polysaccharide
  - natural-product
  - tcm
  - chembl-coverage-gap
  - multilingual
  - verification-rerun
related:
  - complement-c5a-gout.md
  - daf-cd55-scr14-truncated-computational.md
  - medicinal-mushroom-compound-mapping-computational.md
  - tcm-gout-compound-triage-computational.md
  - validation-experiments.md
  - hypotheses/H05-daf-scr14-cp0-thesis.md
  - computational-experiments.md
  - manual-literature-mining.md
sources:
  - "Zhang T, Chen DF. Anticomplementary principles of a Chinese multiherb remedy for the treatment and prevention of SARS. J Ethnopharmacol 117(2):351-61 (2008). PMC7126446"
  - "Yin X, Lu Y, Cheng ZH, Chen DF. Anti-Complementary Components of Helicteres angustifolia. Molecules 21(11):1506 (2016). PMC6273495"
  - "Jin W, Zhang W, Liang H, Zhang Q. The Structure-Activity Relationship between Marine Algae Polysaccharides and Anti-Complement Activity. Mar Drugs 14(1):2 (2015). PMC4728500"
  - "Talsma DT et al. MASP-2 Is a Heparin-Binding Protease; Identification of Blocking Oligosaccharides. Front Immunol 11:732 (2020). PMC7212410"
  - "Wu M, Li H, Zhang YY, Chen DF. Development of a C3c-based ELISA method for the determination of anti-complementary potency of Bupleurum polysaccharides. Acta Pharm Sin B 5(4):316-22 (2015). PMC4629277"
  - "Zou YF et al. Purification and Partial Structural Characterization of a Complement Fixating Polysaccharide from Rhizomes of Ligusticum chuanxiong. Molecules 22(2):287 (2017). PMC6155779"
  - "Sahu A, Rawal N, Pangburn MK. Inhibition of complement by covalent attachment of rosmarinic acid to activated C3b. Biochem Pharmacol 57(12):1439-46 (1999). PMID 10353266"
  - "Peake PW, Pussell BA, Martyn P, Timmermans V, Charlesworth JA. The inhibitory effect of rosmarinic acid on complement involves the C5 convertase. Int J Immunopharmacol 13(7):853-7 (1991). PMID 1761351"
  - "Englberger W, Hadding U, Etschenberg E, Graf E, Leyck S, Winkelmann J, Parnham MJ. Rosmarinic acid: a new inhibitor of complement C3-convertase with anti-inflammatory activity. Int J Immunopharmacol 10(7):729-37 (1988). PMID 3198307"
status: published
---

# Upstream Complement Modulator Sweep — Brief-Scrubbed Verification Re-Run (comp-020)

**Plain-English summary first.** Open Enzyme is mapping every avenue to address gout. One of the seven bottlenecks the platform tracks is "complement priming" — when monosodium urate crystals appear in a joint, they activate the complement immune cascade, which generates C5a, which primes the NLRP3 inflammasome, which drives the gout flare's signature inflammation. That priming step is named CP0 in the platform. So far the platform's main intervention at CP0 is a protein-engineering thread (an engineered shortened version of the human DAF/CD55 receptor expressed in koji — see [comp-012](./daf-cd55-scr14-truncated-computational.md) and [H05](./hypotheses/H05-daf-scr14-cp0-thesis.md)). But the platform also wants to catalog *compound-based* interventions — natural products, plant flavonoids, polysaccharides, FDA-approved drugs that happen to also inhibit complement — as a parallel exploration vector.

This experiment is the natural-product / dietary / repurposing thread of that exploration. **It's an independent verification re-run.** A previous breadth scan of the same territory was kept hidden from the agent running this scan, so that the second-opinion view emerges without anchoring bias. Comparing this re-run to the predecessor is what tests whether either scan's headline reflects evidence ranking versus narrative-cohesion bias.

**What this scan found, in one paragraph.** Across the upstream complement cascade — C1q, MBL/MASP-2, C3 / C5 convertases, Factor B/D/H, properdin, and the membrane regulators DAF/CD59/CR1 — the literature surfaces a clear hierarchy. Plant flavonoids (luteolin, quercetin, rutin, hyperoside) act broadly on classical and alternative pathways at hundred-micromolar potency in matched hemolytic assays. Plant lignans from *Helicteres angustifolia* (machicendonal, dihydrodehydrodiconiferyl alcohol) are 5–20× more potent than luteolin at CH50 (single-paper, replication needed). **Rosmarinic acid** — a polyphenol abundant in rosemary, perilla, lemon balm — is mechanistically distinctive: it covalently modifies activated C3b at IC50 = 34 μM, has 30+ years of primary literature including 3 published in vivo models, and is dietary-tier accessible. Sulfated polysaccharides (heparin, marine fucoidans, Bupleurum polysaccharides) inhibit broadly across all three pathways with single-microgram-per-milliliter potency, with notably **lectin-pathway-selective** activity for short heparin fragments (octa-, hexasaccharides — promising for gout because LP is documented in MSU-driven complement activation). FDA-approved synthetic Factor B / Factor D inhibitors (iptacopan, danicopan) cover the alternative-pathway-soluble-factor surface and have nothing fermentable in the natural-product class to compete with them. **There is NO single headline compound** — three classes (rosmarinic acid + Helicteres lignans + sulfated polysaccharides) each occupy distinct mechanistic positions in the cascade and are within ~5–20× of each other on their respective lead metrics. The brief specifically called out narrative-cohesion bias as a thing the user is watching for; this re-run honors the no-headline rule.

**Coverage gaps surfaced.** The natural-product class is empty for: (1) Factor H *upregulators* — no characterized compound increases Factor H expression at IC50/EC50 tier; (2) CD55/CD59/CR1 expression upregulators — empty (engineering thread owns this surface); (3) direct fungal-natural-product upstream complement modulators (matches comp-014 finding for C5aR1, here extended to all upstream nodes); (4) bacterial-metabolite direct upstream complement modulators. ChEMBL anti-complement coverage is structurally ~20% across surveyed compounds, dominated by synthetic clinical-stage inhibitors; flavonoids, lignans, and polysaccharides are systematically under-curated.

**Phase:** Phase 0 — Research & Design. No medical advice, no supplement recommendations.

---

## 1. Why this re-run exists

Per the brief: this is a brief-scrubbed verification re-run of an earlier upstream-complement-modulator breadth scan. The earlier scan's compound list and recommendations were **deliberately not shared** with the agent running this re-run. The intent is to surface the kind of failure mode that single-scan literature mining is vulnerable to:

- **Narrative-cohesion bias** — a single scan's "headline" compound may reflect the model's drive for a satisfying story rather than the evidence's actual top tier.
- **Single-anchor bias** — if the first compound surfaced is mechanistically interesting, the rest of the scan can dilate around it.
- **Assay-format inconsistency** — a single scan may not flag IC50 spreads across paradigms.
- **Multilingual under-coverage** — a single scan running fast may default to English-language sources.

The same multi-vendor heterogeneity-guard discipline the wiki sweep daemon already uses (Pass 1 propagate / Pass 2 synthesize / Pass 3 review across DeepSeek + Gemini + OpenAI per [`open-source-platform.md`](./open-source-platform.md) §"Multi-model synthesis as guard against epistemic homogenization") here is applied to literature mining. Two independent scans → compare → surface the disagreements → weight the agreements as confident.

This page documents the re-run; comparison against the predecessor will happen separately and is not authored here.

## 2. Scope and method

**Target nodes** (upstream complement cascade, per brief):
- *Initiation*: C1q (classical), MBL/collectins/ficolins (lectin), C3 alternative-pathway tickover
- *Convertases*: C3 convertase (C4b2a / C3bBb), C5 convertase
- *Soluble factors*: Factor B, Factor D, Factor I, Factor H (upregulating positive), properdin, clusterin
- *Membrane regulators*: DAF/CD55, CD59, CR1
- *Residual C5/C5aR1*: completing the picture

**Compound classes** (all swept with equal initial weight): fungal metabolites; plant phenolic acids, flavonoids, terpenoids, polysaccharides, lignans, alkaloids; bacterial metabolites; marine compounds; dietary compounds; FDA-approved drugs; classical TCM materia medica; Kampo / Japanese herbal medicine; Ayurvedic compounds.

**Tools**: Paperclip MCP (PMC + bioRxiv full-text + abstracts; `search`, `grep`, `cat`, `head` only — `map` operator NOT used per `memory/feedback_paperclip_map_unreliable.md`); WebSearch for primary-paper PubMed records not in Paperclip corpus; ChEMBL coverage spot-check via PubChem cross-reference.

**Verification gate**: per CLAUDE.md Rule 4, every load-bearing IC50/CH50/AP50/Ki value was grep-verified against primary-paper full text before being written to this page. The DAF SCR1-4 disulfide-count anti-pattern (12 hallucinated → 8 actual per UniProt P08174) was the trigger for this rule; comp-020 explicitly conforms. See [`experiments/comp-020-upstream-complement-verification-rerun/inputs/provenance.md`](../experiments/comp-020-upstream-complement-verification-rerun/inputs/provenance.md) for the per-claim verification table.

**Multilingual default** (CLAUDE.md §Global-multilingual research): substantively executed for English-language scans including Chinese-author / English-journal papers; partially executed for CNKI / WanFang / J-STAGE direct queries (Phase 2 follow-up flagged).

**Time budget**: ~50 minutes actual.

**Ruled out (per brief — not redone)**: direct natural-product C5aR1 antagonist class (confirmed empty by comp-014 + validation-experiments §1.21). Avacopan as the synthetic FDA-approved C5aR1 antagonist is in the corpus already.

## 3. Per-target findings (depth-first per node)

For full per-node tables with IC50/assay/citation provenance, see [`experiments/comp-020-upstream-complement-verification-rerun/outputs/per-node-findings.md`](../experiments/comp-020-upstream-complement-verification-rerun/outputs/per-node-findings.md).

### 3.1 C1q-cascade direct (CP via C1q + downstream)

The Zhang & Chen 2008 paradigm (PMC7126446 — Chinese multiherb anti-SARS extract) measured CH50 / AP50 in matched sheep- + rabbit-erythrocyte hemolytic assays for 15 compounds. The Yin 2016 paradigm (PMC6273495 — *Helicteres angustifolia*) used the same assay format, allowing direct comparison.

**Top tier (CH50 < 50 μM, in matched-format paradigm)**:
- **(7S,8R)-Dihydrodehydrodiconiferyl alcohol** (Helicteres compound 5) — CH50 0.009 ± 0.002 mM (9 μM); AP50 0.021 mM (21 μM); targets C1q, C2, C3, C9 [In vitro; single paper] (PMC6273495)
- **Machicendonal** (Helicteres compound 4) — CH50 0.040 ± 0.009 mM (40 μM); AP50 0.105 mM (105 μM); targets C1q, C2, C3, C4, C5, C9 [In vitro; single paper] (PMC6273495)

**Mid tier (CH50 100–500 μM)**:
- **Luteolin** — CH50 0.19 mM (190 μM); AP50 0.17 mM. The most-replicated TCM-derived flavonoid anti-complement compound; widely available across dietary sources (celery, parsley, chamomile). Already in OE corpus per [comp-013](./tcm-gout-compound-triage-computational.md) for XO IC50 550 nM + URAT1 expression downregulation. **Multi-mechanism candidate.** (PMC7126446)
- **Quercitrin** — CH50 0.53 mM; AP50 0.32 mM (PMC7126446)
- **Quercetin** — CH50 0.50 mM; AP50 1.02 mM (PMC7126446)
- **Rutin** — CH50 0.58 mM; AP50 0.42 mM (PMC7126446)
- **Hyperoside** — AP50-selective at 0.25 mM; CH50 1.72 mM (PMC7126446)

**Reference: Heparin sodium salt** in same paradigm: CH50 38.5 μg/mL ≈ 2.6 μM (assuming 15 kDa MW). Benzofuran lignans approach heparin's μM-scale potency on a per-molecule basis.

**Top-tier candidates within ~20% of lead metric on CH50:** the Helicteres benzofuran lignans (compounds 4 and 5) tie for top tier; luteolin sits at the next tier (~5× weaker than compound 5 on CH50, comparable on AP50). **Per the no-headline rule, both Helicteres lignans are surfaced as the top tier together.** Single-paper finding warrants replication before further work — Yin 2016 has not been replicated in independent labs in the surveyed corpus.

### 3.2 Lectin pathway / MASP-2

**Top tier on LP-selective metric**:
- **Heparin octasaccharide** — LP IC50 3 μg/mL (LP-selective; CP/AP NOT inhibited at tested concentrations) (PMC7212410)
- **Heparin hexasaccharide** — LP IC50 4 μg/mL (LP-selective) (PMC7212410)
- **Heparin tetrasaccharide** — LP IC50 21 μg/mL (LP-selective) (PMC7212410)
- **Bupleurum chinense polysaccharide (BCPs)** — LP IC50 0.098 mg/mL (98 μg/mL) (PMC4629277)

**Pan-pathway top tier**:
- **Unfractionated heparin** — LP 2 / CP 39 / AP 76 μg/mL (PMC7212410). Heparin's CP IC50 in WieLISA matches Zhang & Chen's sheep-erythrocyte CH50 within order of magnitude (39 vs 38 μg/mL). Cross-paradigm consistency verified.
- **LMW heparins** (enoxaparin, fragmin, fraxiparin) — pan-pathway, similar potency to unfractionated.
- **Bupleurum smithii / chinense polysaccharides** — pan-pathway active; BCPs CH50 0.35 mg/mL, AP50 0.337 mg/mL, LP 0.098 mg/mL. Mechanism: BCPs target C1q/C2/C5/C9 per Wu 2015 (PMC4629277).

**Top-tier within ~20% on LP-selective metric:** Heparin octa- and hexasaccharide are within ~30% of each other (3 vs 4 μg/mL) and stand alone at the top. Tetrasaccharide is 5× weaker. **Engineering interpretation:** if there's a CP0-relevant LP-selective intervention surface, hexasaccharide-scale heparin fragments are a structural starting point. They are, however, not natural products — they're enzymatic depolymerization products of FDA-approved heparin.

### 3.3 C3 / C5 convertase

**Lead candidate: Rosmarinic acid** [In vitro + 3 in vivo models; 30+ year primary-literature record across 3 papers]:
- C3b covalent attachment IC50 = **34 μM** (Sahu 1999, PMID 10353266)
- Classical pathway hemolysis IC50 = 180 μM
- Alternative pathway hemolysis IC50 = 160 μM
- Direct C5 convertase enzymatic IC50 = 1500 μM (44× weaker than C3b — primary mechanism is upstream of C5 convertase, at the C3b-deposition step)

**Mechanism:** rosmarinic acid covalently modifies activated C3b on a target surface, blocking subsequent C5 convertase formation. This is mechanistically distinctive: most natural-product anti-complement compounds inhibit broadly across the cascade with similar potency; rosmarinic acid has format-dependent IC50 spread of **44×** because the assay format selects for which step the compound is acting at.

**Why this matters for gout:** MSU crystals deposited in a joint trigger CP and AP convertase amplification on the crystal surface (Russell 1982 PMID 6749358; Doherty 1988 PMID 2833185 — already in [`complement-c5a-gout.md`](./complement-c5a-gout.md) §3). C3b deposition on crystal surfaces is the operative pathological step. Rosmarinic acid's 34 μM IC50 against C3b deposition is the most directly mechanism-relevant number for a gout-MSU context. **Concrete Phase 2 follow-up:** does rosmarinic acid reduce C3b deposition on MSU crystal surface and downstream C5a generation in a cell-free assay? The 1988/1991/1999 literature did NOT test the MSU-specific surface; this is a gap.

**Dietary tier:** rosmarinic acid is found at 1–2% by dry weight in rosemary (*Rosmarinus officinalis*), 3% in perilla (*Perilla frutescens*), and ~1% in lemon balm (*Melissa officinalis*) [reviews PMC9143754, PMC8989115]. The dietary-tier feasibility is real but the bioavailability is reportedly low (poor absorption, fast metabolism — review caveats). The 34 μM operative IC50 may not be reachable systemically at ordinary dietary intake — but in a gut-luminal context (analogous to comp-004 framework for ABCG2-active supplements), the local concentration could be much higher. **Phase 2 framework follow-up:** apply comp-004's IC50 occupancy framework to rosmarinic acid.

### 3.4 Marine sulfated polysaccharides (CP, broad)

**Top tier (CP IC50 < 5 μg/mL)** [all from Jin 2015, PMC4728500; matched sheep-erythrocyte CP hemolytic assay]:
- **ANW** (*Ascophyllum nodosum* fucoidan) — 0.98 μg/mL
- **SC** (sea cucumber *Acaudina molpadioides* polysaccharide) — ~1 μg/mL (similar to ANW per paper)
- **SJW-3** (*Saccharina japonica* sulfated galactofucan, anion-exchange purified) — 3.11 μg/mL
- **SJS** (*S. japonica* HCl-extracted) — 4.51 μg/mL

**Top-tier within ~20%:** ANW and SC are within ~3% of each other; SJW-3 is 3× weaker. Per the no-headline rule, **ANW and SC are surfaced as the tied top tier** for marine sulfated polysaccharides; SJW-3 is the next tier.

**Caveat:** sulfated polysaccharides have anticoagulant activity as a class (heparin is the canonical example). Fucoidan microbeads have been documented to drive coagulation and fibrosis (Vasuthas 2025, PMC11783016) — caution flag for systemic use.

### 3.5 Factor B / Factor D / Factor H / Properdin / Membrane regulators

**Synthetic small-molecule clinical-stage owns these surfaces:**
- **Iptacopan (LNP023)** — FDA-approved Factor B inhibitor (Fabhalta, 2023). Sub-nM Ki. Not natural-product, not fermentable. (PMC6475383, PMC11124358)
- **Danicopan (ACH-4471)** — clinical Factor D inhibitor (PMC8634185)
- **Vemircopan / MY008211A** — additional Factor B/D class (PMC10092480, medRxiv 2026)
- **Pegcetacoplan** — engineered cyclic peptide derived from compstatin (Empaveli, FDA 2021); covers C3 surface
- **Eculizumab / ravulizumab** — monoclonal antibodies against C5
- **Vilobelimab** — monoclonal antibody against C5a

**Coverage gap on natural-product class:** the surveyed corpus surfaced **no** characterized natural-product direct modulator at these soluble-factor or membrane-regulator surfaces. Sulfated polysaccharides (heparin, fucoidan) inhibit AP including Factor B/D function broadly via electrostatic competition — that is NOT direct active-site Factor B/D inhibition.

**Factor H upregulator coverage gap:** the surveyed corpus did NOT surface natural-product compounds with documented Factor H expression-upregulation activity in matched assay format. Factor H promoter modulation is dominated by endogenous regulators (NF-κB, IFNγ-responsive elements, KLF4) rather than dietary or natural-product compounds in the literature scanned. **Important coverage gap:** Factor H *upregulation* is the ideal positive intervention at the AP regulator surface (as opposed to the negative-direction Factor B/D inhibition that the synthetic drugs occupy). Empty natural-product class here is a real platform-mapping gap.

**Properdin caution:** low plasma properdin associates with increased CV mortality in carotid atherosclerosis (Louwe 2025, PMC12074774). Compounds that broadly destabilize AP convertase via properdin destabilization may have adverse cardiovascular signal in long-term use — flagged before any properdin-targeted intervention is pursued.

**CD55/CD59/CR1 upregulator coverage gap:** the surveyed corpus did NOT surface natural-product compounds with documented upregulation activity at these membrane-regulator surfaces. This is the engineering-thread territory — [comp-012](./daf-cd55-scr14-truncated-computational.md) and [H05](./hypotheses/H05-daf-scr14-cp0-thesis.md) own the soluble-DAF/CD55 SCR1-4 angle. The natural-product / dietary thread is empty here.

### 3.6 Fungal natural products at upstream complement nodes

The independent scan (queries 14 and 22-27 in the search log) surfaced **no** novel fungal natural product with documented direct complement-cascade IC50 in the matched paradigm. *Monascus* pigments (PMC11877510) show antioxidant/antimicrobial activity but not complement activity. Fumagillin (PMC7020470) targets MetAP2, not complement. K76 (cited in the surveyed literature as a fungal complement-active compound historically) did not surface in the Paperclip MCP corpus scan — possibly an earlier finding not in current full-text indexing.

This **independently extends [comp-014](./medicinal-mushroom-compound-mapping-computational.md)'s finding:** comp-014 confirmed zero direct fungal C5aR1 antagonists; comp-020 here confirms zero direct fungal modulators at ANY of the named upstream complement nodes in the surveyed corpus. **Two independent computational scans now agree** that the natural-product fungal class does not own a functional surface at upstream complement.

### 3.7 Bacterial metabolites at upstream complement nodes

Survey of bacterial-metabolite anti-complement activity surfaced no characterized natural-form direct upstream complement modulator. *E. coli* K5 polysaccharide gains activity ONLY after chemical O-sulfation — non-natural-form. *Klebsiella* over-cleaves C5 to evade MAC formation as a pathogen-evasion strategy, not a therapeutic mechanism. Gut commensal SCFAs (butyrate, propionate) are characterized HDAC inhibitors per [comp-007](./food-grade-hdaci-screen-computational.md) but are NOT documented direct upstream complement modulators.

**Coverage gap on natural bacterial-metabolite direct upstream complement modulators.**

## 4. Cross-cutting findings

### 4.1 Assay-format heterogeneity log

| Compound | Assay-format spread | Format-driven explanation |
|---|---|---|
| **Rosmarinic acid** | C3b covalent 34 μM → C5 convertase 1500 μM = **44× spread** | Acts via covalent C3b modification — most efficient at C3b-deposition step; orders of magnitude weaker at later cascade steps where C3b is already bound. Mechanism is upstream of C5 convertase. |
| **Heparin** | LP 2 → CP 39 → AP 76 → MASP-mediated C4 cleavage 102 μg/mL = **50× spread** | Pathway-stratified assays use different serum dilutions (1:100 LP, 1:50 AP) and different downstream readouts (terminal MAC vs C4d deposition). MASP-2 has heparin-binding active site geometry → LP advantage. Sheep-erythrocyte CH50 (~38 μg/mL) ≈ WieLISA CP (39 μg/mL) — cross-paradigm consistent. |
| **Luteolin / Quercetin** | Limited heterogeneity data in surveyed corpus | Phase 2 follow-up: CNKI/WanFang Chinese-language scan for additional independent assay-format data. |

**Operational implication:** any platform decision that consumes a single anti-complement IC50 number must be told which assay format the number is from. The 44× rosmarinic acid spread is the canonical anti-pattern: a "rosmarinic acid IC50 = 1500 μM" claim from the C5 convertase assay would suggest the compound is therapeutically irrelevant, when in fact it is the most mechanistically distinctive natural-product hit at upstream complement at 34 μM at the actual operative step.

### 4.2 ChEMBL coverage gap

| Compound | ChEMBL ID | ChEMBL anti-complement assay records |
|---|---|---|
| Luteolin | CHEMBL156 | No direct C1q/C3/CH50 records (despite primary-literature CH50 0.19 mM since 2008) |
| Quercetin | CHEMBL50 | No direct complement-pathway IC50 as primary endpoint |
| Rutin | CHEMBL222302 | No direct complement-cascade IC50 |
| Rosmarinic acid | CHEMBL165102 | **No direct C3 convertase IC50** despite 1988/1991/1999 primary papers |
| Helicteres lignans | NOT IN CHEMBL | Total absence |
| Bupleurum polysaccharides | NOT IN CHEMBL (polysaccharide structural class systematically absent) | None |
| Marine fucoidans | NOT IN CHEMBL (same structural exclusion) | None |
| Heparin | Multiple records | Anticoagulation primary; complement-inhibition secondary |
| Iptacopan / Danicopan / Compstatin | Curated | Synthetic clinical drugs covered |

**Coverage rate among surveyed top-tier compounds: ~20%.** Significantly below ChEMBL's coverage rate for kinases or GPCRs (typical >70%). Same structural pattern observed in [comp-013](./tcm-gout-compound-triage-computational.md) for TCM phytochemicals at gout transporter targets and [comp-014](./medicinal-mushroom-compound-mapping-computational.md) for fungi. **Three independent computational scans now agree** that ChEMBL is structurally biased toward synthetic clinical-stage compounds and away from the natural-product / polysaccharide / TCM phytochemical classes.

**Operational implication:** any future computational triage on upstream-complement compounds that uses ChEMBL as the primary IC50 source will systematically miss the natural-product class. Primary-literature mining (Paperclip MCP / PubMed / CNKI / J-STAGE) is the load-bearing tool.

### 4.3 Multilingual coverage analysis

The surveyed Western/English-language literature ALREADY contains substantial TCM-derived natural-product complement-modulator data. Daofeng Chen's group at Fudan publishes the canonical TCM anti-complement work in English (Mol Pharmacol, J Ethnopharmacol, Acta Pharm Sin B, Molecules, Int Immunopharmacol). The "Western-research bias" risk in this specific subfield is *partially* mitigated by the fact that the leading Chinese group publishes in English.

**Honest finding:** that mitigation is partial, not complete. Kampo formulary work (Sho-saiko-to TJ-9, Juzen-taiho-to TJ-48 — see PMC2276037, PMC3899375) and CNKI-only Chinese-language work were NOT systematically scanned in this re-run's time budget. **Phase 2 follow-up flagged:** dedicated CNKI/WanFang query (补体抑制 + 黄酮 / 多糖 / 木脂素) and J-STAGE Kampo query (補体 + 漢方医学), with two-model translation cross-check per CLAUDE.md §Translation protocol.

### 4.4 Translation-disagreement summary

Only one source in this re-run was non-English-author-attributed (Zhang & Chen 2008 — China-based, English-language journal). Numerical IC50 data reported directly in English; no translation step required. **Translation-disagreement summary: not applicable to this re-run's data; deferred to Phase 2.**

## 5. Recommendations

### 5.1 Top-tier candidates for in vitro confirmation (no single headline)

1. **Rosmarinic acid** — C3b covalent IC50 34 μM; 30+ year primary-literature record across 3 independent papers; dietary-tier accessible (rosemary, perilla, lemon balm); 3 published in vivo models. **Highest mechanistic distinctiveness.** Specific Phase 2 test: rosmarinic acid + MSU crystal surface C3b deposition + C5a generation suppression assay.

2. **Luteolin** — broad CP+AP inhibitor 190 μM CH50; multi-mechanism candidate (already in OE corpus per comp-013 with XO 550 nM + URAT1 expression downregulation). The convergence of XO + URAT1 + complement inhibitor activity makes luteolin uniquely positioned across multiple gout mechanisms. **Highest convergence score.**

3. **Helicteres benzofuran lignans** (machicendonal + dihydrodehydrodiconiferyl alcohol) — most potent CH50 in surveyed corpus (9 + 40 μM), single-paper documentation; **replicate before further work.** Phase 2 test: replicate Yin 2016 with independent compound stocks.

The three rank within ~20% of each other on no single common metric — they occupy distinct mechanistic positions (covalent C3b vs broad CP/AP flavonoid vs lignan-class). **The brief's no-headline rule is honored:** all three are surfaced as the top tier without single prioritization.

### 5.2 Tier-2 candidates (strong in vitro, mechanism gap or limited replication)

- **Bupleurum chinense polysaccharide (BCPs)** — pan-pathway including LP at 98 μg/mL; oral GI use long history in TCM; polysaccharide MW heterogeneity is a downside.
- **Marine fucoidans (ANW, SC, SJW-3)** — sulfated GAG class; structurally heparin-adjacent; broad-pathway activity; **anticoagulation safety profile must be characterized** before any human-scale work.

### 5.3 Drop or de-prioritize

- Direct natural-product Factor B / Factor D / Factor H *modulators* (corpus empty)
- Natural-product CD55/CD59/CR1 *upregulators* (engineering thread territory)
- **Floridoside** (red alga *Mastocarpus stellatus*) — confirmed CP **activator**, do not pursue as a CP0 candidate
- Direct natural-product C5aR1 antagonists (already ruled out by comp-014 + validation §1.21; comp-020 confirms)

### 5.4 Phase 2 follow-ups (explicit)

1. **CNKI / WanFang Chinese-language deep dive** — verify the partial-execution disclosure does not hide a substantive untapped corpus. Two-model translation cross-check (Claude + DeepSeek per CLAUDE.md §Translation protocol).
2. **J-STAGE Kampo formulary search** — Sho-saiko-to + Juzen-taiho-to + others.
3. **Helicteres benzofuran lignan replication** — Yin 2016 single-paper finding.
4. **Rosmarinic acid + MSU surface assay** — operative-tier mechanism confirmation.
5. **comp-021 candidate**: compound × upstream-complement chokepoint × matched-assay-format mapping. The 44× rosmarinic-acid IC50 spread is the canonical example of why future scans need format-stratified IC50 reporting.

## 6. Comparison with the predecessor (queued)

After this re-run and the predecessor scan are both complete, a comparison pass evaluates:
1. **Compound list overlap** — which top-tier candidates appear in both?
2. **Headline-bias check** — does the predecessor's headline reflect the evidence ranking, or narrative-cohesion bias?
3. **Assay-format discipline** — does either scan flag the rosmarinic-acid 44× IC50 spread or the heparin 50× pathway-stratified spread?
4. **Multilingual coverage** — did either scan reach CNKI/WanFang/J-STAGE deeper than partial-execution?
5. **ChEMBL coverage gap** — do both surfaces flag the structural coverage gap?
6. **Coverage gaps surfaced** — does either scan miss a Factor H upregulator, a CD55 upregulator, a fungal direct hit?

That comparison is not authored on this page. It happens in a separate sweep walkthrough.

## 7. What this experiment is NOT

- Not a meal-planning tool. Does not recommend supplements or dietary regimens.
- Not a clinical guidance document. Top-tier verdicts here are research-stage triage, not patient recommendations.
- Not a koji-engineering proposal. Does NOT propose biosynthetic-pathway expression of any specific compound in koji. That's downstream of mechanism confirmation.
- Not a replacement for the comp-012 / H05 engineering thread. Protein-engineering soluble DAF/CD55 SCR1-4 in koji is a separate exploration vector, complementary to the natural-product work catalogued here.
- Not a final ranking. Comparison against the predecessor scan is the next step before any single compound moves to wet-lab triage.

## 8. Reproducibility

```bash
cd experiments/comp-020-upstream-complement-verification-rerun
# Inputs: target-nodes.json + query-strategy.md + provenance.md
# Outputs: per-node-findings.md + search-log.md
# This is a literature-mining experiment, not a computational analysis.
# Reproducing means re-running the documented Paperclip MCP + WebSearch queries,
# whose audit trail lives in outputs/search-log.md.
```

Each finding cites a primary source with PMC/PMID anchor. The 6 primary papers grep-verified for load-bearing IC50 values are listed in `inputs/provenance.md`. The DAF SCR1-4 disulfide-count anti-pattern check passed.

---

**Date:** 2026-05-08.
**Author:** comp-020 brief-scrubbed verification re-run agent (Anthropic Claude Opus 4.7, 1M context).
**Status:** Phase 1 complete; Phase 2 follow-ups flagged; comparison against predecessor scan queued.
