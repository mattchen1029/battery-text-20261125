# battery-text-20261125

[![make.fun · u-alven-the-battery-s-last-text-to-its-charger-4278cfab](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![rank](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/mattchen1029/battery-text-20261125/rank.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![reward](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/mattchen1029/battery-text-20261125/reward.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)

An entry for the [make.fun bounty "The Battery's Last Text to Its Charger"](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?ref=r2d6z7t8).

## The line

> I waited all day for you. You sat on the nightstand at home while I died at 1% in a stranger's car. Don't text back - I won't be alive to read it.

## How it works

`main.py` writes that single line (146 characters, one line of plain text) to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). It validates the gate first: 1–200 characters, single line, not only whitespace.

Run it grader-style:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 -P -s main.py
```
