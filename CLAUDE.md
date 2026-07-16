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

### logs/ — Compact automation state
`logs/sweep-state.json` holds the current propagation cursor, synthesis cursor, current per-COMP eligibility, and unresolved failures. Successful run history belongs in GitHub Actions and Git, not an append-only live ledger.

### reference/ — Canonical (read-only)
Published papers, external reports, vendor data, machine-generated output (under `reference/generated/`). Never modified by the daemon or by AI edits. Cite as provenance.

### *.html — Published Formatted Versions
Original pretty-printed versions of the primary research docs. **Do not modify.** These are the published public face. The markdown is the working knowledge base.

### Git is the revision history
No inline revision-history sections in documents. Use `git log -p <file>` to see what changed and when. Commit often; commit messages carry the narrative.

---

## Core Rules

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
- Distinguish proven from speculative (see Rule 5)
- No marketing language or overselling
- State assumptions and limitations clearly
- Cite primary sources; include evidence level
- Use active voice, precise language
- Cross-reference liberally

**Example (good):**
> Oridonin blocks NLRP3 inflammasome assembly by preventing ASC oligomerization (in vitro, J. Immunol. 2020). In a murine lipopolysaccharide + MSU model, oridonin reduced IL-1β by 60% relative to vehicle (p < 0.01, n=8). Human efficacy unknown.

**Example (bad):**
> Oridonin is a powerful NLRP3 inhibitor that crushes gout inflammation.

### 4. Pre-commit grep-verify gate for load-bearing numbers

**Every load-bearing quantitative claim in newly-authored wiki content must be grep-verified against its primary source BEFORE the commit lands.** This applies to disulfide counts, residue positions, sequence lengths, kinetic constants (IC50, Km, Ki), dose-response numbers, cohort sizes, percent changes, evidence-tier verdicts — anything downstream reasoning will depend on. Not "verify after the sweep flags an inconsistency"; verify before the content ships into the corpus.

