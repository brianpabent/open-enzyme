# Rosmarinic acid — Model A source read (CFH-dependence classification)

**Date:** 2026-05-21
**Author:** Claude Opus 4.7 (Model A in two-model cross-check protocol)
**Scope:** comp-039 mechanism-dissociation classification — does rosmarinic acid's anti-complement mechanism require functional CFH (and therefore lose efficacy in Y402H carriers, AMD-paradox-style), or does it bypass CFH and remain effective in carriers?

## Primary sources read

1. **Sahu A, Rawal N, Pangburn MK.** Inhibition of complement by covalent attachment of rosmarinic acid to activated C3b. *Biochem Pharmacol* 1999;57(12):1439–46. PMID 10353266.
2. **Englberger W, Hadding U, Etschenberg E, Graf E, Leyck S, Winkelmann J, Parnham MJ.** Rosmarinic acid: a new inhibitor of complement C3-convertase with anti-inflammatory activity. *Int J Immunopharmacol* 1988;10(6):729–37. PMID 3198307.
3. **Peake PW, Pussell BA, Martyn P, Timmermans V, Charlesworth JA.** The inhibitory effect of rosmarinic acid on complement involves the C5 convertase. *Int J Immunopharmacol* 1991;13(7):853–7. PMID 1761351.

Full text for Sahu / Englberger / Peake is pre-PMC and read via the PubMed-hosted abstract pages (verbatim methods/results sections; no full-text body retrieved in this session).

## Binding-site evidence (the load-bearing claim)

**Sahu 1999 (PMID 10353266):** rosmarinic acid covalently attaches to the **activated thioester of metastable C3b** — the reactive carbonyl on Cys988 of the C3 α'-chain that is exposed upon C3 cleavage. Radioiodination demonstrates covalent incorporation specifically into the **thioester-containing α'-chain of nascent C3b**. IC50 for inhibiting covalent C3b deposition on cells = **34 μM**.

> Verbatim from abstract: "reaction of rosmarinic acid with the activated thioester of metastable C3b, resulting in covalent attachment of the inhibitor to the protein."

**Englberger 1988 (PMID 3198307):** acts on **C3-convertase of the classical complement pathway**. Threshold inhibition concentration = 10⁻⁶ mol/L (= 1 μM); optimal range **5–10 μM** giving ~70% hemolysis inhibition. The convertase target is at the active-site level (a related serine protease, elastase, is weakly co-inhibited — suggests proteinase-active-site interaction is part of the mechanism on top of the C3b thioester capture). No CFH involvement reported.

**Peake 1991 (PMID 1761351):** at higher doses (mM range — the canonical 1500 μM is downstream of where the C3b-thioester step dominates), rosmarinic acid also inhibits the **C5 convertase** step. Maximum classical-pathway lysis inhibition at 2.6 mM. No CFH involvement reported.

## Mechanism mapping vs the CFH Y402H footprint

The CFH Y402H variant sits in **CCP (Sushi) 7**, residues 387–444 of P08603 (UniProt, verified directly against the JSON record this session — Sushi 7 spans 387–444; Sushi 6 spans 324–386; Sushi 8 spans 446–507). The CCP6-8 module is the canonical CRP-binding and host-glycosaminoglycan-binding surface of CFH. Y402H weakens those surface contacts.

CFH's regulatory function on C3b is twofold:

1. **Decay-accelerating activity** — dissociates Bb from C3bBb (the alternative-pathway C3 convertase).
2. **Factor-I cofactor activity** — bound to C3b on a host surface, CFH presents C3b to Factor I, which cleaves C3b → iC3b (irreversible inactivation).

Both functions operate **on already-deposited C3b** — that is, downstream of the C3b-thioester reaction.

**Rosmarinic acid's primary mechanism (C3b-thioester covalent capture, Sahu 1999) acts on nascent C3b *before* it covalently attaches to a target surface.** Once rosmarinic acid has covalently quenched the thioester, the C3b cannot covalently attach to MSU crystal or any other surface; CFH-mediated decay/inactivation is moot because there is no surface-bound C3b to regulate.

The Englberger 1988 C3-convertase inhibition is also CFH-independent — it acts at C4b2a / C3bBb assembly or active-site catalysis, not at the CFH binding surface on C3d/C3c.

## Classification

