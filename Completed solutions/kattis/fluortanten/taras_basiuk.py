"""
    Solution to the - https://open.kattis.com/problems/fluortanten

    The approach to the solution is to find a spot in the queue where the sum of reluctance of the children
    behind that spot in the queue is largest. Inserting Björn in that spot thus will yield the largest boost
    to the collective happiness.

    To the above efficiently:
        1. We start traversing the queue (ignoring Björn) from the end moving to the front.
        2. We calculate the running happiness and the sum of the reluctance of the children in the tail of the queue.
        3. Every time we observe the new sum of the reluctance in the tail of the queue we record the new maximum.
        4. Once the traversal is over, the maximum total happiness that can be achieved by moving Björn is the sum
            of the current happiness in the queue with Björn removed plus the maximum sum of reluctance of children
            in the optimal tail of the queue (as inserting Björn at that spot increases the multiplier of every child's
            reluctance in the tail of the queue by one as it contributes to the new sum of happiness).
"""
__author__ = "Taras Basiuk"

if __name__ == "__main__":
    n = int(input().strip()) # Read in the N value
    As = list(map(int, input().strip().split())) # Read in the a_i values

    happiness, sum_reluctance, max_sum_reluctance = 0, 0, 0 # Initialize the happiness and the reluctance trackers
    björn_encountered = False # Flag for tracking whether Björn was already encountered or not

    for i in range(n, 0, -1): # Traverse the queue back to front

        if As[i - 1] == 0: # If Björn is encountered, set the corresponding flag and move over to the next child
            björn_encountered = True
            continue

        """
            Update the total happiness in the queue.
            If Björn wasn't encountered yer, the multiplier of this child's reluctance to the total happiness
                is one less, as Björn will be removed from the queue (before being placed in the optimal position).
        """
        happiness += (As[i - 1] * (i if björn_encountered else i - 1))

        sum_reluctance += As[i - 1] # Record the current sum reluctance of the children at the tail of the queue.

        # If the currently observed sum reluctance is the maximum so far - record it.
        if sum_reluctance > max_sum_reluctance:
            max_sum_reluctance = sum_reluctance

    """
        The result is the sum of the current happiness in the queue (with Björn removed) plus the maximum sum reluctance
        existing at some tail of the queue in from of which Björn will be placed.
    """
    print(happiness + max_sum_reluctance)
