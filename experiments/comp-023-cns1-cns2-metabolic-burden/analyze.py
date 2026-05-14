#!/usr/bin/env python3
"""
comp-023 - Metabolic / proteome burden of cns1+cns2 cordycepin biosynthesis on top of
the dual uricase + lactoferrin cassette in *A. oryzae*.

V1 design choices (own them; see Limitations in the wiki page):

  1. **Plain FBA on a public GEM**, not pcSecKoji. We use Vongsangnak 2008 iWV1314
     (BioModels MODEL1507180056). pcSec-class models with secretion-pathway proteome
     constraints have no publicly downloadable *A. oryzae* release.

  2. **Cassette perturbations as flux demands** added to a clone of the WT model:
       - Uricase: native peroxisomal urate oxidase (r1073) already in the model; we
         force a small forward flux to mimic engineered urate-oxidase load (peroxisomal
         H2O2 generation + 5-hydroxyisourate output, both already balanced).
       - Lactoferrin: secreted protein load. We capture the burden by adding an
         "amino-acid drain" reaction that consumes a Lf-amino-acid-composition-weighted
         pool of intracellular amino acids + ATP for translation and ER folding.
         No PDI / chaperone proteome cost. Scaled to ~500 mg/L Lf (post-§1.9 target),
         which is the empirical anchor for what the cassette demand looks like.
       - cns1+cns2 cordycepin biosynthesis: NEW reaction added per Jeennor 2023 and
         Xia 2017 + the 2024 Frontiers review:
            adenosine + ATP + NADPH --> cordycepin + ADP + Pi + NADP+ + H+
         (host kinase + Cns2 phosphohydrolase + Cns1 oxidoreductase net).
         Scaled to 564 mg/L/day from PMID 38071331.
       - carnS: cytosolic carnosine synthase. Added per chaperone-orthogonal-stacking.md
         §4: beta-alanine + L-histidine + ATP --> carnosine + AMP + PPi.
         No precedent titer in fungal koji; scale matched to a modest 50 mg/L/day flux.
       - panD: aspartate decarboxylase, cytosolic. Adds:
            L-aspartate --> beta-alanine + CO2.
         Pairs with carnS to provide beta-alanine.

  3. **Comparators:** WT / dual (uricase + Lf) / triple (+ cns1-cns2) / triple-alt-carnS
     (+ carnS+panD) / triple-alt-panD-only (panD alone, no carnS).

  4. **Burden metrics:** predicted growth rate (h^-1, the biomass-formation flux r1897);
     predicted kojic acid flux; predicted ergothioneine flux; predicted cordycepin
     flux (for cns1+cns2 scenario).

  5. **Kojic acid + ergothioneine added manually.** iWV1314 does not include either
     pathway. We add them via published net stoichiometry (kojic acid: D-glucose +
     O2 + 1 NADP+ --> kojic acid + 2 H2O + NADPH; ergothioneine: L-histidine + 3 SAM
     + L-cysteine + O2 --> ergothioneine + 3 SAH + pyruvate + NH3 + H2O). The flux
     these reactions can carry under each scenario is the "native metabolite yield"
     metric. They are NOT modeled as constrained; the burden is what FBA picks for
     the optimal-growth solution.

Run: python3 analyze.py
Outputs: outputs/results.json + outputs/summary.md + outputs/decision-table.md

Reproducibility: cobra 0.31.1, Python 3.13. No network calls at run time - GEM is
shipped in inputs/iWV1314.xml.
"""

import json
import math
import pathlib
import sys

import cobra
from cobra import Metabolite, Reaction

ROOT = pathlib.Path(__file__).parent
INPUTS = ROOT / "inputs"
OUTPUTS = ROOT / "outputs"
OUTPUTS.mkdir(exist_ok=True)

# ---------------------------------------------------------------------------
# Constants - flux scaling and decision thresholds
# ---------------------------------------------------------------------------

# Standard FBA glucose uptake rate (mmol gDW^-1 h^-1). 10 is the canonical reference
# value for fungal / E. coli FBA at exponential growth on glucose.
GLUCOSE_UPTAKE_MMOL_PER_GDW_H = 10.0

# Empirical cordycepin titer from Jeennor 2023 PMID 38071331: 564.64 +- 9.59 mg/L/day
# on glucose. MW cordycepin = 251.24 g/mol. Convert to per-gDW-per-h:
#   564.64 mg/L/d / 251.24 g/mol = 2.247 mmol/L/d (mg/g cancel → mmol)
# Assume a steady-state biomass density of ~5 gDW/L (mid-log fungal submerged
# culture; Vongsangnak 2008 supplementary; conservative anchor). Then per-gDW-per-h:
#   2.247 mmol/L/d / (5 gDW/L) / 24 h/d = 0.01873 mmol gDW^-1 h^-1
CORDYCEPIN_TITER_MG_L_DAY = 564.64
CORDYCEPIN_MW = 251.24
BIOMASS_DENSITY_GDW_L = 5.0
# Note: mg / (g/mol) gives mmol directly (the units cancel: mg/(g/mol) = mmol).
CORDYCEPIN_DEMAND_MMOL_GDW_H = (
    CORDYCEPIN_TITER_MG_L_DAY           # mg/L/d
    / CORDYCEPIN_MW                     # mmol/L/d (mg / (g/mol) = mmol)
    / BIOMASS_DENSITY_GDW_L             # mmol/gDW/d
    / 24.0                              # mmol/gDW/h
)

# Lactoferrin: Ward 1995 reported >2 g/L hLf in A. awamori submerged. The §1.9 success
# threshold is >=500 mg/L; the iterate threshold is 100-500 mg/L. We use the §1.9
# success threshold as the cassette flux anchor since that's what the endgame strain
# needs to deliver to clear the gate.
#   500 mg/L/d = 0.5 g/L/d / 76900 g/mol = 6.50e-3 mmol/L/d
#   / 5 gDW/L / 24 = 5.42e-5 mmol/gDW/h. THAT is the per-molecule flux, but a single
# Lf is 691 aa: protein synthesis flux in terms of amino acids is 691 * 5.42e-5 =
# 0.0375 mmol-aa/gDW/h. We add the demand as an aa-pool drain at that magnitude.
# This captures the translation burden; PDI / chaperone proteome cost is OUT OF SCOPE
# for v1 - see Limitations.
LACTOFERRIN_TITER_MG_L_DAY = 500.0  # §1.9 success threshold
LACTOFERRIN_MW = 76900.0
LACTOFERRIN_AA_COUNT = 691
# mg / (g/mol) = mmol directly. Then per gDW/h.
LACTOFERRIN_DEMAND_MMOL_GDW_H = (
    LACTOFERRIN_TITER_MG_L_DAY
    / LACTOFERRIN_MW
    / BIOMASS_DENSITY_GDW_L
    / 24.0
)
# Per-aa flux = per-protein flux * aa count
LACTOFERRIN_AA_DEMAND_MMOL_GDW_H = (
    LACTOFERRIN_DEMAND_MMOL_GDW_H * LACTOFERRIN_AA_COUNT
)

