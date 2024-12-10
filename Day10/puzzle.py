# https://adventofcode.com/2024/day/10

def find_trailhead_scores(grid):
    rows, cols = len(grid), len(grid[0])
    trailheads = []
    peaks = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                trailheads.append((i, j))
            elif grid[i][j] == 9:
                peaks.append((i, j))
    
    def get_valid_neighbors(r, c, curr_height):
        # right, down, left, up directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
        neighbors = []
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            if (0 <= new_r < rows and 
                0 <= new_c < cols and 
                grid[new_r][new_c] == curr_height + 1):
                neighbors.append((new_r, new_c))
        return neighbors
    
    def count_paths(start_r, start_c):
        visited = set()
        reachable_peaks = set()
        
        def dfs(r, c):
            if (r, c) in visited:
                return        
            visited.add((r, c))
            curr_height = grid[r][c]
            if curr_height == 9:
                reachable_peaks.add((r, c))
                return
            for next_r, next_c in get_valid_neighbors(r, c, curr_height):
                dfs(next_r, next_c)
        
        dfs(start_r, start_c)
        return len(reachable_peaks)
    
    total_score = 0
    for r, c in trailheads:
        score = count_paths(r, c)
        total_score += score
    
    return total_score

def find_trailhead_ratings(grid):
    rows, cols = len(grid), len(grid[0])
    trailheads = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                trailheads.append((i, j))
    
    def get_valid_neighbors(r, c, curr_height):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            if (0 <= new_r < rows and 
                0 <= new_c < cols and 
                grid[new_r][new_c] == curr_height + 1):
                neighbors.append((new_r, new_c))
        return neighbors
    
    def count_distinct_trails(start_r, start_c):
        paths = set()
        
        def dfs(r, c, current_path):
            if grid[r][c] == 9:
                paths.add(tuple(current_path))
                return
            
            for next_r, next_c in get_valid_neighbors(r, c, grid[r][c]):
                if (next_r, next_c) not in current_path:
                    dfs(next_r, next_c, current_path + [(next_r, next_c)])
        
        dfs(start_r, start_c, [(start_r, start_c)])
        return len(paths)
    
    total_rating = 0
    for r, c in trailheads:
        rating = count_distinct_trails(r, c)
        total_rating += rating
    
    return total_rating

def main(): 
    grid = []
    with open('input.txt', 'r') as file:
        for line in file:
            row = [int(x) for x in line.strip()]
            grid.append(row)
    result = find_trailhead_scores(grid) # Part 1
    print(result)
    result2 = find_trailhead_ratings(grid) # Part 2
    print(result2)

if __name__ == "__main__":
    main()