# Open Enzyme — AI Working Instructions

Guidelines for any Claude or AI system working on this project. This document ensures consistency, rigor, and maintainability across research and platform development.

---

## Project Context

**Open Enzyme** is an open source library of engineered, food-grade microbial strains producing therapeutic enzymes.

**First targets:**
- **Uricase** — Gout (hyperuricemia, NLRP3-driven inflammation)
- **Digestive enzymes** (lipase, protease, amylase) — Exocrine pancreatic insufficiency (EPI)
- **Koji** (A. oryzae) — Natural multi-enzyme producer; genetic engineering for enzyme enhancement

**Team:** 3 Emory PhDs + 1 engineer (CTO background). Audience = PhD-level scientists. No overselling.

**Phase:** Research & Design (Phase 0)

---

## Document Structure

### docs/ — Primary Research Library
Markdown research documents. **This is the source of truth.** All wiki pages and external materials are synthesized from docs/.

- `open-enzyme-vision.md` — North Star: problem statement, insight, platform vision
- `enzyme-deficit-deep-dive.md` — Epidemiology and clinical burden
- `gout-deep-dive.md` — Uric acid metabolism, NLRP3, current therapies
- `engineered-yeast-uricase-proposal.md` — S. cerevisiae uricase engineering
- `engineered-koji-protocol.md` — A. oryzae multi-enzyme fermentation
- `nlrp3-exploit-map.md` — NLRP3 inhibition strategies (oridonin, disulfiram, peptides)
- `blood-barrier-exploits.md` — Intestinal barrier biology and optimization
- `ai-bio-tools-playbook.md` — Computational strain design and optimization
- `peptide-gout-addendum.md` — BPC-157, KPV, immunomodulatory peptides

### wiki/ — Synthesized Concept Pages
Karpathy-style LLM wiki. Each page integrates across multiple docs/ for rapid navigation. Organized by domain.

- **wiki/INDEX.md** — Master concept index (required reading)
- **wiki/GRAPH.md** — Mermaid diagram of all concept relationships
- `wiki/[concept].md` — Individual concept pages (uricase, NLRP3, organisms, peptides, inhibitors, etc.)

### *.html — Published Formatted Versions
Original pretty-printed versions of docs/. **Do not modify.** These are the "published" public face. The markdown is the working knowledge base.

---

## Core Rules

### 1. Doc Sweep Rule
When new information emerges (new research, evidence, design decision), re-evaluate **ALL docs and wiki pages that reference the affected concepts**.

Example: If a new NLRP3 inhibitor is discovered, update:
- docs/nlrp3-exploit-map.md
- wiki/nlrp3-inflammasome.md
- wiki/GRAPH.md (if mechanism adds new nodes/edges)
- wiki/INDEX.md (if adding new concept page)

### 2. Adding New Research

**Workflow:**
1. Create new doc in docs/ with `.md` extension
2. Include frontmatter: `title`, `date`, `tags`, `related`, `sources`
3. Write with evidence levels (see Rule 4 below)
4. Update all relevant wiki pages and [wiki/INDEX.md](wiki/INDEX.md)
5. Update [wiki/GRAPH.md](wiki/GRAPH.md) if adding new nodes or relationships
6. Ensure [[wiki-links]] in all documents

**Example:** If adding a doc on "Off-Target Enzyme Activity":
- Create docs/off-target-assessment.md
- Link it in [wiki/nlrp3-inflammasome.md](wiki/nlrp3-inflammasome.md) under "Related"
- Update [wiki/INDEX.md](wiki/INDEX.md) with new concept (new section if needed)
- Update [wiki/GRAPH.md](wiki/GRAPH.md) to show off-target effects as downstream of enzyme engineering

### 3. Writing Style

**Tone:** Honest, rigorous, direct. Audience = PhD scientists.

