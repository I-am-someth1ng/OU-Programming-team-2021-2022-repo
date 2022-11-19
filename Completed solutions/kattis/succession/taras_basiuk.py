"""
    Solution to the https://open.kattis.com/problems/succession

    Approach to the solution is recursively traversing the ansestry tree bottom-up for every candidate.
    Our up traversal will terminate on either the founder (1.0 blood fraction) or the child with no parents recorder (0.0 fraction).
    Now going back down, we will record the founder's blood fraction for all the intermidiate parents all the way down to the candidate.
    We will also use memoisation to reduce the number of ansestry look-ups.
"""
__author__ = "Taras Basiuk"

# Read in N, M, ....
N, M = tuple(map(int, input().strip().split()))
founder = input().strip() # ... and the founder name

parents = {} # Container for storing all the parents of each child
for i in range(N): # For every child
    # Read in the names of the child and two parents
    child, parent1, parent2 = input().strip().split()
    parents[child] = {parent1, parent2} # Record the parents of the child

# Container for the fractions of founder blood each child posesses    
blood = {founder: 1.0} # Only founder's fractions is knowns now

# Recursive method for finding fractions of founder's blood for any child
def find_ansestry(c):

    # If the fraction is already known and recorded, just return it
    if c in blood:
        return blood[c]

    # Otherwise, assume the child is unrelated to the founder
    c_blood = 0.0

    # If the child has their parents recorded (otherwise fraction of founder's blood is 0.0)
    if c in parents:
        for p in parents[c]: # For every parent
            c_blood += (find_ansestry(p) / 2) # Add half their fraction of the founder blood as our own

    blood[c] = c_blood # Record our fraction, so we don't have to look for it again
    return c_blood # return the result

# Containers for the name and the founder's blood fraction of the closest candidate
closest = None
best_blood = 0.0

# For every candidate
for i in range(M):
    candidate = input().strip() # Read in the candidate name
    candidate_blood = find_ansestry(candidate) # find out their ansestry

    # If the candidate has the largest fraction of founder's blood so far, record their name and fraction
    if candidate_blood > best_blood:
        best_blood = candidate_blood
        closest = candidate

print(closest) # Output the closest candidate
