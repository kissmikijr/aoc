import subprocess
from collections import defaultdict

def part1(input: str):
    i = 1
    grid = [[x for x in y] for y in input.split("\n")]
    result = 2*len(grid) + 2* len(grid[0]) -4
    while i < len(grid) - 1:
        j = 1
        while j < len(grid[i]) - 1:
            if visible_left(grid, i, j) or visible_right(grid, i, j) or visible_top(grid, i, j) or visible_bot(grid, i, j):
                result += 1
            j +=1
        i+=1


    print('Part1: ',result)
    return str(result)

def visible_left(grid, ii, jj):
    j = 0
    visible = True
    while j < jj:
        if j != jj:
            if grid[ii][j] >= grid[ii][jj]:
                visible = False
                break
        j += 1

    return visible

def visible_right(grid, ii, jj):
    j = jj
    visible = True
    while j < len(grid[0]):
        if j != jj:
            if grid[ii][j] >= grid[ii][jj]:
                visible = False
                break
        j += 1

    return visible

def visible_top(grid: str, ii, jj):
    i = 0
    visible = True
    while i < ii:
        if i != ii:
            if grid[i][jj] >= grid[ii][jj]:
                visible = False
                break
        i += 1

    return  visible

def visible_bot(grid: str, ii, jj):
    i = ii
    visible = True
    while i < len(grid):
        if i != ii:
            if grid[i][jj] >= grid[ii][jj]:
                visible = False
                break
        i += 1

    return  visible


def part2(input: str):
    i = 1
    grid = [[x for x in y] for y in input.split("\n")]
    result = 0
    while i < len(grid) - 1:
        j = 1
        while j < len(grid[i]) - 1:
            sc = view_left(grid, i, j) * view_right(grid, i, j) * view_top(grid, i, j) * view_bot(grid, i, j)
            if sc > result:
                result = sc
            j +=1
        i+=1
    print("Part2: ", result)
    return result


def view_left(grid, ii, jj):
    j = jj - 1
    dist = 0
    while j >= 0:
        dist += 1
        if grid[ii][j] >= grid[ii][jj]:
            break

        j -= 1

    return dist

def view_right(grid, ii, jj):
    j = jj + 1
    dist = 0
    while j < len(grid[0]):
        dist += 1
        if grid[ii][j] >= grid[ii][jj]:
            break

        j += 1

    return dist

def view_top(grid: str, ii, jj):
    i = ii - 1
    dist = 0
    while i >= 0:
        dist += 1
        if grid[i][jj] >= grid[ii][jj]:
            break
        i -= 1

    return dist

def view_bot(grid: str, ii, jj):
    i = ii + 1
    dist = 0
    while i < len(grid):
        dist += 1
        if grid[i][jj] >= grid[ii][jj]:
            break
        i += 1

    return dist

if __name__ == '__main__':
    input_text = open('input.txt', 'r')
    input: str = input_text.read()

    result = part2(input)
    if not result:
        result = part1(input)


    subprocess.run(['pbcopy'], input=str(result).encode('utf-8'))