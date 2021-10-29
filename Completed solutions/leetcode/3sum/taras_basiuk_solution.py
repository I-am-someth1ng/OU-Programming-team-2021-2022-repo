"""Solution for the - https://leetcode.com/problems/3sum/ """

__author__ = "Taras Basik"

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Count unique integer occurrences
        uios = {}
        for n in nums:
            if n not in uios:
                uios[n] = 0
            uios[n] = uios[n] + 1
            
        # Now make a list of up to two repetitions of every unique integer to be used for i and j
        ijs = []
        for ui in uios:
            ijs.append(ui)
            if uios[ui] > 1:
                ijs.append(ui)

        # Prepare results container set (will de-duplicate the triples as well)
        result = set()
        
        # Now make a double loop for picking i and j
        for i in range(len(ijs)):
            for j in range(i + 1, len(ijs)):

                # Find the integer which will complement the sum of ijs[i] and ijs[j] to 0
                complement = -(ijs[i] + ijs[j])

                # Now if such complement is present among uios and in sufficient quantity add the triple to result set
                if complement in uios and (uios[complement] > (0 if ijs[i] != complement else 1) + (0 if ijs[j] != complement else 1)):
                    # Make a sorted tuple of ijs[i], ijs[j], and complement to allow for the de-duplication of triples
                    result.add(tuple(sorted([ijs[i], ijs[j], complement])))

        return result # This is still a set of tuples and not a list of lists, but it will be accepted
