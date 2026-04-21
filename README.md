# Open Enzyme

An open source library of food-grade engineered microbial strains — each producing a therapeutic enzyme, each growable at home, each freely available to anyone. Addresses enzyme deficits (gout, EPI, lactose malabsorption) by combining GRAS-certified fermentation biology with rational enzyme engineering and safe immunomodulation.

**Status:** Phase 0 — Research & Design  
**Founding Vision:** [open-enzyme-vision.md](docs/open-enzyme-vision.md)

---

## Research Library (docs/)

Complete primary research documents spanning enzyme biology, immunology, organism engineering, and therapeutic strategy.

1. **[open-enzyme-vision.md](docs/open-enzyme-vision.md)** — North Star: the problem, insight, and platform vision
2. **[enzyme-deficit-deep-dive.md](docs/enzyme-deficit-deep-dive.md)** — Epidemiology, pathophysiology, and clinical burden of enzyme deficits globally
3. **[gout-deep-dive.md](docs/gout-deep-dive.md)** — Uric acid metabolism, NLRP3 inflammasome, acute flare mechanisms, current therapies
4. **[engineered-yeast-uricase-proposal.md](docs/engineered-yeast-uricase-proposal.md)** — Engineering uricase into S. cerevisiae: construct design, expression optimization, fermentation protocols
5. **[engineered-koji-protocol.md](docs/engineered-koji-protocol.md)** — Multi-enzyme koji (A. oryzae): uricase + lipase + protease + amylase co-expression, home fermentation, rice-based substrate
6. **[nlrp3-exploit-map.md](docs/nlrp3-exploit-map.md)** — NLRP3 inflammasome targeting: ASC-blocking agents (oridonin, disulfiram), gasdermin D inhibitors, peptide modulators (BPC-157, KPV)
7. **[blood-barrier-exploits.md](docs/blood-barrier-exploits.md)** — Intestinal barrier biology, tight-junction engineering via BPC-157, permeability modulation, enzyme bioavailability optimization
8. **[ai-bio-tools-playbook.md](docs/ai-bio-tools-playbook.md)** — Computational biology methods: structure prediction, codon optimization, off-target screening, strain design pipelines
9. **[peptide-gout-addendum.md](docs/peptide-gout-addendum.md)** — Immunomodulatory peptides (KPV, BPC-157) in gout: barrier repair, IL-10 promotion, synergy with enzymatic urate degradation

---

## Wiki (wiki/)

Synthesized concept pages bridging research domains. Each page integrates across multiple documents for rapid navigation.

**Start here:** [wiki/INDEX.md](wiki/INDEX.md) — Concept index organized by domain (pathology, organisms, delivery, peptides, inhibitors, metabolic)

**Visual overview:** [wiki/GRAPH.md](wiki/GRAPH.md) — Mermaid diagram showing all concept relationships, pathways, and therapeutic stacks

**Core concepts:**
- **Organisms:** [Saccharomyces cerevisiae](wiki/saccharomyces-cerevisiae.md), [Aspergillus oryzae](wiki/aspergillus-oryzae.md)
- **Targets:** [Uricase](wiki/uricase.md), [NLRP3 Inflammasome](wiki/nlrp3-inflammasome.md), [Digestive Enzymes](wiki/digestive-enzymes.md)
- **Peptides:** [BPC-157](wiki/bpc-157.md), [KPV Tripeptide](wiki/kpv-peptide.md)
- **Small molecules:** [Oridonin](wiki/oridonin.md), [Disulfiram](wiki/disulfiram.md), [Beta-Hydroxybutyrate](wiki/bhb-ketones.md)
- **Delivery:** [Gut-Lumen Sink](wiki/gut-lumen-sink.md), [Barrier Biology](wiki/blood-barrier.md)
- **Complications:** [SIBO](wiki/sibo.md)

---

## Team

- **Brian Abent** — Platform Architecture, Genetic Engineering, Fermentation Biology
- **Rheinallt Jones, PhD** — Gut Microbiome Ecology, In Vivo Validation, Dosing Strategy
- **Lauren Collier-Hyams, PhD** — NF-κB Signaling, Pharma Translation, Regulatory Pathway
- **Valerie Jones, PhD** — Innate Immune Safety, Off-Target Assessment, Clinical Design

All team members affiliated with Emory University.

---

## Quick Start

### For Researchers
1. Read [Founding Vision](docs/open-enzyme-vision.md) (10 min)
2. Explore [wiki/INDEX.md](wiki/INDEX.md) for your domain (enzyme biology, immunology, organism engineering)
3. Dive into [docs/](docs/) for full citations and methodology
4. Check [wiki/GRAPH.md](wiki/GRAPH.md) to see how concepts connect

### For Engineers & Makers
1. Start with [engineered-yeast-uricase-proposal.md](docs/engineered-yeast-uricase-proposal.md) or [engineered-koji-protocol.md](docs/engineered-koji-protocol.md)
2. Review [ai-bio-tools-playbook.md](docs/ai-bio-tools-playbook.md) for strain design pipelines
3. Cross-reference [wiki/saccharomyces-cerevisiae.md](wiki/saccharomyces-cerevisiae.md) and [wiki/aspergillus-oryzae.md](wiki/aspergillus-oryzae.md)

### For Clinical/Pharma Reviewers
1. Read [gout-deep-dive.md](docs/gout-deep-dive.md) and [enzyme-deficit-deep-dive.md](docs/enzyme-deficit-deep-dive.md)
2. Review [nlrp3-exploit-map.md](docs/nlrp3-exploit-map.md) for immunomodulation strategy
3. Check [blood-barrier-exploits.md](docs/blood-barrier-exploits.md) for safety and bioavailability
4. See [peptide-gout-addendum.md](docs/peptide-gout-addendum.md) for integrated therapeutic stack

---

## Evidence & Rigor

All claims in this library are tagged with evidence level:
- **Clinical Trial** — Data from human RCTs
- **Animal Model** — Preclinical in vivo (murine, primate, etc.)
- **In Vitro** — Cell culture, tissue, or biochemical data
- **Mechanistic Extrapolation** — Reasonable inference from foundational biology

This is research-grade material written for PhD scientists. We distinguish proven from speculative and do not oversell. See [CLAUDE.md](CLAUDE.md) for documentation standards.

---

## Contributing

This is an open source research platform. The codebase is the research library itself (docs/ + wiki/). 

**Before opening an issue or PR:**
- Check [wiki/INDEX.md](wiki/INDEX.md) to see if the concept exists
- If adding new research, create a new doc in docs/, then update relevant wiki pages and [wiki/INDEX.md](wiki/INDEX.md)
- Maintain [[wiki-links]] and cross-references
- Tag evidence levels (clinical, animal, in vitro, mechanistic)

For AI assistants working on this project, see [CLAUDE.md](CLAUDE.md).

---

## License

Open Enzyme is released under [MIT License](LICENSE). All research documents and wiki pages are freely available for scientific, educational, and commercial use.

---

## Contact

**Project Lead:** Brian Abent  
**Email:** brian@headsupresults.com

For press, partnerships, or collaboration inquiries, reach out to the project lead.
