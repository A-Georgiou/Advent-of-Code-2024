import os
import sys
from collections import deque, defaultdict
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from parser import Parser

def generate_node_map(board):
    node_map = defaultdict(list)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != '.':
                node_map[board[i][j]].append((i, j))
    return node_map

def compute_new_positions(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    new_x, new_y = x1 - dx, y1 - dy
    new_positions = set()
    if new_x >= 0 and new_x < len(board) and new_y >= 0 and new_y < len(board[0]):
        new_positions.add((new_x, new_y))
    return new_positions

def generate_anti_nodes(positions):
    new_positions = set()
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            new_positions.update(compute_new_positions(*positions[i], *positions[j]))
            new_positions.update(compute_new_positions(*positions[j], *positions[i]))
    return new_positions

def print_board(board):
    for row in board:
        print(''.join(row))

if __name__ == "__main__":
    board = [list(x) for x in Parser(file_path='input.txt').parse_lines(str, flatten=True)]
    node_map = generate_node_map(board)
    positions = set()
    for key, value in node_map.items():
        positions = positions.union(generate_anti_nodes(value))
    print('Unique anti-node positions:',len(positions))