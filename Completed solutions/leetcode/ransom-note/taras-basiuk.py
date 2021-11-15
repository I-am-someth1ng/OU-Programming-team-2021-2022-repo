"""
    Solution for the - https://leetcode.com/problems/ransom-note/
"""
__author__ = "Taras Basiuk"

"""
    The approach to the solution is to start traversing the note.
    For each character needed by the node we check whether we haven't encountered
    enough of those characters in the magazine before. If we haven't - we start/continue
    traversing the magazine recording the spare encountered characters until we encounter
    the one we're looking for. After that, we return to traversing the note.
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ml = len(magazine)   # Length of the magazine string
        nl = len(ransomNote) # Length of the note string

        if nl > ml: # If the note is longer than the magazine, the note cannot be constructed
            return False

        mi = 0 # Magazine traversal index

        # Array of character counts from the magazine not used in the Note so far.
        # 0 index is for 'a', 1 index is for 'b', and so on...
        spare_chars = [0] * 26

        ni = 0 # Note traversal index
        while ni < nl: # Traverse the entire node

            """
                Character index (in the spare_chars) of the next character from the note
                Since ord('a') returns 97, ord('b') returns 98 and so on,
                we subtract 97 to match the spare_chars index.
            """
            ci = ord(ransomNote[ni]) - 97

            ni += 1 # We can increment the note index at this time

            # If there's already a spare character of the kind we're looking for,
            #     just decrement the count of available characters, and move to the next character in the note
            if spare_chars[ci] > 0:
                spare_chars[ci] -= 1
                continue # Move to the next character in the note

            # If there's no spare characters available, we continue traversing the magazine
            while True:
                if mi >= ml: # If no more characters left in the magazine, the note cannot be constructed
                    return False

                # Update the spare_chars with the next character found in the magazine
                spare_chars[ord(magazine[mi]) - 97] += 1
                mi += 1 # Increment the magazine index

                # If there's enough of the needed character, decrement the count and move over to the next note character
                if spare_chars[ci] > 0:
                    spare_chars[ci] -= 1
                    break

        # If we found enough spare characters for the entire note, than the note can be constructed
        return True
