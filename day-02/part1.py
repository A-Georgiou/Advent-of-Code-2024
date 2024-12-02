import os
import sys

# Combine utils path with curr path.
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from parser import Parser

# Parse input file into rows of int's.
parsed_input = Parser(file_path='input.txt').parse_input(int)

def is_minor_increase(row):
    for i in range(len(row) - 1):
        diff = row[i + 1] - row[i]
        if diff < 1 or diff > 3:
            return False
    return True

def is_minor_decrease(row):
    for i in range(len(row) - 1):
        diff = row[i] - row[i + 1]
        if diff < 1 or diff > 3:
            return False
    return True

safe_count = 0

for row in parsed_input:
    if check_minor_increase(row) or check_minor_decrease(row):
        safe_count += 1

print("Safe Count:",safe_count)