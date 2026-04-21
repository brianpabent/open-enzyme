# Open Enzyme

An open source library of food-grade engineered microbial strains — each producing a therapeutic enzyme, each growable at home, each freely available to anyone. Addresses enzyme deficits (gout, EPI, lactose malabsorption) by combining GRAS-certified fermentation biology with rational enzyme engineering and safe immunomodulation.

**Status:** Phase 0 — Research & Design  
**Dashboard:** [index.md](index.md) — platform thesis, synthesis queue, cheapest-next-experiments, full concept index

---

## Research Library (wiki/)

All research lives in `wiki/` — long-form primary documents and shorter synthesized concept pages side by side. The sweep daemon keeps these current as new findings land.

### Primary Research

| Document | What it covers |
|----------|---------------|
| [open-enzyme-vision.md](wiki/open-enzyme-vision.md) | North Star: the problem, insight, and platform vision |
| [enzyme-deficit-deep-dive.md](wiki/enzyme-deficit-deep-dive.md) | Epidemiology, pathophysiology, and clinical burden of enzyme deficits |
| [gout-deep-dive.md](wiki/gout-deep-dive.md) | Uric acid metabolism, NLRP3 inflammasome, acute flare mechanisms, current therapies |
| [engineered-yeast-uricase-proposal.md](wiki/engineered-yeast-uricase-proposal.md) | Engineering uricase into *S. cerevisiae*: construct design, expression, fermentation |
| [engineered-koji-protocol.md](wiki/engineered-koji-protocol.md) | Multi-enzyme koji (*A. oryzae*): uricase + digestive enzyme co-expression, rice-based substrate |
| [nlrp3-exploit-map.md](wiki/nlrp3-exploit-map.md) | NLRP3 inflammasome targeting: all 6 chokepoints, agents, and combinations |
| [blood-barrier-exploits.md](wiki/blood-barrier-exploits.md) | Intestinal barrier biology, tight-junction dynamics, enzyme bioavailability |
| [ai-bio-tools-playbook.md](wiki/ai-bio-tools-playbook.md) | Computational biology: structure prediction, codon optimization, strain design pipelines |
| [peptide-gout-addendum.md](wiki/peptide-gout-addendum.md) | Immunomodulatory peptides (KPV, BPC-157) in gout: barrier repair and synergy |

### Engineering Deep Dives

**Uricase / *S. cerevisiae* track:**

| Document | What it covers |
|----------|---------------|
| [uricase-variant-selection.md](wiki/uricase-variant-selection.md) | Six variants evaluated; *A. flavus* primary, engineering roadmap |
| [gi-survival-prediction.md](wiki/gi-survival-prediction.md) | GI transit model: 15–25% baseline survival → 40–50% with engineering |
| [protein-engineering-strategy.md](wiki/protein-engineering-strategy.md) | SB-1 / BAL-1 / OPT-1 mutation tiers for acid stability + protease resistance |
| [codon-optimization-expression-cassette.md](wiki/codon-optimization-expression-cassette.md) | *S. cerevisiae* expression cassette design; predicted yield 800–1,200 mg/L |

**Koji / *A. oryzae* track:**

| Document | What it covers |
|----------|---------------|
| [koji-construct-design.md](wiki/koji-construct-design.md) | amyB promoter, uricase expression; expected 40–80 mg/g koji |
| [digestive-enzyme-optimization.md](wiki/digestive-enzyme-optimization.md) | RIB40 strain; lipase 1,813–2,280 U/g; rice bran optimal substrate |
| [nlrp3-inhibitor-screen.md](wiki/nlrp3-inhibitor-screen.md) | Top candidates: ursolic acid, quercetin, carnosine; kojic acid as native bonus |
| [cross-validation.md](wiki/cross-validation.md) | Thesis stress test: risk matrix, feasibility ratings, ALLN-346 clinical bridge |

### Concept Pages

