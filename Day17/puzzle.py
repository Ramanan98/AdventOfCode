# https://adventofcode.com/2024/day/17

def parse_input():
    with open('input.txt', 'r') as f:
        content = f.read()
    f.close()
    registers = content.split('\n')[0:3]
    program = content.split('\n')[4].strip()
    a = int(registers[0].split(':')[1].strip())
    b = int(registers[1].split(':')[1].strip())
    c = int(registers[2].split(':')[1].strip())
    instr = program.split(':')[1].split(',')
    instr = list(map(int, instr))
    return a, b, c, instr

def calculate(a, b, c, instructions):
    def get_value(operand):
        if operand in [0, 1, 2, 3]:
            return operand
        elif operand == 4:
            return a 
        elif operand == 5:
            return b
        elif operand == 6:
            return c
        return None
    
    output = []
    i = 0
    n = len(instructions)

    while True:
        instr = instructions[i]
        opcode = instructions[i+1]
        i += 2
        if instr == 0:
            operand = get_value(opcode)
            a = a // (2**operand)
        elif instr == 1:
            b = b ^ opcode
        elif instr == 2:
            operand = get_value(opcode)
            b = operand % 8
        elif instr == 3:
            if a != 0:
                i = opcode
        elif instr == 4:
            b = b ^ c
        elif instr == 5:
            output.append((get_value(opcode)) % 8)
        elif instr == 6:
            operand = get_value(opcode)
            b = a // (2**operand)
        elif instr == 7:
            operand = get_value(opcode)
            c = a // (2**operand)
        if i >=n:
            break
        if i == n - 2 and instr == 3 and a == 0:
            break
    return output

def find_a(instr):
    target_list = list(instr)
    n = len(target_list)
    a = 1
    match_level = 1
    candidates = []
    for _ in range(8):
        out = calculate(a, 0, 0, instr)
        if list(out[-match_level:]) == target_list[-match_level:]:
            candidates.append(a)
        a += 1
    match_level += 1
    while(match_level <= n):
        candidates_copy = list(candidates)
        candidates.clear()
        for candidate in candidates_copy:
            a = 8 * candidate
            for _ in range(8):
                out = calculate(a, 0, 0, instr)
                if out[-match_level:] == target_list[-match_level:]:
                    if match_level == n:
                        return a
                    candidates.append(a)
                a += 1
        match_level += 1

def main():
    a, b, c, instr = parse_input()
    output = calculate(a, b, c, instr)
    output = ",".join(map(str, output))
    print(output)
    print(find_a(instr))

if __name__ == "__main__":
    main()