"""
    Solution for the - https://open.kattis.com/problems/flipfive

    Approach to the solution is a breadth-first-search exploration of reachable board states.
"""

__author__ = "Taras Basiuk"

# Starting board state. Zero bit represents a white cell, one bit represents black cell.
# First three bits are for the three cells in the top row, next three for the middle row, ...
board = 0b000000000

# Array of possible moves, where 1 bit represents a flipped cell, 0 - an unflipped one
possible_moves = [
    0b110100000, # Top Left
    0b111010000, # Top Center
    0b011001000, # Top Right
    0b100110100, # Middle Left
    0b010111010, # Middle Center
    0b001011001, # Middle Right
    0b000100110, # Bottom Left
    0b000010111, # Bottom Center
    0b000001011  # Bottom Right
]

# Used to record all the boards encountered so far, and how many moves it took us to encounter them
encountered_boards = {board: 0}

# We will use a double-ended queue to record the possible boards exploration process
from collections import deque
exploration = deque()

exploration.append((board, 0)) # Exploration starts with the start board reached in 0 moves

while exploration: # While exploration deque is not empty

    # Take a current board from the left edge of the deque
    current_board, moves = exploration.popleft()

    # Try applying every possible move to the current board.
    # If a new board state encountered, record it and add it for exploration at the right side of the deque.
    # Adding to the right of deque and taking from the left constitutes a breadth-first-search.
    for m in possible_moves:
        new_board = current_board ^ m

        if new_board not in encountered_boards:
            encountered_boards[new_board] = moves + 1
            exploration.append((new_board, moves + 1))

# Now read the input and answer how many moves it'll take to get to the requested board state
N = int(input().strip())
for _ in range(N):

    # Concatenate three lines of input together, replace '.' with 0 and '*' with 1, and convert it into an int
    print(encountered_boards[int(("0b" + input() + input() + input()).replace('.', '0').replace('*', '1'), 2)])
