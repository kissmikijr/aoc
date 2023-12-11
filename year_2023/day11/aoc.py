import re
import itertools

def ints(input: str):
    return [int(x) for x in re.findall(r'-?\d', input)]

def parse_to_grid(input,delimeter="\n"):
    return [[x for x in y] for y in input.split(delimeter)]

def empty_grid_x_by_y(filler, x, y):
    r = []
    for _ in range(x):
        t = []
        for _ in range(y):
            t.append(filler)
        r.append(t)
    return r

def expand(grid):
    expanded_x = []
    for y in range(len(grid)):
        if '#' not in grid[y]:
            for i in range(2):
                expanded_x.append(grid[y])
        else:
            expanded_x.append(grid[y])

    xs_to_expand = []
    for x in range(len(grid[0])):
        col = []
        for y in range(len(grid)):
            col.append(grid[y][x])
        if '#' not in col:
            xs_to_expand.append(x)

    expanded = []
    for y in range(len(expanded_x)):
        exp_row = []
        for x in range(len(expanded_x[y])):
            if x in xs_to_expand:
                for i in range(2):
                    exp_row.append('.')
            else:
                exp_row.append(expanded_x[y][x])
        expanded.append(exp_row)
    return expanded

def get_neighbours(grid, y, x ):
    valid_neighbours = []
    # left
    if x-1 >= 0:
        valid_neighbours.append((y, x-1))
    # right
    if x + 1 <= len(grid[0]) - 1:
        valid_neighbours.append((y, x+1))
    # top
    if y - 1 >= 0:
        valid_neighbours.append((y-1, x))
    # bottom
    if y + 1 <= len(grid) - 1:
        valid_neighbours.append((y+1, x))
    return valid_neighbours


def main():
    input_text = open('input.txt', 'r')
    grid =parse_to_grid(input_text.read())
    grid = expand(grid)
    starting_points = []
    score = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '#':
                starting_points.append((y, x))

    for start, finish in itertools.combinations(starting_points, 2):
        steps_grid = empty_grid_x_by_y(float('inf'),len(grid), len(grid[0]))
        steps_grid[start[0]][start[1]] = 0
        visited = set()
        stack = [start]
        while stack:
            current = stack.pop()
            cv = steps_grid[current[0]][current[1]]
            if current in visited:
                continue

            visited.add(current)
            neighbours = get_neighbours(grid, current[0], current[1])
            neighbour_values = [cv]
            for ny, nx in neighbours: 
                neighbour_values.append(steps_grid[ny][nx])
                stack.append((ny, nx))
            steps_grid[current[0]][current[1]] = min(neighbour_values)+1



        score += steps_grid[finish[0]][finish[1]] - 1

    print('part1', score)

def main2():

    input_text = open('input.txt', 'r')
    score = 0
    for line in input_text.read().split('\n'):
        pass
        
    print('part2:', score)


main()
main2()