"""
    Solution to the - https://open.kattis.com/problems/downtime

    The approach to the solution is to maintain an in-progress double-ended queue to hold the current requests.
    As the minimum number of servers needed can only be exceeded when the new requests are coming in we do the next:
        1. When the new request comes in we add it to the end of the deque
        2. Then we drop all requests processed already after the previous request came in from the begining of the deque
        3. Then we see how many requests are in progress and how many servers needed to serve them
        4. If that number of servers is larger than what we've seen before, we update the new minimum
        5. Once all the requests are processed, the largest observed minimum is returned as the result
"""
__author__ = "Taras Basiuk"

from collections import deque

if __name__ == "__main__":
    n, k = tuple(map(int, input().strip().split())) # Read in N and K

    min_serv = 0 # Minimum number of servers needed to handle the workload
    in_progress = deque([]) # Double-ended queue(deque) holding all the timestamps of the requests currently in progress

    for _ in range(n): # For each of N timestamps
        ct = int(input().strip()) # Read in the next timestamp

        in_progress.append(ct) # Add the timestamp of the current request to the end of the in_progress deque

        # Now remove all the jobs from the beginning of the in_progress deque which must've been processed by now
        while in_progress[0] <= ct - 1000:
            in_progress.popleft()

        cip = len(in_progress) # Record how many jobs are actually currently in progress(cip)
        cur_serv = (cip // k) + (1 if cip % k > 0 else 0) # Calculate how many servers are processing current requests

        # Update the minimum number of servers needed to handle the workload, if appropriate
        min_serv = cur_serv if cur_serv > min_serv else min_serv

    print(min_serv) # Output the result
