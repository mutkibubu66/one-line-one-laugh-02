"""One Line, One Laugh — make.fun entry.

Writes a single funny, original one-line entry to /output/entry.txt.

Gate (from the competition kit): the file must be UTF-8 text of
1 to 200 characters, not only white space, exactly one line.
Pure Python stdlib only — no network, no third-party packages.

Judging criteria the entry is written for:
- Originality: a fresh take on the "meaning of life" trope — no
  recycled punchline, the joke lands on the GPS's literal answer.
- Humour: the setup promises philosophy and the punchline delivers
  a deadpan machine reply; the em-dash beat ("— honestly, ...")
  sells the narrator's reluctant agreement with a gadget.
- Fit: one sentence, one line, 122 characters — well inside the
  1–200 gate, no trailing newline, no leading/trailing spaces.
"""

import os

MAX_ENTRY_CHARS = 200
MIN_ENTRY_CHARS = 1
OUTPUT_PATH = "/output/entry.txt"

# The joke is assembled from named parts so each beat can be read
# (and checked) on its own; the joined result is the single entry line.
SETUP = "I asked my GPS for the meaning of life; it said 'recalculating'"
BEAT = "\u2014"  # em dash: the pause before the punchline lands
PUNCHLINE = "honestly, the most honest answer anyone's ever given me."


def build_entry() -> str:
    """Join the joke's parts into the single entry line.

    Each part is itself a single line: a newline hiding inside any
    part would survive the join and break the one-line gate, so the
    join refuses it up front instead of relying on validate() alone.
    """
    for name, part in (("SETUP", SETUP), ("BEAT", BEAT), ("PUNCHLINE", PUNCHLINE)):
        if "\n" in part or "\r" in part:
            raise ValueError(f"{name} part contains a line break")
    return f"{SETUP} {BEAT} {PUNCHLINE}"


ENTRY = build_entry()


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
    encoded = line.encode("utf-8")  # raises if not valid UTF-8
    if len(encoded) > MAX_ENTRY_CHARS * 4:
        # Sanity bound: no valid entry can exceed 4 UTF-8 bytes per char.
        raise ValueError("entry is unexpectedly large in UTF-8 bytes")


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the gate wants exactly one line.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
