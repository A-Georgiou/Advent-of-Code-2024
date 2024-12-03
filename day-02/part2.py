import os
import sys

# Combine utils path with curr path.
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from parser import Parser

# Parse input file into rows of int's.
parsed_input = Parser(file_path='input.txt').parse_lines(int)

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

# Exhaustive search for a safe row, checking removal of each element in row.
def exhaustive_row_safe_check(row):
    if is_minor_increase(row) or is_minor_decrease(row):
        return True

    for i in range(len(row)):
        modified_row = row[:i] + row[i + 1:]
        if is_minor_increase(modified_row) or is_minor_decrease(modified_row):
            return True
    return False

safe_count = 0

for row in parsed_input:
    if exhaustive_row_safe_check(row):
        safe_count += 1

print("Safe Count:",safe_count)