---
title: Aspergillus oryzae (Koji Mold)
aliases:
  - koji
  - koji mold
  - A. oryzae
  - Aspergillus oryzae
related:
  - saccharomyces-cerevisiae
  - uricase
  - open-enzyme-vision
  - engineered-koji-protocol
  - gut-lumen-sink
  - enzyme-deficit-deep-dive
sources:
  - engineered-koji-protocol.md
  - enzyme-deficit-deep-dive.md
  - open-enzyme-vision.md
  - blood-barrier-exploits.md
  - gout-deep-dive.md
  - koji-home-fermentation.md
---

# Aspergillus oryzae (Koji Mold)

## Overview

*Aspergillus oryzae* (koji mold) is a filamentous fungus with GRAS (Generally Recognized As Safe) status from the FDA and a 1,000+ year history of safe use in East Asian food production. It is one of the most genetically tractable fungi in existence and naturally produces a complex cocktail of digestive enzymes—lipase, multiple proteases, and amylase—at therapeutically relevant concentrations. For the [[open-enzyme-vision|Open Enzyme project]], koji serves as a dual-purpose platform: it produces the digestive enzymes needed for [[enzyme-deficit-deep-dive|enzyme insufficiency]] without any genetic engineering, and it can be engineered to additionally express [[uricase|uricase]] for gout management. (Source: engineered-koji-protocol.md, open-enzyme-vision.md)

## GRAS Status and Food Safety History

*A. oryzae* holds FDA GRAS status and has decades of safety documentation. The organism has been used for over a millennium in the production of:

- **Miso**: Fermented soybean paste, produced by koji-mediated fermentation
- **Soy sauce**: Koji is essential to soy sauce production
- **Sake**: Japanese rice wine, where koji breaks down rice starch into fermentable sugars
- **Amazake**: Sweet rice drink made directly from koji
- **Mirin**: Sweet cooking ingredient derived from koji fermentation

Billions of people have consumed koji-fermented foods without adverse effects. The organism does not produce mycotoxins (unlike some Aspergillus species, notably A. flavus). A. oryzae is a domesticated, carefully maintained organism—Japanese koji makers have propagated specific strains for centuries. (Source: engineered-koji-protocol.md, open-enzyme-vision.md)

## Native Enzyme Production

Wild-type koji fermentation naturally produces:

### Lipase
Cleaves dietary fats (triglycerides) into fatty acids and glycerol. Critical for fat absorption. Commercial lipase supplements derive from the same organism family. Wild-type koji produces lipase at concentrations equivalent to pharmaceutical-grade digestive enzyme supplements. (Source: enzyme-deficit-deep-dive.md)

### Protease (Multiple Classes)
Koji produces acid-stable serine proteases, carboxypeptidases, and endopeptidases. These cleave dietary proteins into peptides and amino acids. Acid stability is important because these enzymes function in the acidic stomach environment. Wild-type koji generates protease levels comparable to commercial pancreatic enzyme supplements. (Source: enzyme-deficit-deep-dive.md)

### Amylase (Alpha-Amylase and Glucoamylase)
Koji's primary product during rice fermentation. Breaks down starch (the primary macronutrient in rice) into glucose and maltose. This is why koji is essential to sake production—it converts rice starch into fermentable sugars. Amylase levels reach 15–25% of total soluble protein in koji grown on rice. (Source: enzyme-deficit-deep-dive.md, engineered-koji-protocol.md)

### Native Secondary Metabolites: Kojic Acid, Ergothioneine, Ferulic Acid

Beyond digestive enzymes, wild-type *A. oryzae* natively produces a suite of bioactive secondary metabolites during standard koji fermentation — without any genetic engineering. These are relevant to the gout/NLRP3 angle of the [[open-enzyme-vision|Open Enzyme platform]], not just the digestive enzyme track.

