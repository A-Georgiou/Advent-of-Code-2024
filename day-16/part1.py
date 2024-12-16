import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from parser import Parser
from collections import deque

def find_start(board):
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == 'S':
                return (i, j)

def print_board(board):
    for row in board:
        print(''.join(row))

def bfs(board, start):
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    start_dir = 0
    seen = {}
    queue = deque([(start, start_dir, 0)])
    min_seen = float('inf')
    while queue:
        (y, x), direction, points = queue.popleft()
        if board[y][x] == '#':
            continue
        if (y, x, direction) in seen:
            if seen[(y, x, direction)] <= points:
                continue
        seen[(y, x, direction)] = points
        if board[y][x] == 'E':
            min_seen = min(min_seen, points)
        new_y, new_x = y + directions[direction][0], x + directions[direction][1]
        queue.append(((new_y, new_x), direction, points + 1))
        queue.append(((y, x), (direction + 1) % 4, points + 1000))
        queue.append(((y, x), (direction - 1) % 4, points + 1000))
    return min_seen

if __name__ == "__main__":
    board = Parser(file_path='input.txt').parse_lines(list, flatten=True)
    start = find_start(board)
    print(start)
    print_board(board)
    print(bfs(board, start))