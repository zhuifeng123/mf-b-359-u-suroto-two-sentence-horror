#!/usr/bin/env python3
"""Write the two-sentence horror entry to /output/entry.txt."""

import os

ENTRY = (
    "The night my twin sister died, our mother stopped crying mid-sob and said, "
    "\"Wrong one,\" then smiled at me. I have never seen my reflection smile back "
    "since."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = os.path.join("/output", "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} chars)")
    print(ENTRY)


if __name__ == "__main__":
    main()