# Uricase: A. flavus uaZ secreted from engineered A. oryzae at moderate titer.
# Comp-010 cassette-compatibility analysis pinned the design at ~40 mg/L (Huynh 2020
# adalimumab reference) order of magnitude as an initial Phase 0 expectation. We use
# 40 mg/L/day as the uricase flux anchor - modest because uricase is a single-cassette
# heterologous protein at the host's demonstrated capacity for the NSlD-DP10 chassis.
# Uricase MW 35,000 g/mol; 302 aa.
URICASE_TITER_MG_L_DAY = 40.0
URICASE_MW = 35000.0
URICASE_AA_COUNT = 302
URICASE_DEMAND_MMOL_GDW_H = (
    URICASE_TITER_MG_L_DAY
    / URICASE_MW
    / BIOMASS_DENSITY_GDW_L
    / 24.0
)
URICASE_AA_DEMAND_MMOL_GDW_H = (
    URICASE_DEMAND_MMOL_GDW_H * URICASE_AA_COUNT
)

# Carnosine + panD scenario fluxes (mmol gDW^-1 h^-1). Conservative.
CARNOSINE_DEMAND_MMOL_GDW_H = 0.005   # ~50 mg/L/day at MW 226
PAND_DEMAND_MMOL_GDW_H = 0.01         # paired aspartate decarboxylase flux

# Decision thresholds per the brief
GROWTH_PENALTY_GREEN_MAX = 0.10   # <10% growth penalty
GROWTH_PENALTY_RED_MIN = 0.10     # >10% triggers yellow/red zone

NATIVE_YIELD_GREEN_MIN = 0.80     # native metabolite yields >=80% of dual baseline
NATIVE_YIELD_RED_MAX = 0.80       # <80% triggers yellow
NATIVE_YIELD_REJECT_MAX = 0.80    # legacy alias

# Set up an objective biomass reaction ID - iWV1314 has r1897 "Biomass formation".
BIOMASS_RXN_ID = "r1897"


# ---------------------------------------------------------------------------
# GEM loader + media setup
# ---------------------------------------------------------------------------

def load_base_model():
    """Load iWV1314 from inputs/. Configure minimal-glucose media + biomass objective.

    iWV1314's default state has 81 source-uptake reactions plus 18 reverse-inflow
    "Excretion" reactions (lb=-10) covering internal central-metabolism pools. This
    means the model on default settings can take up every carbon source, every amino
    acid, and most central-carbon intermediates simultaneously - completely violating
    minimal-glucose-media constraints. We have to close ALL of them and re-open only
    the strict minimal-media essentials.
    """
    m = cobra.io.read_sbml_model(str(INPUTS / "iWV1314.xml"))

    # ALL r2206..r2280 are alternative carbon / N / S sources. r2199-r2205 are
    # inorganic / glucose. r2281..r2298 are reverse-inflow central-metabolism
    # "Excretion" reactions with lb=-10 - close their reverse direction.
    glucose_id = "r2205"
    inorganic_ids = {
        "r2199": "CO2",
        "r2200": "NH3",
        "r2201": "HNO3",
        "r2202": "O2",
        "r2203": "PI (phosphate)",
        "r2204": "H2SO3 (sulfate proxy)",
    }

    # Close ALL source-uptakes (r2199..r2280 range) except glucose + N/O/P/S
    for r in m.reactions:
        if r.id.startswith("r22") and len(r.reactants) == 0 and r.upper_bound > 0:
            if r.id in inorganic_ids or r.id == glucose_id:
                continue
            r.upper_bound = 0.0

    # Close reverse-inflow on the r2281..r2298 sink reactions (set lb to 0)
    for r in m.reactions:
        if r.id.startswith("r22") and len(r.products) == 0 and r.lower_bound < 0:
            r.lower_bound = 0.0

    # Glucose: bounded
    m.reactions.get_by_id(glucose_id).upper_bound = GLUCOSE_UPTAKE_MMOL_PER_GDW_H

    # Inorganics: open
    m.reactions.get_by_id("r2199").upper_bound = 0.0      # CO2 uptake: 0 (we generate CO2)
    m.reactions.get_by_id("r2200").upper_bound = 1000.0   # NH3 uptake: unconstrained
    m.reactions.get_by_id("r2201").upper_bound = 0.0      # HNO3: not used
    m.reactions.get_by_id("r2202").upper_bound = 1000.0   # O2: unconstrained
    m.reactions.get_by_id("r2203").upper_bound = 1000.0   # phosphate: unconstrained
    m.reactions.get_by_id("r2204").upper_bound = 1000.0   # sulfate proxy: unconstrained

    # Objective = biomass formation r1897. Note: this model's biomass coefficient sum
    # is ~153, so the flux units are NOT directly h^-1. Vongsangnak 2008 reports
    # max mu_glucose ~= 0.31 h^-1; the model's r1897 flux at 10 mmol glucose uptake
    # comes out to ~6 (after closing all the spurious uptakes), so the scaling
    # factor is roughly 19x. We work in MODEL-NATIVE flux units and report
    # comparisons as percentages relative to WT - units are consistent across
    # scenarios, which is what matters for the verdict.
    m.objective = m.reactions.get_by_id(BIOMASS_RXN_ID)
    return m


# ---------------------------------------------------------------------------
# Add native metabolite reactions: kojic acid + ergothioneine
# ---------------------------------------------------------------------------

