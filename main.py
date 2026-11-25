"""make.fun bounty entry: u-mang-the-moon-finally-answers-back

Writes the Moon's one-line comeback to /output/entry.txt.
"""

import os

# Verified count: 68 chars (UTF-8 bytes), gate is 1-240 chars, no trailing newline.
LINE = "You wished on me at 2 a.m. again. I am a rock, not customer service."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
