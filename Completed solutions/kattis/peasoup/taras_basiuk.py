"""
    Solution to the https://open.kattis.com/problems/peasoup
"""

__author__ = "Taras Basiuk"

n = int(input().strip()) # Read in the number of restaurants
found = False # Found good enough restaraunt?

for i in range(n): # For every restaraunt
    if found: # Unless found good enough already
        break

    k = int(input().strip()) # Read in the number of menu items
    name = input().strip() # Read in the restaurant name

    looking_for = set(["pea soup", "pancakes"])

    for j in range(k): # For every menu item

        # Remove it from looking_for (if we were looking for it)
        looking_for.discard(input().strip())

        # If not looking for anything else anymore
        if not looking_for:
            print(name) # Print out the found restaurant name
            found = True
            break

if not found: # If never found a good enough restaurant
    print("Anywhere is fine I guess")
