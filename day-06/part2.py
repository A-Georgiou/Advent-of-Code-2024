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

def traverse_board(board, start_row, start_col, track_direction=False, stop_on_loop=False):
    visited = set()
    initial_dir = 0  
    stack = [(start_row, start_col, initial_dir)]

    while stack:
        pos_row, pos_col, curr_dir = stack.pop()
        visited_key = (pos_row, pos_col, curr_dir) if track_direction else (pos_row, pos_col)

        if visited_key in visited and stop_on_loop:
            return visited, True

        visited.add(visited_key)

        while not stack:
            d_row, d_col = DIRECTIONS[curr_dir]
            new_row, new_col = pos_row + d_row, pos_col + d_col

            if not in_bounds(board, new_row, new_col):
                break

            if board[new_row][new_col] == '#':
                curr_dir = (curr_dir + 1) % 4
            else:
                stack.append((new_row, new_col, curr_dir))
    return visited, False

def print_board(board):
    for row in board:
        print(''.join(row))

def guard_traverse():
    board = [list(row) for row in Parser(file_path='input.txt').parse_lines(str, flatten=True)]
    guard_row, guard_col = get_guard_position(board)
    visited_list, _ = traverse_board(board, guard_row, guard_col, track_direction=False, stop_on_loop=False)

    loop_count = 0
    for (row, col) in visited_list:
        if board[row][col] in ('^', '#'):
            continue
        board[row][col] = '#'
        loop_count += traverse_board(board, guard_row, guard_col, track_direction=True, stop_on_loop=True)[1]
        board[row][col] = '.'
    print('Loop Count:', loop_count)

if __name__ == "__main__":
    guard_traverse()
