#!/usr/bin/env python3
import sys
from collections import defaultdict

# Store values by keys
product_terms = defaultdict(list)

# Read input from standard input
for line in sys.stdin:
    key, value = line.strip().split("\t")
    product_terms[key].append(value)

# Compute matrix multiplication result
result = defaultdict(int)
for key, values in product_terms.items():
    a_values = {int(v.split(",")[1]): int(v.split(",")[2]) for v in values if v.startswith("A")}
    b_values = {int(v.split(",")[1]): int(v.split(",")[2]) for v in values if v.startswith("B")}

    for k in a_values:
        if k in b_values:
            result[key] += a_values[k] * b_values[k]

# Print the final matrix product
for key, value in sorted(result.items()):
    print(f"{key}\t{value}")