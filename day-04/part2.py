import os
import sys

# Combine utils path with curr path.
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from parser import Parser

# Parse input file into rows of strings
parsed_input = Parser(file_path='input.txt').parse_whole_input(str).splitlines()

# Check from each center if it is a MAS cross
def is_cross(i, j):
    center = parsed_input[i][j]
    if center != "A":
        return False
    
    top_left = parsed_input[i-1][j-1]
    top_right = parsed_input[i-1][j+1]
    bottom_left = parsed_input[i+1][j-1]
    bottom_right = parsed_input[i+1][j+1]
    return (
        (top_left == "M" and bottom_right == "S" and top_right == "S" and bottom_left == "M") or
        (top_left == "S" and bottom_right == "M" and top_right == "M" and bottom_left == "S") or
        (top_left == "M" and bottom_right == "S" and top_right == "M" and bottom_left == "S") or
        (top_left == "S" and bottom_right == "M" and top_right == "S" and bottom_left == "M")
    )

xmas_count = sum(
    is_cross(i, j)
    for i in range(1, len(parsed_input) - 1)
    for j in range(1, len(parsed_input[i]) - 1)
)

print('X-MAS count:', xmas_count)