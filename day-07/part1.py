import os
import sys
from collections import deque
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from parser import Parser

def bfs(result, numbers):
    queue = deque([(numbers[0], 0)])

    while queue:
        current, idx = queue.popleft()

        if idx == len(numbers) - 1:
            if current == result:
                return True
            continue

        next_num = numbers[idx + 1]
        queue.append((current + next_num, idx + 1))
        queue.append((current * next_num, idx + 1))
    return False

def find_result():
    math_operations = Parser(file_path='input.txt').parse_lines(str, delimiter=': ')
    math_operations = [[int(x), [int(k) for k in y.split()]] for x, y in math_operations]
    return sum(result if bfs(result, numbers) else 0 for result, numbers in math_operations)

if __name__ == "__main__":
    print("Combined Result:", find_result())
