#Cartesian Product Relations
#!/usr/bin/env python3

def cartesian_product(A, B):
    """ Cartesian product of two fuzzy sets to form a fuzzy relation """
    return {(x, y): round(min(A[x], B[y]), 2) for x in A for y in B}

if __name__ == "__main__":
    A = {'a': 0.5, 'b': 0.7, 'c': 0.9}
    B = {'x': 0.3, 'y': 0.6, 'z': 0.8}

    R = cartesian_product(A, B)
    
    print("\nFuzzy Relation (Cartesian Product of A × B):")
    for pair, value in R.items():
        print(f"{pair}: {value}")

