# Solution for - https://leetcode.com/problems/shortest-unsorted-continuous-subarray
__author__ = "Taras Basiuk"

class Solution:
    
    """
        This is a simpler but slower (n log n) solution for this problem.
        
        The approach is to (1) make a sorted copy of the input array.
        
        Then (2) moving from the left (and later right) edge of the array we
        record where we first detect the difference between the two arrays.
        
        We then (3) conclude that all the numbers in the original array between
        the first detected differences will have to be sorted in order for the
        entire array to end up being sorted.
        
        So, we (4) return the length of the region of difference as the output.
    """
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        # Make a sorted copy of the input array
        s_nums = sorted(nums)
        
        # First detect the left edge of the region of difference
        left = 0 # Starting from the left edge of the array

        # Going all the way back to the end of it
        while(left < len(nums)):
            if nums[left] != s_nums[left]: # If we detect the difference
                break # Stop looking
                
            left += 1 # Otherwise, consider the next number on the right

        # Next detect the right edge of the region of difference
        right = len(nums) - 1 # Starting from the left edge of the array

        # Going all the way forward to the left edge of difference region
        while(right > left):
            if nums[right] != s_nums[right]: # If we detect the difference
                break # Stop looking
                
            right -= 1 # Otherwise, consider the next number on the left
            
        # Return the length of the difference region
        # (if it's longer than one, no point of sorting a single number)
        return (right - left) + 1 if right > left else 0
