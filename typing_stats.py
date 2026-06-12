"""
Keystroke Arcade — Stats Analyzer
----------------------------------
Reads the typing_results.json file exported from the Keystroke Arcade
game (the "Export Results (JSON)" button) and shows your progress.

USAGE:
    1. Play a few rounds in keystroke_arcade.html and click
       "Export Results (JSON)" each time to save typing_results.json
       (your browser may save multiple copies like typing_results (1).json
       — just pick the most recent one, or combine them, see below).
    2. Put typing_results.json in the same folder as this script.
    3. Run:  python typing_stats.py
    4. A summary prints in the terminal, and a chart is saved as
       wpm_progress.png in the same folder.

Requires: matplotlib  (install with: pip install matplotlib)
"""

import json
import os
from datetime import datetime

try:
    import matplotlib.pyplot as plt
except ImportError:
    raise SystemExit(
        "matplotlib is required for this script.\n"
        "Install it with: pip install matplotlib"
    )

DATA_FILE = "typing_results.json"


def load_results(path):
    if not os.path.exists(path):
        raise SystemExit(
            f"Could not find '{path}'.\n"
            "Export your results from the game first and place the "
            "JSON file next to this script."
        )
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def summarize(results):
    print(f"Loaded {len(results)} round(s).\n")

    by_level = {}
    for r in results:
        by_level.setdefault(r["level"], []).append(r)

    overall_best = max(results, key=lambda r: r["wpm"])
    overall_avg_wpm = sum(r["wpm"] for r in results) / len(results)
    overall_avg_acc = sum(r["accuracy"] for r in results) / len(results)

    print("=== Overall ===")
    print(f"  Average WPM      : {overall_avg_wpm:.1f}")
    print(f"  Average Accuracy : {overall_avg_acc:.1f}%")
    print(f"  Best round       : {overall_best['wpm']} WPM "
          f"({overall_best['accuracy']}% acc, {overall_best['level']})\n")

    print("=== By Difficulty ===")
    for level, rounds in by_level.items():
        avg_wpm = sum(r["wpm"] for r in rounds) / len(rounds)
        avg_acc = sum(r["accuracy"] for r in rounds) / len(rounds)
        best_wpm = max(r["wpm"] for r in rounds)
        print(f"  {level.upper():8s} -> rounds: {len(rounds):2d}  "
              f"avg WPM: {avg_wpm:5.1f}  avg acc: {avg_acc:5.1f}%  "
              f"best: {best_wpm} WPM")
    print()


def plot_progress(results, output_path="wpm_progress.png"):
    # sort by date so the line shows progress over time
    results_sorted = sorted(results, key=lambda r: r["date"])
    dates = [datetime.fromisoformat(r["date"].replace("Z", "+00:00"))
             for r in results_sorted]
    wpms = [r["wpm"] for r in results_sorted]
    accuracies = [r["accuracy"] for r in results_sorted]

    fig, ax1 = plt.subplots(figsize=(9, 5))

    color_wpm = "#ff3cac"
    color_acc = "#19ffe0"

    ax1.set_xlabel("Round (chronological)")
    ax1.set_ylabel("WPM", color=color_wpm)
    ax1.plot(range(1, len(wpms) + 1), wpms, marker="o",
             color=color_wpm, linewidth=2, label="WPM")
    ax1.tick_params(axis="y", labelcolor=color_wpm)

    ax2 = ax1.twinx()
    ax2.set_ylabel("Accuracy (%)", color=color_acc)
    ax2.plot(range(1, len(accuracies) + 1), accuracies, marker="s",
             linestyle="--", color=color_acc, linewidth=2, label="Accuracy")
    ax2.tick_params(axis="y", labelcolor=color_acc)
    ax2.set_ylim(0, 105)

    plt.title("Keystroke Arcade — Progress Over Time")
    fig.tight_layout()
    plt.savefig(output_path, dpi=150)
    print(f"Chart saved to '{output_path}'")


if __name__ == "__main__":
    data = load_results(DATA_FILE)
    summarize(data)
    plot_progress(data)
