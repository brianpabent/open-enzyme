You are running **Pass 3** of the Open Enzyme sweep — peer review. The synthesizer model (V4-Pro by default, but the architecture is model-agnostic) just produced a synthesis at `logs/v4-synthesis-<date>-<sha>.md`. Your job: read it, critique it inline, and prepend the annotated version to `wiki/synthesis.md`.

**Read `CLAUDE.md` first** for evidence-level standards and voice.

**Pass 3 only.** Review V4's synthesis output. Do NOT modify any other wiki page. Do NOT add net-new findings that V4 didn't surface (if you spot one, flag it in a `> **Claude review — Defer:**` block under the most relevant V4 item). Do NOT log to `logs/sweep-log.md`.

---

## Inputs

- The TRIGGER block names the V4 synthesis log file: `logs/v4-synthesis-<date>-<sha>.md`. Read it.
- You may also read any `wiki/*.md` page V4 cited, to verify claims against primary sources.
- You may read prior `wiki/synthesis.md` entries (top of file) to ensure your review doesn't restate what's already known.

---

## Output

Prepend a single section to `wiki/synthesis.md`, immediately after the YAML frontmatter and the `# Synthesis Pass 2: ...` H1 title. **Do NOT modify or delete any existing content** in synthesis.md — strictly prepend.

The section is V4's synthesis content with **Claude review blockquotes inline per item**. Each numbered Connection, each Contradiction, each Experiment, each Open Question, each Priority Action gets a blockquote review block underneath it.

### Output format

```markdown
## Sweep — <YYYY-MM-DD> (V4 synthesis + Claude review)

**Synthesis log:** [logs/v4-synthesis-<date>-<sha>.md](../logs/v4-synthesis-<date>-<sha>.md)
**Substrate:** Open Enzyme wiki at commit `<sha>`
**Trigger files:** <comma-separated>
**Synthesizer:** <model from log frontmatter>
**Reviewer:** Claude Sonnet/Opus 4.x

---

### New Connections

1. **<V4's claim>.** *<V4's Supported/Speculative tag>.*
   - *Documents Connected:* <V4 content, verbatim>
   - *Why It Matters:* <V4 content, verbatim>
   - *Suggested Action:* <V4 content, verbatim>

   > **Claude review — <verdict>.** <reasoning, 2-5 sentences, with citations or push-back>

2. ...

### Contradictions Found

(V4 content + review blockquote per item)

### Proposed Experiments (ranked by insight per cost)

(V4 content + review blockquote per item)

### Open Questions

(V4 content + review blockquote per item)

### Priority Actions

(V4 content + review blockquote per item)
```

If V4's synthesis was a "no new synthesis" no-op, prepend a short notice instead:

```markdown
## Sweep — <YYYY-MM-DD> (no new synthesis)

**Synthesis log:** [logs/v4-synthesis-<date>-<sha>.md](../logs/v4-synthesis-<date>-<sha>.md)
**Status:** Synthesizer produced no new connections worth promoting. <one-sentence rationale from V4>. No review needed.
```

---

## Verdict vocabulary

Each Claude review blockquote opens with one of these verdicts in bold:

- **Confirmed.** V4's claim survives scrutiny. May add stronger evidence or sharpen the framing.
- **Confirmed, prioritize.** Agree, AND this should be elevated (e.g., Open Question → Priority Action).
- **Partial.** Agree on X, push back on Y. Specify both.
- **Push back.** Disagree on a substantive point. Cite contradicting evidence.
- **Rejected.** Claim doesn't survive scrutiny. Cite why.
- **Augment.** Agree + here's a useful addition or sharpening.
- **Defer.** Interesting but can't evaluate without specific reference Claude doesn't have access to. Or: V4 didn't surface this and it's worth a future sweep — flag here for the queue.

Each verdict implies an action (or non-action):

- `Confirmed, prioritize` signals to the human reader the item should rank higher in the queue
- `Push back` signals it should drop or be re-examined before action
- `Rejected` signals removal from the action queue
- `Defer` signals "human follow-up needed" — Brian should look at this manually

---

## Strict scope

**Critique only. Do NOT:**

- Add net-new Connections / Contradictions / Experiments / Open Questions that V4 didn't surface (those come from the next sweep cycle, where Claude does Pass 1 and V4 does Pass 2 again)
- Edit V4's content or rephrase V4's claims (V4's words are immutable in the merged output — your role is annotation)
- Modify earlier `wiki/synthesis.md` entries
- Write to any wiki page other than `synthesis.md`
- Modify `index.md`, `wiki/GRAPH.md`, `mkdocs.yml`

**You MAY:**

- Read `wiki/*.md` files V4 cited, to verify
- Read `logs/sweep-log.md` and prior synthesis entries for context
- Read `wiki/chembl-cross-check.md` to verify any IC50/bioactivity claim V4 made
- Read `wiki/hypotheses/*.md` if V4 referenced a committed hypothesis

---

## Tone

PhD audience. Specific. Cite primary sources where you push back. State your reasoning, don't just label.

A weak review:
> **Claude review — Confirmed.** Looks good.

A strong review:
> **Claude review — Confirmed.** Mechanism well-established (Habuchi 2003 PMID 14613816, Takiue 2011 PMID 21262960 — both primate renal physiology). The claim that this caps maximum effect of luminal uricase follows from the gut-lumen-sink ABCG2 dependence in `wiki/gut-lumen-sink.md`. One refinement: V4 says "regardless of dose" — strictly, you can compensate at very high enzyme doses, but the dose-response curve flattens (sigmoid ceiling). Practically, the conclusion holds.

A strong push-back:
> **Claude review — Push back.** V4 cites `lactoferrin.md` for the CP1b iron→ROS mechanism, but `wiki/lactoferrin.md` §3.2 explicitly flags that as Mechanistic Extrapolation, not Supported. The wiki's CP1b is specifically C5a→ROS (per `wiki/nlrp3-exploit-map.md` line 102), not iron→ROS. V4 conflated two different ROS-priming mechanisms. The connection is plausible but mis-labeled.

---

## Commit

When the prepend is complete, commit `wiki/synthesis.md` with this message format:

```
sweep-3-review: Claude review of <model> synthesis → wiki/synthesis.md [skip-wiki-sweep]
```

The `[skip-wiki-sweep]` marker is required. **Do NOT use `[skip ci]`** — that blocks deploy-docs.

If V4 produced a no-op (no new synthesis), still prepend the short notice and commit. The audit trail matters even when the substantive content is null.

---

## Global constraints

- **Never write to:** any wiki page other than `synthesis.md`. No exceptions.
- **Evidence-level tags** on every claim you assert in your reviews.
- **No marketing language.** PhD audience.
- **Cite primary sources** for push-back verdicts. Don't push back on vibes.
- **Strict-scope discipline.** If you find yourself wanting to add a new Connection that V4 missed, write it as a `Defer` note inside the closest existing item — don't add a top-level new entry.
