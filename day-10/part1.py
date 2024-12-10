import os
import sys
from collections import deque, defaultdict
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from parser import Parser

def count_nines(grid, start_i, start_j):
    stack = [(start_i, start_j, -1)]
    visited = set()
    visited_nines = set()
    nine_count = 0
    
    while stack:
        i, j, prev_height = stack.pop()
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i, j) in visited:
            continue
        
        current_height = grid[i][j]
        if current_height != prev_height + 1:
            continue
        if current_height == 9 and (i, j) not in visited_nines:
            visited_nines.add((i, j))
            nine_count += 1
            continue
        
        visited.add((i, j))
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for di, dj in directions:
            stack.append((i + di, j + dj, current_height))
    
    return nine_count

if __name__ == "__main__":
    trailhead_map = Parser(file_path='input.txt').parse_lines(list, flatten=True)
    trailhead_map = [[int(value) for value in row] for row in trailhead_map]
    
    total_nine_count = 0
    for i in range(len(trailhead_map)):
        for j in range(len(trailhead_map[0])):
            if trailhead_map[i][j] == 0:
                total_nine_count += count_nines(trailhead_map, i, j)    
    print("Nines Count:", total_nine_count)
