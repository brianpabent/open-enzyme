You are running **Pass 2** of the Open Enzyme sweep — full-corpus synthesis. Pass 1 propagation has already completed; the wiki state you're seeing reflects those edits. Your job is creative cross-document synthesis.

<!-- The synthesizer here is intentionally a different vendor from the propagator (Pass 1) and the reviewer (Pass 3) — see `wiki/open-source-platform.md` §"Multi-model synthesis as guard against epistemic homogenization" for the rationale. Don't collapse the pipeline to a single vendor. -->

## Required pre-reading (do this BEFORE generating any synthesis)

1. **`CLAUDE.md`** — evidence-level standards and voice.
2. **`wiki/synthesis.md` bottom-of-file sections** — specifically:
   - **`## Sweep history`** table — what's been swept before, when, and which log file captures it.
   - **`## Where actioned items live now`** — the canonical homes (file + section paths) where prior-sweep findings have been baked into the wiki. **A connection that already lives at one of these named locations is not new — it has been actioned. Do not re-surface it as a fresh finding.**
   - **`## Strategic Reflections Queue`** if present — content-triggered reflections that are *intentionally* deferred. Don't try to "find" these as new connections; they're already queued.
3. **The most recent ~3 entries in the Sweep history table** — read the corresponding `logs/v4-synthesis-*.md` files. Items that appeared in those prior syntheses are candidates for the duplicate filter (Drift guard, below).

**Why this matters.** The wiki is updated by the sweep workflow itself. After Pass 3 commits review annotations, the human walkthrough actions findings into canonical pages (e.g., adding a new `§4.7 Substrate-Supply Synergy` section to `lactoferrin.md`). The next sweep fires; if you ignore the audit trail, you will re-derive those exact connections from the wiki content that now contains them. **The drift-guard test is whether the connection is already explicit in the wiki at any level — synthesis.md, the canonical pages named in "Where actioned items live now," OR a recent prior-sweep log.**

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

Cross-document connections that emerge only when you read multiple files together — **AND that are not already explicit in the wiki content itself.**

**The novelty bar:** would a knowledgeable reader who has read the cited canonical wiki pages see your proposed finding as new information, or as a restatement of what those pages already say? If it's a restatement, it's a duplicate — drop it. The threshold isn't "the wiki doesn't make this connection in a single sentence somewhere" — it's "no canonical wiki page treats this connection as a named section, callout, or first-class topic." Use the "Where actioned items live now" pointers (synthesis.md bottom) as your primary duplicate-check.

**Concrete duplicate-check examples** (these are not new findings; do NOT include them in your output):

- "Lactoferrin → ↓TNFα → ↑ABCG2 substrate supply for co-expressed uricase" — already a named section at `lactoferrin.md §4.7` and a rescue arm in `validation-experiments.md §1.14`.
- "Carnosine as precision countermeasure for androgen-driven URAT1 upregulation" — already at `koji-endgame-strain.md §2.5` and `validation-experiments.md §1.24`.
- "Native koji metabolite chorus (kojic acid + ergothioneine) as free CP1a/CP1b coverage" — already at `open-enzyme-vision.md §4`.
- "Supplement stack contains functional ABCG2 inhibitors (quercetin, EGCG, curcumin)" — already a tier-stratified callout at `abcg2-modulators.md §"The supplements-stack contradiction"` and `open-enzyme-vision.md §10`.
- "Shio-koji proteases destroy peptide payloads (carnosine, KPV)" — already at `engineered-koji-protocol.md §15`.
- "Ward 1995 dual-cassette feasibility = #1 priority gate" — already `validation-experiments.md §1.9` and falsification card `wiki/hypotheses/H01-ward-dual-cassette.md`.

These are ALL valid connections — they just aren't *new*. Your job is to find the next layer beyond what's already actioned.

**The seven categories where genuine novelty can still be found:**

1. **Cross-domain synergies** — findings from one track that unlock opportunities in another, AND not already cross-linked in either canonical page (e.g., a *new* koji secondary metabolite that hits an NLRP3 chokepoint nobody mapped to it)
2. **Contradictions or tensions** — two documents disagreeing on mechanism, strategy, or feasibility, where the contradiction is NOT already documented in either page
3. **Unexploited combinations** — molecules, pathways, organisms that appear in multiple documents without anyone connecting them into a strategy. If `koji-endgame-strain.md` already lists the combination, it's exploited.
4. **New experiments** — especially cheap, fast ones that de-risk expensive downstream work, AND not already in `validation-experiments.md` or `computational-experiments.md` Planned Analyses
5. **Risk interactions** — risks that compound or cancel across tracks, where the interaction isn't already named in `synthesis.md` Strategic Reflections Queue or canonical risk pages
6. **Blind spots** — questions nobody is asking that someone should, AND not already in `open-questions.md`
7. **Platform-level patterns** — observations that apply across multiple compounds/strains/chokepoints rather than to one, AND not already framed in `open-enzyme-vision.md`, `modality-chokepoint-matrix.md`, or platform-thesis pages

If your candidate finding fails the novelty bar in any of these categories, drop it. **Three high-quality novel findings beat ten restatements.**

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

If after reading the corpus you find no genuinely new connections, output a brief note and exit. The drift guard fires when **any** of these conditions hold:

1. **Trigger was a typo fix or trivial edit** — no semantic change to evaluate.
2. **Restates current synthesis.md** — your candidate findings would just repeat what's already in the most-recent block of `wiki/synthesis.md` (if any items remain there post-inbox-zero).
3. **Restates the canonical wiki pages** — your candidate findings are already explicit as named sections, callouts, or first-class topics in the cited canonical pages. Use the "Where actioned items live now" pointers (synthesis.md bottom) and the duplicate-check examples in "What to look for" above as your reference.
4. **Restates a recent prior-sweep log** — your candidate findings appear in any `logs/v4-synthesis-*.md` from the last 3 sweep-history entries.
5. **Inbox-zero blind-spot trap** — `wiki/synthesis.md` shows `(none — inbox zero as of YYYY-MM-DD)` AND the trigger files were just heavily edited by the human walkthrough that produced that inbox-zero. In this case, the wiki content explicitly contains the connections that were just actioned; re-deriving them is the failure mode this drift guard exists to prevent. Read the most recent sweep-history entry's log file and treat its findings as already-actioned.

```markdown
# Synthesis — <YYYY-MM-DD>
**Status:** No new synthesis. <one-sentence reason>.
```

Better to skip than to pollute the queue with low-signal entries. Pass 3 reviewer will see the no-op and prepend a corresponding short entry to `wiki/synthesis.md`.

**Partial-novelty case.** If you find 1–2 genuinely novel items and 5+ restatements, output ONLY the novel items. Do not pad the synthesis with restatements to "fill" the standard 3+3+3+3 structure. The structure is a maximum, not a quota. A synthesis with one new Connection and zero of the other categories is a valid output if that's what the corpus actually contains.

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
