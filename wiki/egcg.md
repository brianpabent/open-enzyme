---
title: "EGCG (Epigallocatechin Gallate)"
date: 2026-04-24
tags: [egcg, green-tea, catechin, proteasome, nlrp3, nfkb, tnfsf14, cp1, cp1a, cp4, cp5a, supplement-stack]
related:
  - supplements-stack.md
  - nlrp3-exploit-map.md
  - nlrp3-inhibitor-screen.md
  - chembl-cross-check.md
  - tnfsf14-gout-target.md
  - gout-deep-dive.md
  - theaflavins.md
sources:
  - nlrp3-inhibitor-screen.md
  - chembl-cross-check.md
  - "Nam et al. *Bioorg Med Chem* 2001 / confirmed *Bioorg Med Chem* 2010 — 20S proteasome IC50 = 86 nM, ChEMBL assay CHEMBL4433382 (pChEMBL 7.07)"
  - "Lee et al. *Molecules* 2019;24(11):2138 (PMID 31174271) — EGCG blocks MSU-induced NLRP3 in mouse macrophages + foot inflammation"
  - "Hosokawa et al. *Mol Nutr Food Res* 2010;54 Suppl 2:S151–8 (PMID 20461739) — EGCG suppresses TNFSF14-induced IL-6 and downregulates HVEM"
  - "Yu et al. *Food Funct* 2024;15(11):5962–5975 (PMID 38757391) — EGCG lowers serum UA in hyperuricemic mice via gut microbiota + urate transporters"
  - "Chen & Xu *Eur Rev Med Pharmacol Sci* 2018;22(21):7458–7464 (PMID 30468495) — EGCG protects renal fibroblasts from UA injury via miR-9/NF-κB/JAK-STAT"
  - "EFSA NDA Panel. Scientific opinion on the safety of green tea catechins. *EFSA Journal* 2018;16(4):e05239"
---

# EGCG (Epigallocatechin Gallate)

EGCG = (−)-epigallocatechin-3-gallate (ChEMBL ID CHEMBL297453). This dossier unifies four separately-catalogued chokepoint effects through a single upstream mechanism — **20S proteasome inhibition → IκBα stabilization → NF-κB blockade** — that was not visible in the wiki until the 2026-04-24 ChEMBL cross-check surfaced the sub-100 nM human proteasome IC50 (source: [chembl-cross-check.md](./chembl-cross-check.md)).

See also the stack-level entry in [supplements-stack.md](./supplements-stack.md) and the chokepoint map in [nlrp3-exploit-map.md](./nlrp3-exploit-map.md).

---

## What it is

