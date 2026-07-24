---
title: "Cassette Compatibility — Dual-Cassette Koji Multi-Payload Configuration (Computational, comp-010)"
date: 2026-05-05
tags:
  - computational
  - dual-cassette
  - uricase
  - lactoferrin
  - ward-1995
  - kex2
  - codon-usage
  - aspergillus-oryzae
  - cassette-design
  - endgame-strain
  - koji
related:
  - computational-experiments.md
  - validation-experiments.md
  - koji-endgame-strain.md
  - hypotheses/H01-ward-dual-cassette.md
  - uricase-protease-stability-computational.md
  - lactoferrin-protease-stability-computational.md
  - lactoferrin.md
  - uricase-variant-selection.md
sources:
  - "Ward PP, Piddington CS, Cunningham GA, Zhou X, Wyatt RD, Conneely OM. Biotechnology (N Y) 1995;13(5):498-503 (PMID 9634791)"
  - "Huynh HH, Morita N, Sakamoto T, et al. Fungal Biol Biotechnol 2020;7:7 (PMC7257131)"
  - "Rockwell NC, Krysan DJ, Komiyama T, Fuller RS. Chem Rev 2002;102(12):4525-48 (PMID 12475198)"
  - "Brenner C, Fuller RS. Proc Natl Acad Sci 1992;89:922-6 (PMID 1371243)"
  - "Almond MH et al. (2012) PMID 23012214 — fungal-glycan Lf immunogenicity"
  - "Sun XL, Baker HM, Shewry SC, Jameson GB, Baker EN. Acta Crystallogr D Biol Crystallogr 1999;55(Pt 2):403-7 (PMID 10089347)"
status: retired-invalid-model
---

# Cassette Compatibility — Dual-Cassette Koji Multi-Payload Configuration (Computational, comp-010)

The engineering weakness is a cassette that expresses poorly, is processed at an unintended junction, or routes the payload to the wrong compartment. COMP-010 does not establish whether the Q00511 plus P02788 configuration has any of those failures.

## Current evidence boundary

Ward 1995 supplies an *Aspergillus* secretion-architecture precedent (**In Vitro** production study). UniProt supplies the Q00511 and P02788 protein sequences. Neither source establishes expression, junction processing, secretion capacity, glycan state, or retained activity for the proposed dual-payload configuration.

The retired COMP-010 model inferred codon burden without an actual planned CDS, transferred KEX2-family preferences without an *A. oryzae* specificity matrix, double-offset glycosylation coordinates, and converted bulk sequence proxies into a LOW secretion-burden verdict. Its codon-collision, KEX2-cleavage certainty, glycosylation, competitive-capacity, overall-risk, and cross-payload conclusions are invalid. The [COMP-010 tombstone](./etc/experiments/comp-010-cassette-compatibility/) is non-runnable.

> **Research conjecture — exact junction geometry can dominate a nominally valid cassette**{ .research-conjecture-label }
>
> **Grounded premises:** The Ward architecture uses host processing to release a secreted payload (**In Vitro**; Ward 1995, PMID 9634791), while Q00511 and P02788 bring different sequences and folding requirements. The exact planned CDS, junctions, and produced termini have not been tested together.
>
> **Novel leap:** A construct that is acceptable by isolated sequence checks could still fail because one exact carrier–junction–payload combination changes processing or trafficking. No direct study has tested that failure mode in the proposed dual cassette.
>
> **Why it matters:** Junction-specific failure is engineerable and could be missed by aggregate burden scores.
>
> **Discriminating observation:** Build the exact single-cassette controls before the combined configuration; verify transcript, intact product, N- and C-termini, compartment, abundance, and retained activity with matched junction variants.

No result here selects a dual cassette, carrier, junction, tag, or chassis. Configuration testing belongs in [validation experiments](./validation-experiments.md) and the [H01 falsification card](./hypotheses/H01-ward-dual-cassette.md).
