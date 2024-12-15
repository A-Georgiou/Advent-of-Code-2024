import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from parser import Parser

def simulate_t_seconds(pos, vel, board_width, board_height, seconds):
    x = (pos[0] + (seconds * vel[0])) % board_width
    y = (pos[1] + (seconds * vel[1])) % board_height
    return (x,y)

def process_input(pos_vels):
    output = []
    for pos, vel in pos_vels:
        pos = pos.split(',')
        vel = vel.split(',')
        output.append([(int(pos[0][2:]), int(pos[1])), (int(vel[0][2:]), int(vel[1]))])
    return output

def print_board(positions, board_width, board_height):
    board = [[' ' for _ in range(board_width)] for _ in range(board_height)]
    for x, y in positions:
        board[y][x] = '#'
    for row in board:
        print(''.join(row))

def find_no_overlap(positions):
    return len(set(positions)) == len(positions)

if __name__ == "__main__":
    BOARD_WIDTH = 101
    BOARD_HEIGHT = 103
    input_test = Parser(file_path='input.txt').parse_lines(str)
    processed_input = process_input(input_test)
    for seconds in range(1000000):
        output = []
        for pos, vel in processed_input:
            x, y = simulate_t_seconds(pos, vel, BOARD_WIDTH, BOARD_HEIGHT, seconds)
            output.append((x, y))
        if find_no_overlap(output):
            print('Vertical Line found at time:', seconds, ' Merry Christmas!')
            print_board(output, BOARD_WIDTH, BOARD_HEIGHT)
            break