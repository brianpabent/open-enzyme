---
type: open-question
sweep_date: 2026-07-01
sweep_sha: 18d3696
section_index: 1
global_index: 7
pass3_verdict: Confirmed
overlap_tag: NOVEL
---

# How does androgen status interact with BHB's NLRP3-inhibiting effect?

1. **How does androgen status interact with BHB's NLRP3-inhibiting effect?** `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: no]`
   - *Context:* `bhb-ketones.md` documents BHB as a multi-target NLRP3 inhibitor. `androgen-urate-axis.md` documents that androgens have direct but directionally ambiguous effects on NLRP3 priming (anti-inflammatory in general, but pro-inflammatory in cardiac macrophages). The effect in gout-relevant synovial macrophages is unknown. This is a critical gap for the platform's primary demographic (males, often with managed testosterone levels).
   - *Question:* In androgen-elevated individuals, is the required dose of BHB for effective NLRP3 suppression higher, lower, or the same as in baseline individuals? Could the two be synergistic or antagonistic?
   - *Path to resolution:* Extend the proposed experiment in `validation-experiments.md` §1.23 (Androgen x MSU x NLRP3) to include a BHB treatment arm. This would allow for characterization of the three-way interaction between androgen levels, MSU crystal stimulation, and BHB-mediated NLRP3 inhibition in a controlled in vitro system.

> **Pass 3 review — Confirmed.** `[OVERLAP: NOVEL]` This is a well-framed open question. `bhb-ketones.md` documents BHB as a multi-target NLRP3 inhibitor (CP1/CP2/CP4) and `androgen-urate-axis.md` §"Beyond transporters: direct androgen effects on NLRP3 priming" documents directionally ambiguous androgen effects on NLRP3 — anti-inflammatory in most macrophage types, pro-inflammatory in cardiac macrophages, and genuinely unknown in gout-relevant synovial macrophages. The three-way interaction (androgen × MSU × BHB) is untested, and the path to resolution — extend `validation-experiments.md` §1.23 to include a BHB treatment arm — is the lowest-cost experiment that could answer it. One note: the question implicitly assumes BHB's NLRP3 effect is independent of androgen status, but BHB acts partly via HCAR2/GPR109A signaling, and androgen receptor signaling can cross-modulate GPCR expression. Whether HCAR2 expression in macrophages is androgen-sensitive is itself an open sub-question worth flagging. Minor addition, not a correction.

---

## ✓ Actioned 2026-07-13

Added a **BHB interaction arm** to [`validation-experiments.md` §1.23](../../wiki/validation-experiments.md) (androgen × MSU × NLRP3) — a ± DHT × ± BHB × MSU block at Tier 1, near-zero marginal cost, testing whether BHB's NLRP3 suppression is androgen-dependent, plus an **HCAR2/GPR109A qPCR readout** across the DHT conditions (Pass-3's sub-question). Logged the open question (with the HCAR2 sub-question) in [`open-questions.md`](../../wiki/open-questions.md) §"BHB / Ketones". Cheapest way to make the three-way interaction testable; strengthens an experiment already on the docket.
