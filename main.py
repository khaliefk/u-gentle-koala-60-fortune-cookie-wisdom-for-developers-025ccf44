#!/usr/bin/env python3
"""Write one original fortune-cookie line for a software developer."""

import os

FORTUNE = "The legacy code you curse today was once the cleverest code in the room."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
