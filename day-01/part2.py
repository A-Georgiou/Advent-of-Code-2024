import os
import sys
from collections import Counter

# Combine utils path with curr path.
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from parser import Parser

# Parse input file into [int, int] pairs.
parsed_input = Parser(file_path='input.txt').parse_input([int, int])

left_list, right_list = zip(*parsed_input)
right_list = Counter(right_list)

similarity_score = sum(l * right_list.get(l, 0) for l in left_list)
print("Similarity Score:", similarity_score)