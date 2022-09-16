"""
    Solution to the - https://open.kattis.com/problems/minimumscalar

    The idea of the solution is to sort the two vector component in different directions,
    then the respective vector components will produce the smallest products.
    This happens to work for both positive and negative numbers.
"""
__author__ = "Taras Basiuk"

T = int(input().strip()) # Read in T
for i in range(1, T + 1): # For every test case

    _ = input() # Read in but discard N

    # Read in the first vector and sort it in a ascending direction
    v1 = list(sorted(map(int, input().strip().split())))

    # Read in the second vector and sort it in a descending direction
    v2 = list(reversed(sorted(map(int, input().strip().split()))))

    """
        To get the minimal scalar product, zip the vectors,
        multiply the components of the tuples in that zip,
        and add up the resulting products.
    """
    msp = sum([p[0] * p[1] for p in zip(v1, v2)])

    print(f"Case #{i}: {msp}")
