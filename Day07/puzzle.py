# https://adventofcode.com/2024/day/7

from itertools import product

def read_input():
    with open('input.txt','r') as f:
        input_dict = {}
        lines = f.readlines()
        for line in lines:
            result = int(line.split(': ')[0])
            operands = list(map(int, line.split(': ')[1].split(' ')))
            input_dict[result] = operands
    f.close()
    return input_dict

def evaluate(expression, key):
    result = 0
    op = expression.split(' ')
    if int(op[0]) > key:
        return 0
    i = 3
    n = len(op)
    if n < 2:
        return op[0]
    first_operation = op[1]
    if first_operation == '+':
        result = result + int(op[0]) + int(op[2])
    elif first_operation == '*':
        result = result + (int(op[0]) * int(op[2]))
    else:
        result = int(op[0] + op[2])
    if result > key:
        return 0
    if n < 4:
        return result
    while(i < n - 1):
        operation = op[i]
        if operation == '+':
            result = result + int(op[i + 1])
        elif operation == '*':
            result = result * int(op[i + 1])
        else:
            result = int(str(result) + op[i + 1])
        if result > key:
            return 0
        i = i + 2
    return result

def evaluate_combinations(numbers, part, key):
    if len(numbers) < 2:
        return numbers[0]
    if part == 1:
        operators = list(product('+*', repeat=len(numbers)-1))
    elif part == 2:
        operators = list(product('+*|', repeat=len(numbers)-1))
    else:
        return 0
    result = []
    for ops in operators:
        expression = str(numbers[0])
        for num, op in zip(numbers[1:], ops):
            expression += f' {op} {num}'
        result.append((expression, evaluate(expression, key)))
    return result

def get_successful_evaluations(input_dict, part):
    possible_keys = set()
    answer = 0
    for key, value in input_dict.items():
        combos = evaluate_combinations(value, part, key)
        for expr, result in combos:
            if result == key:
                possible_keys.add(result)
    for key in possible_keys:
        answer = answer + key
    return answer

def main():
    input_dict = read_input()
    part_1_answer = get_successful_evaluations(input_dict, 1)
    print(part_1_answer) # Part 1
    part_2_answer = get_successful_evaluations(input_dict, 2)
    print(part_2_answer) # Part 2

if __name__ == "__main__":
    main()