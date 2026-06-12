# Keystroke Arcade

A small typing speed game I built for fun — type out random sentences, see your WPM and accuracy update live, and watch a little speedometer needle react to how fast you're going.

Try it here: https://keystroke28.netlify.app/

## What it does

You pick a difficulty (Easy, Medium, or Hard), get a random sentence, and start typing. As you go:

- correct letters turn one color, mistakes turn another
- a timer counts down (60s on Easy, 45s on Medium, 30s on Hard)
- your WPM and accuracy update in real time
- a gauge needle swings up as your speed increases

Once a round ends you can hit "Export Results" to download your scores as a JSON file.

## The Python part

There's also a small script, `typing_stats.py`, that you can run on your computer after exporting a results file. It reads your `typing_results.json`, prints out your average WPM/accuracy and your best round, and saves a chart (`wpm_progress.png`) showing how you've improved across rounds.

To use it:

```
pip install matplotlib
python typing_stats.py
```

(make sure `typing_results.json` is in the same folder)

## Built with

- HTML/CSS/JS for the game itself
- Python + matplotlib for the stats chart
- Fonts: Bricolage Grotesque and Spline Sans Mono

## Files

- `index.html` — the game
- `typing_stats.py` — the stats/chart script
- `README.md` — this file

## Notes

This was mostly a project to practice working with the DOM, timers, and SVG, plus getting more comfortable with Git/GitHub deployment. Feel free to fork it or suggest passages if you want more variety to type!

---
Made by Himanshu28
