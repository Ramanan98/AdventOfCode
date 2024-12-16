# https://adventofcode.com/2024/day/16

import heapq
from collections import defaultdict

def read_grid():
    grid = []
    with open('input.txt','r') as f:
        lines = f.readlines()
        for line in lines:
            grid.append(line.strip())
    f.close()
    return grid

def get_start_end(grid):
    start = -1, -1
    end = -1, -1
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'S':
                start = i, j
            elif grid[i][j] == 'E':
                end = i, j
    return start, end

def dijkstra(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = {'north': (-1, 0), 'south': (1, 0), 'west': (0, -1), 'east': (0, 1)}
    priority_queue = []
    heapq.heappush(priority_queue, (0, start[0], start[1], 'east', [(start[0], start[1], 'east')]))

    visited_costs = defaultdict(lambda: float('inf'))
    all_paths = defaultdict(list)

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols and grid[r][c] != '#'

    lowest_cost = float('inf')
    best_paths = []

    while priority_queue:
        cost, r, c, facing, path = heapq.heappop(priority_queue)
        if cost > lowest_cost:
            continue
        # Update lowest cost and best paths
        if (r, c) == end:
            if cost < lowest_cost:
                lowest_cost = cost
                best_paths = [path]  # Reset best paths
            elif cost == lowest_cost:
                best_paths.append(path)
            continue
        # Skip visiting a higher cost path
        if cost > visited_costs[(r, c, facing)]:
            continue
        visited_costs[(r, c, facing)] = cost
        all_paths[(r, c, facing)].append(path)
        for direction, (dr, dc) in directions.items():
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc):
                rotation_cost = 1000 if direction != facing else 0
                new_cost = cost + rotation_cost + 1
                heapq.heappush(priority_queue, (new_cost, nr, nc, direction, path + [(nr, nc, direction)]))
    return lowest_cost, best_paths

def main():
    grid = read_grid()
    start, end = get_start_end(grid)
    lowest_cost, all_best_paths = dijkstra(grid, start, end)
    seats = set()
    print(lowest_cost) # Part 1
    for path in all_best_paths:
        for item in path:
            seats.add((item[0], item[1]))
    print(len(seats)) # Part 2

if __name__ == "__main__":
    main()