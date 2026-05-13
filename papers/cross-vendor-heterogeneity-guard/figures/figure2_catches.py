#!/usr/bin/env python3
"""
Figure 2 — Failure-class taxonomy for the cross-vendor heterogeneity-guard paper.

Recast (2026-05-13 per Codex external review):
Earlier version was a bar chart with N=1 per class, which read as a
quantitative distribution and overclaimed the operational record. This
version is a taxonomy: one cell per failure class, with the operational
exemplar and surfacing mechanism. Explicitly qualitative.

Session 9 expansion (2026-05-13): added a fifth cell for §5.6 (corpus-level
contamination) since the audit-driven addition to the paper makes this a
distinct failure class with its own defense mechanism (verification-of-
verification chains targeting primary source, distinct from both cross-
vendor review and within-pipeline manual discipline).

Run: python3 figure2_catches.py
Outputs: figure2_catches.pdf, figure2_catches.png (300dpi)
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

OUT_DIR = Path(__file__).parent

COLORS = {
    "anthropic": "#D4A574",
    "deepseek":  "#5B5B9F",
    "google":    "#5C7C8E",
    "openai":    "#6B8B6B",
    "manual":    "#888888",
    "vov":       "#A05858",  # V-of-V chains; matches Figure 1's human-in-loop red
}

# The five classes, presented as a taxonomy
CLASSES = [
    {
        "title": "Within-vendor cascade",
        "exemplar": "§5.1 — DAF SCR1-4\ndisulfide-count\nhallucination",
        "exemplar_date": "2026-05-06",
        "surfacing": "Pass 2 cross-reference\n+ manual UniProt\ngrep-verify",
        "surfacing_color": "manual",
        "what_it_is": "Single-vendor hallucination\npropagates across multiple\nwiki pages, plausible enough\nto evade casual review.",
    },
    {
        "title": "Upstream-of-subagent\ncontamination",
        "exemplar": "§5.2 — comp-018\nrosmarinic-framing\nbias",
        "exemplar_date": "2026-05-08",
        "surfacing": "Independent re-run\n(comp-020, scrubbed\nbrief)",
        "surfacing_color": "manual",
        "what_it_is": "User framing in subagent\nbrief biases the subagent's\nheadline finding via\nnarrative cohesion.",
    },
    {
        "title": "External-tool\nreliability failure",
        "exemplar": "§5.3 — Paperclip MCP\nmap-operator probe",
        "exemplar_date": "2026-05-05",
        "surfacing": "Ground-truth probe\n(12-paper uricase\nset)",
        "surfacing_color": "manual",
        "what_it_is": "Tool returns plausible-\nlooking but fabricated\nquantitative values; caught\nonly by pre-integration probe.",
    },
    {
        "title": "Cross-vendor\nmethodological catch",
        "exemplar": "§5.4 — DeepSeek\nConnection 7 self-flag",
        "exemplar_date": "2026-04-25",
        "surfacing": "DeepSeek V4-Pro\nindependent\npeer-review",
        "surfacing_color": "deepseek",
        "what_it_is": "Risk class invisible from\nwithin the dominant vendor's\npipeline because the blind\nspot aligns with its own prior.",
    },
    {
        "title": "Corpus-level\ncontamination",
        "exemplar": "§5.6 — Tongkat ali\ncitation laundering /\neurycomanone reversal",
        "exemplar_date": "2026-05-07",
        "surfacing": "Verification-of-\nverification chain\n(primary-source)",
        "surfacing_color": "vov",
        "what_it_is": "Contamination distributes\nidentically across vendors\nbecause it is in every\nvendor's training corpus.",
    },
]


def make_cell(ax, x, y, w, h, cls):
    # Cell vertical layout (top-to-bottom in y-coordinates):
    #   title banner   (top 12% of cell)
    #   what-it-is     (next ~30%)
    #   exemplar       (next ~30%)
    #   surfacing band (bottom 28%)
    top = y + h
    band_h_title = h * 0.13
    band_h_surf  = h * 0.28

    # Outer box
    box = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0,rounding_size=0.05",
        linewidth=1.2, edgecolor="#333333", facecolor="white",
    )
    ax.add_patch(box)

    # Title banner (top)
    title_bg = FancyBboxPatch(
        (x, top - band_h_title), w, band_h_title,
        boxstyle="round,pad=0,rounding_size=0.05",
        linewidth=0, facecolor="#E8E8E8",
    )
    ax.add_patch(title_bg)
    ax.text(x + w/2, top - band_h_title/2, cls["title"],
            ha="center", va="center", fontsize=10, fontweight="bold",
            color="#222222")

    # What-it-is description
    ax.text(x + 0.06, top - band_h_title - 0.08, cls["what_it_is"],
            ha="left", va="top", fontsize=8.5, color="#333333",
            linespacing=1.3)

    # Exemplar section (middle-bottom area)
    exemplar_label_y = y + band_h_surf + 0.85
    ax.text(x + 0.06, exemplar_label_y, "Exemplar:",
            ha="left", va="top", fontsize=8, color="#555555", style="italic")
    ax.text(x + 0.06, exemplar_label_y - 0.12, cls["exemplar"],
            ha="left", va="top", fontsize=8.5, color="#222222",
            fontweight="semibold", linespacing=1.3)
    # Date sits BELOW the exemplar block, accounting for ~3 wrapped lines
    ax.text(x + 0.06, y + band_h_surf + 0.10, cls["exemplar_date"],
            ha="left", va="top", fontsize=7.5, color="#777777")

    # Surfacing band (bottom)
    band_color = COLORS[cls["surfacing_color"]]
    band = FancyBboxPatch(
        (x, y), w, band_h_surf,
        boxstyle="round,pad=0,rounding_size=0.05",
        linewidth=0, facecolor=band_color,
    )
    ax.add_patch(band)
    text_color = "white" if cls["surfacing_color"] != "anthropic" else "black"
    ax.text(x + w/2, y + band_h_surf * 0.72, "Surfaced by",
            ha="center", va="center", fontsize=7.5, color=text_color,
            style="italic")
    ax.text(x + w/2, y + band_h_surf * 0.32, cls["surfacing"],
            ha="center", va="center", fontsize=8.5, color=text_color,
            fontweight="bold", linespacing=1.2)


def main():
    fig, ax = plt.subplots(figsize=(16, 6.2))
    ax.set_xlim(0, 12.5)
    ax.set_ylim(0, 5.0)
    ax.axis("off")

    # 1x5 layout, same per-cell dimensions; figsize widened to fit.
    cell_w = 2.30
    cell_h = 3.9
    gap = 0.18
    y = 0.4
    n = len(CLASSES)
    start_x = (12.5 - n*cell_w - (n-1)*gap) / 2

    for i, cls in enumerate(CLASSES):
        x = start_x + i * (cell_w + gap)
        make_cell(ax, x, y, cell_w, cell_h, cls)

    # Title + caption (centered above the cell row)
    ax.text(6.25, 4.80,
            "Figure 2. Failure-class taxonomy for the cross-vendor heterogeneity guard",
            ha="center", fontsize=11.5, fontweight="bold")
    ax.text(6.25, 4.52,
            "Each cell is qualitative (N=1 in the 13-day operational window); the figure is a taxonomy of failure classes, not a frequency distribution.",
            ha="center", fontsize=8.5, style="italic", color="#555555")

    # Legend
    handles = [
        mpatches.Patch(facecolor=COLORS["deepseek"],
                       label="Cross-vendor surfacing (DeepSeek)"),
        mpatches.Patch(facecolor=COLORS["manual"],
                       label="Within-pipeline manual discipline"),
        mpatches.Patch(facecolor=COLORS["vov"],
                       label="Verification-of-verification (primary-source chain)"),
    ]
    ax.legend(handles=handles, loc="lower center", fontsize=8.5,
              ncol=3, frameon=False, bbox_to_anchor=(0.5, -0.04))

    plt.tight_layout()
    pdf_path = OUT_DIR / "figure2_catches.pdf"
    png_path = OUT_DIR / "figure2_catches.png"
    plt.savefig(pdf_path, bbox_inches="tight")
    plt.savefig(png_path, bbox_inches="tight", dpi=300)
    print(f"Wrote {pdf_path}")
    print(f"Wrote {png_path}")


if __name__ == "__main__":
    main()
