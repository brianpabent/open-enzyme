---
title: Supplements Stack
aliases: [stack, multi-intervention, NLRP3 protocol, inflammasome suppression]
related: [nlrp3-inflammasome, gout-pathophysiology, validation-experiments, androgen-urate-axis, abcg2-modulators, gut-lumen-sink]
sources: [nlrp3-exploit-map.md, gout-deep-dive.md, peptide-gout-addendum.md, abcg2-modulators.md]
---

# Supplements Stack

## Overview

This is a project-generic catalog of compounds with documented activity on NLRP3, urate, or related inflammation pathways. **It is not a recommended stack.** Each compound has trade-offs that depend on context — sex, genetics (notably ABCG2 Q141K and androgen-axis state), comorbidities, current medications, and interactions with other compounds in this catalog. Read individual entries for contraindications, drug interactions, dose-dependent risk, and stack-level antagonisms before considering use.

This catalog is not a replacement for medical care. Work with a physician on any of these compounds, especially those with drug interactions or dose-ceiling concerns.

> **TCM lineage note:** Several compounds in this catalog have explicit TCM materia medica lineage — oridonin (*Rabdosia rubescens* / Dong Ling Cao 冬凌草), EGCG (green tea / Lu Cha 绿茶), theaflavins (black tea / Hong Cha 红茶), berberine (*Coptis chinensis* / Huang Lian 黄连), resveratrol (*Polygonum cuspidatum* / Hu Zhang 虎杖), curcumin (turmeric / Jiang Huang 姜黄). The methodology for applying modern scientific rigor to these compounds — including chokepoint mapping, ChEMBL cross-check, bioavailability-honest framing, and formula decomposition — is formalized in [`tcm-modern-rigor-intersection.md`](./tcm-modern-rigor-intersection.md). (source: tcm-modern-rigor-intersection.md)

> **Species-gap caveat (methodological standard, 2026-04-23)**: Rodent cellular IC50 values for NLRP3 inhibitors routinely diverge from human cellular IC50 by up to 3 orders of magnitude. Example: dapansutrile IC50 = 1 nM in mouse J774A.1 cells vs. 1,000 nM (1 μM) in human MDM cells under LPS+nigericin stimulation (ChEMBL v34). Every rodent-derived IC50 in this document should be read with that translation uncertainty in mind. When evaluating new compounds, prefer human-cell (THP-1, PBMC, human MDM) data over rodent cellular assays. (source: chembl-cross-check.md)

> **Per-entry template (standardized 2026-04-25):** Each compound entry below uses a fixed template — Mechanism, Evidence level, Population context, Dosing range, Contraindications, Drug interactions, Dose-dependent risk profile, Stack interactions (within this catalog), Cost. The Stack-interactions field is the cross-link to [abcg2-modulators.md](./abcg2-modulators.md), [androgen-urate-axis.md](./androgen-urate-axis.md), and the Stack-level interactions section near the bottom of this page. Several compounds in this catalog are functional ABCG2 inhibitors at typical supplement doses and may pharmacologically antagonize the [gut-lumen-sink](./gut-lumen-sink.md) thesis in androgen-dominant or Q141K-positive readers — see the "Stack-level contradictions" subsection.

---

## Section 1: NOW (Available Today)

Compounds currently accessible, with strong evidence, that can be started immediately.

### Beta-Hydroxybutyrate (BHB) / Exogenous Ketones

**Category:** Metabolite / Supplement

**Mechanism:** Direct NLRP3 inflammasome inhibitor; blocks priming (CP1), assembly (CP2), and ASC speck formation (CP3)

**Evidence level:** Established (Nature Medicine study: BHB-specific NLRP3 inhibition in neutrophils)

**Population context:** Broad applicability. Sex-neutral mechanism (NLRP3 inhibition is not androgen-axis-modulated). Caution in T1DM (ketoacidosis risk distinct from physiological ketosis). Pregnancy: ketogenic dietary patterns are debated for fetal substrate provision; exogenous ketone supplementation in pregnancy is unstudied. Patients with metabolic flexibility issues (e.g., long-chain fatty acid oxidation defects) should avoid MCT-based ketosis.

**Dosing range:**
- Ketogenic diet (endogenous BHB production): maintain 2–5 mM serum ketones via carb restriction (~<50g/day)
- Exogenous ketones (ketone salts or esters): 10–20g BHB/day
- MCT oil as alternative: 1–2 tbsp (~15–30g) daily generates ketones via beta-oxidation

**Key insight:** BHB doesn't require fasting or strict keto to work — it acts directly as a signaling molecule on NLRP3 regardless of metabolic pathway. (Source: nlrp3-exploit-map.md)

**Contraindications:** Active gout flare (transient UA rise from ketosis; see dose-dependent risk). T1DM without close glucose monitoring. Pregnancy (insufficient data on exogenous ketone safety). Severe hepatic disease (impaired ketone metabolism). Carnitine-deficiency syndromes if using MCT-based induction.

**Drug interactions:**
- **SGLT2 inhibitors (canagliflozin, empagliflozin, dapagliflozin):** additive ketosis; euglycemic diabetic ketoacidosis risk in T2DM patients on these drugs.
- **Insulin / insulin secretagogues:** dietary ketosis lowers glucose requirements; dose adjustment needed to avoid hypoglycemia.
- **Acetazolamide / topiramate / zonisamide:** carbonic anhydrase inhibitors compound metabolic acidosis risk on ketogenic regimens.

**Dose-dependent risk profile:**
- 5–20g/day exogenous BHB: well-tolerated; GI upset is the main side effect (most common with ketone salts; mineral load matters).
- >30g/day or aggressive nutritional ketosis: transient serum UA rise of 5–10% (ketone bodies and urate compete for renal MCT/URAT1 reabsorption). This is the gout-relevant dose ceiling. Sustained nutritional ketosis can also produce mild hyperuricemia for the same reason.
- MCT >2 tbsp at one sitting: GI distress is the practical limiter.

**Stack interactions (within this catalog):**
- **Antagonism with intermittent fasting during active flares:** both ketogenic states transiently raise serum UA via competition for renal urate excretion; layering fasting on top of exogenous ketones during a flare amplifies the spike.
- **Synergy with NAC, omega-3:** BHB-driven NLRP3 inhibition (CP1–CP3) is mechanistically additive with NAC's glutathione/ROS axis (CP2) and omega-3 SPM-driven resolution (CP5).
- **No ABCG2 interaction documented.** Neutral on the gut-lumen-sink axis.

**Cost:** Negligible (dietary) to $20–40/month (ketone salts)

---

### Intermittent Fasting

**Category:** Behavioral / Lifestyle

**Mechanism:** Induces AMPK activation, mTOR inhibition, autophagy upregulation; generates endogenous BHB

**Evidence level:** Established (extensive longevity literature)

**Population context:** Sex-differential effects documented. Women of reproductive age may experience HPO axis disruption (cycle irregularity, lowered LH/FSH) at aggressive fasting protocols (>20 hour windows or sustained <1500 kcal/day); men tolerate longer windows with less reproductive-axis disruption. Underweight, history of eating disorder, or pregnancy: contraindicated. Adolescents: not appropriate. Older adults (>70): protein-sparing windows preferred over true fasts.

**Dosing range:**
- Minimum: 16:8 (16-hour fast, 8-hour eating window)
- Optimal for NLRP3: 24-hour fasts periodically (weekly or biweekly)
- Examples: dinner-to-dinner, breakfast-to-breakfast

**Contraindications:** Active gout flare (precipitates hyperuricemia worsening). Pregnancy and lactation. T1DM without endocrinology supervision. History of eating disorder. Underweight (BMI <18.5). Adrenal insufficiency. Concurrent fluoroquinolone therapy in older adults (tendinopathy risk amplified by catabolic states).

**Drug interactions:**
- **Sulfonylureas / insulin:** hypoglycemia risk; dose timing must shift.
- **Levothyroxine:** absorption window shifts can affect TSH stability; consistent dosing time relative to feeding window matters more than the specific time.
- **Metformin:** typically well-tolerated; some lactic acidosis case reports under prolonged fasts in CKD.
- **Drugs that must be taken with food (e.g., HIV protease inhibitors, some statins):** schedule conflicts with fasting window.

**Dose-dependent risk profile:**
- 16:8 daily: well-tolerated by most; minimal UA effect outside flares.
- 24-hour fast weekly: transient UA rise of ~0.5–1.0 mg/dL during the fast (ketone competition for renal excretion); resolves on refeed.
- 48–72 hour fast: substantial UA spikes (1–2 mg/dL) and increased flare risk in known gout patients. Ceiling for gout-relevant use is at most one 24-hour fast per week, scheduled away from prodrome periods.

**Stack interactions (within this catalog):**
- **Antagonism (acute, during flare):** as with BHB, transient UA rise during the fasting window can precipitate flares — do not combine fasting with exogenous BHB during prodrome or active flare.
- **Synergy (autophagy axis):** layered with spermidine/trehalose from fermented foods, both push the same TFEB/autophagy axis (CP2/CP3).
- **Synergy with engineered uricase (future):** fasting-induced UA spikes are the precise scenario where a gut-lumen uricase sink would buffer the pathophysiology.

**Cost:** Free

---

### KPV Nasal Spray

**Category:** Peptide

**Mechanism:** α-MSH C-terminal tripeptide (Lys-Pro-Val); stabilizes IκB-α → prevents NF-κB nuclear translocation (CP1)

**Evidence level:** Supported (Published research in gout-specific context: (CKPV)₂ reverses inflammatory effect of urate crystals)

**Population context:** Broad applicability. No documented sex-differential effect. α-MSH-derived peptides have melanocyte-stimulating activity at high systemic doses; intranasal route at the doses listed is well below that threshold. Caution in patients with melanoma history (theoretical, mechanism-extrapolated rather than clinically observed at these doses).

**Dosing range:** 200–500 mcg/day intranasal

**Administration:**
- Morning spray (nasal mucosa, high PepT1 expression)
- Combine timing with BPC-157 spray for convenience

**Contraindications:** Active or recent melanoma (theoretical, based on α-MSH/MC1R signaling). Pregnancy (insufficient data). Pediatric use (insufficient data). Sourcing-quality unknowns: research peptide suppliers vary widely in purity and endotoxin load.

**Drug interactions:**
- **Immunosuppressants (tacrolimus, cyclosporine, biologics):** unstudied; mechanism overlap with NF-κB pathway.
- **Topical/intranasal corticosteroids:** mechanism overlap; no clear pharmacological conflict but redundant signaling.
- No documented small-molecule drug interactions; peptide is rapidly hydrolyzed.

**Dose-dependent risk profile:**
- 200–500 mcg/day intranasal: well-tolerated in published research; main risk is sourcing quality.
- Systemic dosing (subcutaneous, off-label) at multi-mg levels: melanocyte effects (skin darkening) become detectable. Stay intranasal at the doses listed.
- Sourcing: research peptide suppliers without third-party HPLC/MS/endotoxin verification carry product-quality risk that scales with dose and frequency.

**Stack interactions (within this catalog):**
- **Synergy with BPC-157 (non-overlapping pathways):** both small peptides, complementary mechanisms — KPV at NF-κB priming (CP1), BPC-157 at cytoprotection / NO modulation.
- **Mild redundancy with sulforaphane, EGCG, quercetin:** all converge on NF-κB / NLRP3 priming axes; cumulative benefit unclear vs. single-agent.
- **No ABCG2 interaction.** Peptide does not engage transporter axis.

**Cost:** $100–200/month (Peptides@BioTechPackage, GenScript, or research peptide custom synthesis)

---

### BPC-157 Nasal Spray

**Category:** Peptide / Tissue Repair

**Mechanism:**
- Cytoprotective (protects macrophages from MSU crystal-induced damage)
- Nitric oxide system modulation
- CP1 + tissue repair (secondary mechanism)

