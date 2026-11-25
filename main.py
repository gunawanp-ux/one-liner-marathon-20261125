#!/usr/bin/env python3
"""One-Liner Marathon entry: a single joke.

Prints the joke to stdout and writes it to /output/entry.txt,
which is the file the competition harness grades (1-280 chars, UTF-8).
"""

import os

JOKE = "My therapist said I use humor to avoid my feelings, so I laughed and asked if she takes Venmo."

if __name__ == "__main__":
    print(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
