#!/usr/bin/env python3
"""
Figure 1 - The two-layer cross-vendor cycle.

Visual structure:
- TOP band: Layer 1 (vibe-science). Faint amber-tinted region containing
  the Author + Claude Opus box. Output: new wiki content.
- MIDDLE band (handoff): Wiki corpus, sitting on the boundary between
  layers because it's Layer 1's output and Layer 2's input.
- BOTTOM band: Layer 2 (automated sweep daemon). Faint indigo-tinted
  region containing Pass 1, Pass 2, Pass 3, synthesis queue, and the
  human walkthrough that closes the loop.
- A prominent curved arrow returns from the walkthrough (Layer 2) up
  through the wiki boundary and back into the Author box (Layer 1),
  making the cycle visible.
- The episodic peer-review pass is shown OFF both bands at the bottom
  as a dotted optional branch from the walkthrough.

Model assignments (all verified against the codebase):
 - Layer 1 - Anthropic Claude Opus (interactive, via Claude Code)
 - Layer 2 Pass 1 - DeepSeek V4-Pro (.github/workflows/wiki-sweep.yml:185)
 - Layer 2 Pass 2 - DeepSeek V4-Pro primary, Google Gemini 2.5 Pro
   automatic fallback (scripts/synthesize.py:92-93)
 - Layer 2 Pass 3 - OpenAI GPT-5.5 (.github/workflows/wiki-sweep.yml:357)
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
    "trigger":   "#444444",
    "output":    "#444444",
    "human":     "#A05858",
    "loop":      "#A05858",
}

# Faint layer-background tints (very light wash of the layer's primary vendor)
LAYER1_BG = "#FAF1E0"  # very pale amber
LAYER2_BG = "#EEEEF5"  # very pale indigo
BAND_EDGE = "#CCCCCC"


def make_box(ax, x, y, w, h, text, fc, ec="black", lw=1.2, text_color="white", fontsize=9):
    box = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.05,rounding_size=0.1",
        linewidth=lw, edgecolor=ec, facecolor=fc,
    )
    ax.add_patch(box)
    ax.text(x + w/2, y + h/2, text, ha="center", va="center",
            color=text_color, fontsize=fontsize, fontweight="bold")


def straight_arrow(ax, x1, y1, x2, y2, label=None, dashed=False, color="black",
                   offset=0.0, fontsize=7.5, lw=1.2):
    style = "--" if dashed else "-"
    arr = FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle="->", mutation_scale=18,
        linewidth=lw, color=color, linestyle=style,
    )
    ax.add_patch(arr)
    if label:
        mx, my = (x1 + x2)/2, (y1 + y2)/2 + offset
        ax.text(mx, my, label, ha="center", va="center",
                fontsize=fontsize, color=color, style="italic",
                bbox=dict(facecolor="white", edgecolor="none", pad=1.5))


def main():
    fig, ax = plt.subplots(figsize=(13, 9))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 9)
    ax.axis("off")

    # ===== Title row =====
    ax.text(6.5, 8.65,
            "Figure 1. The two-layer cross-vendor cycle",
            ha="center", fontsize=12, fontweight="bold")
    ax.text(6.5, 8.30,
            "Layer 1 originates new content via vibe-science. The wiki corpus is the handoff. Layer 2 propagates and reviews automatically. The human triages and the cycle restarts.",
            ha="center", fontsize=8.5, style="italic", color="#555555")

    # ===== Layer 1 background band =====
    # Top region covering Layer 1 box. Use a soft amber background to make
    # the layer visually distinct without dominating the figure.
    layer1_band = Rectangle((0.2, 6.6), 12.6, 1.4,
                            facecolor=LAYER1_BG, edgecolor=BAND_EDGE,
                            linewidth=0.8, linestyle=":")
    ax.add_patch(layer1_band)
    ax.text(0.4, 7.85, "Layer 1 - Vibe-science (origination)",
            ha="left", va="center", fontsize=10, fontweight="bold",
            color="#7A5A2E")

    # Layer 1 box: author + Claude Opus
    make_box(ax, 0.6, 6.85, 4.0, 1.0,
             "Author + Anthropic Claude Opus\n(Claude Code: curiosity, picks threads,\nnames sub-claims, comp-NNN before wet-lab)",
             fc=COLORS["anthropic"], text_color="black", fontsize=8.5)

    # Layer 1 narrative on the right side of the band
    ax.text(8.7, 7.35,
            "The author drives synthesis with an\nAnthropic Claude Opus session: leading\nwith curiosity, picking threads worth pulling,\nrunning comp-NNN computational experiments\nbefore any wet-lab spend.",
            ha="left", va="center", fontsize=8.5, color="#444444",
            style="italic")

    # ===== Wiki handoff (between the layers) =====
    # Down arrow from Layer 1 box to wiki
    straight_arrow(ax, 2.6, 6.85, 2.6, 6.20, color=COLORS["neutral"],
                   label="new wiki content", offset=0.0)

    make_box(ax, 1.3, 5.6, 2.6, 0.6,
             "Wiki corpus\n~95 pages, ~625k tokens",
             fc="#777777", fontsize=8.5)

    ax.text(4.3, 5.9,
            "(the handoff: Layer 1 writes, Layer 2 reads)",
            ha="left", va="center", fontsize=8, color="#666666", style="italic")

    # ===== Layer 2 background band =====
    layer2_band = Rectangle((0.2, 1.7), 12.6, 3.4,
                            facecolor=LAYER2_BG, edgecolor=BAND_EDGE,
                            linewidth=0.8, linestyle=":")
    ax.add_patch(layer2_band)
    ax.text(0.4, 4.92, "Layer 2 - Automated sweep daemon",
            ha="left", va="center", fontsize=10, fontweight="bold",
            color="#3A3A6A")

    # Wiki -> Pass 1 (down + into the band)
    straight_arrow(ax, 2.6, 5.6, 2.6, 4.45, color=COLORS["neutral"],
                   label="git push triggers", offset=0.0)

    # Pass row
    make_box(ax, 1.4, 3.4, 2.2, 1.0,
             "Pass 1 - Propagate\nDeepSeek V4-Pro",
             fc=COLORS["deepseek"], fontsize=9)
    make_box(ax, 4.2, 3.4, 2.2, 1.0,
             "Pass 2 - Synthesize\nDeepSeek V4-Pro\n(Gemini fallback)",
             fc=COLORS["deepseek"], fontsize=8.5)
    make_box(ax, 7.0, 3.4, 2.2, 1.0,
             "Pass 3 - Review\nOpenAI GPT-5.5\n(Claude Opus alt.)",
             fc=COLORS["openai"], fontsize=8.5)

    # Inter-pass arrows
    straight_arrow(ax, 3.6, 3.9, 4.2, 3.9,
                   label="propagated_files\n+ trigger_files", offset=0.42)
    straight_arrow(ax, 6.4, 3.9, 7.0, 3.9,
                   label="cited_files\n+ synthesis_log", offset=0.42)

    # Pass 3 -> queue (down)
    straight_arrow(ax, 8.1, 3.4, 8.1, 2.65, color=COLORS["neutral"])
    make_box(ax, 7.0, 1.9, 2.2, 0.75,
             "synthesis/queue/\n(verdict-tagged findings)",
             fc=COLORS["output"], fontsize=8)

    # queue -> walkthrough
    straight_arrow(ax, 9.2, 2.28, 9.8, 2.28, color=COLORS["human"])
    make_box(ax, 9.8, 1.9, 2.4, 0.75,
             "Human walkthrough\n(triage: action / defer / drop)",
             fc=COLORS["human"], fontsize=8)

    # ===== THE LOOP BACK (the load-bearing visual element) =====
    # Big curved arrow from the walkthrough, up over the layer-2 band,
    # across the wiki handoff, and back into the Layer-1 box.
    arr_loop = FancyArrowPatch(
        (11.0, 2.65), (4.6, 7.35),
        arrowstyle="->", mutation_scale=24,
        linewidth=2.2, color=COLORS["loop"], linestyle="-",
        connectionstyle="arc3,rad=-0.42",
    )
    ax.add_patch(arr_loop)
    ax.text(12.55, 5.0,
            "the cycle:\nfindings re-enter\nLayer 1\n(vibe-science)\nand a new\nedit starts",
            ha="center", va="center", fontsize=8.5,
            color=COLORS["loop"], fontweight="bold",
            bbox=dict(facecolor="white", edgecolor=COLORS["loop"],
                      pad=4, boxstyle="round,pad=0.4"))

    # ===== Optional Branch: Episodic Peer-Review (below both bands) =====
    ax.text(0.2, 1.40, "Optional branch from the walkthrough (off the critical path)",
            ha="left", va="center", fontsize=8.5, fontweight="bold",
            color="#444444", style="italic")

    make_box(ax, 4.2, 0.45, 2.4, 0.55,
             "Peer-Review (episodic)\nIndependent vendor",
             fc=COLORS["deepseek"], fontsize=8)
    make_box(ax, 7.2, 0.45, 2.6, 0.55,
             "Audit trail\nlogs/v4-peer-review-*.md",
             fc=COLORS["output"], fontsize=8)
    straight_arrow(ax, 6.6, 0.72, 7.2, 0.72, dashed=True, color=COLORS["deepseek"])

    # walkthrough -> peer-review (decision arrow)
    arr_branch = FancyArrowPatch(
        (10.4, 1.9), (5.4, 1.0),
        arrowstyle="->", mutation_scale=16, linewidth=1.1,
        color=COLORS["human"], linestyle=":",
        connectionstyle="arc3,rad=0.25",
    )
    ax.add_patch(arr_branch)
    ax.text(8.0, 1.05, "when warranted:\nfire peer-review",
            ha="center", va="center", fontsize=7.5,
            color=COLORS["human"], style="italic",
            bbox=dict(facecolor="white", edgecolor="none", pad=1.5))

    # substrate arrow from wiki down to peer-review (curved left of pass row)
    arr_sub = FancyArrowPatch(
        (1.3, 5.7), (4.2, 0.72),
        arrowstyle="->", mutation_scale=14, linewidth=1.0,
        color=COLORS["deepseek"], linestyle="--",
        connectionstyle="arc3,rad=0.4",
    )
    ax.add_patch(arr_sub)
    ax.text(0.05, 2.7, "substrate", ha="left", va="center",
            fontsize=7.5, color=COLORS["deepseek"], style="italic",
            bbox=dict(facecolor="white", edgecolor="none", pad=1.5))

    # Legend at the very bottom
    handles = [
        patches.Patch(facecolor=COLORS["anthropic"], label="Anthropic (Layer 1)"),
        patches.Patch(facecolor=COLORS["deepseek"], label="DeepSeek (Pass 1+2)"),
        patches.Patch(facecolor=COLORS["openai"], label="OpenAI (Pass 3)"),
        patches.Patch(facecolor=COLORS["google"], label="Google (Pass 2 fallback)"),
        patches.Patch(facecolor=COLORS["human"], label="Human-in-the-loop"),
    ]
    ax.legend(handles=handles, loc="lower center", fontsize=8, ncol=5,
              frameon=False, bbox_to_anchor=(0.5, -0.04))

    plt.tight_layout()
    pdf_path = OUT_DIR / "figure1_architecture.pdf"
    png_path = OUT_DIR / "figure1_architecture.png"
    plt.savefig(pdf_path, bbox_inches="tight")
    plt.savefig(png_path, bbox_inches="tight", dpi=300)
    print(f"Wrote {pdf_path}")
    print(f"Wrote {png_path}")


if __name__ == "__main__":
    main()
