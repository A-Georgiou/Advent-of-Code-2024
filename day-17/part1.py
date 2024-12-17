import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from parser import Parser
from collections import deque

def run_program(program, reg_a=0, reg_b=0, reg_c=0):
    registers = {'A': reg_a, 'B': reg_b, 'C': reg_c}
    ip = 0
    output = []
    
    def get_combo_value(operand):
        if operand <= 3:
            return operand
        elif operand == 4:
            return registers['A']
        elif operand == 5:
            return registers['B']
        elif operand == 6:
            return registers['C']
        return 0
    
    while ip < len(program) - 1:
        opcode = program[ip]
        operand = program[ip + 1]
        
        if opcode == 0: 
            registers['A'] //= 2 ** get_combo_value(operand)
        elif opcode == 1:
            registers['B'] ^= operand
        elif opcode == 2: 
            registers['B'] = get_combo_value(operand) % 8
        elif opcode == 3: 
            if registers['A'] != 0:
                ip = operand
                continue
        elif opcode == 4: 
            registers['B'] ^= registers['C']
        elif opcode == 5:
            output.append(str(get_combo_value(operand) % 8))
        elif opcode == 6:
            registers['B'] = registers['A'] // 2 ** get_combo_value(operand)
        elif opcode == 7:
            registers['C'] = registers['A'] // 2 ** get_combo_value(operand)
        
        ip += 2
    
    return ','.join(output)


if __name__ == "__main__":
    registers, opcodes = Parser(file_path='input.txt').parse_sections(str)
    registers = [int(x.split(': ')[1]) for x in registers.splitlines()]
    opcodes = [int(x) for x in opcodes.split(': ')[1].split(',')]
    print(run_program(opcodes, *registers))