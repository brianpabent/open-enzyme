# Open Enzyme Concept Graph

A visual map of how all Open Enzyme research domains relate to each other. Use the interactive diagram below to understand dependencies, synergies, and the full therapeutic stack.

## Interactive Concept Map

```mermaid
graph TB
    subgraph Core["CORE PATHOLOGY"]
        A1["Gout"]
        A2["Enzyme Deficits"]
        A3["EPI"]
        A4["Hyperuricemia"]
    end

    subgraph Problem["PROBLEM MECHANISMS"]
        B1["Uric Acid Accumulation"]
        B2["MSU Crystal Formation"]
        B3["Gut Barrier Damage"]
        B4["SIBO/Dysbiosis"]
        B5["Brush Border Erosion"]
    end

    subgraph Immune["IMMUNE CASCADE"]
        C1["MSU Crystals"]
        C2["NLRP3 Inflammasome"]
        C3["ASC Speck Formation"]
        C4["IL-1β / IL-18 Release"]
        C5["Acute Flare"]
    end

    subgraph Host_Enzyme["HOST ENZYMES"]
        D1["Uricase Lost"]
        D2["Lipase Deficit"]
        D3["Protease Deficit"]
        D4["Amylase Deficit"]
    end

    subgraph Platform["ENGINEERED PLATFORMS"]
        E1["Saccharomyces cerevisiae"]
        E2["Aspergillus oryzae"]
        E3["GRAS Certification"]
    end

    subgraph Delivery["DELIVERY TARGETS"]
        F1["Uricase Gene"]
        F2["Lipase Gene"]
        F3["Protease Gene"]
        F4["Amylase Gene"]
        F5["Fermentation Protocol"]
        F6["Dosing Strategy"]
        F7["Shio-Koji Marinade"]
        F8["Amazake Drink"]
        F9["Wild-Type Baseline"]
        F10["Koji-Kin spore inoculum"]
        F11["Koji Rice colonized substrate"]
        F12["OTC PERT Benchmark (BoulderBio 40k FIP)"]
        F13["PERT Dose-Timing Framework (n=1)"]
    end

    subgraph Mechanism["THERAPEUTIC MECHANISM"]
        G1["Gut-Lumen Sink"]
        G2["Enzymatic Degradation"]
        G3["Uric Acid ↓ in Lumen"]
        G4["Re-absorption Prevention"]
    end

    subgraph Barrier["BARRIER REPAIR"]
        H1["Tight Junctions"]
        H2["Intestinal Permeability"]
        H3["TEER"]
    end

    subgraph Peptides["IMMUNOMODULATORY PEPTIDES"]
        I1["BPC-157"]
        I2["KPV Tripeptide"]
        I3["Barrier Integrity"]
        I4["IL-10 Promotion"]
    end

    subgraph Inhibitors["NLRP3 INHIBITORS"]
        J1["Oridonin"]
        J2["Disulfiram"]
        J3["ASC Block"]
        J4["Gasdermin D Block"]
        J5["Colchicine — CP2 P2X7 + CP3 ASC speck"]
        J6["Colchicine — ULT-initiation prophylaxis + CV repositioning (Lodoco FDA 2023)"]
    end

    subgraph Parallel_Path["PARALLEL FLARE PATHWAYS (CP6a)"]
        N1["5-LOX"]
        N2["LTB4"]
        N3["Neutrophil Chemotaxis"]
        N4["Quercetin — 5-LOX IC50 300 nM"]
        N5["AKBA (Boswellia) — allosteric 5-LOX ~2.7 μM"]
        N6["EPA substrate competition → RvE1"]
    end

    subgraph Complement["COMPLEMENT PRIMING (CP0 — NEW)"]
        O1["Complement C5a"]
        O2["C5aR1"]
        O3["ROS Burst (non-transcriptional priming)"]
        O4["Avacopan (C5aR1 antagonist, FDA ANCA)"]
        O5["S100A8/A9 DAMP (2025 flare driver)"]
    end

    subgraph Resolution["ACTIVE RESOLUTION (CP5b — NEW)"]
        P1["ALX/FPR2 Resolution Receptor"]
        P2["RvD1 / RvD2 (DHA-derived)"]
        P3["MaR1 (Maresin, DHA-derived)"]
        P4["Neutrophil Infiltration (resolved)"]
        P5["aggNET (resolution form)"]
        P6["Lactoferrin (fermentable, partial overlap)"]
    end

    subgraph TNFSF14_arm["CP1a AMPLIFIER"]
        Q1["TNFSF14 / LIGHT"]
        Q2["NF-κB Priming"]
    end

    subgraph MultiCP["MULTI-CHOKEPOINT PROTEINS / COMPOUNDS"]
        R1["Lactoferrin — CP1a + CP4/CP6b (GSDMD mitophagy) + CP5b"]
        R2["EGCG — 20S proteasome 86 nM → CP1a + CP4 + CP5"]
        R3["Zileuton — FDA 5-LOX inhibitor (CP6a), never tested in gout"]
        R4["Koji Uricase — upstream crystal elimination (removes trigger)"]
    end

    subgraph Cannabinoids["CANNABINOIDS / TERPENES"]
        M1["CBD"]
        M2["Beta-Caryophyllene"]
        M3["CBG"]
        M4["THCV"]
        M5["Limonene — Nrf2 + TLR4 — MSU rat gout 2025"]
    end

    subgraph Metabolic["METABOLIC MODULATION"]
        K1["Beta-Hydroxybutyrate"]
        K2["Ketogenic State"]
        K3["HDAC Inhibition"]
        K4["Probiotic Fitness"]
    end

    subgraph Clinical["CLINICAL PRECEDENT"]
        L1["ALLN-346 (terminated 2022)"]
        L2["Rasburicase"]
        L3["PULSE Probiotic"]
        L4["PRX-115 Phase 2 (2025)"]
        L5["SSS11 Phase 1 (C. utilis uricase)"]
        L6["Canakinumab FDA 2023 (gout)"]
        L7["TNFSF14 / LIGHT — emerging target"]
    end

    subgraph DiscoveryEngine["DISCOVERY ENGINE (methodology)"]
        DE1["Chokepoint Cascade Map"]
        DE2["Repurposing Surface"]
        DE3["Zileuton — CP6a 5-LOX (FDA asthma)"]
        DE4["Disulfiram — CP6b GSDMD (FDA alcohol)"]
        DE5["Avacopan — CP0 C5aR1 (FDA ANCA)"]
        DE6["Strain Library (synthesis output)"]
        DE7["Modality × Target Matrix — exploration surface"]
    end

    subgraph Androgens["ANDROGEN-URATE AXIS (NEW)"]
        S1["Testosterone (endogenous or exogenous)"]
        S2["Estradiol"]
        S3["SHBG (liver-produced, binds T)"]
        S4["URAT1 (apical reabsorption)"]
        S5["ABCG2 (apical secretion, kidney + gut)"]
        S6["Insulin sensitivity"]
        S7["Clomid / SERMs"]
        S8["Aromatase Inhibitors"]
    end

    subgraph ABCG2Mod["ABCG2 MODULATORS (NEW)"]
        AM1["Butyrate / SCFA from fermentable fiber"]
        AM2["Sulforaphane (Nrf2)"]
        AM3["TNFα / chronic inflammation"]
        AM4["Q141K polymorphism (gout-causing variant)"]
        AM5["Curcumin / Quercetin / EGCG (functional inhibitors)"]
    end

    %% Core relationships
    A1 --> B1
    A4 --> B1
    A2 --> D1
    A2 --> D2
    A3 --> D3
    A3 --> D4
    
    %% Problem to immune cascade
    B1 --> B2
    B2 --> C1
    C1 --> C2
    C2 --> C3
    C3 --> C4
    C4 --> C5

    %% Platform engineering
    D1 --> F1
    D2 --> F2
    D3 --> F3
    D4 --> F4
    
    F1 --> E1
    F1 --> E2
    F2 --> E2
    F3 --> E2
    F4 --> E2
    
    E1 --> E3
    E2 --> E3

    %% Wild-type baseline / home fermentation delivery formats
    %% (source: koji-home-fermentation.md)
    F9 -->|"wild-type koji produces"| F2
    F9 -->|"wild-type koji produces"| F3
    F9 -->|"wild-type koji produces"| F4
    F9 -->|"processed into"| F7
    F9 -->|"processed into"| F8
    F7 -->|"pre-digests protein in marinade"| A3
    F8 -->|"amylase-active digestive aid"| A3
    E2 -->|"engineered strain must outperform"| F9
    %% Koji-kin two-stage process (source: koji-home-fermentation.md)
    F10 -->|"inoculates steamed rice to produce"| F11
    F11 -->|"is the working enzyme substrate"| F9
    %% OTC PERT benchmark and dose-timing framework (source: digestive-enzyme-optimization.md)
    F12 -->|"40k FIP = ~9-10k USP (In Vitro)"| F2
    F12 -->|"n=1 dose-timing informs"| F13
    F13 -->|"2-cap or split-dose required for"| A3
    E2 -->|"1g engineered koji targets"| F12

    %% Mechanism pathway
    E1 --> G1
    E2 --> G1
    F5 --> G1
    G1 --> G2
    G2 --> G3
    G3 --> G4
    
    %% Barrier repair path
    I1 --> H1
    I1 --> H3
    I2 --> I4
    I4 --> H3
    H1 --> B3
    H3 --> B3
    
    %% NLRP3 inhibition path
    J1 --> J3
    J1 --> C2
    J2 --> J4
    J2 --> C2
    %% Colchicine: dual-hit CP2 (P2X7 pore block) + CP3 (microtubule-mediated ASC transport block)
    %% (source: colchicine.md; Leung 2015 PMID 26228647; Misawa 2013 PMID 23502856)
    J5 -->|"P2X7 pore block (CP2)"| C2
    J5 -->|"microtubule depolymerization blocks ASC transport (CP3)"| C3
    %% Colchicine cardiovascular repositioning (COLCOT/LoDoCo2 → Lodoco FDA 2023)
    %% and ULT-initiation prophylaxis role (source: colchicine.md)
    J6 -->|"ULT-initiation prophylaxis prevents dissolution flares"| C5
    J6 -->|"CV repositioning — NLRP3 suppression reduces plaque instability"| C2
    
    %% Metabolic modulation
    K1 --> K2
    K1 --> K3
    K1 --> K4
    K4 --> B4
    K2 --> J2

    %% Clinical precedent links
    L1 -.->|"validated mechanism, program ended"| G1
    L2 --> F1
    L3 --> B4
    L4 -->|"systemic IV, treatment-naive gout"| F1
    L5 -->|"C. utilis uricase, IV"| F1
    L6 -->|"approved IL-1b mAb"| C4
    L7 -->|"flare biomarker, distinct from NLRP3/IL-1b"| C5

    %% Barrier damage prevention
    B3 --> B5
    B4 --> B5
    B5 --> A3
    
    %% 5-LOX / LTB4 parallel neutrophil chemotaxis path (from nlrp3-inhibitor-screen.md ChEMBL cross-check)
    %% Now formally CP6a in v1.2 exploit map
    C1 -->|"MSU also drives 5-LOX"| N1
    N1 -->|"produces"| N2
    N2 -->|"recruits neutrophils"| N3
    N3 --> C5
    N4 -->|"inhibits at 300 nM"| N1
    N5 -->|"allosteric ~2.7 μM"| N1
    N6 -->|"substrate redirect → RvE1 (→ CP5b)"| N1

    %% CP0 — Complement C5a priming (v1.2 restructure, 2026-04-24)
    %% MSU directly activates complement → C5a → ROS → NLRP3 priming (Cumpelik 2016, Khameneh 2017)
    C1 -->|"MSU activates complement"| O1
    O1 -->|"binds"| O2
    O2 -->|"triggers ROS burst"| O3
    O3 -->|"primes NLRP3 (non-transcriptional)"| C2
    O4 -.->|"inhibits (pharma adjunct)"| O2
    O5 -->|"DAMP amplifies NF-κB priming"| Q2

    %% CP1a — TNFSF14 (LIGHT) amplifier (Round 1 work)
    Q1 -->|"amplifies via HVEM"| Q2
    Q2 -->|"transcriptional priming"| C2

    %% CP5b — ALX/FPR2 active resolution (v1.2 restructure, 2026-04-24)
    %% RvD1/MaR1 in MSU gout models (Zaninelli 2022 PMID 35716378, Jiang 2023 PMID 37996809)
    P2 -->|"activates"| P1
    P3 -->|"activates (AMPK/Nrf2 arm)"| P1
    P1 -->|"resolves"| P4
    P4 -.->|"resolves"| N3
    C4 -->|"GSDMD pore-driven NET release"| P5
    P5 -->|"sequesters cytokines → resolution"| P4
    P6 -->|"partial resolution overlap"| P1

    %% Multi-chokepoint proteins/compounds (v1.2 synthesis platform endgame)
    R1 -->|"LPS/CD14 + NF-κB suppression"| Q2
    R1 -->|"GSDMD direct suppression via mitophagy (Shan 2026 PMID 41524100)"| C4
    R1 -->|"partial SPM resolution overlap"| P1
    R2 -->|"proteasome block stabilizes IκBα → NF-κB"| Q2
    R2 -->|"suppresses caspase-1"| C4
    R3 -->|"FDA-approved 5-LOX inhibitor, gout-untested"| N1
    R4 -->|"removes upstream MSU crystal trigger"| C1

    %% Style the v1.2 additions distinctly
    linkStyle default stroke-width:1px
    classDef cp0Style fill:#ffccee,stroke:#cc0066,stroke-width:2px
    classDef cp5bStyle fill:#cce6ff,stroke:#0066cc,stroke-width:2px
    classDef multiCPStyle fill:#e6ffcc,stroke:#66aa00,stroke-width:2px
    class O1,O2,O3,O4,O5 cp0Style
    class P1,P2,P3,P4,P5,P6 cp5bStyle
    class R1,R2,R3,R4 multiCPStyle

    %% Androgen-urate axis (2026-04-24)
    %% Sex hormones gate the transporter biology that sits upstream of hyperuricemia
    S1 -->|"upregulates"| S4
    S1 -->|"suppresses"| S5
    S2 -->|"downregulates"| S4
    S2 -->|"boosts secretion via OAT1/3"| S5
    S4 -->|"↑reabsorption → hyperuricemia"| B1
    S5 -.->|"↓secretion → hyperuricemia (including gut-lumen sink ceiling)"| G1
    S3 -->|"binds T → lowers Free T for given Total T"| S1
    S6 -->|"suppresses SHBG synthesis; high sensitivity = ↑SHBG"| S3
    S7 -->|"↑endogenous T, modestly ↑SHBG, ↑E2"| S1
    S7 -->|"peripheral ER agonism"| S2

    %% ABCG2 modulators (2026-04-26)
    %% Pharmacological levers on the gut urate sink — separate from sex-hormone axis
    AM1 -->|"PPARγ activation → induction"| S5
    AM1 -->|"HDAC inhibition → trafficking rescue"| AM4
    AM2 -->|"Nrf2 activation → induction"| S5
    AM3 -->|"NF-κB → suppression"| S5
    AM4 -->|"folding/trafficking defect → reduced apical expression"| S5
    AM5 -->|"functional inhibition (acute, dose-dependent)"| S5
    S8 -->|"blocks T→E2 aromatization (↑T, ↓E2)"| S1
    S8 -.->|"loss of estrogen's urate-excretion boost"| S2

    %% Discovery engine → repurposing surface (source: open-enzyme-vision.md §2)
    DE1 -->|"produces"| DE2
    DE2 -->|"surfaces"| DE3
    DE2 -->|"surfaces"| DE4
    DE2 -->|"surfaces"| DE5
    DE1 -->|"synthesizes"| DE6
    DE3 -->|"CP6a 5-LOX inhibitor"| N1
    DE4 -->|"CP6b GSDMD inhibitor"| C4
    DE5 -.->|"CP0 C5aR1 antagonist (pharma adjunct)"| O2
    %% Modality × Target Matrix (source: modality-chokepoint-matrix.md)
    DE7 -->|"orthogonal exploration of"| DE1
    DE7 -->|"surfaces novel modalities for"| DE2

    %% Cannabinoid/terpene relationships
    M1 -->|"P2X7/NF-kB"| C2
    M2 -->|"CB2/TLR4/NLRP3 — MSU gout model"| C2
    M2 -->|"CB2 agonism — neutrophil block"| C1
    M3 -->|"NF-kB/MAPK — CIA arthritis"| C2
    M3 -->|"CBG colitis data"| B3
    M4 -->|"CB2 agonism (Ki 7.5 nM)"| C2
    M1 -->|"barrier support"| H1
    M5 -->|"Nrf2 + TLR4 suppression — MSU rat 50 mg/kg"| C2
    M5 -->|"NF-kB priming block"| C1

    %% Styling
    style Core fill:#ffe6e6
    style Problem fill:#fff0e6
    style Immune fill:#ffe6cc
    style Host_Enzyme fill:#e6f3ff
    style Platform fill:#e6ffe6
    style Delivery fill:#f0e6ff
    style Mechanism fill:#ffe6f0
    style Barrier fill:#f0f0f0
    style Peptides fill:#e6f9ff
    style Inhibitors fill:#fff9e6
    style Metabolic fill:#e6ffe6
    style Cannabinoids fill:#e6f0e6
    style Clinical fill:#f0e6ff
    style Parallel_Path fill:#fff0f5
    style Complement fill:#ffe0ee
    style Resolution fill:#e0efff
    style TNFSF14_arm fill:#fff5cc
    style MultiCP fill:#f0ffe0
    style Androgens fill:#e8d8f0
    style DiscoveryEngine fill:#fff8e6
```

