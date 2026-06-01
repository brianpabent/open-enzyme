---
type: priority-action
sweep_date: 2026-05-30
sweep_sha: 0317c56
section_index: 1
global_index: 18
pass3_verdict: unknown
overlap_tag: EXTENSION
---

# Promote theaflavins to supplements-stack.md with explicit ABCG2 warning.

1. **Promote theaflavins to supplements-stack.md with explicit ABCG2 warning.** (1-2 lines on what + why: theaflavins are mechanism-orthogonal to EGCG at NLRP3 but share the functional ABCG2 inhibition profile; add the same risk-tier table used for EGCG/quercetin.)

> **Claude review — Push back.** `[OVERLAP: EXTENSION]` `[GAP: tool-gap]` The action is not evidence-supported as written: `theaflavins.md` says no ABCG2 interaction is documented, while the ABCG2 warning table in `abcg2-modulators.md` covers EGCG/quercetin/curcumin/genistein. Promote theaflavins to the supplement stack for NLRP3/URAT1/GLUT9 evidence if desired, but do not attach an ABCG2-inhibitor warning until a theaflavin-specific BCRP assay exists.

---

## ✓ Actioned 2026-06-01

Priority action pre-resolved by Item 1 + a consistency-propagation edit:

- **"Promote theaflavins to supplements-stack.md"** — already done since 2026-05-05: [`supplements-stack.md` §227](../../wiki/supplements-stack.md) is a full entry (NLRP3-NEK7 mechanism, URAT1/GLUT9 transporter angle, Chen 2023 MSU peritonitis evidence, dosing, stack interactions). No promotion work needed.
- **"with explicit ABCG2 warning"** — **rejected** (Item 1, connection-1 / Pass 3 push-back upheld): theaflavins do not inhibit ABCG2; the multilingual lit scan showed they are ABCG2 *substrates* and in-vivo *up-regulators* (Tai 2020), platform-favorable. No warning added.

**Did the work — propagated the Item 1 finding to the third page.** [`supplements-stack.md` §227 line 261](../../wiki/supplements-stack.md) previously said "a direct theaflavin-on-ABCG2 study has not been done" — stale against Item 1's scan, which found Tai 2020 (in vivo ABCG2↑) + the Caco-2 substrate study. Updated it to the correct framing (substrate + favorable in-vivo up-regulator, hormetic Nrf2-inducer bucket, not inhibitor), consistent with the theaflavins.md §2 and abcg2-modulators class-pattern notes added in Items 1/4. All three theaflavins×ABCG2 surfaces now consistent.

**Process:** one of the three priority-action items already in this queue (the section is retired for future sweeps; these three still get walked + closed).
