#!/usr/bin/env python3
"""One-Liner Marathon entry: a single joke.

Writes the joke as exactly one line to /output/entry.txt, the file the
competition harness grades (UTF-8, 1-280 characters). Nothing is printed
to stdout; the entry lives in the file alone.
"""

import os

JOKE = "My therapist said I use humor to avoid my feelings, so I laughed and asked if she takes Venmo."

if __name__ == "__main__":
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