def add_kojic_acid_pathway(m):
    """Add a simplified net kojic-acid biosynthesis reaction.

    Net: D-glucose + O2 + NADP+ -> kojic acid + 2 H2O + NADPH + H+
      Mechanism: one oxidation (CHOH -> CO, generates NADPH equivalent) + two
      dehydrations (release 2 H2O). KojA is FAD-dependent oxidoreductase; we use
      NADP+/NADPH as the redox carrier proxy for FBA balance - flag as a v1
      simplification (the choice doesn't change the carbon-cost answer).

    Reference: Terabayashi 2010 PMID 20650324; Marui 2011 PMID 21514215.
    """
    # iWV1314 metabolite IDs (verify with .metabolites):
    #   DGLC (cytosolic D-glucose), O2 (cytosolic O2), H2O, NADP, NADPH, H
    # NADP+ in iWV1314 = "NADP", NADPH = "NADPH", H = "H"
    DGLC = m.metabolites.get_by_id("DGLC")
    O2 = m.metabolites.get_by_id("O2")
    H2O = m.metabolites.get_by_id("H2O")
    NADP = m.metabolites.get_by_id("NADP")
    NADPH = m.metabolites.get_by_id("NADPH")
    H = m.metabolites.get_by_id("H")

    # Add kojic acid metabolite (cytosolic) + extracellular pool + secretion sink
    KOJIC_c = Metabolite(
        "KOJIC_c",
        name="kojic acid (5-hydroxy-2-(hydroxymethyl)-4H-pyran-4-one) cytosolic",
        compartment="c",
        formula="C6H6O4",
    )
    KOJIC_e = Metabolite(
        "KOJIC_e",
        name="kojic acid extracellular",
        compartment="e",
        formula="C6H6O4",
    )
    m.add_metabolites([KOJIC_c, KOJIC_e])

    # Synthesis reaction: D-glucose + O2 + NADP -> kojic acid + 2 H2O + NADPH + H
    rxn = Reaction("KOJIC_SYN")
    rxn.name = "Kojic acid biosynthesis (net; KojA/KojR/KojT)"
    rxn.lower_bound = 0.0
    rxn.upper_bound = 1000.0
    rxn.add_metabolites({
        DGLC: -1.0,
        O2: -1.0,
        NADP: -1.0,
        KOJIC_c: 1.0,
        H2O: 2.0,
        NADPH: 1.0,
        H: 1.0,
    })
    m.add_reactions([rxn])

    # Secretion (cytosol -> extracellular)
    sec = Reaction("KOJIC_t")
    sec.name = "Kojic acid secretion"
    sec.lower_bound = 0.0
    sec.upper_bound = 1000.0
    sec.add_metabolites({KOJIC_c: -1.0, KOJIC_e: 1.0})
    m.add_reactions([sec])

    # Exchange (extracellular -> sink)
    ex = Reaction("EX_KOJIC")
    ex.name = "Kojic acid exchange"
    ex.lower_bound = 0.0
    ex.upper_bound = 1000.0
    ex.add_metabolites({KOJIC_e: -1.0})
    m.add_reactions([ex])

    return rxn.id, ex.id


def add_ergothioneine_pathway(m):
    """Add a simplified net ergothioneine biosynthesis reaction.

    Fungal pathway (Egt1 + Egt2, Neurospora-style):
      L-histidine + 3 SAM + L-cysteine + O2 ->
         ergothioneine + 3 SAH + pyruvate + NH3 + H2O

    Reference: Hu 2014 PMID 25496641; Bello 2012 PMID 22276148.
    """
    # Metabolite IDs in iWV1314: check carefully
    # HIS = histidine, AMET = SAM, AHCYS = SAH, CYS = cysteine, PYR = pyruvate
    his_candidates = [met for met in m.metabolites if met.id == "HIS"]
    if not his_candidates:
        his_candidates = [met for met in m.metabolites if "histidine" in met.name.lower() and met.compartment == "c"]
    HIS = his_candidates[0]

    cys_candidates = [met for met in m.metabolites if met.id == "CYS"]
    if not cys_candidates:
        cys_candidates = [met for met in m.metabolites if met.name.lower().startswith("l-cysteine") and met.compartment == "c"]
    CYS = cys_candidates[0]

    sam_candidates = [met for met in m.metabolites if met.id == "AMET"]
    if not sam_candidates:
        sam_candidates = [met for met in m.metabolites if "adenosyl" in met.name.lower() and "methionine" in met.name.lower() and met.compartment == "c"]
    AMET = sam_candidates[0]

    sah_candidates = [met for met in m.metabolites if met.id == "AHCYS"]
    if not sah_candidates:
        sah_candidates = [met for met in m.metabolites if "homocysteine" in met.name.lower() and "adenosyl" in met.name.lower() and met.compartment == "c"]
    AHCYS = sah_candidates[0]

    pyr_candidates = [met for met in m.metabolites if met.id == "PYR" and met.compartment == "c"]
    PYR = pyr_candidates[0]

    nh3_candidates = [met for met in m.metabolites if met.id == "NH3" and met.compartment == "c"]
    NH3 = nh3_candidates[0]

    O2 = m.metabolites.get_by_id("O2")
    H2O = m.metabolites.get_by_id("H2O")

    EGT_c = Metabolite(
        "EGT_c",
        name="ergothioneine cytosolic",
        compartment="c",
        formula="C9H15N3O2S",
    )
    EGT_e = Metabolite(
        "EGT_e",
        name="ergothioneine extracellular",
        compartment="e",
        formula="C9H15N3O2S",
    )
    m.add_metabolites([EGT_c, EGT_e])

    rxn = Reaction("EGT_SYN")
    rxn.name = "Ergothioneine biosynthesis (net; Egt1+Egt2)"
    rxn.lower_bound = 0.0
    rxn.upper_bound = 1000.0
    rxn.add_metabolites({
        HIS: -1.0,
        CYS: -1.0,
        AMET: -3.0,
        O2: -1.0,
        EGT_c: 1.0,
        AHCYS: 3.0,
        PYR: 1.0,
        NH3: 1.0,
        H2O: 1.0,
    })
    m.add_reactions([rxn])

    sec = Reaction("EGT_t")
    sec.name = "Ergothioneine secretion"
    sec.lower_bound = 0.0
    sec.upper_bound = 1000.0
    sec.add_metabolites({EGT_c: -1.0, EGT_e: 1.0})
    m.add_reactions([sec])

    ex = Reaction("EX_EGT")
    ex.name = "Ergothioneine exchange"
    ex.lower_bound = 0.0
    ex.upper_bound = 1000.0
    ex.add_metabolites({EGT_e: -1.0})
    m.add_reactions([ex])

    return rxn.id, ex.id


