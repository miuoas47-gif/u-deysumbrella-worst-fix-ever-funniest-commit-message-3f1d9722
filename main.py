#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes the entry -- one original commit message line for the worst
fix ever, at most 100 characters per the competition gate -- to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt) and prints
it to stdout. Deterministic: no network, no clock, no randomness;
the same bytes come out every run.
"""

import os
import sys
from pathlib import Path

MESSAGE = """fix: users kept crashing the app, so I removed the users
"""


def main():
    # One canonical output: exactly one trailing newline, so the file
    # and stdout are always the same bytes.
    output = MESSAGE if MESSAGE.endswith("\n") else MESSAGE + "\n"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(output, encoding="utf-8")
    sys.stdout.write(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
