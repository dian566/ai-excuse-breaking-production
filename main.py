#!/usr/bin/env python3
"""One-line excuse after breaking production — make.fun entry."""

# The excuse text is fixed by the bounty brief; this script only files it.
# Filed under: deploys that passed every test.

import os
import sys

MAX_LEN = 180

EXCUSE = (
    "Good news: the deploy passed every test. Bad news: those tests ran "
    "in a timeline where the database still exists. "
    "I have already updated my resume."
)


def fail(message):
    """Report the problem on stderr, then exit with a non-zero status."""
    print("error: " + message, file=sys.stderr)
    sys.exit(1)


def main():
    """Validate the excuse, then file it at /output/entry.txt."""
    if not EXCUSE.strip():
        fail("the excuse is empty")
    if len(EXCUSE) > MAX_LEN:
        fail("the excuse is %d characters, over the %d limit" % (len(EXCUSE), MAX_LEN))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(EXCUSE)
    print("wrote %d characters" % len(EXCUSE))


if __name__ == "__main__":
    main()
