# https://adventofcode.com/2024/day/12

def read_grid():
    grid = []
    with open('input.txt','r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            grid.append(line)
    f.close()
    return grid

def island_path(grid, i, j, visited, key):
    if visited is None:
        visited = set()
    if (i, j) in visited:
        return visited
    visited.add((i, j))
    area = 1
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nr, nc = i + dr, j + dc
        if (0 <= nr < rows) and (0 <= nc <cols):
            if grid[nr][nc] == key:
                if (nr, nc) not in visited:
                    sub_visit, sub_area, sub_peri = island_path(grid, nr, nc, visited, key)
                    visited |= sub_visit
                    area += sub_area
                    perimeter += sub_peri
            else:
                perimeter += 1
        else:
            perimeter += 1
    return visited, area, perimeter

def get_locations_dict(grid):
    locations_dict = {}
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] not in locations_dict:
                locations_dict[grid[i][j]] = set()
                locations_dict[grid[i][j]].add((i, j))
            else:
                locations_dict[grid[i][j]].add((i, j))
    return locations_dict

def count_sides(path):
    sides = 0
    for (x, y) in path:
        # Outer corners
        sides += (x - 1, y) not in path and (x, y + 1) not in path
        sides += (x, y + 1) not in path and (x + 1, y) not in path
        sides += (x + 1, y) not in path and (x, y - 1) not in path
        sides += (x, y - 1) not in path and (x - 1, y) not in path
        # Inner corners
        sides += (x - 1, y) in path and (x, y + 1) in path and (x - 1, y + 1) not in path
        sides += (x, y + 1) in path and (x + 1, y) in path and (x + 1, y + 1) not in path
        sides += (x + 1, y) in path and (x, y - 1) in path and (x + 1, y - 1) not in path
        sides += (x, y - 1) in path and (x - 1, y) in path and (x - 1, y - 1) not in path
    return sides

def main():    
    grid = read_grid()
    locations_dict = get_locations_dict(grid)
    result = 0
    discounted_result = 0

    for key, _ in locations_dict.items():
        while True:
            if not locations_dict[key]:
                break
            start_x, start_y = locations_dict[key].pop()
            visited = set()
            visited, area, perimeter = island_path(grid, start_x, start_y, visited, key)
            sides = count_sides(visited)
            result += (area * perimeter)
            discounted_result += (area * sides)
            locations_dict[key].difference_update(visited)

    print(result) # Part 1
    print(discounted_result) # Part 2

if __name__ == "__main__":
    main()