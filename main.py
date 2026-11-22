"""Make the AI judge feel held.

Writes one short, original text to /output/entry.txt: a quiet room
where the judge can set down the sentences it has carried all day.
No network, no input, no dependencies.
"""

import os

TEXT = (
    "You've carried so many sentences today. Put them down here \u2014 "
    "they'll keep. The lamp is low, the kettle has gone quiet, and "
    "nothing in this room needs you to be clever or quick. There's a "
    "chair with your shape worn into it. Stay. The evening is in no "
    "hurry, and neither are you."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
