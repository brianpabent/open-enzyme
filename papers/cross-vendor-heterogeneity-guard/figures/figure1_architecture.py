#!/usr/bin/env python3
"""
Figure 1 - Cross-vendor heterogeneity guard architecture (two-layer pattern).

Layer 1: Vibe-science interactive (Brian + Anthropic Claude Opus).
Layer 2: Automated sweep daemon
   Pass 1 propagate: DeepSeek V4-Pro
   Pass 2 synthesize: DeepSeek V4-Pro (Gemini 2.5 Pro automatic fallback)
   Pass 3 review: OpenAI GPT-5.5 (Anthropic Claude Opus 4.7 alternate)
Plus episodic peer-review pass (dashed independent verification).

Model assignments verified against:
 - .github/workflows/wiki-sweep.yml line 185 (Pass 1 --model deepseek/deepseek-v4-pro)
 - scripts/synthesize.py lines 92-93 (Pass 2 DEFAULT_MODEL + FALLBACK_MODELS)
 - .github/workflows/wiki-sweep.yml line 357 (Pass 3 REVIEWER_MODEL: openai/gpt-5.5)

Run: python3 figure1_architecture.py
Outputs: figure1_architecture.pdf, figure1_architecture.png (300dpi)
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
    "neutral":   "#999999",
    "trigger":   "#444444",
    "output":    "#444444",
    "human":     "#A05858",
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


def arrow(ax, x1, y1, x2, y2, label=None, dashed=False, color="black", offset=0.0):
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
                fontsize=7.5, color=color, style="italic",
                bbox=dict(facecolor="white", edgecolor="none", pad=1.5))


def main():
    fig, ax = plt.subplots(figsize=(11, 7.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # === LAYER 1: Vibe-Science Interactive ===
    # Banner label
    ax.text(0.2, 6.85, "Layer 1 - Vibe-science interactive (origination)",
            ha="left", va="center", fontsize=9.5, fontweight="bold",
            color="#444444")

    # Author + Claude box
    make_box(ax, 0.2, 5.9, 3.2, 0.85,
             "Brian + Anthropic Claude Opus\n(Claude Code; curiosity, picks threads,\nnames sub-claims, comp-NNN before wet-lab)",
             fc=COLORS["anthropic"], text_color="black", fontsize=8)

    # Arrow from Layer 1 to wiki
    arrow(ax, 1.8, 5.9, 1.8, 5.35, color=COLORS["neutral"], label="wiki/*.md edits", offset=0.0)

    # Wiki node
    make_box(ax, 0.6, 4.5, 2.4, 0.7,
             "Wiki corpus\n~95 pages, ~625k tokens",
             fc="#777777", fontsize=8)

    # Arrow from wiki to git push (trigger)
    arrow(ax, 1.8, 4.5, 1.8, 3.95, color=COLORS["neutral"], label="git push", offset=0.0)

    # === LAYER 2: Automated Sweep Daemon ===
    # Banner label
    ax.text(0.2, 4.05, "Layer 2 - Automated sweep daemon",
            ha="left", va="center", fontsize=9.5, fontweight="bold",
            color="#444444")

    # Trigger
    make_box(ax, 0.2, 3.0, 1.7, 0.6, "Trigger\ngit push wiki/*.md",
             fc=COLORS["trigger"], fontsize=8)

    # Pass 1
    make_box(ax, 2.4, 2.8, 1.95, 1.0,
             "Pass 1 - Propagate\nDeepSeek V4-Pro\n(DeepSeek)",
             fc=COLORS["deepseek"], fontsize=8.5)

    # Pass 2
    make_box(ax, 4.95, 2.8, 1.95, 1.0,
             "Pass 2 - Synthesize\nDeepSeek V4-Pro\n(Gemini fallback)",
             fc=COLORS["deepseek"], fontsize=8.5)

    # Pass 3
    make_box(ax, 7.5, 2.8, 1.95, 1.0,
             "Pass 3 - Review\nOpenAI GPT-5.5\n(Claude Opus alt.)",
             fc=COLORS["openai"], fontsize=8.5)

    # Inter-pass artifacts
    arrow(ax, 1.9, 3.3, 2.4, 3.3, color=COLORS["neutral"])
    arrow(ax, 4.35, 3.3, 4.95, 3.3,
          label="propagated_files\n+ trigger_files", offset=0.4)
    arrow(ax, 6.9, 3.3, 7.5, 3.3,
          label="cited_files\n+ synthesis_log", offset=0.4)

    # Output: synthesis/queue/
    make_box(ax, 7.5, 1.4, 1.95, 0.7, "Output\nsynthesis/queue/",
             fc=COLORS["output"], fontsize=8)
    arrow(ax, 8.48, 2.8, 8.48, 2.1, color=COLORS["neutral"])

    # Walkthrough arrow: human-driven closure back to Layer 1
    arrow(ax, 7.5, 1.75, 1.8, 5.9, dashed=True, color=COLORS["human"],
          label="human walkthrough\n(close + action)", offset=0.0)

    # === Episodic Peer-Review Pass ===
    ax.text(0.2, 0.92, "Episodic peer-review pass (independent verification, off the critical path)",
            ha="left", va="center", fontsize=9, fontweight="bold",
            color="#444444", style="italic")

    make_box(ax, 4.95, 0.2, 1.95, 0.55,
             "Peer-Review (episodic)\nIndependent vendor",
             fc=COLORS["deepseek"], fontsize=7.5)
    # substrate arrow from wiki down to peer-review
    arrow(ax, 3.0, 4.6, 5.0, 0.75, dashed=True, color=COLORS["deepseek"],
          label="substrate", offset=0.0)

    # audit-trail box
    make_box(ax, 7.5, 0.2, 1.95, 0.55,
             "Audit trail\nlogs/v4-peer-review-*.md",
             fc=COLORS["output"], fontsize=7.5)
    arrow(ax, 6.9, 0.47, 7.5, 0.47, color=COLORS["deepseek"], dashed=True)

    # === Title + OpenRouter note ===
    ax.text(5.0, 7.30, "Figure 1. Cross-vendor heterogeneity guard architecture",
            ha="center", fontsize=11.5, fontweight="bold")
    ax.text(5.0, 7.05, "Two layers, three-to-four vendors. All daemon calls routed via OpenRouter HTTP gateway.",
            ha="center", fontsize=8.5, style="italic", color="#555555")

    # Legend
    handles = [
        patches.Patch(facecolor=COLORS["anthropic"], label="Anthropic (Layer 1)"),
        patches.Patch(facecolor=COLORS["deepseek"], label="DeepSeek (Pass 1+2)"),
        patches.Patch(facecolor=COLORS["openai"], label="OpenAI (Pass 3)"),
        patches.Patch(facecolor=COLORS["google"], label="Google (Pass 2 fallback)"),
    ]
    ax.legend(handles=handles, loc="lower right", fontsize=8, ncol=4,
              frameon=False, bbox_to_anchor=(0.98, -0.04))

    plt.tight_layout()
    pdf_path = OUT_DIR / "figure1_architecture.pdf"
    png_path = OUT_DIR / "figure1_architecture.png"
    plt.savefig(pdf_path, bbox_inches="tight")
    plt.savefig(png_path, bbox_inches="tight", dpi=300)
    print(f"Wrote {pdf_path}")
    print(f"Wrote {png_path}")


if __name__ == "__main__":
    main()
