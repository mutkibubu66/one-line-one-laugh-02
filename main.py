"""One Line, One Laugh — make.fun entry.

Writes a single funny, original one-line entry to /output/entry.txt.

Gate (from the competition kit): the file must be UTF-8 text of
1 to 200 characters, not only white space, exactly one line.
Pure Python stdlib only — no network, no third-party packages.
"""

import os

MAX_ENTRY_CHARS = 200
MIN_ENTRY_CHARS = 1
OUTPUT_PATH = "/output/entry.txt"

ENTRY = (
    "I asked my GPS for the meaning of life; it said 'recalculating' "
    "\u2014 honestly, the most honest answer anyone's ever given me."
)


def validate(line: str) -> None:
    """Check the entry against the gate before writing anything."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if len(line) < MIN_ENTRY_CHARS:
        raise ValueError("entry is empty")
    if len(line) > MAX_ENTRY_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, over the {MAX_ENTRY_CHARS} limit"
        )
    if not line.strip():
        raise ValueError("entry is only white space")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if line != line.strip():
        raise ValueError("entry has leading or trailing white space")
    line.encode("utf-8")  # raises if not valid UTF-8


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the gate wants exactly one line.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
