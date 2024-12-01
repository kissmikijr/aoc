import re
from collections import Counter

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

left_and_right_pipes = ['-', 'J', '7']
top_and_bottom_pipes = ['|', 'L', 'J']
connections = {
    '|':['|', 'L', 'F', 'J', '7'],
    '-' : ['-','7','L', 'J', 'F'],
    'L': ['|', '-', 'J', 'F'],
    'J': ['-', '|', '7', 'L'],
    '7': ['-','|', 'F','J'],
    'F':['-', '|', '7', 'L'],
    '.': []
}
def valid_neighbours(grid, y, x):
    valid_neighbours = []
    current = grid[y][x]
    if grid[y][x] == '.':
        return []
    # left
    if x-1 >= 0:
        if current in connections[grid[y][x - 1]]:
            print(current,  connections[grid[y][x-1]], '@')
            valid_neighbours.append([y, x-1])
    # right
    if x + 1 <= len(grid[0]) - 1:
        if  current in connections[grid[y][x+1]]:
            print(current,  connections[grid[y][x+1]], '@@')
            valid_neighbours.append([y, x+1])
    # top
    if y - 1 >= 0:
        if current in connections[grid[y-1][x]]:
            print(current,  connections[grid[y-1][x]], '@@@')
            valid_neighbours.append([y-1, x])
    # bottom
    if y + 1 <= len(grid) - 1:
        if current in connections[grid[y+1][x]]:
            print(current,  connections[grid[y+1][x]], '@@@@')
            valid_neighbours.append([y+1, x])
    print(valid_neighbours,'@')
    return valid_neighbours
#    topright
#     if x + 1 <= len(grid[0]) - 1 and y - 1 >= 0:
#         if grid[y-1][x+1] in symbols:
#             return True
#     # topleft
#     if x - 1 >= 0 and y - 1 >= 0:
#         if grid[y-1][x-1] in symbols:
#             return True
#     # bottomleft
#     if x - 1 >= 0 and y + 1 <= len(grid) -1:
#         if grid[y+1][x-1] in symbols:
#             return True
#     # bottomright
#     if x + 1 <= len(grid[0]) - 1 and y + 1 <= len(grid) -1:
#         if grid[y+1][x+1] in symbols:
#             return True

def recurse(grid, neighbours, start_coord, step, steps_grid):
    print(neighbours,'NN')
    for ny, nx in neighbours:
        if (ny, nx) == start_coord:
            return
        # visited.append((ny, nx))
        if step < steps_grid[ny][nx]:
            steps_grid[ny][nx] = step
        print(step, steps_grid[ny][nx], '@##@$@#$@')
        return recurse(grid, valid_neighbours(grid, ny, nx), start_coord, step+1, steps_grid)


def main():
    input_text = open('input.txt', 'r')
    grid =parse_to_grid(input_text.read())
    start_coord = None
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'S':
                start_coord = (y, x)
    grid[start_coord[0]][start_coord[1]] = 'F'
    steps_grid = empty_grid_x_by_y(float('inf'),len(grid), len(grid[0]))
    visited = [start_coord]
    v_neighbours = valid_neighbours(grid, start_coord[0], start_coord[1])
    recurse(grid, v_neighbours, start_coord, 0, steps_grid)
    print(steps_grid)
    print('part1')

def main2():

    input_text = open('input.txt', 'r')
    score = 0
    for line in input_text.read().split('\n'):
        pass
        
    print('part2:', score)


main()
main2()