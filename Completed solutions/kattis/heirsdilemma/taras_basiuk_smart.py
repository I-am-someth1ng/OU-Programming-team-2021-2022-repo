"""
    Solution to the https://open.kattis.com/problems/heirsdilemma

    The approach to the solution is check every 6-element permutation of 9 digits.
    This should be faster than checking every number in the given range, for long ranges.
    On Kattis testset this approach completed in 0.06s vs 0.26s for the straightforward approach.
"""

__author__ = "Taras Basiuk"

# Read in the input.
L, H = tuple(map(int, input().strip().split()))

from itertools import permutations

result = 0
for cand in permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 6): # Generate the permutations

    # Convert the permutation into a number
    number = 0
    for digit in cand:
        number *= 10
        number += digit

    # Check if the number is in range
    if number < L or number > H:
        continue

    # Check if the number is divisible by every digit in the permutation (condition 3)
    cond3 = True
    for digit in cand:
        if number % digit != 0:
            cond3 = False
            break

    result += 1 if cond3 else 0 # If condition 3 holds increment the result

print(result) # Output the result
