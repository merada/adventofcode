import sys

ITERATIONS = 100 
ON = 1
OFF = 0

def main():
    ''' Conway's Game of Life with Christmas lights. Corner lights remain on.
    '''
    grid = []
    for line in sys.stdin.readlines():
        row = []
        for l in line:
            if l == '#':
                row.append(ON)
            elif l == '.':
                row.append(OFF)
        grid.append(row)

    grid = set_corners(grid)

    for i in range(ITERATIONS):
        temp_grid = [[0 for x in range(len(grid))] for x in range(len(grid))]
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                temp_grid[y][x] = get_light_value(grid, y, x)
        grid = set_corners(temp_grid)

    num_lights = sum([sum(x) for x in grid])
    print "Number of lights left on is {}.".format(num_lights)

def get_light_value(grid, y, x):
    min_y = max(0, y - 1)
    max_y = min(len(grid), y + 2)
    min_x = max(0, x - 1)
    max_x = min(len(grid[0]), x + 2)

    sum_neighbours = 0
    for y_ in range(min_y, max_y):
        for x_ in range(min_x, max_x):
            sum_neighbours += grid[y_][x_]
    sum_neighbours -= grid[y][x]

    if grid[y][x] == ON:
        if sum_neighbours == 2 or sum_neighbours == 3:
            return ON
    elif grid[y][x] == OFF:
        if sum_neighbours == 3:
            return ON
    return OFF

def set_corners(grid):
    grid[0][0] = ON
    grid[0][len(grid[0])-1] = ON
    grid[len(grid) - 1][0] = ON
    grid[len(grid) - 1][len(grid[0]) - 1] = ON

    return grid

if __name__ == "__main__":
    main()
