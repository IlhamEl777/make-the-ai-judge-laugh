#!/usr/bin/env python3
"""Entry for make.fun's ai-joke-03, "Make the AI judge laugh".

Writes one joke (a one-liner about AI coding agents) to /output/entry.txt.
Deterministic, no network, stdlib only: the same bytes on every run.
"""

import os

JOKE = (
    "I gave my AI coding agent one task before lunch. By dinner it had "
    "spawned twelve subagents, held a standup with itself, and promoted "
    "the one that agreed with it most."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(JOKE)


if __name__ == "__main__":
    main()
