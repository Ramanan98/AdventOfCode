# https://adventofcode.com/2024/day/18

import heapq

def read_input(n):
    c = set()
    with open('input.txt', 'r') as f:
        for i, line in enumerate(f):
            if i >= n:
                break
            coordinates = line.strip().split(',')
            x, y = int(coordinates[0]), int(coordinates[1])
            c.add((x, y))
    f.close()
    return c

def read_all():
    c = []
    with open('input.txt', 'r') as f:
        for line in f:
            coordinates = line.strip().split(',')
            x, y = int(coordinates[0]), int(coordinates[1])
            c.append((x, y))
    f.close()
    return c

def create_grid(coordinates, rows, cols):
    grid = [['.' for _ in range(cols)] for _ in range(rows)]
    for x, y in coordinates:
        grid[y][x] = '#'
    return grid

def create_empty_grid(rows, cols):
    grid = [['.' for _ in range(cols)] for _ in range(rows)]
    return grid

def dijkstra(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cost, (x, y) = heapq.heappop(pq)
        if (x, y) == end:
            return cost
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dr, dc in directions:
            nr, nc = x + dr, y + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '.':
                heapq.heappush(pq, (cost + 1, (nr, nc)))
    return -1

def find_first_byte(grid, all_bytes):
    rows = len(grid)
    cols = len(grid[0])
    start = 0, 0
    end = rows - 1, cols - 1
    counter = 1
    for byte in all_bytes:
        x, y = byte[0], byte[1]
        grid[y][x] = '#'
        cost = dijkstra(grid, start, end)
        if cost == -1:
            return f"{byte[0]},{byte[1]}"
        counter += 1

def main():
    n = 1024
    rows = 71
    cols = 71
    start = 0, 0
    end = rows - 1, cols - 1
    coordinates = read_input(n)
    all_bytes = read_all()
    grid = create_grid(coordinates, rows, cols)

    lowest_cost = dijkstra(grid, start, end)
    print(lowest_cost) # Part 1

    empty_grid = create_empty_grid(rows, cols)
    print(find_first_byte(empty_grid, all_bytes)) # Part 2

if __name__ == "__main__":
    main()