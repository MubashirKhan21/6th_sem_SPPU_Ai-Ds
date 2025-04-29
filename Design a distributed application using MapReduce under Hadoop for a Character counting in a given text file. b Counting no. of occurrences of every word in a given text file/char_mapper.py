#!/usr/bin/env python3
import sys

# Read input line by line
for line in sys.stdin:
    line = line.strip()  # Remove whitespace
    for char in line:
        if char:  # Ensure it's not an empty character
            print(f"{char}\t1")  # Emit (char, 1)
