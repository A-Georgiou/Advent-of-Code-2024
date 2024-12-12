import os
import sys
from collections import defaultdict
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from parser import Parser
from collections import defaultdict

def simulate_blink(stone_map):
    for stone, count in stone_map.copy().items():
        if stone == 0:
            stone_map[1] += count
            stone_map[0] -= count
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            new_len = int(len(stone_str) / 2)
            stone_1 = int(stone_str[:new_len])
            stone_2 = int(stone_str[new_len:])
            stone_map[stone_1] += count
            stone_map[stone_2] += count
            stone_map[stone] -= count
        else:
            stone_map[stone * 2024] += count
            stone_map[stone] -= count

if __name__ == "__main__":
    stones = Parser(file_path='input.txt').parse_lines(int, flatten=True)
    stone_map = defaultdict(int)
    for stone in stones:
        stone_map[int(stone)] += 1
    for i in range(75):
        blink(stone_map)
    print("Total stones:", sum(stone_map.values()))