"""Toaster error entry writer: one line, no trailing newline."""

from pathlib import Path

ENTRY = "SETTING 11 SELECTED. I am a toaster, not a crematorium."
ENTRY_PATH = Path("/output/entry.txt")


def main() -> None:
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    ENTRY_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
