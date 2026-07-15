# Subagent decisions + multi-surface follow-up tracking

## When to spawn a subagent vs. action inline

| Work type | Action |
|---|---|
| Cross-link updates across 2–6 files | Inline |
| Annotation in `synthesis/queue/` | Inline |
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
| **Background** | Work is genuinely independent. Example: launching subagents in parallel during a walkthrough so you can keep walking other items while they work. |

## Background subagents during a walkthrough — the "auto-append a review item" rule

**Load-bearing rule (added 2026-05-06 after the walkthrough-drift incident).** When you launch a background subagent during a walkthrough whose output will need user review or actioning when it returns:

1. **Launch the subagent normally.** Brief it per the rules below.
2. **Immediately after launching, create a NEW task entry** representing the future review step: `"Item N+X — Review subagent results: <one-line description>"`, referencing the subagent ID.
3. **Append it to the END of the walkthrough queue** (higher item number than the current highest). The total-item count goes up by 1 per background subagent launched.
4. **When the completion notification arrives, DO NOT process it immediately.** Mark the review-task "ready for review" and **continue the current item.** Subagent completion is not a drift trigger.
5. **When the walkthrough naturally reaches the review-task**, present the findings as that item's briefing. Wait for explicit go-ahead. Annotate + commit per the standard step pattern.

**Why:** during the 2026-05-06 walkthrough, three background subagents returned asynchronously; each completion was treated as "process now," which compounded into momentum that carried past Items 16–21 + cleanup + inbox-zero + push, all without per-item approval. Subagent completion is *information*, not authorization.

**Edge case:** when the subagent IS the canonical work for an existing walkthrough item, no new review item is needed — its completion fulfills the item. The rule applies when the subagent's output is *additional to* the current item's scope.

**Auto mode interaction.** Claude Code "Auto Mode" reminders ("execute autonomously, minimize interruptions") do NOT override this skill's per-item discipline. Walkthroughs are explicitly per-item-checkpointed; that supersedes auto mode for the duration of the `/walk-synthesis` invocation. If they conflict, this skill wins.

## Subagent briefing rules

Subagents have NO conversation context. The prompt must be self-contained — brief them like a smart colleague who just walked into the room. Include:

1. **What you're trying to accomplish and why** (the platform-level goal, not just the immediate task).
2. **What you've already learned or ruled out** (so they don't re-do the work).
3. **Files they CAN touch** vs. **files to avoid** (if other agents are in flight, name them).
4. **Constraints** (style, length, evidence-level conventions, any "don't" rules from project CLAUDE.md).
5. **What they should report back** (length cap, structure).
6. **Memory cautions** if relevant (e.g., "Paperclip MCP `map` operator hallucinates — use `search` / `cat` / `grep`" per `feedback_paperclip_map_unreliable.md`).
7. **Global-multilingual default** for any lit-scan/research task. Per `CLAUDE.md` §"Global-multilingual research by default," explicitly include non-English sources: ChiCTR, CNKI / WanFang (Chinese), J-STAGE / CiNii (Japanese), KISS / RISS (Korean), eLIBRARY.RU (Russian), TIB (German), SciELO (Spanish/Portuguese). **MANDATE `local_curl_fetch()` (from `wiki/etc/experiments/lib/agentic_lit_synthesis.py`) for East-Asian sources — non-optional.** CNKI / WanFang / ChiCTR / CQVIP / ChinaXiv / Baidu Scholar are JS-gated and bot-block hosted/browser fetch; `local_curl_fetch()` reaches them via the firewall-whitelisted local `curl` binary. A brief that merely "references the library" is insufficient — subagents fall back to hosted fetch, hit the bot-wall, and mislabel it a "language barrier" (canonical miss: the 2026-07-13 chronic-tophus scan). Name the function; forbid the hosted-fetch fallback.
8. **Translation cross-check protocol** when the subagent ingests non-English source material producing load-bearing claims (evidence tiers, dosing, mechanism). Per `CLAUDE.md` §"Translation protocol": translate with two independent models (one Western-vendor, one Chinese-vendor for Chinese sources); surface disagreements as inline annotations rather than silently picking one. High-risk categories: scientific hedging language, dosing units, classical-TCM terminology, statistical-significance language. (~$0.05/paper.)
9. **Deep multi-metric evaluation discipline** (BioDesignBench, Kim & Romero 2026 — see `wiki/bio-ai-tools.md`). For any comp-NNN authoring / hypothesis-ranking / candidate-evaluation subagent: require **(a) multiple candidates** (not single-shot), **(b) ≥3 orthogonal metric categories** (not single-axis), **(c) head-to-head comparison + filtering before termination** (not first-candidate-wins). The deficit is behavioral and specifically remediable via the brief. The N-of-M concordance pattern (`wiki/autonomous-screening-methodology.md` §5) is the canonical instance.

## File-collision management

When multiple subagents are in flight, brief each on what files OTHER agents are touching. Common collision points:

- `wiki/computational-experiments.md` (any comp-NNN agent edits this)
- `wiki/modality-chokepoint-matrix.md` (peer-track scope-page agents edit per-modality sections)
- `synthesis/queue/` (any agent can add an actioned annotation)
- `wiki/validation-experiments.md` (experiment-creating agents add §X.Y entries)
- `wiki/etc/experiments/lib/protease_stability.py` (locked — orchestrators import only, never modify)

If two agents will touch the same file, sequence them or have only one do the shared-file edits as carry-along.

## Multi-surface follow-up tracking (the "how do we remember" answer)

When an item creates a new exploration vector, peer-track scope page, or set of follow-ups that won't fire today, **bake the tracking across 6 redundant surfaces** so it survives the next sweep.

| Surface | What goes there |
|---|---|
| 1. The new page's own "Open Follow-Ups" section | Phase 2 items as a numbered list with status (Queued / In progress / Done) |
| 2. `wiki/open-questions.md` topical entry | A new section under the right topic heading, mirroring the Phase 2 list |
| 3. `wiki/computational-experiments.md` Planned Analyses table | Any comp-NNN follow-ups (with "Informs" pointing to the new page) |
| 4. `wiki/hypotheses/HNN-<thesis>.md` falsification card stub | Forces "what would kill this thesis" framing; full population queued as a Phase 2 item |
| 5. `index.md` cheapest-experiments table | The 1–2 highest-leverage Phase 2 items (the daemon-fires-on-push surface that catches Brian's eye most often) |
| 6. `synthesis/queue/` actioned annotation + Strategic Reflections Queue | The annotation closes the item; the Reflections Queue holds content-triggered platform reframes |

**Phase taxonomy:**
- **Phase 1:** what we do now in this session
- **Phase 2:** queued in-silico follow-ups, no pharma-partner dependency, subagent-executable in future sessions
- **Phase 3:** content-triggered reflections — fire when accumulated substance crosses a maturity threshold (not calendar-triggered). Belong in `synthesis/strategic-reflections/` so the daemon surfaces them on every sweep.
