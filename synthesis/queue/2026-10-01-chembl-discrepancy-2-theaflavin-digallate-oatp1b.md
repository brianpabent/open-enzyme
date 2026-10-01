---
type: chembl-discrepancy
quarter: 2026-Q4
sweep_date: 2026-10-01
compound: Theaflavin-3,3'-digallate (TF3)
chembl_id: CHEMBL434864
wiki_claim: "Theaflavins.md covers renal transporter expression changes (URAT1↓, GLUT9↓, OAT1↑, OCTN1↑, OAT2↑, ABCG2↑) and intestinal ABCG2 substrate data; hepatic transporters are not discussed."
chembl_curated: "Four pChEMBL records for TF3, all against hepatic uptake transporters from CHEMBL3039007: OATP1B1 Ki pChEMBL 5.82 (~1.5 μM), OATP1B1 IC50 pChEMBL 5.56; OATP1B3 Ki pChEMBL 5.47 (~3.4 μM), OATP1B3 IC50 pChEMBL 5.35."
epistemic_status: evidence-update
---

# ChEMBL discrepancy — Theaflavin-3,3'-digallate (TF3) at OATP1B1/OATP1B3

The ChEMBL bioactivity profile for theaflavin-3,3'-digallate (TF3, CHEMBL434864) contains four pChEMBL-bearing records, all from a single study (CHEMBL3039007), against two hepatic sinusoidal uptake transporters: OATP1B1 (SLCO1B1) Ki pChEMBL 5.82 (~1.5 μM), OATP1B1 IC50 pChEMBL 5.56 (~2.8 μM); OATP1B3 (SLCO1B3) Ki pChEMBL 5.47 (~3.4 μM), OATP1B3 IC50 pChEMBL 5.35 (~4.5 μM). These are hepatic sinusoidal import transporters responsible for the liver uptake of a broad range of organic anions, including statins (notably rosuvastatin and atorvastatin), methotrexate, and, importantly for gout, benzbromarone and possibly other uricosuric agents.

The wiki page for theaflavins (`wiki/theaflavins.md`) discusses the renal-transporter expression profile (URAT1↓, GLUT9↓, OAT1↑, Oct1/2↑) and intestinal ABCG2 substrate and induction data in detail, but does not mention OATP1B1 or OATP1B3. These hepatic transporters are mechanistically distinct from the renal secretion and NLRP3 pathways the page emphasizes. At ~1.5–4.5 μM, inhibition of OATP1B1/1B3 by TF3 is plausible at concentrated tea-extract exposures, though portal vein concentrations of intact TF3 after oral dosing are not established and TF3 undergoes rapid metabolism. The most direct clinical risk would be drug-drug interactions in any protocol that co-administers TF3-containing extracts with OATP1B1/1B3 substrates.

## Suggested action

1. Retrieve and verify the primary paper behind CHEMBL3039007: confirm that TF3 (not a catechin contaminant) was tested, confirm the inhibitor concentration range and Ki methodology, and note the assay system (vesicle, hepatocyte, transfected cell).
2. If confirmed at ~1.5–4.5 μM TF3 free concentration, add a brief safety-interaction note to `wiki/theaflavins.md` under the safety-interaction section, flagging hepatic OATP1B1/1B3 inhibition as an in-vitro signal and noting that portal-vein free-TF3 exposure after oral dosing has not been established — **(In Vitro)** evidence.
3. Cross-reference with the safety-interaction table in `wiki/supplements-stack.md` if the hepatic-DDI signal is confirmed at concentrations achievable in vivo.
4. If the primary-source retrieval does not reproduce the Ki values or attributes them to a different compound, note the mismatch and do not add the wiki claim.