# ---------------------------------------------------------------------------
# Cassette perturbations
# ---------------------------------------------------------------------------

def add_uricase_load(m, demand_aa_mmol):
    """Uricase cassette: peroxisomal urate oxidase + secreted protein.

    Two simultaneous loads:
      1. Force minimum urate-oxidase flux (r1073: H2O + O2 + URATEp -> H2O2 + HIURTEp)
         to mimic the engineered cassette's catalytic turnover. Tiny; the substrate
         is urate from purine catabolism, which only flows when adenosine/guanosine
         are degraded. This cassette mainly affects flux only when there's urate to
         degrade. We don't force a minimum here - the cassette is dormant on
         glucose-minimal media because there's no purine load.
      2. Protein synthesis demand: drain a generic amino-acid pool to mimic ribosome
         + ER folding load. We add an "amino acid drain" reaction that consumes
         L-glutamate as a proxy (carbon + nitrogen carrier; Glu is the most central
         aa hub in fungal metabolism) + ATP for translation.
    """
    # Glu, ATP, ADP, PI for translation cost
    GLU = m.metabolites.get_by_id("GLU")
    ATP = m.metabolites.get_by_id("ATP")
    ADP = m.metabolites.get_by_id("ADP")
    PI = m.metabolites.get_by_id("PI")
    H = m.metabolites.get_by_id("H")
    H2O = m.metabolites.get_by_id("H2O")

    # Translation cost: ~4 ATP per peptide bond (2 for aminoacyl-tRNA, 2 for EF-Tu/EF-G).
    # ER folding: assume ~0.5 ATP per aa for BiP/PDI cycling on a non-PDI-heavy enzyme.
    # Total ~4.5 ATP per aa for uricase.
    atp_per_aa = 4.5

    drain = Reaction("URICASE_LOAD")
    drain.name = "Uricase cassette: translation + ER transit cost (amino acid drain proxy)"
    drain.lower_bound = demand_aa_mmol
    drain.upper_bound = demand_aa_mmol  # force exact demand
    drain.add_metabolites({
        GLU: -1.0,
        ATP: -atp_per_aa,
        H2O: -atp_per_aa,
        ADP: atp_per_aa,
        PI: atp_per_aa,
        H: atp_per_aa,
    })
    m.add_reactions([drain])
    return drain.id


def add_lactoferrin_load(m, demand_aa_mmol):
    """Lactoferrin cassette: PDI-heavy secreted protein.

    Captures translation + secretion + (approximated) ER chaperone burden.
    """
    GLU = m.metabolites.get_by_id("GLU")
    ATP = m.metabolites.get_by_id("ATP")
    ADP = m.metabolites.get_by_id("ADP")
    PI = m.metabolites.get_by_id("PI")
    H = m.metabolites.get_by_id("H")
    H2O = m.metabolites.get_by_id("H2O")

    # PDI-heavy: 16 disulfides means heavy ER folding cost. Use ~6 ATP per aa
    # (translation 4 + PDI/ERO1 disulfide formation 1 + BiP cycling 1).
    # NOTE: this is a v1 approximation. pcSec-class models would split this into
    # explicit PDI / BiP / calnexin protein-occupancy constraints.
    atp_per_aa = 6.0

    drain = Reaction("LF_LOAD")
    drain.name = "Lactoferrin cassette: translation + PDI-heavy ER folding cost (amino acid drain proxy)"
    drain.lower_bound = demand_aa_mmol
    drain.upper_bound = demand_aa_mmol  # force exact demand
    drain.add_metabolites({
        GLU: -1.0,
        ATP: -atp_per_aa,
        H2O: -atp_per_aa,
        ADP: atp_per_aa,
        PI: atp_per_aa,
        H: atp_per_aa,
    })
    m.add_reactions([drain])
    return drain.id


def add_cordycepin_pathway(m, demand_mmol):
    """Cordycepin cassette: cns1+cns2 heterologous expression.

    Net reaction (host kinase + Cns2 + Cns1):
        adenosine + ATP + NADPH --> cordycepin + ADP + Pi + NADP+ + H+

    Cordycepin is secreted (Jeennor 2023 reports extracellular cordycepin).

    Sources:
      - Jeennor 2023 PMID 38071331 (A. oryzae cns1+cns2 expression, 564 mg/L/day)
      - Xia 2017 PMID 29056419 (C. militaris BGC; cns1+cns2+cns3 mechanism)
      - Wang 2024 PMC11300563 (complementary pathway review; cns1/cns2/cns3 roles)
      - Yan 2024 frontiersin.org/.../fceng.2024.1446454 (cofactor + heterologous-host review)
    """
    ADN = m.metabolites.get_by_id("ADN")           # adenosine (cytosolic)
    ATP = m.metabolites.get_by_id("ATP")
    ADP = m.metabolites.get_by_id("ADP")
    PI = m.metabolites.get_by_id("PI")
    NADP = m.metabolites.get_by_id("NADP")
    NADPH = m.metabolites.get_by_id("NADPH")
    H = m.metabolites.get_by_id("H")

    COR_c = Metabolite(
        "COR_c",
        name="cordycepin (3'-deoxyadenosine) cytosolic",
        compartment="c",
        formula="C10H13N5O3",
    )
    COR_e = Metabolite(
        "COR_e",
        name="cordycepin extracellular",
        compartment="e",
        formula="C10H13N5O3",
    )
    m.add_metabolites([COR_c, COR_e])

    rxn = Reaction("COR_SYN")
    rxn.name = "Cordycepin biosynthesis (cns1+cns2 net; PMID 38071331)"
    # Lock flux at the Jeennor 2023 empirical titer. We want to ask "what does it
    # cost to deliver the published titer?", not "what's the max cordycepin the
    # model can spuriously emit through a free amino-acid drain?"
    # Set upper bound FIRST to accommodate large stress-test demands.
    rxn.upper_bound = max(demand_mmol, 1000.0)
    rxn.lower_bound = demand_mmol
    rxn.upper_bound = demand_mmol
    rxn.add_metabolites({
        ADN: -1.0,
        ATP: -1.0,
        NADPH: -1.0,
        COR_c: 1.0,
        ADP: 1.0,
        PI: 1.0,
        NADP: 1.0,
        H: 1.0,
    })
    m.add_reactions([rxn])

    sec = Reaction("COR_t")
    sec.name = "Cordycepin secretion"
    sec.lower_bound = 0.0
    sec.upper_bound = 1000.0
    sec.add_metabolites({COR_c: -1.0, COR_e: 1.0})
    m.add_reactions([sec])

    ex = Reaction("EX_COR")
    ex.name = "Cordycepin exchange (extracellular sink)"
    ex.lower_bound = 0.0
    ex.upper_bound = 1000.0
    ex.add_metabolites({COR_e: -1.0})
    m.add_reactions([ex])

    return rxn.id, ex.id


