import os
import sys

# Combine utils path with curr path.
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from parser import Parser

# Parse input file into [int, int] pairs.
parsed_input = Parser(file_path='input.txt').parse_input([int, int])

left_list, right_list = zip(*parsed_input)
left_list = sorted(left_list)
right_list = sorted(right_list)

dist = sum(abs(l - r) for l, r in zip(left_list, right_list))
print("Distance:", dist)