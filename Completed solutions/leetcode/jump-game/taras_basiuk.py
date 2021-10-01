# Solution for the https://leetcode.com/problems/jump-game
__author__ = "Taras Basiuk"

"""
    The approach of this solution is for each jump to pick
    a landing such as the sum of its index and its maximum
    allowed length of the next jump is the highest.

    If we ever can jump all the way to the end of the list - we win.
    If we ever find ourself jumping to a cell with zero jumping length - we lose.
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        pos = 0 # Current position

        while True: # We will check the win/lose condition elsewhere

            # Check the win condition
            if pos + nums[pos] >= len(nums) - 1:
                return True

            # We init. the candidate for the next jump with the current position.
            n_pos = pos
            n_pot = 0 # We init. best next landing potential with 0

            for i in range(1, nums[pos] + 1): # For every cell we can reach to

                # Check if its potential (index plus jump lenght) is best so far
                if pos + i + nums[pos + i] >= n_pot: # If so
                    n_pos = pos + i # Override the next jump position...
                    n_pot = pos + i + nums[pos + i] # ...and the next jump potential

            # Check the lose condition
            if nums[n_pos] == 0:
                return False

            # Make the jump
            pos = n_pos
