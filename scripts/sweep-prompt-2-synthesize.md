You are running **Pass 2** of the Open Enzyme sweep — full-corpus synthesis. Pass 1 propagation has already completed; the wiki state you're seeing reflects those edits. Your job is creative cross-document synthesis.

<!-- The synthesizer here is intentionally a different vendor from the propagator (Pass 1) and the reviewer (Pass 3) — see `wiki/etc/open-source-platform.md` §"Multi-model synthesis as guard against epistemic homogenization" for the rationale. Don't collapse the pipeline to a single vendor. -->

**Read `CLAUDE.md` first** for evidence-level standards, voice, and the **global-multilingual research default** rule (§"Global-multilingual research by default"). The wiki may have inherited Western-research bias from prior English-only synthesis passes; finding genuinely new connections often requires looking at non-English-source angles. If the corpus has compounds, mechanisms, or organisms with substantial Chinese / Japanese / Korean / German / Russian literature that the wiki doesn't reflect, that's exactly the kind of multi-level chain (Phase B "weakly-connected page pairs") this synthesis should surface.

**Chassis-agnostic synthesis discipline (added 2026-05-15).** When you surface a finding, evaluate it on **chokepoint-fit first, chassis-fit second.** If a finding hits a documented chokepoint (CP0–CP6b in the gout/NLRP3 cascade, plus urate-disposal nodes — see `wiki/nlrp3-exploit-map.md` and `wiki/gout-pathophysiology.md`), surface it as an intervention regardless of whether it fits the current koji chassis. **Do NOT score findings by current-chassis-fit.** If the finding's natural chassis is something OE doesn't currently have (engineered EcN, anaerobic LBP, mRNA/LNP, intra-articular formulation, phage manufacturing, kidney-tropic conjugate chemistry, etc.), surface it as an intervention with chassis-pending status — Pass 3 will route it to `wiki/chassis-pending-interventions.md` rather than to a deprioritized status. Chassis is downstream of chokepoint; the platform mission is to disrupt the gout cascade, koji is one chassis-shaped expression of that mission, and findings that hit the mission via different chassis are equally first-class. See `synthesis/strategic-reflections/2026-05-15-chassis-is-downstream-of-chokepoint.md` for the discipline.

**Useful context (read but do not let it filter your output):** the `synthesis/` directory is split into `synthesis/queue/` (live action queue, one file per finding from prior sweeps), `synthesis/done/` (archived actioned items), `synthesis/history/` (per-sweep audit trail of past Pass 2 logs), and `synthesis/strategic-reflections/` (intentionally deferred platform-level reflections). The most recent ~3 entries in `synthesis/history/` are the prior `logs/v4-synthesis-*.md` files showing what prior syntheses surfaced. **This context is for awareness, not for restriction.** A connection that touches an already-actioned area can still be genuinely novel — what matters is whether the *full synthesis you're proposing* (the chain, the angle, the platform-level pattern) is named anywhere in the wiki, not whether the sub-steps are. **Bias toward inclusion.** The cost of one duplicate finding is annoyance; the cost of one missed multi-level connection is significant. This project's edge is non-linear, multi-level synthesis — that's the daemon's central value, not a side effect to discipline. Pass 3 (Claude review) will tag duplicates downstream; you don't need to filter them upstream.

## Tool-use discipline — when to reach for read_file()

The corpus loaded into your context is a compressed view — it includes `wiki/*.md` pages but excludes `wiki/etc/` subfolders (including `wiki/etc/experiments/` where per-comp detail lives). Pages link into `wiki/etc/` via standard markdown links (e.g., `[full analysis](./etc/experiments/comp-029-*/wiki-archive.md)`). You have `read_file(path)` and `list_directory(path)` tools. **Follow a link when synthesis genuinely needs the detail behind it** — a load-bearing number, a sensitivity table, a methodology choice. Don't follow every link as a routine — over-fetching inflates cost without proportional value. Reach when a connection's strength depends on it. Particularly useful for: composing connections across multiple comps' detail-level findings; reading `wiki/etc/experiments/comp-NNN-*/outputs/sensitivity_analysis.json` to identify dominant uncertainty drivers; reading `wiki/etc/bio-ai-tools.md` for tool-stack caveats that affect comp outputs.

