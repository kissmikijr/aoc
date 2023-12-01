import math
import string
from collections import defaultdict, deque
from queue import PriorityQueue
from functools import lru_cache
import re

def ints(input: str):
    return [int(x) for x in re.findall(r'-?\d+', input)]
def capitals(input:str):
    return re.findall(r'[A-Z][A-Z]', input)

def empty_grid_x_by_y(filler, x, y):
    r = []
    for _ in range(x):
        t = []
        for _ in range(y):
            t.append(filler)
        r.append(t)
    return r

def empty_grid_x_by_y_z(filler, x, y, z):
    zz = []
    for _ in range(z):
        yy = []
        for _ in range(y):
            xx = []
            for _ in range(x):
                xx.append(filler)
            yy.append(xx)
        zz.append(yy)
    return zz

def plain_sides(matrix, pos):
    sides = 6
    x, y, z = pos

    above = (x, y, z +1)
    belove = (x, y, z -1)
    left = (x-1, y, z)
    right = (x+1, y, z)
    up = (x, y -1 , z)
    down = (x, y +1 , z)

    for neighbour in [above, belove, left, right, up, down]:
        xx, yy, zz = neighbour
        if matrix[zz][yy][xx] > 0:
            sides -= 1
            matrix[zz][yy][xx] -= 1
    matrix[z][y][x] = pos

    return matrix, sides

def part1(input: str):
    result = 0
    matrix = empty_grid_x_by_y_z(0, 22,22,22)
    coords = []
    for coord in input.split('\n'):
        coords.append(tuple(ints(coord)))

    for pos in coords:
        sides = 6
        x, y, z = pos

        above = (x, y, z +1)
        belove = (x, y, z -1)
        left = (x-1, y, z)
        right = (x+1, y, z)
        up = (x, y -1 , z)
        down = (x, y +1 , z)

        for neighbour in [above, belove, left, right, up, down]:
            xx, yy, zz = neighbour
            if matrix[zz][yy][xx] > 0:
                sides -= 1
                matrix[zz][yy][xx] -= 1
        matrix[z][y][x] = sides
    r = 0
    for z in matrix:
        for y in z:
             r += sum(y)
    print(r)
    return result


grid_size = 22
def get_neighbours(coord):
    r = []
    x, y, z = coord

    if z+1 < grid_size:
        r.append((x, y, z +1)) 
    if z -1 >= 0:
        r.append((x, y, z -1))
    if x - 1 >= 0:
        r.append((x-1, y, z))
    if x +1 < grid_size:
        r.append((x+1, y, z))
    if y - 1 >= 0:
        r.append((x, y-1, z))
    if y + 1 < grid_size:
        r.append((x, y+1, z))
    return r

def part2(input: str):
    result = 0
    matrix = empty_grid_x_by_y_z(0, 22,22,22)
    coords = []
    for coord in input.split('\n'):
        coords.append(tuple(ints(coord)))

    for pos in coords:
        x, y, z = pos
        matrix[z][y][x] = 1

    stack = [(0,0,0)]
    area = 0
    visited = set()
    while stack:                
        coord = stack.pop()
        if coord in visited:
            continue
        visited.add(coord)
        neighbours = get_neighbours(coord)
        for n in neighbours:
            x, y, z = n
            if matrix[z][y][x] == 1:
                area += 1
            else:
                stack.append(n)
    print(area, 'huh')

    return result


def main():
    input_text = open('input.txt', 'r')
    input: str = input_text.read()


    part1(input)
    part2(input)

main()