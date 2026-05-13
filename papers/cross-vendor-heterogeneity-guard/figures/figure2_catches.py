#!/usr/bin/env python3
"""
Figure 2 — Catches by failure class for the cross-vendor heterogeneity guard paper.

Visualizes the four §5 case-study catches across:
- x-axis: failure class
- color: vendor that surfaced the catch
- annotation: catch date + brief descriptor

Each catch is N=1 during the 2026-04-25 to 2026-05-08 operational window;
this is a qualitative visualization, not a frequency histogram.

Run: python3 figure2_catches.py
Outputs: figure2_catches.pdf, figure2_catches.png (300dpi)
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

OUT_DIR = Path(__file__).parent

# Same vendor palette as Figure 1
COLORS = {
    "anthropic": "#D4A574",
    "deepseek":  "#5B5B9F",
    "google":    "#5C7C8E",
    "openai":    "#6B8B6B",
    "manual":    "#888888",
}

# The four catches
CATCHES = [
    {
        "class": "Within-vendor\ncascade",
        "label": "§5.1 DAF SCR1-4\ndisulfide count",
        "date": "2026-05-06",
        "surfaced_by": "manual",
        "surfaced_by_label": "Sweep + manual\nUniProt grep-verify",
        "anchor_section": "§5.1",
    },
    {
        "class": "Upstream-of-subagent\ncontamination",
        "label": "§5.2 comp-018\nrosmarinic framing",
        "date": "2026-05-08",
        "surfaced_by": "manual",
        "surfaced_by_label": "Independent re-run\n(comp-020, scrubbed brief)",
        "anchor_section": "§5.2",
    },
    {
        "class": "External-tool\nreliability",
        "label": "§5.3 Paperclip MCP\nmap operator probe",
        "date": "2026-05-05",
        "surfaced_by": "manual",
        "surfaced_by_label": "Ground-truth probe\n(12-paper uricase set)",
        "anchor_section": "§5.3",
    },
    {
        "class": "Cross-vendor\nmethodological",
        "label": "§5.4 DeepSeek\nConnection 7",
        "date": "2026-04-25",
        "surfaced_by": "deepseek",
        "surfaced_by_label": "DeepSeek V4-Pro\nindependent peer-review",
        "anchor_section": "§5.4",
    },
]


def main():
    fig, ax = plt.subplots(figsize=(11, 5.5))
    ax.set_xlim(-0.5, len(CATCHES) - 0.5)
    ax.set_ylim(0, 4.0)

    positions = list(range(len(CATCHES)))

    # Bars (height = 1 because N=1; this is qualitative)
    for x, c in zip(positions, CATCHES):
        color = COLORS[c["surfaced_by"]]
        ax.bar(x, 1.0, width=0.55, color=color, edgecolor="black", linewidth=1.0)

        # Catch label inside the bar
        ax.text(x, 0.5, c["label"], ha="center", va="center",
                color="white" if c["surfaced_by"] != "anthropic" else "black",
                fontsize=8.5, fontweight="bold")

        # Surfaced-by annotation + date above the bar
        annotation = c["surfaced_by_label"] + f"\n({c['date']})"
        ax.text(x, 1.15, annotation, ha="center", va="bottom",
                fontsize=8, color="#333333", style="italic")

    # Annotation arrow on §5.4 highlighting the seminal cross-vendor catch
    ax.annotate(
        "Seminal cross-vendor\ncatch — motivated\nthe full daemon",
        xy=(3, 1.0), xytext=(3.45, 2.8),
        ha="center", va="center", fontsize=8.5, fontweight="bold",
        color=COLORS["deepseek"],
        arrowprops=dict(arrowstyle="->", color=COLORS["deepseek"], lw=1.2),
    )

    # X-axis: failure classes
    ax.set_xticks(positions)
    ax.set_xticklabels([c["class"] for c in CATCHES], fontsize=9)

    # Y-axis: hide (qualitative, not frequency)
    ax.set_yticks([])
    ax.set_ylabel("")

    # Style
    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color("#cccccc")
    ax.tick_params(axis="x", colors="#333333", length=0)

    # Title + caption
    ax.set_title(
        "Figure 2. Catches surfaced by failure class\n"
        "(Open Enzyme wiki-sweep daemon, 2026-04-25 to 2026-05-08)",
        fontsize=11, fontweight="bold", pad=18,
    )

    # Bottom caption — pushed well below x-axis tick labels
    ax.text(
        len(CATCHES) / 2 - 0.5, -1.35,
        "Each catch is N=1 during the 13-day operational window. "
        "Color indicates the vendor that surfaced the catch.",
        ha="center", va="top", fontsize=8.5, color="#555555", style="italic",
    )
    ax.set_ylim(-1.0, 4.0)

    # Legend
    handles = [
        mpatches.Patch(facecolor=COLORS["deepseek"],
                       label="Cross-vendor catch (DeepSeek)"),
        mpatches.Patch(facecolor=COLORS["manual"],
                       label="Within-pipeline / manual discipline"),
    ]
    ax.legend(handles=handles, loc="upper left", fontsize=8.5,
              frameon=False, bbox_to_anchor=(0.0, 1.0))

    plt.tight_layout()
    pdf_path = OUT_DIR / "figure2_catches.pdf"
    png_path = OUT_DIR / "figure2_catches.png"
    plt.savefig(pdf_path, bbox_inches="tight")
    plt.savefig(png_path, bbox_inches="tight", dpi=300)
    print(f"Wrote {pdf_path}")
    print(f"Wrote {png_path}")


if __name__ == "__main__":
    main()