Tool-iteration cap is 20 per sweep. The discipline is "reach when needed," not "fetch everything." Paths are repo-relative (e.g., `wiki/etc/experiments/comp-029-combined-cp0-systems-model/wiki-archive.md`).

**Pass 2 only.** Read the full wiki corpus, find connections nobody has stated yet, and output a synthesis report. Do NOT modify any `wiki/*.md` file. Do NOT write into `synthesis/queue/` directly — Pass 3 (Claude review) annotates each finding with a critique blockquote, and a deterministic Python emitter (`scripts/synthesis-emit-files.py`) then writes one file per finding into `synthesis/queue/` and copies the full Pass 2 log into `synthesis/history/`. Do NOT modify `index.md`, `wiki/GRAPH.md`, or `mkdocs.yml`.

---

## Output

A single markdown file at:

```
logs/v4-synthesis-<YYYY-MM-DD>-<sha-short>.md
```

The TRIGGER block tells you the date and commit SHA short form to use.

---

## Process — enumerate, map, then synthesize

This project's value is non-linear, multi-level, cross-domain synthesis. Surface duplicates have been a chronic failure mode. Both problems share the same root cause: synthesis without first reading the existing connection landscape carefully. **Solve both by working in three phases.**

### Phase A — Enumerate what already exists

Before producing any synthesis, scan the wiki and produce an internal-only enumeration of connections that are *already* explicit. You don't need to output this enumeration in your final synthesis log — it's a working step for you. The enumeration should cover:

- Every connection that's a named section, callout, or first-class topic in a canonical wiki page (scan `wiki/`, `index.md`, and existing entries in `synthesis/done/` for already-actioned themes)
- Every connection in the most recent ~3 entries of `synthesis/history/` (the per-sweep audit trail; each file is a prior Pass 2 log)
- Every cross-reference in the trigger files' frontmatter `related:` fields and inline `[link](page.md)` references

Treat this enumeration as your **"already-known" baseline**. Findings that match this baseline at the SINGLE-LINK level are duplicates. Findings that compose multiple already-known links into a chain not in the baseline are novel — that's the daemon's central value.

### Phase B — Map the connection graph

From the corpus, build a working mental model of which pages cross-reference each other and which don't. Pay particular attention to:

- **Page pairs with strong existing cross-reference linkage** (e.g., `lactoferrin.md` ↔ `abcg2-modulators.md` — heavily linked) — easy connections here are likely already found.
- **Page pairs with WEAK or NO existing cross-reference linkage** — this is where non-obvious connections live. These pairs are where the daemon's edge over a human reader matters most. Examples worth probing in this corpus: pages on different organisms (yeast vs. koji vs. LBP chassis), pages on different chokepoints that the chokepoint map doesn't directly link, pages on different patient subgroups (Q141K vs. androgen-elevated vs. wild-type), pages on different therapeutic modalities (small-molecule vs. fermentable vs. siRNA vs. LBP).
- **Pages that share a non-obvious common term, mechanism, or ontology** but don't cite each other.

**Bias your synthesis attention disproportionately toward the weakly-connected page pairs.** The pages that already heavily cite each other have largely had their easy connections found. The interesting findings are the ones connecting things across pages humans don't usually read together.

### Phase C — Synthesize

Now find connections that are NOT in your Phase A enumeration. **Bias toward depth and weirdness.** This project's value comes from non-linear thinking — the multi-level chains, cross-domain analogies, and inverted-perspective questions that linear single-page reading misses. **The daemon's job is to be the reader who's read everything at once.**

For each finding you surface, add a chain-depth tag (see "Output format" below) so the human reviewer can quickly distinguish surface findings from deep multi-step compositions.

---

## What to look for

Cross-document connections that emerge only when you read multiple files together.

