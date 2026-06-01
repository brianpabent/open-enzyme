---
type: connection
sweep_date: 2026-05-30
sweep_sha: 0317c56
section_index: 1
global_index: 1
pass3_verdict: unknown
overlap_tag: EXTENSION
---

# Theaflavins and EGCG are mechanistically orthogonal at NLRP3 but both antagonize the gut-lumen sink via ABCG2 inhibition.

1. **Theaflavins and EGCG are mechanistically orthogonal at NLRP3 but both antagonize the gut-lumen sink via ABCG2 inhibition.** *Supported*. `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: no]`  
   - *Documents Connected:* theaflavins.md, egcg.md, abcg2-modulators.md, nlrp3-exploit-map.md  
   - *Page-pair linkage:* Weakly connected pair — theaflavins and EGCG both appear in nlrp3-inhibitor-screen.md and supplements-stack.md, but theaflavins.md (added 2026-05-05) and egcg.md (updated same sweep) have never been cross-referenced on ABCG2 antagonism; abcg2-modulators.md discusses EGCG but not theaflavins.  
   - *Why It Matters:* Chen 2023 (PMID 37221235) shows theaflavins disrupt NLRP3-NEK7 downstream of ROS (CP2/CP3), distinct from EGCG's proteasome-mediated IκB stabilization (CP1a, 86 nM IC50 per ChEMBL v34). This orthogonality is additive at the inflammasome level. However, both are functional ABCG2 inhibitors at supplement doses (quercetin/curcumin/EGCG/genistein listed in abcg2-modulators.md §"Supplements-stack contradiction"; theaflavins share the tannin-class inhibition profile). In androgen-dominant or Q141K-positive patients (the platform's primary demographic), high-dose layering of either risks closing the gut urate sink that engineered uricase depends on. The net in vivo effect of EGCG on ABCG2/URAT1/GLUT9 is unresolved (Yu 2024 PMID 38757391 shows favorable phenotype despite in vitro inhibition). This elevates the "stack-level contradictions" section of abcg2-modulators.md from footnote to first-class topic and forces genotype-aware dosing when using theaflavins or EGCG.  
   - *Suggested Action:* Add theaflavins to abcg2-modulators.md §"Supplements-stack contradiction" with the same risk-tier table used for EGCG/quercetin. Update supplements-stack.md to include theaflavins entry with explicit ABCG2 warning. Flag in open-questions.md as "theaflavins/EGCG × ABCG2 in vivo resolution needed."

> **Claude review — Push back.** `[OVERLAP: EXTENSION]` `[GAP: tool-gap]` The NLRP3 orthogonality is real — `theaflavins.md` cites Chen 2023 PMID 37221235 for MSU-stimulated macrophages, ASC/caspase-1/GSDMD suppression, and NLRP3-NEK7 disruption — but the ABCG2 claim is unsupported and contradicted by the wiki: `theaflavins.md` explicitly says “No ABCG2 interaction documented” in its stack-interactions section, and `abcg2-modulators.md` lists EGCG/quercetin/curcumin/genistein, not theaflavins, as functional ABCG2 inhibitors. Do not add theaflavins to the ABCG2-inhibitor warning table without a primary transporter assay; the correct action is to add an open question for theaflavin × ABCG2, not a risk-tier entry.

---

## ✓ Actioned 2026-06-01

**NLRP3 orthogonality:** confirmed and already canonical in [`theaflavins.md` §Stack interactions](../../wiki/theaflavins.md) (EGCG → proteasome 86 nM / CP1a; theaflavins → NEK7-NLRP3 assembly disruption / CP2-CP3; additive). No new work needed.

**ABCG2 claim: rejected after lit scan — the synthesizer claim was inverted.** Pass 3 correctly pushed back that the "theaflavins share the tannin-class ABCG2-inhibition profile" claim was unsupported in the corpus. A multilingual lit scan (2026-06-01, Opus subagent; English + Chinese CNKI/WanFang, 茶黄素 × ABCG2/尿酸转运体) went further and found the claim is **contradicted**:
- Theaflavins are ABCG2/BCRP **substrates**, not inhibitors (Caco-2, PMC8409943) — a bioavailability phenomenon, not transport inhibition.
- In vivo (Tai 2020, *J Funct Foods* 66:103803; potassium-oxonate hyperuricemic mice) theaflavins **up-regulate** ABCG2 (gene-level) and lower serum urate — the platform-*favorable* direction (they open the gut sink, not close it).
- No ChEMBL bioactivity record; no transporter-inhibition assay anywhere.

**Edit landed:** added the Tai 2020 ABCG2↑ secretory-transporter arm to [`theaflavins.md` §2](../../wiki/theaflavins.md) (Animal tier, transcript-level caveat) plus a boxed note documenting substrate-not-inhibitor status and explicitly instructing future sweeps not to add an ABCG2-inhibitor warning. This closes a real gap (the page cited Tai-adjacent transporter data but missed the ABCG2 arm) and pre-empts re-hallucination.

**No warning table added to `abcg2-modulators.md`** — correct disposition per evidence.

**Resolves Item 18** (priority-action-1, "promote theaflavins to supplements-stack.md with explicit ABCG2 warning") — the ABCG2-warning premise is rejected; will close Item 18 as pre-resolved when reached, with a note on whether the NLRP3/URAT1 supplement-stack promotion is worth doing on its own merits.

**Calibration note (first Grok-4.20 Pass-2 sweep):** this confident pharmacology claim was a class-analogy extrapolation that got the *sign* wrong. Pass 3 (GPT-5.5) caught "unsupported" but lacked the in-vivo data to catch "inverted." Flag for skepticism on other Grok class-extrapolation claims this round.
