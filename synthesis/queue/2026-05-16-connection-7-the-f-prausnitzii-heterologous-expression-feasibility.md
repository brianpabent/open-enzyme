---
type: connection
sweep_date: 2026-05-16
sweep_sha: 3c1ca4b
section_index: 7
global_index: 7
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# The F. prausnitzii heterologous expression feasibility analysis (comp-008) sharpens the engineered-LBP-chassis payload strategy decisively: butyrate boost is the only GREEN payload, uricase is wrong for this chassis, and the engineering-toolkit gap is the gating constraint.

7. **The F. prausnitzii heterologous expression feasibility analysis (comp-008) sharpens the engineered-LBP-chassis payload strategy decisively: butyrate boost is the only GREEN payload, uricase is wrong for this chassis, and the engineering-toolkit gap is the gating constraint.** *Supported*. `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: no]`

   - *Documents Connected:* `f-prausnitzii-heterologous-expression-computational.md`, `engineered-lbp-chassis.md`, `uricase.md`, `chassis-pending-interventions.md`, `hypotheses/H02-engineered-lbp-thesis.md`

   - *Page-pair linkage:* **Weak.** `engineered-lbp-chassis.md` has a section on butyrate as the highest-leverage payload and lists candidate payloads including uricase, lactoferrin, and sCR1, but comp-008's per-payload composite scoring and the uricase-is-wrong-for-this-chassis finding are new. The scope page was written before comp-008 ran.

   - *Why It Matters:* comp-008 gives four payloads ranked composites with explicit limiting factors:

     1. **Butyrate-pathway boost (native BCoAT): 0.748 GREEN** — CAI = 1.0 (native gene), no secretion, no folding burden, native pathway alignment. The only GREEN payload at the base score and at the toolkit-conditional score (0.875 with toolkit gap excluded).
     2. **sCR1 SCR1-4 truncation: 0.565 YELLOW** — bottlenecked on engineering toolkit maturity + anoxic-environment disulfide folding.
     3. **Human lactoferrin: 0.540 YELLOW** — same bottleneck pattern as sCR1.
     4. ***A. flavus* uricase: 0.393 YELLOW-toward-RED** — the chemistry can't run: uricase uses O₂ as substrate, and F. prausnitzii is an obligate anaerobe in an anoxic colonic lumen. Even with a perfect engineering toolkit, the enzyme's catalytic requirement is incompatible with the host's physiology.

     This is a strategic narrowing function: it tells the LBP-chassis track to **stop considering uricase for Fp** (route to EcN or koji instead), **focus Fp on butyrate boost as the near-term campaign**, and **defer lactoferrin/sCR1 to after the engineering toolkit is established**. It also sharpens the P2-6 (comparative chassis matrix) follow-up: Fp should be benchmarked for butyrate boost against *E. coli* Nissle (facultative anaerobe, mature toolkit, already used in PULSE) — the engineering-toolkit penalty of 0.25 across all Fp payloads may make EcN the faster path even for butyrate, which EcN natively produces at lower titers.

     The GC-match finding (human payloads ~58% GC vs Fp 56.6% — only 1.4 pp mismatch, best of any chassis in the LBP track) is a structural advantage of Fp for mammalian-origin payloads that partially offsets the toolkit penalty. If the toolkit gap closes (Sheridan 2019 Lachnospiraceae conjugation precedent adapted to Fp), Fp's codon-compatibility advantage makes it the preferred chassis for complex mammalian payloads.

   - *Suggested Action:* Update `engineered-lbp-chassis.md` to reflect comp-008's payload ranking: promote butyrate boost to primary near-term campaign, deprioritize uricase for the LBP chassis, and note the toolkit gap + anoxic disulfide folding as the gating constraints for lactoferrin/sCR1. Queue the P2-6 comparative chassis matrix follow-up with comp-008's composite scores as inputs.

   

---

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` `f-prausnitzii-heterologous-expression-computational.md` supports the ranking and the strategic narrowing: native BCoAT butyrate boost scores 0.748 GREEN, sCR1 and lactoferrin are YELLOW with disulfide/toolkit constraints, and *A. flavus* uricase scores 0.393 with host-physiology compatibility 0.1 because uricase requires O₂ and produces H₂O₂ in a strict anaerobe. The “uricase is wrong for Fp” conclusion is not chassis prejudice; it follows directly from enzyme chemistry and host physiology. This should update the LBP track’s payload menu and route uricase to EcN/koji while keeping Fp focused on butyrate first.
