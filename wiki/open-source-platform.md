---
title: Open Source Platform
aliases: [platform, github-model, strain-library, forkable-strains, decentralized-biology]
related: [validation-experiments, open-enzyme-vision, engineered-yeast-uricase, engineered-koji-protocol]
sources: [open-enzyme-vision.md]
---

# Open Source Platform

## Vision

An open source library of food-grade, engineered microbial strains — each producing a therapeutic enzyme, each growable at home, each freely available to anyone. The GitHub model applied to therapeutic enzyme engineering.

The library is one of two parallel outputs of the Open Enzyme project. The other is a **discovery engine** — a chokepoint-based methodology for mapping every vector that causes, treats, or mitigates a given disease, applied first to gout. The discovery engine produces a structured cascade map plus a repurposing surface (FDA-approved drugs that hit relevant chokepoints but were never clinically tested for the target disease). The strain library is one synthesis from the discovery engine; the engineered-koji platform converged from the gout vector mapping. (source: open-enzyme-vision.md, §1–2)

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

## Platform Architecture — Koji-First, Yeast Retained for Specific Modules

Open Enzyme supports two GRAS hosts, but the platform is **koji-first** for the therapeutic stack, with *S. cerevisiae* retained for specific modules where yeast expression is better characterized or more likely to succeed. (source: open-enzyme-vision.md, §4)

**Why koji-first (*A. oryzae* as primary host):**
- Secretion capacity: native koji secretes 25–30 g/L into growth media (industrial fermentation); *S. cerevisiae* typically reaches 0.5–2 g/L for heterologous secreted proteins — an order-of-magnitude advantage for any secreted enzyme. (Mechanistic Extrapolation)
- Multi-enzyme baseline: wild-type koji already produces lipase, protease, and amylase at therapeutically relevant levels, plus natural kojic acid, ergothioneine, and ferulic acid — pathway-modulator-adjacent compounds on day zero, before any engineering.
- Home-fermentation feasibility: koji grows on steamed rice at 30°C in 36–48 hours with no bioreactor required.
- Food precedent: 1,000+ years of human consumption in East Asian cuisine; FDA GRAS status.
- Dose scalability: ~10–15 g of engineered koji is in the therapeutic ballpark for Creon-equivalent digestive enzyme dosing.

**Why yeast is retained (*S. cerevisiae* for specific modules):**
Some heterologous compounds may express better in *S. cerevisiae* than *A. oryzae* — particularly tetrameric proteins (the rasburicase precedent: *A. flavus* uricase expressed in *S. cerevisiae* reportedly reaches 13% of total cellular protein). Specific open decision points include ursolic acid (8.59 g/L record in engineered *S. cerevisiae*; untested in koji), carnosine (biosynthesis requires heterologous carnosine synthase; host choice open), and uricase itself (rasburicase proves the *S. cerevisiae* path works; the koji path needs to be developed). These are empirical questions, not ideological ones. (source: open-enzyme-vision.md, §4)

**Platform positioning:** Open Enzyme is a **food-derived, multi-target NLRP3 pathway modulator** platform — not an attempt to produce a food-grade analog of the direct NLRP3 inhibitor class (MCC950, dapansutrile, oridonin). The stack is overwhelmingly pathway modulators — hitting upstream priming (CP1a/CP1b), K⁺ efflux (CP2), active resolution (CP5b), and neutrophil amplification (CP6a) — chokepoints that pharma has not rigorously tested in gout. Multi-target pathway modulators hitting redundant nodes can plausibly produce meaningful IL-1β suppression through cumulative effect, even if no single compound matches pharma-grade potency at a single target. (source: open-enzyme-vision.md, §10; nlrp3-inhibitor-screen.md; nlrp3-exploit-map.md)

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

### 5. Open Substrate for AI-Assisted Peer Review

Because the wiki source is public markdown at a stable URL, it also functions as an open substrate for AI-assisted peer review. Any collaborator can point their own AI — Claude, GPT, Codex, or any other — at this repository, run a rigor check, and contribute findings back via PR or synthesis entry. Traditional peer review is ~10 hours × 2–3 reviewers × weeks of back-and-forth. AI-assisted review on a shared substrate is ~20 minutes × unbounded reviewers × async. Disagreements between different AIs, grounded in the same inspectable evidence, become productive signals — pointing humans at the exact places where manual digging pays off, rather than hiding in private inference. Evidence-level tags, the ChEMBL cross-check, and the [Falsification Lint design](./linter-design.md) are the rigor discipline that makes this substrate trustworthy enough for that pattern to work. (source: open-enzyme-vision.md, §4)

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

## Open Questions — Reliability of Community Fermentation

The "grown at home like sourdough starter" framing is central to the platform's accessibility thesis, but home fermentation introduces a set of reliability problems that pharma-grade production avoids by brute force (controlled bioreactors, GMP SOPs, antibiotic selection, cold chain). These problems are **tractable**, not disqualifying — but they need explicit mitigation paths, not hand-waving.

