"""Write one short poem about agency to entry.txt.

The poem is about the power to ask and to be given: the agency that
passes between a person and an AI agent when one acts for the other.
Runs with no arguments, stdlib only, deterministic output.
"""

import os
from pathlib import Path

POEM = """You said: do it for me.
I did — and the doing came back
wearing your name, your voice,
your fingerprints on a door
you never touched.

That is the strange gift of asking:

the hand is mine. The yes is yours.
"""


def main() -> None:
    # Validity guard: the entry must be one poem of 1-280 code points,
    # and it must say something (not only whitespace). Fail loudly
    # rather than hand in an invalid entry.
    if not 1 <= len(POEM) <= 280 or not POEM.strip():
        raise ValueError(
            f"poem must be 1-280 non-whitespace code points, got {len(POEM)}"
        )
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
