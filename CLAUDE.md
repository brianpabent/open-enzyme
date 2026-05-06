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

- `wiki/synthesis.md` — Cross-doc connections, contradictions, proposed experiments. **Action queue.** Daemon prepends new findings after Pass 2; AI annotates actioned items inline as the work lands (`**✓ Actioned <date>:**` directly under the relevant Claude review block, briefly describing what landed in which file); Brian prunes manually in his review pass.
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
3. Write with evidence levels (see Rule 5 below)
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

**Operational protocol:** see [`wiki/manual-literature-mining.md` §"Pre-commit verification gate"](./wiki/manual-literature-mining.md#pre-commit-verification-gate-the-rule-that-catches-errors-before-the-sweep-not-after) — the canonical statement of the discipline, including the per-claim micro-protocol (identify load-bearing numbers → name primary source → grep-verify → cite line-anchored → drop or placeholder if unverifiable).

**Why this rule exists:** The wiki sweep daemon catches cross-page inconsistencies in Pass 2 / Pass 3 / Pass 4, but by then the wrong number has already propagated to multiple pages and been ingested into downstream synthesis. The DAF SCR1-4 disulfide-count incident (2026-05-06) is the canonical case: a Sonnet subagent authoring `wiki/daf-cd55-scr14-truncated-computational.md` (comp-012) hallucinated "3 disulfides per SCR domain → 12 total" in 4 places of prose narrative — a number the comp-012 pipeline doesn't actually compute (its Limitations section says "Disulfide bonds not modelled"). The error propagated into `wiki/hypotheses/H05-daf-scr14-cp0-thesis.md` overnight, drove a downstream chaperone-orthogonal triple-cassette synergy panic ("17+12=29 disulfides, 1.8× Huynh"), and was only caught by the next day's sweep + walkthrough verification against UniProt P08174 (which has exactly 8 DISULFID feature annotations in SCR1-4 — canonical sushi/CCP fold, 2 per domain). The sweep is a backstop; the pre-commit gate is where this class of error should die.

**The discipline applies to all comp-NNN authoring runs, all H-card stubs, all scope pages, all primary-research wiki edits.** When delegating wiki authoring to a subagent, the verification protocol must be in the subagent's brief — not "verify if you have time," but "verify each load-bearing number against primary source before writing it into the page."

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
- Link to `index.md` for the dashboard, `wiki/synthesis.md` for the action queue.

**In index.md:**
- Keep the dashboard (platform thesis, synthesis queue, cheapest experiments) at the top.
- Keep the concept/research index below, with one-line descriptions.

**In wiki/GRAPH.md:**
- Update Mermaid diagram whenever concepts or relationships change.
- Ensure all nodes appear in at least one subgraph.
- Label edges with relationship type (e.g., "produces", "inhibits", "activates").

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

### Global-multilingual research by default (no English-only bias)

Treat the wiki sweep, every literature scan, every subagent research task, and every "what does the field say" investigation as **multilingual by default.** The AI substrate (Claude, DeepSeek, Qwen, Gemini) is fluent in Chinese, Japanese, Korean, German, Russian, French, Spanish, Arabic, Hindi, Portuguese, Italian and more. The marginal cost of reading a Chinese-language paper or Japanese database is zero. Treating language as a "barrier" in 2026 is path-dependent narrowing — it silently shrinks the search space and biases findings toward the English-language Western-research subset.

**Operational rules:**

- **Lit scan briefings** (subagent prompts) MUST explicitly include non-English sources where relevant: ChiCTR (China Clinical Trial Registry), CNKI / WanFang (Chinese-language papers — read in original, no translation step needed), J-STAGE / CiNii / J-GLOBAL (Japanese), KISS / RISS (Korean), eLIBRARY.RU (Russian), TIB / GND (German), SciELO (Latin American Spanish/Portuguese). For each query, name the non-English sources to check.
- **The sweep daemon's Pass 2 prompt** should explicitly note that the wiki may have inherited Western-research bias and that finding genuinely new connections often requires looking at non-English-source angles. (`scripts/sweep-prompt-2-synthesize.md` — update separately.)
- **Compound and mechanism investigations** should check both Western (PubMed-indexed) AND Chinese (CNKI / TCM materia medica) AND Japanese (Kampo medicine literature) sources before declaring an evidence-tier verdict. A compound with thin Western evidence but substantial Chinese clinical evidence has stronger empirical backing than the Western-only view shows.
- **Do not flag "language barrier" as a limitation** in wiki pages or subagent briefings. It is not a limitation. If a relevant source is non-English, read it directly, cite it directly (with original-language title in the citation alongside an English gloss).
- **Brian-facing summaries stay in English** — the multilingual ingestion happens upstream; the synthesis you present to Brian is in English. The discipline is about what you READ, not what you WRITE for the project's working language.

**Why this rule exists:** explicitly added 2026-05-05 after a TCM × modern rigor scope page was drafted with "language barrier" listed as a limitation. Brian's correction: *"i think one of the things that i want to take advantage of is that you are multilingual, so you can read chinese papers. you can read chinese text. you can read japanese. so we should be ingesting EVERYTHING not just western-centric research. seems foolish to not search globally in 2026."* Path-dependent narrowing, exactly the failure mode the umbrella's "Curiosity and First-Principles Framing" rule warns against.

#### Translation protocol (two-model independent cross-check + inline disagreement annotations)

When ingesting non-English source material, **translate with two independent models** (different vendors, ideally different training pipelines) and produce an annotated translation that surfaces disagreements rather than collapsing them. Same multi-vendor cross-check discipline the wiki sweep daemon already uses (Pass 2 Gemini + Pass 3 Claude + Pass 4 DeepSeek peer-review per `wiki/open-source-platform.md` §"Multi-model synthesis as guard against epistemic homogenization"). Translation has the same homogenization risk; the same heterogeneity guard applies.

**Operational pattern:**

1. **Two independent translations.** Pick two models from different vendors:
   - Model A: Claude (Anthropic) OR Gemini (Google)
   - Model B: DeepSeek OR Qwen (both Chinese-vendor; native-language depth) OR GPT-5 (OpenAI)
   For Chinese-source material, at least one model should be a Chinese-vendor model (DeepSeek or Qwen) — the native-language training depth catches idiomatic and classical-TCM-terminology nuances Western-trained models miss. For Japanese-source material, prefer including a model with strong Japanese (Claude is competent; Gemini is reasonable; for deep Kampo medicine terminology, a Japanese-vendor option if available; otherwise two competent Western models is acceptable).
2. **Sentence-level comparison.** Compare the two translations at sentence granularity (or paragraph if sentences are too short to differ meaningfully).
3. **Where models AGREE → confident translation.** Use that text directly.
4. **Where models DISAGREE → inline annotation.** Use a clear, scannable convention:
   ```
   The compound shows {Model A: "significant" | Model B: "notable"} reduction in IL-1β secretion at 10 μM.
   ```
   Or for substantive disagreements (different mechanism implications, different evidence tier, different magnitude):
   ```
   {Model A: "decreased serum urate by 1.2 mg/dL"} {Model B: "decreased serum uric acid by approximately 71 μmol/L"}
   [TRANSLATION NOTE: Models agree on direction and rough magnitude (1.2 mg/dL ≈ 71 μmol/L), differ on unit choice in the source. Verify against original-language paper if precision matters for downstream calculation.]
   ```
5. **For load-bearing claims, escalate.** If a translation disagreement affects an evidence-tier judgment, a dose calculation, a mechanism mapping, or a chokepoint assignment — flag it explicitly in the wiki with `[TRANSLATION-DISAGREEMENT]` so future readers know the underlying source has interpretive ambiguity. Do not resolve the disagreement silently by picking one translation.
6. **Specific high-risk categories** where translation disagreement should always be flagged: scientific terminology with mechanism implications (e.g., "inhibits" vs "modulates" vs "suppresses"), evidence-tier hedging language ("shows" vs "suggests" vs "may"), dosing units and routes, classical TCM / Kampo / Ayurvedic terminology vs modernized equivalents, statistical significance language, sample-size and study-design descriptions.

**Why two models, why independent, why surface disagreements:** translation is interpretation. A single model's interpretation has the model's training-distribution bias, vendor bias, and idiomatic-fluency strengths/weaknesses baked in. Two models from different vendors share less bias. The disagreements are EXACTLY where translation nuance lives — silently picking one model's choice loses information the original-language paper had. Surfacing the disagreement preserves the precision the source intended.

**Cost note:** translation runs add a small marginal cost per non-English source ingested (typically <$0.05 per paper at current API pricing). Negligible relative to the value of getting the translation right for load-bearing scientific claims. Does NOT add cost to the sweep daemon (which is English-corpus synthesis) — only to the explicit lit-scan / source-ingestion subagent flows.

**Why this rule exists:** added 2026-05-05 in the same conversation as the global-multilingual default. Brian's specific framing: *"if we bring in non-english papers, i think we need to have a protocol for translation that involves 2 completely independent models and we can have inline annotations where the models may disagree on nuance because in science nuance and precision matter."* The discipline matches the heterogeneity-guard logic already established for the sweep daemon.

### Push-batching discipline (Open Enzyme overrides the umbrella's "push immediately" rule)

The umbrella `~/Documents/Claude/Projects/abent/CLAUDE.md` git steward pattern says "Push immediately after each commit, every time." **That rule is overridden in this repo.** Reason: every push to `wiki/*.md` fires the multi-pass wiki sweep daemon (Pass 1 propagate → Pass 2 synthesize → Pass 3 review → DeepSeek peer-review). Each daemon run costs ~$0.65 and takes ~9–12 minutes; multiple parallel runs cause merge conflicts that consume far more time than the eager push saved.

**Commit eagerly. Push at logical batch boundaries.**

| Push when | Don't push when |
|---|---|
| End of a sweep walkthrough (after the inbox-zero pass) | After every individual commit during active session |
| End of a clearly-bounded work batch (e.g., a peer-track scope page + its 6-surface tracking infrastructure) | After each subagent's output lands in isolation |
| User explicitly says "push" or "ship it" | Just because a commit is "done" |
| End of session | Just because the working tree is clean |
| Before walking away from the laptop with uncommitted work pending | Just because the daemon hasn't caught up yet — let the daemon run on the FULL batch, not piecemeal |

**Operational rules:**
- Commit immediately after each substantive write (per the umbrella steward pattern — that part still applies).
- Hold all pushes until a batch boundary OR end of session.
- If asked "did you push?" — answer honestly. Don't auto-push to clear the conversation.
- Surface uncommitted-but-unpushed state at end of session: "8 commits sitting locally, ready when you want to push."
- The exception: if the work is genuinely time-critical (e.g., a hotfix to a broken page that's actively being read by collaborators), push immediately. Default is batch.

**Why this matters specifically for this repo:** the daemon's value comes from running on a *coherent* batch of related changes. Running it 6 times during a single session as 6 separate sweeps produces 6 fragmented synthesis blocks (often substantively duplicate of each other and of the canonical pages). Running it once at the end produces one coherent sweep on the full batch. The latter is cheaper, faster, and produces better synthesis output.

---

## Contact & Escalation

If you're uncertain about scope, evidence standard, or whether a change triggers the "doc sweep rule", default to **conservatism**: err toward more updates, not fewer. This project is rigorous for PhD scientists, and consistency is non-negotiable.

**Project Lead:** Brian Abent (brian@headsupresults.com)
