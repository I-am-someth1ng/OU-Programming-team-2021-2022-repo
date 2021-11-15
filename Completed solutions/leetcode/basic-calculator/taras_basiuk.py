"""
    Solution for the - https://leetcode.com/problems/basic-calculator/

    Approrach to the solution is breaking the input strings into the segments enclosed in '()'
    brakets. Values of the segments are being (recursively) calculated by adding up the subsegments
    separated by '+/-' operators.
"""
__author__ = "Taras Basiuk"

class Solution:

    # Solution member variables
    s = None # Input string value holder
    l = None # Input string length value holder

    """
        Recursive function which calculates the value of the input string segment,
        starting from the given 'i' index to the unmatched ')' or the end of the string.
        Calculation is done by adding/substracting subsegments of integers and/or expressions
        enclosed in matching set of '()' brakets.

        Input:
            i      - Index of the input string from which the segment value should be
                     calculated.
        Output:
            result - The calcualted value of the segment
            i      - Index of the input string where the segment has ended
                     (ans the supersegment can continue its calculation)
    """
    def calc_segment(self, i):

        result = 0 # Initial value of the segment
        subsegment = 0 # Initial value of the subsegment

        # Whether the operation of integrating the subsegment value (once it's known)
        # into the segment value is add or substract.
        add_op = True

        # Until the end of the input string is reached, or an unmatched ')' is encountered.
        while i < self.l:
            c = self.s[i] # Current character considered

            if c == ')': # If ')' is encountered just break out of the cycle
                break

            # If the whitespace is encontered, just move over to the next character
            if c == ' ':
                i +=1
                continue

            # If the opening bracket is encountered, we need to recursevely call calc_segment
            # to calculate the value of the new subsegment
            if c == '(':
                # As there no case such as '(' is not preceeded by a '+/-' operator,
                # there no need to integrate current value of the subsegment yet
                subsegment, i = self.calc_segment(i + 1)
                i += 1 # increment the index from the last character of the subsegment
            elif c == '+' or c == '-':
                # If we encounter a '+/-' operator, the subsegment has ended,
                # we need to integrate it into the result, and start a new one
                result = result + subsegment if add_op else result - subsegment
                subsegment = 0 # Strat a new subsegment
                add_op = c == '+' # Remember how to integrate the value of the new subsegment
                i += 1
            else:
                # We only get here if we encounter another integer,
                # so we integrate in into the subsegment value.
                subsegment = (subsegment * 10) + int(c)
                i += 1

        # We reach here once the end of the input string is reached or an unmatched ')'
        # is encountered. So we integrate the subsegment into the segment value one last time
        # and return the end index of our segment to the caller.
        return result + subsegment if add_op else result - subsegment, i

    def calculate(self, s: str) -> int:

        # Save the input string and its length as Solution class memebr variables
        self.s = s
        self.l = len(s)

        # Call the cals_segment starting from the first character,
        # accept its returned value as an overall solution
        return self.calc_segment(0)[0]
