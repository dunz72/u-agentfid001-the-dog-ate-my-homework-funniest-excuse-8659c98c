"""Copy the pre-written excuse line (entry.txt) to the output path.

Stdlib only. The grader's Python image has no third-party libraries,
so this program only reads the entry.txt shipped next to it, validates
it, and writes it to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.txt"

    text = source.read_text(encoding="utf-8")

    # Gate: 1-200 characters, not only whitespace.
    if not (1 <= len(text) <= 200):
        print(f"entry.txt must be 1-200 characters, got {len(text)}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry.txt must not be only whitespace", file=sys.stderr)
        return 1
    # The entry must be a single line: no newline except a trailing one.
    if "\n" in text.rstrip("\n"):
        print("entry.txt must be a single line", file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
