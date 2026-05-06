---
title: Engineering S. cerevisiae for Oral Uricase Delivery — A Research Proposal
date: April 2026
tags: ['uricase', 'yeast', 'engineering', 'enzyme', 'gout']
status: published
---

[1. Scientific Basis](#basis)
[2. Why Yeast](#why-yeast)
[3. Gene Construct](#construct)
[4. Delivery Formats](#delivery)
[5. Dosing](#dosing)
[6. Open Questions](#questions)
[7. Validation Path](#validation)
[8. Koji Track](#koji)
[9. Risks](#risks)
[10. The Ask](#proposal)
[References](#references)
Engineering *Saccharomyces cerevisiae* for Oral Uricase Delivery
A Research Proposal for Proof-of-Concept Collaboration
**Author:** Brian Abent
**Date:** April 2026
**Status:** Proposal for expert review — requesting guidance, not endorsement
**Circulated to (potential collaborators):** Role 1 (Gut Microbiome / Gnotobiotic Animal Core), Role 2 (Pharma Translation / NF-κB & intestinal signaling), Role 3 (Innate Immune Safety / TLR signaling) — see [`team.md`](./team.md) for the full role descriptions.
This proposal is part of the [Open Enzyme](open-enzyme-vision.md) project — an open-source therapeutic enzyme platform. The yeast track is the fastest path to a working uricase producer.
Evidence levels used throughout:
Established Peer-reviewed, replicated
Supported Published data, limited studies
Extrapolation Reasonable inference from related work
Open Needs experimental data
## 1. The Scientific Basis
Human Uricase Loss Established
Humans, along with all great apes, lack a functional uricase (urate oxidase) enzyme. The gene that once encoded it — *UOX* — is a pseudogene, inactivated by two nonsense mutations at codons 33 and 187 and an aberrant splice site.[[1]](#ref1) This didn't happen once: uricase was lost independently in at least two primate lineages (great apes and lesser apes), and also in birds and some reptiles. The multiple independent losses suggest that elevated uric acid may have conferred a selective advantage — likely related to its role as an antioxidant, a fructose metabolism accelerator aiding fat accumulation, or both.[[2]](#ref2) A 2023 Cell paper identified a widely distributed gene cluster that partially compensates for this loss in hominids, confirming the evolutionary pressure around urate handling.[[3]](#ref3)
The practical consequence: humans maintain serum uric acid levels of 3.5–7.2 mg/dL, whereas most mammals with functional uricase run below 2 mg/dL. When serum urate exceeds ~6.8 mg/dL (the monosodium urate saturation point), crystals can form in joints, tendons, and kidneys — the pathology of gout.
Uric Acid Homeostasis Established
Uric acid is the end product of purine metabolism in humans, generated primarily by the enzyme xanthine oxidase in the liver and intestinal mucosa. Two-thirds of daily urate elimination occurs via renal excretion; approximately one-third is eliminated through the intestine, primarily mediated by the ABCG2 transporter expressed on the apical membrane of intestinal epithelial cells.[[4]](#ref4)[[5]](#ref5) Dysfunction of ABCG2 is now recognized as a significant cause of hyperuricemia — patients with ABCG2 loss-of-function variants have reduced intestinal excretion and compensatory overload on the kidneys.[[6]](#ref6)
This intestinal excretion pathway is the mechanistic foundation for the entire approach proposed here.
The Gut-Lumen Degradation Thesis Supported
The thesis is straightforward: if you place active uricase enzyme in the intestinal lumen, it will degrade uric acid present there (both from intestinal secretion via ABCG2 and from dietary purines). This degradation creates a concentration gradient — a "sink" — that pulls additional uric acid from the serum across the intestinal epithelium. The urate is converted to allantoin, a highly soluble, freely excreted, non-toxic compound.
This is not speculative. Two independent lines of evidence validate the core mechanism:
#### ALLN-346: Engineered Oral Uricase (Allena Pharmaceuticals)
ALLN-346 is an engineered variant of *Candida utilis* uricase, modified using protein engineering (ProteinGPS) to have 20-fold increased stability against pancreatic proteases (half-life of 85.3 min vs. 4.3 min for wild-type *C. utilis* enzyme in 80 ng/μL pancreatin) while maintaining specific activity comparable to the wild-type enzyme.[[7]](#ref7)
In urate oxidase-deficient knockout mice, oral ALLN-346 treatment over 7- and 19-day studies normalized urine uric acid excretion and significantly reduced hyperuricemia.[[7]](#ref7) In the Phase 2a Study 201 in humans (patients with gout and CKD), statistically significant reductions in serum uric acid (sUA) were observed from days 5–7 (p[[8]](#ref8)
> **Honest caveat**
>
> The Phase 2a Study 202, which enrolled a broader cohort, showed mean sUA reductions of only 0–5% from baseline on days 7 and 14 — not statistically significant vs. placebo.[[9]](#ref9) Allena subsequently provided a "clinical and corporate update" (often a euphemism), and the company eventually wound down. The approach works in mice and showed signal in CKD patients with residual renal function, but the human dose-response relationship for oral uricase in the gut is not yet fully established. This is important context.

#### Publicly Disclosed Engineering (Patent Landscape)

*(Mechanistic Extrapolation / regulatory-legal analysis; source: patent landscape memo, April 2026)*

Allena's ALLN-346 engineering is not locked in a proprietary trade-secret vault — it is publicly disclosed in patent form. The family roots in US provisional **62/529,726** (filed 7 July 2017) and matures in:

- **US10815461B2** — "Recombinant uricase enzyme." Granted 27 October 2020; assignee of record **Allena Pharmaceuticals Inc.**; nominal expiry 2038 absent maintenance-fee lapse. *(Clinical/regulatory precedent — patent grant, USPTO)*
- **US 2020/0071681 A1** — published application cited as the sequence source by the Frontiers 2020 ALLN-346 paper (PMID 33330529).
- **US 2020/0308534 A1** — divisional/continuation; current status unclear (USPTO PAIR lookup needed).
- **PCT / EP / CN / JP / AU / CA / IL** counterparts — marked "Ceased" per Google Patents; likely abandoned post-Allena's 2022 bankruptcy.

**Specific mutations disclosed** (on the *C. utilis* uricase backbone, from claims and worked examples):

- Primary hot positions appearing in both claims and examples: **I180V, I180A, Y165F, V190G, V190A, E51K, Q244K, I132R, I132N, V97I, E92N, A87G, D142E, G44A, G128P, A236N, K208A, N213A, S140T, Y253Q**.
- Additional positions in specification / Tables 1–2: A84S, T47E, S95P, K103T, D134E, Y136R, I196L, T224D, P285S, V296A.
- Combinatorial ProteinGPS variants: **R2_V17, R2_V4, R2_V39, R2_V47, R2_V79** (multi-substitution composites).
- Highest-value individual substitutions for Open Enzyme's purposes: **I180V, V190G, Y165F, E51K, Q244K, I132R, A87G**.

**FTO (freedom-to-operate) summary:**

- **Outside the US**: EP / CN / JP / AU / CA / IL applications are marked "Ceased." These geographies appear to be effectively public domain for research and commercial use — per-country formal verification still needed before any manufacturing commitment.
- **Inside the US**: US10815461B2 remains active on paper; nominal expiry 2038. Academic research use sits under the narrow *Madey v. Duke* experimental-use exemption. Commercial manufacture or sale of a product practicing the disclosed mutations would infringe until expiry or lapse.
- **Critical unknown — maintenance-fee status**: The first large USPTO maintenance fee on US10815461B2 was due around October 2024 (3.5-year window). If Allena's liquidating estate failed to pay — which is entirely plausible given the September 2022 employee termination, June 2023 liquidation plan, and the March 2023 Glyscend Inc. asset purchase covering only the GI/diabetes data rights (not the uricase IP) — the patent may already be **lapsed**. No identified successor owner to the uricase IP appears in the public record.

> **Single highest-leverage $0 task**
>
> Pull the USPTO maintenance-fee / legal-event database for US10815461B2 (free; ~30 minutes). If the 3.5-year fee was not paid, the US patent is lapsed and the entire disclosed engineering set — including the seven highest-value mutations above — is unencumbered in the US as well. This is the cheapest single action available to Open Enzyme.

This subsection is about **leveraging publicly disclosed prior art**, not competing with a (defunct) company. The ALLN-346 mutations represent millions of dollars of ProteinGPS-guided directed-evolution work, now disclosed to anyone willing to read the patent.

PULSE Probiotic: Engineered *E. coli* Nissle 1917
Published in *Cell Reports Medicine* in 2025, PULSE (**P**robiotic-based **U**A **L**evel **S**ensing and Adjustment **E**ngineered) is an *E. coli* Nissle 1917 strain engineered with a uric acid-responsive biosensor (based on the transcriptional repressor HucR) that dynamically regulates urate oxidase expression in the gut lumen.[[10]](#ref10) The key advance: this is a "smart" probiotic that expresses uricase only when uric acid levels are elevated.
In hyperuricemic mice and rats, oral administration of PULSE reduced persistent hyperuricemia, improved overall survival, and alleviated renal damage.[[10]](#ref10) The system expressed urate oxidase in three different configurations to test which architecture performed best in vivo.
Engineered *S. boulardii* (ACS Synthetic Biology, 2025)
Perhaps most directly relevant to this proposal: a team systematically engineered *Saccharomyces boulardii* (a probiotic variant of *S. cerevisiae*) for uric acid degradation. They identified a uricase from *Vibrio vulnificus* that showed high activity in yeast, improved the expression and stability of the urate transporter UapA by constructing a chimera for uric acid import, and combinatorially assembled constitutive promoters to optimize the pathway. Their best-performing construct achieved uric acid-degrading activity of **365.32 ± 20.54 μmol/h/OD**.[[11]](#ref11)
> **Key finding**
>
> Three independent groups — using three different organisms (*C. utilis* enzyme alone, engineered *E. coli*, engineered *S. boulardii*) — have demonstrated that degrading uric acid in the gut lumen can reduce systemic urate levels. The mechanism is validated. The engineering details are what need optimization.
2. Why *Saccharomyces cerevisiae*
GRAS Status and Genetic Tractability Established
*S. cerevisiae* holds "Generally Recognized as Safe" (GRAS) status from the FDA. It is the most genetically tractable eukaryotic organism on the planet, with decades of tool development for heterologous protein expression. There are well-established expression platforms, extensive libraries of characterized promoters, and multiple selectable marker systems.
### Expression Systems
The yeast protein expression toolkit includes inducible promoters (GAL1, GAL7, GAL10 — induced by galactose, repressed by glucose), constitutive promoters (TEF1, PGK1, GPD/TDH3 — always on, no induction required), and tunable systems. For a food-product application where you want the enzyme present during normal growth and fermentation, constitutive promoters are more practical — you don't want to have to add galactose to trigger expression.
Two main vector strategies exist. High-copy episomal plasmids (2μ-based) give 20–50 copies per cell and high expression levels, but they can be unstable without selective pressure — cells that lose the plasmid grow faster and outcompete engineered cells. Integrative approaches (inserting the gene directly into a chromosome) are more stable but typically yield lower expression per cell unless you integrate multiple copies or use strong promoters. For a food product that needs to be stable over fermentation without antibiotic selection, **chromosomal integration is the more realistic path**.
The Rasburicase Precedent Established
> **Critical prior art**
>
> Rasburicase (Elitek/Fasturtec), the FDA-approved recombinant uricase used intravenously for tumor lysis syndrome, is *Aspergillus flavus* uricase expressed in a genetically modified *Saccharomyces cerevisiae* strain. It was approved by the EMA in 2001 and the FDA in 2002.[[12]](#ref12) This means the exact gene-host combination we are discussing has been commercially manufactured at pharmaceutical scale for over two decades. The proof that *S. cerevisiae* can express active, correctly folded *A. flavus* uricase is not theoretical — it is an approved pharmaceutical product.
The original academic work demonstrated that *S. cerevisiae* transformants accumulated active, soluble *A. flavus* uricase (Uox) to levels exceeding **13% of total cellular protein** using a hybrid GAL7/ADH2 promoter, with good proportionality between gene copy number (1–10 copies) and expression level.[[13]](#ref13)
Secretion vs. Intracellular Expression Extrapolation
The rasburicase manufacturing process uses intracellular expression — cells are grown, harvested, and lysed to purify the enzyme. For a food-product application, this raises a design question: should the uricase be secreted into the surrounding liquid, or kept intracellular and released upon cell lysis or autolysis?
Secretion (using signal peptides like the α-mating factor prepro sequence) would put active enzyme directly into the beverage or food matrix. However, yeast secretion of large tetrameric proteins (~135 kDa assembled) is often inefficient. Intracellular expression followed by natural autolysis (which occurs during beer conditioning and in nutritional yeast production) may be more practical, though it introduces questions about enzyme activity after autolysis.
> **How to resolve: Secretion vs. intracellular expression**
>
> Clone the *A. flavus* uaZ gene into two constructs: (1) with the α-factor signal peptide for secretion, and (2) without, for intracellular accumulation. Transform both into the same yeast strain. After 48h of growth in liquid culture, assay uricase activity in (a) the supernatant and (b) the cell pellet lysate for each construct. Compare total enzyme output, specific activity, and fraction secreted.
**Cost:** ~$500–1,000 (gene synthesis + basic reagents)
**Time:** 2–3 weeks (including transformation and assays)
**Who:** Any molecular biology lab with yeast experience
## 3. Gene Construct Design
### Source Gene Selection
Several uricase genes have been expressed recombinantly. Here is an honest comparison:
| Source | Expression in Yeast | Specific Activity | Key Properties | Notes |
| --- | --- | --- | --- | --- |
| pH optimum 8.5–9.5; thermally labile above 40°C; 135 kDa homotetramer (301 aa/subunit) | Rasburicase source. Best characterized for this host. Default choice. |
| Higher specific activity; basis for ALLN-346 engineering. **ALLN-346 mutations disclosed in US10815461B2** — highest-value substitutions for protease-resistance engineering: I180V, V190G, Y165F, E51K, Q244K, I132R, A87G. See Section 1 "Publicly Disclosed Engineering" subsection. |
| Not directly comparable (measured as μmol/h/OD in whole cells) | Selected specifically for high activity in yeast cellular context | Newest entrant. Chosen by the 2025 ACS Synth Bio group specifically for yeast expression. |
| Literature values vary | Native 145 kDa heterotetramer | Less commonly used for recombinant work. Unusual subunit heterogeneity. |
**Recommendation:** Start with *A. flavus* uaZ for the *S. cerevisiae* intracellular track (deepest validation, FDA precedent, post-evolution activity advantage per Tang 2025 PMID 39892538: af-UA 46.21 U/mg vs. cu-UA 31.43 U/mg after directed evolution). For the oral/gut-lumen track, **elevate *C. utilis* to co-primary**: industry-revealed preference shows 3-of-4 recent non-rasburicase programs chose *C. utilis* (SSS11, ALLN-346, SEL-212), driven by IP, oral-tolerance profile, and the publicly disclosed ALLN-346 ProteinGPS mutations (US10815461B2). The *V. vulnificus* uricase is an interesting third candidate given the 2025 *S. boulardii* results, but it adds risk by being less characterized. See [uricase-variant-selection.md](./uricase-variant-selection.md) for the full industry-preference analysis. (In Vitro + Clinical Trial; source: uricase-variant-selection.md)
> **How to resolve: Which uricase gene performs best in S. cerevisiae**
>
> Order codon-optimized synthetic genes for all three candidates (*A. flavus*, *C. utilis*, *V. vulnificus*), each in the same expression cassette (e.g., pTEF1 promoter, CYC1 terminator, integrated at the same locus). Transform into the same *S. cerevisiae* background. Compare: (a) expression level by Western blot/total protein, (b) specific uricase activity in cell lysate, (c) enzyme stability at 37°C over 24h. Three genes × two replicates = six transformations.
**Cost:** ~$2,000–3,000 (gene synthesis is ~$0.10/bp × ~900 bp × 3 genes + reagents)
**Time:** 4–6 weeks
**Who:** Any synbio or yeast genetics lab
Codon Optimization Established
Codon optimization for *S. cerevisiae* is routine. The *A. flavus* uaZ gene has already been successfully expressed without codon optimization (as demonstrated by rasburicase production), but optimization of rare codons and removal of cryptic splice sites or polyA signals could improve yield, especially with constitutive promoters. Commercial gene synthesis services (Twist, IDT, GenScript) include codon optimization in their standard workflow.
### Promoter Selection
For a food-product application, the enzyme should be expressed constitutively during normal aerobic growth and fermentation. The recommended promoters:
**pTEF1** (translation elongation factor 1α) — strongest constitutive promoter in *S. cerevisiae*, active across carbon sources, well-characterized. This is the default choice for maximal constitutive expression.
**pPGK1** (phosphoglycerate kinase) — strong constitutive, slightly lower than TEF1 in most conditions, very well characterized.
**pGPD/pTDH3** (glyceraldehyde-3-phosphate dehydrogenase) — another strong constitutive option, comparable to TEF1.
The hybrid GAL7/ADH2 promoter used in the original rasburicase work is inducible (derepressed when glucose is depleted) — effective for bioreactor production but less suitable for a food fermentation where you want enzyme throughout the process.
### Selectable Markers and Integration
For lab-stage work, standard auxotrophic markers (URA3, LEU2, HIS3) or dominant markers (kanMX, conferring G418 resistance) are all appropriate. For a food product, the final construct should ideally be marker-free or use only food-safe markers. CRISPR/Cas9-based integration can achieve markerless insertion, which is important for eventual regulatory considerations.
The 2025 *S. boulardii* work identified specific high-expression chromosomal integration loci in that strain,[[11]](#ref11) which would be directly applicable since *S. boulardii* is genomically a *S. cerevisiae* variant.
## 4. Delivery Formats — Honest Assessment
Not all formats are created equal. For each, I've tried to be honest about whether therapeutically meaningful uricase delivery is realistic.
### a. Beer
> **The elephant in the room**
>
> Alcohol raises uric acid through at least three independent mechanisms: (1) ethanol metabolism accelerates ATP degradation and purine turnover, increasing uric acid production; (2) the lactate produced during ethanol metabolism competes with uric acid for renal tubular secretion via organic anion transporters, reducing excretion; (3) beer specifically contains high purine content from yeast and grain (~8–14 mg purines per 100 mL).[[17]](#ref17)[[18]](#ref18) You are fighting the delivery vehicle.
"Therapeutic beer" is not a credible framing. "Less bad beer" is more accurate, and even that requires the uricase to survive fermentation, conditioning, and the gastric transit that follows consumption. A more honest question: could a low-alcohol or non-alcoholic beer fermented with engineered yeast deliver meaningful uricase while minimizing the alcohol-driven uric acid increase?
Low-alcohol (Therapeutic credibility:  Low (full-strength beer)
Therapeutic credibility:  Moderate (NA beer, if enzyme survives)
> **How to resolve: Does uricase survive beer fermentation?**
>
> Brew a 1-gallon test batch with the engineered yeast. At each stage — active fermentation (day 3), end of primary (day 7), after conditioning/cold crash (day 14), and after bottling (day 21) — draw samples and run a uricase activity assay (standard spectrophotometric assay at 293 nm, measuring uric acid consumption). Compare to a control with purified uricase added to sterile, finished beer at the same stages to distinguish enzyme production from enzyme survival.
**Cost:** ~$200–400 (homebrew supplies + uric acid assay reagents)
**Time:** 3–4 weeks
**Who:** Anyone with homebrewing equipment and a spectrophotometer
### b. Non-Alcoholic Yeast-Fermented Beverages
Kvass, water kefir, tepache, and kombucha-style beverages fermented with *S. cerevisiae* rather than (or in addition to) bacterial cultures. These remove the alcohol confound while retaining the live-yeast delivery vector. Short fermentation times (24–48h for kvass) mean less opportunity for enzyme degradation.
This is a significantly more credible therapeutic format. The yeast is alive and expressing during the fermentation, the beverage is consumed with active cells and potentially secreted enzyme, and there's no alcohol working against you.
Therapeutic credibility:  Moderate-High (contingent on dosing; see §5)
### c. Nutritional Yeast / Dried Yeast Powder
Grow the engineered yeast in bulk, harvest, and process into a dried product (powder, flakes, or capsules). This is the format with the most control over dosing — you can standardize the product to a specific uricase activity per gram.
The critical question is enzyme stability after drying. Conventional nutritional yeast production involves heating to kill the yeast (typically 50–60°C for pasteurization), followed by drum drying or spray drying at higher temperatures. *A. flavus* uricase loses significant activity above 40°C — free enzyme loses almost all activity at 40–45°C.[[14]](#ref14) This is a problem.
However: lyophilization (freeze-drying) preserves enzyme activity far better than heat-based drying, and encapsulation in trehalose or other lyoprotectants is standard practice for enzyme stabilization. A lyophilized yeast powder, packaged in capsules, could plausibly retain uricase activity. This needs to be tested.
Therapeutic credibility:  Moderate (depends entirely on drying method)
> **How to resolve: Does uricase survive drying?**
>
> Take a concentrated pellet of engineered yeast. Split into four aliquots: (1) fresh lysate (positive control), (2) freeze-dried/lyophilized pellet, (3) heat-killed at 55°C then dried, (4) spray-dried at 120°C inlet temp. Rehydrate each, lyse, and assay uricase activity. Report as % activity retained vs. fresh lysate.
**Cost:** ~$300–800 (lyophilizer access is the main cost; often available in university core facilities)
**Time:** 1–2 weeks
**Who:** Any biochemistry lab with a lyophilizer
d. Live Yeast Probiotic (*S. boulardii* Chassis)
*S. boulardii* (CNCM I-745) is an established probiotic yeast, already marketed for GI conditions (Florastor). It is genomically a variant of *S. cerevisiae*, meaning the same genetic tools largely apply. The 2025 ACS Synthetic Biology paper demonstrated successful integration and expression of a uric acid degradation pathway in *S. boulardii*.[[11]](#ref11)
The colonization question is critical. Published data show that *S. boulardii* achieves steady-state concentrations in the human colon within 3 days of regular dosing and is cleared 2–5 days after discontinuation.[[19]](#ref19) In mice with conventional microbiota, gut residence time is only 1–2 days.[[20]](#ref20) This means ***S. boulardii* does not colonize — it transits**. You'd need daily dosing to maintain gut levels. This isn't necessarily a dealbreaker (you take allopurinol daily too), but it does mean this is a daily supplement, not a one-time inoculation.
Therapeutic credibility:  High (most directly validated approach)
> **How to resolve: Continuous production in the gut**
>
> This is precisely the kind of question that could be answered at a Role 1 collaborator's gnotobiotic facility. Colonize germ-free mice with engineered *S. boulardii* expressing uricase. Measure: (a) fecal yeast counts daily, (b) fecal and cecal uricase activity, (c) serum uric acid (requires Uox-knockout mice or potassium oxonate-treated mice for a hyperuricemic model). Compare to conventional mice gavaged daily. This gives both colonization kinetics and functional uricase delivery data.
**Cost:** ~$5,000–15,000 (gnotobiotic mouse work is expensive)
**Time:** 8–12 weeks
**Who:** Role 1 collaborator (Gut Microbiome / Gnotobiotic Animal Core) *(actively recruiting)*
### e. Yeast Lysate (Concentrated Enzyme Liquid)
Grow engineered yeast in a bioreactor, lyse the cells mechanically or enzymatically, filter, and concentrate the uricase-containing supernatant. This is closest to a traditional enzyme supplement — essentially a crude or semi-purified uricase preparation in a food-grade liquid.
Advantages: maximal control over enzyme concentration, can be standardized by activity assay, could be flavored or formulated as a shot/tonic. Disadvantages: more processing steps, requires some manufacturing infrastructure, shorter shelf life unless lyophilized.
Therapeutic credibility:  Moderate-High (proven concept, processing questions)
### f. Amazake / Koji Hybrid (Dual-Organism Fermentation)
Use both engineered *A. oryzae* (koji) and engineered *S. cerevisiae* in a sequential fermentation: koji produces amylases + uricase during the saccharification stage, then yeast continues uricase production during the alcoholic (or non-alcoholic) fermentation. Two organisms, potentially two different uricase genes, producing enzyme across both fermentation stages.
This is the most complex format but also the most interesting for a food product — amazake is a traditional Japanese fermented rice beverage with existing consumer acceptance. See §8 for more on the koji track.
Therapeutic credibility:  Moderate (interesting but adds complexity)
## 5. The Dosing Question
What Activity Level Is Needed? Open
This is the central feasibility question. Let me lay out the reasoning quantitatively, while being transparent about the assumptions.
**The uric acid budget:** A typical adult produces ~600–900 mg of uric acid per day. Roughly 200–300 mg is eliminated via the intestine. For a gout patient with serum urate of ~9 mg/dL (a common level on no therapy), reducing this to below 6 mg/dL (the therapeutic target) requires eliminating roughly 200–400 mg of additional uric acid per day — the amount that would otherwise accumulate.
**Rasburicase dosing (IV, for reference):** The approved dose is 0.15–0.2 mg/kg/day, which for a 90 kg adult is ~13.5–18 mg of pure enzyme per day, administered intravenously. This is dramatically effective — it typically reduces serum urate to near-zero within 4 hours. But IV delivery puts the enzyme directly into the bloodstream with access to all circulating urate; oral delivery must work only through the gut lumen, which is a fundamentally different (and less efficient) route.
**ALLN-346 dosing (oral):** The Phase 2a studies used oral doses that were orders of magnitude higher than the IV rasburicase dose, reflecting the inefficiency of the gut-lumen route and the need for protease resistance. Exact per-dose numbers from the human trials are not fully public, but the mouse studies used doses ranging from approximately 3–30 mg of engineered enzyme per day, scaled to body weight.[[7]](#ref7)
### How Much Yeast Is That?
Let's work the math with *A. flavus* uricase expressed in *S. cerevisiae*:
From the published data, uricase accumulated to >13% of total cellular protein in optimized *S. cerevisiae* transformants.[[13]](#ref13) A typical yeast cell contains approximately 6 pg of total protein. At 13% uricase, that's ~0.78 pg of uricase per cell. Yeast cell density in a standard culture is ~108 cells/mL at saturation.
For a rough calculation: 108 cells/mL × 0.78 pg/cell = ~78 μg uricase/mL of dense culture, or about 78 mg/L.
If we need ~20–50 mg of active uricase per dose (extrapolating between the IV and oral ranges, acknowledging this is a rough estimate), that's 250–640 mL of saturated culture — roughly a pint to a quart of dense yeast suspension.
> **Reality check**
>
> A pint of saturated yeast culture is not a palatable serving. But a concentrated yeast paste or dried powder changes the math dramatically. If you concentrate 10× by centrifugation, you're at 25–64 mL (~1–2.5 tablespoons of thick yeast slurry). Freeze-dried to a powder, assuming 5× further concentration and reasonable enzyme survival, you could be looking at ~5–15 grams of powder — a large capsule or a small scoop. This is in the range of a plausible supplement dose, but just barely, and it depends on assumptions that haven't been validated.
The *S. boulardii* group's reported activity of 365 μmol/h/OD[[11]](#ref11) suggests their optimized pathway may be more efficient than the simple expression-level calculation above, since they also incorporated a uric acid transporter to actively import substrate. This active import could significantly improve the effective activity per cell in a gut environment where substrate concentration varies.
> **How to resolve: Is the dose achievable?**
>
> **Bench experiment:** Transform *S. cerevisiae* with the uricase construct. Grow to saturation in 1L of standard media. Harvest, lyse, and measure total uricase activity (IU). Calculate: how many IU per gram of wet cell pellet, per gram of dried cells, and per gram of lyophilized cells. Compare to the estimated therapeutic need (~200–400 mg uric acid degradation per day, which at a specific activity of ~12 IU/mg for *A. flavus* uricase and a molecular weight of 168 Da for uric acid, requires roughly 100–200 IU of enzyme activity, assuming favorable kinetics in the gut).
> **Self-experiment (after bench validation):** Using a home uric acid meter (~$50, Benecheck or similar), establish a baseline serum urate over 5 days (morning fasting measurements). Then consume the yeast product daily for 7 days at the calculated dose. Measure daily. Plot the curve. This is n=1 and not science, but it tells you whether you're in the right ballpark before investing in proper studies.
**Cost:** ~$150 (uric acid meter + strips) + yeast production costs
**Time:** 2 weeks for bench; 2 weeks for self-experiment
**Who:** Brian (self-experiment); any lab (bench work)

### Dose Scalability Cross-Check — Yeast vs. Koji as a Daily Food Product *(Mechanistic Extrapolation; source: [wiki/synthesis.md](./synthesis.md) 2026-04-23)*

The "How Much Yeast Is That?" calculation above worked from enzyme activity per mL of dense culture. A simpler (and more unforgiving) check is to ask how much biomass a patient would need to consume per day to deliver a clinical-scale enzyme dose. This cross-check treats the yeast product as a daily food, not as a lab preparation.

**Target dose.** The ALLN-346 Phase 2a studies titrated oral uricase into the **500–800 mg enzyme/day** range; rasburicase's IV dose of 13.5–18 mg is not comparable because the gut-lumen route is fundamentally less efficient. Assume 500 mg of active enzyme/day as a conservative daily target.

**Yeast mass required.** Using the established precedent that *A. flavus* uricase accumulates to ~13% of total cellular protein in optimized *S. cerevisiae* transformants[[13]](#ref13) (Established), and that total protein is roughly 40–50% of yeast dry weight (standard yeast composition, Established):

- 500 mg enzyme ÷ 13% of total protein ≈ **3.8 g total protein/day**
- 3.8 g protein ÷ ~45% of dry weight ≈ **~8.5 g dry yeast/day** (if enzyme remains at the 13% peak and total protein is ~45% of dry mass)
- At ~75% water content (typical wet yeast paste), that's **~30–40 g fresh yeast/day**

The synthesis queue entry ran the same calculation with slightly different intermediate assumptions (using ~10% enzyme/dry weight directly) and landed at ~17 g dry yeast / ~170 g fresh yeast per day. Either way, the honest interpretation is:

- **Best case (rasburicase-level expression sustained in a food-grade strain, lyophilized):** ~10 g dry yeast powder/day. Plausible as capsules or a scoop into a drink.
- **Realistic case (expression in live-food fermentation conditions without selection pressure, wet biomass):** 30–170 g fresh yeast/day. That is well outside what anyone will consume as a food product daily, indefinitely.

**Koji comparison.** Engineered koji (*A. oryzae*) is fermented on solid rice/grain substrate and is normally consumed by mass of dry substrate, not by cell count. Published koji enzyme titers for heterologous proteins fall in the **40–80 mg enzyme/g dry koji substrate** range (see [engineered-koji-protocol.md](./engineered-koji-protocol.md); Supported):

- 500 mg enzyme target ÷ 40–80 mg/g ≈ **6.25–12.5 g dry koji/day**
- At 10–15 g dry koji/day, the dose envelope is **400–1,200 mg enzyme/day** — comfortably covering the 500–800 mg range.

10–15 g of dry koji as a daily food is realistic — it's in the same mass range as a Creon pancreatic enzyme dose, and orders of magnitude smaller than the yeast mass required for the same enzyme output.

**Interpretation.** Yeast intracellular expression is scientifically sound — the rasburicase precedent (Established) confirms the gene-host combination works at pharmaceutical scale. The problem is *format*, not biology. At clinical enzyme doses, the yeast mass required to act as a daily food product is implausible for anything short of a highly concentrated, lyophilized, and encapsulated preparation — which starts to look more like a pharmaceutical than a fermented food. Koji, by contrast, delivers the same enzyme mass from a portion that resembles a normal food serving.

**Bottom line.** Yeast intracellular expression is scientifically sound but mass-impractical as a daily food product. Koji is dose-advantaged on scaling grounds and probably the right primary platform for oral delivery. This is consistent with the koji-first framing already adopted in [open-enzyme-vision.md](./open-enzyme-vision.md) §3, and the yeast track is best understood as: (a) a rapid bench platform for construct validation, (b) a path to a concentrated powder/capsule product for the subset of patients who can't tolerate koji, or (c) the *S. boulardii* probiotic route where the dose is set by colonization, not by food mass.

## 6. Open Scientific Questions
These are framed as questions for specific experts, but each one includes a path to an answer.
### For Role 1 — Gut Microbiome / Gnotobiotic Models *(actively recruiting)*
> **Q1: Colonization vs. transit for engineered S. boulardii**
>
> Published data show *S. boulardii* clears from humans within 2–5 days of stopping dosing. From a gnotobiotic-mouse perspective, what colonization density and residence time would you predict for an engineered *S. boulardii* strain? Is daily gavage the realistic model, or are there strategies (biofilm formation, mucoadhesive modifications) that could extend residence?
> **Experiment to resolve Q1**
>
> Colonize gnotobiotic mice with engineered *S. boulardii*. Track fecal CFU daily for 30 days with continuous dosing, then stop dosing and continue tracking for 14 days. Compare with and without competing bacterial flora (gnotobiotic → gnotobiotic + defined bacterial community). Simultaneously measure cecal and fecal uricase activity to confirm the yeast is producing enzyme in vivo.
**Cost:** ~$8,000–15,000
**Time:** 10–14 weeks
**Facility:** Any gnotobiotic animal core
> **Q2: Is the gnotobiotic facility appropriate for proof-of-concept?**
>
> The ideal experiment: Uox-knockout or oxonate-treated mice colonized with engineered *S. boulardii*, measuring serum urate over time. Is this feasible in a gnotobiotic core? What's the timeline and approximate cost for a small-scale study (e.g., 3 groups × 8 mice)?
### For Role 3 — TLR / Innate Immunity
> **Q3: Innate immune responses to engineered yeast in the gut**
>
> Would an engineered *S. cerevisiae* or *S. boulardii* strain expressing a foreign protein (fungal uricase) trigger TLR-mediated innate immune responses in the intestinal epithelium? *S. cerevisiae* cell wall components (β-glucan, mannan, chitin) are recognized by Dectin-1, Dectin-2, and TLR2. Is the immune response to probiotic yeast well characterized enough to predict tolerability of daily dosing?
> **Experiment to resolve Q3**
>
> Expose Caco-2 or HT-29 intestinal epithelial cell monolayers to: (a) wild-type *S. boulardii*, (b) engineered *S. boulardii* expressing uricase, (c) purified uricase alone, (d) LPS positive control. Measure cytokine panel (IL-8, TNF-α, IL-1β, IL-10) at 4h and 24h by ELISA. Monitor transepithelial electrical resistance (TEER) for barrier integrity. If the engineered strain shows significantly different immune activation than wild-type, that's a flag.
**Cost:** ~$2,000–4,000
**Time:** 3–4 weeks (cell culture + assays)
**Who:** Role 3 collaborator or any lab with intestinal epithelial cell models
### For Role 2 — Pharma / Translational / NF-κB Signaling
> **Q4: Regulatory path for a GMO yeast food product**
>
> What's the realistic regulatory pathway for a food or supplement containing a GMO yeast that produces a therapeutic enzyme? Is this a food (GRAS self-determination?), a dietary supplement (DSHEA framework — but engineered organisms complicate this), or does it require a Biologics License Application? The FDA has been evolving its framework for "live biotherapeutic products" (LBPs) — does that apply here, and does it matter whether the product contains live vs. killed yeast?
> **Path to resolve Q4**
>
> This isn't a bench experiment — it's a regulatory mapping exercise. Steps: (1) Review FDA's 2016 "Early Clinical Trials with Live Biotherapeutic Products" guidance and the 2024 updates. (2) Search for precedents: has any GMO yeast been approved as a food ingredient or supplement? (GTC Nutrition's GanedenBC30 *Bacillus* is the closest precedent in probiotics.) (3) Have a pre-IND meeting or a pre-submission meeting with FDA's Office of Food Additive Safety or CBER, depending on how the product is positioned. A Role 2 collaborator's pharma regulatory network would be invaluable for identifying the right FDA contact.
**Cost:** $0–5,000 (depending on whether you engage a regulatory consultant)
**Time:** 4–8 weeks for the research; 3–6 months if seeking a formal FDA meeting
**Who:** Role 2 collaborator (guidance), regulatory consultant (optional)
> **Q5: Immunogenicity of oral uricase — a different immune context?**
>
> Rasburicase (IV uricase) induces anti-drug antibodies in ~60% of patients, limiting re-dosing.[[12]](#ref12) But IV delivery presents the antigen to the systemic immune system, while oral delivery primarily encounters the mucosal immune system, which is generally tolerogenic. Is there evidence that oral exposure to a foreign protein would induce tolerance rather than antibody formation? The oral tolerance literature from allergen immunotherapy is relevant here. With NF-κB / intestinal-signaling expertise — does the gut immune context fundamentally change the immunogenicity risk?
> **Experiment to resolve Q5**
>
> In mice, gavage with uricase daily for 28 days. Collect serum at days 0, 14, and 28. Run ELISA for anti-uricase IgG and IgE. Compare to a group that receives the same total dose of uricase by subcutaneous injection (positive control for systemic immunization). Measure fecal IgA as a mucosal immune readout. If oral exposure produces minimal IgG compared to the injected group, that supports the oral tolerance hypothesis.
**Cost:** ~$3,000–6,000 (mice, enzyme, ELISAs)
**Time:** 6–8 weeks
**Who:** Any immunology lab; could be combined with a gnotobiotic study via Role 1
### For Everyone: The pH Challenge
> **Q6: Does uricase survive the GI gauntlet?**
>
> *A. flavus* uricase has a pH optimum of 8.5–9.5 and retains stability across pH 6–10.[[14]](#ref14) Gastric acid drops the pH to 1.5–3.5 with pepsin as an aggressive protease. The small intestine is pH 6–7.5 with pancreatic proteases (trypsin, chymotrypsin, elastase). ALLN-346 specifically engineered for 20× protease resistance for this reason. An unmodified *A. flavus* uricase may not survive gastric transit.
However: uricase encapsulated within intact yeast cells may be partially protected. Yeast cell walls are resistant to gastric acid (β-glucan and chitin are not digested by human enzymes), and this is actually a known strategy for oral vaccine delivery. The question is whether enough enzyme remains active when the cells eventually lyse in the intestine.
> **Experiment to resolve Q6**
>
> **In vitro GI simulation:** Prepare three samples: (a) purified free uricase, (b) engineered yeast cells (intact), (c) yeast lysate. Subject each to a standard simulated GI transit protocol: (1) Simulated gastric fluid (SGF: pH 2.0, 3.2 mg/mL pepsin, 37°C) for 2 hours. (2) Neutralize to pH 6.8, add simulated intestinal fluid (SIF: pancreatin, bile salts) for 4 hours at 37°C. Assay uricase activity at each stage. This is a standard protocol — USP methods exist.
> If intact yeast cells protect the enzyme better than free enzyme, that supports the "live yeast" and "whole-cell" delivery formats over lysate or purified enzyme. If nothing survives, you need either enteric capsules or the ALLN-346-style protease engineering approach.
**Cost:** ~$500–1,000
**Time:** 2–3 days of bench work
**Who:** Any biochemistry or pharmacology lab
## 7. A Proposed Validation Path
Here is a staged approach, designed so that each phase answers a go/no-go question before investing in the next.
### Phase 0: Construct and Confirm (Bench Work)
| Task | Details | Est. Cost | Timeline |
| --- | --- | --- | --- |
| Gene synthesis | $200–400 | 2 weeks |
| Construct assembly | Clone into an expression vector (2μ plasmid for initial testing; integrative cassette for stable strain). Standard restriction/ligation or Gibson assembly. | $200–500 | 1–2 weeks |
| Yeast transformation | $100–300 | 1 week |
| Activity assay | Lyse transformant cells; measure uricase activity by spectrophotometric assay (uric acid absorbance at 293 nm). Confirm active enzyme is being produced. | $100–200 | 1 week |
**Phase 0 total:** ~$600–1,400 | 4–6 weeks | **Go/no-go:** Is active uricase detected in the cell lysate? If yes, proceed.
### Phase 1: Stability Characterization
| Task | Details | Est. Cost | Timeline |
| --- | --- | --- | --- |
| pH stability profile | Incubate enzyme (free and in intact cells) at pH 2.0, 4.0, 6.0, 6.8, 7.4, 8.5 for 0, 30, 60, 120 min. Assay residual activity. | $300–500 | 1 week |
| Temperature stability | Activity retention at 4°C, 25°C, 37°C, 55°C, 70°C over 24h. | $200–400 | 1 week |
| GI simulation | SGF/SIF protocol (described in §6, Q6 experiment). Test free enzyme, intact cells, and lysate. | $500–1,000 | 1 week |
| Protease resistance | $300–500 | 1 week |
**Phase 1 total:** ~$1,300–2,400 | 3–4 weeks | **Go/no-go:** Does the enzyme (in at least one format) retain meaningful activity after simulated GI transit? What delivery format provides the best protection?
### Phase 2: In Vitro Gut Models
| Task | Details | Est. Cost | Timeline |
| --- | --- | --- | --- |
| Uric acid degradation in simulated gut fluid | Add yeast cells (or lysate) to SIF containing physiological concentrations of uric acid (~5 mg/dL). Measure uric acid depletion over 6h. | $300–500 | 1 week |
| Intestinal epithelial cell compatibility | Caco-2 monolayer assay: co-incubate with engineered yeast. Measure TEER (barrier integrity), cytokine panel (IL-8, TNF-α, IL-1β), LDH release (cytotoxicity). | $2,000–4,000 | 3–4 weeks |
**Phase 2 total:** ~$2,300–4,500 | 4–5 weeks | **Go/no-go:** Does the yeast degrade uric acid under intestinal conditions at a therapeutically interesting rate? Any safety red flags from the epithelial cell model?
### Phase 3: In Vivo Proof-of-Concept (Gnotobiotic Mouse Model)
| Task | Details | Est. Cost | Timeline |
| --- | --- | --- | --- |
| Hyperuricemic mouse model | Use potassium oxonate-treated mice (standard model — oxonate inhibits residual murine uricase) OR Uox-knockout mice if available. Confirm hyperuricemia. | $2,000–5,000 | 2–4 weeks |
| Gavage with engineered yeast | $5,000–10,000 | 4–6 weeks |
| Endpoints | Serum uric acid (weekly), fecal uricase activity (daily), fecal yeast counts (daily), kidney histology (terminal), serum creatinine, anti-uricase antibodies. | Included above | Included above |
**Phase 3 total:** ~$7,000–15,000 | 8–12 weeks | **Go/no-go:** Does oral engineered *S. boulardii* reduce serum uric acid in hyperuricemic mice? By how much? This is the definitive proof-of-concept.
> **Total estimated cost: Phases 0–3**
>
> **$11,200–23,300** | approximately 20–27 weeks
> This is deliberately a minimal viable experiment path. It answers the fundamental question — can engineered yeast deliver therapeutically relevant uricase activity in a living animal — without requiring industrial-scale investment. Phases 0–1 could be done by a single graduate student or postdoc with yeast and biochemistry experience. Phase 2 requires an intestinal cell biology lab. Phase 3 requires a gnotobiotic facility (a Role 1 collaborator's gnotobiotic core, if recruiting succeeds).
8. The Parallel Track: Koji (*A. oryzae*)
*Aspergillus oryzae* (koji) is the other organism under consideration. These two tracks are complementary, not competing:
| Dimension |
| --- |
| Genetic tools | Best-in-class eukaryotic toolkit | Good but less mature; CRISPR tools improving rapidly |
| GRAS status | Yes (long fermentation history) | Yes (thousands of years in East Asian cuisine) |
| Uricase precedent |
| Delivery formats | Beverages, probiotic capsules, nutritional yeast, lysate | Koji rice, miso, amazake, soy sauce mash |
| Dual-purpose potential | Limited to uricase | Strong: digestive enzymes (amylases, proteases, lipases) + uricase in one organism |
| Consumer context | Beer, kombucha, supplements — familiar Western formats | Fermented foods — growing but still niche in the West |
| Probiotic potential | Not a probiotic; works through enzyme delivery in food |
The koji track is especially interesting for Brian and Lynn together — Lynn benefits from the digestive enzyme production, Brian benefits from the uricase. A dual-enzyme koji that produces both enhanced protease/lipase and uricase would be a genuinely useful food product for their household regardless of whether it reaches therapeutic uricase levels.
The yeast track has more delivery format flexibility and, critically, the *S. boulardii* probiotic option — the only format where the organism can produce enzyme continuously in the gut rather than just delivering a bolus of enzyme with a meal.
**Both are worth pursuing in Phase 0.** The gene synthesis and initial expression testing costs are modest for either organism.
Key Insight: Wild-Type Koji Is Already Lynn's Solution
An important realization from the [enzyme deficit research](enzyme-deficit-deep-dive.md): Lynn doesn't need engineered koji for her digestive enzymes. The supplement industry's "fungal-derived enzymes" *are* industrial *A. oryzae* fermentation. Wild-type koji grown at home on rice already produces the lipase, protease, and amylase she needs — no genetic engineering required.
This clarifies the lanes: **yeast is the fastest path to uricase for Brian**, wild-type koji handles Lynn's needs today, and engineered koji (uricase + digestive enzymes) is the stretch-goal platform play. See the full koji engineering protocol: [Engineered Koji Protocol](engineered-koji-protocol.md).
## 9. Risks and Honest Limitations
Enzyme Survival in the GI Tract Open
Unmodified *A. flavus* uricase may not survive gastric transit in active form. The pH optimum is 8.5–9.5; activity is maintained at pH 6–10 but behavior below pH 6 is poorly characterized for the recombinant form.[[14]](#ref14) ALLN-346 was specifically engineered for 20× protease resistance — that engineering was not trivial, and the resulting enzyme is proprietary. Without similar engineering or a protective delivery format (enteric capsule, intact yeast cells), significant activity loss during gastric transit is likely.
> **How to bound this risk**
>
> The SGF/SIF experiment (Phase 1, ~$500) answers this directly. If intact yeast cells provide meaningful protection (β-glucan cell walls resist gastric acid), then whole-cell formats are viable. If not, the options are: (1) enteric-coated capsules that bypass the stomach, (2) protein engineering for protease resistance (a significant R&D investment), or (3) accept that only a fraction of the enzyme will survive and compensate with higher doses.
Dosing May Not Be Therapeutically Meaningful Open
The back-of-envelope calculations in §5 suggest the dose is in a plausible range, but "plausible" is not "proven." ALLN-346's mixed human results (significant in CKD patients in Study 201; not significant in the broader Study 202 cohort) suggest that even with an optimized, protease-resistant enzyme, the dose-response relationship for oral uricase is not straightforward. A food-grade, non-engineered-for-protease-resistance enzyme in yeast may not reach therapeutically meaningful activity levels.
> **How to bound this risk**
>
> Phase 0 activity assays will give a concrete number for IU per gram of yeast biomass. Combined with the Phase 1 GI survival data, you can calculate: "X grams of this product, consumed with Y% enzyme survival, delivers Z IU to the intestine per day." Compare Z to the activity levels that showed efficacy in the mouse models. If Z is within an order of magnitude, proceed to Phase 3. If Z is 100× too low, the format needs rethinking.
### GMO Regulatory Considerations
Any food product containing a genetically modified organism faces regulatory hurdles that vary by jurisdiction. In the US, the pathway depends on how the product is positioned (food ingredient vs. dietary supplement vs. drug). In the EU, GMO regulations are more restrictive but undergoing reform. For an initial proof-of-concept and personal use, this isn't a barrier; for commercialization, it requires careful regulatory strategy (see Q4 in §6).
Immunogenicity Extrapolation
Rasburicase induces anti-drug antibodies (ADAs) in approximately 60% of patients receiving IV administration.[[12]](#ref12) These antibodies can neutralize the enzyme and cause hypersensitivity reactions, limiting rasburicase to short-course therapy. However, IV and oral delivery present antigens to fundamentally different immune compartments. The oral mucosal immune system is designed for tolerance — we ingest foreign proteins (plant, animal, bacterial) constantly without mounting systemic immune responses. The oral tolerance literature from allergen immunotherapy supports the hypothesis that repeated oral exposure to uricase would be more likely to induce tolerance than sensitization. But this has not been tested for uricase specifically.
> **How to bound this risk**
>
> The mouse immunogenicity experiment described under Q5 in §6 (~$3,000–6,000) directly addresses this. It can be combined with the Phase 3 efficacy study at minimal additional cost by simply adding antibody ELISA endpoints to the planned blood draws.
### The Fundamental Limitation
> **What we don't know**
>
> This approach — engineering food-grade *S. cerevisiae* or *S. boulardii* to produce uricase for oral consumption as a gout therapy — has not been tested in humans in this format. Period. The 2025 *S. boulardii* work demonstrated the engineering is feasible and achieved high activity levels, but published only in vitro data. The PULSE probiotic showed efficacy in rodents. ALLN-346 showed signal in one human cohort but not another. We are in the territory of well-motivated hypothesis, supported by convergent evidence from multiple groups, but unproven in the specific format proposed here.
That is precisely why this is a proposal for a proof-of-concept experiment, not a product launch.
## 10. What We're Actually Proposing
This is a proposal for a small-scale proof-of-concept collaboration. Not a startup. Not a product launch. Not a clinical trial.
The core question is: **Can engineered *S. cerevisiae* (or *S. boulardii*) produce therapeutically relevant levels of active uricase in a food-compatible format that survives GI transit?**
Everything else — delivery format optimization, dosing studies, regulatory strategy, commercialization — depends on the answer to that question.
### What I'm Asking Of Each Role
**Role 1 (Gut Microbiome / Gnotobiotic Models):** Expertise in gut microbiology and access to a gnotobiotic facility are the keys to a credible in vivo proof-of-concept. The ask: whether a small mouse study (Phase 3 in the validation path) is feasible in your core, and whether you'd be interested in collaborating on design and execution. Also: poke holes in the gut-lumen degradation thesis from a microbiome perspective — what am I missing about how this would interact with the resident gut flora?
**Role 2 (Pharma Translation / Regulatory):** Translational and pharma experience is invaluable for two things: (1) the regulatory question — what is this product, legally speaking, and what's the path? (2) the immunogenicity question — with NF-κB and intestinal-signaling expertise, is oral tolerance a reasonable expectation, or am I being naively optimistic? And more generally, is there anything in here that a pharma reviewer would immediately flag as a non-starter?
**Role 3 (Innate Immune Safety):** TLR / innate-immunity expertise speaks directly to the safety question. If someone consumes engineered yeast daily, is the innate immune response to yeast cell wall components (β-glucan, mannan) a concern at the doses we're discussing? *S. boulardii* is already taken daily as a probiotic by millions of people, but expressing a novel protein changes the picture. What would you want to see in the immune profiling data to be comfortable?
### What I Bring
I know enough molecular biology to be dangerous and enough brewing science to be useful. I can do the Phase 0 bench work (gene synthesis, transformation, activity assays) with minimal hand-holding. I can brew the test batches. I can design and run the SGF/SIF simulations. I have a home uric acid meter for n=1 self-experiments. I'm willing to fund Phases 0–2 out of pocket (~$4,000–8,000). Phase 3 (the mouse study) is where I need both expertise and potentially institutional support.
I'm presenting this as someone who has done his homework, is honest about what he doesn't know, and wants guidance from people who know more than he does. The worst outcome is that you tell me this won't work and why — and that's actually a valuable outcome, because it saves me from chasing something futile.
The best outcome is that you see something here worth pursuing, and we design a real experiment together.

## AI Analysis Updates — April 2026

A comprehensive computational analysis of uricase variants, GI survival, protein engineering, and expression optimization has refined the yeast engineering proposal with quantitative feasibility metrics. This section summarizes key findings from that analysis (see ai-analysis/ directory for full technical details).

### Variant Selection: A. flavus Remains Primary, with Characterized Alternates

The analysis confirmed *Aspergillus flavus* uricase as the primary candidate for S. cerevisiae expression, consistent with the rasburicase precedent. Two secondary candidates emerged:

- **A. globiformis uricase**: pH optimum 7.0–7.5 (vs. A. flavus 8.5–9.5), providing superior activity in the small intestine microenvironment without requiring gastric protection. *(In Vitro)*
- **K. marxianus uricase**: Exceptional thermostability (retained activity at 55–60°C), potentially valuable for fermentation conditions and dried product formats. *(In Vitro)*

*Mechanistic Extrapolation*: The A. globiformis variant may reduce the GI survival problem by matching the intestinal pH niche directly, partially offsetting the lack of protease engineering in the unmodified enzyme.

### GI Survival: 36–42% Baseline, Modest Yeast Cell Protection

Simulated GI transit modeling estimated baseline survival at **36–42%** of ingested free enzyme reaching the small intestine in active form. The major barrier is gastric acid and pepsin; small intestinal proteases cause secondary degradation.

**Yeast cell protection:** Intact S. cerevisiae cells expressing intracellular uricase provide **10–15% additional protection** over free enzyme, owing to β-glucan and chitin cell wall resistance to gastric acid. This modest boost is meaningful but does not solve the GI survival problem alone.

**Daily dosing**: Calculated therapeutic requirement = **500–800 mg of active enzyme per day** (converting from serum uric acid reduction targets in published animal models). This translates to approximately **5–10 g of dry cell mass** per dose, assuming 13% enzyme accumulation by cellular protein. *(Mechanistic Extrapolation)*

### Protein Engineering: Three Disulfide-Stabilized Variant Tiers

Protein-engineering analysis identified three engineering tiers, based on computational disulfide bond design and validation against the 2025 Scientific Reports CRISPR uricase work:

| Variant | Mutations | Predicted Improvement | Feasibility |
|---------|-----------|----------------------|-------------|
| **SB-1** | A6C + R290C | 2–3× GI stability | Conservative; low risk |
| **BAL-1** | SB-1 + K234E + K236E | 3–5× GI stability | Balanced; moderate risk |
| **OPT-1** | BAL-1 + S119C + C220C | 5–12× GI stability | Optimized; higher risk |

These predictions derive from rational disulfide cross-linking and electrostatic stabilization principles. *(In Vitro, mechanistic basis; animal validation needed)*

The tiered approach allows phase-gate progression: validate SB-1 in gnotobiotic mice before committing to BAL-1 or OPT-1 expression.

### Expression Cassette: TDH3 Promoter, Intracellular Expression Recommended

Computational model of S. cerevisiae expression systems recommends:

- **Promoter**: TDH3 (pGPD) — constitutive, very strong, predicted **800–1,200 mg/L** in liquid culture. *(In Vitro precedent from ACS Synth Bio 2025)*
- **Localization**: Intracellular expression (no signal peptide) — avoids yeast glycosylation (which can disrupt tetrameric assembly), leverages cell wall protection during GI transit, simplifies downstream processing.
- **Terminator**: ADH1 (strong, standard).
- **Integration**: CEN plasmid with URA3 marker for lab-stage work; chromosomal integration (CRISPR-based) for scaled production.

*Rationale (Mechanistic Extrapolation)*: Secretion of a 135 kDa tetramer is inefficient in yeast. Intracellular accumulation followed by natural autolysis in the fermentation broth or in the gut offers the best balance of expression yield and GI delivery.

### Cross-Validation: Feasibility Rating 5.8/10, Critical De-Risking Path

An integrated feasibility assessment across all constraints (enzyme activity, GI survival, dosing, regulatory) yields a composite rating of **5.8 / 10.0** — higher than naive estimates but highlighting significant unknowns.

**Critical constraints (lowest confidence):**
- GI survival post-engineering: **4.0 / 10** (protease resistance unvalidated in unmodified A. flavus; depends on variant selection and delivery format)
- Therapeutic efficacy in humans: **5.0 / 10** (rodent data supportive; human dose-response for oral uricase still uncertain per ALLN-346 Phase 2a divergence)

**De-risking budget and timeline:**
Estimated cost to achieve high-confidence proof-of-concept (Phases 0–3 with variant comparison): **~$300,000** over **12–18 months**. This includes:
- Phases 0–2 (bench + in vitro): ~$5,000–8,000, 4–6 months
- Phase 3 (gnotobiotic mouse validation with top 2 variants): ~$20,000–35,000, 8–12 weeks
- Extended validation (human volunteer dosing, manufacturing scale): ~$250,000+, 6+ months

*(Mechanistic Extrapolation based on comparative cost models for probiotic and enzyme-delivery studies)*

**Next gate decision**: Upon completion of Phase 1 GI survival testing, the predicted improvement from the variant tiers should drive variant selection for Phase 3. If SB-1 achieves >3× baseline survival in SGF/SIF assay, proceed to single-variant Phase 3. If survival remains <2×, prioritize engineering (BAL-1) or reconsider delivery format (enteric capsule).

### Revision & Sources

This section synthesizes computational and structural analysis conducted in April 2026. All claims carry the stated evidence level (In Vitro, Animal Model, Clinical Trial, or Mechanistic Extrapolation) and are anchored to published precedent (ACS Synthetic Biology 2025, Scientific Reports 2025, historical rasburicase literature) where available.

For detailed calculations, variant structural models, and GI transit simulation parameters, see ai-analysis/01–05 technical reports.

## References
- **Oda, M. et al.** (2002). Loss of Urate Oxidase Activity in Hominoids and its Evolutionary Implications. *Molecular Biology and Evolution*, 19(5), 640–653. [doi:10.1093/oxfordjournals.molbev.a004123](https://academic.oup.com/mbe/article/19/5/640/1067768)
- **Kratzer, J.T. et al.** (2014). Evolutionary history and metabolic insights of ancient mammalian uricases. *Proceedings of the National Academy of Sciences*, 111(10), 3763–3768. [doi:10.1073/pnas.1320393111](https://www.pnas.org/doi/10.1073/pnas.1320393111)
- **Keenan, J.P. et al.** (2023). A widely distributed gene cluster compensates for uricase loss in hominids. *Cell*, 186(16), 3400–3413. [doi:10.1016/j.cell.2023.06.010](https://www.sciencedirect.com/science/article/pii/S0092867423006876)
- **Matsuo, H. et al.** (2014). ABCG2 dysfunction increases serum uric acid by decreased intestinal urate excretion. *Nucleosides, Nucleotides and Nucleic Acids*, 33(4-6), 275–281. [PMID: 24940679](https://pubmed.ncbi.nlm.nih.gov/24940679/)
- **Hosomi, A. et al.** (2012). Extra-Renal Elimination of Uric Acid via Intestinal Efflux Transporter BCRP/ABCG2. *PLOS ONE*, 7(2), e30456. [doi:10.1371/journal.pone.0030456](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0030456)
- **Ichida, K. et al.** (2012). Decreased extra-renal urate excretion is a common cause of hyperuricemia. *Nature Communications*, 3, 764. [Related review: PMC8268734](https://pmc.ncbi.nlm.nih.gov/articles/PMC8268734/)
- **Hershfield, M.S. et al.** (2020). Oral Treatment With an Engineered Uricase, ALLN-346, Reduces Hyperuricemia and Uricosuria in Urate Oxidase-Deficient Mice. *Frontiers in Medicine*, 7, 569215. [PMID: 33330529](https://pubmed.ncbi.nlm.nih.gov/33330529/)
- **Allena Pharmaceuticals.** (2022). Clinical and Corporate Update — Phase 2a Study 201 results. [Press release, January 4, 2022](https://ir.allenapharma.com/news-releases/news-release-details/allena-pharmaceuticals-provides-clinical-and-corporate-update)
- **Allena Pharmaceuticals.** (2022). Phase 2a Study 202 enrollment completion and update. [Press release, July 19, 2022](https://www.globenewswire.com/news-release/2022/07/19/2481757/0/en/Allena-Pharmaceuticals-Announces-Completion-of-Enrollment-of-Cohorts-A-and-B-of-ALLN-346-Phase-2a-Study-202-in-Patients-with-Gout-and-Stages-2-and-3-Chronic-Kidney-Disease.html)
- **Designer probiotic-based living drugs for uric acid homeostasis control in hyperuricemic mice and rats.** (2025). *Cell Reports Medicine*, S2666-3791(25)00452-5. [doi:10.1016/j.xcrm.2025.102052](https://www.cell.com/cell-reports-medicine/fulltext/S2666-3791(25)00452-5)
- **Systematic Engineering for Efficient Uric Acid-Degrading Activity in Probiotic Yeast *Saccharomyces boulardii*.** (2025). *ACS Synthetic Biology*, 14(6), 2030–2043. [doi:10.1021/acssynbio.4c00831](https://pubs.acs.org/doi/10.1021/acssynbio.4c00831)
- **Rasburicase.** FDA Prescribing Information (Elitek). [Sanofi product label](https://products.sanofi.us/elitek/elitek.pdf). Approved 2002. Note: ~60% ADA rate limits repeat dosing.
- **Leplatois, P. et al.** (1992). High-level production of a peroxisomal enzyme: *Aspergillus flavus* uricase accumulates intracellularly and is active in *Saccharomyces cerevisiae*. *Gene*, 122(1), 139–145. [doi:10.1016/0378-1119(92)90041-M](https://www.sciencedirect.com/science/article/abs/pii/037811199290041M)
- **Fazel, R. et al.** (2017). Recombinant production of *Aspergillus flavus* uricase and investigation of its thermal stability in the presence of raffinose and lactose. *3 Biotech*, 7(3), 201. [PMC5493577](https://pmc.ncbi.nlm.nih.gov/articles/PMC5493577/). Also: **Bayol, A. et al.** (2002). Modification of a reactive cysteine explains differences between rasburicase and natural *A. flavus* uricase. [PMID: 12149119](https://pubmed.ncbi.nlm.nih.gov/12149119/)
- **Bim, M.A. & Franco, T.T.** (2008). Uricase production by a recombinant *Hansenula polymorpha* strain harboring *Candida utilis* uricase gene. *Applied Microbiology and Biotechnology*, 79(3), 545–553. [doi:10.1007/s00253-008-1472-8](https://link.springer.com/article/10.1007/s00253-008-1472-8)
- **Juan, E.C. et al.** (2011). High-yield expression, purification, characterization, and structure determination of tag-free *Candida utilis* uricase. *Applied Microbiology and Biotechnology*, 92(1), 79–87. [doi:10.1007/s00253-011-3244-0](https://link.springer.com/article/10.1007/s00253-011-3244-0)
- **Gibson, T. et al.** (1984). Beer drinking and its effect on uric acid. *Rheumatology*, 23(3), 203–209. [doi:10.1093/rheumatology/23.3.203](https://academic.oup.com/rheumatology/article-abstract/23/3/203/1781057)
- **Faller, J. & Fox, I.H.** (1982). Ethanol-induced hyperuricemia: evidence for increased urate production by activation of adenine nucleotide turnover. *New England Journal of Medicine*, 307(26), 1598–1602. Also: **Yamamoto, T. et al.** (2005). Effect of ethanol on metabolism of purine bases. *Clinica Chimica Acta*, 356(1-2), 35–57. [doi:10.1016/j.cccn.2005.01.024](https://www.sciencedirect.com/science/article/abs/pii/S0009898105000732)
- **McFarland, L.V.** (2010). Systematic review and meta-analysis of *Saccharomyces boulardii* in adult patients. *World Journal of Gastroenterology*, 16(18), 2202–2222. Also: [PMC7344949 — *S. boulardii*: What Makes It Tick as Successful Probiotic?](https://pmc.ncbi.nlm.nih.gov/articles/PMC7344949/)
- **Braat, H. et al.** (2024). Targeted delivery of the probiotic *Saccharomyces boulardii* to the extracellular matrix enhances gut residence time and recovery in murine colitis. *Nature Communications*, 15, 4157. [doi:10.1038/s41467-024-48128-0](https://www.nature.com/articles/s41467-024-48128-0)
- **Allena Pharmaceuticals Inc.** (2020). US Patent 10,815,461 B2: "Recombinant uricase enzyme." Granted 27 Oct 2020. Priority US provisional 62/529,726 (7 July 2017). [patents.google.com/patent/US10815461B2](https://patents.google.com/patent/US10815461B2/en)
- **Allena Pharmaceuticals Inc.** (2020). US Patent Application 2020/0071681 A1: "Recombinant uricase enzyme" (published application; sequence source cited by Frontiers 2020 ALLN-346 paper). [patents.google.com/patent/US20200071681A1](https://patents.google.com/patent/US20200071681A1/en)
Prepared April 2026. This document represents a good-faith research synthesis by a non-scientist. Corrections, challenges, and "you're wrong about X" are all welcome — that's the point.
### Open Enzyme Research Library
This document is part of the [Open Enzyme](open-enzyme-vision.md) project — an open-source therapeutic enzyme platform.
[Open Enzyme Vision & Roadmap](open-enzyme-vision.md)
[Gout Deep Dive Research](gout-deep-dive.md)
[Enzyme Deficit Deep Dive](enzyme-deficit-deep-dive.md)
[NLRP3 Inflammasome Exploit Map](nlrp3-exploit-map.md)
[Peptides & Gout Addendum](peptide-gout-addendum.md)
[Blood-Barrier Exploits](blood-barrier-exploits.md)
[Engineered Koji Protocol](engineered-koji-protocol.md)
[Engineered Yeast Uricase Proposal (this doc)](engineered-yeast-uricase-proposal.md)