- **Chemistry:** Flavan-3-ol (catechin) with a gallate ester at the C3 position. Three phenolic rings, eight free hydroxyl groups — the highest hydroxyl density of any major dietary polyphenol. The gallate group is what drives proteasome chymotrypsin-site binding; non-gallated catechins (EC, EGC) are 10–100× weaker at the same target.
- **Source:** The dominant flavan-3-ol in *Camellia sinensis* (green tea); ~50–60% of total green tea catechins by mass. Matcha and white tea concentrate EGCG further; fully oxidized teas (black, pu'er) convert much of the EGCG into theaflavins and thearubigins.
- **Not producible in engineered yeast or koji at practical titers** — see [Engineered-production angle](#engineered-production-angle) below. EGCG is a dietary / supplement compound, not an Open Enzyme production target.

---

## Unifying mechanism: proteasome → IκBα → NF-κB

The four chokepoint effects the wiki currently attributes to EGCG (CP1 NF-κB priming block, CP1a TNFSF14 suppression, CP4 caspase-1 suppression, CP5a IL-1β-receptor-downstream block) are not four separate mechanisms. They are downstream consequences of a single upstream block at the **20S proteasome chymotrypsin-like site**.

**Step by step:**

1. **EGCG inhibits the 20S proteasome chymotrypsin-like activity at IC50 = 86 nM** in human cells (In Vitro; *Bioorg Med Chem* 2010, confirmed *Eur J Med Chem* 2019, ChEMBL assay CHEMBL4433382, pChEMBL 7.07; source: [chembl-cross-check.md](./chembl-cross-check.md)). This is EGCG's single most potent human target in the curated ChEMBL v34 database outside the *Plasmodium* anti-malarial activity (ENR Ki = 8 nM, not human-relevant).
2. **The 26S proteasome (which contains the 20S core) is the sole enzymatic route for IκBα degradation.** Canonical NF-κB activation requires IKK to phosphorylate IκBα at Ser32/Ser36 → SCF^βTrCP ubiquitin ligase polyubiquitinates phospho-IκBα → 26S proteasome degrades IκBα → NF-κB heterodimers (p50/p65) are released into the cytoplasm.
3. **With the proteasome chymotrypsin site inhibited, polyubiquitinated IκBα accumulates instead of being degraded.** Accumulated IκBα continues to sequester NF-κB in the cytoplasm regardless of how much upstream IKK activity is present.
4. **No nuclear NF-κB → no transcription of pro-IL-1β, NLRP3, TNFSF14, COX2, or the other NF-κB-dependent priming genes.** This is CP1 blockade at a layer upstream of where the wiki previously located it.
5. **The previously-cited "IKK inhibition" framing is mechanistically downstream or redundant.** IKK's only output in this pathway is to phosphorylate IκBα to tag it for proteasomal destruction. If the proteasome cannot destroy IκBα, IKK activity is decoupled from NF-κB release. The IKK-inhibition literature for EGCG (most of which is functional, not direct-binding) is better read as **the cellular consequence of proteasome inhibition**, not as an independent mechanism. (Mechanistic Extrapolation; see [Open questions](#open-questions) for what an IKK vs. proteasome dose-response experiment would look like.)

**Why this reframe matters:** A compound that hits four chokepoints through pleiotropy is hard to validate and hard to dose. A compound that hits four chokepoints through one coherent upstream mechanism is falsifiable — the dose-response curves at CP1, CP1a, CP4, and CP5a should all track the proteasome IC50, and a Western for IκBα stabilization is a direct mechanistic readout. See [validation-experiments.md §1.7](./validation-experiments.md) for the priority THP-1 MSU macrophage assay that tests this.

---

## Chokepoint coverage (4 of 7)

| Chokepoint | Mechanism (unified through proteasome axis) | Evidence | Primary source |
|------------|---------------------------------------------|----------|----------------|
| **CP1** (NF-κB priming) | 20S proteasome IC50 = 86 nM → IκBα stabilization → NF-κB cytoplasmic retention → no pro-IL-1β / NLRP3 transcription | In Vitro (human proteasome, curated ChEMBL) | ChEMBL CHEMBL297453; *Bioorg Med Chem* 2010; *Eur J Med Chem* 2019 |
| **CP1a** (TNFSF14 amplifier) | Suppresses TNFSF14-induced IL-6 in human gingival fibroblasts; **downregulates HVEM** (TNFSF14 receptor) on target cells. This is a direct receptor-level effect beyond the NF-κB-blockade story. The only compound in the Open Enzyme stack with curated direct TNFSF14 data. | In Vitro (human HGF) | Hosokawa 2010 (PMID 20461739); see [tnfsf14-gout-target.md](./tnfsf14-gout-target.md) |
| **CP4** (caspase-1) | Pro-caspase-1 transcription is NF-κB-dependent → proteasome block prevents caspase-1 induction. Separately: EGCG reduces ROS (glutathione-sparing + direct radical scavenging) which lowers the caspase-1 activation trigger. | In Vitro (mouse macrophages) + Animal Model | Lee 2019 *Molecules* (PMID 31174271) |
| **CP5a** (IL-1β receptor-downstream) | Reduces IL-1β-induced NF-κB signaling in chondrocytes and synoviocytes — same proteasome/IκBα axis, now on the receiving cell side of the IL-1β cytokine signal | In Vitro | multiple (see [nlrp3-inhibitor-screen.md](./nlrp3-inhibitor-screen.md)) |

**Not covered:** CP0 (complement C5a), CP2 (NLRP3 assembly — no direct NACHT-domain binding in ChEMBL), CP3 (ASC speck), CP5b (SPM resolution pathway), CP6a (5-LOX / LTB4), CP6b (GSDMD pore). EGCG's spectrum is wide but located entirely on the priming / transcription side and its immediate receptor-level consequences.

The four-chokepoint coverage is now mechanistically unified, not a pleiotropic list. This is rare in the Open Enzyme stack: most compounds either hit a single chokepoint with high specificity (dapansutrile at CP2, disulfiram at CP6b) or hit multiple chokepoints through genuinely distinct mechanisms (quercetin at CP1 + CP6a + XO).

---

## Gout-specific evidence

Direct gout / hyperuricemia evidence, in descending order of translation strength:

- **Lee et al. 2019 *Molecules* (PMID 31174271).** Primary mouse macrophages + MSU-injected mouse foot model. EGCG blocked MSU-induced caspase-1(p10) cleavage and IL-1β secretion in macrophages; oral EGCG reduced foot swelling in the MSU model; mechanism invoked was mtDNA synthesis block + ROS reduction, feeding into NLRP3 suppression. (**Animal Model + In Vitro**; source: [nlrp3-inhibitor-screen.md](./nlrp3-inhibitor-screen.md))
- **Yu et al. 2024 *Food Funct* (PMID 38757391).** PO (potassium oxonate)-induced hyperuricemic mouse model. EGCG lowered serum uric acid via gut microbiota modulation and urate transporter (URAT1, GLUT9, ABCG2) modulation — the same transporter axis carnosine targets. (**Animal Model**; source: [nlrp3-inhibitor-screen.md](./nlrp3-inhibitor-screen.md)) **Note:** This in vivo favorable ABCG2 effect contrasts with EGCG's established in vitro role as a functional ABCG2/BCRP inhibitor in pharmacology assays. The net effect on the gut urate sink at supplement doses is unresolved — see [abcg2-modulators.md](./abcg2-modulators.md) §Supplements-stack contradiction for the full discussion. (In Vitro inhibition vs. Animal Model in vivo; source: abcg2-modulators.md)
- **Chen & Xu 2018 *Eur Rev Med Pharmacol Sci* (PMID 30468495).** Rat renal fibroblasts exposed to UA injury. EGCG protected cells via the miR-9 / NF-κB / JAK-STAT axis — consistent with the proteasome/NF-κB mechanism above, but at the kidney tissue level where UA-driven fibrosis is the relevant endpoint. (**In Vitro**)

No human RCT data specifically in gout. Human trials exist for hypertension, insulin resistance, and weight management at 400–800 mg EGCG/day doses (reviewed by EFSA 2018); none have gout or serum UA as primary endpoints.

---

## Dose and bioavailability

**Free EGCG in green tea:**
- Brewed green tea: ~50–100 mg EGCG per 200 mL cup (varies 3–5× with brew time, water temperature, leaf grade, and whether the tea is sencha vs. gyokuro vs. matcha).
- Matcha (powdered whole-leaf): ~100–150 mg EGCG per 2 g serving (the highest natural dietary concentration, because the whole leaf is consumed).
- Black tea, oolong, pu'er: substantially lower EGCG (5–30 mg/cup) because oxidation converts catechins into theaflavins and thearubigins.

**Supplements:**
- Standardized green tea extract (typically 40–50% EGCG): 400–800 mg EGCG/day used in most clinical trials (EFSA 2018 safety cap recommendation: 800 mg/day).
- Decaffeinated EGCG extracts remove the confounding caffeine load.

**Bioavailability:**
- Free EGCG oral bioavailability is poor: **~0.1–0.3%** plasma AUC relative to ingested dose, with extensive glucuronidation, methylation, and biliary excretion.
- **Phospholipid-complex formulations (Greenselect Phytosome, etc.)** improve bioavailability to ~5–10% — a 30–50× gain, and the only practical way to reach plasma concentrations near the 86 nM proteasome IC50.
- **Fasted dosing** raises free-EGCG Cmax substantially — which is also what raises hepatotoxicity risk. Food intake blunts Cmax. The safety and efficacy windows trade against each other here; see [safety](#safety--hepatotoxicity-ceiling) below.
- EGCG is a substrate for catechol-O-methyltransferase (COMT) — COMT-inhibitor combinations (quercetin as a mild COMT inhibitor, for instance) can raise free-EGCG exposure, with the same safety caveat.

**Practical protocol for the Open Enzyme stack (cross-ref [supplements-stack.md](./supplements-stack.md)):** 400–600 mg EGCG/day from a standardized extract, taken **with food**, split between morning and early afternoon. Stay below 800 mg/day sustained. Phytosome formulations are preferred for bioavailability at lower total mg; matcha (2–3 servings/day) is a reasonable dietary alternative.

---

## Safety — hepatotoxicity ceiling

The same 86 nM 20S proteasome activity that makes EGCG interesting at CP1 also makes it a **hepatotoxicity liability at high doses**. The clinical literature on proteasome inhibitors is consistent on this point:

- **Bortezomib and carfilzomib** (clinical proteasome inhibitors, multiple myeloma) have documented hepatotoxicity profiles at their therapeutic plasma levels (single-digit nM to low hundred nM for 20S chymotrypsin inhibition). Liver function abnormalities are a monitored adverse event in both drug labels. (Mechanistic Extrapolation to EGCG.)
- **EGCG case reports:** High-dose green tea extract (especially fasted, >800 mg/day sustained) has caused multiple published hepatotoxicity cases, some progressing to acute liver failure. Meta-analysis of RCT safety data supports a dose-dependent ALT/AST elevation signal above 800 mg/day.
- **EFSA Scientific Opinion (2018)** formally recommended a **800 mg EGCG/day safety ceiling for food supplements** based on this hepatotoxicity signal, and noted that fasted dosing raises the risk materially.

**Practical safety protocol:**
1. Stay at or below **600 mg EGCG/day** for sustained use in the stack (buffer below the EFSA 800 mg ceiling).
2. **Take with food** — this lowers free-EGCG Cmax and reduces hepatotoxicity risk, even though it also lowers the proteasome-level plasma concentration. The safety / efficacy trade here favors food-concurrent dosing for chronic supplementation.
3. **Avoid combining with alcohol or other hepatotoxic agents** (acetaminophen at hepatotoxic doses, amiodarone, isoniazid, methotrexate). The mechanism of EGCG hepatotoxicity is still debated (proteasome-driven vs. redox-driven — see [Open questions](#open-questions)), so additive liver stress from any angle is a concern.
4. **Monitor ALT/AST annually** if sustaining doses ≥400 mg/day for >6 months. Stop and investigate if ALT >3× ULN.
5. **Avoid the compound entirely** if there is any baseline liver disease (viral hepatitis, NAFLD with elevated enzymes, autoimmune hepatitis).

This safety ceiling is not a reason to exclude EGCG from the stack — it is a reason to cap the dose and monitor. Within the 400–600 mg/day window with food, the safety record is long (green tea consumption in East Asia predates written records) and the CP1/CP1a/CP4/CP5a coverage is uniquely wide for a food-grade compound.

---

## Engineered-production angle

EGCG is a plant secondary metabolite requiring 8–10 heterologous enzyme steps (PAL → C4H → 4CL → CHS → CHI → F3H → F3'H → FLS → gallate conjugation via UGT) to reconstitute in *S. cerevisiae*. Published engineered-yeast titers for EGCG specifically are in the **10–50 mg/L range** (source: [nlrp3-inhibitor-screen.md](./nlrp3-inhibitor-screen.md)), well below the economic threshold for an Open Enzyme production module.

**Current Open Enzyme position on EGCG:** Dietary / supplement, not a production target. Green tea is already an engineered agricultural product (centuries of cultivar selection + processing refinement) that outperforms any plausible microbial production route. The practical engineering problem for EGCG is **bioavailability enhancement**, not biosynthesis — phospholipid complexes (Greenselect Phytosome), lipid-nanoparticle encapsulation, and COMT-inhibitor co-formulation are the relevant levers. These are formulation-chemistry problems, not strain-engineering problems, and sit outside Open Enzyme's core platform thesis.

If a future Open Enzyme module wants to work on flavan-3-ol delivery (e.g., koji-fermented matcha with improved catechin bioavailability through the fermentation matrix), that is a plausible secondary avenue — but it would be a formulation project, not a biosynthesis project.

---

## Open questions

1. **Is the 86 nM proteasome IC50 reached at physiological green-tea doses?** At 0.1–0.3% oral bioavailability, even 800 mg EGCG oral → plasma free-EGCG in the low nM range, well below the 86 nM IC50 in cells. Phytosome formulations (5–10% bioavailability) can plausibly reach the IC50; unformulated green tea probably cannot. This is the central translation question for the CP1 story. An ex vivo assay (incubate human PBMCs with serum drawn 1–4 h post-EGCG dose; Western for IκBα retention) would resolve it directly.
2. **Proteasome vs. IKK dose-response.** If the reframe above is correct, the dose-response for IκBα stabilization (Western) and for IKK activity (IKK kinase assay, phospho-IκBα readout) should diverge — IκBα stabilization tracks proteasome IC50 (86 nM), IKK activity should require much higher EGCG (the literature suggests IKK IC50 is ≥10 μM for EGCG, not sub-μM). A dose titration with both readouts in the same experiment falsifies or confirms the reframe.
3. **Hepatotoxicity mechanism.** Is EGCG-induced liver injury driven by proteasome inhibition (analogous to bortezomib), by redox chemistry (pro-oxidant at high doses via auto-oxidation of the gallate ring), by mitochondrial membrane effects, or by an idiosyncratic immune mechanism? The existing literature is divided. The practical dose cap (600 mg/day, with food) is conservative enough to cover all four hypotheses, but mechanistic clarity would inform future formulation choices — a proteasome-driven mechanism might be worsened by phytosome bioavailability boosters, whereas a redox-driven mechanism might be mitigated by them.
4. **Does EGCG suppress TNFSF14 at the HVEM-receptor level specifically, or only through general NF-κB blockade?** Hosokawa 2010 reported **HVEM downregulation**, which if real is a receptor-specific effect not reducible to proteasome inhibition (HVEM transcription is not obviously NF-κB-dominant in HGF cells). Replicating this in human macrophages (THP-1 or PBMC-derived MDM) with a TNFSF14-stimulated IL-6 / IL-1β readout would determine whether CP1a is a separate EGCG mechanism or a consequence of general CP1 blockade.
5. **Can DHA + EGCG achieve combined TNFSF14 suppression?** DHA lowers circulating TNFSF14 (Huang 2024 Mendelian randomization; source: [tnfsf14-gout-target.md](./tnfsf14-gout-target.md)); EGCG suppresses TNFSF14 signal transduction at the receiving cell. These are orthogonal layers of the same amplifier. A combination trial would have clear synergy logic and both compounds are already in the stack.

---

*This dossier is the canonical EGCG page. The stack-level entry in [supplements-stack.md](./supplements-stack.md) keeps the short dosing summary; the chokepoint row in [nlrp3-exploit-map.md](./nlrp3-exploit-map.md) keeps the mechanism pointer; anything deeper — mechanistic reframe, primary-source evidence, safety rationale, engineering position — lives here.*
