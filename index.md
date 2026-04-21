# Open Enzyme

Open source library of engineered, food-grade microbial strains producing therapeutic enzymes. Phase 0 — Research & Design.

**First targets:** Uricase (gout / hyperuricemia + NLRP3-driven inflammation) · Digestive enzymes (EPI) · Koji (*A. oryzae*) as a natural multi-enzyme producer.

---

## Status

**Current platform thesis:** One engineered *A. oryzae* koji strain expressing uricase + NLRP3 inhibitors, fermented on rice bran, positioned as adjunct to allopurinol for gout — not a monotherapy replacement. Derivation in [wiki/synthesis.md](wiki/synthesis.md).

**Synthesis queue:** [wiki/synthesis.md](wiki/synthesis.md) — unreviewed cross-analysis findings. The sweep daemon prepends new findings here after each save; prune by deleting bullets you've acted on. Git preserves the full history.

**Cheapest next experiments** (from current synthesis, ordered by cost/ROI):

| # | Experiment | Cost | Weeks | Decides |
|---|---|---|---|---|
| 1 | Rice bran vs plain rice substrate → uricase GI survival | $800 | 3 | Free substrate optimization, no engineering |
| 2 | Quercetin + ursolic acid + carnosine combo on MSU-stimulated macrophages | $1,500 | 4 | Whether to engineer one NLRP3 inhibitor or three |
| 3 | WT / SB-1 / OPT-1 engineered uricase variants in koji → GI simulation | $2,000 | 8 | Platform choice (koji vs yeast) |

See [wiki/validation-experiments.md](wiki/validation-experiments.md) for the full consolidated experiment list.

---

## Core Pathology & Targets

- **[Gout Pathophysiology](wiki/gout-pathophysiology.md)** — Complete gout cascade: purine metabolism → uric acid → crystallization → NLRP3 → flare; current treatments; clinical pipeline; genomics (351 GWAS loci)
- **[Uricase (Urate Oxidase)](wiki/uricase.md)** — The missing enzyme: evolutionary loss ~15Mya, A. flavus uaZ gene, rasburicase, engineering for gut-lumen degradation
- **[NLRP3 Inflammasome](wiki/nlrp3-inflammasome.md)** — All 6 chokepoints mapped; MSU crystal activation; priming/activation two-signal model; pharmaceutical targets (dapansutrile, firsekibart)
- **[Digestive Enzymes & EPI](wiki/digestive-enzymes.md)** — Lipase, protease, amylase deficits; wild-type koji as immediate solution; commercial supplements (Creon, Zenpep)
- **[SIBO](wiki/sibo.md)** — Lynn's condition; brush-border enzyme damage; NLRP3 involvement; KPV relevance
- **[Fructose Connection](wiki/fructose-connection.md)** — Hidden gout accelerant: fructokinase (no negative feedback), ATP depletion cascade, GLUT9 dual transporter, KHK inhibitors

## Engineered Organisms & Platforms

- **[Saccharomyces cerevisiae](wiki/saccharomyces-cerevisiae.md)** — GRAS yeast; rasburicase expression precedent; S. boulardii; expression systems (TEF1p, GPDp); delivery formats
- **[Aspergillus oryzae](wiki/aspergillus-oryzae.md)** — Koji mold; native enzyme production; transformation methods; dual-purpose strain vision; fermentation on rice
- **[Open Source Platform](wiki/open-source-platform.md)** — GitHub strain library vision; software analogy; no patents; community validation; forkable strains

## Delivery & Barrier Biology

- **[Gut-Lumen Sink](wiki/gut-lumen-sink.md)** — ABCG2 pathway; ~1/3 of UA excretion; the insight that systemic absorption isn't needed; ALLN-346, PULSE probiotic
- **[Blood Barrier](wiki/blood-barrier.md)** — Every delivery route evaluated; why systemic delivery is hard; why gut-lumen wins

## Gene Therapy

- **[CRISPR Uricase](wiki/crispr-uricase.md)** — Georgia State breakthrough (2025); ancestral uricase reconstruction; pseudogene reactivation; delivery vectors (LNP, AAV, base editing)

## Peptides & Compounds

- **[BPC-157](wiki/bpc-157.md)** — 15-amino-acid gastric peptide; NO system modulation; gut healing; gout relevance via gut-UA axis
- **[KPV Tripeptide](wiki/kpv-peptide.md)** — α-MSH fragment; dual NF-κB + NLRP3 inhibition; gut anti-inflammatory; strongest mechanistic case for gout
- **[BHB / Ketones](wiki/bhb-ketones.md)** — Hits 3 of 6 NLRP3 chokepoints; endogenous via fasting/keto; may be more impactful than any single peptide
- **[Oridonin](wiki/oridonin.md)** — Natural NLRP3 inhibitor; covalent NACHT domain Cys279 binding; traditional medicine origin
- **[Disulfiram](wiki/disulfiram.md)** — Gasdermin D blocker (Antabuse); repurposed drug; Chokepoint 5 in NLRP3 map

## Strategy & Practice

- **[Supplements Stack](wiki/supplements-stack.md)** — Practical NOW/SOON/FUTURE recommendations with dosing and evidence levels
- **[Validation Experiments](wiki/validation-experiments.md)** — All proposed experiments consolidated: in vitro, animal, and human self-experimentation phases
- **[Bio-AI Tools](wiki/bio-ai-tools.md)** — Open source protein AI (ESM-2, ColabFold, Boltz-2, RFdiffusion2, ProteinMPNN, SPURS, DiffDock, CodonTransformer) + commercial tools (GPT-Rosalind, Amazon Bio Discovery, Coefficient Bio); project-specific prompts and workflow

## Team

