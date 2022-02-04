"""
    Solution to the - https://open.kattis.com/problems/kodkraft

    The approach to the solution is dynamic programming as follows:
        1. Try start competing on every possible date for the first division.
        2. For each such possibility find the closest date to compete in division 2.
        3. For each distinct date when we can advance, only record the shortest time it took us to get to that date.
        4. Go back to step 2, now advancing to division 3, 4, 5 .. K.
        5. Among all dates of advancement to division K, pick the shortest advancement time.
"""
__author__ = "Taras Basiuk"

import bisect

if __name__ == "__main__":
    n, k = tuple(map(int, input().strip().split())) # Read in N and K
    contests_list = list(map(int, input().strip().split())) # Read in the list of contest dates

    contests_by_division = {} # Container for the dates when the contests in each division happen
    for i in range(k): # For each division
        contests_by_division[i + 1] = [] # Initialize the contest date empty list

    # Populate the contests_by_division dates
    for i in range(n):
        contests_by_division[contests_list[i]].append(i)

    # Set of all possible dates when Nicolas can advance to the next division (and the time it took him to advance)
    advancement = {}

    # Populate the advancement dictioary for the first division with contests dates and 1 as the time it took to advance
    for contest_date in contests_by_division[1]:
        advancement[contest_date] = 1

    for i in range(2, k + 1): # For the advancement to the divisions 2 through K
        next_advancement = {} # We will record the same data date => time taken for the advancement to 'i' division

        # For each date we advanced to the previous division
        for previous_division_date in advancement:

            """
                Find the earliest date Nicolas can advance to the next division:
                    1. If we were to insert the previous_division_date in contests_by_division[i], what would be the
                        insertion index (next_division_date_i)?
                    2. If it's within the length of contests_by_division[i], that's where we will find the date of
                        the next possible advancement.
                    3. If the insertion idex is at the end of the contests_by_division[i] array, we wil instead 
                        take the first available date of the next year.
            """
            next_division_date_i = bisect.bisect(contests_by_division[i], previous_division_date)
            next_division_date = None
            if next_division_date_i < len(contests_by_division[i]):
                next_division_date = contests_by_division[i][next_division_date_i]
            else:
                next_division_date = contests_by_division[i][0]

            # Calculate how long the advancement will take
            advancement_time = next_division_date - previous_division_date # If advancement is later in the same year
            if advancement_time < 0:
                advancement_time = n + advancement_time # if advanecemnt is in the new year (negative)
            # Also add the time it took to advance to the previous division
            advancement_time += advancement[previous_division_date]

            # Update the next advancement dictionary
            if next_division_date not in next_advancement:
                # If we never advanced to the next division on the next_division_date - just record the advancement_time
                next_advancement[next_division_date] = advancement_time
            else:
                # ... otherwise, only record the advancement_time if it's lower than what we've seen before
                if next_advancement[next_division_date] > advancement_time:
                    next_advancement[next_division_date] = advancement_time

        advancement = next_advancement # Copy over (by reference) the advancement dictionary for the next division

    # Now, find the fastest advanecemnt to the division k
    fastest_advancement = 10 ** 12 # large enough initial number
    for last_division_date in advancement:
        if advancement[last_division_date] < fastest_advancement:
            fastest_advancement = advancement[last_division_date]

    # Print out the result
    print(fastest_advancement)
