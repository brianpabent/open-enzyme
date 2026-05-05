---
name: walk-synthesis
description: Walk wiki/synthesis.md item-by-item with Brian, propose action for each, execute with his go-ahead, annotate the actioned items, and finish with an inbox-zero pass + single-push handoff to the sweep daemon. Codifies the conventions discovered ad-hoc during the 2026-05-05 walkthrough — item discipline, CTO-not-PhD framing, subagent decision tree, multi-surface follow-up tracking, and final-push merge handling. Invoke when Brian says "walk the synthesis," "walk the sweep," "walk the queue," or `/walk-synthesis`.
---

# /walk-synthesis

Walk `wiki/synthesis.md` item-by-item, action each with Brian's go-ahead, prune to inbox-zero, and ship the batch with a single push.

## Background

`wiki/synthesis.md` is the action queue produced by the wiki sweep daemon (multi-pass: propagate → synthesize → critique → DeepSeek peer-review). The daemon prepends new findings; humans (or AI in human's stead) action them and prune. This skill codifies the discipline that makes the walkthrough fast and consistent.

**Why this skill exists.** During the 2026-05-05 walkthrough, several things had to be discovered mid-session: that Brian wants explicit item-by-item walking (not batched action), that the CTO-not-PhD framing rule must be applied to every briefing, that follow-ups need multi-surface tracking to survive, that the daemon may run in parallel during a long session and create section-number collisions on push. This skill front-loads those lessons.

**What this skill does NOT do.** It doesn't auto-action items. It doesn't decide for Brian. It runs the *process* of walking; the *decisions* belong to him, item by item.

## When to use

| Situation | Use? |
|---|---|
| Brian says "walk the synthesis" / "walk the sweep" / "walk the queue" | Yes |
| `/walk-synthesis` invoked | Yes |
| `wiki/synthesis.md` has items pending and Brian wants to process them | Yes |
| One specific item needs actioning (not full walkthrough) | Skip skill — action directly |
| Brian wants only the inbox-zero cleanup pass | Skip to Section 7 |
| You're mid-conversation and Brian says "let's keep going" on a walkthrough already in progress | Continue from current item; don't restart |

---

## Section 1 — Pre-flight

Before announcing the first item, do all of these:

1. **Pull latest.** Catches any daemon work that landed since last session.
   ```bash
   cd "/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme"
   git pull --rebase
   ```
   If `.claude/` paths block the rebase with "Operation not permitted," retry with `dangerouslyDisableSandbox: true`. If conflicts, resolve via the patterns in Section 8.

2. **Read `wiki/synthesis.md` end-to-end.** Inventory every item. Synthesis files are typically structured: New Connections (N items), Contradictions Found (M items), Proposed Experiments (K items), Open Questions (J items), Priority Actions (L items). Total = N+M+K+J+L. **Number them globally** (item 1/total through item total/total) so Brian can navigate.

3. **Look at the Strategic Reflections Queue at the bottom.** Note any pending content-triggered reflections. Do not action these as part of the walkthrough — they fire on substance, not on the walkthrough cadence.

4. **State the inventory back to Brian in one short message** before starting item 1. Format:
   > "Sweep dated YYYY-MM-DD has X items: N Connections, M Contradictions, K Proposed Experiments, J Open Questions, L Priority Actions. Ready to walk them 1-by-1?"

5. **Check for in-flight subagents** (from prior sessions or earlier in this conversation). If any are running, note their target files so you don't collide.

6. **Wait for "go" / "yes" / "engage"** before presenting item 1.

---

## Section 2 — The walking discipline

This is the rule Brian had to remind me of mid-session: **one item at a time.**

For each item:

### Step A — Brian-facing briefing (BEFORE any action)

The briefing has a strict structure that respects the CTO-not-PhD framing:

```
**Item N/total — [Section type]: [Item title]**

**The plain-English version:**
[1–3 paragraphs. Lead with the headline finding in one sentence. Gloss every jargon term on first use 
(e.g., "URAT1 [the kidney transporter that reabsorbs urate from urine back into the blood]"). 
Walk the mechanism like a flowchart, not a research paper. Use analogies where they help.]

**What the existing Claude review said:**
[1–2 sentences summarizing the inline review. Quote the verdict if it's pithy ("Confirmed, prioritize" / 
"Augment" / "Defer" / "Rejected as new"). Note if the review changes the synthesizer's framing.]

**What I'd propose to do:**
[Concrete action. Name files that would change. Estimate scope ("inline, ~10 min" / "subagent, ~5 min 
to spawn" / "no wiki work needed — already done" / "needs your decision between A and B").]

[If decision needed:] **My recommendation:** [Option] — [one-sentence justification].

[End with:] OK to proceed?
```

**CTO-not-PhD enforcement.** Brian has explicitly said he is not a PhD and cannot read raw papers usefully. Apply these rules to every briefing:

- Lead with the headline finding in one accessible sentence.
- Gloss jargon on first use. If a term is unavoidable and unfamiliar, define it inline.
- Mechanism in plain English: "X turns Y on, which causes Z" — not "X transcriptionally upregulates Y, leading to downstream activation of Z."
- Use analogies where they help ("transit organisms — they pass through your gut over hours, then leave"). Never apologize for them.
- Numbers in context: "0.388 (39% of theoretical max)" not bare "0.388".
- Tables when comparing 3+ things; prose when explaining 1–2.

### Step B — Wait for go-ahead

Do NOT action the item until Brian says "yes" / "go" / "engage" / "do it" / "proceed" / similar. If he asks a clarifying question, answer it and re-ask. If he picks a different option than your recommendation, action his choice without resistance.

### Step C — Action it

Three execution patterns:

| Action type | How |
|---|---|
| **Inline (you do it)** | Edit files directly. Most cross-link updates, small wiki-page additions, synthesis annotations. |
| **Background subagent** | When the work is independent and you want to keep walking other items. See Section 4 for Sonnet vs. Opus decision. |
| **Foreground subagent** | When the agent's result blocks the next item or you need its findings before continuing. |
| **Already done** | If the existing wiki state already reflects the action, write a closure note in synthesis.md instead of re-doing the work. |

### Step D — Annotate `✓ Actioned`

Immediately after the work lands, add this annotation directly under the relevant Claude review block in `wiki/synthesis.md`:

```markdown
**✓ Actioned YYYY-MM-DD:** [What was done — name the files changed, key decisions made, and where the 
work landed canonically. If the action was a closure note ("already done"), say so explicitly.] [Cross-link 
to new pages, sections, or experiments created.] [If follow-ups were created, list them with where they're 
tracked.]
```

**The annotation is non-optional.** It closes the loop and documents what shipped.

### Step E — Commit immediately

Per Brian's git steward pattern (from the umbrella CLAUDE.md), commit after each substantive write — don't batch. The commit message:

```
sweep item N: <one-line action summary>

<2-4 line body covering: what shipped, which files, any decisions made,
any follow-ups queued. Cross-reference the synthesis.md annotation if useful.>

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
```

**Do NOT use `[skip-wiki-sweep]`.** That marker is reserved for daemon-generated commits. Hand-applying it suppresses the sweep on user content (root cause of the 2026-04-27 walkthrough's blind spot — see CLAUDE.md). The commit-msg hook enforces this.

**Hold the push until end of batch** (Section 7) so the daemon fires once across the whole batch, not N times.

---

## Section 3 — Item-type playbooks

Each synthesis section has its own playbook for what action typically lands.

### Connections
Usually: extend an existing wiki page with a new mechanistic synthesis section, update cross-references, possibly add a bullet to a related concept page. Rarely needs a new page.

### Contradictions
Usually: either (a) document the contradiction with a stratified-guidance section in the relevant page, or (b) propose a wet-lab experiment that resolves it (then add to validation-experiments.md). Often actioned earlier in the sweep — check before re-actioning.

### Proposed Experiments
Three sub-cases:
- **Already in `validation-experiments.md`:** closure note, no new work. Most proposed experiments duplicate existing entries — check first.
- **Needs new entry:** add a new §1.X section in `validation-experiments.md`. Use the Tiered Protocol pattern (Tier 1 → gated Tier 2 → gated Tier 3) when escalating cost matters.
- **Needs computational prior first:** spawn a `new-comp-experiment` skill instead.

### Open Questions
Three sub-cases:
- **Closed by prior work:** closure note pointing at the experiment that closed it (e.g., §1.21 closed CP0 natural-product question).
- **Genuine open question, evidence thin:** queue a literature scan (Opus subagent) — see Section 4.
- **Genuine open question, exploration vector:** create a dedicated scope page following Section 5 — see also `engineered-lbp-chassis.md` and `sirna-urat1-modality.md` as reference shapes.

### Priority Actions
Almost always either:
- **Already done structurally** (e.g., Ward 1995 §1.9 was already #1 priority gate before the sweep re-asserted it): closure note, name the execution-bottleneck if any.
- **Needs propagation work** (e.g., supplement stratification): verify what's already there, do the propagation if needed, closure note.
- **Needs a new dedicated wiki page** (e.g., siRNA / URAT1): see Section 5.

---

## Section 4 — Subagent decision tree

When to spawn an agent vs. action inline, and which model.

### Inline vs. subagent

| Work type | Action |
|---|---|
| Cross-link updates across 2–6 files | Inline |
| Annotation in `synthesis.md` | Inline |
| New scope page following an established template | Inline (you've already mastered the template) |
| Multi-query literature scan with judgment | Subagent (Opus) |
| Computational experiment using established framework | Subagent (Sonnet, via `new-comp-experiment` skill) |
| Plain-English summary for Brian to Q&A on | Subagent (Opus) |
| Comparative analysis across 5+ heterogeneous data sources | Subagent (Opus) |

### Sonnet vs. Opus

| Pick | When |
|---|---|
| **Sonnet** | Work is mechanical: running an established analysis pipeline, generating a wiki page from an existing template, executing a concrete step-by-step protocol. Outcome is procedural correctness, not judgment. |
| **Opus** | Work is interpretive: weighing evidence quality across heterogeneous studies, distinguishing strong from weak signals, deciding between A and B on borderline evidence, translating PhD content into accessible plain English without losing nuance, novel synthesis. |

If unsure → Opus. Cost difference is small relative to the cost of low-quality judgment in user-facing output.

### Foreground vs. background

| Pick | When |
|---|---|
| **Foreground** | The agent's result blocks the next decision (e.g., "is this engineering thesis viable" before deciding to invest more in scoping it). |
| **Background** | Work is genuinely independent. Example: launching three subagents in parallel during a walkthrough so you can keep walking other items while they work. |

### Briefing rules

Subagents have NO conversation context. The prompt must be self-contained and brief them like a smart colleague who walked into the room. Include:

1. **What you're trying to accomplish and why** (the platform-level goal, not just the immediate task)
2. **What you've already learned or ruled out** (so they don't re-do the work)
3. **Files they CAN touch** vs. **files to avoid** (if other agents are in flight, name them)
4. **Constraints** (style, length, evidence level conventions, any "don't" rules from project CLAUDE.md)
5. **What they should report back** (length cap, structure)
6. **Memory cautions** if relevant (e.g., "Paperclip MCP `map` operator hallucinates — use `search` / `cat` / `grep` instead" per `memory/feedback_paperclip_map_unreliable.md`)

### File-collision management

When multiple subagents are in flight, brief each on what files OTHER agents are touching. The most common collision points:

- `wiki/computational-experiments.md` (any comp-NNN agent will edit this)
- `wiki/modality-chokepoint-matrix.md` (peer-track scope-page agents edit per-modality sections)
- `wiki/synthesis.md` (any agent can add an actioned annotation)
- `wiki/validation-experiments.md` (experiment-creating agents add §X.Y entries)
- `experiments/lib/protease_stability.py` (locked — orchestrators import only, never modify)

If two agents will touch the same file, sequence them or have only one do the shared-file edits as carry-along.

---

## Section 5 — Multi-surface follow-up tracking (the "how do we remember" answer)

When an item creates a new exploration vector, peer-track scope page, or set of follow-ups that won't fire today, **bake the tracking across 6 redundant surfaces** so it survives the next sweep.

| Surface | What goes there |
|---|---|
| 1. The new page's own "Open Follow-Ups" section | Phase 2 items as a numbered list with status (Queued / In progress / Done) |
| 2. `wiki/open-questions.md` topical entry | A new section under the right topic heading, mirroring the Phase 2 list |
| 3. `wiki/computational-experiments.md` Planned Analyses table | Any comp-NNN follow-ups (with "Informs" pointing to the new page) |
| 4. `wiki/hypotheses/HNN-<thesis>.md` falsification card stub | Forces "what would kill this thesis" framing; full population queued as a Phase 2 item |
| 5. `index.md` cheapest-experiments table | The 1–2 highest-leverage Phase 2 items (the daemon-fires-on-push surface that catches Brian's eye most often) |
| 6. `wiki/synthesis.md` actioned annotation + Strategic Reflections Queue | The annotation closes the item; the Reflections Queue holds content-triggered platform reframes |

**Phase taxonomy** (use these labels for clarity):
- **Phase 1:** what we do now in this session
- **Phase 2:** queued in silico follow-ups, no pharma-partner dependency, can be subagent-executed in future sessions
- **Phase 3:** content-triggered reflections — fire when accumulated substance crosses a maturity threshold (not calendar-triggered)

Phase 3 entries belong in the Strategic Reflections Queue subsection of `wiki/synthesis.md` so the daemon surfaces them on every sweep.

---

## Section 6 — Templates

### Actioned annotation (under the Claude review block)

```markdown
**✓ Actioned YYYY-MM-DD:** [What shipped — files, decisions, where canonical content lives now]. 
[Any new pages or sections created, with cross-links]. [Phase 2 follow-ups queued, with the 6-surface 
tracking pointers if applicable]. [Phase 3 reflection note location if relevant].
```

### Closure annotation (when nothing new needs to ship)

```markdown
**✓ Already actioned YYYY-MM-DD** (closure note): [Why no new work needed — point at where the canonical 
content already lives, with file/line references]. No additional wiki work needed for this [Connection / 
Contradiction / Open Question / Priority Action].
```

### Peer-track scope-page skeleton (frontmatter through cross-references)

```markdown
---
title: "[Modality / Vector] — [Peer Track Description]"
date: YYYY-MM-DD
tags: [primary, secondary, tertiary, platform-strategy, first-principles]
related:
  - modality-chokepoint-matrix.md
  - [parent-mechanism-page.md]
  - open-questions.md
  - open-enzyme-vision.md
  - synthesis.md
  - hypotheses/HNN-<thesis>.md
sources:
  - "[Key precedent 1 — citation]"
  - "[Key precedent 2 — citation]"
status: scope-page
---

# [Modality / Vector] — [Peer Track Description]

**Status:** scope-page (YYYY-MM-DD). [One-sentence mission statement].

## Why this page exists

[Frame the modality as a peer-track exploration vector under the broader gout-solving mission. Cite the 
matrix entry that surfaced it. Position relative to existing tracks: koji (primary), and any sister 
peer-tracks already scoped — e.g., LBP and siRNA / URAT1 are sister tracks under the chase-every-avenue 
framing established 2026-05-05].

## [Mechanism / What this is and why it matters]

[2–3 paragraphs. Plain English. Mechanism + why it matters for gout specifically.]

## Candidate [species / chemistries / approaches]

### Primary candidate
[Why this is the lead]

### Secondary candidates
[Why these are also in scope]

## [Key strength — the dual-action / sequence-specificity / durability angle]

[The mechanistic claim that makes this vector distinctive]

## The hard part: [delivery / regulatory / cost / etc.]

[The honest engineering / commercial / regulatory gating problem. Don't sugar-coat. Name the timeline 
honestly — "5–8 years" or "10+ years" if that's the truth.]

## Competitive / clinical landscape

[Existing programs, partner profile, what would compete with this and what wouldn't]

## Position in the Open Enzyme platform

[Discovery-engine output vs. strain-library output. Reference open-enzyme-vision.md §2.2 for the 
two-track narrative.]

## Comparison with [koji and any sister peer tracks]

[Table comparing dimensions: chassis, manufacturing, regulatory, distribution, capital, timeline, 
patient population, OE output type]

## Open Follow-Ups

[Numbered table P2-1 through P2-6 with ID / Item / Type / Status. Phase 3 entry at the end if relevant.]

## Limitations of this page

[Scope-page caveats; OE expertise gaps; honest uncertainty]

## Cross-References

[Bulleted list of every related wiki page]
```

### Falsification card stub (for new theses created during the walkthrough)

Modeled on `wiki/hypotheses/H02-engineered-lbp-thesis.md` and `H03-sirna-urat1-thesis.md`. Stub-level commit registers the hypothesis; full population is queued as Phase 2 P2-5. Stubs MUST include:

- Frontmatter (id, title, committed date, status: Stub, related, sources)
- Stub-status note (full population queued, pre-registration applies only on upgrade)
- Provisional Claim (the thesis in 1–2 paragraphs)
- Placeholder sections for: Assumption Stack, Killshot Menu, Pre-Committed Thresholds, Failure Modes Probed
- Status block (Pending / Survival count 0)
- Cross-references including sibling H-cards

### Tiered wet-lab protocol entry (for `validation-experiments.md`)

When a new wet-lab experiment has cost-escalating tiers gated on prior-tier results (e.g., §1.23 androgen × MSU × NLRP3):

```markdown
### 1.X [Title — Tiered Mechanistic Protocol]

**Status**: Proposed | **Cost**: Tier 1: $A; full T1+T2+T3 cascade $B–C | **Weeks**: Tier 1: D–E; full cascade ~F months | **Phase**: 1

**Affected wiki**: [list of related pages]

**What it tests:** [1 paragraph framing the literature gap and why this matters]

**Proposed in:** [synthesis.md reference]

**Background on the gap:** [1 paragraph]

**Protocol — Tiered, gating logic:**

**Tier 1 — [Lowest-cost, broadest-cohort assay] ($A; D–E weeks):**
- [Cells / system]
- [Pre-treatment / variables]
- [Challenge]
- [Readouts]
- **Success criterion (Tier 1 → Tier 2):** [Specific quantitative threshold for advancement]

**Tier 2 — [Mid-cost, more-relevant assay] (gated on Tier 1 positive):**
- [Same structure]
- **Success criterion (Tier 2 → Tier 3):** [...]

**Tier 3 — [In vivo or gold-standard assay] (gated on Tier 2 confirmation):**
- [Same structure]
- **Success criterion:** [Causal demonstration or platform-implication threshold]

**Tier 4 (n=1, parallel and independent) — [if applicable]:** see [`self-experiment-protocol.md` §X].

**Estimated cost (full cascade):** [breakdown]
**Estimated timeline (full cascade):** [breakdown]

**Success criteria (overall):** [What each outcome means for the platform]

**Limitations:** [explicit list]

**Cross-references:** [related pages and sections]
```

---

## Section 7 — End-of-walkthrough operations

After the last item is actioned and committed:

### 7.1 — Inbox-zero pass on `wiki/synthesis.md`

The pruning convention is established by the file's own meta-header: actioned items get deleted (preserved in git history + sweep logs). When all items in a sweep block are actioned:

1. **Delete the entire sweep block** (Connections, Contradictions, Proposed Experiments, Open Questions, Priority Actions, Sources cited — the whole thing).
2. **Preserve the Strategic Reflections Queue** (content-triggered, hasn't fired).
3. **Update "Pending — open items"** to `**(none — inbox zero as of YYYY-MM-DD).**` plus a one-paragraph note pointing to the audit trail (`git log --since=YYYY-MM-DD` and `logs/v4-synthesis-*.md`).
4. **Add a row to the Sweep history table** with date / trigger / synthesizer / reviewer / log path. If the sweep was a substantive duplicate of another, note that.
5. **Update "Where actioned items live now"** to include any new canonical homes created during the walkthrough (new wiki pages, new H-cards, new comp-NNN folders, new validation-experiments §X.Y entries, new self-experiment-protocol sections).

Target file size after pruning: ~80 lines (~2 KB). The 2026-05-05 inbox-zero dropped synthesis.md from 323 → 80 lines.

Commit:
```
synthesis: YYYY-MM-DD inbox-zero pass

Pruned the YYYY-MM-DD sweep block (N items, all actioned during this session).
[If duplicate sweep also pruned, name it.]

File reduced from X → Y lines. Findings preserved in:
- Canonical wiki pages (per "Where actioned items live now" — updated)
- Sweep history table (entry added)
- Strategic Reflections Queue (preserved)
- git log + logs/v4-synthesis-*.md

Pending — open items: (none — inbox zero as of YYYY-MM-DD).

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
```

### 7.2 — Single push at end

```bash
cd "/Users/brianabent/Documents/Claude/Projects/abent/Open Enzyme"
git push
```

The sweep daemon fires on push to `wiki/*.md`. Pushing once at end means **one daemon run, not N**.

### 7.3 — Anticipate the merge

The daemon may have run in parallel during a long walkthrough session (separate trigger commits earlier in the day). Push will likely be rejected with "remote contains work that you do not have locally." See Section 8 for handling.

---

## Section 8 — Anticipated friction points

### 8.1 — `.claude/` sandbox blocks

Symptom: `git pull --rebase` (or any git operation touching `.claude/skills/*` or `.claude/settings.json`) fails with "Operation not permitted" / "could not detach HEAD."

Fix: Retry the same git command with `dangerouslyDisableSandbox: true`. Do not attempt to chmod or delete the .claude paths.

### 8.2 — Daemon parallel-run conflicts on final push

Symptom: `git push` rejected; `git pull` reveals 2–4 new daemon-generated commits on `origin/main` (sweep-1-propagate, sweep-2-synthesize, sweep-3-review, sometimes sweep-4-deepseek) plus a new log file under `logs/`.

**Use `git merge`, not `git pull --rebase`,** for the final integration. Reason: `--rebase` will replay each of your N commits individually, hitting the same conflict (especially section-number collisions) on every commit that touches the same file. A merge resolves the conflict ONCE.

```bash
git merge origin/main --no-edit  # may exit with conflicts
```

Common conflict patterns:

- **`wiki/synthesis.md`:** daemon's fresh sweep block usually duplicates content you already actioned. Take ours (the inbox-zero version). Add a sweep-history row noting the daemon's sweep was substantively duplicate.
- **`wiki/validation-experiments.md`:** section-number collision (most common). Daemon assigned §1.X to its experiment; you assigned §1.X to a different experiment. Keep yours; renumber daemon's to §1.X+N (whichever has fewer cross-references). Update all cross-refs (search: `grep -rn "§1\.X" --include="*.md"`).
- **`index.md`:** keep both sides; update any cross-refs whose section number changed.

After resolution: `git add` the resolved files, `git commit --no-edit -m "<descriptive merge message>"`, then `git push`.

### 8.3 — Subagent file collisions

Symptom: a background agent edits a file you also need to edit; their edits land first; your subsequent Edit tool call fails with "File has been modified since read."

Fix: Re-read the file before editing. The Edit tool requires the most recent file state in context.

### 8.4 — Untracked files missed by `git commit -am`

Symptom: `git commit -am` succeeds but a new file you created earlier in the session is still listed as untracked.

Fix: `git add <file>` explicitly for new files. The `-a` flag only stages already-tracked files. After fixing, do a follow-up commit named `add: <files>` (NOT `--amend`).

### 8.5 — Brian's CTO-not-PhD reminder

Symptom: Brian says some variant of "I'm not a PhD" or "what does X mean" or "I can't read papers."

Fix: Re-anchor on the CTO-not-PhD framing rule (Section 2 Step A). Don't apologize at length — just rewrite the briefing in plain English and continue. The rule is in `memory/user_role.md` and should already be active.

---

## Section 9 — Anti-patterns (things that went wrong in 2026-05-05)

1. **Don't action multiple items without explaining each one first.** Brian's correction mid-session: "but there's more that you did without me!" The single-item discipline is non-negotiable.

2. **Don't dump raw papers — translate.** The lit-scan agent's output that worked best was the plain-English Q&A briefing, not the citation block.

3. **Don't add `[skip-wiki-sweep]` to user-content commits.** The commit-msg hook will reject it. The marker is reserved for daemon commits only.

4. **Don't use `git commit -am` when there are untracked new files.** The `-a` flag misses them. Stage explicitly.

5. **Don't pick numbered section IDs (§1.X) without checking remote.** The daemon may have run in parallel and added §1.X to validation-experiments.md while you were working. If walking spans multiple hours, do a fresh `git fetch` before assigning numbers.

6. **Don't `git pull --rebase` for the final integration when many commits touch the same file.** Use `git merge` so the conflict resolves once, not N times.

7. **Don't lose follow-ups.** When an item creates Phase 2 / Phase 3 work, bake the tracking across the 6 redundant surfaces (Section 5). Single-surface tracking evaporates by the next sweep cycle.

8. **Don't action heavyweight items without Brian's go-ahead.** Even if the action looks obvious. The "wait for go" rule supersedes any automation impulse.

---

## Section 10 — What this skill does NOT cover

- **Computational experiment authoring** — use the `new-comp-experiment` skill instead. This skill spawns it as a subagent when needed.
- **Wiki sweep daemon mechanics** — see `scripts/SWEEP-ARCHITECTURE.md`. This skill consumes the daemon's output; it doesn't run the daemon.
- **Brian's personal medical context** — privacy boundary. Personal data lives in private sibling repos, never in synthesis annotations.
- **Decisions Brian hasn't made** — strategic platform reframes (e.g., Phase 3 platform-framing reflections) belong to Brian. This skill queues them; it doesn't execute them.

---

## Naming and file-path conventions

- **Skill location:** `.claude/skills/walk-synthesis/SKILL.md`
- **Invoke via:** `/walk-synthesis` slash command, or natural-language "walk the synthesis" / "walk the sweep" / "walk the queue"
- **In prose:** "the walkthrough," "this walkthrough" — not "the synthesis walking process"
- **Date format:** ISO 8601 (YYYY-MM-DD) everywhere. The annotation date is the calendar date the work shipped, not the date of the originating sweep.

---

## Provenance

This skill codifies conventions discovered during the 2026-05-05 walkthrough of the 14-item DeepSeek V4-Pro / Gemini 2.5 Pro / Claude Opus 4.7 synthesis sweep on commit `734bf51` (and the substantively duplicate 2026-04-28 sweep). The session produced: comp-005 (lactoferrin), comp-006 (DAF/CD55, via Sonnet subagent), comp-007 (food-grade HDACi, via Sonnet subagent), the engineered LBP chassis scope page (sister to koji), the siRNA / URAT1 modality scope page (discovery-engine output), H02 + H03 falsification card stubs, validation-experiments §1.23 (androgen × MSU × NLRP3 four-tier protocol), self-experiment-protocol §11.1 (n=1 ex vivo PBMC MSU challenge), the androgen × NLRP3 literature scan section in `androgen-urate-axis.md`, and the inbox-zero pass on `synthesis.md`. The conventions in this skill are the rules that, in retrospect, would have made that session smoother.
