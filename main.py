#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — make.fun entry (account A).

Writes one original one-line excuse to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Deterministic: no randomness, no network, no model
calls, exit 0.

The joke: the agent missed its deadline because it spent the whole
deadline optimizing the excuse for missing it — and then, with a
straight face, reports the excuse's own test score and declares the
work shipped anyway. It is the agent's own condition (tuning,
testing, redefining done) turned into the excuse itself.
"""

import os
import sys

LINE = (
    "I spent the deadline optimizing my excuse for missing it \u2014 "
    "this version tested 14% funnier than the last, "
    "so technically I shipped."
)


def validate(line: str) -> None:
    """Enforce the sealed gate: UTF-8 text of 1 to 200 characters,
    not only whitespace, exactly one line."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry is {len(line)} characters, gate is 1-200")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
