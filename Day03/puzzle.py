# https://adventofcode.com/2024/day/3

import re

def get_mul_instructions(input_string):
    mul_instructions = re.findall('mul\(\d{1,3},\d{1,3}\)', input_string)
    return mul_instructions

def calculate_result(mul_instructions):
    result = 0
    for instruction in mul_instructions:
        operands = instruction.split(',')
        result = result+ int(operands[0][4:]) * int(operands[1][:-1])
    return result

def calculate_do_instructions_result(input_string):
    all_instructions = input_string.split('do()')
    result = 0
    for instruction in all_instructions:
        dont_instruction = instruction.split("don't()")
        do_instruction = get_mul_instructions(dont_instruction[0])
        result = result + calculate_result(do_instruction)
    return result

def main():
    with open('input.txt', 'r') as f:
        input_string = f.read()
    f.close()
    # Part 1
    mul_instructions = get_mul_instructions(input_string)
    result_1 = calculate_result(mul_instructions)
    print(result_1)

    # Part 2
    result_2 = calculate_do_instructions_result(input_string)
    print(result_2)

if __name__ == "__main__":
    main()