## Key Pathway Descriptions

### 1. **Pathology → Immune Activation Loop**
- Hyperuricemia → MSU crystal formation → NLRP3 activation → IL-1β cascade → acute gout flare
- Enzyme deficits → poor luminal digestion → dysbiosis + barrier erosion → SIBO

### 2. **Uricase Platform Loop**
- Host loses uricase ~15M years ago → hyperuricemia endemic
- Engineer S. cerevisiae or A. oryzae with uricase gene
- Ferment at home → colonize gut lumen
- Degradation in situ → uric acid ↓ → MSU crystals prevented

### 3. **Barrier Repair + Immunomodulation**
- BPC-157 + KPV → tight-junction integrity
- Integrity → reduced inflammatory translocation
- Reduced NLRP3 priming + oridonin/disulfiram for inflammasome block = dual suppression

### 4. **Metabolic Synergy**
- BHB (ketones) → NLRP3 inhibition + probiotic fitness
- Engineered strains (engineered S. cerevisiae/A. oryzae) outcompete pathogens
- Prevents SIBO; supports barrier homeostasis

### 5. **Combinatorial Stack** (Full Gout Resolution)
```text
Engineered Uricase (S. cerevisiae)
    ↓
Gut-Lumen Sink (enzymatic uric acid ↓)
    ↓
BPC-157 (barrier repair)
    ↓
Oridonin (NLRP3 direct inhibition)
    ↓
BHB (metabolic support + probiotic advantage)
    ↓
**Complete flare prevention + remission**
```

## Reading the Graph

- **Boxes** = Concepts (conditions, molecules, mechanisms, platforms)
- **Arrows** = Causal or mechanistic relationships
- **Colors** = Domains (pathology=red, immune=orange, platform=green, etc.)
- **Subgraphs** = Grouped by functional domain for easier navigation

### High-Level Dependencies

**Must-Have (Gout):**
- Uricase platform (S. cerevisiae or A. oryzae)
- Gut-lumen sink mechanism
- NLRP3 inhibition (any of: oridonin, disulfiram, or dietary BHB)

**Enhanced (Barrier + Metabolic):**
- BPC-157 or KPV (barrier repair)
- BHB (ketogenic state or supplementation)
- Probiotic advantage via metabolic modulation

**For EPI:**
- Engineered A. oryzae with multi-enzyme expression (lipase, protease, amylase)
- Same barrier repair stack (BPC-157 + BHB)
- SIBO prevention via microbiome management

---

## Related Documentation

See [wiki/INDEX.md](INDEX.md) for detailed concept pages.  
See `docs/` folder for full research citations and methodology.
