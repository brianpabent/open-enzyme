# Friction points + anti-patterns

## Anticipated friction points

### `.claude/` sandbox blocks
Symptom: `git pull --rebase` (or any git op touching `.claude/settings.json`, or the `.claude/skills → ../skills` symlink) fails with "Operation not permitted" / "could not detach HEAD."
Fix: retry the same git command with `dangerouslyDisableSandbox: true`. Do not chmod or delete the `.claude` paths.

### Daemon parallel-run conflicts on final push
Symptom: `git push` rejected; `git pull` reveals 2–4 new daemon-generated commits on `origin/main` (sweep-1-propagate, sweep-2-synthesize, sweep-3-review, sometimes sweep-4-deepseek) plus a new `logs/` file.

**Use `git merge`, not `git pull --rebase`,** for the final integration. `--rebase` replays each of your N commits individually, hitting the same conflict (especially section-number collisions) on every commit that touches the same file; a merge resolves the conflict ONCE.

```bash
git merge origin/main --no-edit  # may exit with conflicts
```

Common conflict patterns:
- **`synthesis/queue/`:** daemon's fresh sweep block usually duplicates content you already actioned. Take ours (the inbox-zero version). Note in a sweep-history row that the daemon's sweep was substantively duplicate.
- **`wiki/validation-experiments.md`:** section-number collision (most common). Daemon assigned §1.X to its experiment; you assigned §1.X to a different one. Keep yours; renumber daemon's to §1.X+N (whichever has fewer cross-refs). Update all cross-refs (`grep -rn "§1\.X" --include="*.md"`).
- **`index.md`:** keep both sides; update any cross-refs whose section number changed.

After resolution: `git add` the resolved files, `git commit --no-edit -m "<descriptive merge message>"`, then `git push`.

### Subagent file collisions
Symptom: a background agent edits a file you also need; their edits land first; your Edit call fails with "File has been modified since read."
Fix: re-read the file before editing. The Edit tool requires the most recent file state in context.

### Untracked files missed by `git commit -am`
Symptom: `git commit -am` succeeds but a new file created earlier is still untracked.
Fix: `git add <file>` explicitly. The `-a` flag only stages already-tracked files. Follow up with a commit named `add: <files>` (NOT `--amend`).

### Brian's CTO-not-PhD reminder
Symptom: Brian says some variant of "I'm not a PhD" / "what does X mean" / "I can't read papers."
Fix: re-anchor on the CTO-not-PhD framing (SKILL.md §Step A). Don't apologize at length — rewrite the briefing in plain English and continue. The rule is in `memory/user_role.md`.

---

## Anti-patterns (things that went wrong in the 2026-05-05 → 2026-05-08 walkthroughs)

1. **Don't action multiple items without explaining each one first.** Brian's mid-session correction 2026-05-05: "but there's more that you did without me!" Single-item discipline is non-negotiable.
2. **Don't dump raw papers — translate.** The lit-scan output that worked best was the plain-English Q&A briefing, not the citation block.
3. **Don't add `[skip-wiki-sweep]` to user-content commits.** The commit-msg hook rejects it; the marker is reserved for daemon commits only.
4. **Don't use `git commit -am` when there are untracked new files.** The `-a` flag misses them — stage explicitly.
5. **Don't pick numbered section IDs (§1.X) without checking remote.** The daemon may have run in parallel and added §1.X to validation-experiments.md while you worked. If walking spans hours, `git fetch` before assigning numbers.
6. **Don't `git pull --rebase` for the final integration when many commits touch the same file.** Use `git merge` so the conflict resolves once, not N times.
7. **Don't lose follow-ups.** When an item creates Phase 2 / Phase 3 work, bake tracking across the 6 redundant surfaces (`subagent-decisions.md` §"Multi-surface follow-up tracking"). Single-surface tracking evaporates by the next sweep.
8. **Don't action heavyweight items without Brian's go-ahead** — even if the action looks obvious. "Wait for go" supersedes any automation impulse.

### Drift-trigger anti-patterns (added 2026-05-06)