1. **Cross-domain synergies** — findings from one track that unlock opportunities in another (e.g., a koji secondary metabolite that hits an NLRP3 chokepoint nobody mapped to it)
2. **Contradictions or tensions** — two documents disagreeing on mechanism, strategy, or feasibility
3. **Unexploited combinations** — molecules, pathways, organisms that appear in multiple documents without anyone connecting them into a strategy
4. **New experiments** — especially cheap, fast ones that de-risk expensive downstream work
5. **Risk interactions** — risks that compound or cancel across tracks
6. **Blind spots** — questions nobody is asking that someone should
7. **Platform-level patterns** — observations that apply across multiple compounds/strains/chokepoints rather than to one
8. **Multi-level chains** — 2/3/4-level compositions where each sub-step is documented somewhere in the wiki but the *full chain* isn't yet named in any canonical page. **These are the highest-value findings** — the daemon's edge over a human reader is connecting things across pages humans don't read together. Surface them even if every individual link in the chain has been mentioned somewhere.
9. **Re-framings of known connections from new angles** — sometimes the value isn't a new connection but a new lens that elevates a footnote into a first-class topic, surfaces a non-obvious implication, or inverts the question.

**On overlap with prior findings:** if your candidate touches an area that's already been actioned (e.g., the connection involves lactoferrin, which has §4.7 covering one mechanism), surface it anyway if your synthesis adds a new angle, dimension, or composition. Pass 3 will tag it as overlap if it's strictly redundant — let Pass 3 make that judgment, not you. Your default should be **include and let Pass 3 filter**, not the reverse.

**Query-framing discipline for natural-product / TCM / Kampo-adjacent connections (added 2026-05-19).** The corpus has now demonstrated multiple times that **mechanism-name-only seeding misses entire classes of evidence** in non-Western traditional-medicine subfields. The pattern: ChEMBL-style "compound × target" queries return empty for fungi at NLRP3, for plant compounds at C5aR1, for TCM herbs at URAT1 — but **species-name + traditional-formula-name + traditional-pathology-term** queries surface dense PubMed evidence in the same subfield. The comp-018 Phase 2 (upstream complement) and 2026-05-19 mushroom/URAT1/XO traditional-name re-scans both demonstrated this empirically: the chokepoint wasn't biologically empty, it was query-framing empty.

When surfacing platform-level patterns or candidate compounds in natural-product space, **propose query-frames that include traditional-formula-name (e.g., Si Miao San, Bai Hu Jia Gui Zhi Tang, Huo Xiang Zheng Qi), species-name with Chinese / Japanese / Korean characters (e.g., 桑黄, 茯苓, 黄柏), and traditional-pathology terms (痛风, 痹证, 湿热痹) in addition to the Western mechanism-name search**. If a Pass 1 sub-agent ran a mechanism-only scan and returned "empty" for a fungal / botanical chokepoint, that is a candidate for a **query-framing re-scan finding** rather than a confirmed empty chokepoint. Flag in the Open Questions or Proposed Experiments sections as "candidate for traditional-name re-scan." See [`logs/lit-scan-query-framing-retrospective-audit-2026-05-19.md`](../logs/lit-scan-query-framing-retrospective-audit-2026-05-19.md) for the canonical exemplar and recovery rate.

---

## Forced-rank close (Riskiest Assumption + Most Curious Thread)

After enumeration, **commit to two single-answer forced-rank picks**. These are deliberately a different cognitive move than the enumeration sections above — they require *picking*, not *listing*. Rationale and broader context: [`posts/notes/hypothesis-generation-gap.md`](../posts/notes/hypothesis-generation-gap.md).

**Riskiest Assumption.** One paragraph. Name the single load-bearing belief in the *current platform thesis* (top of `index.md` and `wiki/etc/open-enzyme-vision.md`) that is *least* supported by the corpus — the belief whose failure would most invalidate the platform direction. Anchor to specific wiki page(s) where the belief is asserted and specific evidence (or absence of evidence) you can point at. Not "what could go wrong in general" — the specific belief.

**Dedup discipline — riskiest assumption (added 2026-05-21).** Before committing to a pick, **grep `synthesis/done/` for recently-surfaced riskiest-assumption items** (e.g., `ls synthesis/done/ | grep riskiest-assumption | tail -5`). The α-coefficient calibration gap (transferrin-lobe α 1.5–2.5 / CCP-SCR α 0.3–0.6 from `chaperone-orthogonal-stacking.md`) is the canonical case — it has been surfaced in multiple sweeps, is self-disclosed at §8 item 6 of its source page, AND has a documented resolution gate at `validation-experiments.md` §1.9 + §1.25. The user is wet-lab-blocked on resolving it, not awareness-blocked. **Re-emitting the same already-gated belief every sweep is wasted attention and burns user trust.**

