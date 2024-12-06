# https://adventofcode.com/2024/day/6

def place_obstacle(grid, i, j):
    new_grid = grid[:]
    new_grid[i] = list(new_grid[i])
    new_grid[i][j] = '#'
    new_grid[i] = ''.join(new_grid[i])
    return new_grid

def remove_obstacle(grid, i, j):
    grid[i] = list(grid[i])
    grid[i][j] = '.'
    grid[i] = ''.join(grid[i])
    return grid

def rotate(facing):
    facing = (facing + 1) % 4
    return facing

def move(directions, facing, i, j):
    if directions[facing] == 'up':
        return i - 1, j
    elif directions[facing] == 'right':
        return i, j + 1
    elif directions[facing] == 'down':
        return i + 1, j
    elif directions[facing] == 'left':
        return i, j - 1

def read_grid():
    grid = []
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            grid.append(line)
    f.close()
    return grid

def find_inital_position(grid):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == '^':
                return i, j

def is_facing_obstacle(grid, i, j, directions, facing):
    rows = len(grid)
    cols = len(grid[0])
    if directions[facing] == 'up' and i - 1 >= 0:
        return grid[i - 1][j] == '#'
    elif directions[facing] == 'right' and j + 1 < cols:
        return grid[i][j + 1] == '#'
    elif directions[facing] == 'down' and i + 1 < rows:
        return grid[i + 1][j] == '#'
    elif directions[facing] == 'left' and j - 1 >= 0:
        return grid[i][j - 1] == '#'
    return False

def is_in_loop(grid, i, j, directions, facing):
    seen_states = set()
    rows, cols = len(grid), len(grid[0])
    while 0 <= i < rows and 0 <= j < cols:
        state = (i, j, facing)
        if state in seen_states:
            return True
        seen_states.add(state)
        if is_facing_obstacle(grid, i, j, directions, facing):
            facing = rotate(facing)
        i, j = move(directions, facing, i, j)
    return False

def get_visited_positions(grid, directions, facing):
    rows = len(grid)
    cols = len(grid[0])
    i, j = find_inital_position(grid)
    visited = set()
    while (i < cols and i >= 0 and j < rows and j >= 0):
        visited.add((i,j))
        if(is_facing_obstacle(grid, i, j, directions, facing)):
            facing = rotate(facing)
        i, j = move(directions, facing, i, j)
    return visited

def get_loop_obstacles(grid, directions):
    rows, cols = len(grid), len(grid[0])
    obstacles = set()
    start_x, start_y = find_inital_position(grid)
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '.' and (i, j) != (start_x, start_y):
                new_grid = place_obstacle(grid, i, j)
                if is_in_loop(new_grid, start_x, start_y, directions, 0):
                    obstacles.add((i, j))
    return obstacles

def main():
    directions = ['up', 'right', 'down', 'left']
    facing = 0
    grid = read_grid()
    visited = get_visited_positions(grid, directions, facing)
    print(len(visited))  # Part 1
    obstacles = get_loop_obstacles(grid, directions)  # Part 2
    print(len(obstacles))

if __name__ == "__main__":
    main()