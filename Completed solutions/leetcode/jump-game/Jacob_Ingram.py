# Author:Jacob Ingram
# Problem:https://leetcode.com/problems/jump-game/submissions/

# This solution implements a greedy algorithm that goes down 
# the array by finding the best next point to jump to, if it 
# can't find a better place to jump to from its current position
# it assumes that there are no good moves that can be made and
# returns false.
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # keeps track of where we are in the array
        pos = 0 
        while True:
            # keeps track of the current best jump size available to us
            bestJumpSize = 0
            # keeps track of where the index of the best place to jump to is when searching for the next place to jump
            bestJumpIndex = 0
            #if we can jump to the end from where we are at now, we know that we can jump to the last index
            if nums[pos] + pos + 1 >= len(nums):
                return True
            else:
                # this else statement handles most of the logic in this solution, finding the best place to jump 
                # to from where we are currently at in the array.
                for i in range(1, nums[pos] + 1):
                    if nums[i + pos] + (i + pos) >= bestJumpSize + bestJumpIndex:
                        bestJumpIndex = i + pos
                        bestJumpSize = nums[i + pos]
                # if bestJumpSize equals zero, then there are no possible jumps that can get us to the end of the array
                if bestJumpSize == 0:
                    return False
                else:
                    pos = bestJumpIndex
