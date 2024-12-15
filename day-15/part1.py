import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from parser import Parser
from enum import Enum

class Direction(Enum):
    UP = '^'
    DOWN = 'v'
    LEFT = '<'
    RIGHT = '>'

def find_robot(board):
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == '@':
                return (i, j)

def print_board(board):
    for row in board:
        print(''.join(row))

def check_valid_move(board, y, x, direction):
    dir_y, dir_x = {
        Direction.UP: (-1, 0),
        Direction.DOWN: (1, 0),
        Direction.LEFT: (0, -1),
        Direction.RIGHT: (0, 1)
    }[direction]
    
    new_y, new_x = y + dir_y, x + dir_x
    
    if (new_y < 0 or new_y >= len(board) or 
        new_x < 0 or new_x >= len(board[0]) or 
        board[new_y][new_x] == '#'):
        return False, (y, x), []
    
    if board[new_y][new_x] == '.':
        return True, (new_y, new_x), []
    
    if board[new_y][new_x] == 'O':
        boxes_to_move = [(new_y, new_x)]
        curr_y, curr_x = new_y, new_x
        
        while True:
            next_y, next_x = curr_y + dir_y, curr_x + dir_x
            
            if (next_y < 0 or next_y >= len(board) or 
                next_x < 0 or next_x >= len(board[0]) or 
                board[next_y][next_x] == '#'):
                return False, (y, x), []
            
            if board[next_y][next_x] == '.':
                return True, (new_y, new_x), boxes_to_move
            
            if board[next_y][next_x] == 'O':
                boxes_to_move.append((next_y, next_x))
                curr_y, curr_x = next_y, next_x
                continue
            
            return False, (y, x), []
    
    return False, (y, x), []

def shift_board(board, robot_y, robot_x, new_y, new_x, direction, boxes_to_move):
    dir_y, dir_x = {
        Direction.UP: (-1, 0),
        Direction.DOWN: (1, 0),
        Direction.LEFT: (0, -1),
        Direction.RIGHT: (0, 1)
    }[direction]
    
    new_board = [row[:] for row in board]
    
    new_board[robot_y][robot_x] = '.'
    for box_y, box_x in boxes_to_move:
        new_board[box_y][box_x] = '.'
    
    for box_y, box_x in boxes_to_move:
        new_box_y = box_y + dir_y
        new_box_x = box_x + dir_x
        new_board[new_box_y][new_box_x] = 'O'
    
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
            if board[i][j] == 'O':
                cum_sum += (100 * i) + j

    return cum_sum

if __name__ == "__main__":
    board, move_set = [x.splitlines() for x in Parser(file_path='input.txt').parse_sections(str)]
    board = [list(row) for row in board]
    print("Initial board:")
    move_set = [b for b in move_set for b in b]
    
    robot_y, robot_x = find_robot(board)
    directions = map_moves_to_directions(move_set)
    
    final_board = simulate_moves(board, directions, robot_y, robot_x)

    print("\nFinal board:")
    print_board(final_board)
    
    print('GPS Sum:', calculate_gps(final_board))