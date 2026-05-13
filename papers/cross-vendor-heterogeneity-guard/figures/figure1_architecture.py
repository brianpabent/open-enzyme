#!/usr/bin/env python3
"""
Figure 1 - Cross-vendor heterogeneity guard architecture (two-layer cycle).

The architecture is a LOOP, not a linear pipeline:

  Vibe-science (Brian + Claude Opus)
      |
      v  (new wiki content)
  Wiki corpus
      |
      v  (git push triggers daemon)
  Pass 1 DeepSeek -> Pass 2 DeepSeek/Gemini -> Pass 3 GPT-5.5
                                                       |
                                                       v
                                              synthesis/queue/
                                                       |
                                                       v
                                              Human walkthrough  ----+
                                                       |             |
                                  (back into vibe-science: cycle)    |
                                                                     v
                                                          (optional branch)
                                                            Episodic peer-review pass
                                                            (independent vendor on
                                                             wiki substrate -> audit trail)

Model assignments verified against:
 - .github/workflows/wiki-sweep.yml line 185 (Pass 1 deepseek/deepseek-v4-pro)
 - scripts/synthesize.py lines 92-93 (Pass 2 default + fallback)
 - .github/workflows/wiki-sweep.yml line 357 (Pass 3 openai/gpt-5.5)
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
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


def make_box(ax, x, y, w, h, text, fc, ec="black", lw=1.2, text_color="white", fontsize=9):
    box = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.05,rounding_size=0.1",
        linewidth=lw, edgecolor=ec, facecolor=fc,
    )
    ax.add_patch(box)
    ax.text(x + w/2, y + h/2, text, ha="center", va="center",
            color=text_color, fontsize=fontsize, fontweight="bold")


def straight_arrow(ax, x1, y1, x2, y2, label=None, dashed=False, color="black", offset=0.0, fontsize=7.5):
    style = "--" if dashed else "-"
    arr = FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle="->", mutation_scale=18,
        linewidth=1.2, color=color, linestyle=style,
    )
    ax.add_patch(arr)
    if label:
        mx, my = (x1 + x2)/2, (y1 + y2)/2 + offset
        ax.text(mx, my, label, ha="center", va="center",
                fontsize=fontsize, color=color, style="italic",
                bbox=dict(facecolor="white", edgecolor="none", pad=1.5))


def curved_arrow(ax, x1, y1, x2, y2, rad=-0.3, color="black", dashed=False, lw=1.4):
    style = "--" if dashed else "-"
    arr = FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle="->", mutation_scale=20,
        linewidth=lw, color=color, linestyle=style,
        connectionstyle=f"arc3,rad={rad}",
    )
    ax.add_patch(arr)


def main():
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 8)
    ax.axis("off")

    # ===== Title =====
    ax.text(6.5, 7.65,
            "Figure 1. The two-layer cross-vendor cycle",
            ha="center", fontsize=11.5, fontweight="bold")
    ax.text(6.5, 7.35,
            "Vibe-science originates → daemon propagates and reviews → human triages → cycle restarts. All daemon calls routed via OpenRouter.",
            ha="center", fontsize=8.5, style="italic", color="#555555")

    # ===== LAYER 1: Vibe-Science (top-left) =====
    ax.text(0.2, 6.85, "Layer 1 - Vibe-science interactive (origination)",
            ha="left", va="center", fontsize=9.5, fontweight="bold",
            color="#444444")
    make_box(ax, 0.2, 5.85, 3.4, 0.9,
             "Author + Anthropic Claude Opus\n(Claude Code: curiosity, picks threads,\nnames sub-claims, comp-NNN before wet-lab)",
             fc=COLORS["anthropic"], text_color="black", fontsize=8.5)

    # Down to wiki
    straight_arrow(ax, 1.9, 5.85, 1.9, 5.35, color=COLORS["neutral"],
                   label="new wiki content", offset=0.0)

    # Wiki
    make_box(ax, 0.6, 4.55, 2.6, 0.75,
             "Wiki corpus\n~95 pages, ~625k tokens",
             fc="#777777", fontsize=8.5)

    # Wiki -> Pass 1 (down + right)
    straight_arrow(ax, 1.9, 4.55, 2.9, 3.85, color=COLORS["neutral"],
                   label="git push triggers", offset=0.0)

    # ===== LAYER 2: Sweep Daemon (middle row) =====
    ax.text(0.2, 4.10, "Layer 2 - Automated sweep daemon",
            ha="left", va="center", fontsize=9.5, fontweight="bold",
            color="#444444")

    make_box(ax, 2.6, 2.85, 2.1, 1.0,
             "Pass 1 - Propagate\nDeepSeek V4-Pro",
             fc=COLORS["deepseek"], fontsize=9)
    make_box(ax, 5.3, 2.85, 2.1, 1.0,
             "Pass 2 - Synthesize\nDeepSeek V4-Pro\n(Gemini fallback)",
             fc=COLORS["deepseek"], fontsize=8.5)
    make_box(ax, 8.0, 2.85, 2.1, 1.0,
             "Pass 3 - Review\nOpenAI GPT-5.5\n(Claude Opus alt.)",
             fc=COLORS["openai"], fontsize=8.5)

    # Inter-pass arrows
    straight_arrow(ax, 4.7, 3.35, 5.3, 3.35,
                   label="propagated_files\n+ trigger_files", offset=0.4)
    straight_arrow(ax, 7.4, 3.35, 8.0, 3.35,
                   label="cited_files\n+ synthesis_log", offset=0.4)

    # Pass 3 -> queue (down)
    straight_arrow(ax, 9.05, 2.85, 9.05, 2.15, color=COLORS["neutral"])
    make_box(ax, 8.0, 1.4, 2.1, 0.75,
             "synthesis/queue/\n(verdict-tagged findings)",
             fc=COLORS["output"], fontsize=8)

    # queue -> human walkthrough (right)
    straight_arrow(ax, 10.1, 1.78, 10.7, 1.78, color=COLORS["human"])
    make_box(ax, 10.7, 1.4, 1.9, 0.75,
             "Human walkthrough\n(triage: action / defer / drop)",
             fc=COLORS["human"], fontsize=8)

    # ===== THE LOOP BACK to Vibe-Science =====
    # Human walkthrough -> back up and over to Layer 1 box.
    # Curve out to the right, up, and into the top of the Layer-1 box.
    arr_loop = FancyArrowPatch(
        (11.65, 2.15), (3.4, 6.30),
        arrowstyle="->", mutation_scale=22,
        linewidth=1.8, color=COLORS["loop"], linestyle="-",
        connectionstyle="arc3,rad=-0.35",
    )
    ax.add_patch(arr_loop)
    ax.text(12.4, 4.6, "cycle restarts:\nfindings re-enter\nvibe-science",
            ha="center", va="center", fontsize=8.5,
            color=COLORS["loop"], fontweight="bold",
            bbox=dict(facecolor="white", edgecolor=COLORS["loop"], pad=3,
                      boxstyle="round,pad=0.3"))

    # ===== Optional Branch: Episodic Peer-Review =====
    ax.text(0.2, 0.95, "Optional branch from walkthrough: episodic peer-review pass (independent vendor on wiki substrate)",
            ha="left", va="center", fontsize=8.5, fontweight="bold",
            color="#444444", style="italic")

    make_box(ax, 5.3, 0.2, 2.2, 0.55,
             "Peer-Review (episodic)\nIndependent vendor",
             fc=COLORS["deepseek"], fontsize=8)
    make_box(ax, 8.0, 0.2, 2.4, 0.55,
             "Audit trail\nlogs/v4-peer-review-*.md",
             fc=COLORS["output"], fontsize=8)
    straight_arrow(ax, 7.5, 0.47, 8.0, 0.47, dashed=True, color=COLORS["deepseek"])

    # Human walkthrough -> peer-review branch (decision arrow down)
    arr_branch = FancyArrowPatch(
        (11.0, 1.4), (6.4, 0.78),
        arrowstyle="->", mutation_scale=16, linewidth=1.1,
        color=COLORS["human"], linestyle=":",
        connectionstyle="arc3,rad=0.3",
    )
    ax.add_patch(arr_branch)
    ax.text(8.7, 1.05, "when warranted:\nfire peer-review",
            ha="center", va="center", fontsize=7.5,
            color=COLORS["human"], style="italic",
            bbox=dict(facecolor="white", edgecolor="none", pad=1.5))

    # Wiki -> peer-review substrate (curved, around the left of Pass column)
    arr_sub = FancyArrowPatch(
        (0.7, 4.55), (5.3, 0.47),
        arrowstyle="->", mutation_scale=14, linewidth=1.0,
        color=COLORS["deepseek"], linestyle="--",
        connectionstyle="arc3,rad=0.35",
    )
    ax.add_patch(arr_sub)
    ax.text(0.05, 2.4, "substrate", ha="left", va="center",
            fontsize=7.5, color=COLORS["deepseek"], style="italic",
            bbox=dict(facecolor="white", edgecolor="none", pad=1.5))

    # Legend
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
