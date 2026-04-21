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
    end

    subgraph Metabolic["METABOLIC MODULATION"]
        K1["Beta-Hydroxybutyrate"]
        K2["Ketogenic State"]
        K3["HDAC Inhibition"]
        K4["Probiotic Fitness"]
    end

    subgraph Clinical["CLINICAL PRECEDENT"]
        L1["ALLN-346"]
        L2["Rasburicase"]
        L3["PULSE Probiotic"]
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
    
    %% Metabolic modulation
    K1 --> K2
    K1 --> K3
    K1 --> K4
    K4 --> B4
    K2 --> J2

    %% Clinical precedent links
    L1 --> G1
    L2 --> F1
    L3 --> B4

    %% Barrier damage prevention
    B3 --> B5
    B4 --> B5
    B5 --> A3
    
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
    style Clinical fill:#f0e6ff
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
```
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
