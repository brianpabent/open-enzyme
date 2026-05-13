#!/usr/bin/env python3
"""
Figure 1 — Architecture diagram for the cross-vendor heterogeneity guard paper.

Renders a 4-pass cross-vendor sweep diagram showing:
- Trigger (git push to wiki/*.md)
- Pass 1 Propagate (Anthropic Sonnet)
- Pass 2 Synthesize (DeepSeek / Google Gemini fallback)
- Pass 3 Review (Anthropic Opus / OpenAI GPT alt.)
- Episodic peer-review pass (DeepSeek, dashed line)
- Inter-pass artifact handoff annotations
- Output to synthesis/queue/

Color codes vendors:
- Anthropic: amber (#D4A574)
- DeepSeek: indigo (#5B5B9F)
- Google: blue-grey (#5C7C8E)
- OpenAI: green-grey (#6B8B6B)

Run: python3 figure1_architecture.py
Outputs: figure1_architecture.pdf, figure1_architecture.png (300dpi)
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from pathlib import Path

OUT_DIR = Path(__file__).parent

# Vendor colors
COLORS = {
    "anthropic": "#D4A574",
    "deepseek":  "#5B5B9F",
    "google":    "#5C7C8E",
    "openai":    "#6B8B6B",
    "neutral":   "#999999",
    "trigger":   "#444444",
    "output":    "#444444",
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
    fig, ax = plt.subplots(figsize=(10, 6.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6.5)
    ax.axis("off")

    # Trigger
    make_box(ax, 0.2, 5.5, 2.0, 0.8, "Trigger\ngit push wiki/*.md",
             fc=COLORS["trigger"], fontsize=8.5)

    # Pass 1
    make_box(ax, 0.2, 3.8, 2.0, 1.2,
             "Pass 1 — Propagate\nClaude Sonnet 4.6\n(Anthropic)",
             fc=COLORS["anthropic"], text_color="black")

    # Pass 2
    make_box(ax, 3.5, 3.8, 2.0, 1.2,
             "Pass 2 — Synthesize\nDeepSeek V4-Pro\n(Gemini 2.5 Pro fallback)",
             fc=COLORS["deepseek"])

    # Pass 3
    make_box(ax, 6.8, 3.8, 2.0, 1.2,
             "Pass 3 — Review\nGPT-5.5\n(Claude Opus 4.7 alt.)",
             fc=COLORS["openai"])

    # Inter-pass artifacts
    arrow(ax, 2.2, 4.4, 3.5, 4.4,
          label="propagated_files\n+ trigger_files", offset=0.45)
    arrow(ax, 5.5, 4.4, 6.8, 4.4,
          label="cited_files\n+ synthesis_log", offset=0.45)

    # Trigger -> Pass 1
    arrow(ax, 1.2, 5.5, 1.2, 5.0, color=COLORS["neutral"])

    # Output: synthesis/queue/
    make_box(ax, 6.8, 1.8, 2.0, 0.8, "Output\nsynthesis/queue/",
             fc=COLORS["output"], fontsize=8.5)
    arrow(ax, 7.8, 3.8, 7.8, 2.6, color=COLORS["neutral"])

    # Episodic peer-review pass (dashed, independent)
    make_box(ax, 3.5, 1.8, 2.0, 0.8,
             "Peer-Review (episodic)\nDeepSeek V4-Pro\n(independent)",
             fc=COLORS["deepseek"], fontsize=7.5)
    arrow(ax, 6.8, 4.1, 5.5, 2.5, dashed=True, color=COLORS["deepseek"],
          label="substrate")
    arrow(ax, 4.5, 1.8, 1.5, 1.2, dashed=True, color=COLORS["deepseek"],
          label="differential\nanalysis", offset=0.2)

    # Audit trail / differential output
    make_box(ax, 0.2, 0.4, 2.0, 0.8,
             "Audit trail\nlogs/v4-peer-review-*.md",
             fc=COLORS["output"], fontsize=7.5)

    # OpenRouter annotation
    ax.text(5.0, 6.15, "All vendor calls routed via OpenRouter HTTP gateway",
            ha="center", fontsize=8.5, style="italic", color="#555555")

    # Title
    ax.text(5.0, 6.40, "Figure 1. Cross-vendor heterogeneity guard architecture",
            ha="center", fontsize=11, fontweight="bold")

    # Legend
    legend_y = 0.1
    handles = [
        patches.Patch(facecolor=COLORS["anthropic"], label="Anthropic"),
        patches.Patch(facecolor=COLORS["deepseek"], label="DeepSeek"),
        patches.Patch(facecolor=COLORS["google"], label="Google (fallback)"),
        patches.Patch(facecolor=COLORS["openai"], label="OpenAI (alt.)"),
    ]
    ax.legend(handles=handles, loc="lower right", fontsize=8, ncol=4,
              frameon=False, bbox_to_anchor=(0.98, -0.02))

    plt.tight_layout()
    pdf_path = OUT_DIR / "figure1_architecture.pdf"
    png_path = OUT_DIR / "figure1_architecture.png"
    plt.savefig(pdf_path, bbox_inches="tight")
    plt.savefig(png_path, bbox_inches="tight", dpi=300)
    print(f"Wrote {pdf_path}")
    print(f"Wrote {png_path}")


if __name__ == "__main__":
    main()
