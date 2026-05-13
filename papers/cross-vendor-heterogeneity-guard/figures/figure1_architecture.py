#!/usr/bin/env python3
"""
Figure 1 - The two-layer cross-vendor cycle.

Clean vertical-flow layout. The cycle is the figure's single load-bearing
visual element. Inter-pass artifact handoff details belong in prose, not
in the figure. The peer-review optional branch is shown as a small inset
beside the cycle, not woven through it.

Layout (top to bottom):
   +-- LAYER 1 BAND (amber) ----------------------------+
   |  Author + Anthropic Claude Opus                    |
   +-----------------+----------------------------------+
                     |  new wiki content
                     v
                Wiki corpus
                     |  git push triggers
                     v
   +-- LAYER 2 BAND (indigo) ---------------------------+
   |  Pass 1 (DeepSeek) -> Pass 2 (DeepSeek/Gemini)     |
   |                   -> Pass 3 (GPT-5.5)              |
   |                   -> synthesis/queue/              |
   +-----------------+----------------------------------+
                     |  verdict-tagged findings
                     v
              Human walkthrough
                     |
                     +--- LOOP back to Layer 1 ---^

Peer-review optional branch shown to the right as a small inset.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle
from pathlib import Path

OUT_DIR = Path(__file__).parent

COLORS = {
    "anthropic": "#D4A574",
    "deepseek":  "#5B5B9F",
    "google":    "#5C7C8E",
    "openai":    "#6B8B6B",
    "neutral":   "#888888",
    "human":     "#A05858",
    "output":    "#444444",
}

LAYER1_BG = "#FAF1E0"
LAYER2_BG = "#EEEEF5"
BAND_EDGE = "#BBBBBB"


def make_box(ax, x, y, w, h, text, fc, ec="black", lw=1.2,
             text_color="white", fontsize=9):
    box = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.05,rounding_size=0.1",
        linewidth=lw, edgecolor=ec, facecolor=fc,
    )
    ax.add_patch(box)
    ax.text(x + w/2, y + h/2, text, ha="center", va="center",
            color=text_color, fontsize=fontsize, fontweight="bold")


def vertical_arrow(ax, x, y_top, y_bot, label=None, color="black",
                   fontsize=8, lw=1.5):
    arr = FancyArrowPatch(
        (x, y_top), (x, y_bot),
        arrowstyle="->", mutation_scale=22,
        linewidth=lw, color=color,
    )
    ax.add_patch(arr)
    if label:
        ax.text(x + 0.25, (y_top + y_bot) / 2, label,
                ha="left", va="center", fontsize=fontsize,
                color=color, style="italic")


def main():
    # Tall-narrow aspect so the vertical flow reads cleanly.
    # Cycle column on the left half; peer-review inset on the right.
    fig, ax = plt.subplots(figsize=(11, 11))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 11)
    ax.axis("off")

    # Title
    ax.text(5.5, 10.80, "Figure 1. The two-layer cross-vendor cycle",
            ha="center", fontsize=12, fontweight="bold")
    ax.text(5.5, 10.45,
            "Layer 1 originates new wiki content. Layer 2 propagates and reviews it automatically. The human triages the queue and the cycle restarts.",
            ha="center", fontsize=8.5, style="italic", color="#555555")

    # === Layer 1 band (top) ===
    # Band extended up to y=10.05 to give the title breathing room above
    # the Author/Opus box (Brian's read-pass note 2026-05-13).
    band1 = Rectangle((0.5, 8.4), 6.5, 1.65, facecolor=LAYER1_BG,
                      edgecolor=BAND_EDGE, linewidth=0.8, linestyle=":")
    ax.add_patch(band1)
    ax.text(0.7, 9.88, "Layer 1 - Vibe-science (origination)",
            ha="left", va="center", fontsize=10, fontweight="bold",
            color="#7A5A2E")
    make_box(ax, 1.6, 8.55, 4.3, 1.0,
             "Author + Anthropic Claude Opus\n(via Claude Code: curiosity, picks threads,\nnames sub-claims, comp-NNN before wet-lab)",
             fc=COLORS["anthropic"], text_color="black", fontsize=9)

    # Arrow Layer 1 -> wiki
    vertical_arrow(ax, 3.75, 8.4, 7.85, label="new wiki content",
                   color=COLORS["neutral"])

    # Wiki corpus (between bands)
    make_box(ax, 2.25, 7.05, 3.0, 0.75,
             "Wiki corpus\n~95 pages, ~625k tokens",
             fc="#777777", fontsize=9)

    # Arrow wiki -> Layer 2
    vertical_arrow(ax, 3.75, 7.05, 6.45, label="git push triggers",
                   color=COLORS["neutral"])

    # === Layer 2 band ===
    band2 = Rectangle((0.5, 3.5), 6.5, 3.0, facecolor=LAYER2_BG,
                      edgecolor=BAND_EDGE, linewidth=0.8, linestyle=":")
    ax.add_patch(band2)
    ax.text(0.7, 6.25, "Layer 2 - Automated sweep daemon",
            ha="left", va="center", fontsize=10, fontweight="bold",
            color="#3A3A6A")

    # Pass row (horizontal inside Layer 2 band)
    make_box(ax, 0.7, 5.0, 1.95, 0.9,
             "Pass 1\nPropagate\nDeepSeek V4-Pro",
             fc=COLORS["deepseek"], fontsize=8.5)
    make_box(ax, 2.83, 5.0, 1.95, 0.9,
             "Pass 2\nSynthesize\nDeepSeek (Gemini fallback)",
             fc=COLORS["deepseek"], fontsize=8)
    make_box(ax, 4.96, 5.0, 1.95, 0.9,
             "Pass 3\nReview\nOpenAI GPT-5.5",
             fc=COLORS["openai"], fontsize=8.5)

    # Pass 1 -> Pass 2 -> Pass 3 (small arrows between)
    for x_start, x_end in [(2.65, 2.83), (4.78, 4.96)]:
        arr = FancyArrowPatch(
            (x_start, 5.45), (x_end, 5.45),
            arrowstyle="->", mutation_scale=14, linewidth=1.0,
            color=COLORS["neutral"])
        ax.add_patch(arr)

    # Synthesis queue centered under the pass row, narrower than passes so
    # the connecting arrow from Pass 3 reads as a clean short diagonal.
    make_box(ax, 2.4, 3.7, 3.1, 0.7,
             "synthesis/queue/  (verdict-tagged findings)",
             fc=COLORS["output"], fontsize=9)

    # Pass 3 -> queue: short straight diagonal (no kink).
    arr_p3 = FancyArrowPatch(
        (5.94, 5.0), (5.4, 4.4),
        arrowstyle="->", mutation_scale=16, linewidth=1.2,
        color=COLORS["neutral"],
    )
    ax.add_patch(arr_p3)

    # Arrow Layer 2 -> walkthrough
    vertical_arrow(ax, 3.75, 3.5, 2.25,
                   label="verdict-tagged findings", color=COLORS["human"])

    # Walkthrough
    make_box(ax, 1.4, 1.4, 4.7, 0.85,
             "Human walkthrough\n(triage: action / defer / drop)",
             fc=COLORS["human"], fontsize=9.5)

    # === LOOP back to Layer 1 ===
    # Three explicit segments (left, up, right) so the arrow arrives at
    # Author's left edge perpendicularly.  Arc3 curves can't produce this
    # arrival geometry (control-point constraint), and a free-bowing arc
    # reads as "where is this arrow going" rather than "cycle."
    LOOP_X = 0.45
    loop_color = COLORS["human"]
    loop_lw = 2.6
    # Bottom: walkthrough left edge -> LOOP_X
    ax.plot([1.4, LOOP_X], [1.83, 1.83],
            color=loop_color, linewidth=loop_lw, solid_capstyle="round")
    # Vertical: up the left side
    ax.plot([LOOP_X, LOOP_X], [1.83, 9.05],
            color=loop_color, linewidth=loop_lw, solid_capstyle="round")
    # Top + arrowhead: LOOP_X -> Author's left edge
    arr_loop = FancyArrowPatch(
        (LOOP_X, 9.05), (1.6, 9.05),
        arrowstyle="->", mutation_scale=26,
        linewidth=loop_lw, color=loop_color,
    )
    ax.add_patch(arr_loop)
    # "the cycle" label inside the loop, rotated.
    ax.text(0.85, 5.4, "the cycle",
            ha="center", va="center", fontsize=10,
            color=loop_color, fontweight="bold", rotation=90)

    # === Peer-review optional branch (right column) ===
    ax.text(7.5, 6.30, "Optional branch\n(when warranted; off critical path)",
            ha="left", va="top", fontsize=9, fontweight="bold",
            color="#444444", style="italic")

    # From walkthrough into peer-review.  Use a clean right-angle elbow
    # (right first, then up) — every curve attempt at this aspect ratio
    # reads wrong; a deterministic elbow reads as "branch off the cycle."
    arr_branch = FancyArrowPatch(
        (6.1, 1.83), (8.3, 5.0),
        arrowstyle="->", mutation_scale=16, linewidth=1.1,
        color=COLORS["human"], linestyle=":",
        connectionstyle="angle,angleA=0,angleB=-90,rad=8",
    )
    ax.add_patch(arr_branch)

    # Peer-review box
    make_box(ax, 7.5, 5.0, 3.0, 0.7,
             "Peer-Review (episodic)\nIndependent vendor",
             fc=COLORS["deepseek"], fontsize=9)

    # Substrate from Layer 1 (Author/Opus) to peer-review (dashed).
    # The substrate IS the wiki corpus, but it's produced by Layer 1, so the
    # provenance line originates there (Brian's note 2026-05-13: "the line
    # should come from Layer 1").
    arr_sub = FancyArrowPatch(
        (5.9, 8.55), (8.0, 5.7),
        arrowstyle="->", mutation_scale=14, linewidth=1.0,
        color=COLORS["deepseek"], linestyle="--")
    ax.add_patch(arr_sub)
    ax.text(7.15, 7.35, "substrate", ha="left", va="center",
            fontsize=8, color=COLORS["deepseek"], style="italic")

    # Audit trail
    make_box(ax, 7.5, 3.9, 3.0, 0.7,
             "Audit trail\nlogs/v4-peer-review-*.md",
             fc=COLORS["output"], fontsize=8.5)
    arr_audit = FancyArrowPatch(
        (9.0, 5.0), (9.0, 4.6),
        arrowstyle="->", mutation_scale=14, linewidth=1.0,
        color=COLORS["deepseek"], linestyle="--")
    ax.add_patch(arr_audit)

    # Legend
    handles = [
        patches.Patch(facecolor=COLORS["anthropic"], label="Anthropic (Layer 1)"),
        patches.Patch(facecolor=COLORS["deepseek"], label="DeepSeek (Pass 1+2)"),
        patches.Patch(facecolor=COLORS["openai"], label="OpenAI (Pass 3)"),
        patches.Patch(facecolor=COLORS["google"], label="Google (Pass 2 fallback)"),
        patches.Patch(facecolor=COLORS["human"], label="Human-in-the-loop"),
    ]
    ax.legend(handles=handles, loc="lower center", fontsize=8.5, ncol=5,
              frameon=False, bbox_to_anchor=(0.5, -0.02))

    plt.tight_layout()
    pdf_path = OUT_DIR / "figure1_architecture.pdf"
    png_path = OUT_DIR / "figure1_architecture.png"
    plt.savefig(pdf_path, bbox_inches="tight")
    plt.savefig(png_path, bbox_inches="tight", dpi=300)
    print(f"Wrote {pdf_path}")
    print(f"Wrote {png_path}")


if __name__ == "__main__":
    main()
