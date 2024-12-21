
# https://adventofcode.com/2024/day/21

key_locations = {
    '7': (0, 0),
    '8': (0, 1),
    '9': (0, 2),
    '4': (1, 0),
    '5': (1, 1),
    '6': (1, 2),
    '1': (2, 0),
    '2': (2, 1),
    '3': (2, 2),
    '0': (3, 1),
    'A': (3, 2),
    '^': (0, 1),
    'a': (0, 2),
    '<': (1, 0),
    'v': (1, 1),
    '>': (1, 2)
}

def read_input():
    codes = []
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            codes.append(line.strip())
    return codes

def manhattan_distance(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return abs(x2 - x1) + abs(y2 - y1)

def evaluate_paths(paths):
    min_cost = float('inf')
    min_length = min(len(sublist) for sublist in paths)
    if min_length == 0:
        return ""
    for list in paths:
        path_cost = 0
        for i in range(len(list) - 1):
            path_cost += manhattan_distance(key_locations[list[i]], key_locations[list[i + 1]])
        path_cost += manhattan_distance(key_locations[list[len(list) - 1]], key_locations['a'])
        if path_cost < min_cost:
            min_cost = path_cost
            shortest_path = list
    return shortest_path

def find_path(start, end, type):

    start = key_locations[start]
    end = key_locations[end]

    if type == 'num':
        grid = [
            ["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "3"],
            ["", "0", "A"]
        ]
        empty_space = (3, 0)
    elif type == 'dir':
        grid = [
            ["", "^", "a"],
            ["<", "v", ">"],
        ]
        empty_space = (0, 0)

    directions = {
        (1, 0): "v",
        (-1, 0): "^",
        (0, 1): ">",
        (0, -1): "<"
    }

    def bfs(start, end, empty_space):
        queue = [(start, [])]
        visited = set()
        paths = []
        while queue:
            current, path = queue.pop(0)
            if current == end:
                paths.append(path)
            if current in visited:
                continue
            visited.add(current)
            x, y = current
            moves = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            for move in moves:
                mx, my = move
                if 0 <= mx < len(grid) and 0 <= my < len(grid[0]) and grid[mx][my] and move != empty_space:
                    direction = directions[(mx - x, my - y)]
                    queue.append((move, path + [direction]))
        return paths
    
    return bfs(start, end, empty_space)

def find_paths(start, end, type):
    start = key_locations[start]
    end = key_locations[end]
    
    if type == 'num':
        grid = [
            ["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "3"],
            ["", "0", "A"]
        ]
        blocked = (3, 0)
    elif type == 'dir':
        grid = [
            ["", "^", "a"],
            ["<", "v", ">"],
        ]
        blocked = (0, 0)
    rows, cols = len(grid), len(grid[0])
    directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    shortest_paths = []
    shortest_length = float('inf')
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and (x, y) != blocked
    
    def backtrack(x, y, path, visited):
        nonlocal shortest_length
        if (x, y) == end:
            path_length = len(path)
            if path_length < shortest_length:
                shortest_length = path_length
                shortest_paths.clear()
            if path_length == shortest_length:
                shortest_paths.append(path[:])
            return
        
        visited.add((x, y))
        
        for dir_name, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and (nx, ny) not in visited:
                path.append(dir_name)
                backtrack(nx, ny, path, visited)
                path.pop()
        
        visited.remove((x, y))
    
    backtrack(start[0], start[1], [], set())
    return shortest_paths

def get_num_path(string):
    start = 'A'
    path = ''
    for char in string:
        try:
            to_add = find_paths(start, char, 'num')
            path += "".join(to_add)
        except TypeError:
            to_add_path = evaluate_paths(to_add)
            path += "".join(to_add_path)
        path += 'a'
        start = char
    return path

def get_dir_path(string):
    start = 'a'
    path = ''
    for char in string:
        try:
            to_add = find_paths(start, char, 'dir')
            path += "".join(to_add)
        except TypeError:
            to_add_path = evaluate_paths(to_add)
            path += "".join(to_add_path)
        path += 'a'
        start = char
    return path

def main():
    codes = read_input()
    result = 0
    for code in codes:
        path = get_num_path(code)
        for i in range(2):
            path = get_dir_path(path)
        path_size = len(path)
        result += int(code.replace('A', '')) * path_size
    print(result)

if __name__ == "__main__":
    main()