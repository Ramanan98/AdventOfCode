# https://adventofcode.com/2024/day/8

def read_grid():
    grid = []
    with open('input.txt','r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            grid.append(line)
    f.close()
    return grid

def find_in_grid(grid, x):
    for line in grid:
        if str(x) in line:
            return str(x)

def count_occurrences_in_grid(grid, x):
    occurrences = 0
    for line in grid:
        if x in line:
            occurrences += line.count(x)
    return occurrences

def find(grid):
    antennas = set()
    num = set()
    cap = set()
    small = set()
    for i in range(48,58):
        num.add(find_in_grid(grid, chr(i)))
    for i in range(65,91):
        cap.add(find_in_grid(grid, chr(i)))
    for i in range(97,123):
        small.add(find_in_grid(grid, chr(i)))
    antennas = num | cap | small
    return antennas

def place_antinode(grid, antenna, locations, antinode_locations):
    rows = len(grid)
    cols = len(grid[0])
    n = len(locations)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            else:
                dist_x = locations[j][0] - locations[i][0]
                dist_y = locations[j][1] - locations[i][1]
                antinode_location_x = locations[j][0] + dist_x
                antinode_location_y = locations[j][1] + dist_y
                # print(f'Distance for {locations[j]} and {locations[i]} is ({antinode_location_x},{antinode_location_y})')
                if antinode_location_x >= 0 and antinode_location_x < cols and antinode_location_y >=0 and antinode_location_y < rows:
                    antinode_locations.add((antinode_location_x, antinode_location_y))
    return antinode_locations

# Part 2
def place_harmonic_antinode(grid, antenna, locations, antinode_locations):
    rows = len(grid)
    cols = len(grid[0])
    n = len(locations)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            else:
                dist_x = locations[j][0] - locations[i][0]
                dist_y = locations[j][1] - locations[i][1]
                antinode_location_x = locations[j][0] + dist_x
                antinode_location_y = locations[j][1] + dist_y
                if antinode_location_x >= 0 and antinode_location_x < cols and antinode_location_y >=0 and antinode_location_y < rows:
                    if grid[antinode_location_x][antinode_location_y] == '.':
                        antinode_locations.add((antinode_location_x, antinode_location_y))
                mul = 2
                while (antinode_location_x >= 0 and antinode_location_x < cols and antinode_location_y >=0 and antinode_location_y < rows):
                    harmonic_dist_x = mul * dist_x
                    harmonic_dist_y = mul * dist_y
                    antinode_location_x = locations[j][0] + harmonic_dist_x
                    antinode_location_y = locations[j][1] + harmonic_dist_y
                    if antinode_location_x >= 0 and antinode_location_x < cols and antinode_location_y >=0 and antinode_location_y < rows:
                        if grid[antinode_location_x][antinode_location_y] == '.':
                            antinode_locations.add((antinode_location_x, antinode_location_y))
                    mul = mul + 1
    return antinode_locations

# Get the locations of the antennas in the grid. Key is the antenna, value is a list of locations.
def get_antenna_locations(grid, antennas):
    rows = len(grid)
    cols = len(grid[0])
    antenna_locations = {}
    for antenna in antennas:
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == antenna:
                    if antenna not in antenna_locations:
                        antenna_locations[antenna] = []
                    antenna_locations[antenna].append((i, j))
    return antenna_locations

def main():
    grid = read_grid()
    antennas = find(grid)
    antenna_locations = get_antenna_locations(grid, antennas)

    antinode_locations = set()

    for antenna, locations in antenna_locations.items():
        antinode_locations = antinode_locations | place_antinode(grid, antenna, locations, antinode_locations)
    print(len(antinode_locations))

    # Part 2
    antinode_locations.clear()
    for antenna, locations in antenna_locations.items():
        antinode_locations = antinode_locations | place_harmonic_antinode(grid, antenna, locations, antinode_locations)

    occurrences = 0
    for antenna, locations in antenna_locations.items():
        occurrences += count_occurrences_in_grid(grid, antenna)

    print(len(antinode_locations)+occurrences)

if __name__ == '__main__':
    main()