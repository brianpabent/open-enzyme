"""
Build the multilingual query plan for the Houttuynia cordata polysaccharide
structure-activity lit scan (2026-07-14).

Scope: fraction-directionality problem — which HCP fraction is pro- vs
anti-inflammatory, what structural feature predicts direction, and what
commercial capsule extracts actually contain. Feeds wet-lab §1.30 Arm A choice
+ a pro-inflammatory-directionality safety caution.
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "wiki/etc/experiments/lib"))

from agentic_lit_synthesis import (  # noqa: E402
    build_language_native_query_plan,
    audit_query_strategy_language_framing,
    write_json,
)

HERE = Path(__file__).resolve().parent

# Western mechanism-name frame (PubMed / English)
western = [
    "Houttuynia cordata polysaccharide structure",
    "Houttuynia cordata polysaccharide anti-inflammatory",
    "Houttuynia cordata polysaccharide TLR4",
    "Houttuynia cordata polysaccharide complement",
    "Houttuynia cordata homogalacturonan",
    "Houttuynia cordata polysaccharide macrophage IL-1beta",
    "Houttuynia cordata polysaccharide NLRP3",
    "Houttuynia cordata polysaccharide molecular weight monosaccharide",
    "HCPM Houttuynia polysaccharide",
    "Houttuynia cordata pectin rhamnogalacturonan",
    "Houttuynia cordata polysaccharide pro-inflammatory PBMC",
    "Houttuynia cordata capsule extract composition",
]

plan = build_language_native_query_plan(
    scope="Houttuynia cordata polysaccharide fraction structure-activity / directionality (pro- vs anti-inflammatory) for MSU-NLRP3 gout screen §1.30",
    # mechanism frame: use raw mechanism labels (native map covers NLRP3/complement/inflammation)
    mechanisms=["NLRP3", "complement", "inflammation"],
    species=["鱼腥草", "魚腥草", "蕺菜", "Houttuynia cordata"],
    # not a single classical formula per se, but Houttuynia appears in these; include as formula frame
    formulas=["鱼腥草", "鱼腥草多糖", "蕺菜"],
    pathologies=["inflammation", "complement"],
    languages=("zh", "ja", "ko"),
    western_queries=western,
    natural_product_scope=True,
)

# Enrich zh frame with polysaccharide-structure-specific native terms the generic
# map doesn't include (多糖 structure / fraction-directionality vocabulary).
zh_structure_terms = [
    "鱼腥草多糖 结构",           # HCP structure
    "鱼腥草多糖 单糖组成",       # monosaccharide composition
    "鱼腥草多糖 分子量",         # molecular weight
    "鱼腥草多糖 抗炎",           # anti-inflammatory
    "鱼腥草多糖 促炎",           # pro-inflammatory
    "鱼腥草多糖 巨噬细胞",       # macrophage
    "鱼腥草多糖 TLR4",
    "鱼腥草多糖 补体",           # complement
    "鱼腥草多糖 同型半乳糖醛酸聚糖",  # homogalacturonan
    "鱼腥草 果胶多糖",           # pectic polysaccharide
    "鱼腥草多糖 白细胞介素",     # interleukin
    "鱼腥草多糖 免疫调节",       # immunomodulation
    "鱼腥草胶囊 成分",           # capsule composition
    "鱼腥草多糖 提取 纯化",      # extraction/purification
    "HCPM 鱼腥草",
    "蕺菜多糖 结构 活性",        # Houttuynia (alt name) polysaccharide structure-activity
]
for framing in plan["framings"]:
    if framing.get("language") == "zh" and framing.get("type") == "mechanism_native":
        framing["queries"] = list(dict.fromkeys(framing["queries"] + zh_structure_terms))

audit = audit_query_strategy_language_framing(plan)

write_json(HERE / "inputs" / "query-strategy.json", {"plan": plan, "audit": audit})
print(json.dumps(audit, indent=2, ensure_ascii=False))
print("\nframe types present:", sorted({f["type"] for f in plan["framings"]}))
n = sum(len(f["queries"]) for f in plan["framings"])
print("total queries:", n)
