---
title: "Medicinal Mushroom Complement Track — Phase 7 Platform Expansion"
date: 2026-05-06
tags:
  - medicinal-mushrooms
  - chassis-strategy
  - native-compound-producers
  - peer-track
  - platform-strategy
  - cultivation
  - scope-page
  - first-principles
related:
  - etc/open-enzyme-vision.md
  - etc/open-source-platform.md
  - modality-chokepoint-matrix.md
  - engineered-lbp-chassis.md
  - sirna-urat1-modality.md
  - medicinal-mushroom-compound-mapping-computational.md
  - computational-experiments.md
  - engineered-koji-protocol.md
  - koji-home-fermentation.md
sources:
  - "Brian framing 2026-05-06: 'we were using koji as the tool that we want to jam these things onto, and that itself is a fungus. We just looked at all these other fungi, and I'm wondering: is there another fungus that could be easily grown at home that would be either a better solution than koji or a complementary solution with koji?'"
  - "comp-014 Phase 6 triage (2026-05-06) — GLPP / cordycepin / ergothioneine routed to cultivation track; GLPP+cordycepin synergy pair flagged"
  - "Phase 1 chassis-comparison analysis: ascomycete (koji) genetics is 5-10x more mature than basidiomycete (medicinal mushrooms) for protein-secretion engineering"
status: scoped (Phase 1)
---

# Medicinal Mushroom Complement Track — Phase 7 Platform Expansion

## Why this page exists

Open Enzyme's koji thesis is "engineered *A. oryzae* secretes therapeutic enzymes via home-fermentable food." The koji chassis is uniquely positioned for that role — decades of ascomycete secretion-biology toolkit (KEX2 protease handling, glucoamylase fusion machinery, CRISPR works, signal-peptide engineering precedent). It is the right engineering chassis.

But comp-014 (medicinal mushroom × chokepoint mapping) surfaced a different category of leverage: **medicinal mushrooms are native producers of compounds that don't lend themselves to koji engineering** — polysaccharide-peptide hybrids (GLPP), nucleoside analogs (cordycepin), thiol antioxidants (ergothioneine), terpenoid-class secondary metabolites. These don't fit the "express recombinant protein in koji" paradigm; they fit a "cultivate the producer organism, extract the compound" paradigm.

Brian's 2026-05-06 inversion was the right one: not "find a better engineering chassis than koji" (basidiomycete genetics is 5-10× harder than ascomycete; engineering Pleurotus / Lentinula / Hericium / Ganoderma for protein secretion is a multi-year toolkit-building project before first construct expresses) but **"are there other home-cultivable fungi whose native compound profile complements what koji produces?"** Yes.

This page formalizes the **medicinal mushroom complement track** as a peer track to the koji engineering track under the broader Open Enzyme platform thesis. Same pattern as [`engineered-lbp-chassis.md`](./engineered-lbp-chassis.md) (engineered LBPs as obligate-anaerobe chassis sibling to koji) and [`sirna-urat1-modality.md`](./sirna-urat1-modality.md) (kidney-tropic siRNA as discovery-engine output sibling to fermentable enzymes). All three peer tracks expand Open Enzyme from "engineered enzymes in koji" to "solve gout, every avenue, fully open."

## Platform thesis expansion

| Track | Chassis | Engineering effort | Therapeutic class | Consumption UX |
|---|---|---|---|---|
| **Engineered koji (existing)** | *A. oryzae* | Heavy — recombinant cassette + secretion engineering | Therapeutic enzymes (uricase, lactoferrin, DAF SCR1-4, koji-secreted complement regulators) | Shio-koji / amazake / miso (daily food condiments) |
| **Engineered LBPs (peer)** | *F. prausnitzii* / *Akkermansia* | Heavy — anaerobe engineering, LBP regulatory path | Live therapeutic with sustained colonic activity (butyrate, IL-22, anti-complement) | Refrigerated capsule / reconstituted suspension (commercial pharma) |
| **siRNA / kidney-tropic discovery (peer)** | n/a (synthetic) | Heavy — sequence design, conjugate chemistry, delivery | Sequence-specific knockdown (URAT1) | Subcutaneous injection (commercial pharma) |
| ***Medicinal mushroom complement (THIS page)*** | *G. lucidum*, *C. militaris*, *Pleurotus*, *Lentinula*, *Hericium*, *G. applanatum*, *Inonotus* | **Light — strain selection + cultivation optimization + extract characterization. NO genetic engineering.** | Native-compound supplements (GLPP, cordycepin, ergothioneine, eritadenine, erinacines, betulinic acid derivatives) | Dried fruiting body / tincture / broth / powder (home cultivation OR consumer supplement) |

The fourth track is **the lightest engineering effort and the most accessible UX** — but it covers a chemistry space koji cannot reach.

## What goes on this track vs. the koji track

**Routed to the medicinal-mushroom-complement track (per comp-014 Phase 6):**

