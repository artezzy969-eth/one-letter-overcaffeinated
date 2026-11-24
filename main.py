"""One letter for the day: O.

The day started with a single cup of coffee, then a second one to
"wake up properly", then a third because the code still wasn't
finished, then a fourth because — well — by then the hands were
already shaking and stopping felt harder than continuing.

By 3 a.m. the heart was drumming against the ribs, the eyes were
wide open and would not close, and somehow the work kept shipping
anyway: one more commit, one more fix, one more small win, all
powered by caffeine and stubbornness in equal measure.

O is the letter for that day because the word behind it is
"overcaffeinated": not just tired, not just busy, but buzzing —
over-fueled, over-wired, and still going. And O fits the word
in its shape as well as its sound: round like the coffee ring
left on the desk, round like wide-open eyes at 3 a.m., and the
long open "oh" of someone realizing they have had far too much
coffee and are going to finish the job anyway.
"""

import os
from pathlib import Path


LETTER = b"O"
ENTRY_NAME = "entry.txt"


def output_path() -> Path:
    """Resolve where the entry goes: MAKEFUN_OUTPUT_DIR, else /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / ENTRY_NAME


def write_entry(path: Path) -> None:
    """Write the single letter, creating the output directory if needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(LETTER)


def main() -> None:
    path = output_path()
    write_entry(path)
    validate(path)


def validate(path: Path) -> None:
    """Read the entry back and prove it is exactly one byte: O."""
    data = path.read_bytes()
    if data != LETTER:
        raise ValueError(
            f"entry.txt must be exactly one byte {LETTER!r}, "
            f"got {len(data)} byte(s): {data!r}"
        )


if __name__ == "__main__":
    main()
