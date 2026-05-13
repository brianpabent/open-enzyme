---
title: Future papers + blogs pipeline
date: 2026-05-13
status: living document
purpose: capture noteworthy findings from the heterogeneity-guard audit (and future audits) that don't belong in the current paper but earn a future write-up
---

# Future papers + blogs pipeline

Living index. Items here originated in deep-dives done for the heterogeneity-guard methodology paper (`papers/cross-vendor-heterogeneity-guard/`) but are out-of-scope for that paper's argument. Each entry names the angle, where the source material lives, why it earns its own write-up, and whether it reads more naturally as a paper or a blog.

When an item moves into active drafting, create a sibling directory under `papers/` (for papers) or under `abent-family/brian/blog/drafts/` (for blogs) and link both ways.

---

## Items earmarked for active development

### F1. Verification-of-verification as a discipline

**Angle.** When AI-summarized literature inherits supplement-industry citation laundering, multi-vendor cross-checks don't help (every vendor inherits the same contaminated training corpus). What defends is a second independent subagent that checks the first subagent's verification against primary source. This is structurally distinct from cross-vendor heterogeneity and earns its own treatment.

**Source material:**
- `operations/notable-moments.md` 2026-05-07 entry (three-layer laundering of the "37% testosterone elevation" figure)
- `papers/cross-vendor-heterogeneity-guard/audit-2026-05-13-catch-history.md` §1.7 + §3.2
- Commits `a61f0d9`, `c32a623` (eurycomanone direction-of-effect reversal: GOUT-UNFAVORABLE → GOUT-FAVORABLE)

**Why it earns its own write-up:** the heterogeneity paper's §5 will mention this as a case study, but the *discipline* (V-of-V protocol, cost economics, when to fire it) needs its own argument. Cost was $3-4 per verification chain. The flipped direction-of-effect is a real biology consequence — supplement marketing has gout-favorable compounds tagged as gout-unfavorable for a decade.

**Recommended channel:** short paper (methods note for biorxiv or Patterns letter) OR a long-form Substack blog. The blog version reaches the right audience faster (supplement-skeptical biology people) and doesn't need formal peer review.

**Status:** placeholder.

---

### F2. Translation protocol — two-model cross-check + inline disagreement

**Angle.** When ingesting non-English scientific literature (Chinese CNKI, Japanese J-STAGE, Korean KISS, etc.), two-model independent translation with inline disagreement annotation preserves the precision the source paper intended. Single-model translation silently collapses interpretive ambiguity.

**Source material:**
- `CLAUDE.md` §"Translation protocol (two-model independent cross-check + inline disagreement annotations)"
- The 2026-05-05 conversation that codified the rule (path-dependent narrowing fix)

**Why it earns its own write-up:** TCM/Kampo/Ayurvedic literature is structurally underweighted in English-trained models. The protocol's value is empirical (catches mechanism-level mistranslations) but hasn't been demonstrated with a concrete worked example yet. Could pair well with a specific OE compound investigation that surfaced a translation-driven catch.

**Recommended channel:** short methods paper, paired with a worked example from an OE compound (eurycomanone, berberine, or other CNKI-rich compound). Or blog post if the worked example isn't yet substantial.

**Status:** placeholder; needs a worked example before drafting.

---

### F3. Pre-daemon vs. post-daemon quantitative comparison

**Angle.** Before 2026-04-25, synthesis was a single Claude-Opus working session. After 2026-04-25, synthesis is the three-pass daemon. The git history spans both eras. Quantifying catches per sweep window, time-to-catch, and class-of-error coverage across the two eras would test the heterogeneity-guard hypothesis empirically — not just defensively (catches not made) but generatively (catches surfaced that weren't on the human's radar).

**Source material:**
- `audit-2026-05-13-catch-history.md` §4 has rough numbers; needs validation against actual sweep logs and `operations/notable-moments.md`
- `synthesis/done/` closure annotations are the canonical "what was actioned" record
- Each pre-daemon catch needs to be identified from `operations/notable-moments.md` + wiki commit history before 2026-04-25

