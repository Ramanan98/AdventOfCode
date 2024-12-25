# https://adventofcode.com/2024/day/25

def parse_input():
    keys = []
    locks = []
    with open('input.txt', 'r') as f:
        content = f.read()
        grids = content.split('\n\n')
        for grid in grids:
            sub_grid = []
            rows = grid.split('\n')
            for row in rows:
                sub_grid.append(row)
            key = all(char == '.' for char in sub_grid[0])
            if key:
                keys.append(sub_grid)
            else:
                locks.append(sub_grid)
    return keys, locks

def count_hash(grid):
    num_columns = len(grid[0]) if grid else 0
    column_counts = [0] * num_columns
    for row in grid:
        for col_index, char in enumerate(row):
            if char == '#':
                column_counts[col_index] += 1
    tup =  tuple(column_counts)
    return tuple(x - 1 for x in tup)
def add_tuples(tup1, tup2):
    return tuple(a + b for a, b in zip(tup1, tup2))

def main():
    keys, locks = parse_input()
    keys_info = []
    locks_info = []
    row_count = 7
    for key in keys:
        keys_info.append(count_hash(key))
    for lock in locks:
        locks_info.append(count_hash(lock))
    result = 0
    for key_info in keys_info:
        for lock_info in locks_info:
            tup = add_tuples(key_info, lock_info)
            if all(x < row_count - 1 for x in tup):
                result += 1
    print(result)

if __name__ == "__main__":
    main()