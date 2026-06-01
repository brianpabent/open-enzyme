---
type: contradiction
sweep_date: 2026-05-30
sweep_sha: 0317c56
section_index: 1
global_index: 4
pass3_verdict: unknown
overlap_tag: EXTENSION
---

# EGCG in vivo phenotype (PMID 38757391) contradicts its in vitro ABCG2 inhibition profile.

1. **EGCG in vivo phenotype (PMID 38757391) contradicts its in vitro ABCG2 inhibition profile.** Locations: egcg.md §"Gout-specific evidence" (Yu 2024 favorable ABCG2/URAT1/GLUT9 in hyperuricemic mice) vs. abcg2-modulators.md §"Supplements-stack contradiction" (established BCRP inhibitor at supplement doses). Analysis: The in vivo net-favorable effect on gut urate sink (despite in vitro functional inhibition) suggests dose- and chronicity-dependent behavior — acute gut-lumen concentrations inhibit transport, but chronic exposure may upregulate ABCG2 transcription via Nrf2. This is the canonical case of "in vitro pharmacology vs. animal-model phenotype" that the query-framing retrospective audit (2026-05-19) warned about. Pass 3 should not resolve the contradiction — it is a real open question for the platform.

> **Claude review — Confirmed.** `[OVERLAP: EXTENSION]` This is a real contradiction in the corpus: `egcg.md` cites Yu 2024 PMID 38757391 for favorable in vivo urate-transporter phenotype in hyperuricemic mice, while `abcg2-modulators.md` flags EGCG as a functional BCRP/ABCG2 inhibitor in vitro and explicitly says the net gut-sink effect is unresolved. The proposed chronic-transcriptional-upregulation vs acute-functional-inhibition explanation is plausible but should remain hypothesis, not resolution.

---

## ✓ Actioned 2026-06-01

**Contradiction already canonical** (anchored to primary sources Yu 2024 PMID 38757391 + pharmacology literature, not corpus-absence): documented at [`egcg.md` line 77](../../wiki/egcg.md) (with cross-link + evidence tiers), and [`abcg2-modulators.md` §"The supplements-stack contradiction"](../../wiki/abcg2-modulators.md) — EGCG row in the inhibitor table (in-vitro vs in-vivo flagged), the risk-tier stratification table, and open-question #4 with a resolution path (direct in vivo gut-ABCG2 measurement). Pass 3 verdict *Confirmed* — kept unresolved as hypothesis per its guidance.

**Value-add from this walk (do the work): the EGCG paradox is now a two-compound class pattern.** Item 1's lit scan established that theaflavins follow the same in-vitro-inhibition / in-vivo-ABCG2↑ split (Tai 2020, Nrf2/HO-1). Added a note to [`abcg2-modulators.md` §"The supplements-stack contradiction"](../../wiki/abcg2-modulators.md) framing EGCG + theaflavins as a candidate **hormetic, Nrf2-driven ABCG2 up-regulation** class pattern under chronic exposure — same mechanism as the corpus-documented inducer sulforaphane — while explicitly keeping it a hypothesis (rodent, transcript-level, mechanism inferred; acute high-dose inhibition still real). Added reciprocal cross-link from [`theaflavins.md` §2](../../wiki/theaflavins.md).

This is an EXTENSION that emerged from doing the work in Item 1 — it sharpens the chronic-vs-acute hypothesis from speculation-about-one-compound to a class pattern with two independent examples, without resolving the contradiction.