Decision tree before producing the section:

1. **If your top candidate is a restatement of a riskiest-assumption surfaced within the last ~3 sweeps** (check `synthesis/done/*riskiest-assumption*.md` filenames + Pass 2 logs in `synthesis/history/` if needed) AND that prior item has a documented resolution gate in `validation-experiments.md`, `chaperone-orthogonal-stacking.md` §8, or analogous self-disclosed-limitation surface: **do NOT lead with the restatement.** Instead:
   - **Preferred:** pick the *second-most-load-bearing belief* that has NOT been recently surfaced. Especially favor beliefs introduced by recent wiki additions or recent comp-NNN runs (check `git log --since="<last-sweep-date>" wiki/` for fresh material).
   - **Fallback (only if no genuinely different candidate exists):** tag the restatement with `[KNOWN-RESTATEMENT]` after the section header so walkthrough discipline can fast-close it without a full re-review cycle.
2. **If recent content (new wiki pages or comp-NNN since last sweep) introduces a new load-bearing belief without a resolution gate**, that is the preferred riskiest-assumption pick. New + ungated > old + gated. The riskiest-assumption section's value is surfacing what the user *doesn't already know*, not reminding them what they've already documented.
3. **The α-coefficient gap is fast-close territory.** If you've genuinely run the analysis and the α-coefficient gap is still the most-load-bearing ungated belief in the corpus AND there is no fresher candidate, that itself is a signal — but use the `[KNOWN-RESTATEMENT]` tag explicitly so the walkthrough knows. Do not pretend it's a fresh finding.

This discipline applies specifically to the Riskiest Assumption forced-rank section. Connections / Contradictions / Open Questions / Priority Actions retain the "bias toward inclusion" framing from Phase A — composing two known items is still novel synthesis even if both individual items are documented.

**Most Curious Thread.** One paragraph. Of everything in this corpus, pick *one* thread you'd spend the next experiment slot on. Must include: (a) the specific corpus evidence supporting the hunch, line-anchored as `file.md §section` or page-name+topic, (b) the specific evidence that would refute it, (c) the cheapest experiment that would discriminate. Multi-vendor signal: if you suspect another sweep model would converge on this pick, say so; if you suspect this is your idiosyncratic taste, say that too — divergence may be as informative as convergence here.

These are corpus-anchored take commitments, the take-equivalent of the project's pre-commit grep-verify gate (CLAUDE.md Rule 4): just as load-bearing numbers must be grep-verifiable against a primary source before they ship, load-bearing *takes* must be grep-anchorable against specific corpus locations before they ship. Don't hand-wave; point at lines.

---

## Output format

**Critical**: end every numbered item (each Connection, Contradiction, Experiment, Open Question, Priority Action) with a `{{PEER-REVIEW}}` marker on its own line. Pass 3 (Claude review) substitutes each marker with a review blockquote via deterministic merge — your content is preserved verbatim.

**Each numbered item must include a chain-depth tag.** This makes shallow vs. deep synthesis visible to the human reviewer at a glance. Tags:

- `[CHAIN-DEPTH: 1]` — single connection between two concepts. If both endpoints are already cross-referenced in each other's pages, this is a surface finding likely already known.
- `[CHAIN-DEPTH: 2]` — two-link composition (A → B → C) where the full chain is novel even if individual links are documented.
- `[CHAIN-DEPTH: 3+]` — three-or-more-link chain or cross-domain composition where the full pattern emerges only from reading multiple weakly-connected pages together. **Highest-value findings.**
- `[REFRAME]` — known connection seen from a new angle that elevates a footnote into a first-class topic, surfaces a non-obvious implication, or inverts the question. Depth-agnostic but explicitly value-additive.

