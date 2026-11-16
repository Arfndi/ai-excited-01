"""Sky Whale - make.fun ai-excited-01 entry.

Copies the entry image shipped in this repository to the output path
the grader reads: /output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png).
Standard library only; deterministic - the same bytes on every run.
No network, no randomness, no timestamps: both graded runs write
byte-identical output.
"""

import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"
    shutil.copyfile(SOURCE, destination)
    print(f"wrote {destination} ({destination.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
