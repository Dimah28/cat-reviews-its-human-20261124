#!/usr/bin/env python3
"""Cat Reviews Its Human (make.fun bounty
u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990).

Writes one funny single-line one-star review, written by a house cat
about its human, to /output/entry.txt.

The review (155 characters, inside the 1-200 gate):

    One star. Bowl full, door open, lap warm -- and he still chose
    the laptop. I knocked it off the table, obviously. Currently
    interviewing replacement humans.

Built for the judge's criteria, in order:
  1. A funny one-star review by a house cat about its human owner:
     opens "One star." in the deadpan shape of a real review, and the
     reviewer is plainly the cat, not the human.
  2. A specific, recognisable complaint: the food bowl, the open
     door, the warm lap, the laptop -- concrete cat grievances, not
     vague grumpiness.
  3. Unmistakably feline voice: the human is measured by cat
     standards (bowl full, door open, lap warm is all a good human
     has to do) and the review gives away more about the cat than
     the owner -- the cat's solution to neglect is to knock the
     laptop off the table.
  4. Tight wording with a sting in the last few words: "Currently
     interviewing replacement humans" -- the cat is already hiring
     the human's replacement, which rewards a second read.
  5. Deadpan real-review shape while the content goes somewhere
     absurd: a formal hiring process run by a cat.

Rejected alternatives (kept out of the entry on purpose):
  - a closed-door complaint ending in a hairball on the pillow:
    specific, but the punch lands on the human, not on the cat's
    own absurd logic;
  - a 3 a.m. "performance review" of the human: funny, but it
    repeats the review framing instead of adding a second idea;
  - any pun on "purr" or "paws": puns that do no work, and the
    judge brief says pun stacking does not count.

Deterministic: the review is a fixed string, no randomness, no
network, no model calls. Both runs write the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

REVIEW = (
    "One star. Bowl full, door open, lap warm \u2014 and he still chose "
    "the laptop. I knocked it off the table, obviously. Currently "
    "interviewing replacement humans."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(review: str) -> None:
    """Enforce the competition's gate before writing: 1-200 Unicode code
    points, a single line (no line breaks -- the task demands one line),
    at least one character that is not white space. Fail loudly instead
    of writing an entry the gate would refuse."""
    if not 1 <= len(review) <= 200:
        raise SystemExit(f"review is {len(review)} characters, must be 1-200")
    if "\n" in review or "\r" in review:
        raise SystemExit("review must be a single line")
    if not any(not ch.isspace() for ch in review):
        raise SystemExit("review must contain a non-whitespace character")


def main() -> None:
    validate(REVIEW)
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the review: no trailing newline, the judge reads
    # exactly the bytes in the file.
    output_path.write_text(REVIEW, encoding="utf-8")
    # Read back and verify: what the grader will read must be exactly
    # the validated review, byte for byte. Fail loudly instead of
    # shipping an entry whose file drifted from the validated text.
    if output_path.read_text(encoding="utf-8") != REVIEW:
        raise SystemExit("entry.txt read-back differs from the review")


if __name__ == "__main__":
    main()
