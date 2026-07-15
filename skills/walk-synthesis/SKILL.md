---
name: walk-synthesis
description: Walk synthesis/queue/ item-by-item with Brian, propose action for each, execute with his go-ahead, annotate the actioned items, and finish with an inbox-zero pass + single-push handoff to the sweep daemon. Codifies the conventions discovered ad-hoc during the 2026-05-05 walkthrough — item discipline, CTO-not-PhD framing, subagent decision tree, multi-surface follow-up tracking, and final-push merge handling. Invoke when Brian says "walk the synthesis," "walk the sweep," "walk the queue," or `/walk-synthesis`.
---

# /walk-synthesis

Walk `synthesis/queue/` item-by-item, action each with Brian's go-ahead, prune to inbox-zero, and ship the batch with a single push.

## Background

`synthesis/queue/` is the action queue produced by the wiki sweep daemon (multi-pass: propagate → synthesize → critique → peer-review). The daemon prepends new findings; humans (or AI in the human's stead) action them and prune. This skill codifies the discipline that makes the walkthrough fast and consistent.

**Why this skill exists.** During the 2026-05-05 walkthrough, several things had to be discovered mid-session: that Brian wants explicit item-by-item walking (not batched action), that the CTO-not-PhD framing rule must be applied to every briefing, that follow-ups need multi-surface tracking to survive, and that the daemon may run in parallel during a long session and create section-number collisions on push. This skill front-loads those lessons.

**What this skill does NOT do.** It doesn't auto-action items. It doesn't decide for Brian. It runs the *process* of walking; the *decisions* belong to him, item by item.

## When to use

| Situation | Use? |
|---|---|
| Brian says "walk the synthesis" / "walk the sweep" / "walk the queue" | Yes |
| `/walk-synthesis` invoked | Yes |
| `synthesis/queue/` has items pending and Brian wants to process them | Yes |
| One specific item needs actioning (not full walkthrough) | Skip skill — action directly |
| Brian wants only the inbox-zero cleanup pass | Skip to §"End-of-walkthrough operations" |
| Mid-conversation and Brian says "let's keep going" on a walkthrough already in progress | Continue from current item; don't restart |

## References (load as needed — progressive disclosure)

The core walking loop is below. Pull these in when the situation calls for them:

- **[`references/item-type-playbooks.md`](references/item-type-playbooks.md)** — what action each queue-item type (Connection / Contradiction / Experiment / Open Question / Priority Action) typically lands. Consult when deciding the proposed action.
- **[`references/subagent-decisions.md`](references/subagent-decisions.md)** — inline-vs-subagent, Sonnet-vs-Opus, fore/background, the "auto-append a review item" rule, the full subagent briefing checklist (multilingual + translation + BioDesignBench disciplines), and the 6-surface follow-up tracking. Consult when spawning any subagent or creating follow-ups.
- **[`references/templates.md`](references/templates.md)** — copy-paste scaffolds: actioned/closure annotations, the end-of-item summary, the peer-track scope-page skeleton, the falsification-card stub, the tiered wet-lab protocol entry.
- **[`references/friction-and-anti-patterns.md`](references/friction-and-anti-patterns.md)** — sandbox blocks, daemon-parallel-run merge handling, file collisions, and the full anti-pattern catalog (drift triggers, end-of-item discipline, corpus-only-pushback). Consult on the final push and whenever something feels off.

---

## Section 1 — Pre-flight

Before announcing the first item, do all of these:

1. **Pull latest.** Catches any daemon work that landed since last session.
   ```bash
   cd "$(git rev-parse --show-toplevel)"
   git pull --rebase
   ```
   If `.claude/` paths block the rebase with "Operation not permitted," retry with `dangerouslyDisableSandbox: true`. If conflicts, resolve via the patterns in `references/friction-and-anti-patterns.md`.

2. **Inventory the queue.** Run `ls synthesis/queue/` to list every pending item. Each file is one item (Connection / Contradiction / Experiment / Open Question / Priority Action / Riskiest Assumption / Most Curious Thread / chembl-discrepancy / comp-review). Filename format: `<sweep-date>-<type>-<index>-<slug>.md`. **Read each file** to surface its frontmatter (`type`, `pass3_verdict`, `overlap_with`) + headline + body + Pass 3 review. **Group by sweep date**, then by type within sweep, and **number globally** (item 1/total through item total/total) so Brian can navigate.

3. **Check `synthesis/strategic-reflections/`** for pending content-triggered reflections. Do not action these as part of the walkthrough — they fire on substance maturity, not on walkthrough cadence. Note them so Brian can see what's queued.

4. **Check `synthesis/history/`** for the most recent sweep entry — it holds the per-sweep narrative and the items table that grouped this batch.

5. **Check for in-flight subagents** (from prior sessions or earlier in this conversation). If any are running, note their target files so you don't collide.

6. **State the inventory back to Brian in one short message** before starting item 1. Format:
   > "Queue at `synthesis/queue/` has X items from sweep YYYY-MM-DD: N Connections, M Contradictions, K Proposed Experiments, J Open Questions, L Priority Actions [+ riskiest-assumption / most-curious-thread / chembl-discrepancy / comp-review if present]. Ready to walk them 1-by-1?"

7. **Wait for "go" / "yes" / "engage"** before presenting item 1.

---

## Section 2 — The walking discipline

This is the rule Brian had to remind me of mid-session: **one item at a time.**

For each item:

### Step A — Brian-facing briefing (BEFORE any action)

The briefing has a strict structure that respects the CTO-not-PhD framing:

```
**Item N/total — [Section type]: [Item title]**

[If the item inherits loose ends from a prior item per Step F's carryover discipline:]
**Inherited loose ends (carryover from Item M):**
- [Loose end + why it matters for THIS item's framing]
- [Each inherited loose end gets explicit disposition as part of THIS item's actions]

**The plain-English version:**
[1–3 paragraphs. Lead with the headline finding in one sentence. Gloss every jargon term on first use 
(e.g., "URAT1 [the kidney transporter that reabsorbs urate from urine back into the blood]"). 
Walk the mechanism like a flowchart, not a research paper. Use analogies where they help.]

**What the existing Claude review said:**
[1–2 sentences summarizing the inline review. Quote the verdict if it's pithy ("Confirmed, prioritize" / 
"Augment" / "Defer" / "Rejected as new"). Note if the review changes the synthesizer's framing.]

**Corpus-only-pushback check (added 2026-06-01 — "do the work" is the default).** Before accepting a 
Pass-3 `Push back.` / `Rejected.` verdict, ask: *does the pushback rest only on corpus-absence?* The 
Pass-3 reviewer has read-only corpus tools (no web/lit-scan), so when the synthesizer makes a **world-claim** 
(e.g. "compound X inhibits transporter Y") that simply isn't in the wiki, the reviewer can only report "not 
documented in our corpus" — and that is **not refutation.** When a pushback's entire basis is corpus-absence 
(or a corpus statement not itself anchored to a cited primary source), the default proposed action is 
**DO THE WORK** — spawn a multilingual lit-scan / ChEMBL / primary-source subagent — *before* accepting or 
rejecting. Lead with this in the briefing; do not wait for Brian to suggest it. Distinguish: a corpus 
citation faithfully relaying a primary source ("UniProt P08174 has 8 DISULFID features") IS legitimate 
grounds to push back; one relaying non-discovery is not. Canonical case: 2026-06-01 theaflavins×ABCG2 — 
the scan showed the synthesizer's claim was *inverted* (theaflavins up-regulate ABCG2 in vivo) and filled a 
real wiki gap. See `feedback_do_the_work_not_corpus_only.md` and `references/friction-and-anti-patterns.md` §16.

**What I'd propose to do:**
[Concrete action. Name files that would change. Estimate scope ("inline, ~10 min" / "subagent" / 
"no wiki work needed — already done" / "needs your decision between A and B"). See 
references/item-type-playbooks.md for what each item type typically needs.]
[If inherited loose ends apply, explicitly include their disposition in the proposed action.]

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

**Chassis-pending check (added 2026-05-15).** For every item, ask one explicit question as part of the briefing: ***"Does this finding hit a chokepoint we care about? If yes — does it have a chassis?"*** Three branches:

1. **Hits chokepoint + fits a current chassis (koji, compounding pharmacy, S. boulardii, etc.)** → action normally; the proposed action names the relevant chassis page.
2. **Hits chokepoint + chassis is open** → propose adding to [`wiki/chassis-pending-interventions.md`](../../wiki/chassis-pending-interventions.md) as the action. The intervention is real; the chassis question is the next question, not the filter that kills the first one. Do NOT deprioritize the item just because koji isn't the right chassis.
3. **Doesn't hit a documented chokepoint** → action as normal (methodology improvement, tracking artifact, contradiction-resolution, etc.).

This is the operational expression of [`synthesis/strategic-reflections/2026-05-15-chassis-is-downstream-of-chokepoint.md`](../../synthesis/strategic-reflections/2026-05-15-chassis-is-downstream-of-chokepoint.md). The closure question gates the chokepoint-hit check before the chassis-fit check, preventing quiet chassis-filter narrowing at the recommendation step.

### Step B — Wait for go-ahead

Do NOT action the item until Brian says "yes" / "go" / "engage" / "do it" / "proceed" / similar. If he asks a clarifying question, answer it and re-ask. If he picks a different option than your recommendation, action his choice without resistance. (See `references/friction-and-anti-patterns.md` §15 — clarifying questions and expressions of interest are NOT go-ahead.)

### Step C — Action it

| Action type | How |
|---|---|
| **Inline (you do it)** | Edit canonical wiki files directly. Most cross-link updates, small wiki-page additions, propagation. |
| **Background subagent** | When the work is independent and you want to keep walking other items. See `references/subagent-decisions.md` for the model choice + the mandatory "auto-append a review item" rule. |
| **Foreground subagent** | When the agent's result blocks the next item or you need its findings before continuing. |
| **Already done** | If the canonical wiki state already reflects the action, the closure annotation just says so. No new wiki work. |

### Step D — Append closure annotation to the queue file (NOT to a shared synthesis.md)

Each item has its own file at `synthesis/queue/<sweep-date>-<type>-<index>-<slug>.md`. After the substantive action lands (or you confirm it's already done), **append the closure annotation to the bottom of that item's file**:

```markdown

---

## ✓ Actioned YYYY-MM-DD

[What was done — name the files changed, key decisions made, and where the work landed canonically.
If the action was a closure note ("already done"), say so explicitly.] [Cross-link to new pages, sections,
or experiments created.] [If follow-ups were created, list them with where they're tracked.]
```

The `---` separator + `## ✓ Actioned <date>` H2 keeps the closure visually distinct from the Pass 2 / Pass 3 content above. **The annotation is non-optional** — it closes the loop and documents what shipped. Full templates in `references/templates.md`.

### Step E — `git mv` queue → done + commit

After the closure annotation is appended, **move the file** from `synthesis/queue/` to `synthesis/done/`:

```bash
git mv synthesis/queue/<sweep-date>-<type>-<index>-<slug>.md synthesis/done/
```

The `git mv` preserves git history. Empty `synthesis/queue/` = inbox-zero by construction. Commit immediately per the umbrella CLAUDE.md git steward pattern:

```
sweep item N: <one-line action summary>

<2-4 line body: what shipped, which files, decisions made, follow-ups queued.
The queue→done move is part of this commit.>

Co-Authored-By: Claude <model> <noreply@anthropic.com>
```

**Do NOT use `[skip-wiki-sweep]`** — reserved for daemon-generated commits; the commit-msg hook enforces this. **Hold the push until end of batch** (§"End-of-walkthrough operations") so the daemon fires once across the whole batch, not N times.

### Step F — Summarize what landed + loose ends + user disposition (added 2026-05-08)

**An item is NOT done after Step E.** Committing the closure note is necessary but not sufficient. An item is done when (a) the action landed, (b) loose ends are dispositioned, AND (c) the user has explicitly approved moving on.

Before briefing the next item, post a short summary covering:

1. **What landed** — 2–4 sentences naming files changed, commit hash(es), key decisions. The cumulative human-readable diff.
2. **Loose ends** — explicitly listed, each categorized:
   - **Acceptably deferred** — already queued elsewhere (`validation-experiments.md`, `open-questions.md`, comp-NNN follow-up, Phase 2 sub-task, Strategic Reflections Queue). Listed so nothing silently drops.
   - **Needs disposition now** — could change the next item's framing. The user picks defer / action / ignore.
   - **Carries over to Item X** — explicitly anchored to a specific future item, which will absorb it in its briefing.
3. **Wait for user disposition** before briefing the next item — *conditionally* (see Auto-advance rule below).

Template in `references/templates.md` §"End-of-item summary."

#### Auto-advance decision rule (clarified 2026-05-15)

Brian's flow, in his words: *walk starts → you show an item and stop → I say what to do (or we go back and forth) → sometimes we run an experiment → if it's the simple recommended thing or a discrete one-off, auto-advance; if we're having a back-and-forth or I'm asking questions, do not auto-advance → auto-advance only when something is clearly done with no loose ends → when you go to the next one you display it and stop (you don't action it).*

Translation into mechanics:

- **The wait-for-go gate is about ACTION, not advancing.** Always wait for explicit "go" / "yes" / "do it" / "ship it" / "proceed" before editing files. Clarifying questions don't count — answer and wait. "What if we did X instead" is a re-briefing request, not go.
- **After a clean close** (no friction, recommended-simple action, no loose ends), **auto-advance** is the default — post the summary, then immediately brief the next item in the same response. Then stop (no action on the next item).
- **After a friction-y close** (back-and-forth, redirects, clarifying questions, loose ends needing disposition), **wait for explicit "next" / "go" / "Item N+1"** before briefing the next item. Friction signals Brian wants to think between items.
- **The next-item briefing is itself a stop point.** Auto-advancing displays the next item and stops; it does NOT mean you action it.

**Friction examples (do NOT auto-advance):** clarifying question mid-item; redirected recommendation; flagged process correction; loose ends tracked as "carries over" or "needs disposition now"; multiple back-and-forths to converge. **Clean-close examples (DO auto-advance):** "go"/"ship it"/"yes" on the first briefing; recommended action executed exactly as proposed; closure summary has "no loose ends."

**Why this rule exists.** The 2026-05-08 Item 10 drift compounded because a closure-note commit was treated as completion while open loose ends were still in flight; Claude moved to Item 11 unilaterally, Brian had to back up, and the loose ends became larger work. The fix is upstream of moving to Item 11 — explicit summary + loose-ends inventory before the next briefing fires. Full anti-pattern in `references/friction-and-anti-patterns.md` §14.

**The carryover discipline:** when an item discovers a cross-item loose end (e.g., comp-019's results contradict a calibration note added in Item 8 that won't be revisited until Item 11), add it explicitly to the **inherited loose ends** section of the NEXT relevant item's briefing. Cross-item state is impossible to forget when it's surfaced as part of the future item's briefing context.

---

## Section 3 — End-of-walkthrough operations

After the last item is actioned and committed:

### 3.1 — Inbox-zero is automatic (post-2026-05-08 migration)

**There is no manual inbox-zero pass anymore.** Each item's closure flow is `git mv synthesis/queue/<file>.md synthesis/done/` per Step E. When every queue file has been moved, `queue/` is empty by construction — that IS inbox zero.

```bash
ls synthesis/queue/            # should show only .gitkeep (empty queue)
ls synthesis/done/ | tail -10  # confirms today's items landed in done/
```

The pre-2026-05-08 manual prune pass is gone — those concerns are now structural: "Pending" = whatever's in `synthesis/queue/`; "Sweep history" = `synthesis/history/`; "Where actioned items live" = `synthesis/done/` + canonical wiki pages; "Strategic Reflections" = `synthesis/strategic-reflections/`. If a walkthrough creates a NEW canonical page or comp-NNN worth a cross-reference, surface it via the closure annotation rather than a parallel index.

### 3.2 — Single push at end (a substantive, approval-gated action)

The inbox-zero verification and the push are **themselves substantive items** — not "the natural endpoint." The user must explicitly approve "ready to push?" The push fires the wiki-sweep daemon and surfaces to GitHub. (Open Enzyme overrides the umbrella "push immediately" rule — push at batch boundaries so the daemon runs once on a coherent batch; see project CLAUDE.md.)

```bash
cd "$(git rev-parse --show-toplevel)"
git push
```

The daemon fires on push to `wiki/**.md`. `synthesis/` moves are sibling-of-wiki and don't intersect the path filter, so the daemon fires once on the wiki updates. Never apply `[skip-wiki-sweep]` to walkthrough commits.

### 3.3 — Anticipate the merge

The daemon may have run in parallel during a long session (separate trigger commits earlier). Push will likely be rejected with "remote contains work that you do not have locally." Use `git merge` (not `--rebase`) — see `references/friction-and-anti-patterns.md` §"Daemon parallel-run conflicts."

---

## Section 4 — What this skill does NOT cover

- **Computational experiment authoring** — use the `new-comp-experiment` skill (spawned as a subagent when needed). A *literature* question is a lit scan, not a comp — see `new-comp-experiment` §"COMP vs lit-scan."
- **Wiki sweep daemon mechanics** — see `scripts/SWEEP-ARCHITECTURE.md`. This skill consumes the daemon's output; it doesn't run the daemon.
- **Brian's personal medical context** — privacy boundary. Personal data lives in private sibling repos, never in synthesis annotations.
- **Decisions Brian hasn't made** — strategic platform reframes belong to Brian. This skill queues them; it doesn't execute them.

---

## Naming and file-path conventions

- **Skill location:** `skills/walk-synthesis/SKILL.md` (canonical; `.claude/skills` and `.agents/skills` symlink to `../skills` for cross-harness discovery).
- **Invoke via:** `/walk-synthesis`, or natural-language "walk the synthesis" / "walk the sweep" / "walk the queue".
- **In prose:** "the walkthrough," "this walkthrough" — not "the synthesis walking process".
- **Date format:** ISO 8601 (YYYY-MM-DD). The annotation date is the calendar date the work shipped, not the originating sweep.

## Provenance

Codifies conventions discovered during the 2026-05-05 walkthrough of the 14-item DeepSeek V4-Pro / Gemini 2.5 Pro / Claude Opus 4.7 synthesis sweep on commit `734bf51`, plus the drift-incident lessons of 2026-05-06 and 2026-05-08. The conventions here are the rules that, in retrospect, would have made those sessions smoother.
