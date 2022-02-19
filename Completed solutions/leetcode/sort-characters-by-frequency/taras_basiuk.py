"""
    Solution to the - https://leetcode.com/problems/sort-characters-by-frequency/

    Approach to the solution is to count the occurances of each character in the input string.
    Then we compose the solution string by multiplying each occuring character by the number
    of its occurances and adding the reuslting sustring to the end of the solution string in
    the descending order of the character count occurances.
"""
__author__ = "Taras Basiuk"

class Solution:
    def frequencySort(self, s: str) -> str:

        # Count the character occurances
        char_counts = {}
        for c in s:
            if c not in char_counts:
                char_counts[c] = 0

            char_counts[c] = char_counts[c] + 1

        # Converst the char_counts into a list of [('char1': count1), ('char2': count2), ...]
        result = list(char_counts.items())

        # Sort the above list in the descending order of character counts
        from operator import itemgetter
        result.sort(reverse=True, key=itemgetter(1))

        """
            For each tuple in the above list, multiple each character by its occurance count
            and join the resulting substrings into the returned solution string.
        """
        return "".join(map(lambda t: t[0] * t[1], result))
