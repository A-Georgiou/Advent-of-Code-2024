import os
import sys
from collections import deque, defaultdict
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from parser import Parser

def find_gap_length(disk_map, start_idx):
    next_idx = start_idx
    while next_idx < len(disk_map) and disk_map[next_idx] is None:
        next_idx += 1
    return next_idx - start_idx

def create_disk_map(input_str):
    disk_map, current_id, is_file = deque([]), 0, True
    for number in input_str:
        number = int(number)
        if is_file:
            disk_map.extend([current_id] * number)
            current_id += 1
        else:
            disk_map.extend([None] * number)
        is_file = not is_file
    return disk_map

def left_push_blocks(input_str):
    for file_id in range(max(x for x in disk_map if x is not None), -1, -1):
        file_length = disk_map.count(file_id)
        gap_idx = disk_map.index(None)
        file_idx = disk_map.index(file_id)
        
        while gap_idx < file_idx:
            gap_len = find_gap_length(disk_map, gap_idx)
            
            if gap_len < file_length:
                gap_idx = disk_map.index(None, gap_idx + gap_len)
            else:
                while file_id in disk_map:
                    disk_map[disk_map.index(file_id)] = None
                    
                for n in range(file_length):
                    disk_map[gap_idx + n] = file_id
                break
    
    return disk_map

def check_sum(disk_map):
    checksum = sum(id * idx for idx, id in enumerate(disk_map) if id is not None)
    return checksum

if __name__ == "__main__":
    input_lines = list(Parser(file_path='input.txt').parse_whole_input(str).strip())
    disk_map = create_disk_map(input_lines)
    left_pushed_disk = left_push_blocks(disk_map)
    check_sum = check_sum(left_pushed_disk)
    print("Check Sum:", check_sum)