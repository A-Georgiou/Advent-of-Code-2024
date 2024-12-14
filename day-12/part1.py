import os
import sys
from collections import deque
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from parser import Parser

def calculate_shape(garden_plot, i, j):
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    area_count, perim_count  = 0, 0
    current_char = garden_plot[i][j]
    char_num = ord(garden_plot[i][j]) - ord('A')
    queue = deque([(i, j)])
    visited = set()
    while queue:
        y, x = queue.popleft()

        if (y, x) in visited:
            continue
        
        if y < 0 or y >= len(garden_plot) or x < 0 or x >= len(garden_plot[0]):
            perim_count += 1
            continue

        if garden_plot[y][x] != current_char:
            perim_count += 1
            continue
        
        garden_plot[y][x] = '.'
        visited.add((y, x))
        area_count += 1

        for di, dj in directions:
            ni, nj = y + di, x + dj
            queue.append((ni, nj))
    return (area_count * perim_count), garden_plot
            
if __name__ == "__main__":
    garden_plot = Parser(file_path='input.txt').parse_lines(list, flatten=True)
    count = 0
    for i in range(len(garden_plot)):
        for j in range(len(garden_plot[0])):
            if garden_plot[i][j] != '.':
                temp_count, garden_plot = calculate_shape(garden_plot, i, j)
                count += temp_count
    print("Result: ", count)