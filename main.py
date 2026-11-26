#!/usr/bin/env python3
"""The Absurd Clause Contest: an absurd clause buried in a
terms-of-service agreement.

The program writes a single clause, at most 200 characters, to
/output/entry.txt. The sealed gate wants UTF-8 text of 1 to 200
characters, not only white space, so the clause is validated here
before it is written.
"""

import os

# The gate accepts 1 to 200 characters; keep the cap in one place so
# the clause and the check can never drift apart.
MAX_CHARS = 200

ENTRY = (
    "Section 7.1: If you sneeze while using this service, you agree "
    "to bless yourself out loud within three (3) business days."
)


def validate(line):
    """Return True when the line is a legal entry for the gate."""
    if not line or not line.strip():
        return False
    if len(line) > MAX_CHARS:
        return False
    return True


def main():
    if not validate(ENTRY):
        raise SystemExit("entry is not valid: check length and content")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")
    print("wrote /output/entry.txt (%d chars)" % len(ENTRY))


if __name__ == "__main__":
    main()
