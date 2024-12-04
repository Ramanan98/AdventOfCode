# https://adventofcode.com/2024/day/4

def get_grid():
    grid = []
    with open('input.txt','r') as f:
        input = f.readlines()
        for line in input:
            grid.append(line)
    f.close()
    return grid

def count_xmas(grid):
    count = 0
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            try:
                # Horizontal
                string = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i][j+3]
                if string == 'XMAS' or string == 'SAMX':
                    count += 1
            except IndexError:
                continue
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            try:
                # Vertical
                string = grid[i][j] + grid[i+1][j] + grid[i+2][j] + grid[i+3][j]
                if string == 'XMAS' or string == 'SAMX':
                    count += 1
            except IndexError:
                continue
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            try:
                # Diagonally right
                string = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] + grid[i+3][j+3]
                if string == 'XMAS' or string == 'SAMX':
                    count += 1
            except IndexError:
                continue
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            try:
                # Diagonally left
                string = grid[i][j] + grid[i+1][j-1] + grid[i+2][j-2] + grid[i+3][j-3]
                if string == 'XMAS' or string == 'SAMX':
                    count += 1
            except IndexError:
                continue
    return count

def count_x_mas(grid):
    count = 0
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            try:
                string1 = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
                string2 = grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2]
                if (string1 == 'MAS' or string1 == 'SAM') and (string2 == 'MAS' or string2 == 'SAM'):
                    count += 1
            except IndexError:
                continue
    return count
                

def main():
    grid = get_grid()
    count = count_xmas(grid)
    print(count)
    mas_count = count_x_mas(grid)
    print(mas_count)

if __name__ == "__main__":
    main()