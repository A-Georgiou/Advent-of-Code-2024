import re
import os
import sys

# Combine utils path with curr path.
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from parser import Parser

# Parse input file into rows of strings
parsed_input = Parser(file_path='input.txt').parse_whole_input(str)
parsed_input = parsed_input.splitlines()

# I only check for right-up-diagonal, right, right-down-diagonal, down directions to avoid duplicate checks.
directions = [(1, 0), (0, 1), (1, 1), (-1, 1)]
target_words = {"XMAS", "SAMX"}

def get_xmas_count(i, j):
    count = 0
    for direction in directions:
            word = ""
            for step in range(4): 
                x = i + step * direction[0]
                y = j + step * direction[1]
                if x < 0 or y < 0 or x >= len(parsed_input) or y >= len(parsed_input[i]):
                    break

                word += parsed_input[x][y]

            if word in target_words:
                count += 1
    return count

xmas_count = sum(
        get_xmas_count(i,j)
        for i in range(len(parsed_input))
        for j in range(len(parsed_input[i]))
        )

print('XMAS count:', xmas_count)