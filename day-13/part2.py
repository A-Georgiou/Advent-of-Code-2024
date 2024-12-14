import os
import sys
from math import gcd
from typing import Optional, Tuple
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from parser import Parser

def process_input(buttons):
    i = 0
    output = []
    while i < len(buttons):
        button_a = buttons[i][1].split(', ')
        button_b = buttons[i+1][1].split(', ')
        prize = buttons[i+2][1].split(', ')
        output.append([
            [int(button_a[0][2:]), int(button_a[1][2:])],
            [int(button_b[0][2:]), int(button_b[1][2:])],
            [int(prize[0][2:]) + 10000000000000, int(prize[1][2:]) + 10000000000000]])
        i += 4
    return output

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def find_solution(button_a, button_b, prize):
    a_x, a_y = button_a
    b_x, b_y = button_b
    prize_x, prize_y = prize
    
    det = a_x * b_y - a_y * b_x
    if (det == 0
        or (prize_x * b_y - prize_y * b_x) % det != 0
        or (a_x * prize_y - a_y * prize_x) % det != 0): 
        return 0

    A = (prize_x * b_y - prize_y * b_x) // det
    B = (a_x * prize_y - a_y * prize_x) // det
    
    return 0 if A < 0 or B < 0 else 3 * A + B

if __name__ == "__main__":
    claw_buttons = Parser(file_path='input.txt').parse_lines(str, delimiter=': ')
    processed_input = process_input(claw_buttons)
    cum_sum = 0
    for i, machine in enumerate(processed_input):
        cum_sum += find_solution(*machine)
    print("Cumulative sum:", cum_sum)