#!/usr/bin/env python3
"""
comp-039 per-candidate query plan builder.

Builds multi-frame query plans (Western mechanism + native zh/ja mechanism +
species + traditional formula + traditional pathology) for the four candidates
under CFH-dependence classification: rosmarinic acid, luteolin, Houttuynia
cordata polysaccharide (HCP/HCPM), Helicteres benzofuran lignans.

Writes JSON into ../inputs/per-candidate-query-plan.json.
"""

from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
LIB = HERE.parent.parent.parent / "wiki" / "etc" / "experiments" / "lib"
sys.path.insert(0, str(LIB))

from agentic_lit_synthesis import (  # noqa: E402
    audit_query_strategy_language_framing,
    build_language_native_query_plan,
    write_json,
)


CANDIDATES = [
    {
        "candidate": "rosmarinic_acid",
        "scope": (
            "comp-039 CFH-dependence classification of rosmarinic acid: "
            "binding-site evidence relative to CFH CCP6-8 Y402H footprint. "
            "Anchored on Sahu 1999 (C3b covalent IC50 34 μM), Englberger 1988 "
            "(C3 convertase IC50 5-10 μM), Peake 1991 (C5 convertase 1500 μM)."
        ),
        "mechanisms": ["complement"],
        "pathologies": ["complement", "inflammation", "gout"],
        "species": ["迷迭香", "紫苏", "ローズマリー"],
        "formulas": [],
        "western_queries": [
            "rosmarinic acid C3 convertase",
            "rosmarinic acid C3b covalent",
            "rosmarinic acid complement factor H",
            "rosmarinic acid CFH binding",
            "rosmarinic acid alternative pathway complement",
            "rosmarinic acid classical pathway complement",
            "rosmarinic acid C5 convertase",
            "Sahu Pangburn rosmarinic C3b",
            "Englberger rosmarinic C3 convertase",
            "Peake rosmarinic C5 convertase",
        ],
    },
    {
        "candidate": "luteolin",
        "scope": (
            "comp-039 CFH-dependence classification of luteolin: binding-site "
            "evidence relative to CFH CCP6-8 Y402H footprint. Anchored on "
            "Zhang & Chen 2008 (PMC7126446) CH50 0.19 mM / AP50 0.17 mM."
        ),
        "mechanisms": ["complement"],
        "pathologies": ["complement", "inflammation", "gout"],
        "species": ["木犀草", "苦地胆", "ルテオリン"],
        "formulas": [],
        "western_queries": [
            "luteolin C3 convertase",
            "luteolin C3b binding",
            "luteolin complement factor H",
            "luteolin CFH binding",
            "luteolin alternative pathway complement",
            "luteolin classical pathway complement CH50",
            "luteolin C5 convertase",
            "luteolin C1q binding",
            "flavonoid complement factor H displacement",
            "flavonoid C3b binding site",
        ],
    },
    {
        "candidate": "houttuynia_cordata_polysaccharide",
        "scope": (
            "comp-039 CFH-dependence classification of Houttuynia cordata "
            "polysaccharide (HCP/HCPM): binding-site / multi-target evidence "
            "relative to CFH CCP6-8. Anchored on Chen Daofeng / Fudan papers, "
            "Li 2025 PMC12254813, Yu 2026 PMC12937656, Cheng 2014 PMC7112369."
        ),
        "mechanisms": ["complement"],
        "pathologies": ["complement", "inflammation"],
        "species": ["鱼腥草", "蕺菜", "どくだみ"],
        "formulas": [],
        "western_queries": [
            "Houttuynia cordata polysaccharide complement",
            "Houttuynia anticomplementary polysaccharide",
            "Houttuynia C2 C4 binding",
            "Houttuynia C3 convertase",
            "Houttuynia complement factor H",
            "Houttuynia TLR4 MD-2 polysaccharide",
            "HCP HCPM anticomplementary",
            "Chen Daofeng Houttuynia anticomplementary",
            "Houttuynia gout hyperuricemia polysaccharide",
            "Houttuynia NLRP3 inflammasome polysaccharide",
        ],
    },
    {
        "candidate": "helicteres_benzofuran_lignans",
        "scope": (
            "comp-039 CFH-dependence classification of Helicteres angustifolia "
            "benzofuran sesquilignans (machicendonal compound 4; "
            "dihydrodehydrodiconiferyl alcohol compound 5). Anchored on "
            "Yin 2016 PMC6273495 (CH50 9 / 40 μM). Single-paper finding."
        ),
        "mechanisms": ["complement"],
        "pathologies": ["complement", "inflammation"],
        "species": ["山芝麻", "Helicteres angustifolia"],
        "formulas": [],
        "western_queries": [
            "Helicteres angustifolia anticomplementary",
            "Helicteres benzofuran lignan C1q",
            "Helicteres compound 5 dihydrodehydrodiconiferyl",
            "Helicteres machicendonal CH50",
            "Yin 2016 Helicteres complement",
            "benzofuran lignan complement factor H",
            "benzofuran lignan C3 convertase",
            "Sterculiaceae anticomplementary lignan",
        ],
    },
]


def main():
    plans = {}
    for candidate in CANDIDATES:
        plan = build_language_native_query_plan(
            scope=candidate["scope"],
            mechanisms=candidate["mechanisms"],
            species=candidate["species"],
            formulas=candidate["formulas"],
            pathologies=candidate["pathologies"],
            languages=("zh", "ja"),
            western_queries=candidate["western_queries"],
            natural_product_scope=True,
        )
        audit = audit_query_strategy_language_framing(plan, languages=("zh", "ja"))
        plans[candidate["candidate"]] = {
            "candidate": candidate["candidate"],
            "plan": plan,
            "audit": audit,
        }

    out = HERE.parent / "inputs" / "per-candidate-query-plan.json"
    write_json(out, plans)
    print(f"Wrote {out}")
    for name, payload in plans.items():
        print(f"  {name}: audit={payload['audit']['verdict']}")


if __name__ == "__main__":
    main()