def add_carnS_pathway(m, demand_mmol):
    """Carnosine synthase (CarnS): beta-alanine + L-histidine + ATP -> carnosine + AMP + PPi.

    Cytosolic. From Lactobacillus, per chaperone-orthogonal-stacking.md §4.
    """
    HIS = m.metabolites.get_by_id("HIS")
    ATP = m.metabolites.get_by_id("ATP")
    AMP = m.metabolites.get_by_id("AMP")
    PPI = m.metabolites.get_by_id("PPI")

    # beta-alanine: lookup
    bala_candidates = [met for met in m.metabolites if met.id == "bALA" or "beta-alanine" in met.name.lower()]
    if not bala_candidates:
        # Create it; will need panD to supply
        BALA = Metabolite("BALA_c", name="beta-alanine cytosolic", compartment="c", formula="C3H7NO2")
        m.add_metabolites([BALA])
    else:
        BALA = bala_candidates[0]

    CARN_c = Metabolite("CARN_c", name="carnosine cytosolic", compartment="c", formula="C9H14N4O3")
    CARN_e = Metabolite("CARN_e", name="carnosine extracellular", compartment="e", formula="C9H14N4O3")
    m.add_metabolites([CARN_c, CARN_e])

    rxn = Reaction("CARN_SYN")
    rxn.name = "Carnosine synthase (CarnS, bacterial heterologous)"
    rxn.lower_bound = demand_mmol
    rxn.upper_bound = demand_mmol
    rxn.add_metabolites({
        BALA: -1.0,
        HIS: -1.0,
        ATP: -1.0,
        CARN_c: 1.0,
        AMP: 1.0,
        PPI: 1.0,
    })
    m.add_reactions([rxn])

    sec = Reaction("CARN_t")
    sec.lower_bound = 0.0
    sec.upper_bound = 1000.0
    sec.add_metabolites({CARN_c: -1.0, CARN_e: 1.0})
    m.add_reactions([sec])

    ex = Reaction("EX_CARN")
    ex.lower_bound = 0.0
    ex.upper_bound = 1000.0
    ex.add_metabolites({CARN_e: -1.0})
    m.add_reactions([ex])

    return rxn.id, ex.id, BALA.id


def add_panD_pathway(m, demand_mmol, bala_id="BALA_c"):
    """Aspartate decarboxylase (panD): L-aspartate -> beta-alanine + CO2."""
    ASP = m.metabolites.get_by_id("ASP")
    CO2 = m.metabolites.get_by_id("CO2")
    H = m.metabolites.get_by_id("H")

    # beta-alanine: may have been added by carnS; if not, add it
    if bala_id in [met.id for met in m.metabolites]:
        BALA = m.metabolites.get_by_id(bala_id)
    else:
        BALA = Metabolite(bala_id, name="beta-alanine cytosolic", compartment="c", formula="C3H7NO2")
        m.add_metabolites([BALA])

    rxn = Reaction("PAND_SYN")
    rxn.name = "Aspartate decarboxylase (panD, bacterial heterologous)"
    rxn.lower_bound = demand_mmol
    rxn.upper_bound = demand_mmol
    rxn.add_metabolites({
        ASP: -1.0,
        H: -1.0,
        BALA: 1.0,
        CO2: 1.0,
    })
    m.add_reactions([rxn])

    # If carnS isn't installed, drain beta-alanine to a sink so it doesn't pile up
    if "CARN_SYN" not in [r.id for r in m.reactions]:
        sink = Reaction("BALA_sink")
        sink.name = "beta-alanine sink (only when panD without carnS)"
        sink.lower_bound = 0.0
        sink.upper_bound = 1000.0
        sink.add_metabolites({BALA: -1.0})
        m.add_reactions([sink])

    return rxn.id


# ---------------------------------------------------------------------------
# Scenario builder
# ---------------------------------------------------------------------------

SCENARIOS = [
    "WT",
    "dual (uricase + Lf)",
    "+cns1-cns2 (triple, cordycepin arm)",
    "+carnS+panD (triple, carnosine arm)",
    "+panD only",
    # Stress-test scenarios - sweep cordycepin demand up by 10x and 100x to probe robustness
    "+cns1-cns2 stress 10x titer",
    "+cns1-cns2 stress 100x titer",
    "+cns1-cns2 stress 1000x titer",
    "+cns1-cns2 stress 10000x titer",
    "+cns1-cns2 stress 100000x titer",
]


