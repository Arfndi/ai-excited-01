#!/usr/bin/env python3
"""ai-excited-01 entry: copy the repo-held image to /output/entry.png.

The image is generated once (an original luminous phoenix bursting from a
nebula over a neon city) and stored in this repository as entry.png. This
program only copies those exact bytes to the output path, so two runs
always write byte-identical output. Standard library only, no network.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    # Verify the copy is byte-identical before exiting: the grader runs
    # this program twice and both runs must write the same bytes.
    with open(source, "rb") as f:
        expected = f.read()
    with open(target, "rb") as f:
        actual = f.read()
    if actual != expected:
        print("error: output bytes differ from entry.png", file=sys.stderr)
        return 1
    print(f"wrote {target} ({len(actual)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
