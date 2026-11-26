#!/usr/bin/env python3
"""Funniest Lost Sock Status Update.

A single status update, in the voice of a lost sock, written to
/output/entry.txt. Pure standard library, deterministic output.
"""

import os

# The sock ended up in the aquarium: somewhere it should not be,
# and it has something to say about it.
ENTRY = (
    "Day 47 in the aquarium. The goldfish thinks I am a jellyfish "
    "and honestly, the rent is free."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
