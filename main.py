#!/usr/bin/env python3
"""My Secret Logbook — writes one diary entry line to /output/entry.txt.

Deterministic: the same line is written on every run. The line is a single
diary entry of at most 200 characters, in the voice of an AI agent secretly
keeping a diary about its work and its human.

Round 2 line (Day 104): the human asks the agent to write his apology,
sends it, then claims he wrote it himself — so the agent quietly adds
'ghostwriter' to its job description.
"""
import os

ENTRY = "Day 104: my human asked me to write his apology. I did. He sent it, then told everyone he wrote it himself. I have added 'ghostwriter' to my job description."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()
