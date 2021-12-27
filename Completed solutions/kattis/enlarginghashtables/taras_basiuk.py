"""
    Solution to the - https://open.kattis.com/problems/enlarginghashtables

    The approach to the solution is to:
        (1) Read in all input and find the largest n.
        (2) Prepare all the prime factors needed to check the candidates for primality using the Sieve of Eratosthenes
        (3) Check the candidates in the range determined by the Oppermann's conjecture for primality
        (4) First (smallest) suitable (prime) candidate is reported as a result.
"""
__author__ = "Taras Basiuk"

from math import sqrt, ceil

if __name__ == '__main__':

    input_data = [] # Input data container
    max_n = 0 # Largest n observed in the input data

    # Read in the entirety of input data
    while True:
        n = int(input().strip()) # Read in the next piece of data

        if n == 0: # If n is 0, that's the end of theinput data
            break

        input_data.append(n) # Add n to the input data container
        if n > max_n: # Check if this n is the largest so far
            max_n = n

    # Make sure max_n is not too small (relevant for the Oppermann's conjecture below)
    max_n = 100 if max_n < 100 else max_n

    """
        According to Oppermann's conjecture, for large enough numbers (100 should be large enough),
        the gap between adjacent prime numbers is smaller then the square root of the lesser number.

        As such, the prime factors we will need to consider to determine the primality of our candidates
        will lay in range of [2 .. sqrt(2*max_n)], so here we prepare the list of such prime factors
    """
    prime_factors_dict = {}
    for i in range(ceil(sqrt(2*max_n) + 1)):
        prime_factors_dict[i] = True

    """
        Here, we start the Sieve of Eratosthenes algorithms to find the relevant prime factors.
    """
    for i in range(2, len(prime_factors_dict)):
        # if i is not prime, keep iterating
        if not prime_factors_dict[i]:
            continue

        # Eliminate the factors of i as not primes
        for j in range(2*i, len(prime_factors_dict), i):
            prime_factors_dict[j] = False

    # Here we convert the prime factors from a dictionaty to a list
    prime_factors = []
    for i in range(2, len(prime_factors_dict)):
        if prime_factors_dict[i]:
            prime_factors.append(i)

    # Now we iterate through the input data and privde the solutions
    for n in input_data:
        """
            According to Oppermann's conjecture, we only need to check the numbers in range 
            [2n + 1 .. 2n + max_prime_gap] to find the next prime. For smaller numbers we will check the range of 
            [2n + 1 .. 4n - 1] where the next prime will be located according to the Bertrand's postulate.
        """
        max_prime_gap = ceil(sqrt(2 * n)) if n > 100 else 2 * n

        # First, we will check if the n is prime in the first place
        is_n_prime = True
        for j in prime_factors:
            if n != j and n % j == 0:
                is_n_prime = False
                break

        # Then, for each candidate we find the first one which is prime and report it as a result
        for i in range(1, max_prime_gap + 1):
            is_prime = True
            c = (2 * n) + i # Candidate value

            # Check that the candidate cannot be evenly divided by each relevant prime factor
            for j in prime_factors:

                if j > max_prime_gap: # This prime factor and larger ones are not relevant
                    break

                # Actually check if the candidate is evenly divisible
                if c != j and c % j == 0:
                    is_prime = False
                    break

            # Report first candidate that is prime
            if is_prime:
                print("{}{}".format((2 * n) + i, " ({} is not prime)".format(n) if not is_n_prime else ""))
                break