**Evidence level:** Established (published literature; you're already using this)

**Population context:** Broad applicability. No documented sex-differential effect. Most published data is in rodent injury models; human use is largely off-label and based on mechanistic extrapolation from cytoprotection literature. The peptide's growth-promoting / angiogenic effects raise theoretical concerns in active malignancy (mechanism-extrapolated, not clinically demonstrated).

**Dosing range:** 200–500 mcg/day intranasal

**Contraindications:** Active malignancy (theoretical, based on angiogenic signaling — not clinically demonstrated). Pregnancy (insufficient data). Sourcing-quality unknowns as with KPV.

**Drug interactions:**
- **Anti-VEGF agents (bevacizumab):** theoretical antagonism; BPC-157 promotes angiogenesis.
- **Immunosuppressants:** unstudied.
- No documented small-molecule interactions at standard intranasal dosing.

**Dose-dependent risk profile:**
- 200–500 mcg/day intranasal: well-tolerated, clinical safety established at this range.
- Higher doses (multi-mg systemic, IM injection): pushes into less-characterized territory; main risk is sourcing-quality variability.
- Long-term continuous use beyond 6 months has minimal published human safety data — pulse dosing or treatment cycles are conservative.

**Stack interactions (within this catalog):**
- **Synergy with KPV (non-overlapping):** see KPV entry.
- **Synergy with omega-3 SPMs:** both promote resolution-phase tissue repair (efferocytosis, M1→M2 switching).
- **No ABCG2 interaction.**

**Cost:** Existing supply (continue current)

---

### Sulforaphane (Broccoli Sprouts)

**Category:** Phytonutrient

**Mechanism:** Activates Keap1-Nrf2 pathway → master regulator of cellular antioxidant defense; cross-talk with NF-κB (CP1/CP2). **Sub-μM Nrf2 activation: EC50 = 580 nM** (*J Med Chem* 2019, ChEMBL) — rare potency for a food-derived compound. **ABCG2 induction bonus:** Sulforaphane activates Nrf2 in enterocytes → upregulates intestinal ABCG2 expression, increasing gut urate secretion capacity (In Vitro + Animal Model; source: abcg2-modulators.md). This makes sulforaphane the only stack compound that simultaneously suppresses NLRP3 priming (CP1/CP2) AND enhances the gut-lumen sink substrate supply.

**Evidence level:** Established (Nrf2 activation) + **Animal Model hyperuricemia (2026-04-23 re-audit, PROMOTED from Tier 4)** — Wang 2022 *J Adv Res* (PMID 36371056): sulforaphane decreased urate synthesis + increased renal urate excretion + Nrf2-mediated epigenetic modification in hyperuricemic rats. This bridges the uric-acid and inflammation axes in a single compound. The prior "no gout-specific evidence" framing was keyword-gated on "gout" in abstracts and missed the hyperuricemia rat model. (source: nlrp3-inhibitor-screen.md 2026-04-23 re-audit) **Upgraded to Tier 2 on 2026-05-05** with two additional citations: Yang 2018 *Rheumatology (Oxford)* (PMID 29340626) — oral SFN attenuated MSU-crystal-induced foot-pad swelling and air-pouch acute gout in mice (Animal Model, oral); Greaney 2015 *J Leukoc Biol* (PMID 26269198) — sulforaphane inhibits NLRP1, NLRP3, NAIP5/NLRC4, and AIM2 inflammasomes **independent of Nrf2** in macrophages and in vivo acute gout peritonitis. Adds a direct caspase-1 / inflammasome-assembly mechanism distinct from the Nrf2 → ABCG2 / NF-κB axis.

**Population context:** Broad applicability. Animal-model UA evidence is in male rats; sex-differential effect on urate axis is not characterized. Goitrogenic effect of cruciferous glucosinolates is dose-dependent and clinically negligible at supplement-relevant doses, but patients with overt iodine deficiency or untreated hypothyroidism may want iodine adequacy in parallel. Hashimoto's patients: cruciferous goitrogen concern is largely overstated at dietary doses but present at concentrated extract doses.

**Dosing range:**
- **Raw broccoli sprouts:** 100–150g/day (contains glucoraphanin + myrosinase)
  - Must be raw/freshly chopped — cooking kills myrosinase and defeats the mechanism
  - Chewing or blending activates the conversion: glucoraphanin → sulforaphane
- **Sulforaphane supplement:** ~50 mg/day (extract or stabilized form)
- **Bioavailability hack:** If using cooked broccoli, add mustard seed powder (~1–2 tsp) to restore myrosinase activity
- **Highest bioavailability:** Freeze-dried broccoli sprout powder with active myrosinase in capsule form

**Contraindications:** Untreated hypothyroidism with iodine deficiency (theoretical, dose-dependent goitrogen effect). Severe G6PD deficiency (Nrf2 activators interact with the glutathione pathway — clinically minor at supplement doses but worth noting). Pregnancy: dietary intake fine; concentrated extract doses unstudied.

**Drug interactions:**
- **Acetaminophen (paracetamol):** sulforaphane upregulates phase II detox enzymes including glutathione synthesis — theoretically protective against acetaminophen hepatotoxicity rather than antagonistic, but quantitative impact is small.
- **CYP3A4 substrates with narrow therapeutic index:** sulforaphane modestly induces phase II conjugation; minor effect on CYP3A4-cleared drugs (tacrolimus, cyclosporine, some statins) is theoretically possible but clinically not significant at dietary or supplement doses.
- **Levothyroxine:** dietary cruciferous intake at any reasonable level is fine; theoretical iodine-uptake competition is overstated.

**Dose-dependent risk profile:**
- 50 mg/day sulforaphane equivalent or 100–150g/day raw sprouts: well-tolerated; standard supplement range.
- Concentrated extracts >100 mg/day: GI upset, sulfurous breath/body odor; theoretical goitrogen effect approaches clinical relevance but still small in iodine-replete individuals.
- Raw broccoli >300g/day chronic: goitrogen effect becomes clinically detectable in iodine-deficient individuals.

**Stack interactions (within this catalog):**
- **Stack synergy (Nrf2 activator cluster):** sulforaphane + quercetin + oridonin all activate Nrf2 — cumulative effect at the Nrf2 axis but diminishing-returns regime; combining all three is redundant rather than additive at the maximal-effect ceiling.
- **ABCG2 axis:** Nrf2 activation **transcriptionally induces ABCG2** in enterocytes (gut-selective at moderate; also induces hepatic and BBB Nrf2-driven targets at high systemic exposure). Per [abcg2-modulators.md](./abcg2-modulators.md), sulforaphane is a Tier 1 inducer of the gut urate sink — **synergistic with the platform thesis** rather than antagonistic. Distinct from curcumin/quercetin/EGCG/genistein which are functional inhibitors of the same transporter.
- **Synergy with NAC:** both push the glutathione/Nrf2 axis (CP2).

**Cost:** $5–10/week (raw sprouts) or $20–30/month (supplement)

---

### Theaflavins (Black Tea Polyphenols) — ADDED 2026-05-05

**Category:** Phytonutrient / NLRP3 inhibitor / multi-transporter renal urate handling

**Mechanism:** Theaflavins are dimeric polyphenols formed when EGCG and ECG are oxidized by polyphenol oxidase during black-tea fermentation; they are the dominant red-orange pigments of black tea, oolong, and pu'er. **Mechanism is distinct from EGCG:** theaflavins disrupt the **NLRP3-NEK7 interaction** downstream of mitochondrial ROS suppression (CP2/CP3 — assembly-step), whereas EGCG's dominant route is proteasome-mediated IκB stabilization (CP1a). **Unique to theaflavins in the OE stack:** simultaneous downregulation of **URAT1 + GLUT9** (apical and basolateral renal urate reabsorption) and upregulation of OAT1/OCTN1/OAT2/Oct1/2 (proximal-tubule secretion) — the only multi-transporter renal urate handling compound in the stack besides carnosine, and without carnosine's serum-carnosinase clearance ceiling. Secondary CP1a coverage via TNFSF14/HVEM modulation (TF3 specifically; Hosokawa 2010 PMID 20461739 — already cited in `tnfsf14-gout-target.md`).

**Evidence level:**
- **In vitro:** Chen 2023 *Acta Pharmacol Sin* (PMID 37221235) — 50–200 μM theaflavin dose-dependently inhibited NLRP3 inflammasome activation in LPS-primed macrophages stimulated with **MSU crystals**, ATP, or nigericin; suppressed ASC speck formation, caspase-1 p10 cleavage, GSDMD-NT pyroptosis, and IL-1β release. Mechanism: protected mitochondrial function, reduced mtROS, blocked NLRP3-NEK7 interaction. (In Vitro)
- **Animal Model (oral, MSU peritonitis):** Same Chen 2023 paper — oral theaflavin significantly attenuated MSU-induced mouse peritonitis (acute-gout-flare proxy model). (Animal Model)
- **Mechanism review:** Chen 2023 *Phytomedicine* (PMID 36990009) — comprehensive anti-gout mechanism review covering URAT1/GLUT9 downregulation + OAT1/OCTN1/OAT2 upregulation + network-pharmacology prediction (ABCB1, MAPK14, TERT, STAT1, MMP2/14, BCL2 as anti-gout targets).
- **No human gout RCT exists.** Cardiovascular and lipid trials (700–2,500 mg/day theaflavin-enriched extract for 12+ weeks) establish a safety baseline at typical supplement doses.

**Population context:** Broad applicability. The unique URAT1 angle is particularly relevant for under-excreter phenotypes (URAT1 hyperactivity-driven hyperuricemia, the male-predominant subtype documented in `androgen-urate-axis.md`). No documented sex-differential effect specific to theaflavins.

**Dosing range:**
- **Theaflavin-enriched extract:** 200–500 mg/day, standardized to 30–80% theaflavins. TF3 (theaflavin-3,3'-digallate) is the most potent fraction; some commercial products specify TF3 content separately.
- **Black tea:** 4–6 cups/day delivers ~50–150 mg theaflavins. Pu'er > black > oolong on a per-gram-leaf basis.
- **Combine with EGCG, not substitute:** mechanism-orthogonal at NLRP3; additive when stacked.

**Contraindications:** Pregnancy (concentrated extract doses unstudied; dietary intake fine). Iron-deficiency anemia (theaflavins, like other tannins, chelate non-heme iron — separate from iron-containing meals or supplements by ≥1 hour).

**Drug interactions:**
- **CYP3A4 substrates with narrow therapeutic index:** weak inhibition (similar to other tea polyphenols); minor effect at supplement doses for tacrolimus, cyclosporine, simvastatin.
- **Iron supplements / iron-rich meals:** spaced dosing required.
- **Caffeine confounder:** black tea contains caffeine; concentrated theaflavin extracts may or may not be decaffeinated — check the label.

**Dose-dependent risk profile:**
- 200–500 mg/day theaflavin-enriched extract: well-tolerated at supplement range based on cardiovascular trial data.
- >1,000 mg/day chronic: GI upset (tannin-driven), possible iron-status drift; not gout-specific risk.

**Stack interactions (within this catalog):**
- **EGCG (additive, not redundant):** EGCG and theaflavins overlap on TNFSF14/HVEM but the dominant non-redundant activities are different (EGCG → proteasome 86 nM; theaflavins → URAT1/inflammasome assembly). Combining adds CP1a + CP2/CP3 + URAT1 coverage. Strong recommended pairing.
- **Carnosine (overlap at URAT1 — pick one):** both downregulate URAT1 in animal models. Theaflavins do not face the carnosinase clearance ceiling. **Diminishing returns if stacked at maximum dose; pick one for the URAT1 axis** — theaflavins are favored if the carnosinase question is unresolved.
- **Sulforaphane / quercetin / oridonin (Nrf2 axis):** theaflavins do not strongly activate Nrf2. Mechanism-orthogonal — combine without redundancy.
- **No ABCG2 interaction documented.** Theaflavins are not on the curcumin/quercetin/EGCG/genistein ABCG2 functional-inhibitor list per `abcg2-modulators.md`, but a direct theaflavin-on-ABCG2 study has not been done.

**Cost:** $20–40/month for theaflavin-enriched supplement (300 mg/day). ~$10/week if relying on brewed black tea.

**Reference:** [theaflavins.md](./theaflavins.md) for the full dossier including TF1/TF2A/TF2B/TF3 sub-fraction context, formulation strategies, and open questions.

---

### Oridonin (Rabdosia rubescens Extract)

**Category:** Natural Compound / NLRP3 Inhibitor (direct, curated in ChEMBL)

**Mechanism:** Covalently binds Cys279 in NLRP3 NACHT domain (Michael addition); blocks NLRP3-NEK7 interaction (CP2). Also activates Nrf2 and suppresses NF-κB (CP1/CP2).

**Evidence level:** Established — Nature Communications 2018 (cell-free / mouse covalent-binding kinetics at 0.5–2 µM); **curated human THP-1 cellular IC50 = 5.18 μM** per ChEMBL v34 (*Eur J Med Chem* 2023, 2026-04-23 MCP cross-check). The two figures measure different things — 0.5–2 μM is covalent-binding potency in cell-free / mouse assays; 5.18 μM is human cellular IC50. Oridonin is one of only two compounds in the full wiki stack with a curated direct human NLRP3 bioactivity in ChEMBL (the other is dapansutrile at 1.0 μM human MDM). (In Vitro; source: nlrp3-inhibitor-screen.md)

**Population context:** Broad applicability for NLRP3 mechanism. No documented sex-differential effect. Mostly studied in rodent models and Chinese-medicine clinical literature; English-language clinical trial data is thin. Caution in patients on covalent-mechanism medications (irreversible MAOIs, some PPIs at high dose, omeprazole) — not a known clinical interaction but mechanistically plausible.

**Dosing range:** 50–100 mg/day

**Form:** Rabdosia rubescens extract or purified oridonin

**Sourcing:**
- Chinese herb suppliers (Solstice Medicine, Dragon Herbs)
- Research chemical suppliers (Sigma, MedChemExpress, Selleck Chem)

**Contraindications:** Pregnancy (insufficient data; covalent-binding mechanism warrants caution). Pediatric use. Active hepatic disease (some Rabdosia preparations have hepatotoxicity case reports at high TCM-formula doses). Combination with other covalent-mechanism drugs without spacing.

**Drug interactions:**
- **CYP3A4 substrates:** preliminary in vitro data suggests modest CYP3A4 inhibition by oridonin — relevant for tacrolimus, cyclosporine, simvastatin, some calcium channel blockers, and direct oral anticoagulants.
- **Omeprazole, PPIs:** mechanistic-extrapolation concern only; no clinical data.
- **Covalent-mechanism drugs (clopidogrel, prasugrel, aspirin at antiplatelet dose):** theoretical compounding of covalent off-target effects; no clinical signal.

**Dose-dependent risk profile:**
- 50–100 mg/day purified oridonin: tolerated in published TCM and supplement dosing; main risk is sourcing-quality and standardization.
- 200–500 mg/day high-dose extracts: case reports of transient ALT elevation; not common but flagged.
- Sourcing variability: Rabdosia rubescens whole-extract preparations contain other diterpenoids with unclear safety profiles. Purified oridonin from research chemical suppliers is more characterizable.

**Stack interactions (within this catalog):**
- **Synergy with sulforaphane, quercetin (Nrf2 axis):** all three are Nrf2 activators; cumulative effect with diminishing returns.
- **Mechanistic complementarity with BCP, BHB, dapansutrile (CP2):** oridonin (Cys279 covalent), BCP (CB2 / TLR4), BHB (K+ efflux), dapansutrile (NACHT) all suppress NLRP3 assembly through distinct molecular touch-points — orthogonal additivity expected.
- **No documented ABCG2 interaction.**

**Cost:** $30–60/month

---

### Omega-3 (High EPA / DHA)

**Category:** Fatty Acid / SPM Precursor

**Mechanism:**
- EPA → Resolvin E1 (RvE1)
- DHA → Resolvin D1/D2 (RvD1/D2), Protectin D1 (PD1), Maresin 1 (MaR1)
- These specialized pro-resolving mediators (SPMs) suppress neutrophil recruitment (massive effect in gout flares), promote M1→M2 macrophage switching, and enhance efferocytosis
- Hits CP1 (priming suppression) and CP5a/CP5b (IL-1β downstream effects + active resolution via ALX/FPR2)
- **Direct MSU gout evidence (2026-04-24):** RvD1 reduced mechanical hyperalgesia, joint IL-1β, leukocyte recruitment, and ASC speck formation in murine gout (Zaninelli 2022; Animal Model); MaR1 suppressed gout inflammation via Prdx5 → AMPK/Nrf2 (Jiang 2023; Animal Model). This makes omega-3-derived SPMs among the most gout-specific compounds in the stack at CP5b. See [SPM Resolution Pathway](./spm-resolution-pathway.md). (source: spm-resolution-pathway.md)

**Evidence level:** Established

**Population context:** Broad applicability. Pregnancy: DHA is recommended (fetal neural development); EPA-dominant formulations are less studied in pregnancy. Older adults on antiplatelet/anticoagulant therapy: bleeding-risk amplification at >3g/day combined EPA+DHA. Atrial fibrillation: high-dose (>4g/day prescription-grade) omega-3 has a modest signal of new-onset AF in recent RCTs (e.g., STRENGTH, REDUCE-IT post-hoc) — not at concern at typical 1–2g/day doses, but flagged at the upper end.

**Dosing range:** 3–4g EPA+DHA daily

> **DHA-specific update (2026-04-24 Pass 2 synthesis):** The direct MSU-gout animal evidence driving this entry's CP5b ranking is **DHA-derived, not EPA-derived**:
> - RvD1 (DHA-derived) — murine MSU gout (Zaninelli 2022, PMID 35716378)
> - MaR1 (DHA-derived) — MSU peritonitis (Jiang 2023, PMID 37996809)
> - DHA separately correlates with lower circulating TNFSF14 (Huang 2024, PMID 38235898, Mendelian randomization — see [tnfsf14-gout-target.md](./tnfsf14-gout-target.md))
>
> **For gout-specific use, prefer DHA-emphasis formulations or high-DHA fish oils.** EPA is not inactive (EPA → RvE1 at CP5b; EPA substrate competition reduces LTB4 at CP6a), but the specific pro-resolving and TNFSF14-suppressing signals that matter most for gout are DHA-derived. Prior "2:1 or 3:1 EPA:DHA" guidance was generalized from non-gout contexts and does not match the gout-specific data.

**Form:** Fish oil (DHA-emphasis preferred for gout), algae oil (often DHA-only), or krill oil

**Contraindications:** Severe fish/shellfish allergy (algae oil is the alternative). Active variceal bleeding. Pre-operative window (most surgeons request hold 7–14 days before procedures). Severe atrial fibrillation under aggressive rate control with high-dose (>4g/day) prescription icosapent ethyl (modest AF risk signal).

**Drug interactions:**
- **Warfarin:** high-dose omega-3 (>3g/day combined) increases bleeding risk via platelet inhibition; INR may shift. Monitor and consider lower dose or hold.
- **Direct oral anticoagulants (apixaban, rivaroxaban, dabigatran):** additive bleeding risk at high doses; less INR-monitorable than warfarin.
- **Antiplatelet drugs (aspirin, clopidogrel, prasugrel, ticagrelor):** additive antiplatelet effect at >3g/day.
- **Statins:** generally synergistic on cardiovascular risk; no negative pharmacological interaction.
- **Antihypertensives:** modest additive BP-lowering at multi-g/day omega-3.

**Dose-dependent risk profile:**
- 1–2g/day combined EPA+DHA: well-tolerated; main effect is mild. Standard cardiovascular and dietary range.
- 3–4g/day (gout-relevant range): bleeding risk becomes clinically detectable in patients on antiplatelets/anticoagulants. AF risk signal absent at this range.
- >4g/day prescription-grade icosapent ethyl: documented small AF risk signal in REDUCE-IT and STRENGTH trial post-hoc analyses. Bleeding risk more pronounced.
- Quality matters more than gross dose: oxidized fish oil at any dose is pro-inflammatory (peroxide value flag).

**Practical note:** Most consumer fish oil is heavily oxidized (damages efficacy). Use pharmaceutical-grade options:
- Nordic Naturals Pro Series (molecularly distilled)
- Omegaquest (clinical grade)
- Or direct EPA supplementation (prescription icosapent ethyl, or OTC concentrated EPA)

**Stack interactions (within this catalog):**
- **Synergy with NAC, sulforaphane:** SPM resolution layered on Nrf2/glutathione antioxidant defense.
- **Synergy with KPV, BPC-157 at the resolution phase (CP5):** SPMs drive efferocytosis; peptides drive cytoprotection — complementary.
- **Caution layered with EGCG, quercetin in patients on warfarin:** all three have modest antiplatelet effects; combined effect on bleeding risk is multiplicative at upper-end doses.
- **No documented direct ABCG2 effect.** PPARγ-mediated effects of omega-3 metabolites would *induce* ABCG2 (per [abcg2-modulators.md](./abcg2-modulators.md), PPARγ row); favorable for the gut-lumen-sink platform.

**Cost:** $30–50/month (quality matters)

---

### Cherry Extract (Tart Cherry Concentrate)

**Category:** Botanical

**Mechanism:** Anthocyanins inhibit xanthine oxidase (direct uric acid production) and suppress CRP/IL-6; secondary anti-inflammatory

**Evidence level:** Supported (published pilot trials in gout; modest effect)

**Population context:** Broad applicability. No documented sex-differential effect. Diabetic / pre-diabetic patients should account for sugar load in cherry juice concentrate (8–12 oz can carry 30–50g sugar) — capsule form sidesteps this. Patients on tight glycemic control or low-FODMAP regimens: capsules preferred.

**Dosing range:**
- Tart cherry juice concentrate: 8–12 oz/day (or 2–3 tbsp concentrate in water)
- Dried cherry extract capsules: 500–1500 mg/day

**Contraindications:** None absolute. Glycemic-load concern in T2DM if using juice concentrate. Salicylate sensitivity (cherries contain natural salicylates; rare clinical relevance).

**Drug interactions:**
- **Warfarin:** rare case reports of mild INR shifts at high cherry juice intakes (likely vitamin K and salicylate effects); not robust signal.
- **Allopurinol / febuxostat:** pharmacodynamic synergy (both reduce UA via XO inhibition); generally additive rather than antagonistic, but layering may exceed XO-suppression target.
- **NSAIDs:** mild salicylate cross-effect; clinically negligible.

**Dose-dependent risk profile:**
- 500–1500 mg capsule extract or 8–12 oz juice/day: well-tolerated. Effect size modest (~15–20% CRP reduction).
- Higher juice intakes (>16 oz/day chronic): GI upset, glycemic load. No upper-bound toxicity signal but diminishing returns past this range.

**Stack interactions (within this catalog):**
- **Synergy with quercetin, EGCG (XO axis):** all three inhibit xanthine oxidase to varying degrees — additive effect on UA production.
- **Synergy with engineered uricase (future):** XO inhibition reduces UA *production*; gut-lumen uricase reduces UA *pool* — the two mechanisms compose.
- **No ABCG2 interaction documented.**

**Cost:** $20–30/month

---

### NAC (N-Acetyl Cysteine)

**Category:** Amino Acid Precursor

**Mechanism:**
- Replenishes glutathione (master intracellular antioxidant)
- Scavenges ROS (CP2)
- Targets mitochondrial dysfunction

**Evidence level:** Established

**Population context:** Broad applicability. No documented sex-differential effect. Asthma patients: NAC can transiently increase mucus secretion (mucolytic effect) — this is therapeutic in COPD/CF but can transiently worsen reactive airway symptoms in unstable asthma. Patients on nitroglycerin therapy: NAC potentiates nitrate effects (hypotension risk). Pregnancy: NAC is FDA-approved for acetaminophen overdose in pregnancy; otherwise generally regarded as safe.

**Dosing range:** 600–1,200 mg/day (split AM + evening)

**Contraindications:** Active asthma exacerbation (theoretical mucus-thinning concern; clinically minor). Pregnancy outside acetaminophen-overdose context: insufficient safety data at chronic supplement dose.

**Drug interactions:**
- **Nitroglycerin / isosorbide / nitrate-class:** potentiates nitrate-induced hypotension; clinically relevant in cardiac patients.
- **Activated charcoal:** binds NAC; spacing required if using both.
- **Carbamazepine:** NAC may reduce serum carbamazepine levels (case-report level); monitor in epilepsy.

**Dose-dependent risk profile:**
- 600–1200 mg/day: well-tolerated; sulfurous odor / GI upset are the practical limiters.
- 1800–2400 mg/day (high-dose protocols, e.g., trichotillomania, COPD): mostly tolerated; nausea more common.
- IV protocols (acetaminophen toxicity) reach much higher doses safely in supervised settings.

**Stack interactions (within this catalog):**
- **Synergy with sulforaphane, omega-3:** all three activate the antioxidant defense / resolution axis (CP2 + CP5).
- **Mild antagonism conceptual concern:** NAC's glutathione restoration could theoretically blunt some oxidative-stress-dependent signals (e.g., apoptosis induction in cancer cells); irrelevant to gout.
- **No ABCG2 interaction documented.**

**Cost:** $10–15/month

---

### EGCG (Green Tea Catechin) — Widest-Spectrum Natural Compound

**Category:** Flavonoid / Polyphenol

> **See [wiki/egcg.md](./egcg.md) for the full dossier** — proteasome → IκBα → NF-κB unifying mechanism, safety-ceiling rationale, gout-specific evidence summary, and open mechanistic questions. This entry keeps only the short stack-level summary.

**Mechanism (4 of 7 chokepoints, unified through the proteasome → IκBα → NF-κB axis):**
- **CP1 (NF-κB priming):** **20S proteasome inhibition → IκBα stabilization → NF-κB blockade** (IC50 = 86 nM human proteasome, ChEMBL v34, *Bioorg Med Chem* 2010 / *Eur J Med Chem* 2019). Prior "IKK inhibition" framing is downstream of / redundant with this — IKK's sole output in this pathway is to mark IκBα for proteasomal destruction, which EGCG blocks one step later.
- **CP1a (TNFSF14 / LIGHT direct suppression):** Hosokawa 2010 (PMID 20461739) — **the only stack compound with direct TNFSF14 data**. Gout-relevant since TNFSF14 is an emerging gout-specific priming amplifier (see [tnfsf14-gout-target.md](./tnfsf14-gout-target.md)). (In Vitro; source: nlrp3-inhibitor-screen.md)
- **CP4 (caspase-1 suppression):** pro-caspase-1 transcription is NF-κB-dependent → same proteasome/IκBα axis blocks its induction. ROS reduction is a secondary contributor. **Sub-100 nM proteasome potency is a hepatotoxicity dose-ceiling flag** for intense-use protocols.
- **CP5a (IL-1β receptor-downstream suppression):** same proteasome/IκBα axis on receiving cells (chondrocytes, synoviocytes) blocks IL-1β-induced NF-κB signaling.

**Evidence level (PROMOTED to Tier 2 supplement use, 2026-04-23 re-audit):** Direct MSU mouse gout evidence — Lee 2019 *Molecules* (PMID 31174271): EGCG blocked MSU-induced caspase-1(p10) and IL-1β in primary mouse macrophages; oral EGCG alleviated MSU-injected mouse foot inflammation via NLRP3 suppression; mechanism = mtDNA synthesis block + ROS reduction. Plus hyperuricemic mouse serum-UA lowering (Yu 2024, *Food Funct*, PMID 38757391). The prior "no gout evidence" framing missed these. (Animal Model; source: nlrp3-inhibitor-screen.md)

**Population context:** Broad applicability for NLRP3 mechanism, but **functional ABCG2 inhibitor** at supplement doses — relevant for the engineered-uricase platform. Yu 2024 mouse data shows favorable in vivo phenotype on urate axis in hyperuricemic mice despite EGCG's known in vitro BCRP inhibition; net clinical effect on the gut sink in androgen-dominant patients is unresolved (see Stack-level contradictions section). Hepatotoxicity risk is **dose-dependent and sex-irrelevant** but amplified by alcohol, fasting, pre-existing liver disease, and male androgen-axis liver-stress patterns. Avoid in pregnancy at supplement (>500 mg/day) doses; food-level intake (matcha, green tea) is acceptable.

**Dosing range:** 400–800 mg EGCG/day (standardized green tea extract) OR 3–5 cups matcha/day

**Form:** Standardized green tea extract (typically 50% EGCG) OR matcha powder (highest natural concentration)

**Contraindications:** Active hepatic disease or recent ALT/AST elevation. Pregnancy at supplement doses (folate antagonism + theoretical hepatotoxicity). Concurrent alcohol use disorder or chronic high alcohol intake (additive hepatotoxicity). Iron-deficiency anemia (EGCG strongly chelates non-heme iron — separate iron supplementation by 2+ hours from EGCG).

**Drug interactions:**
- **Warfarin:** EGCG may modestly antagonize warfarin (vitamin K-like effect from green tea has been reported; effect is small but can shift INR).
- **Bortezomib (proteasome inhibitor chemotherapy):** EGCG directly binds and inactivates bortezomib; **avoid coadministration** in oncology patients on bortezomib.
- **Beta-blockers (nadolol):** EGCG reduces nadolol oral bioavailability via OATP1A2 inhibition; clinically significant.
- **Hepatotoxic drugs (acetaminophen, isoniazid, methotrexate, statins):** additive hepatotoxicity risk at high EGCG doses.
- **Iron supplements:** chelation; separate dosing.
- **CYP3A4 substrates (modest):** in vitro inhibition; clinically modest.

**Dose-dependent risk profile:**
- 200–400 mg/day EGCG (standardized extract): well-tolerated; comparable to heavy daily green tea drinker.
- 400–800 mg/day (gout-relevant range): hepatotoxicity risk becomes detectable, especially under fasting conditions or with alcohol. Periodic ALT/AST monitoring recommended.
- >800 mg/day: case reports of serum hepatitis (idiosyncratic, low absolute incidence). Hard ceiling for chronic intense use.
- Matcha-based dosing (food matrix) appears safer at equivalent EGCG content than capsule extracts — likely due to slower absorption and matrix-buffered exposure.

> **Hepatotoxicity dose ceiling:** The 86 nM 20S proteasome IC50 is a safety flag at high-dose intense use. Stay at or below 800 mg EGCG/day; avoid combining high-dose EGCG with alcohol or other hepatotoxic agents; consider periodic ALT/AST monitoring at sustained high doses.

**Stack interactions (within this catalog):**
- **Stack contradiction (ABCG2 axis):** EGCG is a functional ABCG2 inhibitor (Tier 2 contradiction; see Stack-level contradictions table at bottom and [abcg2-modulators.md](./abcg2-modulators.md)). Yu 2024 (PMID 38757391) shows net-favorable effect on ABCG2/URAT1/GLUT9 in vivo in hyperuricemic mice — direction opposite to in vitro inhibition — so net effect on the gut sink in androgen-dominant patients is **unresolved**. Avoid layering EGCG with curcumin, quercetin, genistein in high-T or Q141K-positive patients until the in vivo question is resolved.
- **Synergy with quercetin, sulforaphane (NF-κB / Nrf2 axis):** mechanistically compatible at the NLRP3 priming level.
- **Hepatotoxic stacking concern:** EGCG + high-dose curcumin + acetaminophen / alcohol creates a multiplicative liver-stress profile. Stagger or substitute.

**Summary framing:** EGCG is the widest-spectrum natural compound in the current Open Enzyme stack, hitting four of seven chokepoints. Its 20S proteasome sub-100 nM activity is a hepatotoxicity flag at high dose — safety dose-ceiling for intense use protocols.

> ⚠️ **ABCG2 functional inhibitor warning (source: abcg2-modulators.md):** EGCG is a documented functional ABCG2/BCRP inhibitor in pharmacology assays. Yu et al. 2024 (*Food Funct*, PMID 38757391) showed a net-favorable effect on ABCG2/URAT1/GLUT9 expression at the tissue level in a hyperuricemic mouse model — direction opposite to the in vitro inhibition story. Net clinical effect on the gut urate sink is unresolved. Until resolved, treat high-dose EGCG (>400 mg/day) as a potential ABCG2 inhibitor in the gut-lumen context, particularly in androgen-dominant or Q141K-positive patients. (Mixed: In Vitro inhibition vs. Animal Model in vivo; source: abcg2-modulators.md)

**Cost:** $15–25/month (standardized extract); $30–50/month (high-grade matcha)

---

### Limonene (d-Limonene, Citrus Peel Oil) — PROMOTED Tier 3 Supplement

**Category:** Monoterpene / Food Additive (GRAS)

**Mechanism:** Nrf2 activator + TLR4 suppression (upstream NLRP3 priming block); also suppresses NF-κB, NLRP3, ASC, caspase-1 expression via NRF2-dependent pathway.

**Evidence level (PROMOTED to Tier 3 supplement, 2026-04-23 re-audit):** Direct rat PO+MSU dual gout model — Venkatesan 2025 *Nutrients* (PMID 41515190): 50 mg/kg limonene reduced paw thickness, serum UA, IL-1β/TNF/IL-6, and improved antioxidant status; authors invoke NLRP3-IL-1β suppression as the mechanistic frame. (Animal Model; source: nlrp3-inhibitor-screen.md)

**Population context:** Broad applicability. No documented sex-differential effect. GERD patients: d-limonene is actually marketed for GERD support, but at the same dose can transiently worsen reflux in subset (paradoxical effect from LES relaxation in some). Pregnancy: insufficient supplement-dose data; food-level intake fine.

**Dosing range:** 500–1,000 mg d-limonene/day (standardized capsules). Supplement capsule is the practical path — engineered microbial production is infeasible (<20 mg/L titers + volatility).

**Form:** d-limonene softgel capsules (commonly sold for GERD / digestive support)

**Contraindications:** None absolute. Citrus allergy (rare; d-limonene is the dominant terpene in citrus peel).

**Drug interactions:**
- **CYP3A4 substrates (statins, calcium channel blockers, immunosuppressants):** d-limonene weakly induces CYP3A4 at chronic doses; clinical significance is small at the gout-relevant range.
- **Acid-suppression drugs (PPIs, H2 blockers):** mechanistic overlap with GERD use; not a pharmacological conflict.

**Dose-dependent risk profile:**
- 500–1,000 mg/day: well-tolerated. GRAS food-additive compound at much higher cumulative dietary exposure (orange peel, citrus oils in foods).
- >2 g/day chronic: case reports of mild hepatic enzyme elevation (rare; idiosyncratic).
- Inhalation/vaporized forms have very different PK and are not appropriate for NLRP3/gout endpoint use.

**Stack interactions (within this catalog):**
- **Synergy with sulforaphane, oridonin (Nrf2 axis):** cumulative Nrf2 induction with diminishing returns.
- **No ABCG2 interaction documented.**

**Cost:** $15–25/month

---

### Lactoferrin (Bovine) — NEW CP5 Entry

**Category:** Glycoprotein / Food-Grade Supplement

**Mechanism (CP5 — the one CP5-active entry in the stack that isn't a $300K/year biologic):**
- NLRP3 / caspase-1 / GSDMD axis suppression → reduces IL-1β and IL-18 output
- Orthogonal to polyphenol CP1 mechanisms and direct NLRP3 binders (CP2)
- Talactoferrin (recombinant human lactoferrin, ChEMBL2108651) reached Phase 3 oncology at multi-g/day oral doses — safety and oral bioavailability established

**Evidence level:** Animal (murine nephrotoxicity, PMID 37926296 — 300 mg/kg/day back-translates to ~3 g/day human); In Vitro (macrophages + IEC-6 intestinal epithelial cells); Clinical Phase 3 (talactoferrin oncology). Direct MSU-gout validation not yet published — CP5 mechanism is the gout-relevant class; priority experimental screen. (Animal Model + Clinical Trial; source: nlrp3-inhibitor-screen.md)

**Population context:** Broad applicability. No documented sex-differential effect. Iron-related considerations: lactoferrin is iron-binding but bovine lactoferrin in supplement form is largely iron-saturated (apo-lactoferrin vs holo-lactoferrin distinction matters mechanistically). Patients with hemochromatosis: theoretical iron-loading concern with high-dose holo-lactoferrin; minor clinically. Bovine milk allergy: cross-reactive risk (lactoferrin is a milk protein).

**Dosing range:**
- Commercial oral bovine lactoferrin: 100–300 mg/day (typical capsule)
- Murine protective dose (300 mg/kg/day) back-translates to ~3 g/day human — achievable at engineered *P. pastoris* fermentation scale (3.5 g/L demonstrated, PMID 27294912)

**Form:** Bovine colostrum-derived capsules (commercial supplement); future: engineered *P. pastoris* or koji (*A. oryzae*) recombinant production

**Contraindications:** Bovine milk allergy. Hemochromatosis (relative; high-dose chronic only). Pregnancy: dietary lactoferrin from colostrum is generally regarded as safe; supplement-dose chronic is less characterized.

**Drug interactions:**
- **Iron supplements:** lactoferrin can compete with or chelate iron depending on its iron-saturation state; spacing recommended.
- **Antibiotics (tetracyclines, fluoroquinolones):** theoretical chelation via lactoferrin's iron-binding sites; minor clinical relevance, separate dosing if both prescribed simultaneously.
- **No major small-molecule pharmacological interactions documented.**

**Dose-dependent risk profile:**
- 100–300 mg/day (commercial capsule range): well-tolerated.
- 1–3 g/day (talactoferrin Phase 3 range): tolerated in oncology populations; GI symptoms most common.
- Bridge between commercial and trial doses (300 mg → 3 g) is the practical scale-up question for the platform.

**Stack interactions (within this catalog):**
- **Mechanism orthogonality (the strategic position):** lactoferrin is the only CP5-active stack compound that is not a $300K/year biologic (canakinumab) — fills a unique position. Mechanism does not overlap with polyphenol NF-κB/Nrf2 cluster.
- **No ABCG2 interaction documented.**

**Strategic position:** The only CP5 candidate in the stack that is fermentable at scale, food-grade, and has direct NLRP3/IL-1β evidence. Fills the Open Enzyme CP5 gap that canakinumab currently occupies at ~$300K/year. Koji expression not yet tried — potential future module for the Open Enzyme platform.

**Cost:** $30–60/month (bovine oral capsules, 300 mg/day)

---

### Carnosine (L-Carnosine, β-Alanyl-L-Histidine) — Dual UA + NLRP3

**Category:** Dipeptide / Endogenous Muscle Metabolite

**Mechanism (unique dual phenotype: serum UA reduction + NLRP3 suppression in same compound):**
- ROS scavenging, p-p65 (NF-κB) suppression, p-JNK dampening
- Direct NLRP3, caspase-1 suppression (downstream of ROS / NF-κB block)
- URAT1 and GLUT9 transporter modulation → enhanced renal urate excretion

**Evidence level:** Animal Model (hyperuricemia rat) — carnosine reduces serum uric acid AND suppresses NLRP3 inflammasome activation simultaneously; the only compound in the stack with this documented dual phenotype. (Amino Acids 2024; see [nlrp3-inhibitor-screen.md](./nlrp3-inhibitor-screen.md) for full citation trail.)

**Population context:** Broad applicability with **specific relevance to androgen-driven hyperuricemia**. Carnosine's URAT1 modulation is mechanistically aligned with reversing the androgen-driven URAT1 upregulation documented in [androgen-urate-axis.md](./androgen-urate-axis.md) — making carnosine particularly well-suited for male gout patients on TRT, SERMs, or with high endogenous T. Vegetarians/vegans: dietary carnosine intake is essentially zero from plant foods; supplementation produces a larger relative shift.

**Dosing range:** 500–1,000 mg/day oral L-carnosine (split doses preferred; dipeptide transporter-mediated absorption)

**Form:** L-carnosine capsules (widely available); avoid carnosine analogs (anserine, balenine) unless specified

**Contraindications:** None absolute. Pregnancy: insufficient supplement-dose data; dietary intake from meat fine.

**Drug interactions:** Minimal documented interactions. Mechanistically:
- **ACE inhibitors:** carnosine is endogenously degraded by serum carnosinase; ACE inhibitors are unrelated.
- **Histidine-axis drugs (rare):** clinically negligible.

**Dose-dependent risk profile:**
- 500–1,000 mg/day: well-tolerated. Serum carnosinase rapidly degrades free carnosine, so plasma levels are transient — practical absorption ceiling.
- Higher doses produce diminishing returns due to carnosinase saturation; β-alanine supplementation is a precursor strategy that bypasses some of this but produces tingling (paresthesia) at therapeutic doses.

**Stack interactions (within this catalog):**
- **Strong synergy with engineered-uricase platform (mechanism-orthogonal):** carnosine reduces UA via URAT1/GLUT9 (renal) modulation; engineered uricase reduces UA via gut-lumen sink. Two non-overlapping mechanisms — additive expected.
- **Synergy in androgen-driven hyperuricemia:** counters URAT1 upregulation that exogenous T / SERMs / AAS produce.
- **No ABCG2 interaction documented.** Does not antagonize the platform.

**Strategic position:** Unique dual-phenotype (UA + NLRP3) that other stack compounds don't match. ~150 mg/L estimated titer in engineered yeast — moderate engineering complexity, lower titer than polyphenols, but the only compound that compresses both problems (hyperuricemia + inflammasome) into a single molecule. Co-engineering with uricase in koji is the long-term platform play.

**Cost:** $20–35/month (oral L-carnosine, 500–1,000 mg/day)

---

### Quercetin (Phytosome Form Preferred)

**Category:** Flavonoid

**Mechanism (reordered 2026-04-24 by dominant curated activity):**
- **PRIMARY — 5-lipoxygenase (5-LOX) inhibition, IC50 = 300 nM (CP6a)** — blocks leukotriene B4 (LTB4) production, suppressing the neutrophil chemotaxis that amplifies MSU-driven gout flares. This is quercetin's single most potent curated ChEMBL bioactivity (*J Med Chem* 1991, ChEMBL v34, 2026-04-23). More potent than its NF-κB/NLRP3-pathway IC50 (~11 μM functional) by ~36×. Quercetin is now framed primarily as a CP6a compound on the exploit map. (In Vitro; source: nlrp3-inhibitor-screen.md)
- **SECONDARY — NF-κB inhibition (CP1)** — NLRP3 pathway modulator via NF-κB priming block (not direct NLRP3 binding; zero curated human NLRP3 IC50 in ChEMBL)
- **TERTIARY — Xanthine oxidase inhibition** — direct uric acid production reduction (metabolic / upstream of MSU crystal formation)
- Mast cell stabilization

> ⚠️ **ABCG2 functional inhibitor warning (source: abcg2-modulators.md):** Quercetin is a competitive substrate/inhibitor of ABCG2 at low μM gut-lumen concentrations — the same range achieved at supplement doses (500–1,000 mg/day). This means quercetin may acutely suppress intestinal urate secretion, pharmacologically antagonizing the gut-lumen-sink thesis. The net effect is dose-dependent and context-dependent: chronic low-dose dietary quercetin may show transcriptional upregulation of ABCG2 in some animal studies, but supplement-grade acute dosing is the concern. **For male gout patients on TRT, SERMs, or with Q141K polymorphism — where ABCG2 is already suppressed — high-dose quercetin supplementation may compound the deficit.** (In Vitro; source: abcg2-modulators.md)

**Evidence level:** In Vitro 300 nM 5-LOX IC50 per ChEMBL; Established (NF-κB + xanthine oxidase)

**Labeling note:** Quercetin has **zero curated direct human NLRP3 bioactivities in ChEMBL** — it is more accurately an "NLRP3 pathway modulator" (NF-κB priming block) than a direct NLRP3 binder. The gout-relevant case rests on three orthogonal mechanisms: NF-κB priming block, xanthine oxidase inhibition, and 5-LOX/LTB4 block. (source: nlrp3-inhibitor-screen.md)

**Population context:** Broad applicability for NLRP3/XO mechanism, but **functional ABCG2 inhibitor** at typical supplement doses (Stack-level contradiction; see bottom section and [abcg2-modulators.md](./abcg2-modulators.md)). Particularly relevant for male gout patients on TRT/SERMs/AAS or Q141K-positive patients where the gut-lumen-sink is already androgen-suppressed — high-dose quercetin may further close the leaky-gate. Pregnancy: limited supplement-dose data; dietary intake from onions, apples, capers is fine.

**Dosing range:** 500–1,000 mg/day

**Form:** Phytosome (Quercefit) has ~20× better absorption than standard quercetin

**Contraindications:** None absolute. Patients on tight CYP3A4-substrate dosing (cyclosporine, tacrolimus) should be cautious at high-dose quercetin. Pregnancy: insufficient supplement-dose data.

**Drug interactions:**
- **CYP3A4 substrates (cyclosporine, tacrolimus, simvastatin, calcium channel blockers):** quercetin inhibits CYP3A4 in vitro at supplement-relevant gut concentrations; clinically detectable drug-level increases possible.
- **Warfarin:** modest antiplatelet/anticoagulant effect; INR may shift.
- **Quinolone antibiotics (ciprofloxacin, levofloxacin):** quercetin chelates and reduces absorption; separate dosing.
- **Allopurinol:** quercetin's XO inhibition is mechanistically additive — not necessarily problematic, but UA may drop more than expected when both are dosed together.

**Dose-dependent risk profile:**
- 250–500 mg/day standard quercetin or phytosome equivalent: well-tolerated; dietary range upper end.
- 500–1,000 mg/day (gout-relevant range): well-tolerated; CYP3A4 inhibition becomes clinically detectable.
- 1,500–2,000 mg/day chronic: rare nephrotoxicity case reports at very high doses; unlikely at the gout-relevant range.

**Practical note:** Triple mechanism: hits CP1 (priming), uric acid production (xanthine oxidase), AND neutrophil chemotaxis (5-LOX/LTB4). The 5-LOX leg is parallel to boswellic acids (AKBA) at the same target. Synergizes with sulforaphane (both Nrf2 activators). (Source: nlrp3-exploit-map.md)

**Stack interactions (within this catalog):**
- **Stack contradiction (ABCG2 axis):** quercetin is a functional ABCG2 inhibitor at low-μM gut concentrations — Tier 2 contradiction in the Stack-level contradictions table at bottom. Per [abcg2-modulators.md](./abcg2-modulators.md), chronic dosing also produces some transcriptional ABCG2 upregulation in animal studies — net effect on the gut-lumen sink is **dose- and duration-dependent and poorly characterized in humans**. Acutely (peak gut concentration after a high-dose phytosome), the inhibitory effect dominates.
- **Synergy with sulforaphane, oridonin (Nrf2 axis):** Nrf2 cluster.
- **Synergy with cherry extract (XO axis):** overlapping XO inhibition; additive UA reduction.
- **Caution with EGCG, curcumin, genistein:** all four are functional ABCG2 inhibitors — stacking them concentrates the gut-sink antagonism in androgen-dominant readers.

**Cost:** $15–25/month

---

### Beta-Caryophyllene (Black Pepper / Clove Extract)

**Category:** Sesquiterpene / CB2 Agonist / Food Additive (GRAS)

**Mechanism:** Selective CB2 receptor agonist (Ki ~155 nM; CB2-over-CB1 selectivity >100×). In MSU-induced gouty arthritis (rat, animal model), 100–400 mg/kg oral dose-dependently reduced ankle swelling, serum IL-1β/IL-6/TNF-α, and synovial NLRP3/caspase-1/ASC/TLR4/MyD88/NF-κB expression — hits CP1 (NF-κB via TLR4/MyD88) AND CP2 (NLRP3/caspase-1). Mechanistically distinct from oridonin (Cys279) or BHB (K⁺ efflux) — additive potential. (*Front Pharmacol* 2021;12:651305, PMID: 33967792.) (source: cannabinoids-terpenes.md)

**Evidence level:** Animal Model (MSU crystal rat gouty arthritis — the only cannabinoid or terpene with direct gout-model data)

**Population context:** Broad applicability. No documented sex-differential effect. CB2-selective mechanism avoids the CB1-mediated gut motility slowdown that would be a concern in EPI patients (relevant given the Open Enzyme dual-target focus). GRAS food additive; non-psychoactive.

**Dosing range:**
- Standardized beta-caryophyllene (BCP) supplement: 50–200 mg/day (available as copaiba oil extract, 45–55% BCP standardization)
- Dietary: Black pepper, clove, hops, copaiba — dietary intake typically <10 mg/day from food alone

> **Dose-translation caveat (flagged 2026-04-23, see `wiki/synthesis.md`):** The 2021 MSU rat gout efficacy was demonstrated at 100–400 mg/kg oral. BSA-scaled to a 70 kg human, that is ~1.1–4.5 g/day — **20–50× above the typical supplement dose listed above**. Whether 50–200 mg/day reproduces the synovial NLRP3/TLR4/NF-κB suppression seen in rats is unverified. Treat this entry as "plausible mechanism, dose adequacy unconfirmed" until a PK/PD translation check or human bioavailability study resolves the gap. The orthogonal CB2 mechanism still makes BCP a reasonable low-risk addition; just do not assume the rat dose-response translates to supplement-range doses.

**Contraindications:** None absolute. Pregnancy: dietary spice exposure is fine; supplement-dose chronic is unstudied.

**Drug interactions:**
- **CB2-targeted experimental drugs:** competitive at CB2; not clinically relevant outside research settings.
- **CYP2C9, CYP3A4 substrates:** mild in vitro inhibition; clinical relevance small at supplement doses.
- **Cannabinoid-class drugs (dronabinol, nabilone):** mechanism overlap (different receptor selectivity); no clear clinical conflict.

**Dose-dependent risk profile:**
- 50–200 mg/day BCP capsules: well-tolerated; food-additive level cumulative exposure.
- Higher doses up to 1 g/day in animal studies: tolerated; no hepatotoxicity signal.
- Inhalation/vaporized cannabis terpene products have very different PK and are not equivalent to oral BCP capsules for this endpoint.

**Practical note:** Non-psychoactive, not cannabis-derived (present in many food spices). GRAS food additive. Not a CB1 agonist — avoids the THC regulatory/psychoactivity concerns and the CB1-mediated gut-motility slowdown that would be a risk in EPI. (source: cannabinoids-terpenes.md)

**Stack interactions (within this catalog):**
- **Mechanism orthogonality (CP2):** distinct molecular touch-point from oridonin (Cys279), BHB (K+ efflux), dapansutrile (NACHT) — additive at the NLRP3-assembly level.
- **No ABCG2 interaction documented.**

**Cost:** $15–30/month (BCP-standardized copaiba capsules)

---

### Vitamin D3 + K2

**Category:** Fat-Soluble Vitamin

**Mechanism:** VDR activation suppresses NF-κB (CP1); K2 prevents vascular calcification (secondary benefit)

**Evidence level:** Established

**Population context:** Broad applicability with population-specific dosing. Sun-exposed individuals at temperate latitudes often need less; high-latitude / dark-skinned / indoor-occupation individuals need more. Pregnancy: D3 supplementation routinely recommended (2000–4000 IU). Patients with sarcoidosis, primary hyperparathyroidism, or granulomatous diseases: D3 supplementation can cause hypercalcemia and is contraindicated without specialist supervision. Patients on warfarin: K2 directly antagonizes warfarin effect and requires INR monitoring or dose adjustment.

**Dosing range:**
- Vitamin D3: 5,000–10,000 IU/day (target serum 50–70 ng/mL; test annually)
- K2 (MK-7): 200 mcg/day

**Contraindications:** Sarcoidosis or granulomatous disease (D3-driven hypercalcemia risk). Primary hyperparathyroidism. Hypercalcemia of any cause. **K2: warfarin therapy is a relative contraindication** — K2 directly antagonizes warfarin and requires INR re-stabilization or dose adjustment.

**Drug interactions:**
- **Warfarin:** K2 directly antagonizes warfarin via vitamin K-cycle competition; clinically significant. Requires INR monitoring with consistent K2 dosing or dose adjustment.
- **Thiazide diuretics:** D3-driven calcium retention is amplified; hypercalcemia risk.
- **Glucocorticoids:** can reduce D3 efficacy on bone via competing pathways.
- **Statins:** generally favorable interaction (D3 may modestly improve statin tolerance via myopathy risk reduction).
- **Anticonvulsants (phenytoin, phenobarbital, carbamazepine):** induce CYP24A1, accelerating D3 catabolism; higher D3 doses may be needed.

**Dose-dependent risk profile:**
- 1,000–4,000 IU/day D3: standard supplemental range; minimal hypercalcemia risk.
- 5,000–10,000 IU/day (gout-relevant range): track 25-OH-D level annually; target 50–70 ng/mL. Hypercalcemia rare in non-granulomatous patients at this range.
- >10,000 IU/day chronic: hypercalcemia risk becomes detectable; serum monitoring (Ca, 25-OH-D, PTH) recommended.
- K2 200 mcg/day: well-tolerated; no toxicity ceiling identified at typical supplement doses.

**Practical note:** Must be taken with fat to absorb

**Stack interactions (within this catalog):**
- **No major stack interactions.** D3 is mechanistically synergistic at the broad NF-κB suppression level but operates on its own axis (VDR).
- **No ABCG2 interaction documented.**

**Cost:** $10–15/month

---

## Section 2: SOON (Implementation Within 2-4 Weeks)

Compounds and approaches that are viable near-term but require medical discussion or sourcing from specialty suppliers.

### Disulfiram (Antabuse)

**Category:** Approved Drug / GSDMD Inhibitor

**Mechanism:** Covalently modifies Cys191 on gasdermin D → blocks pore formation (CP6). Allows IL-1β cleavage but prevents pyroptosis and cell rupture.

**Evidence level:** Established (Nature Immunology 2020; works at nanomolar concentrations in humans)

**Population context:** Broad applicability for GSDMD mechanism, but **the absolute alcohol contraindication is the dominant population filter**. Patients who consume alcohol in any form (including some mouthwashes, OTC cold preparations, kombucha, or fermented foods with residual ethanol) cannot use disulfiram safely. Patients with hepatic dysfunction: dose-reduced or contraindicated. Pregnancy: contraindicated. Older adults: increased CNS side effects.

**Dosing range:** 250 mg once daily (standard for alcohol use disorder; off-label for gout)

**Key advantage:** FDA-approved for 70+ years, well-tolerated in alcohol-abstinent patients, ~$30/month

**Contraindications:** **Any alcohol use** (acute disulfiram-ethanol reaction: flushing, tachycardia, hypotension, severe nausea — can be fatal at high alcohol doses). Active hepatic disease (LFTs >3× upper limit of normal). Severe coronary artery disease (cardiovascular collapse risk on ethanol exposure). Severe psychosis (case reports of psychotic exacerbation). Pregnancy. Concurrent metronidazole or other disulfiram-like agents.

**Drug interactions:**
- **Metronidazole, tinidazole, cefoperazone, griseofulvin, certain MAOIs, isoniazid:** disulfiram-like reactions amplified.
- **Warfarin:** disulfiram inhibits warfarin metabolism → increased anticoagulation; INR monitoring required.
- **Phenytoin:** disulfiram inhibits phenytoin metabolism → toxicity risk.
- **Theophylline, caffeine (high-dose):** disulfiram inhibits clearance; toxicity risk.
- **Benzodiazepines metabolized by CYP3A4 (alprazolam, midazolam):** disulfiram inhibits clearance; sedation risk.
- **Acetaminophen at high doses:** competing hepatic stress (additive hepatotoxicity).
- **Many ethanol-containing medications (some elixirs, sublingual sprays, IV preparations):** trigger reaction.

**Dose-dependent risk profile:**
- 250 mg/day (standard): well-tolerated in alcohol-abstinent patients. Hepatotoxicity (idiosyncratic) is the main rare serious side effect; baseline + periodic LFTs recommended.
- 500 mg/day (historical dose, less common now): more side effects (drowsiness, peripheral neuropathy, hepatic stress) without proportional efficacy gain.
- Disulfiram-ethanol reaction severity scales with both disulfiram dose and ethanol exposure.

**Medical requirement:** Requires physician discussion. Can frame as off-label GSDMD inhibitor for gout flare prevention, or as standard-of-care for any alcohol use history.

**Practical note:** This is the single most accessible pharma-grade NLRP3 pathway exploit in the entire supplement arsenal. (Source: nlrp3-exploit-map.md)

**Stack interactions (within this catalog):**
- **Mechanism orthogonality (CP6):** distinct CP from any other stack compound — covers pyroptosis pore-formation specifically.
- **Hepatotoxicity stacking concern with EGCG, high-dose curcumin, acetaminophen:** all four contribute to hepatic stress; layering is a relative contraindication.
- **Caution with fermented foods:** kombucha and some koji preparations may contain residual ethanol that could trigger reaction in disulfiram-sensitive patients. Practical limit: dietary intake of well-fermented foods at typical portion sizes is generally below the threshold but is patient-specific.
- **No ABCG2 interaction documented.**

**Cost:** ~$30/month

---

### Tranilast

**Category:** Approved Drug (Japan/Korea) / NLRP3 Inhibitor

**Mechanism:** Direct NACHT domain binder; blocks NLRP3 oligomerization via different mode than MCC950/oridonin

**Evidence level:** Established (EMBO Molecular Medicine: "remarkable preventive or therapeutic effects" on gouty arthritis, CAPS, type 2 diabetes)

**Population context:** Broad applicability for NLRP3 mechanism. Approved in Japan (Rizaben) and South Korea since 1982; not FDA-approved in US. International sourcing introduces supply-quality variability. Pregnancy: insufficient data for off-label indication.

**Dosing range:** 300–600 mg/day

**Access:** Approved in Japan (Rizaben) and South Korea since 1982; not FDA-approved in US but available through:
- International pharmacies
- Informed physician compassionate use
- Clinical trial if enrolled (unlikely for gout specifically)

**Safety profile:** Up to 600 mg/day used clinically for months without hepatotoxicity (unlike MCC950)

**Contraindications:** Pregnancy (insufficient gout-indication data, though approved in pregnancy for keloid prevention in Japan with documented safety). Severe hepatic or renal disease.

**Drug interactions:**
- **Warfarin:** modest interaction reported in Japanese post-marketing data; INR monitoring at initiation.
- **Loop diuretics:** mild renal interaction at high tranilast doses.
- **No major CYP-mediated clinical interactions documented at standard doses.**

**Dose-dependent risk profile:**
- 300–600 mg/day: well-tolerated chronically (decades of post-marketing data).
- Higher doses (>600 mg/day): rare bladder symptoms, hepatic enzyme elevation; not the gout-relevant range.

**Medical requirement:** Requires physician discussion; insurance unlikely to cover off-label, may be out-of-pocket

**Stack interactions (within this catalog):**
- **Mechanism orthogonality (CP2 NACHT):** distinct binding mode from oridonin (Cys279); could be additive.
- **No ABCG2 interaction documented.**

**Cost:** $50–100/month (international shipping)

---

### Fermented Foods (Spermidine & Trehalose Boost)

**Category:** Dietary

**Mechanism:**
- Spermidine induces autophagy (CP2/CP3 target); direct NLRP3 suppression
- Trehalose activates TFEB → autophagy via mTOR-independent pathway
- Both compounds suppress NLRP3 accumulation

**Evidence level:** Established

**Population context:** Broad applicability with diet-specific considerations. Histamine-intolerant patients: aged cheese, natto, kimchi, kombucha all carry significant histamine load; may not tolerate. Disulfiram users: kombucha and koji-fermented foods may carry residual ethanol triggering reaction. SIBO patients: fermented foods with live cultures may transiently worsen symptoms before improving.

**Foods:**
- **Spermidine-rich:** Aged cheese (Parmesan, cheddar), natto (fermented soy), mushrooms, wheat germ
- **Trehalose-rich:** Mushrooms, honey, shrimp

**Dosing range:**
- Spermidine supplement: 1–6 mg/day, but food sources preferred
- Natto: 1–2 servings/week provides ~70 nmol/g (one of richest sources)
- Trehalose: 5–10g/day in water or added to beverages

**Contraindications:** Histamine intolerance (aged/fermented foods). Disulfiram therapy (residual ethanol concern in kombucha specifically). Severe immunocompromise (live-culture fermented foods may carry small infection risk).

**Drug interactions:**
- **Warfarin:** natto is exceptionally high in vitamin K2 — directly antagonizes warfarin and requires either consistent intake with INR adjustment, or avoidance.
- **MAOIs:** aged cheese and some fermented foods carry tyramine load; hypertensive crisis risk with MAOIs.
- **Disulfiram:** see above (residual ethanol).

**Dose-dependent risk profile:**
- Dietary fermented foods at normal portion sizes: well-tolerated.
- High-dose spermidine supplements (>6 mg/day): under-characterized; some animal data suggests longevity benefits but human data is thin.
- Trehalose >20g/day: GI upset (osmotic).

**Stack interactions (within this catalog):**
- **Synergy with intermittent fasting (autophagy axis):** both push TFEB/autophagy — additive.
- **Synergy with omega-3 (resolution-phase):** SPMs + autophagy = clearance and resolution.
- **Soy-derived fermented foods (miso, natto, tempeh) carry genistein and daidzein** — small but measurable amounts of ABCG2-functional inhibitors at high consumption (see Stack-level contradictions).
- **No major direct ABCG2 interaction at dietary doses.**

**Practical note:** Fermentation naturally produces these compounds. Eating traditional fermented foods (miso, soy sauce, kimchi, kombucha) provides dual benefits: living probiotics + NLRP3-suppressing metabolites. (Source: nlrp3-exploit-map.md)

**Koji fermentation note:** Home-made shio-koji and amazake (from wild-type *A. oryzae*) are practical fermented-food additions that also deliver digestive enzymes (amylase, protease, lipase). For the complete small-batch home protocol (koji-kin → koji rice → shio-koji / amazake), see [Koji Home Fermentation](./koji-home-fermentation.md). Yellow koji (*A. oryzae*) is the recommended strain for digestive-enzyme home use. (Mechanistic Extrapolation; source: koji-home-fermentation.md)

**ABCG2 induction via fermentable fiber (source: abcg2-modulators.md):** Fermentable fiber (resistant starch, inulin, GOS, beta-glucan) → colonic SCFA production → butyrate → PPARγ activation in enterocytes → ABCG2 transcriptional induction. Li et al. 2023 (*Biomedicine & Pharmacotherapy*, PMID 36948133) demonstrated that sodium butyrate in a hyperuricemic mouse model decreased serum UA AND restored intestinal ABCG2 expression. (Animal Model; source: abcg2-modulators.md) For Q141K-positive gout patients (~30–50% of the gout population), butyrate also rescues the Q141K variant's trafficking defect via HDAC inhibition — a separate, additive mechanism. DASH diet clinical data: 0.25 mg/dL mean UA reduction (0.73 mg/dL in patients with baseline UA ≥8 mg/dL) attributable to the fiber/ABCG2 axis (Juraschek et al. 2021, *Arthritis & Rheumatology*, PMID 33615722; Clinical Trial). Aim ≥25–30 g fermentable fiber/day for meaningful ABCG2 induction.

**Cost:** Negligible to modest ($5–10/week for specialty fermented products)

---

### Discussion with Doctor: Disulfiram or Tranilast

**Timeline:** Schedule rheumatology or primary care visit in next 2–4 weeks

**Talking points:**
1. You're interested in exploring GSDMD pathway inhibition for gout flare prevention
2. Disulfiram is a 70-year safety record, FDA-approved drug with specific GSDMD-blocking activity
3. Tranilast is approved in Asia with clinical data in gout; worth exploring if willing to use international pharmacy
4. Neither is standard-of-care but both have mechanism-based rationale and published clinical efficacy in gout

**What to expect:** Many rheumatologists will be unfamiliar with these mechanisms but may be willing to discuss as off-label options, especially if you share the published papers.

---

## Section 3: FUTURE (Dependent on Engineered Strains)

These become available as Open Enzyme [[engineered-yeast-uricase]] and [[engineered-koji-protocol]] strains are validated and deployed.

### Engineered Yeast (S. cerevisiae or S. boulardii) — Uricase

**Category:** Living Therapeutic / Engineered Probiotic

**Mechanism:** Expresses uricase in gut lumen; degrades uric acid in place, creating a concentration sink that pulls systemic uric acid into intestine for degradation (Source: [[engineering-yeast-uricase-proposal]], [[open-enzyme-vision]])

**Population context:** Designed for under-excreter gout patients (~90% of gout population). **Particularly relevant for patients with androgen-suppressed ABCG2** (TRT, SERM, AAS users) and Q141K-positive carriers — the populations where the gut-lumen-sink works hardest. Pre-clinical only; population stratification will be empirically refined in Phase 2 animal and Phase 3 human work.

**Dosing range:** TBD from Phase 2 animal studies; likely 10–20g dried yeast powder daily or equivalent live cells

**Format:**
- Dried/lyophilized powder in capsules
- Fermented beverage (kvass, water kefir, kombucha-style with engineered yeast)
- Nutritional yeast sprinkled on food

**Contraindications:** TBD. Anticipated: severe immunocompromise (live probiotic risk), prior reaction to S. cerevisiae or S. boulardii (rare), active gut barrier disease (theoretical translocation risk for live probiotics). Pregnancy: no data; live engineered probiotic in pregnancy will require dedicated safety work.

**Drug interactions:** TBD. Anticipated minimal small-molecule pharmacokinetic interactions; functional interactions with the gut-lumen-sink axis are the relevant question (see Stack-level contradictions).

**Dose-dependent risk profile:** TBD from validation experiments.

**Stack interactions (within this catalog):**
- **Antagonism by ABCG2 inhibitors in stack:** curcumin, quercetin, EGCG, genistein at supplement-relevant doses functionally inhibit ABCG2 — the transporter the engineered uricase depends on for its mechanism. **The platform thesis is pharmacologically antagonized by these compounds in androgen-dominant or Q141K-positive readers.** See Stack-level contradictions section.
- **Synergy with butyrate / fermentable fiber, sulforaphane, indole-3-carbinol:** all induce ABCG2 (Tier 1 inducers per [abcg2-modulators.md](./abcg2-modulators.md)) — open the gate on which the platform depends. Strong recommended pairing.
- **Synergy with carnosine:** carnosine modulates URAT1/GLUT9 (renal); engineered uricase modulates gut UA pool — orthogonal additive.

**Timeline to availability:** Phase 1 in vitro validation (weeks 1–10), Phase 2 animal studies (weeks 12–24), Phase 3 self-experimentation (weeks 24+). Earliest realistic availability: late 2026.

**Expected benefit:** 15–30% reduction in serum uric acid; potential for eliminating need for allopurinol or febuxostat in responders

**Cost:** TBD (target: cost-of-fermentation pricing)

---

### Engineered Koji (A. oryzae) — Dual-Enzyme (Digestive + Uricase)

**Category:** Living Therapeutic / Engineered Food Organism

**Mechanism:**
- Native koji enzymes: lipase, acid-stable protease, amylase (digestive enzyme support for Lynn)
- Engineered addition: A. flavus uricase (uric acid degradation for Brian)
- Grown on rice, consumed as fermented food (e.g., amazake, koji rice)

**Population context:** Designed for dual-target use (gout under-excreter + EPI-pattern digestive insufficiency). Population-context particulars TBD from Phase 2/3 work.

**Dosing range:** TBD; likely 10–20g koji per day (equivalent to ~1 cup koji rice)

**Format:**
- Fresh koji grown on rice (traditional fermentation)
- Dried koji powder
- Koji amazake (sweet rice beverage)
- Koji in soup or side dishes

**Contraindications:** TBD. Aspergillus allergy (rare but documented for occupational exposures). Severe immunocompromise (live probiotic concern). Pregnancy: no engineered-strain data; wild-type koji is GRAS at any dietary level.

**Drug interactions:** TBD. Wild-type koji digestive enzymes may interact with certain pharmaceutical preparations (acid-stable protease + protein-bound drugs); functional rather than pharmacokinetic.

**Dose-dependent risk profile:** TBD.

**Stack interactions (within this catalog):**
- **Same ABCG2 antagonism / synergy pattern as engineered yeast.** See Stack-level contradictions.
- **Resistant-starch substrate (rice) provides incidental fermentable fiber → colonic butyrate → PPARγ-mediated ABCG2 induction.** Substrate selection for the engineered koji platform may be tunable for incremental SCFA yield. (Mechanistic Extrapolation; see [abcg2-modulators.md](./abcg2-modulators.md) §"Engineering implications.")

**Timeline to availability:** Phase 1 koji optimization (weeks 4–10), Phase 2 EPI model (weeks 12–18), Phase 3 human trial (weeks 20–32+). Earliest: Q2 2026 for validation, Q3–Q4 2026 for deployment.

**Expected benefit:**
- Brian: 15–30% reduction serum uric acid, potential 50% reduction flare frequency
- Lynn: Improved fat absorption, normalized GI symptoms, reduced inflammatory markers

**Cost:** TBD

---

## Reference daily pattern (NOT a recommendation)

> **Framing note (2026-04-25 catalog refactor):** The block below is **one possible scheduling pattern, kept for reference**, not a recommended daily protocol. It survived from a pre-catalog version of this page and is preserved because the dose-timing logic (fat-soluble with meals, peptide on rising, fiber away from minerals, etc.) is reusable. **Do not read this as "the Open Enzyme stack."** Compound selection should always be filtered by individual contraindications, drug interactions, and the Stack-level contradictions section below.

**Morning (with breakfast):**
- Vitamin D3 (5,000–10,000 IU) + K2 (200 mcg) — with fat
- Sulforaphane supplement (50 mg) OR raw broccoli sprouts (100g)
- Quercetin phytosome (500 mg)
- Omega-3 (high-DHA preferred for gout; 2g EPA+DHA) — with food
- NAC (600 mg) — optional, can take on empty stomach if prefer
- KPV nasal spray (200–300 mcg) — before breakfast

**Midday:**
- Oridonin (50 mg) — with lunch
- Exogenous BHB or MCT oil if not doing ketogenic diet (10–15g)

**Evening (with dinner):**
- Omega-3 (2g EPA+DHA) — second dose
- Cherry extract (8 oz juice concentrate or equivalent)
- NAC (600 mg) — if split dosing

**Intermittent Fasting Window:**
- Minimum 16:8 daily
- One 24-hour fast weekly or biweekly (if tolerated; skip during active flares)

**Optional/As Tolerated:**
- Fermented foods daily: natto, aged cheese, miso, kimchi, kombucha
- Trehalose (5–10g) mixed into coffee or tea

**PRN (As Needed During Prodrome of Flare):**
- Disulfiram (250 mg daily × 7–14 days) — if flare symptoms appear
- Consider BPC-157 IM injection or intensify nasal spray dosing

---

## Evidence Level Summary

| Compound | Evidence Level | Chokepoints Hit | Mechanism | Cost/Month |
|----------|---|---|---|---|
| BHB/Ketones | Established | CP1, CP2, CP3 | Direct NLRP3 inhibition | $0–40 |
| Intermittent Fasting | Established | CP1, CP2, CP3 | AMPK/mTOR/autophagy | Free |
| KPV peptide | Supported | CP1 | NF-κB stabilization | $100–200 |
| BPC-157 | Established | CP1 (tissue repair) | Cytoprotection, NO modulation | Existing |
| Sulforaphane | Established | CP1, CP2 | Nrf2/NF-κB crosstalk; **ABCG2 inducer (gut-sink synergy)** | $5–30 |
| Oridonin | Established | CP1, CP2 | NLRP3 covalent inhibitor (5.18 μM human IC50) | $30–60 |
| Omega-3 (DHA-emphasis) | Animal Model (gout SPMs) | CP1, CP5a, CP5b | SPM precursors; RvD1/MaR1 direct gout evidence | $30–50 |
| Cherry extract | Supported | CP1 (XO inhibition) | Anthocyanins | $20–30 |
| NAC | Established | CP2 | Glutathione replenishment | $10–15 |
| Quercetin (Phytosome) | Established | **CP6a (5-LOX 300 nM, primary)**, CP1, XO | 5-LOX/LTB4 + NF-κB + XO; **functional ABCG2 inhibitor (stack contradiction)** | $15–25 |
| **EGCG** (green tea) | Animal Model (MSU mouse, Lee 2019) | CP1, CP1a (TNFSF14), CP4, CP5a | Widest-spectrum natural compound; 4 of 7 chokepoints; hepatotox ceiling; **functional ABCG2 inhibitor (stack contradiction; in vivo unresolved)** | $15–25 |
| **Limonene** (d-limonene) | Animal Model (MSU rat, Venkatesan 2025) | CP1, CP2 | Nrf2 + TLR4 suppression | $15–25 |
| **Lactoferrin** (bovine) | Animal + Clinical Ph3 (talactoferrin) | CP5 | NLRP3/caspase-1/GSDMD axis; fills canakinumab gap | $30–60 |
| **Carnosine** (L-carnosine) | Animal Model (HUA rat) | CP1, CP2, +urate | Dual UA + NLRP3 (unique in stack); androgen-axis aligned | $20–35 |
| Beta-caryophyllene | Animal Model (MSU gout) | CP1, CP2 | CB2 agonism / TLR4 / NLRP3 | $15–30 |
| Vitamin D3 + K2 | Established | CP1 | VDR activation | $10–15 |
| Disulfiram | Established | CP6b | GSDMD pore blockade | ~$30 |
| Tranilast | Established | CP2 | NACHT domain binding | $50–100 |
| Fermented foods | Established | CP2, CP3 | Spermidine/trehalose; **soy-fermented = trace genistein (mild ABCG2 functional inhibitor at supplement-level intakes only)** | $5–10 |
| **Engineered Yeast** | *Validated Ph2* | Upstream (uric acid) | Direct degradation; **depends on ABCG2 — stack contradictions apply** | *TBD 2026* |
| **Engineered Koji** | *Validated Ph2* | Upstream + Digestive | Dual enzyme; **depends on ABCG2 — stack contradictions apply** | *TBD 2026* |

---

## Stack-level interactions

The per-compound entries above flag interactions one compound at a time. This section consolidates the patterns that emerge when multiple compounds are stacked — particularly the cases where the catalog as a whole pulls in opposing directions on a shared mechanism.

### 1. Stack-level contradictions: ABCG2-axis antagonism of the platform thesis

The engineered-uricase platform's [gut-lumen-sink](./gut-lumen-sink.md) mechanism depends on intestinal ABCG2 to actively secrete urate from blood into gut lumen, where the engineered uricase degrades it. **Several compounds in this catalog at typical supplement doses are functional inhibitors of ABCG2** — they pharmacologically antagonize the platform thesis, particularly in male / androgen-dominant / Q141K-positive readers (the dominant gout demographic).

Detailed mechanism, primary citations, and tissue-selectivity discussion in [`abcg2-modulators.md`](./abcg2-modulators.md). Summary table:

| Compound | ABCG2 effect | Evidence | Net effect on gut sink | Stack flag |
|---|---|---|---|---|
| **Curcumin** | Functional BCRP/ABCG2 inhibitor in vitro (Ki ~5–10 μM) | Established in vitro pharmacology (multiple labs) | Likely negative acutely at 500–1000 mg supplement doses (gut concentrations easily reach Ki) | **Antagonist** |
| **Quercetin** | Substrate/inhibitor at low μM (functional inhibition); transcriptional ABCG2 upregulation reported in chronic-dosing animal studies (mixed) | In vitro + Animal Model (mixed direction by chronicity) | Probably negative acutely; chronic effect unresolved | **Antagonist (acute)** |
| **EGCG** | Functional BCRP inhibitor in pharmacology assays. Yu 2024 (PMID 38757391) showed mouse PO-induced hyperuricemic model net-favorable effect on ABCG2/URAT1/GLUT9 expression in vivo — direction opposite to in vitro inhibition | Pharmacology in vitro vs. Animal Model in vivo (contradicts) | **Unresolved** — net clinical effect on gut sink in androgen-dominant patients pending direct measurement | **Antagonist (in vitro), Synergist (some animal in vivo)** |
| **Genistein / soy isoflavones** | Established BCRP substrate-inhibitor | Pharmacology literature | Dietary intake from natto/miso/tempeh: clinically negligible. Supplement-grade isoflavone capsules: meaningful inhibition at 50–100 mg/day | **Antagonist (supplement-grade only; food-level fine)** |

> **Note:** Curcumin is not currently a separate entry in this catalog — it's flagged here because it is the prototypical functional ABCG2 inhibitor in this class, and is frequently stacked alongside the catalog compounds in real gout-supplement use. If curcumin is added in the future, it carries the same stack-contradiction flag as quercetin.

**Risk-tier stratification** (added 2026-04-27 per synthesis Pass 3 review — "blanket warnings undermine compliance when the actual risk is genotype/dose-dependent"):

| User profile | ABCG2 status | Risk tier | Practical implication |
|---|---|---|---|
| Q141K homozygote + androgen-suppressed (TRT / SERM / AAS) + high-dose flavonoid (>500 mg quercetin OR >600 mg EGCG OR >500 mg curcumin) | Triple-hit suppressed | **Highest concern** | Gut sink may be functionally closed during dose window. Pause inhibitor flavonoids until ABCG2-axis status is established; favor inducers (sulforaphane, fermentable fiber → butyrate per [abcg2-modulators.md](./abcg2-modulators.md) §6). |
| Q141K heterozygote OR androgen-dominant (high-T, no SERM) + supplement-grade flavonoid | One axis suppressed + acute pharmacological inhibition | **High concern** | Meaningful gut-sink narrowing during the dose window. Time inhibitor flavonoids away from urate spikes (post-fructose meals, peri-flare). Acceptable with UA monitoring. |
| Wild-type ABCG2 + supplement-grade flavonoid | Pharmacological inhibition only | **Moderate concern** | Net effect is dose- and chronicity-dependent. Watch UA trajectory after introduction; discontinue or down-titrate if UA rises. |
| Any genotype + dietary-level flavonoid (onions, tea, turmeric, fermented soy at normal food portions) | Sub-Ki gut concentrations | **Minimal concern** | No restriction. Food-level intake is unlikely to be clinically significant for the gut sink. |

Stratification matters because a blanket "avoid quercetin" message undermines compliance for the largest cohort (wild-type genotype, dietary intake) where the risk is essentially zero. The clinically meaningful signal concentrates in androgen-suppressed Q141K-positive readers at supplement-grade doses.

**Practical inference for high-T or Q141K-positive readers:** avoid high-dose curcumin and quercetin acutely when the gut sink matters most (post-meal urate spikes, fructose challenges, peri-flare). Dietary-level intake (turmeric in food, onions, tea, fermented soy at normal portions) is unlikely to be clinically problematic; supplement-grade doses are the concern.

**Counter-balancing inducers in the catalog (Tier 1 ABCG2 inducers per [abcg2-modulators.md](./abcg2-modulators.md)):**
- **Sulforaphane** (Nrf2 axis) — gut-enriched
- **Fermentable-fiber-derived butyrate** (PPARγ axis; not a discrete catalog entry, but fermented-foods + dietary fiber adjacent) — strongest evidence (Juraschek DASH 2021, Li 2023)
- **Indole-3-carbinol / DIM, AhR-active probiotic strains** — gut-enriched (not currently discrete catalog entries; flagged as adjacent)

A reader most concerned about the gut-lumen-sink (e.g., on TRT or known Q141K-positive) should preferentially weight inducers over inhibitors when considering catalog entries.

### 2. Stack-level synergies and redundancies

These are cases where multiple catalog compounds converge on the same mechanism — additive at low fractional saturation, redundant at high fractional saturation.

**Nrf2 activator cluster (sulforaphane + quercetin + oridonin + limonene + omega-3 metabolites):** all five drive Nrf2 transcriptional activation. At individual supplement doses each is sub-saturating; layering produces cumulative effect with diminishing returns. Combining all five is redundant beyond a certain ceiling — pick 2–3 for the Nrf2 axis rather than every one.

**NF-κB priming block cluster (KPV + sulforaphane + EGCG + quercetin + carnosine + curcumin (if added)):** all six suppress NF-κB priming via different molecular routes. Mechanism-orthogonal at the molecular level (peptide/IκB-α stabilization vs. proteasome inhibition vs. transcriptional vs. ROS-dependent), so additive at the pathway level. Again, diminishing returns past 3–4 stacked.

**XO inhibition cluster (cherry + quercetin + EGCG):** all three modestly inhibit xanthine oxidase. Additive on UA production; layering with allopurinol or febuxostat may exceed XO-suppression target.

**CP2 NLRP3-assembly orthogonality (oridonin + BCP + tranilast + dapansutrile (if available) + BHB):** distinct molecular touch-points (Cys279 covalent / CB2-TLR4 / NACHT direct / NACHT direct / K+ efflux). Genuinely additive; not a redundancy cluster.

**SPM resolution + peptide cytoprotection (omega-3 DHA-emphasis + KPV + BPC-157):** complementary at the resolution phase (CP5). Resolution-phase mechanism (efferocytosis, M1→M2 switch) is undersupplied in most stack designs — this triad is one of the genuine non-redundant synergies.

**Autophagy axis (intermittent fasting + spermidine/trehalose from fermented foods):** mechanism-aligned (TFEB / mTOR-independent autophagy). Additive within the same axis.

### 3. Stack-level safety amplifications

Cases where multiple catalog compounds compound a single safety risk.

**Hepatotoxicity stacking (EGCG + acetaminophen + alcohol + disulfiram + high-dose curcumin if added):** all converge on hepatic stress. The 86 nM 20S proteasome IC50 of EGCG sets a hepatotoxicity dose ceiling at ~800 mg/day; layering with any other hepatotoxic input shifts the ceiling lower. Periodic ALT/AST monitoring is conservative for any reader running EGCG + a second hepatotoxic input chronically.

**Bleeding risk stacking (omega-3 ≥3g/day + EGCG + quercetin + warfarin / DOACs / antiplatelets):** the polyphenol cluster has modest antiplatelet effects that aggregate with omega-3's platelet inhibition. INR shifts (on warfarin) are documented for omega-3 alone; adding EGCG and quercetin is additive. Practical: at the upper end of stack doses, surgical / dental procedures should trigger a 7–14 day hold on the polyphenol + omega-3 layer.

**CYP3A4 inhibition stacking (quercetin + EGCG + oridonin + d-limonene at chronic doses):** all four show in vitro CYP3A4 inhibition at gut-relevant concentrations. Simvastatin, tacrolimus, cyclosporine, calcium channel blockers, and direct oral anticoagulants are the highest-leverage drug classes affected. A reader on any narrow-therapeutic-index CYP3A4 substrate should avoid layering 3+ of these compounds chronically without therapeutic drug monitoring.

**Disulfiram-ethanol amplification (disulfiram + kombucha / koji-fermented foods + alcohol-containing OTC preparations):** any residual ethanol input can trigger disulfiram-ethanol reaction. Practical: disulfiram users should avoid kombucha entirely and treat any koji-derived fermented foods as a per-batch ethanol-content question.

**Vitamin K2 + warfarin (already flagged at compound level):** worth re-flagging at the stack level because **natto (fermented foods entry)** is one of the highest natural K2 sources known. Warfarin patients eating natto plus taking K2 supplements compound the warfarin antagonism.

**Hypercalcemia stacking (D3 + K2 + thiazide diuretic):** D3 increases calcium absorption; thiazides reduce renal calcium excretion. K2 directs calcium to bone but does not negate the absorption × retention compounding. Patients on thiazides at high D3 supplemental doses should monitor serum calcium.

---

## Practical Implementation

(Implementation discussion below remains catalog-level — i.e., "if a reader were to consider these compounds, here's a rough sequencing logic." It is not a recommended protocol; see the "Reference daily pattern" framing above.)

**Week 1 (low-friction entry):**
- Begin BHB/ketones (dietary or supplement)
- Start intermittent fasting (16:8 minimum)
- Add sulforaphane + quercetin (both are safe, rapid onset); note quercetin's ABCG2-functional-inhibitor flag for androgen-dominant readers
- Continue BPC-157 nasal spray (already in use)

**Week 2–3:**
- Add KPV nasal spray (order from supplier)
- Add omega-3 (DHA-emphasis) and NAC
- Add cherry extract
- Add oridonin (order from Chinese herb supplier or research chemical)
- Begin raw broccoli sprout protocol (if not using supplement form)

**Week 4+:**
- Introduce vitamin D3 + K2 (warfarin-incompatible without monitoring)
- Consider fermented foods (natto 1–2×/week minimum, with same warfarin flag)
- Schedule physician visit to discuss disulfiram/tranilast if appropriate

**Ongoing:**
- Track serum uric acid monthly (initially), then every 3 months
- Monitor flare frequency/severity in journal
- Re-read Stack-level contradictions section before adding curcumin or high-dose isoflavones
- Periodic ALT/AST monitoring for any reader running EGCG ≥600 mg/day chronically

---

*This catalog is a living document. Update as [[validation-experiments]] (Phase 2 & 3) generate new data. Individual compounds may be emphasized or de-emphasized based on personal context, tolerability, and efficacy.*

*Not medical advice. All use should be supervised by a physician.*
