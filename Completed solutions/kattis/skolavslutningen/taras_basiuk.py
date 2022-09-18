"""
    Solution to the - https://open.kattis.com/problems/skolavslutningen
"""
__author__ = "Taras Basiuk"

# Read in the number of lines, columns and classes
lines, columns, classes = tuple(map(int, input().strip().split()))

# Read in the lineup as a list of strings
lineup = []
for _ in range(lines):
    lineup.append(input().strip())

class_colors = {} # Mapping from a class to the color used
color_count = 0 # Number of colors already used

for c in range(columns): # For every column

    # (1) First we check if anyone in the column already has color assigned
    color = None
    for l in range(lines):
        if lineup[l][c] in class_colors:
            color = class_colors[lineup[l][c]]
            break

    # (2) If no assigned color was found pick a new color
    if color == None:
        color_count += 1
        color = color_count

    # Paint everyone in the column in the color from (1) or (2)
    for l in range(lines):
        class_colors[lineup[l][c]] = color

print(color_count) # Return the result