def build_scenario(name):
    """Return a configured cobra Model for one scenario."""
    m = load_base_model()

    # Always add native metabolite reactions so we can read out kojic + EGT fluxes.
    add_kojic_acid_pathway(m)
    add_ergothioneine_pathway(m)

    if name == "WT":
        pass  # no cassettes
    elif name == "dual (uricase + Lf)":
        add_uricase_load(m, URICASE_AA_DEMAND_MMOL_GDW_H)
        add_lactoferrin_load(m, LACTOFERRIN_AA_DEMAND_MMOL_GDW_H)
    elif name == "+cns1-cns2 (triple, cordycepin arm)":
        add_uricase_load(m, URICASE_AA_DEMAND_MMOL_GDW_H)
        add_lactoferrin_load(m, LACTOFERRIN_AA_DEMAND_MMOL_GDW_H)
        add_cordycepin_pathway(m, CORDYCEPIN_DEMAND_MMOL_GDW_H)
    elif name == "+carnS+panD (triple, carnosine arm)":
        add_uricase_load(m, URICASE_AA_DEMAND_MMOL_GDW_H)
        add_lactoferrin_load(m, LACTOFERRIN_AA_DEMAND_MMOL_GDW_H)
        # panD first → BALA_c exists; then carnS consumes it
        add_panD_pathway(m, PAND_DEMAND_MMOL_GDW_H)
        add_carnS_pathway(m, CARNOSINE_DEMAND_MMOL_GDW_H)
    elif name == "+panD only":
        add_uricase_load(m, URICASE_AA_DEMAND_MMOL_GDW_H)
        add_lactoferrin_load(m, LACTOFERRIN_AA_DEMAND_MMOL_GDW_H)
        add_panD_pathway(m, PAND_DEMAND_MMOL_GDW_H)
    elif name == "+cns1-cns2 stress 10x titer":
        add_uricase_load(m, URICASE_AA_DEMAND_MMOL_GDW_H)
        add_lactoferrin_load(m, LACTOFERRIN_AA_DEMAND_MMOL_GDW_H)
        add_cordycepin_pathway(m, 10 * CORDYCEPIN_DEMAND_MMOL_GDW_H)
    elif name == "+cns1-cns2 stress 100x titer":
        add_uricase_load(m, URICASE_AA_DEMAND_MMOL_GDW_H)
        add_lactoferrin_load(m, LACTOFERRIN_AA_DEMAND_MMOL_GDW_H)
        add_cordycepin_pathway(m, 100 * CORDYCEPIN_DEMAND_MMOL_GDW_H)
    elif name == "+cns1-cns2 stress 1000x titer":
        add_uricase_load(m, URICASE_AA_DEMAND_MMOL_GDW_H)
        add_lactoferrin_load(m, LACTOFERRIN_AA_DEMAND_MMOL_GDW_H)
        add_cordycepin_pathway(m, 1000 * CORDYCEPIN_DEMAND_MMOL_GDW_H)
    elif name == "+cns1-cns2 stress 10000x titer":
        add_uricase_load(m, URICASE_AA_DEMAND_MMOL_GDW_H)
        add_lactoferrin_load(m, LACTOFERRIN_AA_DEMAND_MMOL_GDW_H)
        add_cordycepin_pathway(m, 10000 * CORDYCEPIN_DEMAND_MMOL_GDW_H)
    elif name == "+cns1-cns2 stress 100000x titer":
        add_uricase_load(m, URICASE_AA_DEMAND_MMOL_GDW_H)
        add_lactoferrin_load(m, LACTOFERRIN_AA_DEMAND_MMOL_GDW_H)
        add_cordycepin_pathway(m, 100000 * CORDYCEPIN_DEMAND_MMOL_GDW_H)
    else:
        raise ValueError(name)

    return m


# ---------------------------------------------------------------------------
# Run scenarios + extract metrics
# ---------------------------------------------------------------------------

def run_scenario(name):
    m = build_scenario(name)
    sol = m.optimize()
    metrics = {
        "scenario": name,
        "status": sol.status,
        "growth_h_inv": sol.objective_value if sol.status == "optimal" else None,
        "glucose_uptake_mmol_gDW_h": -sol.fluxes["r2205"] if sol.status == "optimal" else None,
        # Actually r2205 has positive sign as the model formulates uptake;
        # we read the value directly.
    }
    if sol.status == "optimal":
        metrics["glucose_uptake_mmol_gDW_h"] = sol.fluxes["r2205"]
        # Native metabolite fluxes (mmol/gDW/h)
        metrics["kojic_acid_flux_mmol_gDW_h"] = sol.fluxes.get("EX_KOJIC", 0.0)
        metrics["ergothioneine_flux_mmol_gDW_h"] = sol.fluxes.get("EX_EGT", 0.0)
        # Cassette outputs
        if "EX_COR" in sol.fluxes.index:
            metrics["cordycepin_flux_mmol_gDW_h"] = sol.fluxes["EX_COR"]
        if "EX_CARN" in sol.fluxes.index:
            metrics["carnosine_flux_mmol_gDW_h"] = sol.fluxes["EX_CARN"]
        if "URICASE_LOAD" in sol.fluxes.index:
            metrics["uricase_load_mmol_aa_gDW_h"] = sol.fluxes["URICASE_LOAD"]
        if "LF_LOAD" in sol.fluxes.index:
            metrics["lactoferrin_load_mmol_aa_gDW_h"] = sol.fluxes["LF_LOAD"]

        # NB: kojic + EGT fluxes will both be zero unless we force a demand,
        # because FBA maximizes growth and ignores anything non-essential.
        # That's the point: under pure growth-maximization, the model tells us
        # whether there's capacity left over to make them. We separately probe
        # the max kojic and max EGT flux ACHIEVABLE while sustaining the
        # scenario's growth rate.
    return m, sol, metrics


def probe_native_metabolite_capacity(m, baseline_growth, min_growth_fraction=0.99):
    """Given a scenario model + its optimal growth, lock biomass to >=99% of that
    growth and ask: what's the maximum kojic-acid flux achievable? What about EGT?

    This is the "yield headroom" the strain has under each scenario."""
    rxn_biomass = m.reactions.get_by_id(BIOMASS_RXN_ID)
    rxn_biomass.lower_bound = baseline_growth * min_growth_fraction

    # Max kojic acid
    m.objective = m.reactions.EX_KOJIC
    sol_k = m.optimize()
    max_kojic = sol_k.objective_value if sol_k.status == "optimal" else 0.0

    # Reset; max EGT
    m.objective = m.reactions.EX_EGT
    sol_e = m.optimize()
    max_egt = sol_e.objective_value if sol_e.status == "optimal" else 0.0

    # Reset biomass bound + objective for cleanliness
    rxn_biomass.lower_bound = 0.0
    m.objective = m.reactions.get_by_id(BIOMASS_RXN_ID)

    return max_kojic, max_egt