**Standards:**
- Distinguish proven from speculative (see Rule 4)
- No marketing language or overselling
- State assumptions and limitations clearly
- Cite primary sources; include evidence level
- Use active voice, precise language
- Cross-reference liberally

**Example (good):**
> Oridonin blocks NLRP3 inflammasome assembly by preventing ASC oligomerization (in vitro, J. Immunol. 2020). In a murine lipopolysaccharide + MSU model, oridonin reduced IL-1β by 60% relative to vehicle (p < 0.01, n=8). Human efficacy unknown.

**Example (bad):**
> Oridonin is a powerful NLRP3 inhibitor that crushes gout inflammation.

### 4. Evidence Levels

**Always state the level of evidence for claims.** Use these tags:

| Tag | Definition | Examples |
|-----|-----------|----------|
| **Clinical Trial** | Data from human randomized controlled trials | FDA phase data, published RCTs |
| **Animal Model** | Preclinical in vivo (murine, primate, dog, etc.) | NLRP3 knockout mice, gout flare in rats |
| **In Vitro** | Cell culture, tissue, biochemical assay | Uricase kinetics in solution, NLRP3 activation in macrophages |
| **Mechanistic Extrapolation** | Reasonable inference from foundational biology; no direct evidence | "BHB inhibits HDAC, which suppresses IL-1β signaling (known mechanism); therefore BHB may suppress gout" |

**Format in text:**
- "Uricase degrades uric acid in vitro with Km = 2.1 mM (Biochemistry, 1998)."
- "Oridonin blocks ASC speck formation (in vitro, J. Immunol. 2020)."
- "S. cerevisiae colonizes the mouse gut (animal model, murine gnotobiotic, Microbiome. 2023)."
- "Mechanistic extrapolation: If engineered S. cerevisiae express uricase at high levels and survive passage to the colon, they should degrade luminal uric acid."

### 5. Cross-References & Links

**In wiki pages:**
- Use [[wiki-links]] to related concepts: `[[uricase]]`, `[[nlrp3-inflammasome]]`
- Link to source docs in footer: `See [gout-deep-dive.md](../docs/gout-deep-dive.md)`

**In docs/ pages:**
- Include YAML frontmatter with `related:` list and `sources:` list
- Link to wiki pages in text where relevant: "For more on NLRP3, see [[nlrp3-inflammasome]]"

**In wiki/INDEX.md:**
- Keep master list of all concepts with one-line descriptions
- Link to each concept page and its description

**In wiki/GRAPH.md:**
- Update Mermaid diagram whenever concepts or relationships change
- Ensure all nodes appear in at least one subgraph
- Label edges with relationship type (e.g., "produces", "inhibits", "activates")

### 6. The HTML Files Are Published Versions

- **Do not edit *.html files.** They are the formatted public versions.
- The markdown (docs/) is the working knowledge base.
- If edits are needed, edit docs/\*.md first, then republish HTML via external tool.

---

## Key Science References (Context)

These are frequently cited or mechanistically central. Use as touchstones:

| Reference | Relevance | Citation |
|-----------|-----------|----------|
| ALLN-346 Phase 2a trial | Oral uricase in gut lumen; proof-of-concept for enzymatic urate degradation | Phase 2a, oral, MSU flares |
| PULSE probiotic (Cell Reports Medicine, Oct 2025) | Live probiotic efficacy in humanized microbiome model | Oral + barrier repair synergy |
| ACS Syn Bio 2025 | S. boulardii engineered lipase; 365 μmol/h/OD | High expression in GRAS organism |
| Rasburicase (FDA 2001) | A. flavus uricase in S. cerevisiae background; IV clinical use | Proof that yeast uricase engineering works at scale |
| ABCG2 gut secretion pathway | Accounts for ~1/3 of uric acid excretion; target for absorption-limiting strategies | Physiology, not just enzymatic degradation |
| Georgia State CRISPR uricase (Scientific Reports, July 2025) | CRISPR-edited S. cerevisiae for uricase expression; 8-fold improvement over WT | Modern genetic engineering benchmark |

