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
    blueprints = {}
    for line in input.split('\n'):
        integers = ints(line)
        blueprints[integers[0]] = {
            "ore": {"ore": integers[1], "clay":0, "obsidian": 0},
            "clay": {"ore": integers[2], "clay": 0, "obsidian": 0},
            "obsidian": {"ore": integers[3], "clay":integers[4], "obsidian": 0},
            "geode": {"ore": integers[5], "clay": 0, "obsidian": integers[6]}
        }
    minutes = 24
    for k, bp in blueprints.items():
        minute = 1
        resources = {"ore":0, "clay": 0, "obsidian": 0, "geode": 0}
        robots = {"ore":1, "clay": 0, "obsidian": 0, "geode": 0}
        while minute <= minutes:
            print(minute, resources, robots)

            
            if resources["ore"] >= bp["geode"]["ore"] and resources["clay"] >= bp["geode"]["clay"] and resources["obsidian"] >= bp["geode"]["obsidian"]:
                # can build
                resources["ore"] -=  bp["geode"]["ore"]
                resources["clay"] -=  bp["geode"]["clay"]
                resources["obsidian"] -=  bp["geode"]["obsidian"]

                robots["geode"] += 1

            elif resources["ore"] >= bp["obsidian"]["ore"] and resources["clay"] >= bp["obsidian"]["clay"] and resources["obsidian"] >= bp["obsidian"]["obsidian"]:
                # can build
                resources["ore"] -=  bp["obsidian"]["ore"]
                resources["clay"] -=  bp["obsidian"]["clay"]
                resources["obsidian"] -=  bp["obsidian"]["obsidian"]

                robots["obsidian"] += 1

            elif resources["ore"] >= bp["clay"]["ore"] and resources["clay"] >= bp["clay"]["clay"] and resources["obsidian"] >= bp["clay"]["obsidian"]:
                # can build
                resources["ore"] -=  bp["clay"]["ore"]
                resources["clay"] -=  bp["clay"]["clay"]
                resources["obsidian"] -=  bp["clay"]["obsidian"]

                robots["clay"] += 1
            elif resources["ore"] >= bp["ore"]["ore"] and resources["clay"] >= bp["ore"]["clay"] and resources["obsidian"] >= bp["ore"]["obsidian"]:
                # can build
                resources["ore"] -=  bp["ore"]["ore"]
                resources["clay"] -=  bp["ore"]["clay"]
                resources["obsidian"] -=  bp["ore"]["obsidian"]

                robots["ore"] += 1

            for r_k, number_of_robots in robots.items():
                if number_of_robots > 0:
                    resources[r_k] += number_of_robots

            minute += 1
        result += k * resources["geode"] 
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