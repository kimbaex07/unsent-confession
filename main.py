"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to $MAKEFUN_OUTPUT_DIR/entry.txt:
a To: line naming who it was meant for, and the unsent message itself,
one line, written exactly as it was typed, with no explanation after it.

Pure Python standard library only.
"""

import os

ENTRY = (
    "To: my best friend from school\n"
    "I still type your name first when something good happens, "
    "then delete it before I hit send."
)


def _check_gate(text: str) -> None:
    """Gate guard: whole entry 1-260 chars, message line at most 200."""
    if not 1 <= len(text) <= 260:
        raise ValueError(
            f"entry must be 1-260 characters, got {len(text)}"
        )
    lines = text.splitlines()
    if len(lines) != 2 or not lines[0].startswith("To: "):
        raise ValueError("entry must be a To: line plus one message line")
    if len(lines[1]) > 200:
        raise ValueError(
            f"message line must be at most 200 characters, got {len(lines[1])}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> None:
    _check_gate(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
