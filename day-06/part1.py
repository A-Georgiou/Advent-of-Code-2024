import os
import sys
from collections import defaultdict

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from parser import Parser

# Directions: Up, Right, Down, Left
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def get_guard_position(board):
    for row_idx, row in enumerate(board):
        for col_idx, cell in enumerate(row):
            if cell == '^':
                return row_idx, col_idx
    return None, None

def in_bounds(board, row, col):
    return 0 <= row < len(board) and 0 <= col < len(board[row])

def board_dfs(board, start_row, start_col):
    visited = set()
    stack = [(start_row, start_col)]
    curr_dir = 0

    while stack:
        pos_row, pos_col = stack.pop()

        if board[pos_row][pos_col] == '#':
            curr_dir = (curr_dir + 1) % 4
            continue

        visited.add((pos_row, pos_col))

        while not stack:
            new_dir = curr_dir % 4
            d_row, d_col = DIRECTIONS[new_dir]
            new_row, new_col = pos_row + d_row, pos_col + d_col

            if not in_bounds(board, new_row, new_col):
                return list(visited)

            if board[new_row][new_col] == '#':
                curr_dir = (curr_dir + 1) % 4
            else:
                stack.append((new_row, new_col))

    return list(visited)

def print_board(board):
    for row in board:
        print(''.join(row))

def guard_traverse():
    board = [list(row) for row in Parser(file_path='input.txt').parse_lines(str, flatten=True)]
    guard_row, guard_col = get_guard_position(board)
    visited_list = board_dfs(board, guard_row, guard_col)
    print("Unique Visited:",len(visited_list))

if __name__ == "__main__":
    guard_traverse()
