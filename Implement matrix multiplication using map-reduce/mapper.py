#!/usr/bin/env python3
import sys

# Read input line by line
for line in sys.stdin:
    line = line.strip()
    matrix, row, col, value = line.split()
    row, col, value = int(row), int(col), int(value)

    if matrix == 'A':  # Emit values to be multiplied with B
        for k in range(2):  # Assuming B has 2 columns
            print(f"{row},{k}\tA,{col},{value}")

    elif matrix == 'B':  # Emit values to be multiplied with A
        for i in range(2):  # Assuming A has 2 rows
            print(f"{i},{col}\tB,{row},{value}")