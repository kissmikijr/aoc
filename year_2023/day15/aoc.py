import math
import string
from collections import defaultdict, deque
from queue import PriorityQueue
from functools import lru_cache
import re

def ints(input: str):
    return [int(x) for x in re.findall(r'-?\d+', input)]


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
    positions = []
    for l in input.split('\n'):
        coords = ints(l)
        sensor = (coords[0], coords[1])
        bacon = (coords[2], coords[3])
        distance = abs(sensor[0] - bacon[0]) + abs(sensor[1] - bacon[1])
        positions.append({"sensor":sensor, "bacon": bacon, "distance":distance})

    y = 2000000
    # y = 10
    result = set()
    for data in positions:
        sensor = data.get('sensor')
        distance = data['distance']
        if sensor[1] > y:
            # sensor=18, y=10
            # dist=7
            overflow = sensor[1] - distance - y
            if overflow < 0:
                result.add((sensor[0], overflow, y))
        elif sensor[1] < y:
            # sensor=5, y=10
            # dist=7
            overflow = sensor[1] + distance - y
            if overflow > 0:
                result.add((sensor[0], overflow, y))



    ranges = set()
    result = list(result)
    for i, p in enumerate(result):
        curr_range = (min(result[i][0]-result[i][1], result[i][0]+result[i][1]),  max(result[i][0]-result[i][1], result[i][0]+result[i][1]))
        ranges.add(curr_range)

    ranges = list(ranges)
    merge = True
    while merge:
        merge = False
        for i in range(len(ranges)):
            curr_range = ranges[i]
            for j in range(len(ranges)):
                next_range = ranges[j]
                if i == j:
                    continue
                if curr_range[0] > next_range[1] or curr_range[1] < next_range[0]:
                    continue
                else:
                    # (-1, 2), (2, 12)
                    merge = True
                    ranges[i] = (min(next_range[0], curr_range[0]), max(next_range[1], curr_range[1]))
                    ranges.pop(j)
                    break
            if merge:
                break
    
    print(ranges)
    return result


def part2(input: str):
    result = 0
    positions = []
    for l in input.split('\n'):
        coords = ints(l)
        sensor = (coords[0], coords[1])
        bacon = (coords[2], coords[3])
        distance = abs(sensor[0] - bacon[0]) + abs(sensor[1] - bacon[1])
        positions.append({"sensor":sensor, "bacon": bacon, "distance":distance})
    nr = []
    for y in range(21):
        ranges = set()
        print(y)
        print(nr)
        # y = 2000000
        # y = 10
        result = set()
        for data in positions:
            sensor = data.get('sensor')
            distance = data['distance']
            if sensor[1] > y:
                # sensor=18, y=10
                # dist=7
                overflow = sensor[1] - distance - y
                if overflow < 0:
                    result.add((sensor[0], overflow, y))
            elif sensor[1] < y:
                # sensor=5, y=10
                # dist=7
                overflow = sensor[1] + distance - y
                if overflow > 0:
                    result.add((sensor[0], overflow, y))


        result = list(result)
        for i, p in enumerate(result):
            curr_range = (min(result[i][0]-result[i][1], result[i][0]+result[i][1]),  max(result[i][0]-result[i][1], result[i][0]+result[i][1]))
            ranges.add(curr_range)

        ranges = list(ranges)
        merge = True
        while merge:
            merge = False
            for i in range(len(ranges)):
                curr_range = ranges[i]
                for j in range(len(ranges)):
                    next_range = ranges[j]
                    if i == j:
                        continue
                    if curr_range[0] > next_range[1] or curr_range[1] < next_range[0]:
                        continue
                    else:
                        # (-1, 2), (2, 12)
                        merge = True
                        ranges[i] = (min(next_range[0], curr_range[0]), max(next_range[1], curr_range[1]))
                        ranges.pop(j)
                        break
                if merge:
                    break
        nr.append(ranges)
    print(nr)
    canvas = []
    for x in range(len(nr)):
        for l, r in nr[x]:
            row = []
            for i in range(20):
                if i >= l:
                    row.append('#')
                else:
                    row.append('.')
            canvas.append(row) 
    for l in canvas:
        print(l)

    return result


def main():
    input_text = open('input-test.txt', 'r')
    input: str = input_text.read()


    # part1(input)
    part2(input)

main()