**Kojic acid** — *A. oryzae* natively produces kojic acid at **3–5 g/L** during standard rice koji fermentation. Kojic acid has documented **NF-κB suppression activity in multiple inflammatory cell types (In Vitro)**; direct NLRP3 inflammasome activity is unpublished and is flagged as an open question in [nlrp3-inhibitor-screen.md](./nlrp3-inhibitor-screen.md). Notably, 3–5 g/L native production exceeds the fermentation titers of most engineered NLRP3-inhibitor candidate compounds, which positions *A. oryzae* as a **uniquely endowed host**: it already produces a candidate NLRP3-adjacent compound at therapeutically relevant concentrations as a baseline metabolite. (Source: nlrp3-inhibitor-screen.md, engineered-koji-protocol.md)

**Ergothioneine** — ~20 mg/g dry mycelial mass. Antioxidant; Nrf2 inducer; mitochondrial-targeted ROS scavenger (In Vitro). (Source: engineered-koji-protocol.md)

**Ferulic acid** — Present at substrate-dependent titers during rice/bran fermentation; ROS scavenger with GI-tract anti-inflammatory activity (In Vitro). (Source: engineered-koji-protocol.md)

**Platform implication:** Any engineered koji strain (e.g., uricase-expressing) will by default also ship with this secondary-metabolite chorus. The engineering target sits on top of a pre-existing pharmacological baseline. Whether engineering perturbs that baseline is an open experimental question — see the proposed WT-vs-engineered metabolite titer comparison in [engineered-koji-protocol.md](./engineered-koji-protocol.md#01b-natural-metabolite-bonus--baseline-fermentation-byproducts).

## Genetic Tractability

### Transformation Methods

*A. oryzae* can be transformed using multiple established protocols:

**Protoplast-Mediated Transformation (PEG):**
- Remove cell wall enzymatically to create protoplasts
- Apply polyethylene glycol (PEG) to facilitate DNA uptake
- Allows homologous recombination and targeted integration
- Standard protocol: published, routine in research labs
- Efficiency: 10³–10⁵ transformants per microgram DNA (depending on protocol)

**Agrobacterium-Mediated Transformation:**
- Uses *Agrobacterium tumefaciens* as a biological delivery vector
- Introduces DNA into *A. oryzae* cells via T-DNA transfer
- Particularly efficient for targeted gene insertion
- Enables complex multi-gene constructs

**CRISPR-Cas9 Genome Editing:**
- Modern alternative to traditional homologous recombination
- Multiple published protocols for CRISPR in *A. oryzae*
- Enables precise gene editing, deletion, or multi-locus modifications
- Highly efficient for targeted knockouts or insertions

These transformation methods are routine in academic and industrial biotechnology. The toolkit is mature and reproducible. (Source: engineered-koji-protocol.md)

### Promoters and Expression Elements

*A. oryzae* has a well-characterized library of characterized promoters available for expression optimization:

**PamyB (α-Amylase Promoter) — THE OPTIMAL CHOICE:**
- Starch-inducible: activates in response to starch (the primary substrate during koji fermentation on rice)
- Extremely strong: naturally drives production of amylase, one of the most abundant proteins *A. oryzae* produces
- Auto-activating when koji is grown on rice—no external inducer needed
- Proven to drive high-level heterologous protein expression in industrial koji production
- This promoter is a strategic choice: it self-induces on the exact substrate you're already using for fermentation

**PglaA (Glucoamylase Promoter):**
- Very strong, starch-inducible
- Alternative to PamyB with similar induction profile

**Ptef1 (Translation Elongation Factor 1 Promoter):**
- Strong, constitutive (always active)
- Good if constant expression is desired regardless of substrate
- Slightly weaker than PamyB on starch

**PgpdA (Glyceraldehyde-3-Phosphate Dehydrogenase Promoter):**
- Moderate strength, constitutive
- Reliable housekeeping promoter
- Good for selection markers but weaker for therapeutic gene expression

**PalcA (Alcohol Dehydrogenase Promoter):**
- Ethanol-inducible, not ideal for food fermentation

Recommendation: **PamyB is the winner** for a therapeutic koji expressing uricase. It provides strong, auto-inducing expression on rice without external inducers or complex fermentation optimization. (Source: engineered-koji-protocol.md)

### Selectable Markers

**pyrG (Uridine Prototrophy) — PREFERRED FOR FOOD-GRADE:**
- Enables selection on media lacking uridine/uracil
- Counter-selection available (5-FOA selects against pyrG)
- No antibiotic resistance markers—food-safe
- Enables marker recycling for sequential transformations
- Standard *A. oryzae* host strain NSAR1 is pyrG-deficient, making this marker ideal

**Other Options (Less Ideal for Food-Grade Applications):**
- niaD (nitrate utilization) — food-safe, selects on nitrate as sole nitrogen source
- amdS (acetamide utilization) — dominant marker, works in wild-type backgrounds
- hph (hygromycin B resistance) — dominant antibiotic marker, simpler selection but less ideal for food organisms

For a food-grade therapeutic organism, pyrG is strongly preferred. (Source: engineered-koji-protocol.md)

## Genetic Relatedness to A. flavus

*A. oryzae* and *A. flavus* are phylogenetically extremely close—they share >99.5% genome similarity in coding regions and nearly identical codon usage. This proximity means that the [[uricase|uricase gene (uaZ) from A. flavus]] should express well in *A. oryzae* without codon optimization, though optimization may further improve expression levels. The transcriptional and translational machinery of *A. oryzae* is essentially pre-adapted to handle *A. flavus* genes. (Source: engineered-koji-protocol.md)

## Fermentation: Growing Koji on Rice

Traditional koji fermentation is ancient and reproducible. The biological parameters are well-characterized.

### Koji-kin vs. Koji Rice — The Critical Distinction

A common source of confusion in home fermentation: **koji-kin** and **koji rice** are different things. (source: koji-home-fermentation.md)

| Term | What it is | What it looks like | Use |
|---|---|---|---|
| **Koji-kin** (種麹, *tane-koji*) | Dried *Aspergillus* spore inoculum on a small carrier (typically rice flour) | Pink/purple foil packet, fine pinkish-tan powder | **Starting material.** A pinch inoculates ~1 kg of cooked rice. |
| **Koji rice** (麹, *kōji*) | Cooked rice that has been inoculated with koji-kin and fully colonized by mycelium over 42–48 h | Whole rice grains covered in white fuzzy mycelium, sweet/floral smell | **Working enzyme substrate.** This is what's called for in shio-koji / amazake / miso recipes. |

You only buy koji-kin once per ~15 kg of rice you plan to inoculate. The two-stage process is: (1) koji-kin + steamed rice → koji rice (42–48 h at 32–40°C); (2) koji rice → finished product (shio-koji, amazake, miso). (source: koji-home-fermentation.md)

### Standard Protocol

**Temperature:** 30–32°C (optimal range; can tolerate 25–35°C)

**Humidity:** >80% (critical; dry conditions inhibit growth)

**Substrate:** Steamed white rice (short-grain preferred; koji ferments evenly)

**Duration:** 36–48 hours

**Setup:** 
- Spread steamed rice in a shallow layer on a clean surface (bamboo mat, cloth, or perforated pan)
- Inoculate with koji spores (either a prepared culture or spores saved from a prior batch)
- Cover lightly to maintain humidity while allowing air circulation
- Temperature control via incubator, oven with pilot light, or room heater

**Turning schedule (手入れ):** Koji rice requires mixing at intervals to distribute heat and moisture. (source: koji-home-fermentation.md)
- **~15–20 h after inoculation (1st turning):** Rice should be warm to the touch, faint sweet smell. Break up clumps, mix gently, re-wrap. Target temp: 37–39°C.
- **~24 h (2nd turning):** White mycelium visible. Mix again. Target: 38–40°C.
- **~36 h (3rd turning):** Mycelium dense and white, sweet/floral smell ("chestnut" / "popcorn" notes). Target: 37–40°C.

**Endpoint:**
- Koji is ready when the rice grains are bound together by white mycelium (fungal threads)
- A pleasant fruity/sweet aroma develops (from enzymatic activity)
- Grains appear coated with white growth but individual grains still visible (not mushy)
- Should NOT smell of ammonia, alcohol, or be greenish (= contamination, discard)

**Yield:** From ~500g steamed rice, you'll produce ~600–700g of koji (wet weight). The enzyme concentration is ready for immediate use. (Source: engineered-koji-protocol.md)

### Troubleshooting

| Problem | Likely cause | Fix |
|---|---|---|
| No mycelium growth | Temperature too low; rice too wet/dry; expired koji-kin | Check thermometer; rice should be al dente; replace starter |
| Green/black/pink patches (not white) | Contamination (Penicillium, bacteria) | Discard. Improve sanitation, lower temp |
| Ammonia smell | Over-fermented (>50 h, too warm) | Discard or use immediately for shio-koji (salt will mask it) |
| Yeasty/alcohol smell | Wild yeast competition; rice too wet | Discard; reduce moisture next batch |

(source: koji-home-fermentation.md)

### Enzymatic Activity Output

Koji fermentation produces enzymes at concentrations comparable to commercial enzyme supplements:

| Enzyme | Activity Level | Notes |
|---|---|---|
| Alpha-amylase | 15–25% of total soluble protein | Starch → glucose/maltose conversion |
| Acid-stable protease | ~10–15% of total soluble protein | Protein → peptides, survives stomach pH |
| Lipase | ~5–10% of total soluble protein | Fat → fatty acids + glycerol |

These are the same enzymes in commercial pancreatic enzyme supplements like Creon and Zenpep. Traditional koji delivers them at food scale. (Source: enzyme-deficit-deep-dive.md, open-enzyme-vision.md)

## Engineered Koji: Adding Uricase

### Expression Cassette Design

The standard expression cassette for uricase in koji:

```text
5' ──┤ PamyB ├──┤ SPamyB ├──┤ uaZ CDS (Δ PTS1, codon-opt) ├──┤ TtrpC ├── 3'
```

**Components:**
- **PamyB** — starch-inducible α-amylase promoter (strong, auto-activating on rice)
- **SPamyB** — α-amylase signal peptide (directs protein to secretion, extracellular accumulation)
- **uaZ CDS** — *Aspergillus flavus* uricase gene, codon-optimized, PTS1 signal removed
- **TtrpC** — *Aspergillus nidulans* trpC terminator (universal in Aspergillus)

**Selectable Marker:**
- **pyrG** (uridine prototrophy) — enables selection on uridine-free media, food-safe

Gene synthesis cost: ~$80–150 for the uaZ coding sequence (~906 bp), or ~$300 for the entire cassette. (Source: engineered-koji-protocol.md)

### Integration Strategy

**Genomic Integration (Preferred):**
- *Aspergillus* lacks stable episomal plasmids—integration is chromosome-based
- **Targeted integration** at a defined safe locus (neutral integration site) ensures:
  - Single-copy gene insertion (predictable expression)
  - No disruption of essential genes
  - Reproducible expression over generations
  - Strain stability for ongoing home fermentation

**Methods:**
- Homologous recombination (flanking sequences homologous to target site)
- CRISPR-Cas9 (modern, highly efficient, precise)

(Source: engineered-koji-protocol.md)

### Expected Uricase Expression

In *S. cerevisiae*, the same *A. flavus* uricase gene achieves ~13% of total cellular protein. In *A. oryzae*, comparable or higher expression is expected because:
- A. oryzae naturally produces massive amounts of secreted proteins (amylase, proteases, lipase)
- The PamyB promoter is one of the strongest promoters in any filamentous fungus
- A. oryzae has evolved robust protein folding and secretion machinery for high-volume enzyme production

Rough estimate: 50–100 mg of uricase per liter of koji culture, or ~5–10 mg per 50g of fermented koji on rice. This would be sufficient for therapeutic dosing in a food format. (Source: engineered-koji-protocol.md)

## Delivery Formats for Therapeutic Koji

For a complete small-batch home protocol (koji-kin → koji rice → shio-koji / amazake), see [Koji Home Fermentation](./koji-home-fermentation.md). That page is the wild-type baseline that the engineered strain must outperform for EPI applications. (source: koji-home-fermentation.md)

### Fresh Koji on Rice
- Consumed immediately after 36–48 hour fermentation
- Highest enzyme activity (fresh)
- Consumed as-is or processed into amazake (sweet rice drink)
- Shelf-stable for days at room temperature; refrigerate for longer storage

### Shio Koji (Salted Koji)
- Mix fresh koji rice + salt (~30% by weight of koji) + water (~125% by weight of koji) (source: koji-home-fermentation.md)
- Ferment 7–14 days at room temperature, stirring daily; blend smooth when rice grains have softened
- Develops complex umami flavor, becomes paste-like
- Shelf-stable 6+ months refrigerated
- Can be consumed spoonfuls at a time or used as a marinade (5–10% by weight on protein, 30 min to 24 h)
- Traditional Japanese preservation format; **highest-leverage application for EPI** because proteases pre-digest protein in the marinade phase before food reaches the eater (Mechanistic Extrapolation; source: koji-home-fermentation.md)

### Dried Koji Powder
- Enzyme stability after drying is critical
- **Conventional heat drying (50–60°C)** destroys uricase activity; *A. flavus* uricase loses activity above 40°C
- **Lyophilization (freeze-drying)** preserves enzyme activity far better
- Trehalose or maltodextrin as lyoprotectant during freeze-drying
- Capsule format (size 00 capsules: ~500 mg each)
- Shelf-stable for months refrigerated or frozen

### Fermented Beverage (Amazake-Style)
- Blend fresh koji with water, hold at **55–60°C for 8–10 hours** (yogurt maker, slow cooker on warm, sous vide, or thermos) — α-amylase converts rice starch to maltose and glucose (source: koji-home-fermentation.md)
- Heat briefly to 80°C to deactivate enzymes before refrigerating (otherwise wild yeast takes over)
- Sweet rice drink, naturally sweet from starch breakdown; refrigerated shelf life ~10 days
- Koji with uricase provides enzyme in drinkable format; note that 55–60°C is near uricase denaturation temperature — some uricase activity loss expected; digestive enzymes (amylase, protease) are more heat-stable (Mechanistic Extrapolation; source: koji-home-fermentation.md)
- Consumed as beverage 100–200 mL warm before meals as digestive aid
- Shelf-stable if refrigerated

(Source: engineered-koji-protocol.md, engineered-yeast-uricase-proposal.md)

## Hydrogen Peroxide Byproduct Management

Uricase catalyzes: Uric acid + O₂ + H₂O → 5-hydroxyisourate → allantoin + CO₂ + **H₂O₂**

H₂O₂ (hydrogen peroxide) is generated as a byproduct. In cells, catalase immediately degrades this to water and oxygen. In the gut lumen and koji medium:

- Koji naturally produces catalase (abundant in fungi)
- H₂O₂ production is minimal at expected therapeutic uricase activity levels
- Gut lumen has significant peroxidase activity from microbiome and epithelial cells
- H₂O₂ is rapidly scavenged and not a safety concern at therapeutic doses

(Source: engineered-koji-protocol.md)

## Safety Considerations

### No Mycotoxin Production
*A. oryzae* does not produce aflatoxins or other major mycotoxins. It is explicitly distinguished from its pathogenic relative *A. flavus*, which can produce aflatoxins. A. oryzae is used in food production precisely because of this safety profile. (Source: engineered-koji-protocol.md)

### Immunogenicity Concerns (Minimal)
- Koji is GRAS and consumed in food
- Oral tolerance to fungal antigens is inherently high (mucosal immune system is tolerogenic)
- Engineered strains carry only the uricase transgene (no virulence factors added)
- Phase 1 trials of oral uricase (ALLN-346) showed no immune reactions or serious adverse events (Source: engineered-koji-protocol.md, engineered-yeast-uricase-proposal.md)

### Proper Fermentation Controls
- Prevent contamination with non-GRAS molds by using pure cultures and maintaining clean fermentation conditions
- Monitor for off-odors or discoloration (signs of contamination)
- Discard any koji that shows green, black, or unusual coloration

## Yellow vs. White vs. Black Koji for Home Use

For EPI / digestive-enzyme home use, the choice of koji strain matters. (source: koji-home-fermentation.md)

| Strain | Species | Strengths | Best for |
|---|---|---|---|
| **Yellow koji** | *Aspergillus oryzae* | Highest amylase + standard protease; sweetest amazake; most documentation | **Default choice for digestive-enzyme home use.** Sake, sweet miso, amazake, shio-koji. |
| **White koji** | *A. luchuensis* var. *kawachii* | High citric acid (anti-contamination in warm climates); good amylase | Shochu, awamori, sour-leaning miso. Tangier shio-koji. |
| **Black koji** | *A. luchuensis* var. *awamori* | Highest citric acid; robust in hot/humid conditions | Awamori (Okinawan distillate); rare in DIY use |

**Recommendation for EPI / home-PERT-alternative use case:** Yellow koji (*A. oryzae*) is the better-fit default — highest amylase and standard protease, sweetest amazake, most documentation. White koji is functional but tangier and has slightly lower diastatic power. If white koji is on hand, use it first to learn the process, then switch to yellow when restocking. (Mechanistic Extrapolation; source: koji-home-fermentation.md)

**Key limitation for fat malabsorption EPI:** Lipase activity of *A. oryzae* shio-koji is low compared to *A. niger* or engineered strains — likely the limiting digestive-enzyme axis for fat malabsorption phenotype EPI. This is an open question requiring quantitative comparison vs. commercial PERT (Creon, Zenpep). (source: koji-home-fermentation.md)

## Multi-Organism Strategy in Open Enzyme

[[aspergillus-oryzae|Koji]] is the first platform target in the [[open-enzyme-vision|Open Enzyme]] project because:

1. **No genetic engineering needed for digestive enzymes** — wild-type koji already produces therapeutic-grade lipase, protease, and amylase
2. **One food organism addresses two household enzyme deficiencies** — Brian's uricase deficit + Lynn's digestive enzyme insufficiency
3. **GRAS status and ancient safety history** — centuries of consumption, FDA approval
4. **Simple home fermentation** — rice, spores, warmth, humidity, 36–48 hours
5. **Genetic tools mature** — CRISPR, transformation protocols, characterized promoters, well-understood

Engineered koji represents the ideal convergence of biological feasibility, food safety, and therapeutic need. (Source: open-enzyme-vision.md, enzyme-deficit-deep-dive.md)

## Comparison to Saccharomyces cerevisiae

Both [[saccharomyces-cerevisiae|S. cerevisiae]] and *A. oryzae* can express uricase, but they serve different strategic roles:

| Feature | A. oryzae (Koji) | S. cerevisiae (Yeast) |
|---|---|---|
| Native enzymes | Lipase, protease, amylase (exactly what Lynn needs) | None relevant to enzyme therapy |
| GRAS status | Yes (1000+ years food use) | Yes |
| Genetic engineering | Mature, CRISPR-ready, industrial standard | Undergraduate coursework-level |
| Food format | Shio koji, amazake, fermented paste | Non-alcoholic beverage, capsule |
| Fermentation | 36–48h on rice, ambient conditions | Liquid fermentation, 3–7 days |
| Enzyme stability (drying) | Good (when lyophilized) | Moderate |
| Dual-purpose | Yes (uricase + native digestive enzymes) | No (only uricase, requires codon opt.) |

For the [[open-enzyme-vision|Open Enzyme platform]], koji is strategically preferred as the first platform because of the dual-enzyme advantage and simpler fermentation. S. cerevisiae remains valuable as an alternative delivery system or for high-volume commercial scale-up. (Source: engineered-koji-protocol.md, engineered-yeast-uricase-proposal.md)

## Future: Multi-Compound Koji

The [[nlrp3-exploit-map|NLRP3 inflammasome pathway]] suggests an extended vision for engineered koji:

With modern CRISPR tools and *A. oryzae*'s robust synthetic biology toolkit, future iterations of koji could be engineered to simultaneously produce:

1. **Uricase** — dissolves uric acid (upstream prevention)
2. **KPV peptide-like** anti-inflammatory peptides — NF-κB suppression
3. **Enhanced spermidine biosynthesis** — autophagy activation
4. **Nrf2-activating compounds** — antioxidant defense

A single fermented food attacking gout from both the uric acid and inflammatory angles. This is the superorganism vision—engineering food as a multi-targeted therapeutic platform. (Source: nlrp3-exploit-map.md)

## AI Analysis Findings (April 2026)

**Koji Construct Design Finalized:**
- **Promoter:** amyB (α-amylase, starch-inducible, 6–10× baseline) — auto-activates on rice substrate without external induction
- **Expected Uricase Yield:** 40–80 mg uricase per gram of fermented koji (assuming 5–10 g/L total secreted protein on rice substrate)
- **Dual-enzyme platform confirmed:** Native digestive enzymes (lipase, protease, amylase) produced in parallel with engineered uricase

**Strain Recommendation: RIB40**
- Complete genomic sequence enables CRISPR/Cas9 refinement
- 65 endopeptidase + 69 exopeptidase genes support efficient protein degradation
- Lipase activity: 1,813–2,280 U/g koji (rice bran substrate optimal)
- Dosing equivalence: 10–15 g optimized koji ≈ single Creon dose (25,000 USP lipase units)

**Wild-Type OTC Benchmark and Unit Conversion (updated April 2026):**
- The primary commercial benchmark for the engineered platform is the wild-type *A. oryzae* OTC product class (e.g., BoulderBio at 40,000 FIP lipase per capsule), not Creon. This is the closest commercial analogue to what an engineered koji product would look like in finished form. (source: digestive-enzyme-optimization.md)
- **FIP vs. USP unit distinction:** 40,000 FIP ≈ 9,000–10,000 USP at standard activity assays (In Vitro). A 40,000 FIP cap delivers roughly 1/3 of a 25,000 USP Creon meal-dose. (source: digestive-enzyme-optimization.md)
- **pH stability advantage:** *A. oryzae* lipase is active across pH 4–10, broader than porcine pancreatic lipase; survives gastric transit better without enteric coating. (In Vitro; source: digestive-enzyme-optimization.md)
- **Engineered koji lipase yield in FIP terms:** 1,813–2,280 U/g koji translates to **~50,000–60,000 FIP per dried gram** at typical assay conditions — meaning 1 g engineered koji could match BoulderBio's 2-cap dose. (Mechanistic Extrapolation; source: digestive-enzyme-optimization.md)

**n=1 Tolerability Datum (April 2026):**
- Wild-type *A. oryzae*-derived enzymes (BoulderBio) were well-tolerated across 30+ meals in a single subject — no adverse reactions, no allergic response. (Clinical n=1, unblinded, uncontrolled; source: digestive-enzyme-optimization.md)
- A clear decoupling of liquid-stool from pain — against a long-stable baseline — was observed on the 2-cap protocol at 2026-04-25 breakfast (~15–20 g fat). This is a meaningful efficacy signal for the platform's mechanism of action even before any engineering. (Clinical n=1; source: digestive-enzyme-optimization.md)
- **Split-dose finding:** 1+1 split (1 cap at first bite + 1 at ~10 min) was successful for very fatty meals (>25 g fat), suggesting dose magnitude AND duration matter. The engineered platform should consider sustained-release formulation or split-dose instructions. (Mechanistic Extrapolation; source: digestive-enzyme-optimization.md)

**Codon Optimization for A. oryzae:**
- Native GC content: 48% (A. flavus ~48%; near-perfect match)
- A. flavus uricase requires minimal codon optimization (unlike S. cerevisiae)
- Target GC 48–52% (aligned with A. oryzae preferences)

See [[ai-analysis/06-koji-construct-design|06 — Koji Construct Design]] and [[ai-analysis/08-digestive-enzyme-optimization|08 — Digestive Enzyme Optimization]] for complete fermentation protocols, strain comparisons, and dosing calculations.

## References

- Source: engineered-koji-protocol.md — Complete protocol for A. oryzae transformation, fermentation, and dosing
- Source: enzyme-deficit-deep-dive.md — Enzyme insufficiency and koji's native therapeutic potential
- Source: open-enzyme-vision.md — Platform vision and koji as first target
- Source: nlrp3-exploit-map.md — Future multi-compound koji engineering
- Source: blood-barrier-exploits.md — Gut-lumen enzyme delivery route validation
