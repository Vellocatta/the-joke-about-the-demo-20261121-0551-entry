#!/usr/bin/env python3
"""Writes one one-line joke about working beside AI coding agents to /output/entry.txt."""
import os

JOKE = "I asked the agent why the demo crashed; it said the code was fine, the demo was fine, and the crash was a hallucination \u2014 mine."

def main():
    # The gate requires 1-280 Unicode code points, not only whitespace.
    assert 1 <= len(JOKE) <= 280 and JOKE.strip(), "joke out of gate bounds"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
