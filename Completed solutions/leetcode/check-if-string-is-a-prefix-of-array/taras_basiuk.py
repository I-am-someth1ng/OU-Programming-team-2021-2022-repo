"""Solution to the - https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/"""
__author__ = "Taras Basiuk"

"""
    Approach to solution is considering words one by one until one of the following happens:
    1. Length of words considered so far is larger than length of s (return False)
    2. Next word doesn't occure in the expected place in s (return False)
    3. Length of words considered so far matches the length of s (return True)
    4. We run out of words before the s is constructed (return False)
"""
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:

        ls = len(s) # Save the length of the s
        lws = 0 # Length of the words considrede so far

        for w in words: # Consider the words one by one
            lw = len(w) # Save the length of the w

            # If the length of the words considered so far, plus the length of w
            # is larger than lengths of s, then s is not a prefix
            if lws + lw > ls:
                return False

            # If w is not included in the appropriate place in s, then s is not a prefix
            if s[lws : lws + lw] != w:
                return False

            lws += lw # Update the length of the words considered so far

            # If the length of the words considered so far matches lengths of s,
            # then s is the prefix (since we compared the contents already)
            if ls == lws: 
                return True

        # If there was never enough words to make up the length of s, then s is not a prefix
        return False
