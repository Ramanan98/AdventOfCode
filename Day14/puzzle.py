# https://adventofcode.com/2024/day/14

import os
import matplotlib.pyplot as plt
from collections import defaultdict

def read_input():
    robots = {}
    with open('input.txt', 'r') as f:
        data = f.readlines()
    f.close()
    for index, line in enumerate(data):
        line = line.strip()
        p_part, v_part = line.split()
        p = tuple(map(int, p_part[2:].split(',')))
        v = tuple(map(int, v_part[2:].split(',')))
        robots[index] = [p, v]
    return robots

def calculate_position(pos_x, pos_y, vel_x, vel_y, rows, cols, multiplier):
    final_x = (pos_x + (vel_x * multiplier) % cols) % cols
    final_y = (pos_y + (vel_y * multiplier) % rows) % rows
    return final_x, final_y

# Plots the position of the robots in a graph and saves the file
def plot_grid(coordinates_set, num):
    if not os.path.exists('plots'):
        os.makedirs('plots')
    for x, y in coordinates_set:
        plt.plot(x, 0 - y, 'go')
    plt.savefig(f'plots/coordinates_plot_{num}.png')
    plt.close()

# Checks if more than {lim} points appear in a single line
def check_line(coordinates_set, lim):
    hashmap = defaultdict(int)
    for x, y in coordinates_set:
        hashmap[y] += 1
    for key, value in hashmap.items():
        if value >= lim:
            return True, key
    return False, -1

def get_safety_factor(robots, rows, cols):
    n = len(robots)
    multiplier = 100
    quadrant_counts = [0, 0, 0, 0]
    safety_factor = 1
    middle_row = rows // 2
    middle_col = cols // 2
    for i in range(n):
        final_x, final_y = calculate_position(robots[i][0][0], robots[i][0][1], robots[i][1][0], robots[i][1][1], rows, cols, multiplier)
        if final_x == middle_col or final_y == middle_row:
            pass
        if final_x < middle_col and final_y < middle_row:
            quadrant_counts[0] += 1
        elif final_x > middle_col and final_y < middle_row:
            quadrant_counts[1] += 1
        elif final_x < middle_col and final_y > middle_row:
            quadrant_counts[2] += 1
        elif final_x > middle_col and final_y > middle_row:
            quadrant_counts[3] += 1
    for count in quadrant_counts:
        safety_factor *= count
    return safety_factor

def save_plots(robots, rows, cols):
    coordinates_set = set()
    mul = 1
    n = len(robots)
    while mul <= rows * cols:
        for i in range(n):
            final_x, final_y = calculate_position(robots[i][0][0], robots[i][0][1], robots[i][1][0], robots[i][1][1], rows, cols, mul)
            coordinates_set.add((final_x, final_y))
        check, row = check_line(coordinates_set, 25)
        if check:
            print(f'Line forming after {mul} seconds!')
            plot_grid(coordinates_set, mul)
        mul += 1
        coordinates_set.clear()

def main():
    robots = read_input()
    rows = 103
    cols = 101
    print(get_safety_factor(robots, rows, cols)) # Part 1
    # Save all plots where at least 25 robots appear in a single line
    # Check which one forms a christmas tree
    save_plots(robots, rows, cols) # Part 2

if __name__ == "__main__":
    main()