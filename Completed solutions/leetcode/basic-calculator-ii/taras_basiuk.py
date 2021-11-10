"""Solution to the - https://leetcode.com/problems/basic-calculator-ii/"""
__author__ = "Taras Basiuk"

class Solution:
    def calculate(self, s: str) -> int:
        """
            Approach to the solution is the following:
                1. Whenever we encounter a whitepace - we ignore it.
                2. We consider the input string to be a sequence of segments separated by the '+' or '-' operations
                3. Each segment consists of subsegments separated by the '*' and '/' operators
                4. Both segments and subsegments are initialized with the value of 0
                5. Subsegment's value increases when we encounter another integer
                6. Segment's value increases/decreases when we find the value of the subsegment to be multipled/divided by
                7. When the segment ends (we enounter another '+' or '-') it's value is added/substracted to the result

            For example, in "2*3+6/4", "2*3" and "6/4" are segments, "2" and "3" are subsegments of the first segment.
        """

        result = 0 # Result of adding up or substructing segments of expression together

        segment = 0 # Initiate new segment
        sum_op = True # sum_op is True if will add the segment to the result, False if we will substact

        subsegment = 0 # Initiate new subsegment
        # mul_op is True if will multiply the subsegment to the segment, False if we will divide
        mul_op = None # None is a special case for the first subsegment

        i = 0 # string character index used for iteration though the string
        while i < len(s): # Inner loop

            if s[i] == ' ': # Ignore the whitespace
                pass

            elif s[i] == '*' or s[i] == '/': # If we encountered '*' or '/' that means that the previous subsegment has ended
                if mul_op == None:
                    segment = subsegment # If this was the first subsegment, it will be the current value of the segment
                else:
                    # Otherwise, multiply/divide the current value of the segment by the subsement value
                    # depending on wether the previous operator was multiplication or division
                    segment = segment * subsegment if mul_op else segment // subsegment
                subsegment = 0 # Initilize new subsegment
                mul_op = (s[i] == '*') # Record the type of (now) previous operator

            elif s[i] == '+' or s[i] == '-': # If we encountered '+' or '-' that means that the previous segment has ended
                # First we integrate the value of the last subsegment into the segment the same way as before
                if mul_op == None:
                    segment = subsegment
                else:
                    segment = segment * subsegment if mul_op else segment // subsegment

                # Then we integrate the value of the segment into the result
                result = result + segment if sum_op else result - segment

                # Then we initialize a new segment and a new subsegment.
                segment = 0
                subsegment = 0
                sum_op = (s[i] == '+')
                mul_op = None

            else: # Digit was encountered, increase the subsegment value
                subsegment = (10 * subsegment) + int(s[i])

            i += 1 # Keep iterating through the string

        # Once the iteration through the string is done,
        #   we still need to integrate the last subsegment and segment into the final solution.
        if mul_op == None:
            segment = subsegment
        else:
            segment = segment * subsegment if mul_op else segment // subsegment

        return result + segment if sum_op else result - segment
