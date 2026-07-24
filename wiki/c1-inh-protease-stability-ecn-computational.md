---
title: "C1-INH EcN Construct Question (comp-037 retired)"
date: 2026-05-17
tags: [complement, C1-INH, SERPING1, protease, EcN, LBP, computational, CP0]
related:
  - complement-c5a-gout.md
  - engineered-lbp-chassis.md
  - computational-experiments.md
  - validation-experiments.md
sources:
  - "UniProt P05155 (human SERPING1 / C1-INH)"
  - "Bos 1998 PMID 9799502"
  - "Stavenhagen 2018 PMID 29381136"
status: retired-invalid-model; exact-construct function unresolved
---

# C1-INH EcN Construct Question

C1-INH could exploit upstream complement initiation by inhibiting C1r, C1s, and MASP proteases, but an exact EcN-produced material must first be shown to attain its native serpin function and retain that function under the intended exposure conditions. COMP-037 does not answer that question.

The [COMP-037 tombstone](./etc/experiments/comp-037-c1-inh-protease-stability-ecn/) is non-runnable. Its pLDDT-as-accessibility mapping, sequence-filter scores, risk colors, cleavage and survival claims, glycosylation-feasibility verdict, construct preference, EcN assignment, and cross-payload conclusions are invalid. Git retains the historical implementation; no numerical proxy output is current evidence.

What remains source-backed:

- UniProt P05155 annotates the C1-INH reactive region and two intrachain disulfides. These are sequence features, not evidence that an EcN product folds, survives, or inhibits its targets.
- Native C1-INH is glycosylated (**In Vitro**; PMID 9799502 and PMID 29381136). Those records do not establish whether a particular unglycosylated bacterial product retains useful function.
- Productive target engagement and unproductive cleavage at or near a serpin reactive-center loop are distinct kinetic outcomes (**Mechanistic Extrapolation**; source: the P05155 annotation and established serpin mechanism). Their competition has not been measured for an EcN-produced C1-INH configuration.

> **Research conjecture — productive inhibition may outcompete cleavage in an exact EcN configuration**{ .research-conjecture-label }
>
> **Grounded premises:** C1-INH uses a reactive-center serpin mechanism and is natively glycosylated (**In Vitro / Mechanistic Extrapolation**; sources: [UniProt P05155](https://www.uniprot.org/uniprotkb/P05155/entry), PMID 9799502, and PMID 29381136). Exact EcN-produced C1-INH materials have not been shown here to attain native fold or retained C1r, C1s, and MASP inhibition.
>
> **Novel leap:** An exact EcN-produced C1-INH configuration may retain enough native serpin function for productive target engagement to outcompete unproductive cleavage under the intended exposure. No direct evidence establishes this for an EcN-produced C1-INH configuration.
>
> **Why it matters:** A positive configuration-level result would preserve an upstream-complement payload without declaring EcN, C1-INH, or a multi-payload architecture generally viable.
>
> **Discriminating observation:** For each prespecified construct × export route × folding-support configuration, measure product identity, intact recovery, native fold or validated structural-function readout, disulfide state, concentration-dependent inhibition of C1r/C1s/MASP-2, matched protease-challenge cleavage, and retained inhibition after challenge. Advance only the exact configuration that passes prespecified quality and kinetic gates.

A negative result kills only the tested construct × route × support × exposure condition. It does not reject upstream complement inhibition or another production chassis. Access, delivery, safety, and portfolio ranking remain separate questions.

Related: [complement portfolio](./complement-c5a-gout.md) · [engineered LBP chassis](./engineered-lbp-chassis.md) · [COMP registry](./computational-experiments.md)
