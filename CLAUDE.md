# Open Enzyme — AI Working Instructions

Guidelines for any Claude or AI system working on this project. This document ensures consistency, rigor, and maintainability across research and platform development.

---

## Project Context

**Mission:** Use red-teaming techniques to identify exploitable weaknesses in gout, and use creative engineering to exploit them.

Open Enzyme is a portfolio of falsifiable research tracks. Koji, yeast, live biotherapeutics, transporter modulation, repurposed compounds, local delivery, and other modalities are candidate tracks—not the project. A failed track is documented, killed or revised at the scope justified by the evidence, and followed by the next best exploit.

**Team:** Currently just Brian (CTO background). Three PhD-level collaborator roles are actively being recruited (Gut Microbiome / In Vivo Validation, Pharma Translation / Regulatory, Innate Immune Safety) — see [`wiki/team.md`](wiki/etc/team.md). Audience = PhD-level scientists. No overselling.

**Phase:** Research & Design (Phase 0)

---

## Document Structure

### wiki/ — Research Library (living)
All research — long-form primary research docs and shorter concept pages — lives here side by side. Source of truth. Push-time propagation updates affected pages; deliberate full synthesis searches the complete corpus for new cross-domain findings.

- `synthesis/queue/` — Active reviewed findings only. Close an item by applying the action and deleting the queue file in the same commit. Git is the archive. See [`synthesis/README.md`](./synthesis/README.md).
- `wiki/[concept].md` — Individual wiki pages. Long-form research (e.g. `gout-deep-dive.md`, `engineered-koji-protocol.md`) and shorter concept pages (`uricase.md`, `nlrp3-inflammasome.md`) are both here. Organize by topic, not by length.

Prefer standard markdown links (`[text](./path.md)`) over `[[wiki-links]]` in any file expected to be shared externally — GitHub only renders the standard form.

### index.md (repo root) — Dashboard
Top of file: current mission and portfolio state, synthesis queue pointer, cheapest-next-experiments table. Bottom: concept index + primary-research doc list + AI-analysis links. This is the "what should I look at?" landing page.

### logs/ — Compact machine-readable receipts
`logs/sweep-state.json` holds the current propagation cursor, synthesis cursor, current per-COMP eligibility, and unresolved failures. `logs/evidence-radar-state.json` holds replaceable source cursors, review backlogs/monitors, and the latest query/review receipt; the deterministic compressed trial-fingerprint store sits beside it in `logs/evidence-radar-clinical-records.json.gz`. `logs/chembl-refresh-state.json` is the replaceable latest-run ChEMBL query/failure receipt. These are operational state and excluded from synthesis. `logs/lit-scans/*.json` retains compact literature-search reproducibility receipts: exact queries, sources attempted, counts, failures, translation checks, and verification status. Scientific findings live only in canonical wiki pages; do not store a second findings narrative in logs. Successful automation history belongs in GitHub Actions and Git, not an append-only live ledger.

### reference/ — Canonical (read-only)
Published papers, external reports, vendor data, machine-generated output (under `reference/generated/`). Never modified by the daemon or by AI edits. Cite as provenance.

### *.html — Published Formatted Versions
Original pretty-printed versions of the primary research docs. **Do not modify.** These are the published public face. The markdown is the working knowledge base.

### Git is the revision history
No inline revision-history sections in documents. Use `git log -p <file>` to see what changed and when. Commit often; commit messages carry the narrative.

---

## Core Rules

### 0. Epistemic operating principle

**Be conservative about what we claim and aggressive about what we imagine.**

Accuracy and creativity are separate obligations:

- A factual claim must remain inside its source and evidence boundary.
- A **Mechanistic Extrapolation** connects established premises by a supported inference.
- A **Research Conjecture** preserves a novel, useful leap that has not been directly tested. It is an epistemic status, not an evidence level and not permission to present the leap as fact.
- Lack of direct evidence is a reason to label and test a good idea, not automatically a reason to delete it. Delete a conjecture when it is duplicated, no longer useful, or a required premise fails. A negative result kills only the scope it tested.

Put a compact conjecture on the wiki page that owns its mechanism. Use this exact shape and keep the whole block near 100–200 words:

```markdown
> **Research conjecture — [short title]**{ .research-conjecture-label }
>
> **Grounded premises:** [Source-backed premises, each with its evidence level and provenance.]
>
> **Novel leap:** [The untested connection. Say explicitly that direct evidence is absent.]
>
> **Why it matters:** [The upside if the leap is true.]
>
> **Discriminating observation:** [The cheapest observation or experiment that would advance, redirect, or kill it.]
```

`wiki/open-questions.md` may index the lead with a one-line link; do not copy the block. Promote a lead to `wiki/hypotheses/` only when it is specific enough for a falsification card and Brian is ready to commit resources. `synthesis/queue/` holds the unresolved action needed to route or test a lead, never the only copy of the scientific idea. When the action closes, update the owning page and delete the queue file; Git is the archive.

