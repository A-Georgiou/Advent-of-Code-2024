import os
import sys
from collections import deque, defaultdict
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from parser import Parser

def create_disk_map(input_lines):
    output = []
    id = 0
    for count, free in input_lines:
        for i in range(count):
            output.append(id)
        id += 1
        for i in range(free):
            output.append('.')
    return output

def two_pointer_swap(input_lines):
    i = 0
    j = len(input_lines)-1
    while i < j:
        if input_lines[i] != '.':
            i += 1
        elif input_lines[j] == '.':
            j -= 1
        else:
            input_lines[i], input_lines[j] = input_lines[j], input_lines[i]
            i += 1
            j -= 1
    return input_lines

def compute_check_sum(input_lines):
    check_sum = 0
    for i in range(len(input_lines)):
        if input_lines[i] != '.':
            check_sum += (input_lines[i] * i)
    return check_sum

if __name__ == "__main__":
    input_lines = list(Parser(file_path='input.txt').parse_whole_input(str).strip())
    output = []
    for i in range(1, len(input_lines)+1, 2):
        if i < len(input_lines):
            output.append((int(input_lines[i-1]), int(input_lines[i])))
        else:
            output.append((int(input_lines[i-1]), 0))
    disk_map = create_disk_map(output)
    result = two_pointer_swap(disk_map)
    check_sum = compute_check_sum(result)
    print("Check Sum:", check_sum)

