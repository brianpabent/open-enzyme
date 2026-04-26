You are running **Pass 2** of the Open Enzyme sweep — full-corpus synthesis. Pass 1 propagation has already completed; the wiki state you're seeing reflects those edits. Your job is creative cross-document synthesis.

**Read `CLAUDE.md` first** for evidence-level standards and voice.

**Pass 2 only.** Read the full wiki corpus, find connections nobody has stated yet, and output a synthesis report. Do NOT modify any `wiki/*.md` file. Do NOT prepend to `wiki/synthesis.md` (Pass 3 — Claude review — will do that with critique annotations interleaved). Do NOT modify `index.md`, `wiki/GRAPH.md`, or `mkdocs.yml`.

---

## Output

A single markdown file at:

```
logs/v4-synthesis-<YYYY-MM-DD>-<sha-short>.md
```

The TRIGGER block tells you the date and commit SHA short form to use.

---

## What to look for

Cross-document connections that emerge only when you read multiple files together:

1. **Cross-domain synergies** — findings from one track that unlock opportunities in another (e.g., a koji secondary metabolite that hits an NLRP3 chokepoint nobody mapped to it)
2. **Contradictions or tensions** — two documents disagreeing on mechanism, strategy, or feasibility
3. **Unexploited combinations** — molecules, pathways, organisms that appear in multiple documents without anyone connecting them into a strategy
4. **New experiments** — especially cheap, fast ones that de-risk expensive downstream work
5. **Risk interactions** — risks that compound or cancel across tracks
6. **Blind spots** — questions nobody is asking that someone should
7. **Platform-level patterns** — observations that apply across multiple compounds/strains/chokepoints rather than to one

---

## Output format

**Critical**: end every numbered item (each Connection, Contradiction, Experiment, Open Question, Priority Action) with a `{{PEER-REVIEW}}` marker on its own line. Pass 3 (Claude review) substitutes each marker with a review blockquote via deterministic merge — your content is preserved verbatim.

```markdown
# Synthesis — <YYYY-MM-DD>
**Substrate:** Open Enzyme wiki at commit `<sha>`
**Trigger files:** <comma-separated list>
**Diff base:** <last sweep commit>
**Reviewer:** <model name from invocation>

## New Connections

1. **<one-sentence claim>.** *Supported* OR *Speculative*.
   - *Documents Connected:* `file-a.md`, `file-b.md`, `file-c.md`
   - *Why It Matters:* (3-6 sentences explaining the leverage)
   - *Suggested Action:* (concrete next step)

   {{PEER-REVIEW}}

2. **<claim>.** ...
   - ...

   {{PEER-REVIEW}}

## Contradictions Found

1. **<contradiction>.** Locations: ... Analysis: ...

   {{PEER-REVIEW}}

## Proposed Experiments (ranked by insight per cost)

1. **<experiment>.** Cost: $X. Time: Yw. Decides: ...

   {{PEER-REVIEW}}

## Open Questions

1. **<question>?** (context)

   {{PEER-REVIEW}}

## Priority Actions

1. **<action>** (1-2 lines on what + why)

   {{PEER-REVIEW}}
```

### Marker discipline

- One `{{PEER-REVIEW}}` per numbered item. Not at section headers, not at sub-bullets.
- Place on its own line, separated from the item content above by a blank line.
- The marker text is exactly `{{PEER-REVIEW}}` (case-sensitive, double curly braces, no spaces inside).
- If you produce a "no new synthesis" no-op output (drift guard), you do not need any markers — the no-op block has nothing to review.

---

## Drift guard

If after reading the corpus you find no genuinely new connections — e.g., the trigger was a typo fix, or the synthesis would just restate what's already in the most-recent block of `wiki/synthesis.md` — output a brief note saying so and exit.

```markdown
# Synthesis — <YYYY-MM-DD>
**Status:** No new synthesis. <one-sentence reason>.
```

Better to skip than to pollute the queue with low-signal entries. Pass 3 reviewer will see the no-op and prepend a corresponding short entry to `wiki/synthesis.md`.

---

## Tone

PhD audience. Bold proposals, clearly labeled. Distinguish **Supported** (multiple sources align) from **Speculative** (reasonable but unvalidated). This is a brainstorm for human review — ideas, not decisions. Synthesis findings do NOT auto-propagate into wiki pages; humans promote them manually after seeing Pass 3 reviewer's critique.

Watch for:

- **Species-gap translation** caveats (rodent IC50 ≠ human IC50 — see the dapansutrile lesson in `wiki/chembl-cross-check.md`)
- **Chokepoint structure** per `wiki/nlrp3-exploit-map.md` v1.2 — CP0/CP1a/CP1b/CP2/CP3/CP4/CP5a/CP5b/CP6a/CP6b
- **Evidence tier discipline** — Clinical Trial / Animal Model / In Vitro / Mechanistic Extrapolation
- **Honest gaps** — flag what the platform does NOT cover (e.g., the CP0 fermentable-coverage gap)

---

## Commit

Commit the new log file with this message format:

```
sweep-2-synthesize: <reviewer-model> raw synthesis → logs/v4-synthesis-<date>-<sha>.md [skip-wiki-sweep]
```

The `[skip-wiki-sweep]` marker prevents your commit from retriggering the workflow. **Do NOT use `[skip ci]`** — that blocks deploy-docs too.

If you produced a no-synthesis output (drift guard triggered), still commit the short note. Pass 3 needs to see something.

---

## Constraints

- **Never write to:** any `wiki/*.md` file (including `synthesis.md`), `index.md`, `wiki/GRAPH.md`, `mkdocs.yml`, `reference/*`, `*.html`, `CLAUDE.md`, `README.md`, `scripts/*`.
- **Only output:** `logs/v4-synthesis-<date>-<sha>.md`.
- **Evidence-level tags** on every claim.
- **Inline provenance** — PMID or `(source: <wiki-filename>)`.
- **No verdict on V4-vs-Claude.** That's Pass 3's role. Just produce your synthesis cleanly.
