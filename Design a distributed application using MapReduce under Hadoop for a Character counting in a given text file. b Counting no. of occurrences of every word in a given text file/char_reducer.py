#!/usr/bin/env python3
import sys
from collections import defaultdict

char_count = defaultdict(int)

# Read input from standard input
for line in sys.stdin:
    line = line.strip()
    if not line or "\t" not in line:  # Ignore empty or invalid lines
        continue

    try:
        char, count = line.split("\t")
        char_count[char] += int(count)
    except ValueError:
        continue  # Ignore lines that don't match expected format

# Print the final counts
for char, count in char_count.items():
    print(f"{char}\t{count}")
