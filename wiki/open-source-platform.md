---
title: Open Source Platform
aliases: [platform, github-model, strain-library, forkable-strains, decentralized-biology]
related: [validation-experiments, open-enzyme-vision, engineered-yeast-uricase, engineered-koji-protocol]
sources: [open-enzyme-vision.md]
---

# Open Source Platform

## Vision

An open source library of food-grade, engineered microbial strains — each producing a therapeutic enzyme, each growable at home, each freely available to anyone. The GitHub model applied to therapeutic enzyme engineering.

---

## The Software Analogy

The architecture snaps into focus when you think of it as software infrastructure:

| Software World | Open Enzyme |
|---|---|
| Repository | Strain definition (enzyme + host + construct) |
| Source code | Gene construct (promoter + gene + terminator) |
| Runtime / VM | Host organism (S. cerevisiae, A. oryzae, etc.) |
| Deployment | Fermentation protocol (grow on rice, dry, capsule) |
| Dependencies | Selection markers, auxotrophies, media recipes |
| CI / Testing | In vitro activity assays, biomarker tracking |
| Fork & PR | Modify a strain, contribute improvements back |
| Release | Validated strain with full documentation |

(Source: open-enzyme-vision.md, §3)

---

## Platform Principles

### 1. No Patents

Every strain, construct, and protocol is open source. Patent-free. The point is accessibility. If this works, it should be available to every gout patient, every person with digestive enzyme insufficiency, every family managing phenylketonuria — not locked behind intellectual property walls.

(Source: open-enzyme-vision.md, §10)

### 2. GRAS Organisms Only

Every strain is built in a host organism that has FDA GRAS (Generally Recognized As Safe) status and centuries of safe human consumption. We use established transformation methods with known safety profiles.

