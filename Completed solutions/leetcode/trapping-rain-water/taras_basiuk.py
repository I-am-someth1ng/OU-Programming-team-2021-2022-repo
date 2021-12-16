"""
    Solution to the - https://leetcode.com/problems/trapping-rain-water/
"""
__author__ = "Taras Basiuk"

class Solution:
    def trap(self, height: List[int]) -> int:

        # First we find the (first occurance of the) highest elevation index (hei) in the whole array
        hei = 0
        l = len(height)
        for i in range(1, l):
            if height[i] > height[hei]:
                hei = i

        water = 0 # Total water captured counter

        # We traverse the elevations from the left edge of the array to 'hei'
        cei = 0 # Current elevation index
        for i in range(1, hei + 1):

            # If we encounter an elevation that is higher or equal than the current elevation
            if height[i] >= height[cei]:
                # 1. Backtrack and collect all the water for elevations lower than 'cei'
                for j in range(cei + 1, i):
                    water += (height[cei] - height[j])

                # 2. Update the cei to new elevation
                cei = i

        # Now we traverse the elevations from the right edge of the array to 'hei'
        cei = l - 1 # Current elevation index
        for i in range(l - 2, hei - 1, -1):

            # If we encounter an elevation that is higher or equal than the current elevation
            if height[i] >= height[cei]:
                # 1. Backtrack and collect all the water for elevations lower than 'cei'
                for j in range(cei - 1, i, -1):
                    water += (height[cei] - height[j])

                # 2. Update the cei to new elevation
                cei = i

        return water
