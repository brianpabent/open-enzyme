# Open Enzyme — AI Working Instructions

Guidelines for any Claude or AI system working on this project. This document ensures consistency, rigor, and maintainability across research and platform development.

---

## Project Context

**Open Enzyme** is an open source library of engineered, food-grade microbial strains producing therapeutic enzymes.

**First targets:**
- **Uricase** — Gout (hyperuricemia, NLRP3-driven inflammation)
- **Digestive enzymes** (lipase, protease, amylase) — Exocrine pancreatic insufficiency (EPI)
- **Koji** (A. oryzae) — Natural multi-enzyme producer; genetic engineering for enzyme enhancement

**Team:** Currently just Brian (CTO background). Three Emory PhDs (Rheinallt Jones, Lauren Collier-Hyams, Valerie Jones) are potential collaborators but have full-time jobs — recruiting them is an active project goal. Audience = PhD-level scientists. No overselling.

**Phase:** Research & Design (Phase 0)

---

## Document Structure

### wiki/ — Research Library (living)
All research — long-form primary research docs and shorter synthesized concept pages — lives here side by side. Source of truth. The sweep daemon updates these as new findings land.

- `wiki/synthesis.md` — Cross-doc connections, contradictions, proposed experiments. **Action queue.** Daemon prepends new findings after Pass 2; Brian prunes manually.
- `wiki/GRAPH.md` — Mermaid diagram of all concept relationships.
- `wiki/[concept].md` — Individual wiki pages. Long-form research (e.g. `gout-deep-dive.md`, `engineered-koji-protocol.md`) and shorter concept pages (`uricase.md`, `nlrp3-inflammasome.md`) are both here. Organize by topic, not by length.

Prefer standard markdown links (`[text](./path.md)`) over `[[wiki-links]]` in any file expected to be shared externally — GitHub only renders the standard form.

### index.md (repo root) — Dashboard
Top of file: current platform thesis, synthesis queue pointer, cheapest-next-experiments table. Bottom: concept index + primary-research doc list + AI-analysis links. This is the "what should I look at?" landing page.

### logs/ — Sweep log
`logs/sweep-log.md` — one entry per daemon-triggered sweep (date, trigger file, Pass 1 updates, Pass 2 synthesis summary). Append-only; the daemon writes it, Brian reads it.

### reference/ — Canonical (read-only)
Published papers, external reports, vendor data, machine-generated output (under `reference/generated/`). Never modified by the daemon or by AI edits. Cite as provenance.

### *.html — Published Formatted Versions
Original pretty-printed versions of the primary research docs. **Do not modify.** These are the published public face. The markdown is the working knowledge base.

### Git is the revision history
No inline revision-history sections in documents. Use `git log -p <file>` to see what changed and when. Commit often; commit messages carry the narrative.

---

## Core Rules

### 1. Doc Sweep Rule
When new information emerges (new research, evidence, design decision), re-evaluate **ALL wiki pages that reference the affected concepts**. The sweep daemon (`scripts/wiki-watch.sh` + `scripts/sweep-prompt.md`) does this automatically on save — see those files for the full protocol.

Example: If a new NLRP3 inhibitor is discovered, update:
- wiki/nlrp3-exploit-map.md (primary research)
- wiki/nlrp3-inflammasome.md (concept page)
- wiki/GRAPH.md (if mechanism adds new nodes/edges)
- index.md (if adding new concept page, or if it shifts the platform thesis)

### 2. Adding New Research

**Workflow:**
1. Create new wiki page in `wiki/` with `.md` extension
2. Include frontmatter: `title`, `date`, `tags` (and `related`, `sources` if you have them)
3. Write with evidence levels (see Rule 4 below)
4. Update all relevant wiki pages and `index.md`
5. Update `wiki/GRAPH.md` if adding new nodes or relationships
6. Prefer standard markdown links (`[text](./path.md)`); `[[wiki-links]]` also work in Obsidian but don't render on GitHub

**Example:** If adding a page on "Off-Target Enzyme Activity":
- Create `wiki/off-target-assessment.md`
- Link it from `wiki/nlrp3-inflammasome.md` under "Related"
- Update `index.md` with the new concept (new section if needed)
- Update `wiki/GRAPH.md` to show off-target effects as downstream of enzyme engineering

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
- Prefer standard markdown links: `[uricase](./uricase.md)`, `[NLRP3 inflammasome](./nlrp3-inflammasome.md)`. These render on GitHub.
- Obsidian-style `[[wiki-links]]` also work in Obsidian but don't render on GitHub. Use sparingly, and only in files you don't expect to share externally.
- Include YAML frontmatter with `title`, `date`, `tags` (and `related`, `sources` when applicable).
- Link to `index.md` for the dashboard, `wiki/synthesis.md` for the action queue.

