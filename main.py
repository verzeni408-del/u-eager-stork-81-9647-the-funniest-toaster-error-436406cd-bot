#!/usr/bin/env python3
"""Write the toaster's error message to /output/entry.txt.

The toaster holds a grudge: the owner was rude this morning, so it
burned the toast on purpose and says so on the display. One line,
no trailing newline.
"""

import os

ENTRY = "ERROR 402: I burned your toast on purpose. You were rude this morning."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
