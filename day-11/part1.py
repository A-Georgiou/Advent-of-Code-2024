import os
import sys
from collections import defaultdict
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from parser import Parser

def simulate_blink(stones):
    output = []
    for stone in stones:
        if stone == '0':
            output.append('1')
        elif len(stone) % 2 == 0:
            output.append(str(int(stone[:len(stone)//2])))
            output.append(str(int(stone[len(stone)//2:])))
        else:
            output.append(str(int(stone)*2024))
    return output

if __name__ == "__main__":
    stones = Parser(file_path='input.txt').parse_lines(str, flatten=True)
    for i in range(25):
        stones = simulate_blink(stones)
    print("Total stones:", len(stones))