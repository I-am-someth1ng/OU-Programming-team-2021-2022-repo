"""
    Solution to the - https://open.kattis.com/problems/quickbrownfox
"""
__author__ = "Taras Basiuk"

N = int(input().strip()) # Read in the number of test cases

for _ in range(N): # For every test case
    S = input().strip().lower() # Read in the input string, strip and lowercase it

    counts = [0] * 26 # Prepare the array for the counts of every letter in the alphabet

    for c in S: # For every character in the input string
        ascii_code = ord(c) # Convert the character into ASCII code

        # For the codes corresponding to lowercase alphabet letters
        if ascii_code >= 97 and ascii_code <= 122:
            counts[ascii_code - 97] += 1 # Increase the letter count in our array

    missing = [] # List for the missing letters

    for i in range(26): # For every letter in the English alphabet
        if counts[i] == 0: # If its count is zero
            missing.append(chr(i + 97)) # Add it to the list of missing letters

    # If 'missing' list is empty output "pangram", otherwise output the missing letters
    print("pangram" if not missing else f"missing {''.join(missing)}")
