import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from parser import Parser
from collections import defaultdict

def simulate_100_seconds(pos, vel, board_width, board_height):
    x = (pos[0] + (100 * vel[0])) % board_width
    y = (pos[1] + (100 * vel[1])) % board_height
    return (x,y)

def process_input(pos_vels):
    output = []
    for pos, vel in pos_vels:
        pos, vel = pos.split(','), vel.split(',')
        output.append([(int(pos[0][2:]), int(pos[1])), (int(vel[0][2:]), int(vel[1]))])
    return output

def print_board(board):
    for row in board:
        print(''.join(row))

def get_quadrant(x, y, board_width, board_height):
    if x == board_width // 2 or y == board_height // 2:
        return 0
        
    if x < board_width // 2:
        return 1 if y < board_height // 2 else 3
    else:
        return 2 if y < board_height // 2 else 4

def calculate_safety_factor(positions, board_width, board_height):
    quadrant_counts = defaultdict(int)
    
    for x, y in positions:
        quadrant = get_quadrant(x, y, board_width, board_height)
        if quadrant != 0:
            quadrant_counts[quadrant] += 1
    
    result = 1
    for quadrant in range(1, 5):
        result *= quadrant_counts[quadrant]
    
    return result

if __name__ == "__main__":
    BOARD_WIDTH = 101
    BOARD_HEIGHT = 103
    input_test = Parser(file_path='input.txt').parse_lines(str)
    processed_input = process_input(input_test)
    output = []
    for pos, vel in processed_input:
        x, y = simulate_100_seconds(pos, vel, BOARD_WIDTH, BOARD_HEIGHT)
        output.append((x, y))
    print('Safety Factor:', calculate_safety_factor(output, BOARD_WIDTH, BOARD_HEIGHT))