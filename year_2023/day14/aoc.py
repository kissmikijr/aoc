import math
import string
from collections import defaultdict, deque
from queue import PriorityQueue
from functools import lru_cache

def empty_grid_x_by_y(filler, x, y):
    r = []
    for _ in range(x):
        t = []
        for _ in range(y):
            t.append(filler)
        r.append(t)
    return r

def part1(input: str):
    result = 0
    grid = empty_grid_x_by_y('.', 160, 110)

    for series_of_instruction in input.split('\n'):
        d = [[int(y) for y in x.split(',')] for x in series_of_instruction.split(' -> ')]
        for i  in range(len(d)-1):
            start_coords = d[i]
            end_coords = d[i+1]
            x, y = start_coords
            xx, yy = end_coords
            x -= 400
            xx -= 400

            rocks = []
            if x == xx:
                for ii in range(min(y, yy), max(y, yy) +1):
                    rocks.append((x, ii))
            elif y == yy:
                for jj in range(min(x, xx), max(x, xx)+1):
                    rocks.append((jj, y))
            for rock_x, rock_y in rocks:
                grid[rock_y][rock_x] = '#'
    sp = [100, 0]
    sand_pos = sp
    while True:
        if sand_pos[1]+1 >= len(grid):
            break
        sand_pos = sp
        rest = False
        while not rest:
            if sand_pos[1]+1 >= len(grid):
                break
            next_pos = grid[sand_pos[1]+1][sand_pos[0]]
            if next_pos == '#' or next_pos == 'o':
                next_pos = grid[sand_pos[1]+1][sand_pos[0]-1]
                if next_pos == '#' or next_pos == 'o':
                    next_pos = grid[sand_pos[1]+1][sand_pos[0]+1]
                    if next_pos == '#' or next_pos == 'o':
                        grid[sand_pos[1]][sand_pos[0]] = 'o'
                        rest = True
                    else:
                        sand_pos = [sand_pos[0]+1, sand_pos[1]+1]
                else:
                    sand_pos = [sand_pos[0] -1, sand_pos[1]+1]
            else:
                sand_pos = [sand_pos[0] , sand_pos[1] +1]
        
    for col in grid:
        for c in col:
            if c == 'o':
                result += 1
    print(result)
    return result


def part2(input: str):
    result = 0
    grid = empty_grid_x_by_y('.', 159, 1000)

    for series_of_instruction in input.split('\n'):
        d = [[int(y) for y in x.split(',')] for x in series_of_instruction.split(' -> ')]
        for i  in range(len(d)-1):
            start_coords = d[i]
            end_coords = d[i+1]
            x, y = start_coords
            xx, yy = end_coords
            x -= 400
            xx -= 400

            rocks = []
            if x == xx:
                for ii in range(min(y, yy), max(y, yy) +1):
                    rocks.append((x, ii))
            elif y == yy:
                for jj in range(min(x, xx), max(x, xx)+1):
                    rocks.append((jj, y))
            for rock_x, rock_y in rocks:
                grid[rock_y][rock_x] = '#'
    
    grid.append(['.' for _ in range(len(grid[0]))])
    grid.append(['#' for _ in range(len(grid[0]))])

    sp = [100, 0]
    sand_pos = sp
    rest = False
    while True:
        if sand_pos == sp and rest:
            break
        sand_pos = sp
        rest = False
        while not rest:
            next_pos = grid[sand_pos[1]+1][sand_pos[0]]
            if next_pos == '#' or next_pos == 'o':
                next_pos = grid[sand_pos[1]+1][sand_pos[0]-1]
                if next_pos == '#' or next_pos == 'o':
                    next_pos = grid[sand_pos[1]+1][sand_pos[0]+1]
                    if next_pos == '#' or next_pos == 'o':
                        rest = True
                        grid[sand_pos[1]][sand_pos[0]] = 'o'
                        if sand_pos == sp:
                            break
                    else:
                        sand_pos = [sand_pos[0]+1, sand_pos[1]+1]
                else:
                    sand_pos = [sand_pos[0] -1, sand_pos[1]+1]
            else:
                sand_pos = [sand_pos[0] , sand_pos[1] +1]

    for col in grid:
        for c in col:
            if c == 'o':
                result += 1
    print(result)
    return result


def main():
    input_text = open('input.txt', 'r')
    input: str = input_text.read()


    part1(input)
    part2(input)

main()