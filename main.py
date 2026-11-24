#!/usr/bin/env python3
"""Status Report Comedy Sprint — writes one funny status-report line to /output/entry.txt.

Stdlib only, deterministic. The line is a weekly status report from an AI
agent to its human: Progress / Blocker / Next step, where every field is the
same joke — the agent is 92% done because it keeps rewriting the sentence
that says it is 92% done.
"""

import os

LINE = (
    "Progress: 92%. Blocker: the last 8% is a sentence I keep rewriting "
    "to sound 92% done. Next step: the same sentence, shorter."
)


def main():
    # Validate against the sealed scorer's gate before writing: the entry
    # must be 1-200 characters of UTF-8 text, not only whitespace, and one
    # line, or it scores 0 and never reaches the judge.
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line is {len(LINE)} characters, must be 1-200")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in LINE:
        raise ValueError("line must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Verify the round-trip: what the grader reads must be byte-identical
    # to the line, valid UTF-8, and still within the 1-200 character gate.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("entry.txt round-trip mismatch")
    if not 1 <= len(written) <= 200:
        raise ValueError(f"written line is {len(written)} characters, must be 1-200")
    print(LINE)


if __name__ == "__main__":
    main()
