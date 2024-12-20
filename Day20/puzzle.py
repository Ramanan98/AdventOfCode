# https://adventofcode.com/2024/day/20

import heapq

def read_grid():
    grid = []
    with open('input.txt', 'r') as f:
        for line in f:
            grid.append(list(line.strip()))
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

def get_start_end(grid):
    start, end = None, None
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'E':
                end = (i, j)
    return start, end

def get_walls(grid):
    walls = set()
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '#':
                walls.add((i, j))
    return walls

def main():
    grid = read_grid()
    start, end = get_start_end(grid)
    walls = get_walls(grid)
    grid[start[0]][start[1]] = '.'
    grid[end[0]][end[1]] = '.'
    shortest_path_cost = dijkstra(grid, start, end)
    paths = 0

    for wall in walls:
        grid[wall[0]][wall[1]] = '.'
        cost = dijkstra(grid, start, end)
        if shortest_path_cost - cost >= 100:
            paths +=1
        grid[wall[0]][wall[1]] = '#'

    print(paths) # Part 1

if __name__ == "__main__":
    main()