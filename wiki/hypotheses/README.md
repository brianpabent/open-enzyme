---
title: "Hypotheses Index — Committed Scientific Claims, Falsification Cards, Survival Tallies"
date: 2026-04-24
tags:
  - hypotheses
  - falsification
  - commit
  - index
  - rigor
  - killshot-menu
related:
  - ../linter-design.md
  - ../synthesis.md
  - ../open-questions.md
  - ../validation-experiments.md
sources:
  - "linter-design.md (design doc for the two-linter architecture)"
  - "falsification-lint-brief.md (2026-04-24, personal download — the source brief)"
status: index
---

# Hypotheses Index

This directory holds **committed scientific hypotheses** in Falsification Card form. Each file is a self-contained artifact: the claim, the assumptions it rests on, the killshot menu ranked by information weight per dollar, pre-committed thresholds for Alive / Killed / Pending / Retracted, kill switches, execution log, and survival score.

The schema and the rationale live in [linter-design.md](../linter-design.md). This page is the entry point and the index.

---

## What "Committed" Means

A hypothesis is *committed* when it is written to a file in this directory with a first git commit. That commit is the pre-registration: the claim, the initial assumption stack, and the killshot menu are frozen as of that SHA. Any subsequent edit creates a new commit with a visible diff. This is the git-native equivalent of the brief's call for `{claim, killshots, thresholds}` hashing — see `linter-design.md` §6.

Convention: the hypothesis file's first commit is the load-bearing one. Subsequent commits carry rationale in the commit message (e.g., `H01: tighten lactoferrin threshold from 100 to 500 mg/L — Ward 1995 submerged baseline is 2 g/L, 500 mg/L is the Phase B acceptance floor`). The git log is the audit trail.

Committing to a hypothesis is a commitment to *attempt to falsify it*, not a commitment to defend it. A hypothesis that survives zero killshots after a year isn't defended; it's pruned or retracted.

---

## File Naming

- Pattern: `H0N-slug.md` where `N` is zero-padded two-digit (H01, H02, …, H99). Three digits (H001, H002) when the collection exceeds 99.
- `slug` is short, hyphenated, mnemonic. Prefer 2–4 words. Example: `H01-ward-dual-cassette.md`.
- No dates, no authors, no status in the filename. Those live in frontmatter (`committed:`, `status:`) and mutate over time. Filenames are stable identifiers.

---

## Current Hypotheses

| ID | Title | Status | Survival count | Committed | Link |
|---|---|---|---|---|---|
| H01 | Ward 1995 glucoamylase-KEX2 dual-cassette architecture layers uricase + lactoferrin in *A. oryzae* solid-state rice koji | Pending | 0 | 2026-04-24 | [H01-ward-dual-cassette.md](./H01-ward-dual-cassette.md) |

*(Add new rows as hypotheses are committed. Sort by ID.)*

---

## Lifecycle

1. **Commit.** Write the Falsification Card (claim, assumption stack, killshot menu, thresholds, kill switches, empty log) to `H0N-slug.md`. Git commit. Status: `Pending`.
2. **Lint.** Run Falsification Lint (manual / agent invocation) against the committed file. The linter reads the hypothesis + cross-referenced wiki pages, may propose additional killshots or assumptions, and may suggest the cheapest-upstream redirect per the brief's hero interaction. The author decides what to adopt; adoption creates a new commit with the diff visible.
3. **Test.** Execute killshots in the order the menu dictates — cheapest, highest-info first. Record results inline in the `Log` table. Each executed killshot updates `status` and `survival_count`.
4. **Log outcome.** For each killshot: date, killshot identifier, outcome (killed / survived / ambiguous), notes, and any deviations from the pre-committed protocol. Survival-count and survival-score are updated per `linter-design.md` §6.
5. **Update status.** `Pending` → `Alive` on first survived killshot. `Pending` or `Alive` → `Killed` on first threshold-crossing kill. Status can move Alive → Killed if a later killshot crosses a threshold; it can move Killed → Alive only via Retraction (§ below).
6. **Retract if needed.** If a killshot result is later invalidated (bad control, assay artifact, substrate batch problem), document the retraction in the file's Retraction History section and recompute status based on remaining valid killshots. Status: `Retracted` while the recount is pending; resolves to `Alive` / `Killed` / `Pending` on re-evaluation.

The lifecycle is sequential per hypothesis but not per directory. Multiple hypotheses can be at different lifecycle stages simultaneously.

---

## Status Meanings

- **Pending.** Committed, no killshot yet executed. The default initial state.
- **Alive.** At least one killshot has been run; the claim has not been falsified per its pre-committed thresholds. Survival count > 0.
- **Killed.** At least one killshot has crossed its Killed threshold. The claim is falsified. Documented in the Log with the killshot result.
- **Retracted.** A previously-counted killshot result has been invalidated. Status is being recomputed; intermediate holding state.

A hypothesis with status **Killed** is not deleted. The file stays; the killed claim is part of the wiki's epistemic history. A Killed hypothesis can motivate a new committed hypothesis (a revised claim at a new file, H0M-*), but the Killed file itself is preserved.

---

## Relationship to `wiki/synthesis.md` and `wiki/open-questions.md`

- **synthesis.md** is the generative action queue — new dot-connections, proposed experiments, cross-doc findings. It is promiscuous, fast-moving, and pruned manually by Brian. Items in synthesis.md are candidates for hypothesis promotion; not all candidates graduate.
- **open-questions.md** is a cross-wiki index of unresolved questions. Some of those questions map to committed hypotheses; most don't. An open question is a prompt for investigation; a committed hypothesis is a specific falsifiable claim plus a plan to attempt falsification.
- **hypotheses/** is where a specific, falsifiable claim gets a Falsification Card and a commit. Not everything in synthesis or open-questions becomes a hypothesis — only the ones the user is ready to commit resources against.

Flow (typical): synthesis.md finding → open-questions.md entry → (if worth testing) → hypotheses/H0N commit → Falsification Lint → execute killshots → update status.

---

## Conventions Summary

- One file per hypothesis. Filename is the stable identifier.
- First commit is the pre-registration. Subsequent edits are visible diffs with rationale in commit message.
- Status is frontmatter (`status:`). Survival count is frontmatter (`survival_count:`).
- Killshot menu is a table, sorted by `score` descending.
- Thresholds are pre-committed — declared before the first killshot runs.
- Failure modes are tagged from `linter-design.md` §5.
- Retraction history is in-line, not in a separate directory. Visibility is the point.
