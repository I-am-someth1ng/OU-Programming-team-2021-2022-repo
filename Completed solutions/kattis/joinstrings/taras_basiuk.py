"""
    Solution for the - https://open.kattis.com/problems/joinstrings

    Approach to the solution it two-pronged:
        1. Processing the joins going forward count how large (in number of segments) every sa will get.
        2. Then processing the joins going backward calculate where each sb will have to go in the result
            given their sizes, sa sizes and sa positions (last sa will have to be the first in the result). 
"""

__author__ = "Taras Basiuk"

N = int(input().strip()) # Read in the number of segments

# Edgecase check. If there's only single string fragment, output it as a result as soon as you red it in.
if N == 1:
    print(input().strip())
    import sys
    sys.exit(0)

strings = {} # Container for string segments
for i in range(N): # Read in the segments
    strings[i + 1] = input().strip()

joins = [] # List of perfomed joins [(sa, sb), ...]
seg_counts = {k: 1 for k in range(1, N + 1)} # Container for resulting sa segment counts

for i in range(N - 1): # For every join
    sa, sb = map(int, input().strip().split()) # Read in sa and sb
    joins.append((sa, sb)) # Record the join
    seg_counts[sa] += seg_counts[sb] # Increment the resulting sa segment count by the sb segment count

ind_to_seg = [None] * N # Mapping pointing from result segment index to the input segment index 
ind_to_seg[0] = joins[-1][0] # Last sa will be placed in the first position of the result

seg_to_ind = {k: None for k in range(1, N)} # Mapping from input segment to where it goes in the result
seg_to_ind[joins[-1][0]] = 0 # First position of the result is ocupied by the last sa

while joins: # Process all joins starting with the last and going backwards
    sa, sb = joins.pop()

    # To figure out where sb goes in the resuls, take sa position, add sa length and substract sb length
    ind_to_seg[seg_to_ind[sa] + seg_counts[sa] - seg_counts[sb]] = sb 

    # Record the same as above but in the inverse map
    seg_to_ind[sb] = seg_to_ind[sa] + seg_counts[sa] - seg_counts[sb]

    # sa segment count is now reduced by sb segment count, effectively un-joining them
    seg_counts[sa] -= seg_counts[sb]

# Finally print out the result using the ind_to_seg mapping
for i in ind_to_seg:
    print(strings[i], end='')
print("")
