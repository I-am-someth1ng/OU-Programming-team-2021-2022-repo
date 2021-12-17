"""
    Solution for the - https://leetcode.com/problems/integer-break/
"""
__author__ = "Taras Basiuk"

"""
    The approach to the solution is the following:
        1. If we know k, the maximum product can be obtained by keeping the factors as equal as possible.
        2. We don't know how to pick the optimal k correctly, but we can afford to try all of the feasible ones.
"""
class Solution:
    def integerBreak(self, n: int) -> int:

        best_result = 1 # Container for the maximum product across different Ks

        for k in range(2, (n // 2) + 2): # Feasible Ks appear to be in range 2 .. (n // 2) + 1
            component = n // k # This calculates the smallest factor value
            plus_ones = n % k # This calculates how many factors will be one larger than the minimumm
            result = 1 # Container for the product for the current k

            for i in range(k): # For each factor
                result *= ((component + 1) if (i < plus_ones) else component) # Caluclate the product

            # If the product for this k is larger than what we've seen before, store the new best
            if result > best_result:
                best_result = result

        return best_result # Return the largest product
