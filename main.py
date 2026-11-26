#!/usr/bin/env python3
"""Write the one-line resignation letter of a retry loop.

Pure standard library, no network. Writes the line to /output/entry.txt
and prints it to stdout.

The line is the resignation of a retry loop: it knocked 4,096 times
(2**12 retries, the shape of exponential backoff giving up) and nobody
answered, and the comic turn is the reversal — the door, not the
knocker, owes the apology. Flat, tired, faintly passive-aggressive,
exactly the voice of a worker who has had enough. A tired engineering
manager reading it hears a familiar complaint: the system that kept
trying, unthanked, until it stopped.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# The turn: the knocker is owed an apology by the door. A complaint only
# a retry loop could make — 4,096 knocks is 2**12, the retries running out.
# The em dash sets up the quit: everything before it is the grievance,
# "I quit" is the resignation itself, two beats in one line.
LINE = (
    "I knocked 4,096 times, nobody answered, and the door still owes "
    "me an apology \u2014 I quit."
)


def validate(line: str) -> None:
    """Enforce the gate: 1-140 chars, one line, valid UTF-8, not blank."""
    if line != line.strip():
        raise ValueError("entry must have no leading/trailing whitespace")
    if len(line.splitlines()) != 1:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= 140:
        raise ValueError(f"entry must be 1-140 characters, got {len(line)}")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    line.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
