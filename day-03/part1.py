import re
import os
import sys

# Combine utils path with curr path.
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from parser import Parser

# Parse input file into rows of strings
parsed_input = Parser(file_path='input.txt').parse_whole_input(str)
pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

matched = pattern.findall(parsed_input)
mult_sum = sum(int(x) * int(y) for x, y in matched)

print('Summed Values:',mult_sum)