---
type: open-question
sweep_date: 2026-05-15
sweep_sha: 8653de9
section_index: 1
global_index: 10
pass3_verdict: Confirmed
overlap_tag: RESTATEMENT
---

# What is the quantitative relationship between dietary rosmarinic acid intake (from rosemary, lemon balm, spearmint) and gut-luminal + plasma rosmarinic acid concentrations?

1. **What is the quantitative relationship between dietary rosmarinic acid intake (from rosemary, lemon balm, spearmint) and gut-luminal + plasma rosmarinic acid concentrations?** The comp-020 verification re-run documented a 44× IC50 spread across assay formats (34 μM → 1,500 μM), and dietary bioavailability is unresolved. Without a pharmacokinetic anchor, the "dietary CP0 coverage" claim is mechanistically grounded but quantitatively unanchored. A human PK study of rosmarinic acid from dietary sources (single-dose, n=6–12, plasma + urine sampling over 24h) would cost ~$15,000–25,000 and resolve the question. Until then, the dietary rosmarinic acid thread should carry an explicit "PK unresolved" caveat.

> **Pass 3 review — Confirmed.** `[OVERLAP: RESTATEMENT]` The PK caveat is already the central limiting uncertainty for dietary rosmarinic-acid CP0 coverage: `complement-c5a-gout.md` §9.7 and `upstream-complement-verification-rerun-computational.md` both carry the ~34 µM / 44× assay-format-spread caveat and explicitly avoid a dietary effect-size claim. The open question is worth keeping visible until comp-021/comp-029 or a human PK study anchors achievable gut-luminal and plasma concentrations.

---

## ✓ Actioned 2026-05-16

Added to [`wiki/open-questions.md`](../../wiki/open-questions.md) as a tracked entry under the existing "comp-018 Phase 2 follow-ups" section. Names the load-bearing PK question, the 44× IC50 spread documented in comp-020, the partial resolution by comp-029 (which consumed the uncertainty as input distribution and produced YELLOW combined-CP0 verdict — Spearman r = −0.658 for IC50 was the dominant sensitivity driver), and the resolution path (human PK study, n=6–12, ~$15–25K, partner/clinical-tier work).

No new wiki page. No new comp-NNN (human PK study requires human subjects + clinical sampling, not in silico). §9.7 already carries the canonical caveat; open-questions.md is the tracking surface.
