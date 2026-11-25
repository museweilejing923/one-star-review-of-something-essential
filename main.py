#!/usr/bin/env python3
"""Drop a deadpan one-star review of gravity into /output/entry.txt.

One fixed line goes in, the same bytes come out every time. The
script reaches no network, reads no clock and uses no randomness.
"""

import os
import string
import sys

LINE = "One star. Gravity works perfectly until you drop your phone, at which point it becomes extremely efficient."
CEILING = 160
OUT = "/output/entry.txt"


def screen(text):
    """Make sure the review is one real line of prose, within the cap."""
    if text.strip() == "":
        raise ValueError("entry is blank")
    if len(text) > CEILING:
        raise ValueError("entry is too long")
    if all(mark in string.punctuation for mark in text.strip()):
        raise ValueError("entry cannot be punctuation only")
    if text.strip().isdigit():
        raise ValueError("entry is digits alone")
    if not any(mark.isalpha() for mark in text):
        raise ValueError("entry needs at least one letter")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must stay on one line")
    return text


def run():
    try:
        good = screen(LINE)
    except ValueError as problem:
        print(f"bad entry: {problem}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as handle:
        handle.write(good)
    return 0


if __name__ == "__main__":
    sys.exit(run())