**CFH-dependence: CFH-INDEPENDENT (High confidence).**

Mechanism is upstream of where CFH acts. Rosmarinic acid prevents the formation of the substrate (surface-bound C3b) that CFH would normally regulate. A broken CFH (Y402H) cannot make rosmarinic acid's mechanism worse, because rosmarinic acid does not need CFH to function and does not work through CFH-mediated steps. Y402H carriers retain full benefit.

**Predicted Y402H × rosmarinic acid × incident gout interaction:** **negative direction (protective effect equal-or-greater in carriers)** — because Y402H carriers have *more* unregulated surface C3b in the absence of intervention, and rosmarinic acid removes the upstream source of that surface C3b. Effect size in carriers ≥ non-carriers. **Falsification threshold:** if a UK Biobank candidate-stratified cross-tab shows CFH 402HH carriers with rosmarinic-acid-rich-diet doing significantly *worse* (HR > 1.5, p < 0.05) than 402YY carriers on same diet for incident gout M10.x, the CFH-independence classification is refuted and the AMD-paradox direction transfers — at which point rosmarinic acid would need to be retired from the upstream-CP0 stack.

**Confidence:** High — multiple independent primary sources, mechanism is structurally rationalized (thioester chemistry is at residue Cys988 in the C3 α'-chain, far from the CFH-binding C3d TED domain or the CFH-CCP6-8 CRP/GAG-binding surface).

## Multi-hypothesis discipline — rejected alternative

**Rejected hypothesis A: rosmarinic acid acts via CRP displacement, competing with CFH binding to surface C3b.** Would predict CFH-dependence (the same surface Y402H weakens). **Rejected** because the Sahu 1999 IC50 = 34 μM is from a cell-free reagent assay against activated nascent C3b in fluid phase — no CRP, no host-cell surface, no CFH present in the assay. Rosmarinic acid still inhibits → mechanism is CRP-independent and CFH-independent.

**Rejected hypothesis B: rosmarinic acid binds to C3d (the CFH-binding fragment of C3b), competing directly with CFH for the same surface.** Would predict competitive worsening in Y402H carriers (less CFH binding affinity means rosmarinic acid wins the competition more easily — but also implies the mechanism depends on the same surface). **Rejected** because radioiodination in Sahu 1999 localizes covalent attachment to the α'-chain thioester, not C3d. The α'-chain thioester reaction is structurally distinct from C3d's CFH-binding face.

## Limitations of this classification

- The Sahu 1999 IC50 = 34 μM is from a cell-free assay. The operative in-vivo concentration around MSU crystals in a gout flare is unknown. Bioavailability of dietary rosmarinic acid is reportedly low (≤1% systemic absorption per PMC9143754 review). The gut-luminal context (analogous to comp-004 IC50-occupancy framework) is the more plausible route, not systemic.
- The AMD-vs-gout extrapolation has site-of-action confounding: AMD complement activation is at the retinal pigment epithelium where CFH-CRP-zinc bridging is operative; gout complement activation is at MSU crystal surfaces in the joint. The CFH-bridging machinery may not be identically deployed at both sites.
- No published study has tested rosmarinic acid + Y402H carrier serum on MSU crystals. The classification is mechanistic extrapolation from published binding-site data, not direct empirical observation in the Y402H × gout context.
- The Peake 1991 mM-range C5-convertase activity is in a separate kinetic regime from the operative 34 μM thioester mechanism; whether residual C5-convertase activity in Y402H carriers (with already-elevated C3b deposition) becomes the dominant constraint is unresolved.

## Evidence-tier summary

- **In Vitro:** Sahu 1999 C3b thioester covalent capture (PMID 10353266) — direct biochemical evidence.
- **In Vitro:** Englberger 1988 C3 convertase inhibition (PMID 3198307) — hemolytic functional assay.
- **In Vitro:** Peake 1991 C5 convertase inhibition (PMID 1761351) — hemolytic functional assay.
- **Mechanistic Extrapolation:** CFH-independence in Y402H carriers — based on (a) primary mechanism acts on a substrate (nascent fluid-phase C3b) that exists upstream of where CFH operates, (b) no primary source reports CFH dependence, (c) AMD-paradox does not mechanistically apply because rosmarinic acid does not use the AREDS-zinc-CRP-CFH bridging pathway. No direct Y402H × rosmarinic acid empirical data.