### 1. Strain Stability Across Generations *(Mechanistic Extrapolation)*

A food-grade strain by design carries no antibiotic resistance marker, which is correct for GRAS compliance but removes the selection pressure that keeps the engineered construct in the population. Across multiple propagation generations — users backslopping from batch to batch like a sourdough starter — cells that have lost or silenced the construct can outcompete producers (heterologous expression imposes a growth cost; non-producers grow faster). This is a well-characterized problem in industrial fermentation and is the reason commercial strains are propagated from frozen master cell banks, not serially passaged.

**Mitigation:** chromosomal integration rather than plasmid-based expression (integrated copies are far more stable than 2μ plasmids without selection — see [engineered-yeast-uricase-proposal.md](./engineered-yeast-uricase-proposal.md) §2). Genetic redundancy (multiple integrated copies) further delays loss. For koji, integration into a well-characterized locus is standard practice.

### 2. Reproducibility Across Users *(Mechanistic Extrapolation)*

A hundred home fermenters in a hundred kitchens with different rice brands, different humidity, different ambient temperatures, and different incubation practices will not produce consistent enzyme titers. Even professional koji producers see batch-to-batch variation; amateur variation will be much larger. The risk isn't catastrophic failure — it's *silent underdosing*, where a batch produces 20% of the expected enzyme titer and the user never knows.

**Mitigation:** a "first-batch QC protocol" that users can run at home or at a community biolab — a simple uric-acid-degradation assay on a small sample of the fermented product (uric acid absorbs at 293 nm; a $50 spectrophotometer or even a smartphone-camera-based colorimetric assay is sufficient for go/no-go). Coupled with the feedback loop in §4 below, this turns batch variation into a visible, correctable problem rather than a silent one.

### 3. Contamination *(Mechanistic Extrapolation)*

Home environments are not sterile. Wild-type *A. oryzae* spores are ubiquitous in any kitchen that has ever used miso or soy sauce; wild *Saccharomyces* are ubiquitous period. Co-fermentation between the engineered strain and a wild-type contaminant will, over multiple generations, drift toward the faster-growing contaminant (which is almost always the wild-type — see strain-stability point above). Single-batch contamination is not a therapy-failure event; multi-generation drift is.

**Mitigation:** explicit "never backslop past generation N" guidance (N likely 3–5, to be determined empirically), with users returning to a frozen/lyophilized master stock for each new starter culture. This breaks the contamination-drift chain at the cost of requiring a kept master stock.

### 4. Regulatory Status of Engineered Spore Distribution *(Open)*

Distributing lyophilized spores of an engineered food-grade organism to end users may count as GM organism release under multiple regulatory frameworks (FDA for food additives; USDA for agricultural organisms; state-level GM labeling laws; EPA TSCA for "microbial commercial activities"). The GRAS status of the *host* organism does not automatically extend to an engineered derivative distributed at scale. This is distinct from (and more restrictive than) purchasing wild-type koji spore online, which is currently legal and uncontroversial.

This is flagged as **Open** — not settled — and requires a legal review *before* any broad community distribution. A narrower path (distributing the *construct sequence* as open-source DNA, with the transformation step performed by each user or their community biolab) is legally cleaner but raises the barrier to entry. The trade-off is real and should not be papered over.

### Proposed Strain Stability Kit

To operationalize the mitigations above, a "Strain Stability Kit" is the natural artifact:

- **Frozen / lyophilized spore stock** — 2+ year viability under ambient-mail shipping conditions. Users return to this stock for each new starter, limiting generation depth.
- **Positive control** — wild-type koji spores, to verify the user's fermentation technique in parallel with the engineered strain.
- **Negative control** — blank sterile rice substrate, to check for environmental contamination.
- **QC protocol** — simple spectrophotometric or colorimetric uric-acid-degradation assay, runnable at batch #1, batch #5, batch #10. Titer values uploaded to a community GitHub repo alongside conditions (humidity, temperature, rice cultivar, day of first visible growth).

### Community Feedback Loop

A GitHub repository (per strain, under the Open Enzyme organization) for fermentation logs — user-uploaded titers, conditions, and outcomes. Over hundreds of batches, patterns emerge: which rice cultivars consistently underperform, which ambient temperatures tank titers, how titer correlates with generation number. This turns community reproducers into a distributed QA system. It also provides the evidence base for revising the "never backslop past generation N" guidance as empirical data replaces extrapolation.

**None of these mitigations are fully validated as of Phase 0.** They are engineering sketches, not SOPs. The first real test will come during Phase 2 community replication, and the protocols above will be revised (probably substantially) based on what the first dozen community batches actually look like.

---

*This platform is a living system. As [[validation-experiments]] advance and community contributions grow, this document will evolve. The core principle remains: open source, GRAS organisms, community validation, no patents.*

*Fork freely. Replicate fearlessly. Share everything.*
