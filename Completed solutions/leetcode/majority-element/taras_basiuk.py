"""Solution to - https://leetcode.com/problems/majority-element/"""
__author__ = "Taras Basiuk"

"""
    Approach to the solution is to use Boyer-Moore majority Vote Algorithm, 
    which is similar to king-of-the-hill competition - 
        https://www.cs.utexas.edu/~moore/best-ideas/mjrty/
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        cand = None # Current canidate is unknown
        support = 0 # Support of the current candidate

        for n in nums: # For every number in nums

            # If n is current candidate, increase support for current canidate
            if n == cand:
                support += 1

            # If n is not current candidate, but support for current candidate is positive,   
            # decrement the support for the current candidate 
            elif support > 0:
                support -= 1

            # If n is not current candidate, and the support for current candidate is zero,
            # make n the new candidate with the support of 1
            else:
                cand = n
                support = 1

        # Majority candidate is guaranteed to win this king-of-the-hill voting
        return cand
