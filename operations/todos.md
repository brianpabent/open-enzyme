---
title: Open Enzyme Operational TODOs
date: 2026-05-05
status: active
---

# Operational TODOs

Active action items across the project that don't fit `wiki/synthesis.md`'s Strategic Reflections Queue (which is for content-triggered research-strategy reflections, not transactional todos). Triaged by category. Date-stamped when added.

## §1.9 Ward 1995 dual-cassette execution path

- **[2026-05-05] Wait for Lauren Collier-Hyams' read on §1.9.** She replied "ok lemme try to dig into this and i'll get back to ya" after the Huynh-2020 + comp-010 follow-up. If no response by 2026-05-12, send a soft check-in nudge.
- **[2026-05-05] Outreach to Maruyama group at Tokyo University.** See [`ward-1995-lab-access.md`](./ward-1995-lab-access.md) for substantive context. Two asks: MTA on NSlD-ΔP10 (minimum) + collaboration / fee-for-service on the dual-cassette transformation (more ambitious). Send when Lauren's path is clearer (parallel-track, don't double-ask).
- **[2026-05-05] Verify NSlD-ΔP10 is genuinely not in any public strain repository.** Direct catalog queries to JCM, NBRC, CGMCC, CBS-KNAW, ATCC, FGSC. The lab-access subagent's verification was best-effort; one batch of confirmation emails would close this with certainty. Particularly check NBRC (the Japanese repository the Maruyama group is most likely to deposit through).
- **[2026-05-05] Pull PI corresponding-author emails for Jiangnan, DTU, Wösten, South China Univ of Tech groups.** They exist in the published papers' corresponding-author footers but weren't pulled into [`ward-1995-lab-access.md`](./ward-1995-lab-access.md). Pre-outreach data hygiene.
- **[2026-05-05] Espacenet patent landscape deep-dive on *A. oryzae* dual-cassette.** Per H01 Killshot #1's residual caveat (~30% probability of unpublished industrial IP from Novonesis [née Novozymes], DSM-Firmenich, Genencor lineage). Worth running through Emory's authenticated patent database access if Lauren engages further.

## Project-context outreach (general)

- **[2026-05-05] Verify wiki page URLs render on the GitHub Pages site** before sending links to external collaborators. Particularly the deeply-anchored URLs (`#19-ward-1995-...`) that depend on mkdocs-material slug generation. Last-known-working URL pattern: `https://brianpabent.github.io/open-enzyme/<page-slug>/#<heading-slug>`.
- **[Standing] Add Phase 2 follow-up subagent runs to the queue when Brian has bandwidth.** From the four peer-track scope pages:
  - LBP track: P2-1 *F. prausnitzii* engineering toolkit lit scan, P2-2 commercial landscape lit scan, P2-3 FDA LBP regulatory path lit scan, P2-4 comp-008 *F. prausnitzii* expression feasibility, P2-5 H02 full population, P2-6 chassis comparative matrix
  - siRNA / URAT1 track: P2-1 kidney-tropic conjugate chemistry lit scan, P2-2 comp-009 URAT1 mRNA target site analysis, P2-3 commercial landscape lit scan, P2-4 vs. pozdeutinurad comparative analysis, P2-5 H03 full population, P2-6 FDA siRNA regulatory path lit scan
  - TCM × rigor track: P2-1 classical TCM gout formulas lit scan (multilingual: ChiCTR + CNKI + J-STAGE), P2-2 comp-011 ChEMBL cross-check of TCM gout compounds, P2-3 Smilax glabra deep-dive, P2-4 Si Miao San decomposition, P2-5 H04 full population, P2-6 bioavailability characterization
  - Engineered LBP H02 + siRNA H03 + TCM H04 falsification card stubs all need full population
- **[Standing] Run /sweep-status before declaring inbox-zero at end of any working session.** Don't rely on memory of "did I push everything?" — the registry is authoritative.

## Sweep daemon / workflow

- **[2026-05-05 — RESOLVED in commit `5199aba`]** Pass 3 token-budget bug. Failure mode was 1.02M cumulative prompt > 1M Opus cap. Fixed by lowering `build_evidence_context` char_budget (2.8M → 1.4M) + adding cumulative-loop size guard. End-to-end success on commit `487fad3` (Pass 1 + Pass 2 + Pass 3 all landed cleanly).
- **[2026-05-05 — RESOLVED in commit `dd66e56`]** Pass 2 model swap to DeepSeek V4-Pro primary + Gemini 2.5 Pro fallback. Verified context fits (611K corpus < 1M cap). End-to-end success on commit `487fad3`.
- **[Open] Verify the Pass 2 prompt enhancements (Phase A enumerate / B map / C synthesize + chain-depth tagging + Phase-A-match self-tag) actually reduce duplicates in production.** First test landed in commit `487fad3` Pass 2 output — read the synthesis log and assess whether duplicates dropped vs. the 2026-04-28 / earlier 2026-05-05 baseline.
- **[Open] Verify the Pass 3 [OVERLAP: NOVEL/EXTENSION/RESTATEMENT] tagging works in production.** First test in commit `487fad3` Pass 3 output — read the review blockquotes and assess whether the tags are being applied, used consistently, and adding signal.
- **[Standing] Pass 3 file-inlining smarter prioritization.** Currently inlines trigger files first (always), then cited files until budget. Could be sharper — e.g., prioritize cited files by citation count in the synthesis log, or by recency of the wiki page edit. Low priority unless we hit another budget overrun.

## Self-experiment / personal-protocol items

Operational notes about Brian's personal n=1 experimentation cadence and framework decisions. The research-grade content (the framework itself, the rigor discipline) lives in `wiki/self-experiment-protocol.md`. Cadence reminders and framework-decision logs live here.

**Content that's fine here (operational, framework-level, no PHI):** "consider the §11.1 add-on at next quarterly draw," "review the rigor framework before next quarter's panel cycle." **Content that does NOT go here (PHI per umbrella privacy boundary):** specific lab values, specific clinical-decision data, dated/identifiable medical event logs. Those belong in private sibling repos. The boundary is content-sensitivity, not folder-name; same rule applies in `wiki/` and everywhere else in this repo.

- **[Standing] Quarterly blood panel cadence.** Operational reminder — the rigor framework is in `wiki/self-experiment-protocol.md` §2–4.
- **[2026-05-05] Consider §11.1 ex vivo MSU PBMC challenge add-on at next quarterly draw.** Per the new self-experiment-protocol §11.1 add-on for androgen-elevated subjects. Decision is Brian's; this just surfaces the option.

---

## How to use this file

- Add new TODOs at the top of the appropriate category section with date stamp `[YYYY-MM-DD]`.
- Mark resolved with `[YYYY-MM-DD — RESOLVED in commit `<sha>`]` or similar; keep the entry for audit trail until the next major prune.
- For research-strategy reflections (Phase 3 platform-framing reframe, etc.) → `wiki/synthesis.md` Strategic Reflections Queue, NOT here.
- For Phase 2 queued lit scans + comp-NNN follow-ups that ARE research → already tracked in scope pages' Open Follow-Ups; the entry here is just a reminder to run them.