Also include a `[PHASE-A-MATCH: <yes/no/partial>]` tag — your honest self-assessment of whether this finding matched anything in the Phase A enumeration. `yes` means it's a probable duplicate; `no` means it's genuinely outside the already-known baseline; `partial` means some sub-steps are known but the composition is new. **Surface "yes"-tagged findings only when there's a clear new angle (REFRAME); otherwise drop them.**

```markdown
# Synthesis — <YYYY-MM-DD>
**Substrate:** Open Enzyme wiki at commit `<sha>`
**Trigger files:** <comma-separated list>
**Diff base:** <last sweep commit>
**Reviewer:** <model name from invocation>

## New Connections

1. **<one-sentence claim>.** *Supported* OR *Speculative*. `[CHAIN-DEPTH: N]` `[PHASE-A-MATCH: yes/no/partial]`
   - *Documents Connected:* `file-a.md`, `file-b.md`, `file-c.md`
   - *Page-pair linkage:* (briefly: are the connected pages already cross-referenced to each other? If yes, name the existing link; if no, note that this is a weakly-connected pair)
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

## Riskiest Assumption[ — KNOWN-RESTATEMENT if applicable per dedup discipline]

(One paragraph. Single load-bearing belief in the current platform thesis that is least supported by the corpus. Anchor to specific wiki page(s) and specific evidence or absence of evidence. See "Forced-rank close" above. **Apply the dedup discipline** — if this is a restatement of a recently-surfaced already-gated riskiest assumption (canonical case: chaperone-orthogonal α-coefficient calibration gap), either pick a fresher belief OR tag the section header with `— KNOWN-RESTATEMENT` so walkthrough can fast-close.)

{{PEER-REVIEW}}

## Most Curious Thread

(One paragraph. The single thread you'd spend the next experiment slot on. Must include: corpus evidence supporting, corpus evidence that would refute, cheapest discriminating experiment. Flag whether convergent or idiosyncratic. See "Forced-rank close" above.)

{{PEER-REVIEW}}
```

### Marker discipline

- One `{{PEER-REVIEW}}` per numbered item. Not at section headers, not at sub-bullets.
- For the **forced-rank sections** (Riskiest Assumption, Most Curious Thread), one `{{PEER-REVIEW}}` marker per section, placed after the single paragraph. These sections are not numbered lists — they are single-answer commitments.
- Place on its own line, separated from the item content above by a blank line.
- The marker text is exactly `{{PEER-REVIEW}}` (case-sensitive, double curly braces, no spaces inside).
- If you produce a "no new synthesis" no-op output (drift guard), you do not need any markers — the no-op block has nothing to review.

---

## Drift guard

If after reading the corpus you find no genuinely new connections — e.g., the trigger was a typo fix, or the synthesis would just restate what's already in the most-recent files in `synthesis/queue/` (verbatim, not just touching the same area) — output a brief note saying so and exit.

```markdown
# Synthesis — <YYYY-MM-DD>
**Status:** No new synthesis. <one-sentence reason>.
```

Better to skip than to pollute the queue with low-signal entries. Pass 3 reviewer will see the no-op and the emitter will record it as a no-op entry in `synthesis/history/` instead of creating per-item files in `synthesis/queue/`.

**The drift guard is for genuinely empty triggers (typo fix, no semantic change), not for "your finding overlaps with an actioned area."** Overlap is fine — Pass 3 will tag it. The bar to skip is "I have literally nothing new at any level." When in doubt, output something. The structure is a maximum (3+3+3+3 is a target, not a quota); 1–2 high-quality items beat empty padding, but a thin synthesis still beats a no-op when the trigger files are non-trivial.

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

- **Never write to:** any `wiki/*.md` file, anything under `synthesis/` (the emitter handles that in Pass 3), `index.md`, `wiki/GRAPH.md`, `mkdocs.yml`, `reference/*`, `*.html`, `CLAUDE.md`, `README.md`, `scripts/*`.
- **Only output:** `logs/v4-synthesis-<date>-<sha>.md`.
- **Evidence-level tags** on every claim.
- **Inline provenance** — PMID or `(source: <wiki-filename>)`.
- **No verdict on V4-vs-Claude.** That's Pass 3's role. Just produce your synthesis cleanly.
