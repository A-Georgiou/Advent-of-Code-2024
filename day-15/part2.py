import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from parser import Parser
from enum import Enum
import time

class Direction(Enum):
    UP = '^'
    DOWN = 'v'
    LEFT = '<'
    RIGHT = '>'

def double_width_board(board):
    doubled = []
    for row in board:
        new_row = []
        for cell in row:
            if cell == '#':
                new_row.extend(['#', '#'])
            elif cell == 'O':
                new_row.extend(['[', ']'])
            elif cell == '.':
                new_row.extend(['.', '.'])
            elif cell == '@':
                new_row.extend(['@', '.'])
        doubled.append(new_row)
    return doubled


def find_robot(board):
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == '@':
                return (i, j)

def print_board(board):
    print("\x1b[H", end="")
    for row in board:
        temp_row = [cell if cell != '.' else ' ' for cell in row]
        print(''.join(temp_row))

def check_valid_move(board, y, x, direction):
    dir_y, dir_x = {Direction.UP: (-1, 0), Direction.DOWN: (1, 0),
                    Direction.LEFT: (0, -1), Direction.RIGHT: (0, 1)
                    }[direction]
    
    new_y, new_x = y + dir_y, x + dir_x
    
    if (new_y < 0 or new_y >= len(board) or 
        new_x < 0 or new_x >= len(board[0]) or 
        board[new_y][new_x] == '#'):
        return False, (y, x), []
    
    if board[new_y][new_x] == '.':
        return True, (new_y, new_x), []
    
    boxes_to_move_result = []
    if board[new_y][new_x] in ['[', ']']:
        seen_box = set()
        boxes_to_move = [(new_y, new_x, board[new_y][new_x])]
        if board[new_y][new_x] == '[':
            boxes_to_move.append((new_y, new_x + 1, board[new_y][new_x + 1]))
        else:
            boxes_to_move.append((new_y, new_x - 1, board[new_y][new_x - 1]))
        
        while boxes_to_move:
            curr_y, curr_x, box = boxes_to_move.pop()
            next_y, next_x = curr_y + dir_y, curr_x + dir_x
            
            if (curr_y < 0 or curr_y >= len(board) or 
                curr_x < 0 or curr_x >= len(board[0]) or 
                board[curr_y][curr_x] == '#'):
                return False, (y, x), []
            
            if board[curr_y][curr_x] == '.' or (curr_y, curr_x) in seen_box:
                continue

            if board[next_y][next_x] == ']' and (next_y, next_x) not in seen_box:
                boxes_to_move.append((next_y, next_x, ']'))
                boxes_to_move.append((next_y, next_x - 1, '['))
            elif board[next_y][next_x] == '[' and (next_y, next_x) not in seen_box:
                boxes_to_move.append((next_y, next_x, '['))
                boxes_to_move.append((next_y, next_x + 1, ']'))
            else:
                boxes_to_move.append((next_y, next_x, board[next_y][next_x]))
            boxes_to_move_result.append((curr_y, curr_x, box))
            seen_box.add((curr_y, curr_x))
    return True, (new_y, new_x), boxes_to_move_result

def shift_board(board, robot_y, robot_x, new_y, new_x, direction, boxes_to_move):
    dir_y, dir_x = {
        Direction.UP: (-1, 0),
        Direction.DOWN: (1, 0),
        Direction.LEFT: (0, -1),
        Direction.RIGHT: (0, 1)
    }[direction]
    
    new_board = [row[:] for row in board]
    new_board[robot_y][robot_x] = '.'

    for box_y, box_x, box in boxes_to_move:
        if box == '[':
            new_board[box_y][box_x] = '.'
            new_board[box_y][box_x + 1] = '.'

    for box_y, box_x, box in boxes_to_move:
        if box == '[':
            new_box_y = box_y + dir_y
            new_box_x = box_x + dir_x
            new_board[new_box_y][new_box_x] = '['
            new_board[new_box_y][new_box_x + 1] = ']'
    
    new_board[new_y][new_x] = '@'
    
    return new_board

def simulate_moves(board, directions, robot_y, robot_x):
    current_board = [row[:] for row in board]
    current_y, current_x = robot_y, robot_x
    
    for direction in directions:
        valid_move, (new_y, new_x), boxes_to_move = check_valid_move(current_board, current_y, current_x, direction)
        if valid_move:
            current_board = shift_board(current_board, current_y, current_x, new_y, new_x, direction, boxes_to_move)
            current_y, current_x = new_y, new_x
            time.sleep(0.05)
            print_board(current_board)
    return current_board

def map_moves_to_directions(move_set):
    output = []
    for move in move_set:
        if move == '^':
            output.append(Direction.UP)
        elif move == 'v':
            output.append(Direction.DOWN)
        elif move == '<':
            output.append(Direction.LEFT)
        elif move == '>':
            output.append(Direction.RIGHT)
    return output

def calculate_gps(board):
    cum_sum = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '[': 
                cum_sum += (100 * i) + j
    return cum_sum

if __name__ == "__main__":
    board, move_set = [x.splitlines() for x in Parser(file_path='input.txt').parse_sections(str)]
    board = [list(row) for row in board]
    
    board = double_width_board(board)
    print("Initial board:")
    print_board(board)
    
    move_set = [b for b in move_set for b in b]
    robot_y, robot_x = find_robot(board)
    directions = map_moves_to_directions(move_set)
    
    final_board = simulate_moves(board, directions, robot_y, robot_x)
    print("\nFinal board:")
    print_board(final_board)
    
    print('GPS Sum:', calculate_gps(final_board))