#Fuzzy Set Operations
#!/usr/bin/env python3

def fuzzy_union(A, B):
    """ Union of two fuzzy sets (max operation) """
    return {x: max(A.get(x, 0), B.get(x, 0)) for x in set(A) | set(B)}

def fuzzy_intersection(A, B):
    """ Intersection of two fuzzy sets (min operation) """
    return {x: min(A.get(x, 0), B.get(x, 0)) for x in set(A) & set(B)}

def fuzzy_complement(A):
    """ Complement of a fuzzy set (1 - membership value) """
    return {x: round(1 - A[x], 2) for x in A}

def fuzzy_difference(A, B):
    """ Difference of two fuzzy sets (A - B = min(A, 1 - B)) """
    return {x: min(A.get(x, 0), 1 - B.get(x, 0)) for x in A}

if __name__ == "__main__":
    A = {'a': 0.5, 'b': 0.7, 'c': 0.9}
    B = {'a': 0.2, 'b': 0.8, 'd': 0.6}

    print("Union:", fuzzy_union(A, B))
    print("Intersection:", fuzzy_intersection(A, B))
    print("Complement of A:", fuzzy_complement(A))
    print("Difference A - B:", fuzzy_difference(A, B))
