# https://adventofcode.com/2024/day/15

from collections import deque

directions = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}

def parse_input():
    grid = []
    with open('input.txt', 'r') as f:
        content = f.read()
    f.close()
    map = content.split('\n\n')[0]
    moves = content.split('\n\n')[1].replace('\n', '').strip()
    map = map.split('\n')
    for line in map:
        line = line.strip()
        grid.append(line)
    return grid, moves

def get_box_coordinates(grid):
    coordinates = []
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'O':
                coordinates.append((i, j))
    return coordinates

def move_box(cur_x, cur_y, dir, box_pos, grid):
    dr, dc = directions[dir]
    nr, nc = cur_x + dr, cur_y + dc
    if grid[nr][nc] == '#':
        return box_pos
    if (nr, nc) in box_pos:
        box_pos = move_box(nr, nc, dir, box_pos, grid)
    if grid[nr][nc] != '#' and (nr, nc) not in box_pos:
        index = box_pos.index((cur_x, cur_y))
        box_pos[index] = (nr, nc)
    return box_pos
    
def move_robot(robot_pos_x, robot_pos_y, dir, box_pos, grid):
    dr, dc = directions[dir]
    nr, nc = robot_pos_x + dr, robot_pos_y + dc
    if (grid[nr][nc] == '#'):
        return robot_pos_x, robot_pos_y, box_pos
    if (nr, nc) in box_pos:
        box_pos = move_box(nr, nc, dir, box_pos, grid)
        if (nr, nc) in box_pos:
            return robot_pos_x, robot_pos_y, box_pos
        else:
            return nr, nc, box_pos
    return nr, nc, box_pos

def get_robot_pos(grid):
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '@':
                return (i, j)
    return -1, -1

def solve_part_2(grid, moves):
    rows = len(grid)
    cols = len(grid[0])
    grid = [[grid[r][c] for c in range(cols)] for r in range(rows)]
    big_grid = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if grid[i][j]=='#':
                row.append('#')
                row.append('#')
            if grid[i][j]=='O':
                row.append('[')
                row.append(']')
            if grid[i][j]=='.':
                row.append('.')
                row.append('.')
            if grid[i][j]=='@':
                row.append('@')
                row.append('.')
        big_grid.append(row)
    grid = big_grid
    cols = len(grid[0])
    start_x, start_y = get_robot_pos(grid)
    i, j = start_x, start_y
    for move in moves:
        dr,dc = directions[move]
        nr,nc = i+dr,j+dc
        if grid[nr][nc]=='#':
            continue
        elif grid[nr][nc]=='.':
            i,j = nr,nc
        elif grid[nr][nc] in ['[', ']', 'O']:
            box_queue = deque([(i,j)])
            seen = set()
            ok = True
            while box_queue:
                nr,nc = box_queue.popleft()
                if (nr,nc) in seen:
                    continue
                seen.add((nr,nc))
                rrr,ccc = nr+dr, nc+dc
                if grid[rrr][ccc]=='#':
                    ok = False
                    break
                elif grid[rrr][ccc]=='[':
                    box_queue.append((rrr,ccc))
                    box_queue.append((rrr,ccc+1))
                elif grid[rrr][ccc]==']':
                    box_queue.append((rrr,ccc))
                    box_queue.append((rrr,ccc-1))
            if not ok:
                continue
            while len(seen) > 0:
                for nr,nc in sorted(seen):
                    rrr,ccc = nr+dr,nc+dc
                    if (rrr,ccc) not in seen:
                        grid[rrr][ccc] = grid[nr][nc]
                        grid[nr][nc] = '.'
                        seen.remove((nr,nc))
            i = i + dr
            j = j + dc
    gps_sum = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '[':
                gps_sum += 100*i+j
    return gps_sum

def main():
    grid, moves = parse_input()
    box_pos = get_box_coordinates(grid)
    cur_robot_x, cur_robot_y = get_robot_pos(grid)
    for i in range(len(moves)):
        try:
            cur_robot_x, cur_robot_y, box_pos = move_robot(cur_robot_x, cur_robot_y, moves[i], box_pos, grid)
        except TypeError:
            print(f'Error occured for {cur_robot_x}, {cur_robot_y}, {i+1}th move, {box_pos}')
    gps_sum = 0
    for (x, y) in box_pos:
        gps_sum += 100 * x + y
    print(gps_sum) # Part 1
    print(solve_part_2(grid, moves)) # Part 2

if __name__ == "__main__":
    main()