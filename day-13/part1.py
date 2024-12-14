import os
import sys
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
            [int(button_a[0][2:]),  int(button_a[1][2:])],
            [int(button_b[0][2:]),  int(button_b[1][2:])],
            [int(prize[0][2:]),     int(prize[1][2:])]])
        i += 4
    return output

def min_jump_cost(button_a, button_b, prize):
    a_cost = 3
    b_cost = 1
    curr_x, curr_y = 0, 0
    curr_price = 0
    min_price = float('inf')
    while curr_x <= prize[0] and curr_y <= prize[1]:
        diff_x = prize[0] - curr_x
        diff_y = prize[1] - curr_y
        if (diff_x % button_a[0] == 0 and diff_y % button_a[1] == 0 and 
            diff_x // button_a[0] == diff_y // button_a[1]):  
            min_price = min(min_price, curr_price + (a_cost * (diff_x // button_a[0])))
        curr_x += button_b[0]
        curr_y += button_b[1]
        curr_price += b_cost
    if min_price == float('inf'):
        return 0
    return min_price

if __name__ == "__main__":
    claw_buttons = Parser(file_path='input.txt').parse_lines(str, delimiter=': ')
    processed_input = process_input(claw_buttons)
    cum_sum = 0
    for i in range(len(processed_input)):
        cum_sum += min_jump_cost(*processed_input[i])
    print("Cumulative sum: ", cum_sum)

    