- **[Team](wiki/team.md)** — Brian Abent (Platform/Engineering, sole current member); potential collaborators: Rheinallt Jones PhD (Gut Microbiome), Lauren Collier-Hyams PhD (NF-κB/Pharma), Valerie Jones PhD (Innate Immune Safety)

---

## Primary Research (long-form)

These are the long-form research documents that the shorter concept pages above are synthesized from. Living documents — the sweep daemon updates them as new findings land.

- **[Open Enzyme Vision](wiki/open-enzyme-vision.md)** — North Star: problem statement, insight, platform vision
- **[Enzyme Deficit Deep Dive](wiki/enzyme-deficit-deep-dive.md)** — Epidemiology and clinical burden of enzyme deficiencies
- **[Gout Deep Dive](wiki/gout-deep-dive.md)** — Uric acid metabolism, NLRP3, current therapies
- **[Engineered Yeast Uricase Proposal](wiki/engineered-yeast-uricase-proposal.md)** — *S. cerevisiae* uricase engineering
- **[Engineered Koji Protocol](wiki/engineered-koji-protocol.md)** — *A. oryzae* multi-enzyme fermentation
- **[NLRP3 Exploit Map](wiki/nlrp3-exploit-map.md)** — NLRP3 inhibition strategies (oridonin, disulfiram, peptides)
- **[Blood Barrier Exploits](wiki/blood-barrier-exploits.md)** — Intestinal barrier biology and optimization
- **[AI Bio Tools Playbook](wiki/ai-bio-tools-playbook.md)** — Computational strain design, optimization, and tool access (includes Codex Life Sciences plugin setup)
- **[Peptide Gout Addendum](wiki/peptide-gout-addendum.md)** — BPC-157, KPV, immunomodulatory peptides

---

## Cross-Analysis & Synthesis

- **[Synthesis (current)](wiki/synthesis.md)** — Cross-doc connections, contradictions, and proposed experiments. The sweep daemon prepends new findings here after each save. **This is the action queue — read it, then prune what you've acted on.**
- **[Concept Graph](wiki/GRAPH.md)** — Mermaid diagram of all concept relationships (produces / inhibits / activates / requires / synergizes / degrades)

### Engineering & Design (deep dives)

Detailed technical analyses for the uricase and koji engineering tracks.

**Uricase / *S. cerevisiae* track:**
- **[Uricase Variant Selection](wiki/uricase-variant-selection.md)** — Six variants evaluated; *A. flavus* primary, *A. globiformis* secondary. Rasburicase FDA precedent. Engineering roadmap.
- **[GI Survival Prediction](wiki/gi-survival-prediction.md)** — Transit model: 15–25% baseline survival → 40–50% with enteric coating + disulfide engineering.
- **[Protein Engineering Strategy](wiki/protein-engineering-strategy.md)** — Three mutation tiers (SB-1 / BAL-1 / OPT-1) for acid stability, protease resistance, and catalytic retention. Includes full mutation lookup table.
- **[Codon Optimization & Expression Cassette](wiki/codon-optimization-expression-cassette.md)** — *S. cerevisiae* cassette: TDH3p constitutive promoter, intracellular uricase, ADH1 terminator. Predicted yield 800–1,200 mg/L.

**Koji / *A. oryzae* track:**
- **[Koji Construct Design](wiki/koji-construct-design.md)** — *A. oryzae* uricase via amyB promoter (starch-inducible, 6–10× baseline). Expected 40–80 mg/g koji.
- **[Digestive Enzyme Optimization](wiki/digestive-enzyme-optimization.md)** — RIB40 strain; lipase 1,813–2,280 U/g koji; rice bran optimal substrate; CRISPR tglA target. 10–15 g koji ≈ Creon equivalence.
- **[NLRP3 Inhibitor Screen](wiki/nlrp3-inhibitor-screen.md)** — Top candidates: ursolic acid (8.59 g/L yeast), quercetin (930 mg/L), carnosine. Kojic acid native production (3–5 g/L) flagged as free bonus.

**Cross-platform:**
- **[Cross-Validation (Thesis Stress Test)](wiki/cross-validation.md)** — Risk matrix across all tracks; NLRP3 suppression confirmed; variant redundancy tested; ALLN-346 clinical bridge.

---

## Cross-Domain Relationships

**Uricase engineering loop:** uricase → *S. cerevisiae* / *A. oryzae* → gut-lumen-sink → NLRP3 inflammasome suppression → gout flare prevention

**Barrier repair loop:** BPC-157 + KPV → blood-barrier integrity → NLRP3 suppression via barrier signal transduction → oridonin / disulfiram (optional intensification)

**Metabolic synergy:** BHB (ketogenic diet or supplementation) → NLRP3 inhibition + probiotic fitness advantage → enzyme-producing strains outcompete pathogenic flora (SIBO prevention)

**Full-stack example (gout):** Engineered *A. oryzae* koji (uricase + NLRP3 inhibitors) + rice bran substrate + allopurinol adjunct → multi-target gout resolution (current platform thesis)

---

## Reference & Conventions

- **`wiki/`** — Living research documents. Updated as new findings land. Written in markdown with standard links (`[text](./path.md)`) so they render on GitHub.
- **`logs/`** — Sweep daemon log (`logs/sweep-log.md`). One entry per triggered sweep.
- **`reference/`** — Canonical read-only material (published papers, external reports, vendor data). The sweep daemon reads but never writes here.
- **Evidence levels** on every claim: `Clinical Trial`, `Animal Model`, `In Vitro`, or `Mechanistic Extrapolation`.
- **Inline provenance** on new content: `(source: <filename>)`.
- **Git is the revision history** — no inline changelogs; use `git log -p <file>` to see what changed.
