"""
    Solution to the -https://open.kattis.com/problems/reseto

    The approach to the solution is a straightforward implementation of the sieve of Eratosthenes algorithm.
"""
__author__ = "Taras Basiuk"

if __name__ == "__main__":
    n, k = tuple(map(int, input().strip().split())) # Read in N and K

    ps = [True] * (n + 1) # Prepare a zero-indexed array for prime numbers
    i = 2 # Initialize array iterator
    result = None # Result container

    while i <= n and k > 0: # Iterate through the array while still have numbers to cross out
        if ps[i]: # If encountered a prime number

            for j in range(i, n + 1, i): # For each multiple of the prime number in range
                if ps[j]: # If not crossed out yet
                    ps[j] = False # Cross the number out
                    k -= 1 # Decrement the crossing out counter

                    if k == 0: # If no numbers left to cross out
                        result = j # Record the last crossed out number as the result
                        break # No need to cross the numbers out anymore

        i += 1 # Increment the array iterator

    print(result) # Print out the end result