### 1. Propagation and synthesis rule
When new information emerges, re-evaluate every current page that depends on the affected concept. Bounded propagation runs on relevant pushes. Full-corpus synthesis is separate and manual: it reads the complete current corpus twice, compares all domain pairs, rehydrates candidates from raw sources, and independently reviews them. Never trigger full synthesis merely to publish or propagate a push.

Example: If a new NLRP3 inhibitor is discovered, update:
- wiki/nlrp3-exploit-map.md (primary research)
- wiki/nlrp3-inflammasome.md (concept page)
- index.md (if adding a new concept page, or if it shifts the mission or portfolio)

### 2. Adding New Research

**Workflow:**
1. Create new wiki page in `wiki/` with `.md` extension
2. Include frontmatter: `title`, `date`, `tags` (and `related`, `sources` if you have them)
3. Write with evidence levels (see Rule 5 below)
4. Update all relevant wiki pages and `index.md`
5. Prefer standard markdown links (`[text](./path.md)`); `[[wiki-links]]` also work in Obsidian but don't render on GitHub

**Example:** If adding a page on "Off-Target Enzyme Activity":
- Create `wiki/off-target-assessment.md`
- Link it from `wiki/nlrp3-inflammasome.md` under "Related"
- Update `index.md` with the new concept (new section if needed)

### 3. Writing Style

**Tone:** Honest, rigorous, direct. Audience = PhD scientists.

**Standards:**
- Distinguish evidence, mechanistic extrapolation, and research conjecture (see Rules 0 and 5)
- No marketing language or overselling
- State assumptions and limitations clearly
- Cite primary sources; include evidence level
- Use active voice, precise language
- Cross-reference liberally

**Reader contract for intervention and compound pages:**
1. Lead with the gout weakness the intervention might exploit and the strength of the evidence.
2. Explain where the intervention is found or sourced, how it could reach the relevant compartment, and what limits useful exposure.
3. End with the experiment or observation that would advance, redirect, or kill the hypothesis.
4. Discuss a production chassis only when chassis choice changes an active sourcing or delivery decision. Never screen every intervention through yeast or koji by default.
5. Keep editorial history in Git. Creation dates, sweep provenance, “added/promoted/reframed” narration, and statements about when the wiki noticed something do not belong in reader-facing prose.
6. Do not describe a page as canonical, explain why the page exists, or narrate how content is distributed across the corpus. State the current knowledge and link to the supporting evidence home.
7. Research pages describe evidence and experiments, not personalized dosing or treatment instructions. Established clinical practice may be summarized only with its evidence and scope made explicit.
8. A focused intervention or chassis page must stand on its own evidence, sourcing, delivery, and falsification gates. Cross-track rankings belong in portfolio comparison surfaces such as `modality-chokepoint-matrix.md` and `chassis-pending-interventions.md`; do not use another track as the page's narrative foil.

**Example (good):**
> Oridonin blocks NLRP3 inflammasome assembly by preventing ASC oligomerization (in vitro, J. Immunol. 2020). In a murine lipopolysaccharide + MSU model, oridonin reduced IL-1β by 60% relative to vehicle (p < 0.01, n=8). Human efficacy unknown.

**Example (bad):**
> Oridonin is a powerful NLRP3 inhibitor that crushes gout inflammation.

### 4. Pre-commit grep-verify gate for load-bearing numbers

**Every load-bearing quantitative claim in newly-authored wiki content must be grep-verified against its primary source BEFORE the commit lands.** This applies to disulfide counts, residue positions, sequence lengths, kinetic constants (IC50, Km, Ki), dose-response numbers, cohort sizes, percent changes, evidence-tier verdicts — anything downstream reasoning will depend on. Not "verify after the sweep flags an inconsistency"; verify before the content ships into the corpus.

Follow the per-claim protocol in [`manual-literature-mining.md`](./wiki/etc/manual-literature-mining.md): identify the load-bearing claim, name and inspect the primary source, verify the exact value, cite it, and omit or mark the claim unresolved when verification fails. This applies to COMPs, hypothesis cards, scope pages, and primary-research edits. Put the requirement in every delegated authoring brief.

**COMP lifecycle gate:** every new or materially revised comp-NNN requires two context-isolated adversarial reviews: one of code, inputs, provenance, rules, and planned outputs before result-bearing execution; another of the complete artifact and every proposed interpretation after execution. Each review binds to a SHA-256 manifest. Any post-run change to the model, code, inputs, parameters, decision rules, or sensitivity plan returns to the pre-run gate. Follow [`new-comp-experiment`](./skills/new-comp-experiment/SKILL.md) and [`comp-review-manifest.py`](./scripts/comp-review-manifest.py). Push review is an additional backstop, not a substitute.

**Brief hygiene:** propagate the user's scope and method, not predictions, metaphors, or contrived examples that could bias the result.

### 5. Evidence Levels

**Always state the level of evidence for claims.** Use these tags:

