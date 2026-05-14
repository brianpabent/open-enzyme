---
type: connection
sweep_date: 2026-05-09
sweep_sha: 259a8e8
section_index: 3
global_index: 3
pass3_verdict: Confirmed
overlap_tag: EXTENSION
---

# The personal-genome protocol unlocks genotype-personalized T-axis adjuvant selection within the androgen-elevated stack path.

3. **The personal-genome protocol unlocks genotype-personalized T-axis adjuvant selection within the androgen-elevated stack path.** *Speculative*. `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* `personal-genome-protocol.md`, `t-axis-adjuvant-urate-mapping-computational.md`, `androgen-natural-modulation.md`
   - *Page-pair linkage:* Weak. `personal-genome-protocol` identifies ABCG2, URAT1, and HLA-B*58:01 as pharmacogenomic targets but does not mention T-axis adjuvants at all. `t-axis-adjuvant-urate-mapping` (comp-015 v2) ranks cordycepin and eurycomanone as gout-favorable but does not connect genotype to selection. No page in the wiki currently suggests that a Q141K-positive, androgen-elevated user might differentially benefit from eurycomanone’s multi-target transporter modulation over cordycepin’s URAT1-only mechanism.
   - *Why It Matters:* The androgen-elevated path (`gout-action-guide.md`) recommends both cordycepin and eurycomanone as parallel options without genotype-based guidance. If personal genome sequencing becomes load-bearing (per `personal-genome-protocol`), it could be used to **select the optimal T-axis adjuvant** rather than trial them sequentially. A Q141K homozygote on TRT, for example, has both compromised ABCG2 and elevated URAT1 — eurycomanone’s dual ABCG2-up + URAT1-down mechanism may be a better match than cordycepin’s URAT1-only pathway. This is a natural extension of the “precision countermeasure” framing already used for carnosine in the koji endgame strain.
   - *Suggested Action:* Add a subsection to `personal-genome-protocol.md` linking Q141K / URAT1 variants to T-axis adjuvant selection. Queue a future comp-NNN that stratifies the comp-015 v2 candidate panel by known sex-hormone–transporter genotypes (ABCG2 Q141K, SLC22A12, SLC2A9). In-silico only.

> **Pass 3 review — Confirmed.** `[OVERLAP: EXTENSION]` This survives scrutiny: `personal-genome-protocol.md` lists ABCG2 Q141K, SLC2A9, SLC22A12/URAT1, and HLA-B*58:01 as gout-relevant pharmacogenomic queries but does not tie those variants to T-axis adjuvant choice, while `t-axis-adjuvant-urate-mapping-computational.md` distinguishes cordycepin’s URAT1-dominant favorable profile from eurycomanone/eurycomanol’s multi-target transporter + PRPS profile. Keep the recommendation explicitly speculative: the eurycomanone ABCG2-up / URAT1-down evidence is animal/in-vitro/RCT-adjacent and not Q141K-genotype-stratified.

---

## ✓ Actioned 2026-05-14

Added new `## Genotype-stratified T-axis adjuvant selection (speculative)` section to [`wiki/personal-genome-protocol.md`](../../wiki/personal-genome-protocol.md). The section ties ABCG2 Q141K, SLC22A12 (URAT1), and SLC2A9 (GLUT9) variants to cordycepin (URAT1-dominant) vs eurycomanone (multi-target transporter + PRPS) selection, with a four-row genotype × bottleneck × prediction table. Framed explicitly as hypothesis-generation, not clinical selection rule, per Pass 3's speculation guardrail. Added bidirectional cross-link from [`wiki/t-axis-adjuvant-urate-mapping-computational.md`](../../wiki/t-axis-adjuvant-urate-mapping-computational.md) §Cross-references.

Future comp candidate flagged inline: genotype-stratified scoring of the comp-015 v2 panel (cordycepin, eurycomanone, icariin, echinacoside) by ABCG2 Q141K / URAT1 / SLC2A9. Not queued in computational-experiments.md yet; sits as a documented next step in the new section.

Closes alongside [2026-05-09-priority-action-3](./2026-05-09-priority-action-3-integrate-the-personal-genome-protocol-with-the-androgen.md) (same action).
