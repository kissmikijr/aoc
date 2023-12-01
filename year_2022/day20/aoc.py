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
    data = []
    for l in input.split('\n'):
        data.append(int(l))
    mutable = [x for x in data]
    keep_track = [y for y in range(len(data))]
    print(data)
    for i, d in enumerate(data):
        next_coord = i+d
        ii = keep_track[i]
        if next_coord > len(data):
            next_coord = (ii+d ) % len(mutable)
        elif next_coord < 0:
            next_coord = ((ii+d) % len(mutable)) * -1
        print(i, d, next_coord, mutable)
        if i >= len(mutable)-1:
            continue
        for j in range(next_coord+1):
            # data = [1, 2, -3, 3, -2, 0, 4]
            # mutable = [2, 1, -3, 3, -2, 0, 4]
            # keep_track = [1,0,2,3,4,5]
            mutable[keep_track[i]+j], mutable[keep_track[i]+1+j] = mutable[keep_track[i]+1+j], mutable[keep_track[i]+j]
            keep_track[i+j], keep_track[i+j+1] = i+j+1, i+j

    nr1 = mutable[(1000 % len(data))]
    nr2 = mutable[(2000 % len(data))]
    nr3 = mutable[(3000 % len(data))]
    print(nr1, nr2, nr3)

    nr1 = mutable[(1000 % len(data)-1)]
    nr2 = mutable[(2000 % len(data)-1)]
    nr3 = mutable[(3000 % len(data)-1)]
    print(nr1, nr2, nr3)

    result += sum([nr1, nr2, nr3])
    print('Part1: ', result)
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

    return result


def main():
    input_text = open('input-test.txt', 'r')
    input: str = input_text.read()


    part1(input)
    part2(input)

main()