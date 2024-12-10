import os
import sys
from collections import defaultdict
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from parser import Parser

def count_paths(grid, i, j, dp):
    if dp[i][j] != -1:
        return dp[i][j]
    
    current_height = grid[i][j]
    if current_height == 9:
        dp[i][j] = 1
        return 1
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    total_paths = 0
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
            if grid[ni][nj] == current_height + 1:
                total_paths += count_paths(grid, ni, nj, dp)
    
    dp[i][j] = total_paths
    return dp[i][j]

if __name__ == "__main__":
    trailhead_map = Parser(file_path='input.txt').parse_lines(list, flatten=True)
    trailhead_map = [[int(value) for value in row] for row in trailhead_map]
    dp = [[-1] * len(trailhead_map[0]) for _ in range(len(trailhead_map))]

    rating_sum = 0
    for i in range(len(trailhead_map)):
        for j in range(len(trailhead_map[0])):
            if trailhead_map[i][j] == 0:
                rating_sum += count_paths(trailhead_map, i, j, dp)
    print("Distinct Trailhead count:", rating_sum)