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

def expand2(grid):
    expanded_rows_y_index = []
    expanded_cols_x_index = []
    for y in range(len(grid)):
        if '#' not in grid[y]:
            expanded_rows_y_index.append(y)

    for x in range(len(grid[0])):
        col = []
        for y in range(len(grid)):
            col.append(grid[y][x])
        if '#' not in col:
            expanded_cols_x_index.append(x)

    return sorted(expanded_rows_y_index, reverse=True), sorted(expanded_cols_x_index, reverse=True)



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
        score += abs(start[0] - finish[0]) + abs(start[1] - finish[1])

    print('part1', score)

def main2():
    input_text = open('input.txt', 'r')
    grid =parse_to_grid(input_text.read())
    rrange = 1000000-1
    expanded_rows_y_index, expanded_cols_x_index = expand2(grid)
    starting_points = []
    score = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '#':
                new_x = x
                for xi in expanded_cols_x_index:
                    if xi < x:
                        new_x += rrange
                new_y = y
                for yi in expanded_rows_y_index:
                    if yi < y:
                        new_y += rrange

                starting_points.append((new_y, new_x))

    for start, finish in itertools.combinations(starting_points, 2):
        score += abs(start[0] - finish[0]) + abs(start[1] - finish[1])

    print('part2', score)

main()
main2()