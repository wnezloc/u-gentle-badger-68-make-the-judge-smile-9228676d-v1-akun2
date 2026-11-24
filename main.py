#!/usr/bin/env python3
"""Make the Judge Smile — one-line entry.

Writes a single line (at most 200 characters) to /output/entry.txt
about a small good thing that happened today: one concrete detail,
a warm turn, and a surprise in how it is told.

Stdlib only, offline, deterministic: every run writes the same bytes.
"""

import os
from pathlib import Path

# The line: 6 a.m., a still-warm roll, a fence, a whisper — warmth
# with one concrete detail and a surprise at the end.
# Counted at 118 characters — inside the 1..200 window.
LINE = (
    "At 6 a.m. the baker next door slipped a still-warm roll "
    "through my fence and whispered, 'You looked hungry yesterday.'"
)


def output_dir() -> Path:
    """Where the grader expects the entry file.

    The grader runs the program from /bot with output at /output and
    no environment variables set, so the fallback is absolute.
    """
    return Path(os.environ.get("OUTPUT_DIR", "/output"))


def main() -> None:
    """Write the line to entry.txt."""
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE, encoding="utf-8")


# Guard: only run when executed directly.
if __name__ == "__main__":
    main()
