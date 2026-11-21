"""Write one short text to /output/entry.txt.

The text is a single quiet scene, written to slow the reader down:
a small light kept in a dark that has been there far longer than us.
No network, no randomness, no clock -- every run writes the same bytes.
"""

import os

TEXT = (
    "Far below the last sunlight, a lanternfish lights its small lamp. "
    "The dark does not end there. It only deepens, slow as an old sea, "
    "and the water holds the light the way night holds one lit window. "
    "Nothing hurries, and the sea, dark longer than anything alive, "
    "keeps the glow."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