9. **Don't treat subagent completion as authorization for the next item.** A completion notification is *information*, not a green-light. Use the auto-appended review-task pattern (`subagent-decisions.md`): the subagent's output becomes a future walkthrough item that gets its own briefing + go-ahead. If you're thinking "the subagent finished, let me action its output and continue" — STOP.
10. **Don't treat cleanup or propagation work as continuation.** Cross-reference back-fills, stray-pattern grep cleanups, and "while we're here" propagations are themselves substantive items requiring approval — not "natural follow-on." Either (a) stop and brief the discovered cleanup as its own item, or (b) auto-append it for explicit approval at its turn. The 2026-05-06 drift compounded through cleanup that "felt obvious" but was never approved.
11. **The inbox-zero pass and the final push are themselves substantive items** — not "the natural endpoint." The user must explicitly approve "ready for inbox-zero?" and "ready to push?" Both are high-stakes: inbox-zero deletes large file swaths (irreversible without git surgery); the push fires the wiki-sweep daemon and surfaces to GitHub (visible to the world).
12. **Auto Mode does NOT override this skill.** Walkthroughs are per-item-checkpointed; the skill supersedes auto mode for the duration of the invocation. The 2026-05-06 failure: a periodic Auto-Mode reminder fired between Items 15 and 16 and was treated as overriding per-item discipline. It doesn't.
13. **The `.claude/hooks/block-push-without-approval.py` push hook is a backstop, not a license.** It blocks daemon-triggering pushes unless the user grants `CLAUDE_PUSH_AUTHORIZED=1`. "The hook will catch me if I drift" is not permission to drift — the hook fires when the discipline already failed.

### End-of-item discipline (added 2026-05-08)

14. **Don't treat "I committed the closure note" as "the item is done."** An item is done when (a) the action landed AND (b) loose ends are dispositioned. Step F (SKILL.md §Section 2) is the fix: end-of-item summary + loose-ends inventory. The 2026-05-08 Item 10 drift compounded because a closure-note commit was treated as completion while four open loose ends were still in flight; Brian had to back the conversation up, and the loose ends became much larger work. **Loose ends compound.** Three categories per loose end: acceptably deferred / needs disposition now / carries over to Item X. **When loose ends need disposition or carry over, do NOT auto-advance** — wait for Brian's explicit "next." Clean closes (no loose ends, recommended action shipped as proposed) can auto-advance per the Auto-advance rule in SKILL.md §Step F.
15. **Don't action without explicit go.** The wait-for-go discipline is about ACTION, not advancing. "Going to proceed unless you redirect" / "Proceeding with X" before Brian says go is opt-out actioning — wrong even when the content is right. Clarifying questions, expressions of interest ("sounds like a good idea"), and process discussion are NOT go-ahead. Only explicit "go" / "yes" / "do it" / "ship it" / "proceed" count. If Brian asks "are we drafting or implementing?" — answer, restate scope, re-ask.
16. **Don't accept a corpus-only pushback as refutation — do the work.** When a Pass-3 `Push back.` / `Rejected.` verdict rests *only* on "not in our corpus," that is not evidence the synthesizer's world-claim is wrong — it means we haven't discovered it (the reviewer has no lit-scan tools, only corpus grep). Default response: a primary-lit scan (multilingual), NOT closing the item on corpus-absence and NOT an open-question stub when a 5-minute scan would resolve it. Lead with the scan in the briefing. Canonical: 2026-06-01 theaflavins×ABCG2 — Pass-3 pushed back citing only corpus-absence; the scan showed the claim was *inverted* and filled a real wiki gap. See `memory/feedback_do_the_work_not_corpus_only.md`.
17. **Don't try to edit `wiki/synthesis.md` — it doesn't exist anymore.** Post-2026-05-08 migration, the action queue is `synthesis/queue/` (per-item files), history is `synthesis/history/`, reflections are `synthesis/strategic-reflections/`. New flow: `ls synthesis/queue/` to inventory; append closure annotation to the per-item file (Step D); `git mv` to `synthesis/done/` (Step E); inbox-zero is automatic. Migration spec: [`operations/specs/2026-05-08-synthesis-filesystem-migration.md`](../../../../operations/specs/2026-05-08-synthesis-filesystem-migration.md).
