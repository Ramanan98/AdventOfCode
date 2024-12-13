# https://adventofcode.com/2024/day/13

def solve_equations(a1, b1, c1, a2, b2, c2):
    det = a1*b2 - a2*b1
    if det == 0:
        return -1, -1
    else:
        x = (c1*b2 - c2*b1) / det
        y = (a1*c2 - a2*c1) / det
        if x.is_integer() and y.is_integer():
            return int(x), int(y)
        else:
            return -1, -1

def parse_input_file():
    button_a = {'x': [], 'y': []}
    button_b = {'x': [], 'y': []}
    prize = {'x': [], 'y': []}
    
    with open('input.txt', 'r') as file:
        while True:
            button_a_line = file.readline().strip()
            if not button_a_line:
                break
            button_b_line = file.readline().strip()
            prize_line = file.readline().strip()
            file.readline()
            x_val = int(button_a_line.split('X+')[1].split(',')[0])
            y_val = int(button_a_line.split('Y+')[1])
            button_a['x'].append(x_val)
            button_a['y'].append(y_val)
            x_val = int(button_b_line.split('X+')[1].split(',')[0])
            y_val = int(button_b_line.split('Y+')[1])
            button_b['x'].append(x_val)
            button_b['y'].append(y_val)
            x_val = int(prize_line.split('X=')[1].split(',')[0])
            y_val = int(prize_line.split('Y=')[1])
            prize['x'].append(x_val)
            prize['y'].append(y_val)
    file.close()
    
    return button_a, button_b, prize

def get_tokens(button_a, button_b, prize):
    tokens = 0
    n = len(button_a['x'])
    for i in range(n):
        sol_a, sol_b = solve_equations(button_a['x'][i], button_b['x'][i], prize['x'][i], button_a['y'][i], button_b['y'][i], prize['y'][i])
        if (sol_a, sol_b) != (-1, -1):
            if sol_a > 100 or sol_b > 100:
                continue
            else:
                tokens += 3 * sol_a + sol_b
    return tokens

def get_corrected_tokens(button_a, button_b, prize):
    corrected_tokens = 0
    n = len(button_a['x'])
    for i in range(n):
        sol_a, sol_b = solve_equations(button_a['x'][i], button_b['x'][i], prize['x'][i] + 10000000000000, button_a['y'][i], button_b['y'][i], prize['y'][i] + 10000000000000)
        if (sol_a, sol_b) != (-1, -1):
            corrected_tokens += 3 * sol_a + sol_b
    return corrected_tokens

def main():
    button_a, button_b, prize = parse_input_file()
    print(get_tokens(button_a, button_b, prize)) # Part 1
    print(get_corrected_tokens(button_a, button_b, prize)) # Part 2

if __name__ == "__main__":
    main()