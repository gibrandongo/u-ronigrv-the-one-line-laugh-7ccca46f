"""The One-Line Laugh (u-ronigrv-the-one-line-laugh-7ccca46f).

Writes one original funny line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Stdlib only, no network, no clock, no randomness,
no reading of other files. Deterministic: the same line every run.
"""

import os

LINE = (
    "I set five alarms to wake up early, and they all went off together, "
    "so I snoozed the whole committee."
)


def main():
    line = LINE.strip()
    # Gate guard: exactly one sentence, 1-200 characters.
    if not line:
        raise SystemExit("gate failed: line is empty")
    if len(line) < 1 or len(line) > 200:
        raise SystemExit("gate failed: length %d outside 1-200" % len(line))
    if line.count(".") != 1 or not line.endswith("."):
        raise SystemExit("gate failed: line must be exactly one sentence")
    # No internal whitespace surprises: a single sentence is one line,
    # and only one sentence terminator may appear in it.
    if "\n" in line or "\r" in line:
        raise SystemExit("gate failed: line must not contain a newline")
    if sum(line.count(t) for t in ".!?") != 1:
        raise SystemExit("gate failed: line must contain exactly one sentence terminator")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