| Tag | Definition | Examples |
|-----|-----------|----------|
| **Clinical Trial** | Data from human randomized controlled trials | FDA phase data, published RCTs |
| **Animal Model** | Preclinical in vivo (murine, primate, dog, etc.) | NLRP3 knockout mice, gout flare in rats |
| **In Vitro** | Cell culture, tissue, biochemical assay | Uricase kinetics in solution, NLRP3 activation in macrophages |
| **Mechanistic Extrapolation** | Reasonable inference from foundational biology; no direct evidence | "BHB inhibits HDAC, which suppresses IL-1β signaling (known mechanism); therefore BHB may suppress gout" |

Attach the tag and source close to the claim. Do not infer a higher tier from a downstream marker, adjacent disease, or computational prediction.

**Research Conjecture is not a fifth evidence level.** Apply evidence tags to its grounded premises, then isolate the unsupported leap in the conjecture block. Do not relabel an unsupported factual assertion as a conjecture merely to save it; the block must contain a real connection, a reason it matters, and a discriminating observation.

### 6. Cross-References & Links

**In wiki pages:**
- Prefer standard markdown links: `[uricase](./uricase.md)`, `[NLRP3 inflammasome](./nlrp3-inflammasome.md)`. These render on GitHub.
- Obsidian-style `[[wiki-links]]` also work in Obsidian but don't render on GitHub. Use sparingly, and only in files you don't expect to share externally.
- Include YAML frontmatter with `title`, `date`, `tags` (and `related`, `sources` when applicable).
- Link to `index.md` for the dashboard, `synthesis/queue/` for the action queue (or `synthesis/README.md` for the architecture overview).

**In index.md:**
- Keep the dashboard (mission, portfolio state, synthesis queue, cheapest experiments) at the top.
- Keep the concept/research index below, with one-line descriptions.

### 7. The HTML Files Are Published Versions

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

## Authoring workflow

Publishing and bounded propagation run on relevant pushes; full-corpus synthesis runs only on explicit request. For new evidence: identify affected concepts, update the evidence page and direct dependents, tag evidence and provenance, update or redirect any conjecture whose premises changed, and update `index.md` only for discoverability or mission/portfolio changes. For a new connection: verify its premises, write the unsupported leap as a compact Research Conjecture on the owning page, and index it only when useful. Then run link, privacy, corpus-hygiene, and relevant test checks. Changed COMP artifacts require current push review before derived claims become eligible.

### Task: Query Reactome pathway data

Use the repo-local Reactome integration before manually downloading reports:

1. Load `skills/reactome/SKILL.md` for workflow guidance.
2. Run `python3 tools/reactome/reactome_analysis.py --help` to inspect available commands.
3. Use `query`, `contained-events`, `event-ancestors`, `participants`, `search`, and `diagram` to inspect stable IDs programmatically.
4. Treat Reactome as curated pathway infrastructure, not primary evidence. Before updating `wiki/`, grep-verify load-bearing PMIDs, DOIs, residue positions, kinetic constants, ChEBI IDs, UniProt accessions, and evidence tiers against primary sources.

---

## Safety & Compliance Notes

- All claims about gout, EPI, or other conditions are research-stage. No medical advice.
- All compounds are evaluated for off-target effects and gut dysbiosis risk.
- Engineered organisms are GRAS-certified (or GRAS-pathway) hosts only.
- All safety data (toxicity, allergenicity, interactions) is explicitly noted.
- This is a research library, not a clinical protocol. Emphasize: "Phase 0 — Research & Design."

---

### Global-multilingual research by default (no English-only bias)

Literature scans and research tasks are multilingual by default. Use relevant regional sources, including ChiCTR, CNKI/WanFang, J-STAGE/CiNii/J-GLOBAL, KISS/RISS, eLIBRARY.RU, TIB/GND, and SciELO. For traditional-medicine compounds, search traditional formula name, species name, and traditional pathology framing in addition to the modern mechanism name; mechanism-only and ChEMBL-only searches under-cover this literature. Read and cite non-English sources directly with the original title plus an English gloss. Do not list language as a limitation. Brian-facing synthesis remains in English.

#### Translation protocol (two-model independent cross-check + inline disagreement annotations)

Translate non-English source material with two independent vendors; for Chinese, one must be DeepSeek or Qwen. Annotate disagreements inline and flag load-bearing dose, mechanism, or evidence-tier disagreements as `[TRANSLATION-DISAGREEMENT]`. Follow the protocol in [`manual-literature-mining.md`](./wiki/etc/manual-literature-mining.md).

### Push-batching discipline (Open Enzyme overrides the umbrella's "push immediately" rule)

Commit substantive writes promptly. Push only at a logical batch boundary, explicit user request, end of session, or urgent hotfix. Report unpushed commits honestly. Relevant pushes publish, review changed COMPs, and run bounded propagation; full synthesis remains manual. Coherent batches reduce repeated review, propagation cost, and merge contention.

---

## Contact & Escalation

If you're uncertain about scope, evidence standard, or whether a change triggers the "doc sweep rule", default to **conservatism**: err toward more updates, not fewer. This project is rigorous for PhD scientists, and consistency is non-negotiable.

**Project Lead:** Brian Abent (brian.abent@gmail.com)
