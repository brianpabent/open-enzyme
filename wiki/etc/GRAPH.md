# Open Enzyme Dependency Graph

This graph is a compact routing surface for current decisions. It does not rank interventions, chassis, UOX sequences, topologies, or product formats. Scientific evidence and limitations live in the linked topic pages.

## Portfolio map

```mermaid
flowchart TD
    M["Mission: identify exploitable gout weaknesses and test engineered exploits"]
    S["System map: urate production, transport, crystallization, inflammation, and resolution"]
    P["Portfolio of independently falsifiable tracks"]

    T1["Urate-production and transporter tracks"]
    T2["Luminal UOX hypothesis"]
    T3["Local-tissue and systemic UOX routes"]
    T4["Inflammation and resolution tracks"]
    T5["Other disposal and delivery mechanisms"]

    M --> S
    S --> P
    P --> T1
    P --> T2
    P --> T3
    P --> T4
    P --> T5
```

The system map routes questions to distinct tests. Evidence for one route does not transfer to another, and failure of one track does not stop the portfolio.

## Luminal UOX decision path

```mermaid
flowchart TD
    H08["H08: luminal UOX sink remains an open hypothesis"]
    C44["comp-044: legacy unconditional flat-dose classification was not robust to the tested diagnostics"]
    V["Candidate UOX sequences remain unranked"]
    CH["Candidate yeast, koji, bacterial, and cell-free configurations remain unranked"]
    B["Verified matched constructs: identity, active UOX, localization, process retention, and controls"]
    G133["§1.33: configuration-level physiological substrate × oxygen × peroxide"]
    G136["§1.36: urate antioxidant loss × H2O2 × epithelial safety"]
    NEXT["Later dynamic modeling and translational study design"]
    REDIRECT["Stop or redesign only the failed configuration"]

    H08 --> C44
    C44 --> G133
    V --> B
    CH --> B
    B --> G133
    G133 -->|"passes matched reaction-site rule"| G136
    G133 -->|"fails"| REDIRECT
    G136 -->|"supports further study"| NEXT
    G136 -->|"fails"| REDIRECT
```

### What the edges mean

- **comp-044 → §1.33:** COMP-019's unconditional flat-dose classification is not robust to COMP-044's tested substrate-occupancy and finite-window diagnostics. The audit supplies no replacement ΔSUA, dose, genotype order, physiological regime, efficacy model, topology/chassis selection, production-sufficiency target, or safety conclusion. **Mechanistic Extrapolation.**
- **Construct build → §1.33:** protein mass, transcript, promoter strength, or activity at a high-substrate benchmark is insufficient. The decision variable is reproducible active UOX at the intended reaction site under the matched physiological test.
- **§1.33 → §1.36:** only an exact configuration with product formation at the human-baseline prior, without a prespecified extracellular-H2O2 or viability penalty relative to matched controls, advances to the dedicated epithelial-safety test. A topology conclusion is transferable only within a controlled host comparison.
- **§1.36 → later work:** lower H2O2 alone does not pass if barrier injury persists after urate removal. A pass supports designing the next study; it does not establish a human dose or serum-urate effect.
- **Failure → redirect:** a failed sequence, topology, chassis, or process updates only that tested configuration.

## Evidence and decision homes

- [Mission and operating principles](./open-enzyme-vision.md)
- [Gout system map](../gout-pathophysiology.md)
- [Modality × target matrix](../modality-chokepoint-matrix.md)
- [Delivery route × compound-class matrix](../delivery-route-matrix.md)
- [Chassis-pending interventions](../chassis-pending-interventions.md)
- [Gut-lumen UOX sink](../gut-lumen-sink.md)
- [Systemic UOX delivery attack surface](../blood-barrier-exploits.md)
- [UOX variant selection](../uricase-variant-selection.md)
- [Yeast UOX research plan](../engineered-yeast-uricase-proposal.md)
- [Koji UOX construct screen](../koji-construct-design.md)
- [comp-044 physiological-regime audit](../gut-lumen-uricase-physiologic-regime-computational.md)
- [comp-045 topology × oxygen × peroxide design](../uricase-topology-oxygen-peroxide-design-computational.md)
- [Validation experiments §§1.33 and 1.36](../validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial)
- [Open Enzyme dashboard](../../index.md)