Current approved hosts:
- *Saccharomyces cerevisiae* (baker's yeast)
- *Saccharomyces boulardii* (probiotic yeast variant)
- *Aspergillus oryzae* (koji mold)

Possible future hosts (all GRAS):
- *Lactobacillus plantarum*
- *Bacillus subtilis*
- *Kluyveromyces lactis*

(Source: open-enzyme-vision.md, §10)

### 3. Rigorous But Accessible

Every protocol is followable by a motivated non-scientist with basic lab access (community biolab level). But "accessible" never means "sloppy." Documentation is detailed, methods are validated, results are quantified.

This is the bridge between citizen science and pharmaceutical rigor.

(Source: open-enzyme-vision.md, §10)

### 4. Community Validation Through Replication

Replication is not optional — it's the core quality mechanism. Encourage independent reproduction. Share all results (including failures). Build a community of practice around each strain.

The distributed nature of the platform means each person working with a strain is both a user and a QA engineer.

(Source: open-enzyme-vision.md, §10)

### 5. Not Medical Advice

This is citizen science, self-experimentation, and open knowledge sharing. We document what we build, what we observe, and what the published literature supports. We do not prescribe, diagnose, or claim to cure.

(Source: open-enzyme-vision.md, §10)

---

## Strain Repository Structure

Each strain in the library follows this documentation format:

```text
strains/
├── uricase-yeast/
│   ├── README.md (overview, purpose, key claims)
│   ├── CONSTRUCT.md (gene map, promoters, regulatory elements)
│   ├── PROTOCOL.md (step-by-step transformation, validation)
│   ├── ACTIVITY_DATA.md (uricase specific activity, conditions)
│   ├── FERMENTATION.md (growth conditions, media, timeline)
│   ├── DOSING.md (estimated therapeutic dose, bioavailability)
│   ├── SAFETY_DATA.md (toxicology, off-target effects, conflicts)
│   ├── CHANGELOG.md (versions, improvements, contributors)
│   └── CONTRIBUTORS.md (who built this, reproducibility)
│
├── koji-digestive/
│   ├── (same structure)
│   └── DUAL_EXPRESSION.md (if expressing multiple enzymes)
│
└── [future strains as developed]
```

---

## GitHub Workflow for Strains

### 1. Create a Strain

Submit a pull request adding a new strain directory with:
- Gene construct documentation (source gene, codon optimization, regulatory elements)
- Transformation protocol (detailed, replicable)
- Validation data (in vitro activity assays, expression levels)
- Proposed fermentation format (beverage, powder, food)
- Preliminary safety assessment

**Example:** "Add uricase-yeast strain expressing A. flavus uaZ in S. cerevisiae with pTEF1 promoter"

---

### 2. Fork & Improve a Strain

Modify an existing strain and propose changes:

**Examples of forks:**
- Change promoter (stronger/weaker expression)
- Add second enzyme (dual-expression strain)
- Optimize for different host organism
- Improve secretion signal (increase extracellular activity)
- Engineer for different fermentation format

**Example PR:** "Improve koji-digestive: add secretion signal for enhanced lipase yield in fermentation"

---

### 3. Validation Data Repository

A parallel data directory logs:
- Replication attempts (successful and failed)
- Biomarker data from users
- Activity assays from community labs
- Safety observations
- Manufacturing notes (scalability, shelf life, contamination patterns)

```text
validation_data/
├── uricase-yeast/
│   ├── activity_assays/ (institution, date, method, results)
│   ├── fermentation_trials/ (batch size, yield, enzyme stability)
│   ├── user_outcomes/ (biomarker tracking, flare frequency, adverse events)
│   └── manufacturing_notes/ (community biolab batch reports)
└── [strain]/
```

---

## Current Strains (Roadmap)

### Tier 1: Foundation Strains (Under Active Development)

**Uricase-Yeast**
- Status: Phase 1 in vitro validation (engineered-yeast-uricase-proposal.md)
- Host: S. cerevisiae
- Gene: A. flavus uaZ
- Timeline: Q2–Q3 2026 (Phase 1–2)
- Purpose: Reduce serum uric acid via gut-lumen degradation

**Koji-Digestive**
- Status: Phase 1 optimization (engineered-koji-protocol.md)
- Host: A. oryzae (wild-type for now)
- Enzymes: Native lipase, protease, amylase
- Timeline: Q2 2026 (ready for Phase 2 EPI validation)
- Purpose: Digestive enzyme supplementation for pancreatic insufficiency

---

### Tier 2: Planned Strains (Design Phase)

**Koji-Dual-Enzyme** (Uricase + Digestive Enzymes)
- Status: Design phase (engineering feasibility confirmed in nlrp3-exploit-map.md, §3)
- Host: A. oryzae
- Genes: Native lipase/protease/amylase + engineered A. flavus uaZ
- Timeline: Q3–Q4 2026 (after individual components validated)
- Purpose: Single organism addressing both enzyme deficiencies

**Lactase-Yeast**
- Status: Early design (open-enzyme-vision.md, §4 — expanding library)
- Host: S. cerevisiae
- Gene: Lactase (TBD source; *K. lactis* native or heterologous)
- Timeline: 2027 (not prioritized; global lactose intolerance ~4.7B people but most manage via diet/supplements)
- Purpose: Lactose intolerance support

**Oxalate-Decarboxylase-Yeast**
- Status: Early design
- Host: S. cerevisiae
- Gene: Oxalate decarboxylase from *Oxalobacter formigenes* or engineered
- Timeline: 2027
- Purpose: Oxalate kidney stone prevention (~10% lifetime prevalence)

---

### Tier 3: Future Strains (Long-term)

- **Phenylalanine hydroxylase** (PKU): Rare genetic disorder, small patient population, complex enzyme
- **Diamine oxidase** (Histamine intolerance): ~1–3% population prevalence; less studied
- **Multi-enzyme strains** combining 3+ enzymes in single organism (depends on expression stability)

---

## Quality Gates: From Idea to "Release"

### Pre-Alpha (Design Phase)
- Literature review complete
- Gene source identified and sequenced
- Transformation strategy designed
- **Deliverable:** CONSTRUCT.md + literature references

### Alpha (Laboratory Phase)
- Gene synthesized and basic transformation confirmed
- In vitro activity assay demonstrates enzyme function
- Stability tests pass (pH, temperature, drying)
- **Deliverable:** PROTOCOL.md + ACTIVITY_DATA.md + preliminary safety notes

### Beta (Small-Scale Validation Phase)
- Protocol replicated by second independent lab (or community biolab)
- Animal model data (Phase 2) complete
- Fermentation format optimized
- Safety and tolerability assessment updated
- **Deliverable:** Validated PROTOCOL.md + FERMENTATION.md + animal data summary

### Release (Approved for Community Use)
- At least two independent replications confirmed
- Phase 3 human self-experimentation data available (or planned)
- Full SAFETY_DATA.md documented
- Community feedback incorporation (bug fixes, improvements)
- **Deliverable:** Complete strain directory + user guide + disclaimer

---

## Example: Uricase-Yeast Strain Card

```markdown
# Uricase-Yeast (v1.0)

## Summary
S. cerevisiae expressing A. flavus uricase for oral uric acid degradation.
Targets gut-lumen uric acid via ABCG2 intestinal secretion pathway.

## Key Data
- Expression level: ~13% total cellular protein
- Specific activity: 365 μmol/h/OD
- Target dose: 10–20g lyophilized yeast daily
- Estimated serum uric acid reduction: 15–30%

## Host Organism
- *Saccharomyces cerevisiae*
- GRAS status: Yes (FDA, decades of safe use)
- Genetic tractability: Excellent (most developed eukaryotic expression system)

## Gene
- Source: *Aspergillus flavus* uaZ (urate oxidase)
- GenBank: X61766.1 (also used in Elitek/rasburicase)
- Codon-optimized: Yes, for S. cerevisiae
- Size: ~906 bp coding sequence

## Expression Cassette
- Promoter: pTEF1 (constitutive, strong)
- Signal peptide: Optional (α-factor for secretion, or intracellular)
- Terminator: CYC1
- Integration: Chromosomal (markerless with CRISPR recommended for scale)

## Fermentation Formats
1. Lyophilized powder (capsules) — best for dosing control
2. Kvass/water kefir fermented beverage — live cells, active enzyme
3. Nutritional yeast powder — traditional format, stability TBD
4. Live S. boulardii probiotic — daily dosing, transit organism

## Validation Status
- In vitro: ✓ (Phase 1 complete, Q2 2026)
- Animal models: ✓ (Phase 2 complete, hyperuricemic rats, Q3 2026)
- Human self-experimentation: 🔄 (Phase 3 ongoing, Q4 2026 expected)

## Sourcing the Strain
1. Request from Open Enzyme repository (free, open source)
2. Transform into your own S. cerevisiae background (lab or community biolab)
3. Or: Obtain from ATCC or other culture collection once strain is deposited (post-validation)

## Cost to Reproduce
- Gene synthesis: ~$100
- Transformation reagents: $200–500
- Screening assays: $300–500
- **Total:** ~$600–1,100 for lab-scale development

## How to Contribute Improvements
1. Fork the strain repository
2. Make modifications (promoter change, codon optimization variant, dual-expression version)
3. Validate in your lab
4. Submit pull request with data
5. Community review + merge if reproducible

## Safety & Disclaimers
- Strain uses GRAS organism with 70+ years safety history
- Uricase is the same enzyme as FDA-approved rasburicase (IV drug)
- Oral formulation (gut lumen expression) avoids systemic enzyme exposure
- No modified antibiotic resistance genes (marker-free)
- Preliminary human data available; long-term safety TBD

## Related Strains
- Koji-digestive (complementary digestive enzyme support)
- Koji-dual-enzyme (when available; same uricase, different host)

## Funding/Contributors
- Design: Brian Abent (Open Enzyme)
- Validation (potential collaborators, not yet confirmed): Rheinallt Jones (Emory Gnotobiotic Core), Lauren Collier-Hyams (pharma expertise)
- Community reproducers: [Your lab name here]

## Next Steps
- Extend Phase 3 to 6-month long-term flare prevention trial
- Optimize fermentation for higher enzyme yield
- Develop plant-based encapsulation (algae capsules)
- Explore dual-expression version with digestive enzymes
```

---

## Community Tools & Infrastructure

### 1. Strain Registry

A searchable database (GitHub, or dedicated site) listing:
- All strains with current status (alpha/beta/release)
- Key performance data (enzyme activity, yield)
- Contributors and replications
- Links to protocols and validation data

### 2. Discussion Forum / Chat

- Slack, Discord, or GitHub Discussions for:
  - Technical troubleshooting
  - Fermentation sharing
  - Biomarker results discussion
  - Cross-strain engineering ideas

### 3. Community Biolab Network

Partner with existing community biolabs (BioCurious, Genspace, Community Lab, etc.) to:
- Provide transformation services
- Host validation experiments
- Train users on strain propagation
- Share equipment access

### 4. Manufacturing SOP Archive

Once a strain is validated, document manufacturing at scale:
- Commercial fermentation (GMP considerations if needed)
- Shelf-life testing (stability at different storage conditions)
- Contamination prevention (especially important for food organisms)
- Cost breakdown (materials, labor, equipment)

---

## Licensing & IP

**All strains released under:**
- **Construct DNA:** CC-BY-SA 4.0 (open attribution, share-alike)
- **Protocols:** CC-BY-SA 4.0
- **Strain deposits:** Made available to ATCC or other culture collections with public access
- **No patent claims:** Explicit waiver of patent rights

This ensures:
- Researchers can use, modify, improve, share
- Commercial use is allowed (but not proprietary derivatives)
- Anyone can manufacture and distribute improved versions
- Patent landscape is clear (not locked by defensive patents)

(Source: open-enzyme-vision.md, §10)

---

## The Vision in Action

**Year 1 (2026):**
- Validate uricase-yeast (Phase 1–2–3)
- Release koji-digestive (Phase 1–2 complete, Phase 3 ongoing)
- Establish community reproducers network

**Year 2 (2027):**
- Release uricase-yeast to community
- Begin koji-dual-enzyme validation
- Expand strain library to lactase-yeast (design + Phase 1)
- Document manufacturing for scale (GMP-lite)

**Year 3+ (2028+):**
- 5–10 validated strains in library
- Decentralized production (anyone can grow approved strains)
- Self-sustaining community of contributors
- Potential commercial partnerships (non-exclusive, open source terms)

---

## Not a Company (Yet)

This is a passion project born from personal necessity, built in the open. If it grows into something larger, it will be because:
1. The science worked
2. The community demanded it
3. The open source model proved sustainable

The goal is not venture funding or IPO. The goal is accessibility.

(Source: open-enzyme-vision.md, §11)

---

*This platform is a living system. As [[validation-experiments]] advance and community contributions grow, this document will evolve. The core principle remains: open source, GRAS organisms, community validation, no patents.*

*Fork freely. Replicate fearlessly. Share everything.*
