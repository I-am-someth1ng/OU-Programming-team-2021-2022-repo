"""
    Solution to the - https://open.kattis.com/problems/jobbyte

    The approach to the solution is to:
        1. Sequencially inspect the jobs from first to last.
        2. If the job is occupied by the right person, move along.
        3. If the job is occupied by the wrong person, switch them with the person who occupies their job.
            a. Repeat (3) until we finally get our person from some other job. Then move to the next job.
"""

__author__ = "Taras Basiuk"

if __name__ == "__main__":

    N = int(input().strip()) # Read in N
    js = list(map(int, input().strip().split())) # Read in Js

    switches = 0 # Switch counter

    i = 0 # Job iterator
    while i < N: # For every job

        if js[i] == i + 1: # If the job is already occupied by the right person ...
            i += 1 # ... move along.
            continue

        # Otherwise, switch the person occupying our job with whoever occupies their correct job.
        tmp = js[i] # Momorize current person
        js[i] = js[js[i] - 1] # Get the one who occupies our person's correct job
        js[tmp - 1] = tmp # Send our person to their correct job
        switches += 1 # Record the switch happening

    print(switches) # Output the resulting number of total switches that happened.
