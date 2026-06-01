---
type: open-question
sweep_date: 2026-05-30
sweep_sha: 0317c56
section_index: 5
global_index: 12
pass3_verdict: unknown
overlap_tag: RESTATEMENT
---

# Does the proline-rigidification strategy generalize to other secreted OE payloads with structured-mandatory-connector-type linker vulnerabilities?

5. **Does the proline-rigidification strategy generalize to other secreted OE payloads with structured-mandatory-connector-type linker vulnerabilities?** (Lactoferrin inter-lobe linker redesign pilot, comp-034.) (source: lactoferrin-linker-redesign-computational.md)

> **Claude review — Push back.** `[OVERLAP: RESTATEMENT]` `[GAP: tool-gap]` This open question is outdated against its own cited source: `lactoferrin-linker-redesign-computational.md` says the 2026-05-30 Rosetta/SASA analysis found proline-rigidification **self-defeating on lactoferrin itself**, with MPNN `NEEEQQQEEEQ` winning by preserving the helix. The question should be rewritten as whether “strip protease-preferred residues while preserving protective secondary structure” generalizes; asking whether proline-rigidification generalizes preserves the pre-2026-05-30 error.

---

## ✓ Actioned 2026-06-01

**Pass 3's push-back was correct** — and doing the work found the same internal-inconsistency root cause as Item 7. The synthesizer (Grok) restated the outdated "does *proline-rigidification* generalize?" framing, which comp-034's own 2026-05-30 physics analysis (Rosetta ΔΔG + structure-gated cleavage) had already overturned: proline-rigidification is **self-defeating** on lactoferrin's structured α-helical inter-lobe linker (destabilizes fold +20 to +57 REU, breaks the protective helix, only −3% to −17% cleavage benefit). The winning redesign is helix-preserving charge/polar substitution (`NEEEQQQEEEQ`, ΔΔG ≈ 0, −66% cleavage).

**Why Grok restated the stale framing:** [`lactoferrin-linker-redesign-computational.md`](../../wiki/lactoferrin-linker-redesign-computational.md) already carried the 2026-05-30 correction at its line-96 ⚠ note, but the **section header + intro (lines 79, 81)** still framed the question as "does proline-rigidification generalize?" — page contradicts itself (stale top, corrected bottom), Grok read the top. Same root cause as Item 7 (stale §1.25 cost vs re-scoped header).

**Fix:** re-scoped the comp-034 open-follow-up **header + intro** to the corrected generalization question — "**strip protease-preferred residues while preserving the protective secondary structure**" — with an explicit note on the inversion (proline-rigidification self-defeating on a structured helix; may only suit genuinely flexible/loop connectors). Candidate-class definition + the DAF-not-the-exemplar correction left intact. Verified the outdated framing was **not** in open-questions.md (only the chaperone α-coefficient generalization question is there), so the fix is contained to this page.