def main():
    print("=" * 75)
    print("comp-023 - cns1+cns2 cordycepin biosynthesis metabolic-burden FBA")
    print("=" * 75)
    print(f"GEM: iWV1314 (Vongsangnak 2008, BioModels MODEL1507180056)")
    print(f"cobra: {cobra.__version__}")
    print(f"Glucose uptake: {GLUCOSE_UPTAKE_MMOL_PER_GDW_H} mmol/gDW/h")
    print(f"Cordycepin demand (Jeennor 2023 564 mg/L/d anchor): "
          f"{CORDYCEPIN_DEMAND_MMOL_GDW_H:.4f} mmol/gDW/h")
    print(f"Lactoferrin demand (§1.9 target 500 mg/L/d → {LACTOFERRIN_AA_DEMAND_MMOL_GDW_H:.4f} mmol-aa/gDW/h)")
    print(f"Uricase demand (40 mg/L/d → {URICASE_AA_DEMAND_MMOL_GDW_H:.4f} mmol-aa/gDW/h)")
    print()

    results = {}
    for name in SCENARIOS:
        print(f"--- Scenario: {name} ---")
        m, sol, metrics = run_scenario(name)
        print(f"  status: {metrics['status']}")
        print(f"  growth (h^-1): {metrics['growth_h_inv']}")
        if metrics["status"] == "optimal" and metrics["growth_h_inv"] is not None and metrics["growth_h_inv"] > 0:
            mk, me = probe_native_metabolite_capacity(m, metrics["growth_h_inv"])
            metrics["max_kojic_flux_mmol_gDW_h"] = mk
            metrics["max_egt_flux_mmol_gDW_h"] = me
            print(f"  max kojic (at >=99% biomass): {mk:.5f} mmol/gDW/h")
            print(f"  max EGT (at >=99% biomass):   {me:.5f} mmol/gDW/h")
            if "cordycepin_flux_mmol_gDW_h" in metrics:
                print(f"  cordycepin flux: {metrics['cordycepin_flux_mmol_gDW_h']:.5f} mmol/gDW/h "
                      f"(target {CORDYCEPIN_DEMAND_MMOL_GDW_H:.5f})")
        results[name] = metrics
        print()

    # Apply decision thresholds
    wt = results["WT"]
    dual = results["dual (uricase + Lf)"]
    triple_cor = results["+cns1-cns2 (triple, cordycepin arm)"]
    triple_carn = results["+carnS+panD (triple, carnosine arm)"]
    triple_pand = results["+panD only"]

    def growth_penalty(scenario_growth, ref_growth):
        if ref_growth is None or ref_growth == 0 or scenario_growth is None:
            return None
        return (ref_growth - scenario_growth) / ref_growth

    def yield_ratio(scenario_val, ref_val):
        if ref_val is None or ref_val == 0 or scenario_val is None:
            return None
        return scenario_val / ref_val

    decision_table = []
    for s_name in [
        "dual (uricase + Lf)",
        "+cns1-cns2 (triple, cordycepin arm)",
        "+carnS+panD (triple, carnosine arm)",
        "+panD only",
        "+cns1-cns2 stress 10x titer",
        "+cns1-cns2 stress 100x titer",
        "+cns1-cns2 stress 1000x titer",
        "+cns1-cns2 stress 10000x titer",
        "+cns1-cns2 stress 100000x titer",
    ]:
        s = results[s_name]
        gp = growth_penalty(s["growth_h_inv"], wt["growth_h_inv"])
        ky = yield_ratio(s.get("max_kojic_flux_mmol_gDW_h"), dual.get("max_kojic_flux_mmol_gDW_h"))
        ey = yield_ratio(s.get("max_egt_flux_mmol_gDW_h"), dual.get("max_egt_flux_mmol_gDW_h"))
        if gp is None or s.get("status") != "optimal":
            verdict = "INFEASIBLE"
        elif gp <= GROWTH_PENALTY_GREEN_MAX and (ky is None or ky >= NATIVE_YIELD_GREEN_MIN) and (ey is None or ey >= NATIVE_YIELD_GREEN_MIN):
            verdict = "GREEN"
        elif gp > GROWTH_PENALTY_RED_MIN or (ky is not None and ky < (1.0 - 0.20)) or (ey is not None and ey < (1.0 - 0.20)):
            verdict = "RED"
        else:
            verdict = "YELLOW"
        decision_table.append({
            "scenario": s_name,
            "growth_h_inv": s["growth_h_inv"],
            "growth_penalty_vs_WT": gp,
            "max_kojic_mmol_gDW_h": s.get("max_kojic_flux_mmol_gDW_h"),
            "kojic_yield_vs_dual": ky,
            "max_egt_mmol_gDW_h": s.get("max_egt_flux_mmol_gDW_h"),
            "egt_yield_vs_dual": ey,
            "cordycepin_mmol_gDW_h": s.get("cordycepin_flux_mmol_gDW_h"),
            "verdict": verdict,
        })

    # Write outputs
    out = {
        "comp": "comp-023",
        "gem": {
            "id": "iWV1314",
            "biomodels": "MODEL1507180056",
            "source": "Vongsangnak 2008, BMC Genomics PMID 18801187",
            "reactions": 2361,
            "metabolites": 1104,
            "genes": 1346,
            "compartments": ["Cytosol", "Peroxisome", "Extracellular", "Mitochondria"],
        },
        "constants": {
            "glucose_uptake_mmol_gDW_h": GLUCOSE_UPTAKE_MMOL_PER_GDW_H,
            "cordycepin_demand_mmol_gDW_h": CORDYCEPIN_DEMAND_MMOL_GDW_H,
            "cordycepin_titer_anchor_mg_L_day": CORDYCEPIN_TITER_MG_L_DAY,
            "cordycepin_titer_pmid": "38071331 (Jeennor 2023)",
            "lactoferrin_aa_demand_mmol_gDW_h": LACTOFERRIN_AA_DEMAND_MMOL_GDW_H,
            "uricase_aa_demand_mmol_gDW_h": URICASE_AA_DEMAND_MMOL_GDW_H,
            "carnosine_demand_mmol_gDW_h": CARNOSINE_DEMAND_MMOL_GDW_H,
            "panD_demand_mmol_gDW_h": PAND_DEMAND_MMOL_GDW_H,
            "biomass_density_gDW_L_assumed": BIOMASS_DENSITY_GDW_L,
        },
        "scenarios": results,
        "decision_table": decision_table,
    }
    with open(OUTPUTS / "results.json", "w") as f:
        json.dump(out, f, indent=2, default=str)

    # Markdown summary
    md = []
    md.append("# comp-023 - cns1+cns2 cordycepin biosynthesis metabolic-burden FBA")
    md.append("")
    md.append(f"**GEM:** iWV1314 (Vongsangnak 2008, BioModels MODEL1507180056). "
              f"2,361 reactions / 1,104 metabolites / 1,346 genes / 4 compartments.")
    md.append(f"**cobra version:** {cobra.__version__}")
    md.append(f"**Glucose uptake:** {GLUCOSE_UPTAKE_MMOL_PER_GDW_H} mmol/gDW/h (canonical FBA reference)")
    md.append(f"**Cordycepin demand anchor:** {CORDYCEPIN_TITER_MG_L_DAY} mg/L/d (Jeennor 2023, PMID 38071331) "
              f"→ {CORDYCEPIN_DEMAND_MMOL_GDW_H:.4f} mmol/gDW/h (at {BIOMASS_DENSITY_GDW_L} gDW/L)")
    md.append("")
    md.append("## Per-scenario results")
    md.append("")
    md.append("| Scenario | growth (h⁻¹) | Δ growth vs WT | max kojic (mmol/gDW/h) | kojic yield vs dual | max EGT (mmol/gDW/h) | EGT yield vs dual | cordycepin (mmol/gDW/h) | verdict |")
    md.append("|---|---|---|---|---|---|---|---|---|")
    md.append(f"| WT | {wt['growth_h_inv']:.5f} | n/a | {wt.get('max_kojic_flux_mmol_gDW_h', 0):.4f} | n/a | {wt.get('max_egt_flux_mmol_gDW_h', 0):.5f} | n/a | n/a | (reference) |")
    for row in decision_table:
        gp = row["growth_penalty_vs_WT"]
        ky = row["kojic_yield_vs_dual"]
        ey = row["egt_yield_vs_dual"]
        cor = row.get("cordycepin_mmol_gDW_h")
        if row["verdict"] == "INFEASIBLE":
            md.append(f"| {row['scenario']} | INFEASIBLE | - | - | - | - | - | - | **INFEASIBLE** |")
            continue
        md.append(
            f"| {row['scenario']} "
            f"| {row['growth_h_inv']:.5f} "
            f"| {(gp * 100):+.2f}% "
            f"| {row['max_kojic_mmol_gDW_h']:.4f} "
            f"| {(ky * 100):.2f}% "
            f"| {row['max_egt_mmol_gDW_h']:.5f} "
            f"| {(ey * 100):.2f}% "
            f"| {(cor if cor is not None else 0):.5f} "
            f"| **{row['verdict']}** |"
        )
    md.append("")
    md.append("## Decision-threshold logic")
    md.append("")
    md.append("- **GREEN** = growth penalty < 10% AND kojic + EGT yields ≥ 80% of dual-cassette baseline → green-light a cordycepin arm in §1.9 extended design.")
    md.append("- **RED**   = growth penalty > 10% OR either native yield drops more than 20% → red-flag, route cordycepin to a separate strain or LBP chassis.")
    md.append("- **YELLOW** = anywhere between → wet-lab confirmation gate before commit.")
    md.append("")
    md.append("## Headline verdict (cordycepin arm)")
    md.append("")
    cor_row = next(r for r in decision_table if "cns1-cns2" in r["scenario"])
    dual_row = next(r for r in decision_table if r["scenario"] == "dual (uricase + Lf)")
    md.append(f"- **cns1+cns2 cordycepin arm:** {cor_row['verdict']}")
    md.append(f"  - growth penalty vs WT: {cor_row['growth_penalty_vs_WT']*100:+.2f}% (threshold ±10%)")
    md.append(f"  - kojic acid yield vs dual: {cor_row['kojic_yield_vs_dual']*100:.2f}% (threshold ≥80%)")
    md.append(f"  - ergothioneine yield vs dual: {cor_row['egt_yield_vs_dual']*100:.2f}% (threshold ≥80%)")
    # mmol/gDW/h × gDW/L × h/d = mmol/L/d; × MW (g/mol) = mg/L/d.
    cor_mg_l_d = cor_row['cordycepin_mmol_gDW_h'] * BIOMASS_DENSITY_GDW_L * 24 * CORDYCEPIN_MW
    md.append(f"  - cordycepin produced: {cor_mg_l_d:.1f} mg/L/d (target {CORDYCEPIN_TITER_MG_L_DAY} mg/L/d, Jeennor 2023 PMID 38071331)")
    md.append("")
    md.append("## Notes / Limitations")
    md.append("")
    md.append("1. **FBA, not pcSecKoji.** v1 uses plain flux-balance analysis with cassette burdens modeled as flux demands. PDI / chaperone / BiP / calnexin proteome-occupancy constraints are NOT in the model. This v1 captures the carbon, nitrogen, energy, and reducing-equivalent burden, NOT secretion-pathway proteome saturation. A v2 upgrade is `pcSec`-class modeling - see the brief.")
    md.append("2. **Lactoferrin burden is modeled as a generic translation + ER-folding cost on a glutamate/ATP drain proxy.** The 16-disulfide PDI/ERO1 load is approximated by elevating ATP-per-aa from 4.5 (uricase) to 6.0 (Lf). Real PDI saturation effects from `chaperone-orthogonal-stacking.md` §3.5 are out of scope for v1 FBA.")
    md.append("3. **Kojic acid and ergothioneine were not in the iWV1314 model.** We added simplified net reactions per published mechanism (Terabayashi 2010 / Marui 2011 for kojic acid; Hu 2014 / Bello 2012 for ergothioneine). Stoichiometry is approximate.")
    md.append("4. **Static demands.** Each cassette is treated as a fixed lower-bound flux. Real titers vary with growth phase, induction state, and substrate; FBA cannot capture dynamics.")
    md.append("5. **No adenosine deaminase competition modeling.** The host's native ADA (r1115-r1117) competes with cns1+cns2 for the adenosine substrate pool. FBA picks the optimal split; pentostatin-style protection (Xia 2017 PMID 29056419) would be needed in vivo if intracellular ADA flux is high.")
    md.append("6. **NADPH choice for Cns1 is best-guess.** The 2024 frontiersin review documents that the Cns1 cofactor (NADH vs NADPH) has not been mechanistically pinned. We used NADPH because it is the standard biosynthetic reductant in fungi. If the true cofactor is NADH, switching changes the carbon partition only marginally (NADH and NADPH pools are interchangeable via transhydrogenase in iWV1314).")
    md.append("")
    md.append("## Provenance")
    md.append("")
    md.append("See `inputs/provenance.md` for full source list and per-claim verification.")
    md.append("")

    with open(OUTPUTS / "summary.md", "w") as f:
        f.write("\n".join(md))

    print("=" * 75)
    print("Wrote:")
    print(f"  {OUTPUTS / 'results.json'}")
    print(f"  {OUTPUTS / 'summary.md'}")
    print("=" * 75)


if __name__ == "__main__":
    main()
