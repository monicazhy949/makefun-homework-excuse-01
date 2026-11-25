"""The Dog Ate My Homework: Funniest Excuse.

Writes a single-line excuse, in the dog's own voice, to /output/entry.txt.
"""

from pathlib import Path

ENTRY = "I read it first — the answers were wrong, so I fixed them the only way I know how. You're welcome. I saved your grade."


def main() -> None:
    print(ENTRY)
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
