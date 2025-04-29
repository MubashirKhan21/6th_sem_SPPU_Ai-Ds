#Max-Min Composition
#!/usr/bin/env python3
import numpy as np

def max_min_composition(R1, R2):
    """ Max-Min Composition of two fuzzy relations """
    X = sorted(set(x for x, _ in R1))
    Y = sorted(set(y for _, y in R1))
    Z = sorted(set(z for _, z in R2))

    matrix_R1 = np.array([[R1.get((x, y), 0) for y in Y] for x in X])
    matrix_R2 = np.array([[R2.get((y, z), 0) for z in Z] for y in Y])

    composed_matrix = np.zeros((len(X), len(Z)))

    for i in range(len(X)):
        for j in range(len(Z)):
            composed_matrix[i][j] = max(min(matrix_R1[i, k], matrix_R2[k, j]) for k in range(len(Y)))

    return {(X[i], Z[j]): composed_matrix[i, j] for i in range(len(X)) for j in range(len(Z))}

if __name__ == "__main__":
    A = {'a': 0.5, 'b': 0.7, 'c': 0.9}
    B = {'x': 0.3, 'y': 0.6, 'z': 0.8}
    C = {'p': 0.4, 'q': 0.7}

    R1 = {(a, b): min(A[a], B[b]) for a in A for b in B}
    R2 = {(b, c): min(B[b], C[c]) for b in B for c in C}

    print("\nMax-Min Composition of R1 and R2:")
    composition = max_min_composition(R1, R2)
    for pair, value in composition.items():
        print(f"{pair}: {value}")

