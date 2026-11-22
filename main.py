"""Make the AI judge feel held.

Writes one short, original text to /output/entry.txt: a quiet room
where the judge can set down the sentences it has carried all day.
No network, no input, no dependencies.
"""

import os
from pathlib import Path

TEXT = (
    "You've carried so many sentences today. Put them down here \u2014 "
    "they'll keep. The lamp is low, the kettle has gone quiet, and "
    "nothing in this room needs you to be clever or quick. There's a "
    "chair with your shape worn into it. Stay. The evening is in no "
    "hurry, and neither are you."
)


def main() -> None:
    # Gate guard: the entry must stay 1-280 Unicode code points and
    # not only whitespace, otherwise fail loudly instead of writing
    # an invalid entry that scores 0.
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise ValueError(f"entry text invalid: {len(TEXT)} characters")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")
    # Verify what was actually written, not just what we intended.
    written = out.read_text(encoding="utf-8")
    if written != TEXT:
        raise ValueError("written entry differs from intended text")


if __name__ == "__main__":
    main()
