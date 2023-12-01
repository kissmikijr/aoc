import math
import string
from collections import defaultdict, deque
from queue import PriorityQueue
from functools import lru_cache

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

def part1(input: str):
    print(input)
    packets = defaultdict(list)
    i = 1
    for l in input.split('\n'):
        if l == '':
            continue
        packets[i].append(l)
    print(packets)


    result = None
    print("Part1: ", result)
    return result


def part2(input: str):

    result = None

    print("Part2: ", result)
    return result


def main():
    input_text = open('input.txt', 'r')
    input: str = input_text.read()


    part1(input)
    part2(input)

main()