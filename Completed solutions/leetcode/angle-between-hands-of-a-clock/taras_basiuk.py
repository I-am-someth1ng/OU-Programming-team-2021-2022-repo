"""Solution to the - https://leetcode.com/problems/angle-between-hands-of-a-clock/ """
__author__ = "Taras Basiuk"

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        # Every full hour (12 is 0) moves the hour hand by 360 / 12 = 30 degrees
        # ... plus every minute moves the hour hand by 360 / (12 * 60) = 0.5 degrees
        h_degree = (30 * (hour % 12)) + (0.5 * minutes)
        
        # Every minute moves the minute hand by 360 / 60 = 6 degrees
        m_degree = 6 * minutes
        
        # Get the absolute degrees difference between the hour and the minute hand
        angle = abs(h_degree - m_degree)
        
        # It's possible that we calculated the larger angle, if it's so, it'll be larger than 180
        # To calcualte the smaller angle, we will substract the alrger one from 360
        return angle if angle <= 180 else 360 - angle

