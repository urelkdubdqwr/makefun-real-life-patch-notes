"""Write the make.fun entry text to entry.txt in the output directory.

Standard library only. The output directory is taken from the environment
variable MAKEFUN_OUTPUT_DIR when it is set and non-empty, otherwise /output.
"""

import os
import sys

ENTRY_TEXT = (
    "v5.0.3: walking into a room no longer deletes the reason you walked in. "
    "The reason is now persisted. Retention: 4%.\n"
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as exc:
        print(f"error: cannot create output directory {output_dir!r}: {exc}",
              file=sys.stderr)
        return 1
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as entry_file:
        entry_file.write(ENTRY_TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