---

## Workflow for Updates

### When new data emerges:

1. **Determine scope:** Which concepts or mechanisms does this affect?
   - Example: "New data on BHB + NLRP3" → affects docs/nlrp3-exploit-map.md, wiki/bhb-ketones.md, wiki/GRAPH.md

2. **Update docs/ first:**
   - Add new doc or edit existing doc with new information and evidence level
   - Update YAML frontmatter if adding cross-references

3. **Update wiki pages:**
   - Edit affected concept pages in wiki/
   - Add [[wiki-links]] to related concepts

4. **Update wiki/INDEX.md:**
   - Add new concept pages if created
   - Reorganize categories if needed

5. **Update wiki/GRAPH.md:**
   - Add/modify nodes and edges in Mermaid diagram
   - Ensure relationships are labeled

6. **Verify consistency:**
   - Check all [[wiki-links]] are bidirectional
   - Ensure no orphaned concepts in docs/ or wiki/
   - Verify evidence levels are tagged throughout

---

## Common Tasks

### Task: Add a new intervention (e.g., a small-molecule NLRP3 inhibitor)

1. Create `docs/[compound]-mechanism.md` with structure:
   - Mechanism of action
   - Evidence (in vitro → animal → clinical)
   - Dosing, safety, GI tolerability
   - Synergies with uricase/barrier repair

2. Create or edit `wiki/[compound].md` with one-sentence hook

3. Update:
   - wiki/INDEX.md (add to "Small-Molecule Agents" section)
   - wiki/nlrp3-inflammasome.md (add to related concepts)
   - wiki/GRAPH.md (add node + edges to NLRP3 and relevant pathways)

### Task: Revise a mechanism based on new data

1. Edit the relevant doc(s) in docs/
2. Update evidence level tags and citations
3. Re-read all wiki pages that reference this mechanism
4. Update wiki pages with new understanding
5. Check wiki/GRAPH.md for any edge changes

### Task: Ensure a new doc is discoverable

1. Add to wiki/INDEX.md with one-line description
2. Add [[wiki-links]] in related concept pages
3. Link the doc in wiki/GRAPH.md (if a new concept)
4. Include YAML frontmatter in the doc with `related:` and `sources:`

---

## Safety & Compliance Notes

- All claims about gout, EPI, or other conditions are research-stage. No medical advice.
- All compounds are evaluated for off-target effects and gut dysbiosis risk.
- Engineered organisms are GRAS-certified (or GRAS-pathway) hosts only.
- All safety data (toxicity, allergenicity, interactions) is explicitly noted.
- This is a research library, not a clinical protocol. Emphasize: "Phase 0 — Research & Design."

---

## Questions to Ask When Evaluating New Information

1. **What's the evidence level?** (Clinical, animal, in vitro, mechanistic)
2. **Does this affect multiple docs/wiki pages?** (Trigger doc sweep rule)
3. **Are there new concepts?** (Trigger new wiki page creation)
4. **Are there new relationships?** (Update wiki/GRAPH.md)
5. **Are assumptions/limitations stated clearly?** (Maintain rigor)
6. **Is it PhD-audience appropriate?** (No marketing, honest about unknowns)

---

## Version Control & Maintenance

- **Primary source of truth:** docs/
- **Derived materials:** wiki/ (synthesized from docs/)
- **Published format:** *.html (do not edit directly)
- **Metadata:** YAML frontmatter in all .md files
- **Cross-references:** Use [[wiki-links]] and relative URLs consistently

---

## Contact & Escalation

If you're uncertain about scope, evidence standard, or whether a change triggers the "doc sweep rule", default to **conservatism**: err toward more updates, not fewer. This project is rigorous for PhD scientists, and consistency is non-negotiable.

**Project Lead:** Brian Abent (brian@headsupresults.com)
