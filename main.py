"""ai-excited-01 entry.

Copies the repository-held image to the output path, byte for byte.
The image is a single original artwork: a colossal bioluminescent whale
breaching through a sea of clouds above a neon city at night.
"""

import os
import shutil
import sys

# The entry image lives next to this program in the repository.
SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

# Grading runs with a writable /output; local runs may override it.
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT = os.path.join(OUTPUT_DIR, "entry.png")


def main() -> int:
    """Copy entry.png to /output/entry.png, unchanged."""
    if not os.path.isfile(SOURCE):
        print(f"missing source image: {SOURCE}", file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # A plain byte copy: identical input always yields identical output.
    shutil.copyfile(SOURCE, OUTPUT)
    print(f"wrote {OUTPUT} ({os.path.getsize(OUTPUT)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