**Operational protocol:** see [`wiki/manual-literature-mining.md` §"Pre-commit verification gate"](./wiki/etc/manual-literature-mining.md#pre-commit-verification-gate-the-rule-that-catches-errors-before-the-sweep-not-after) — the canonical statement of the discipline, including the per-claim micro-protocol (identify load-bearing numbers → name primary source → grep-verify → cite line-anchored → drop or placeholder if unverifiable).

**Why this rule exists:** The wiki sweep daemon catches cross-page inconsistencies in Pass 2 / Pass 3, but by then the wrong number has already propagated to multiple pages and been ingested into downstream synthesis. The DAF SCR1-4 disulfide-count incident (2026-05-06) is the canonical case: a Sonnet subagent authoring `wiki/daf-cd55-scr14-truncated-computational.md` (comp-012) hallucinated "3 disulfides per SCR domain → 12 total" in 4 places of prose narrative — a number the comp-012 pipeline doesn't actually compute (its Limitations section says "Disulfide bonds not modelled"). The error propagated into `wiki/hypotheses/H05-daf-scr14-cp0-thesis.md` overnight, drove a downstream chaperone-orthogonal triple-cassette synergy panic ("17+12=29 disulfides, 1.8× Huynh"), and was only caught by the next day's sweep + walkthrough verification against UniProt P08174 (which has exactly 8 DISULFID feature annotations in SCR1-4 — canonical sushi/CCP fold, 2 per domain). The sweep is a backstop; the pre-commit gate is where this class of error should die.

**The discipline applies to all comp-NNN authoring runs, all H-card stubs, all scope pages, all primary-research wiki edits.** When delegating wiki authoring to a subagent, the verification protocol must be in the subagent's brief — not "verify if you have time," but "verify each load-bearing number against primary source before writing it into the page."

**COMP lifecycle gate:** every new or materially revised comp-NNN must receive two context-isolated adversarial subagent reviews. The first occurs after the experiment code, inputs, provenance, decision rules, and planned outputs are written but **before any result-bearing execution**. The second occurs after execution and must inspect the complete code/input/output contract plus every generated output, summary, and proposed wiki update before completion or commit. Each review binds to a SHA-256 manifest of the exact artifact; manifest verification immediately before execution and commit prevents post-review drift. A post-run finding that changes the model, code, inputs, parameters, decision rules, or sensitivity plan returns the comp to the pre-run gate before rerun. Follow [`skills/new-comp-experiment/SKILL.md`](./skills/new-comp-experiment/SKILL.md), [`scripts/comp-review-manifest.py`](./scripts/comp-review-manifest.py), and the review briefs in [`scripts/comp-pre-run-review-prompt.md`](./scripts/comp-pre-run-review-prompt.md) and [`scripts/comp-review-prompt.md`](./scripts/comp-review-prompt.md). The push-triggered comp-review daemon is an additional backstop, not a substitute for either authoring-time gate.

**Sister discipline — subagent brief hygiene:** when *composing* a subagent's brief, scope and method propagate from user direction; predictions and contrived examples don't. User's contrived "if it's rosemary I'll grow rosemary" framing landed verbatim in the comp-018 brief 2026-05-08 and biased the headline finding toward narrative-cohesion. Full discipline + empirical case at [`scripts/SWEEP-ARCHITECTURE.md` §"Subagent brief hygiene"](./scripts/SWEEP-ARCHITECTURE.md). Retrospective at [`operations/comp-018-vs-comp-020-retrospective.md`](./operations/comp-018-vs-comp-020-retrospective.md). The pre-commit grep-verify gate above catches errors *inside* the subagent's output; subagent brief hygiene catches contamination *upstream of* the subagent's run. Different failure modes, both worth disciplined practice.

### 5. Evidence Levels

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

## Workflow for Updates

Publishing and bounded propagation run on relevant pushes. Full-corpus synthesis does not: dispatch it explicitly at a logical research batch boundary. Changed COMP artifacts receive independent push review before their derived claims become eligible for propagation or synthesis. The steps below describe the authoring responsibilities that remain regardless of automation.

### When new data emerges:

1. **Determine scope:** Which concepts or mechanisms does this affect?
   - Example: "New data on BHB + NLRP3" → affects `wiki/nlrp3-exploit-map.md`, `wiki/bhb-ketones.md`

2. **Update the relevant wiki page(s):**
   - Add new content or revise existing claims inline with evidence level and inline provenance (`(source: <filename>)`)
   - Update YAML frontmatter if adding cross-references

3. **Update `index.md`** if a new page was created or the mission or portfolio changed.

4. **Verify consistency:**
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

### Task: Revise a mechanism based on new data

1. Edit the relevant wiki page(s)
2. Update evidence level tags and citations
3. Re-read all wiki pages that reference this mechanism
4. Update wiki pages with new understanding

### Task: Ensure a new page is discoverable

1. Add to `index.md` with one-line description
2. Link from related wiki pages using standard markdown links
3. Include YAML frontmatter with `title`, `date`, `tags` (and `related`, `sources` when applicable)

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

## Questions to Ask When Evaluating New Information

1. **What's the evidence level?** (Clinical, animal, in vitro, mechanistic)
2. **Does this affect multiple wiki pages?** (Trigger doc sweep rule)
3. **Are there new concepts?** (Trigger new wiki page creation)
4. **Are assumptions/limitations stated clearly?** (Maintain rigor)
5. **Is it PhD-audience appropriate?** (No marketing, honest about unknowns)

---

## Version Control & Maintenance

- **Source of truth:** `wiki/`
- **Dashboard:** `index.md` (repo root)
- **Action queue:** `synthesis/queue/` (per-item files); architecture at `synthesis/README.md`
- **Canonical material (read-only):** `reference/`
- **Published format:** `*.html` (do not edit directly)
- **Metadata:** YAML frontmatter in all `.md` files
- **Cross-references:** Prefer standard markdown links; Obsidian `[[wiki-links]]` work in Obsidian but not on GitHub
- **Revision history:** Git. No inline changelogs in documents.

### Global-multilingual research by default (no English-only bias)

Treat the wiki sweep, every literature scan, every subagent research task, and every "what does the field say" investigation as **multilingual by default.** The AI substrate (Claude, DeepSeek, Qwen, Gemini) is fluent in Chinese, Japanese, Korean, German, Russian, French, Spanish, Arabic, Hindi, Portuguese, Italian and more. The marginal cost of reading a Chinese-language paper or Japanese database is zero. Treating language as a "barrier" in 2026 is path-dependent narrowing — it silently shrinks the search space and biases findings toward the English-language Western-research subset.

**Operational rules:**

- **Lit scan briefings** (subagent prompts) MUST explicitly include non-English sources where relevant: ChiCTR (China Clinical Trial Registry), CNKI / WanFang (Chinese-language papers — read in original, no translation step needed), J-STAGE / CiNii / J-GLOBAL (Japanese), KISS / RISS (Korean), eLIBRARY.RU (Russian), TIB / GND (German), SciELO (Latin American Spanish/Portuguese). For each query, name the non-English sources to check.
- **Distributed synthesis prompts** should explicitly note that the wiki may have inherited Western-research bias and that genuinely new connections may require non-English-source angles.
- **Compound and mechanism investigations** should check both Western (PubMed-indexed) AND Chinese (CNKI / TCM materia medica) AND Japanese (Kampo medicine literature) sources before declaring an evidence-tier verdict. A compound with thin Western evidence but substantial Chinese clinical evidence has stronger empirical backing than the Western-only view shows.
- **Query-framing discipline** *(added 2026-05-19, Cluster M walkthrough — promoted from comp-018 Phase 2 finding)***:** for non-Western-medicine compound discovery, **query by traditional-formula-name + species-name + traditional-pathology-framing IN ADDITION TO mechanism-name.** Mechanism-name is the wrong starting point for non-Western literature — it silently filters out traditional-name-anchored papers that the Western citation network underweights. The canonical worked example: a "C3 convertase inhibitor" query misses *Houttuynia cordata*; a "*Houttuynia cordata* anti-complementary" query catches it (comp-018 Phase 2). The lesson generalizes across mechanism classes:
  - **URAT1 inhibitors:** "URAT1 inhibitor natural product" misses Smilax glabra formulations; "Si Miao San 四妙散 hyperuricemia" catches them.
  - **XO inhibitors:** "XO inhibitor flavonoid" misses many curcuminoids; "Jiang Huang 姜黄 xanthine oxidase" (turmeric) catches them.
  - **NLRP3 inhibitors:** "NLRP3 inhibitor natural product" misses *G. lucidum* spore-powder evidence; "Lingzhi 灵芝 anti-inflammatory mechanism" catches it.
  - **Complement modulators:** Pass 3's diagnosis was "language barrier" for Chen Daofeng / Yamada-Kiyohara groups — actually wrong; those groups publish 80–95% in English. The real barriers are **citation-network insularity + traditional-name vs mechanism-name query framing + source-journal impact-factor underweighting.** Treating it as a language barrier silently shrinks the search space.
  
  **Operational pattern:** every lit-scan subagent prompt should include traditional-formula-name + species-name + traditional-pathology-framing query variants when the compound class has non-Western traditional-use literature. ChEMBL-only coverage (comp-013, comp-014, comp-018, comp-020 all document) systematically undercovers non-Western natural-product domains; the query-framing discipline is the cheapest fix for that gap.
- **Do not flag "language barrier" as a limitation** in wiki pages or subagent briefings. It is not a limitation. If a relevant source is non-English, read it directly, cite it directly (with original-language title in the citation alongside an English gloss).
- **Brian-facing summaries stay in English** — the multilingual ingestion happens upstream; the synthesis you present to Brian is in English. The discipline is about what you READ, not what you WRITE for the project's working language.

**Why this rule exists:** explicitly added 2026-05-05 after a TCM × modern rigor scope page was drafted with "language barrier" listed as a limitation. Brian's correction: *"i think one of the things that i want to take advantage of is that you are multilingual, so you can read chinese papers. you can read chinese text. you can read japanese. so we should be ingesting EVERYTHING not just western-centric research. seems foolish to not search globally in 2026."* Path-dependent narrowing, exactly the failure mode the umbrella's "Curiosity and First-Principles Framing" rule warns against.

#### Translation protocol (two-model independent cross-check + inline disagreement annotations)

When ingesting non-English source material, **translate with two independent models** (different vendors) and produce an annotated translation that **surfaces disagreements as inline annotations rather than silently picking a winner** — the same heterogeneity guard the sweep daemon uses (translation carries the same homogenization risk). For Chinese sources, at least one model must be a Chinese-vendor model (DeepSeek / Qwen). Load-bearing disagreements (evidence tier, dose, mechanism) get a `[TRANSLATION-DISAGREEMENT]` flag. Rationale: translation is interpretation, and the disagreements are exactly where nuance lives.

**Full protocol** — operational pattern, disagreement-annotation conventions, high-risk categories, the Model-A cost rule, and the "why": [`wiki/etc/manual-literature-mining.md` §"Translation protocol"](./wiki/etc/manual-literature-mining.md). The `lit-scan` skill and `translate_source_two_model()` in `wiki/etc/experiments/lib/agentic_lit_synthesis.py` implement it. (Added 2026-05-05; consolidated to the methodology doc 2026-07-14.)

### Push-batching discipline (Open Enzyme overrides the umbrella's "push immediately" rule)

The umbrella repo's `CLAUDE.md` git steward pattern says "Push immediately after each commit, every time." **That rule is overridden in this repo.** Relevant pushes run publishing, exact COMP review when applicable, and bounded propagation. Full synthesis is manual, but coherent push batches still reduce repeated propagation, review cost, and merge contention.

**Commit eagerly. Push at logical batch boundaries.**

| Push when | Don't push when |
|---|---|
| End of a queue walkthrough (after the inbox-zero pass) | After every individual commit during active session |
| End of a clearly-bounded work batch (e.g., a peer-track scope page + its 6-surface tracking infrastructure) | After each subagent's output lands in isolation |
| User explicitly says "push" or "ship it" | Just because a commit is "done" |
| End of session | Just because the working tree is clean |
| Before walking away from the laptop with unpushed work pending | Just because propagation has not caught up yet |

**Operational rules:**
- Commit immediately after each substantive write (per the umbrella steward pattern — that part still applies).
- Hold all pushes until a batch boundary OR end of session.
- If asked "did you push?" — answer honestly. Don't auto-push to clear the conversation.
- Surface uncommitted-but-unpushed state at end of session: "8 commits sitting locally, ready when you want to push."
- The exception: if the work is genuinely time-critical (e.g., a hotfix to a broken page that's actively being read by collaborators), push immediately. Default is batch.

**Why this matters specifically for this repo:** coherent batches reduce repeated COMP review and propagation while preserving free publishing. Full synthesis accumulates changes across any number of pushes and runs only when explicitly requested.

---

## Contact & Escalation

If you're uncertain about scope, evidence standard, or whether a change triggers the "doc sweep rule", default to **conservatism**: err toward more updates, not fewer. This project is rigorous for PhD scientists, and consistency is non-negotiable.

**Project Lead:** Brian Abent (brian.abent@gmail.com)
