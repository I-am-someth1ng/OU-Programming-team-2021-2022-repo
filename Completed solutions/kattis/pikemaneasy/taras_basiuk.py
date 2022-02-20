"""
    Solution to the - https://open.kattis.com/problems/pikemaneasy

    The approach to the solution is to:
        1. Calculate the time it takes to solve each solution by using the formula given.
        2. Sort the solution times in ascending order.
        3. Submit solutions one by one until we run out of time or solutions.
"""

__author__ = "Taras Basiuk"

if __name__ == "__main__":

    N, T = tuple(map(int, input().strip().split())) # Read in N and T
    ts = [0] * N # Prepare an array for the solution times of N problems

    # Read in A, B, C, ts[0]
    A, B, C, ts[0] = tuple(map(int, input().strip().split()))

    # Calculate the solution times for all other porblems and sort them in ascending order.
    for i in range(1, N):
        ts[i] = ((A * ts[i - 1] + B) % C) + 1
    ts.sort()

    # Trackers for problems solved, time expended, and penalty accrued.
    solved, time, penalty = 0, 0, 0

    for t in ts: # For every solution
        time += t # Update the time when we can submit this solution the earliers

        if time > T: # If the submission time is above the limit, break out of the loop.
            break

        solved += 1 # Submit the solution and update the number of solved problems ...
        penalty = (penalty + time) % 1000000007 # ... and the penalty accrued

    print(solved, penalty) # Print out the results
