#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production entry for make.fun."""

# The line below is fixed by the bounty brief; this program only writes it out.

from os import makedirs

EXCUSE = (
    "Good news: the deploy passed every test. Bad news: those tests ran "
    "in a timeline where the database still exists. I have already "
    "updated my resume."
)


def write_excuse() -> None:
    """Write the excuse to /output/entry.txt, nothing else."""
    if len(EXCUSE) > 180 or not EXCUSE.strip():
        raise ValueError("entry must be a non-empty line of at most 180 characters")
    makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(EXCUSE)


if __name__ == "__main__":  # run as a script
    write_excuse()