**Why it earns its own write-up:** the heterogeneity paper makes the architectural argument; this paper would test the empirical claim. Distinct contributions. The current paper acknowledges "operational data does not yet support a quantitative false-positive rate estimate" (§5.4 → §6 transition); the quantitative paper closes that gap once the operational record extends to ~6 months.

**Recommended channel:** paper (Patterns short communication, or follow-up to the methodology paper). Needs longer operational window before it's defensible.

**Status:** placeholder; revisit at ~6 months operational record (target ~2026-10).

---

### F4. The git record IS the methodology paper

**Angle.** Traditional methodology papers freeze recommendations at publication time and decay as the system evolves. The Open Enzyme repo's git history is the methodology artifact — every discipline emerges empirically (failure → diagnosis → fix → codification) and the audit trail is queryable. This argues for "working in the open with git as canonical record" as a publishing alternative for fast-moving systems.

**Source material:**
- `audit-2026-05-13-catch-history.md` §10 "Final note: operational discipline as knowledge"
- Cross-reference to `wiki/open-source-platform.md` §"Multi-model synthesis as guard against epistemic homogenization"
- Counterpoint: papers like Lu et al. 2024 (AI Scientist) freeze methodology; the methodology has since evolved.

**Why it earns its own write-up:** meta-point about the publishing model itself. The heterogeneity paper would have a circular dependency if it argued this internally ("you should publish papers about why papers are decaying" inside a paper). Better as a blog post that argues the case independently, citing the OE wiki as worked example.

**Recommended channel:** blog (Substack) — the argument has bite for an audience reading independent AI/research writers more than journal readers.

**Status:** placeholder.

---

### F5. Convergence without coordination — generative property of heterogeneity

**Angle.** On 2026-05-08, Brian published a blog post about the DAF SCR1-4 multi-vendor catch (private repo, not on the wiki) the same day the daemon's Pass 2 synthesizer independently surfaced "write up the DAF SCR1-4 incident as a mini case study." Two independent reads converged on the same valuable external-communications angle without coordination. The heterogeneity paper's §5.5 covers convergence as a generative property in research; this incident shows the same property in *communications/strategy*.

**Source material:**
- `operations/notable-moments.md` 2026-05-08 entry "Two independent reads of the same wiki, same day, same external-comms insight"
- The blog draft itself (private repo)
- Daemon Pass 2 Gemini synthesis log from that day

**Why it earns its own write-up:** the methodology paper covers the research-finding convergence; this incident is about *what to publish*, not *what is true*. Distinct angle. Reflexively interesting since the audience for the future write-up is exactly the kind of person who finds this incident interesting.

**Recommended channel:** blog post (Substack), short.

**Status:** placeholder.

---

## Items NOT promoted (logged for completeness; revisit if pattern recurs)

### N1. Synthesis filesystem migration spec review (2026-05-08)

Too operational, low generalizability. The lesson (collaborative design review surfaces oversights that single-pass review misses) is already covered by the broader heterogeneity argument and doesn't need its own paper. Specifics live in `operations/specs/2026-05-08-synthesis-filesystem-migration-*.md` for the repo's internal memory.

### N2. Cursor advancement bug (2026-05-07)

CI-specific bug. Lives in commit `45db8eb` and `scripts/SWEEP-ARCHITECTURE.md`. Reproducibility detail; not a methodology contribution.

### N3. Per-commit truncation tolerance (2026-05-08 to 2026-05-09)

Resource-budgeting failure with graceful-degradation fix. Architectural principle is real but might fit better as a paragraph in a future "graceful degradation in multi-pass AI pipelines" piece if one ever justifies itself. Not promoted on its own.

### N4. Prompt caching as implicit heterogeneity (2026-05-06)

Vendor-capability difference rather than vendor-bias difference. Could fit as a paragraph in the heterogeneity paper itself if §3 or §4 expands; otherwise too narrow for its own write-up.

---

## Process notes

- New items should cite a specific source file or commit before going in this list.
- "Recommended channel" is a guess; reassess when the item moves to drafting.
- When promoting from this file to active drafting, leave the entry behind with a `**moved to:** <path>` line so the trail survives.
- Audits like `audit-2026-05-13-catch-history.md` are primary sources. This file curates from them.