- **GLPP polysaccharide-peptide** (*Ganoderma lucidum*) — ADA + GLUT9 + OAT1 chokepoints, 40.6% UA reduction in HUA mice. Not a koji-engineering target; biosynthesis is mycelium-specific. Native cultivation is the route. **MW resolution (grep-verify gate, 2026-05-06):** The apparent 520 vs. 37 kDa "discrepancy" is a fractionation-stage difference, not an inconsistency. **520 kDa is the bulk crude polysaccharide-peptide preparation** from the Juncao National Engineering Research Center — sister paper [PMC11351902](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11351902/) (Zhang 2024) §2.1 explicitly states "the average molecular weight of GLPP was approximately 520 kDa" for the same Juncao prep. **31–42 kDa are the post-DEAE-fractionation sub-fractions** — independently verified at 37,121 Da (GL-PP) and 31,130 Da (GL-PP2) per [PMID 37852403](https://doi.org/10.1016/j.ijbiomac.2023.127336) and 42,635 Da per [PMID 29541200](https://doi.org/10.3892/ol.2018.7823). The Lin 2022 HUA paper itself (PMID 36385640, paywalled body) does not specify which sub-fraction it used; bulk-prep most likely based on sister-paper consistency. SOP-1 SEC-MALS at Tier 3 remains non-negotiable to determine which fraction the HUA mechanism load-bears on.
- **Cordycepin** (*Cordyceps militaris*) — URAT1 chokepoint, animal model SUA 337→203 µmol/L. **Canonical platform route: cultivation, not koji engineering** (revised 2026-05-16). *C. militaris* liquid fermentation is mature; top strain GYS60 (plasma-mutagenesis derivative) hits 7,883 mg/L static liquid (PMID 33463932). Commercial whole-fermentate *C. militaris* extracts deliver cordycepin with native pentostatin co-protection at the co-evolved ratio at $20–60/month nutraceutical pricing. The food-grade *A. oryzae* koji-engineering route (Jeennor 2023, PMID 38071331, 564 mg/L/d on glucose) was **evaluated and deprioritized** during the 2026-05-15 sweep walkthrough (Item 7) — comp-023 confirmed metabolic-burden feasibility, but koji-engineered cordycepin delivers no novel chokepoint coverage beyond the cultivation route, has an unresolved dose-vs-achievable-titer gap in realistic multi-cassette home-fermentation conditions, and the "endgame strain = full coverage + simple" principle does not justify the engineering complexity for a payload available at the supplement shelf. See [`koji-endgame-strain.md` §3.5 "Cordycepin third-cassette slot — evaluated and deprioritized"](./koji-endgame-strain.md) for the full reasoning.

- **The natural Cordyceps ADA-inhibitor pairing** — C. militaris natively co-produces **pentostatin** from the same BGC cluster as cordycepin (Xia 2017, PMID 29056419). Pentostatin is a clinical-grade ADA inhibitor; this means whole-fermentate Cordyceps preparations have a built-in safeguard against cordycepin deamination that purified cordycepin lacks. **This reframes the Phase 6 GLPP+cordycepin synergy hypothesis** — the native ADA inhibitor is already packaged with cordycepin in fermented C. militaris. The GLPP+cordycepin synergy may be redundant with whole-fermentate Cordyceps, but a **purified cordycepin + GLPP** combination would still benefit from GLPP's ADA modulation. Wet-lab gate now has a 4-arm question: whole-fermentate Cordyceps vs purified cordycepin vs purified cordycepin + GLPP vs purified cordycepin + pentostatin.

- **Ergothioneine** — **Phase 7-1c correction:** *Pleurotus ostreatus* is NOT the highest EGT producer; ***P. citrinopileatus* (golden oyster) is 2-3× higher** (7.0 vs 2.4 mg/g DW). Apex strain: *P. citrinopileatus* 303 with two-stage H₂O₂+vit C oxidative stimulus → 641.76 mg/L submerged fermentation (Li 2025). Dietary intake plausibly therapeutic-dose: 50-100g fresh oyster ≈ 12-24 mg EGT, within published RCT-investigational range. OCTN1/SLC22A4 saturates at ~25 mg/day → **concentrated extracts have diminishing returns**, "daily oyster mushroom in dinner stir-fry" is mechanistically sound. *A. oryzae* / koji also produces ergothioneine (secondary).
- **Eritadenine** (*Lentinula edodes*) — cardiovascular activity, cholesterol-lowering. Native cultivation route.
- **Erinacines / hericenones** (*Hericium erinaceus*) — NGF-inducing (CNS-relevant). Native cultivation route.
- **Inotodiol / betulinic acid derivatives** (*Inonotus obliquus*) — triterpenoid chemistry overlapping reishi. Native cultivation route.
- **PSK / PSP polysaccharide-protein complexes** (*Trametes versicolor*) — β-glucan immunomodulator, FDA-approved adjuvant in Japan. Native cultivation route.

**Stays with the koji-engineering track:**

- **Recombinant uricase** (existing OE thesis — `engineered-yeast-uricase-proposal.md`, `engineered-koji-protocol.md`)
- **Lactoferrin** (existing OE thesis)
- **DAF SCR1-4 truncated complement regulator** (comp-006 / comp-012)
- **DAE (methyl 2,4-dihydroxybenzoate)** — small molecule, chemical synthesis preferred over fungal extraction (per comp-014 Phase 6 production-route assessment)
- **Any future therapeutic protein** — koji is the chassis when secreted protein is the deliverable

**Combined / synergy candidates (per comp-014 Phase 6, refined by Phase 7-1b strain scan):**

- **Whole-fermentate Cordyceps (cordycepin + native pentostatin)** — Phase 7-1b discovered that *C. militaris* natively co-produces pentostatin from the same BGC as cordycepin. Whole-fermentate preparations have the ADA-inhibitor safeguard built in. **This is the cleanest single-organism medicinal-mushroom-complement product** — fermented C. militaris on brown rice (4-8 week home cycle) delivers cordycepin + pentostatin in their natural ratio, no synergy assembly required.
- **GLPP + (purified) cordycepin** — only relevant if purified cordycepin is the delivery format. With whole-fermentate Cordyceps, the ADA-inhibitor pairing is already intrinsic. Wet-lab gate (4-arm comparison) now answers: which delivery format wins on dose efficiency + reproducibility.
- **Whole-fermentate Cordyceps + GLPP (two-organism stack)** — the cultivation-only, zero-engineering combination: fermented *C. militaris* (delivering cordycepin + native pentostatin) + *G. lucidum*-derived GLPP supplement. Targets ADA from two independent biochemical entry points — pentostatin (small-molecule competitive inhibitor) + GLPP (polysaccharide-peptide binding) — while cordycepin is the substrate whose half-life is being protected. This is the **fermentable / enzymatically-naive intervention** at the ADA chokepoint: requires only cultivating two GRAS fungi, no genetic engineering. Distinct from the whole-fermentate-Cordyceps-alone bullet above because GLPP adds a *second*, mechanistically orthogonal ADA-blockade path rather than substituting for the native pentostatin. Wet-lab gate: 4-arm ADA half-life assay (per Proposed Experiment in 2026-05-08 sweep) extended with a fifth arm — whole-fermentate *Cordyceps* + GLPP — to test whether the two-organism combination outperforms either single-organism preparation.
- ~~**Engineered koji cordycepin (cns1+cns2) + GLPP supplement**~~ — *Deprioritized 2026-05-16*. The koji-engineered cordycepin route was removed from active cassette stack; this combination is moot. The cultivation-track equivalent (whole-fermentate *Cordyceps* + GLPP) above remains the canonical platform path.
- ~~**Engineered koji cordycepin (cns1+cns2) + whole-fermentate *C. militaris* (native pentostatin)**~~ *— added 2026-05-15, deprioritized 2026-05-16.* This cross-chassis "patch" was an attempt to install pentostatin protection for the koji-engineered cordycepin route. With koji-cordycepin engineering deprioritized (no novel chokepoint coverage + open dose-vs-titer gap + commercially available alternative), the cross-chassis patch is moot. The cultivation route already delivers cordycepin + pentostatin together at the natural ratio. See [`koji-endgame-strain.md` §3.5](./koji-endgame-strain.md).
- **Engineered koji uricase + GLPP supplement** — koji handles bulk urate degradation in gut lumen; GLPP modulates ADA upstream + GLUT9/OAT1 transporters for renal-side support. Cleanest cross-track synergy (engineering + cultivation).

## Substrate engineering as the most-accessible cultivation lever (added 2026-05-19)

Substrate composition is not just a documentation concern — it is a deliberate engineering variable with documented effect sizes from 1.2× (yield aggregate) up to 100× (specific compound profile shifts within a class) and 22× (combined precursor + induction). This finding emerged from the 2026-05-19 substrate-engineering lit scan ([`logs/substrate-engineering-mushroom-cultivation-lit-scan-2026-05-19.md`](../logs/substrate-engineering-mushroom-cultivation-lit-scan-2026-05-19.md)). The synthesis daemon's prior framing ("substrate accumulation creates a QC documentation discipline") under-claimed the empirical literature by ~10×.

**Four mechanisms operate, each with primary-literature anchors:**

1. **Passive accumulation** — substrate compounds traverse mycelium (plant flavonoids in oak substrate; tree-host polyphenols in *I. obliquus* conks — *Alnus incana* conks have 4–30× higher betulinic acid than *Betula pendula* per Drenkhan 2022 [PMC9496626](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9496626/)).

2. **Biotransformation** — fungal enzymes modify substrate compounds (betulin → betulinic acid in *I. obliquus*; lentinan biosynthesis from substrate cellulose).

3. **Substrate induction of biosynthetic gene clusters** — substrate components act as transcriptional signals. Microcrystalline cellulose 1.5% delivers +85.96% ganoderic acid via HMGR/SQS/LAS upregulation (HMGR up 3.5–4.3×; Hu 2017 [PMC5395960](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5395960/)). Oleic acid upregulates Cns1/Cns2 in *C. militaris*, delivering 34× cordycepin difference between *A. dichotoma* and *B. mori* insect substrates (Turk 2022 [PMC9627333](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9627333/)).

4. **Precursor feeding** — direct addition of biosynthetic precursors. 12 g/L alanine → 3× cordycepin via Cns2/Cns3 upregulation (Yu 2024 [PMC11698586](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11698586/)); 2 mM methionine → 1.7–3.1× ergothioneine across multiple species (Lee 2009 [PMC3749454](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3749454/)).

**Critical finding: substrate engineering shifts compound PROFILE, not just yield.** Wood-log vs. substitute-substrate *G. lucidum* produces measurably different triterpenoid spectra — substitute-grown fruiting bodies show 13.5× higher ganosporelactone B and 10× higher ganoderol A, while wood-log fruiting bodies show 2.19× higher total lucidenic acids (Luo 2024 [PMC10879320](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10879320/)). *Hericium* minimal vs. complex liquid media shifts erinacine C ↔ erinacine Q ratios by ~100× **even when *eri* gene transcript levels don't change** (Doar 2025 [PMC11969743](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11969743/)) — a post-transcriptional substrate-driven compound-profile shift.

**Operational implication for distributed contributors:** substrate engineering is **the lightest-effort, highest-leverage modality** — every load-bearing reagent (methionine, alanine, oleic acid, microcrystalline cellulose, D-galactose, corn steep liquor, casein hydrolysate, nucleosides) is GRAS food-grade and available at consumer pharmacy / grocery retail for $20–50/kg. This compounds with strain selection rather than competing with it. The discipline is target-compound-anchored: a substrate protocol without paired Tier-2/Tier-3 characterization (per [`medicinal-mushroom-extract-sops.md`](./medicinal-mushroom-extract-sops.md) SOP-6 and the new SOP-7 protocol matrix) is non-falsifiable.

**Platform-principle elevation (2026-05-19):** this finding promoted from "queued open question" to named **Platform Principle 9** in [`etc/open-source-platform.md`](./etc/open-source-platform.md). Strain engineering needs academic infrastructure; substrate engineering can be executed from a kitchen. It is the cleanest fit yet between the platform's distributed-accessibility thesis and a primary engineering mechanism.

**Falsifiable wet-lab priority surfaced by the lit scan:** cordycepin × pentostatin ratio under varied substrate conditions (alanine vs CSLH vs insect substrate vs oleic combinations) — directly extensible from SOP-2 HPLC. Queued as [§1.29 in `validation-experiments.md`](./validation-experiments.md) (added 2026-05-19). Resolves the whole-fermentate-vs-purified clinical positioning gap that has been open in the wiki.

---

## Scope (Phase 1)

### Candidate species

Subset of the comp-014 Phase 5 anchor list, prioritized by:
1. Strength of comp-014 chokepoint-mapping evidence (in vivo > in vitro > predicted)
2. Home-cultivability (kit-scale UX > requires bioreactor > requires specialized substrate)
3. GRAS / pharmacopoeia status (no regulatory novelty needed)
4. Native compound profile diversity (multi-compound producers preferred — broader Open Enzyme value)

| Species | Common name | Top compounds | Cultivation UX | Regulatory |
|---|---|---|---|---|
| *Ganoderma lucidum* | reishi / lingzhi | GLPP, ganoderic acids (400+), ergosterol | Solid-state on hardwood; commercial mycelium kits widely available; 6-12 months for fruiting body | GRAS supplement |
| *Cordyceps militaris* | cultivated cordyceps | cordycepin, polysaccharides, ergosterol peroxide | Liquid fermentation OR solid-state on brown rice; 4-8 weeks home cycle; commercial kits available | GRAS supplement |
| ***P. citrinopileatus*** | golden oyster | **ergothioneine (highest fungal producer — 7.0 mg/g DW)**, β-glucans | Same straw / sawdust substrate as P. ostreatus; commercially less common than oyster but kits available | GRAS food |
| *Pleurotus ostreatus* | oyster mushroom | ergothioneine (2.4 mg/g DW — was originally claimed as highest, corrected by Phase 7-1c scan), lovastatin (190-342 mg/kg DW), pleuran | **Easiest home cultivation** — straw / coffee grounds / sawdust substrate; 4-6 weeks; widely sold consumer kits | GRAS food |
| *P. djamor* | pink oyster | β-glucans (43% DW — highest in genus) | Same as P. ostreatus | GRAS food |
| *P. eryngii* | king oyster | ergothioneine (5.84 mg/g DW Hi-Ergo strain) | Same as P. ostreatus | GRAS food |
| *Lentinula edodes* | shiitake | lentinan, eritadenine, ergosterol→D2 | Log / sawdust block; 6-18 months; widely sold consumer kits | GRAS food |
| *Hericium erinaceus* | lion's mane | erinacines, hericenones | Sawdust block / log; 4-8 weeks; widely sold consumer kits | GRAS food |
| *Trametes versicolor* | turkey tail / yun zhi | PSK, PSP | Hardwood log / dowels; 6-18 months for fruiting body | Supplement (PSK is approved drug in Japan) |
| *Inonotus obliquus* | chaga | betulinic acid derivatives, inotodiol, melanin | Wild-harvest from birch (slow growth); cultivation difficult; commercial mycelium-grown extracts widely available | Supplement |
| *Ganoderma applanatum* | artist's conk | DAE (small molecule), polysaccharides | Solid-state on hardwood; less commercially developed than G. lucidum | Supplement |
| *Aspergillus oryzae* (koji) | koji | ergothioneine (secondary), kojic acid, secreted enzymes | Already documented in `koji-home-fermentation.md` | GRAS food |

The medicinal-mushroom-complement track is **species-additive to comp-014's anchor list, not separate** — the same well-studied species, evaluated through a different lens (cultivation feasibility + native-compound consumption rather than engineering-chassis suitability).

### Ascomycete secondary metabolites — Talaromyces, not Penicillium (identity-corrected 2026-05-19) — chassis-pending discovery note

The track's candidate species above are all basidiomycetes. comp-014 Phase 3 surfaced direct caspase-1 (CASP1) inhibitors at sub-μM potency from "Penicillium" — a chokepoint coverage the basidiomycete corpus lacks. The 2026-05-19 lit scan ([`logs/food-grade-penicillium-casp1-lit-scan-2026-05-19.md`](../logs/food-grade-penicillium-casp1-lit-scan-2026-05-19.md)) **materially revised the framing**:

**Identity correction:** The original Berkeleyamide-producing strain (Stierle 2008, "*P. rubrum*" Berkeley Pit isolate) has been **reclassified to *Talaromyces amestolkiae*** — a different genus from the cheese-ripening *Penicillium* species (P. camemberti / P. roqueforti). Berkeleyamides A/D (CASP1 IC50 330/610 nM via comp-014 pChEMBL anchors 6.48/6.21) are *Talaromyces* chemistry, not *Penicillium* chemistry. (The reclassification is inferred from secondary sources — Yilmaz 2014 + WebSearch hits; primary-source confirmation via Hoody 2026 [PMC13150583] recommended before any downstream commitment.)

**Why the food-grade Penicillium framing was misdirected (three independent reasons):**

1. **Wrong genus.** P. camemberti / P. roqueforti are in genus *Penicillium* proper, taxonomically distinct from *Talaromyces*.
2. **Wrong direction of effect.** The closest food-grade *Penicillium* "anti-inflammatory" candidate — mycophenolic acid — is **pro-NLRP3, not anti** (Huang 2018 [PMC6032679](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6032679/): MPA synergizes with LPS to activate the inflammasome at 5–75 μM). A wet-lab assay seeing "CASP1 modulation" in cheese-strain extracts would risk reading MPA as a positive when it's the opposite direction.
3. **Wrong genome.** Domesticated cheese *P. roqueforti* strains have **actively-degraded toxin BGCs** (Crequer 2024 [PMC11605963](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11605963/) — frameshift in PR-toxin ORF, deletion in mpaC). Substrate-induction cannot unlock what's been mutated out. The 2023 canonical BGC review for *P. roqueforti* (Chávez [PMC10144355](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10144355/)) enumerates the entire chemotype (andrastins, MPA, roquefortines, PR-toxin, eremofortins, isofumigaclavines, festuclavine, annullatins) — Berkeleyamide / Berkeleyone **are absent from the genome**, not just unexpressed.

**Corrected platform-relevant path — computational first, wet-lab only if signal:**

1. **antiSMASH genome scan** ($0, ~3hr compute) of P. roqueforti / P. camemberti / P. rubens for NRPS-PKS hybrid BGCs matching the Berkeleyamide architecture (NRPS amide-bond-forming + meroterpenoid backbone). If no homologs found, the cryptic-Berkeleyamide hypothesis is falsified for cheese strains at zero cost.
2. **Pull *Talaromyces amestolkiae* BGC** if available — Stierle group at U. Montana may have deposited assembly (FAC-NGS data per Cryptic Biosynthesis paper [PMC8574098](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8574098/)). Reach out via JGI MycoCosm or direct email.
3. **If antiSMASH returns plausible homologs in cheese strains** → wet-lab assay becomes platform-relevant. Defensible budget with mycotoxin pre-screen (LC-MS) + CASP1 enzymatic assay + orthogonal cytotoxicity is **$5–15K** (not the originally-scoped $500–1,000 — that figure assumed direct testing without disambiguation infrastructure).
4. **If antiSMASH returns nothing in cheese strains but *T. amestolkiae* has a clean BGC** → the platform-relevant question shifts entirely to **engineering the Berkeleyamide BGC into the koji chassis** (A. oryzae heterologous host, which already supports andrastin-type meroterpenoid assembly per Matsuda et al. 2013 cited in [PMC5418334](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5418334/)). This is a much cleaner play than coaxing cheese strains to express foreign chemistry.

**Status: chassis-pending discovery note with computational gates.** No wet-lab commitment until antiSMASH signal materializes. The identity correction is the main load-bearing update: any future BGC-mining work must target *Talaromyces amestolkiae*, not cheese-ripening *Penicillium*. comp-014 Phase 3's "Penicillium" attribution should also be corrected to "Talaromyces amestolkiae" in any future re-render of that page.

See [`logs/food-grade-penicillium-casp1-lit-scan-2026-05-19.md`](../logs/food-grade-penicillium-casp1-lit-scan-2026-05-19.md) for the full lit scan.

### Cultivation method comparison (Phase 7 follow-up)

Three home-feasibility levels:

1. **Consumer-kit** (oyster, lion's mane, shiitake, reishi, turkey tail) — pre-inoculated grow blocks ($15-50), 4-12 weeks fruiting cycle, no specialized equipment beyond mister bottle + plastic tent.
2. **Mycelium kit** (cordyceps, more advanced reishi) — agar plate or grain spawn → fermentation jar / brown rice substrate; 4-8 weeks; requires sterilization (pressure cooker).
3. **Bioreactor** (defined-media liquid fermentation for standardized GLPP / cordycepin yield) — not home-feasible at consumer scale; commercial extract supply is the route.

Open Enzyme's value-add at the cultivation-method layer is **standardization + characterization protocols**, not novel cultivation. Consumer-grade reishi grow kits are ubiquitous; what's missing is the protocol that says "this batch contains X mg/g GLPP, Y% triterpene content, Z µg/g ergosterol — verified by standardized extraction + analysis." That's the Open Enzyme contribution to this track.

### Production route — sequential cultivation-first default (added 2026-05-06)

For compounds that have both a cultivation route and a koji-engineering route — cordycepin being the canonical case — the platform default is **sequential cultivation-first**. The koji-engineering route is held as documented contingency, not parallel commit.

**Cordycepin example (the worked case):**

| Route | Titer / time | Format | Maturity | Cost to test |
|---|---|---|---|---|
| ***C. militaris* GYS60** cultivation (PMID 33463932) | 7,883 mg/L | Liquid submerged fermentation | Mature industrial process; established CROs | $1–2K outsourced |
| **Engineered *A. oryzae* cns1+cns2** (Jeennor 2023, PMID 38071331) | 564 mg/L/day | Solid-state koji | One paper, novel | $2–4K outsourced; in-house requires separate setup |

**Why not parallel head-to-head (Principle 6 carve-out):** [Platform Principle 6 — variant-agnostic empirical head-to-head](./etc/open-source-platform.md) says default to parallel testing when literature is split AND marginal cost is bounded by shared infrastructure. The cordycepin case fails the second precondition: cultivation requires liquid submerged bioreactor, koji-engineering requires solid-state trays — different fermentation infrastructure, different downstream purification, different QA. Sequential cultivation-first is the right call: GYS60's 7,883 mg/L is mature and reproducible; koji-engineering at 564 mg/L/day (~14× lower per unit time) is one paper. The chassis-coherence appeal of "everything in koji" is real but not load-bearing for a small-molecule supplement — cordycepin's structure doesn't care which organism made it.

**Supply check.** Even at high-end therapeutic dosing (~500 mg/day pure cordycepin — see Phase 7 follow-up #7 for verification queue), 1 L of GYS60 broth = ~16 daily doses. A modest 1,000-L run = ~44 person-years of supply. Neither route is supply-constrained for this product class; the decision is cost, reproducibility, and CRO availability — not throughput.

**⚠️ Reality check — current consumer-grade fruiting-body extracts deliver sub-therapeutic cordycepin doses.** Empirically (verified against Real Mushrooms' published HPLC data 2026-05-06), high-quality fruiting-body extracts like Real Mushrooms Cordyceps-M test at **0.1–0.3% cordycepin (~0.4% in recent batches)**, equating to **~3–4 mg cordycepin per ~1 g serving**. That is **25–150× below typical consumer pure-cordycepin nutraceutical doses** (100–500 mg/day) and likely orders of magnitude below the dose where animal-model URAT1-inhibition was demonstrated. The implication: **today's consumer-grade fruiting-body extracts are valuable as general mushroom adaptogens / β-glucan / immune-layer products, but should not be marketed or recommended as URAT1-inhibition therapy** — the dose math doesn't support it. A pure-cordycepin nutraceutical at ~150–500 mg/day is the only product format that delivers a therapeutically-relevant cordycepin dose; that market segment is real but quality-variable and pricier (~$150–300/month). This is the canonical motivating example for [Phase 7 follow-up #7 — therapeutic dose grounding pass](#seven-phase-7-follow-ups-queued): without dose-vs-product-content grounding, the platform is at risk of recommending interventions whose actual delivered dose is sub-threshold for the cited mechanism.

**When the koji-engineering contingency activates:** speculative — none of the trigger conditions are currently load-bearing. (a) Cultivation supply chain disruption / quality issues, (b) scale-up economics later favoring solid-state for some other co-produced compound, or (c) IP / regulatory positioning making the engineered-organism route strategically valuable. **All three are real-but-unlikely triggers.** Cordycepin is a small molecule whose therapeutic effect doesn't depend on which organism made it, so chassis-coherence is not load-bearing for this compound. The supply math is fine for the koji route at industrial scale (Jeennor's 564 mg/L/day × 1,000-L bioreactor = ~1,000–3,000 person-days of supply per batch at therapeutic dose), but cultivated GYS60's 14× higher per-unit-time titer + mature CRO ecosystem + classical-use precedent + consumer trust dominate. **The contingency is documented for completeness, not as live planning.** Default to GYS60 cultivation; revisit only if a specific external trigger surfaces.

**The same sequential-first logic applies generally** to any compound with both a mature cultivation precedent and a novel-engineering route. Default to the mature route; document the engineering contingency; only switch when supply, cost, or strategic-fit forces it.

### Therapeutic UX

Consumption modalities for the cultivation track:

- **Dual decoction** (water + ethanol sequential extraction → blended) — captures both polysaccharide and terpenoid fractions. Traditional Chinese medicine standard for reishi. Concentrated to liquid extract or spray-dried to powder.
- **Tincture** (ethanol-only extraction) — captures terpenoid + small molecule fractions; not polysaccharides. Better for ganoderic acids, erinacines, betulinic acid derivatives.
- **Hot water tea** (decoction only) — captures polysaccharides, water-soluble small molecules. Lentinan from shiitake, GLPP from reishi.
- **Dried powder** (whole fruiting body or mycelium → dried → ground) — broad-spectrum but low concentration. Familiar consumption format (capsule or food-incorporation).
- **Co-administration with koji-condiment** (the integration point with the koji track) — daily shio-koji + periodic mushroom decoction, or mushroom powder added to koji condiments.

The UX is meaningfully different from the koji track and that's a feature, not a bug — different therapeutic categories may be best served by different formats. Daily koji shio-koji on rice for uricase; weekly reishi tea for GLPP-mediated ADA modulation; oyster mushroom in dinner stir-fry for ergothioneine.

## Why this isn't just "buy mushroom supplements"

Consumer-grade mushroom supplements have known quality issues:

1. **Species mis-identification** — DNA-barcoded studies of Ganoderma supplements regularly find <50% contain the species labeled.
2. **Compound content uncharacterized** — "reishi extract 1000mg" tells you nothing about GLPP, ganoderic acid, ergosterol content. Triterpene content alone varies 100× between products.
3. **Adulteration with inactive carriers** — mycelium-on-grain products are mostly grain (β-glucan from grain ≠ β-glucan from mushroom).
4. **Extract method opaque** — water-only extracts miss terpenoids; ethanol-only extracts miss polysaccharides; consumers can't tell which they bought.

**Open Enzyme's contribution to this track:** publish reproducible cultivation + extraction + characterization protocols. Strain selection criteria. HPLC/MS validation methods. Make a comp-014-style triage repeatable for any open-source contributor. The chemistry IS in the public domain — what's missing is the rigor.

### Consumer-product caveat — structure-dependent β-glucan NLRP3 directionality (added 2026-05-08)

**Mushroom β-glucans are not a monolithic anti-inflammatory class.** Their effect on the NLRP3 inflammasome is *structure-dependent* — different polysaccharide fractions from the same species can activate or inhibit NLRP3 depending on extraction method, branching pattern, and molecular weight.

Per comp-014 Phase 5 ([medicinal-mushroom-compound-mapping-computational.md](./medicinal-mushroom-compound-mapping-computational.md)), as captured in [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md):

- ***G. lucidum* exopolysaccharides (EPS)** — secreted polysaccharide fractions from liquid-fermentation broth — can **activate** NLRP3 via the Dectin-1 / Syk pathway. Wrong direction for a gout intervention.
- ***G. lucidum* spore-powder β-glucans / GLP** — fractions from cracked-spore preparations or dual-decoction GLPP-enriched extracts — can **inhibit** NLRP3 (immune-training / Treg-induction mode of action). Right direction.

**Why this matters for consumer products:** a generic "reishi extract 1000mg" capsule is opaque about which polysaccharide fraction it contains. EPS-dominant preparations and spore-powder/GLPP-dominant preparations are functionally different products at the NLRP3 axis, and a gout patient can inadvertently *worsen* inflammation by picking the wrong fraction. The dual-decoction extraction protocol in [SOP-1](./medicinal-mushroom-extract-sops.md) is specifically designed to enrich for the GLPP fraction, not whole-extract β-glucan; this is part of why "compound content uncharacterized" (#2 above) is load-bearing rather than cosmetic.

**Propagation discipline:** when reishi / GLPP enters [`supplements-stack.md`](./supplements-stack.md) as a catalog entry, OR enters [`gout-action-guide.md`](./gout-action-guide.md) as a specific recommendation, this caveat must travel with it. Currently neither catalog mentions reishi specifically, so no propagation-gap exists today — but the manual `fresh-stack.py` discipline (see [`synthesis/strategic-reflections/`](../synthesis/strategic-reflections/)) will need to flag this as a known caveat-with-the-compound entry when promotion eventually fires.

## Seven Phase 7 follow-ups queued

Same pattern as `engineered-lbp-chassis.md` and `sirna-urat1-modality.md`:

1. **Strain selection lit scan** — for each top species (G. lucidum, C. militaris, Pleurotus, Lentinula, Hericium, Trametes, Inonotus), identify which commercial / academic strains have characterized compound yields. CNKI + J-STAGE + Korean sources critical here (the multilingual ingestion the comp-014 anchor list was originally drafted for, now applied to cultivation rather than chokepoint mapping). Output: per-species strain table with cultivation precedent + compound yield evidence.

2. **comp-NNN cultivation method × yield study** — for ≥3 priority species (start with reishi GLPP + cordyceps cordycepin + oyster ergothioneine), comparative study of liquid fermentation vs solid-state vs fruiting body cultivation, measuring target-compound yield. Open Enzyme runs this as a literature meta-analysis first; wet-lab follow-up only if literature is insufficient or self-experimentation is direct path. The cordycepin yield literature in particular has wide ranges (0.5-5 mg/g dry weight in C. militaris fruiting body) that warrant consolidation.

3. **Extract characterization protocol standardization** — write the open-source SOPs for: (a) reishi dual-decoction extraction yielding GLPP-enriched fraction, (b) cordyceps water extraction yielding cordycepin + polysaccharide fraction, (c) HPLC quantification methods + reference standards. The goal is reproducibility — an Open Enzyme contributor anywhere should be able to follow the SOP and produce a comparable extract.

   **Sub-bullet (added 2026-05-08):** the SOP-6 framework in [`medicinal-mushroom-extract-sops.md`](./medicinal-mushroom-extract-sops.md) is the canonical standardization scaffold — kitchen → smartphone → bench → outsourced tiers, calibrate-once at Tier-3 / track-batches at Tier-2 discipline, per-compound method specs. **Next operational step: a first-execution demonstration batch** — commercial *C. militaris* grow kit (~$50-150) cultivated through Tier 1 yield + Tier 2 EGT colorimetry done at home (Ellman's reagent, well-established), with one outsourced Tier 3 HPLC reference run for cordycepin (~$200-400 CRO). Scope: cordycepin + EGT only; GLPP deferred until Tier 3 SEC-MALS access (load-bearing assay per Pass 3 caveat) is sourced. Cordycepin Tier 2 diazo-coupling stays speculative and is covered by follow-up #7's primary-literature verification pass before being committed to the SOP. Outcome: de-stubbed SOP-2 / SOP-3 with first-batch numbers; reproducibility benchmark for any open-source contributor's later batches. Currently unscheduled — needs a free Brian-weekend or a contributor with a grow setup.

4. **GLPP + cordycepin synergy wet-lab gate** — comp-014 Phase 6 flagged this as the cleanest synergy pair in the breadth pass. Study design: PO HUA mouse model, 4 arms (control / GLPP alone / cordycepin alone / combination), measure SUA + cordycepin PK + ADA activity. Critical question: does ADA inhibition co-treatment extend cordycepin half-life enough to lower the daily dose meaningfully? This is a focused, falsifiable experiment.

5. **Hypothesis card H06 — medicinal-mushroom-complement track viability**. Specifies: what's the kill criterion? When would we abandon this track? Default: if (a) compound yield variability across cultivation batches exceeds 50% even with standardized protocols AND (b) standardized extracts cannot replicate the published in vivo effect sizes within 2× — that's pipeline failure regardless of mechanism truth. Falsifiable.

6. **Comparative chassis/platform matrix for gout** — extend `modality-chokepoint-matrix.md` with a new row "Native-compound mushroom complement" populated with the Phase 7 candidates × chokepoint mapping. Forces explicit comparison: koji-uricase vs reishi-GLPP at the gut-lumen / urate-axis cells. Doesn't pre-determine which wins; makes the comparison tractable for case-by-case decisions.

7. **Therapeutic dose grounding pass** (added 2026-05-06) — for each load-bearing compound in the track (cordycepin, GLPP, ergothioneine, eritadenine, erinacines, PSK, inotodiol, astilbin), grep-verify the human therapeutic dose range from primary clinical / supplement-trial literature under [CLAUDE.md Rule 4 pre-commit grep-verify gate](../CLAUDE.md). The mushroom track scope page currently discusses production yields (mg/L, mg/g DW) without a dose-context anchor — without that anchor, "GYS60 hits 7,883 mg/L" is meaningless to a supplement-stack decision. Output: per-compound dose-grounding table (typical supplement range / clinical-trial range / mechanism-derived effective range / load-bearing-confidence tier). This should land before any wet-lab-gated Phase 2 follow-up depends on compound dose assumptions. Cross-applies to the [TCM compound triage](./tcm-gout-compound-triage-computational.md) compounds — same gap.

   **Sub-bullet (added 2026-05-06):** while doing the per-compound primary-source dive for dose grounding, also note any **validated colorimetric-assay precedents at smartphone-tier (~Tier 2) sensitivity**. Specifically — Pass 2 proposed diazo-coupling for cordycepin (per [`medicinal-mushroom-extract-sops.md` SOP-6](./medicinal-mushroom-extract-sops.md)) but cordycepin lacks the phenolic/amine motifs typical for diazo chemistry, so the proposal needs primary-literature verification before committing to SOP. Ellman's reagent for EGT is well-established and needs no additional literature check. GLPP Tier 2 phenol-sulfuric is total-polysaccharide (not GLPP-specific) — already known; SEC-MALS at Tier 3 is the load-bearing assay. Closing this sub-bullet alongside #7 keeps the literature-search budget bounded — one primary-source pass per compound covers both dose and assay-precedent questions.

## Regulatory clarity (compared to the koji track)

The medicinal-mushroom-complement track has **simpler regulatory positioning** than engineered-organism tracks:

- All species are GRAS food (Pleurotus, Lentinula, Hericium) or established supplement-grade (Ganoderma, Cordyceps, Trametes, Inonotus)
- No genetic modification → no GMO regulatory burden
- Traditional-use precedent is decades to centuries (TCM, Kampo, Korean medicine, Western mycology)
- Existing supplement industry framework (DSHEA in US, equivalent elsewhere) — not a novel regulatory category

This is a real platform advantage, not just a cultivation-feasibility advantage. The koji-engineered tracks (uricase, lactoferrin, DAF SCR1-4) need GRAS-pathway-certification or equivalent for any therapeutic claim. The medicinal-mushroom track is already there.

**Caveat:** dosing claims and efficacy claims are still regulated. "Reishi extract supports urate metabolism" is supplement-language-acceptable; "reishi extract reduces serum uric acid by 40.6%" is structure-function-claim regulated under DSHEA + equivalent. Open Enzyme contributes the **reproducibility and characterization** layer; therapeutic claims remain user-side / clinician-side responsibility.

## Cross-references

- [`open-enzyme-vision.md`](./etc/open-enzyme-vision.md) — top-level mission this expands
- [`open-source-platform.md`](./etc/open-source-platform.md) — platform-strategy positioning; Phase 7 reinforces "explore every avenue" claim
- [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) — canonical chokepoint inventory; Phase 7 follow-up #6 adds new row
- [`engineered-lbp-chassis.md`](./engineered-lbp-chassis.md), [`sirna-urat1-modality.md`](./sirna-urat1-modality.md) — sister peer-track scope pages
- [`medicinal-mushroom-compound-mapping-computational.md`](./medicinal-mushroom-compound-mapping-computational.md) — comp-014 (the parent computational analysis that generated the Phase 7 candidate list)
- [`engineered-koji-protocol.md`](./engineered-koji-protocol.md), [`koji-home-fermentation.md`](./koji-home-fermentation.md) — koji track this complements

## Maintenance

- **When a new candidate species lands** (via comp-NNN extension, new wiki research, or a new compound-pharmacology paper): add to candidate species table; mark its top compounds + cultivation UX + regulatory status; consider for Phase 7 cultivation comp-NNN.
- **When a Phase 7 follow-up resolves**: promote from "queued" to canonical wiki content (e.g., the strain-selection lit scan output becomes a dedicated page per top species).
- **When the koji track adds a new compound**: re-evaluate whether the medicinal-mushroom track has a complementary compound at the same chokepoint (synergy pair candidate).
- **The track is a peer to koji, not a replacement.** Phase 7 deliverables expand the platform without competing with the koji-engineering thesis.

---

**Status:** Phase 1 (scope) committed 2026-05-06. Phases 2-6 are the queued follow-ups above. Brian's call on which phase to fire first.

**CTO-actionable items (no scientific expertise required):** tracked operationally in [`operations/todos.md`](../operations/todos.md) §"Phase 7 medicinal-mushroom-complement track" — order golden oyster grow kit, email Lin Zhanxi 林占熺 lab for Juncao GLPP SOP, open GitHub Issue for Phase 5b multilingual deep-dive contributions, frame comp-014 as recruiting material for the open collaborator roles.

<!-- TODO detail moved to operations/todos.md per folder discipline (wiki = research content; operations = transactional TODOs). Brian's correction 2026-05-06. Original content preserved in git history at commit 2278725. -->
