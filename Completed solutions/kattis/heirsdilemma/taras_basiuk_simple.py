"""
    Solution to the https://open.kattis.com/problems/heirsdilemma

    The approach to the solution is straightforward. Check all the numbers
    from L to H and see if the conditions hold on them.
"""

__author__ = "Taras Basiuk"

# Read in the input.
L, H = tuple(map(int, input().strip().split()))

result = 0

# Check all the numbers in range
for i in range(L, H + 1):

    # Convert the number into the set of its digits
    digits = {int(c) for c in str(i)}

    # Check condition 1 and 2 by making sure:
    # (1) There are 6 digits in the set (no repeats)
    # (2) Zero is not among the digits
    if len(digits) != 6 or 0 in digits:
        continue

    # Check condition 3
    cond3 = True

    # For each digit
    for d in digits:
        if i % d != 0: # If it doesn't divide the number evenly 
            cond3 = False # Condition is violated
            break # No sense of checking further

    # If conditions held, increment the result
    result += 1 if cond3 else 0

print(result) # Output the result
