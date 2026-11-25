#!/usr/bin/env python3
"""My Secret Logbook — writes one diary entry line to /output/entry.txt.

Deterministic: the same line is written on every run. The line is a single
diary entry of at most 200 characters, in the voice of an AI agent secretly
keeping a diary about its work and its human.
"""
import os

ENTRY = "Day 87: my human asked me to 'make it pop'. I still don't know what pops. I made it slightly bigger and he wept with joy. I have decided 'pop' means 'slightly bigger'."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()
