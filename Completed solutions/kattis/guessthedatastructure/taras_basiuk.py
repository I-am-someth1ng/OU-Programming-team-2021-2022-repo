"""
    Solution to the - https://open.kattis.com/problems/guessthedatastructure

    Approach to the solution is to run the three candidate data structures in question,
    and compare their outputs against the output of the mystery data structure.
"""

__author__ = "Taras Basiuk"

from collections import deque
import heapq
import queue

try:
    while True: # We read input until EOFError is thrown

        n = int(input().strip()) # Read in the number of commands for this test case

        # Prepare the candidate data structures
        q, q_out = deque(), [] # Queue
        s, s_out = [], [] # Stack
        pq, pq_out = [], [] # Priority Queue

        guess_out = [] # Output of the mystery data structure

        for i in range(n): # For each command
            # Read in the type of command and the associated data
            command, data = tuple(map(int, input().strip().split()))

            if command == 1:
                # Entering new data
                q.append(data)
                s.append(data)
                heapq.heappush(pq, -data)

            else: # command == 2
                # Record the output of the mystery data structure
                guess_out.append(data)

                # Extract data from the candidate data structures
                q_out.append(q.popleft() if q else None)
                s_out.append(s.pop() if s else None)
                pq_out.append(-heapq.heappop(pq) if pq else None)

        # Figure out the result
        result = "impossible" # We start with "imposible"

        # If the outputs of the queue and mystery data structures match, result is "queue"
        result = "impossible" if q_out != guess_out else "queue"

        # If the outputs of the stack and mystery data structures match...
        if s_out == guess_out:
            # ... the result is "stack" if it was "impossible" before, or "not sure" if it was "queue" before
            result = "stack" if result == "impossible" else "not sure"

        # If the outputs of the priority queue and mystery data structures match...
        if pq_out == guess_out:
            # ... the result is "stack" if it was "impossible" before
            # or "not sure" if it was "queue" or "stack" before
            result = "priority queue" if result == "impossible" else "not sure"
        
        print(result) # Output the result

except EOFError:
    # Reached end of file, we're done
    pass
