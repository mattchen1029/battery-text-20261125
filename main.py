"""Battery's last text to its charger.

Writes one line of plain text (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt by default).
"""

import os

MIN_CHARS = 1
MAX_CHARS = 200
OUTPUT_NAME = "entry.txt"

TEXT = (
    "I waited all day for you. You sat on the nightstand at home while "
    "I died at 1% in a stranger's car. Don't text back - "
    "I won't be alive to read it."
)


def validate_line(line: str) -> str:
    """Enforce the competition gate: 1-200 chars, single line, non-blank."""
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        raise ValueError(f"line is {len(line)} chars, must be {MIN_CHARS}-{MAX_CHARS}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    return line


def write_entry(line: str, out_dir: str) -> str:
    """Write the validated line to <out_dir>/entry.txt and return the path."""
    checked = validate_line(line)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(checked + "\n")
    return path


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(TEXT, out_dir)


if __name__ == "__main__":
    main()