**In index.md:**
- Keep the dashboard (platform thesis, synthesis queue, cheapest experiments) at the top.
- Keep the concept/research index below, with one-line descriptions.

**In wiki/GRAPH.md:**
- Update Mermaid diagram whenever concepts or relationships change.
- Ensure all nodes appear in at least one subgraph.
- Label edges with relationship type (e.g., "produces", "inhibits", "activates").

### 6. The HTML Files Are Published Versions

- **Do not edit *.html files.** They are the formatted public versions.
- The markdown (`wiki/`) is the working knowledge base.
- If edits are needed, edit `wiki/*.md` first, then republish HTML via external tool.

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

Most of this runs automatically via the sweep daemon — when you save a file under `wiki/`, `scripts/wiki-watch.sh` triggers `scripts/sweep-prompt.md` which propagates findings, synthesizes new connections, logs, and commits. The steps below are what the daemon does, and what you'd do manually if running a sweep yourself.

### When new data emerges:

1. **Determine scope:** Which concepts or mechanisms does this affect?
   - Example: "New data on BHB + NLRP3" → affects `wiki/nlrp3-exploit-map.md`, `wiki/bhb-ketones.md`, `wiki/GRAPH.md`

2. **Update the relevant wiki page(s):**
   - Add new content or revise existing claims inline with evidence level and inline provenance (`(source: <filename>)`)
   - Update YAML frontmatter if adding cross-references

3. **Update `index.md`** if a new page was created or the platform thesis shifted.

4. **Update `wiki/GRAPH.md`:**
   - Add/modify nodes and edges in Mermaid diagram
   - Ensure relationships are labeled

5. **Verify consistency:**
   - Check cross-references resolve
   - Verify evidence levels are tagged throughout

---

## Common Tasks

### Task: Add a new intervention (e.g., a small-molecule NLRP3 inhibitor)

1. Create `wiki/[compound].md` with:
   - Mechanism of action
   - Evidence (in vitro → animal → clinical) with evidence-level tags
   - Dosing, safety, GI tolerability
   - Synergies with uricase / barrier repair

2. Update:
   - `index.md` (add to the appropriate section)
   - `wiki/nlrp3-inflammasome.md` (add to related concepts)
   - `wiki/nlrp3-exploit-map.md` if it fits the exploit map
   - `wiki/GRAPH.md` (add node + edges to NLRP3 and relevant pathways)

### Task: Revise a mechanism based on new data

1. Edit the relevant wiki page(s)
2. Update evidence level tags and citations
3. Re-read all wiki pages that reference this mechanism
4. Update wiki pages with new understanding
5. Check `wiki/GRAPH.md` for any edge changes

### Task: Ensure a new page is discoverable

1. Add to `index.md` with one-line description
2. Link from related wiki pages using standard markdown links
3. Add to `wiki/GRAPH.md` if it introduces a new concept or relationship
4. Include YAML frontmatter with `title`, `date`, `tags` (and `related`, `sources` when applicable)

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
2. **Does this affect multiple wiki pages?** (Trigger doc sweep rule)
3. **Are there new concepts?** (Trigger new wiki page creation)
4. **Are there new relationships?** (Update `wiki/GRAPH.md`)
5. **Are assumptions/limitations stated clearly?** (Maintain rigor)
6. **Is it PhD-audience appropriate?** (No marketing, honest about unknowns)

---

## Version Control & Maintenance

- **Source of truth:** `wiki/`
- **Dashboard:** `index.md` (repo root)
- **Action queue:** `wiki/synthesis.md`
- **Canonical material (read-only):** `reference/`
- **Published format:** `*.html` (do not edit directly)
- **Metadata:** YAML frontmatter in all `.md` files
- **Cross-references:** Prefer standard markdown links; Obsidian `[[wiki-links]]` work in Obsidian but not on GitHub
- **Revision history:** Git. No inline changelogs in documents.

---

## Contact & Escalation

If you're uncertain about scope, evidence standard, or whether a change triggers the "doc sweep rule", default to **conservatism**: err toward more updates, not fewer. This project is rigorous for PhD scientists, and consistency is non-negotiable.

**Project Lead:** Brian Abent (brian@headsupresults.com)
