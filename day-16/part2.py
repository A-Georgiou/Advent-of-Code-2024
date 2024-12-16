import os
import sys
from heapq import heappush, heappop
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from parser import Parser
from enum import Enum
from collections import defaultdict

class Direction(Enum):
    EAST = 1
    SOUTH = 2
    WEST = 3
    NORTH = 4

def find_start(board):
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == 'S':
                return (i, j)

def print_board(board, path_set=None):
    if path_set is None:
        for row in board:
            print(''.join(row))
        return
    
    marked_board = [list(row) for row in board]
    for y, x in path_set:
        if marked_board[y][x] not in ['S', 'E']:
            marked_board[y][x] = 'O'
    
    for row in marked_board:
        print(''.join(row))

def djikstra(board, start):
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    start_dir = 0
    
    pq = [(0, start[0], start[1], start_dir, {(start[0], start[1])})]
    seen = defaultdict(lambda: float('inf'))
    optimal_paths = []
    min_score = float('inf')
    
    while pq:
        score, y, x, direction, path = heappop(pq)
        
        if score > seen[(y, x, direction)]:
            continue
            
        if board[y][x] == 'E':
            if score < min_score:
                min_score = score
                optimal_paths = [path]
            elif score == min_score:
                optimal_paths.append(path)
            continue
            
        new_y, new_x = y + directions[direction][0], x + directions[direction][1]
        if 0 <= new_y < len(board) and 0 <= new_x < len(board[0]) and board[new_y][new_x] != '#':
            new_score = score + 1
            new_path = path | {(new_y, new_x)}
            if new_score <= seen[(new_y, new_x, direction)]:
                seen[(new_y, new_x, direction)] = new_score
                heappush(pq, (new_score, new_y, new_x, direction, new_path))
        
        for new_dir in [(direction - 1) % 4, (direction + 1) % 4]:
            new_score = score + 1000
            if new_score <= seen[(y, x, new_dir)]:
                seen[(y, x, new_dir)] = new_score
                heappush(pq, (new_score, y, x, new_dir, path))
    
    all_tiles = set()
    for path in optimal_paths:
        all_tiles.update(path)
    
    return min_score, all_tiles

if __name__ == "__main__":
    board = Parser(file_path='input.txt').parse_lines(list, flatten=True)
    start = find_start(board)
    
    min_score, optimal_tiles = djikstra(board, start)
    
    print(f"Part 1: Minimum score = {min_score}")
    print(f"Part 2: Number of tiles in optimal paths = {len(optimal_tiles)}")
    print("\nBoard with optimal paths marked (O):")
    print_board(board, optimal_tiles)