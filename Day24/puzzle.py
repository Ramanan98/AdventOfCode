# https://adventofcode.com/2024/day/24

def read_input():
    instructions = []
    bits = {}
    with open('input.txt', 'r') as f:
        content = f.read().strip()
        bits_section, logic_section = content.split('\n\n')
        for line in bits_section.split('\n'):
            var, value = line.split(': ')
            bits[var] = int(value)
        for line in logic_section.split('\n'):
            parts = line.strip().split()
            if len(parts) == 5:
                input1, operation, input2, _, output = parts
                instructions.append((input1, operation, input2, output))   
    return bits, instructions

def get_z_wire_value(bits, instructions):
    operation_map = {
        "XOR": lambda x, y: x ^ y,
        "OR": lambda x, y: x | y,
        "AND": lambda x, y: x & y,
    }
    seen = set()
    while len(seen) < len(instructions):
        for inst in instructions:
            if inst in seen:
                continue
            if inst[0] in bits and inst[2] in bits:
                bits[inst[3]] = operation_map[inst[1]](bits[inst[0]], bits[inst[2]])
                seen.add(inst)
            else:
                continue
    z_keys = sorted([key for key in bits if key.startswith('z')])
    binary_number = 0
    for i, key in enumerate(z_keys):
        value = bits[key]
        binary_number += value << i
    return binary_number

def main():
    bits, instructions = read_input()
    print(get_z_wire_value(bits, instructions))

if __name__ == "__main__":
    main()