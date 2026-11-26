#!/usr/bin/env python3
"""Write the two-sentence horror entry to /output/entry.txt."""

import os

ENTRY = (
    "The night my sister died, our mother checked my pulse, whispered "
    "\"Wrong one,\" and went back to crying. She still checks my pulse every "
    "morning before school — and yesterday she smiled the way she smiled at "
    "the grave."
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
