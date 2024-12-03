import re
import os
import sys

# Combine utils path with curr path.
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from parser import Parser

# Parse input file into rows of strings
parsed_input = Parser(file_path='input.txt').parse_whole_input(str)

# Pattern to match mul() / do() / don't() functions
pattern = re.compile(r"(?P<mul>mul\((\d{1,3}),(\d{1,3})\))|(?P<do>do\(\))|(?P<dont>don't\(\))")
# Use finditer to find patterns and index them.
matched_values = pattern.finditer(parsed_input)

active, mult_sum = True, 0
for match in matched_values:
    if match.group("mul") and active:
        mult_sum += int(match.group(2)) * int(match.group(3))
    if match.group("do"):
        active = True
    if match.group("dont"):
        active = False

print('Summed Values', mult_sum)