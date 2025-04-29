#!/usr/bin/env python3
import sys

# Read input line by line
for line in sys.stdin:
    line = line.strip()  # Remove whitespace
    words = line.split()  # Split into words
    for word in words:
        print(f"{word}\t1")  # Emit (word, 1)