**Core Targets:**
[Uricase](wiki/uricase.md) · [NLRP3 Inflammasome](wiki/nlrp3-inflammasome.md) · [Digestive Enzymes](wiki/digestive-enzymes.md) · [Gout Pathophysiology](wiki/gout-pathophysiology.md)

**Organisms:**
[Saccharomyces cerevisiae](wiki/saccharomyces-cerevisiae.md) · [Aspergillus oryzae](wiki/aspergillus-oryzae.md)

**Delivery:**
[Gut-Lumen Sink](wiki/gut-lumen-sink.md) · [Blood Barrier](wiki/blood-barrier.md)

**Compounds:**
[BPC-157](wiki/bpc-157.md) · [KPV Tripeptide](wiki/kpv-peptide.md) · [BHB / Ketones](wiki/bhb-ketones.md) · [Oridonin](wiki/oridonin.md) · [Disulfiram](wiki/disulfiram.md)

**Synthesis & Graph:**
[synthesis.md](wiki/synthesis.md) — cross-doc connections and proposed experiments (action queue) · [GRAPH.md](wiki/GRAPH.md) — Mermaid concept graph

---

## Team

- **Brian Abent** — Founder, Platform Architecture

### Potential Collaborators (actively recruiting)

- **Rheinallt Jones, PhD** — Gut Microbiome Ecology, In Vivo Validation, Dosing Strategy
- **Lauren Collier-Hyams, PhD** — NF-κB Signaling, Pharma Translation, Regulatory Pathway
- **Valerie Jones, PhD** — Innate Immune Safety, Off-Target Assessment, Clinical Design

All three trained at Emory's Epithelial Pathobiology Unit under Andrew Neish.

---

## Quick Start

### For Researchers
1. Read [open-enzyme-vision.md](wiki/open-enzyme-vision.md) (10 min)
2. Browse [index.md](index.md) for the current platform thesis and concept map
3. Check [wiki/synthesis.md](wiki/synthesis.md) for the latest cross-doc connections
4. Dive into primary research docs for full citations and methodology

### For Engineers & Makers
1. Start with [engineered-yeast-uricase-proposal.md](wiki/engineered-yeast-uricase-proposal.md) or [engineered-koji-protocol.md](wiki/engineered-koji-protocol.md)
2. See [protein-engineering-strategy.md](wiki/protein-engineering-strategy.md) for the mutation tier roadmap
3. Review [ai-bio-tools-playbook.md](wiki/ai-bio-tools-playbook.md) for strain design pipelines

### For Clinical/Pharma Reviewers
1. Read [gout-deep-dive.md](wiki/gout-deep-dive.md) and [cross-validation.md](wiki/cross-validation.md)
2. Review [nlrp3-exploit-map.md](wiki/nlrp3-exploit-map.md) for immunomodulation strategy
3. Check [blood-barrier-exploits.md](wiki/blood-barrier-exploits.md) for safety and bioavailability

---

## Evidence & Rigor

All claims are tagged with evidence level:
- **Clinical Trial** — Data from human RCTs
- **Animal Model** — Preclinical in vivo (murine, primate, etc.)
- **In Vitro** — Cell culture, tissue, or biochemical data
- **Mechanistic Extrapolation** — Reasonable inference from foundational biology

Written for PhD scientists. We distinguish proven from speculative and do not oversell. See [CLAUDE.md](CLAUDE.md) for documentation standards.

---

## Contributing

This is an open source research platform. The research library is the codebase.

**Before opening an issue or PR:**
- Check [index.md](index.md) to see if the concept exists
- If adding new research, create a page in `wiki/`, update relevant pages and `index.md`
- Use standard markdown links (`[text](./path.md)`) — they render on GitHub
- Tag all claims with evidence levels

For AI assistants working on this project, see [CLAUDE.md](CLAUDE.md).

---

## License

Open Enzyme is released under [MIT License](LICENSE). All research documents and wiki pages are freely available for scientific, educational, and commercial use.

---

## Contact

**Project Lead:** Brian Abent  
**Email:** brian@headsupresults.com
