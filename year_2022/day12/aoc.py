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

    grid = parse_to_grid(input)

    result = 0

    start = (20, 0)
    end = (20, 107)

    visited = set()
    distances =  empty_grid_x_by_y(float('inf'),len(grid), len(grid[0]))
    distances[start[0]][start[1]] = 1

    queue = PriorityQueue()
    queue.put((0, start))

    while not queue.empty():
        current_dist, current = queue.get()
        if end in visited:
            break
        if current not in visited:
            visited.add(current)

            neighbours = [
                (current[0] -1, current[1]),
                (current[0]+1, current[1]),
                (current[0], current[1]-1),
                (current[0], current[1]+1),
            ]
            for n in neighbours:
                if n[0] < 0 or n[1] < 0 or n[0] >= len(grid) or n[1] >= len(grid[0]):
                    continue

                neighbour_height = grid[n[0]][n[1]]
                current_height = grid[current[0]][current[1]]

                nh_int = string.ascii_lowercase.index(neighbour_height)
                ch_int = string.ascii_lowercase.index(current_height)

                if nh_int <= ch_int or (nh_int-ch_int == 1):
                    old_dist = distances[n[0]][n[1]]
                    new_dist = current_dist + 1
                    if new_dist <= old_dist:
                        distances[n[0]][n[1]] = new_dist
                        queue.put((new_dist, n))
    print(distances)
    print(distances[end[0]][end[1]])

    print("Part1: ", result)
    return result


def part2(input: str):

    grid = parse_to_grid(input)

    result = 0

    start = (20, 0)
    end = (20, 107)

    visited = set()
    distances =  empty_grid_x_by_y(float('inf'),len(grid), len(grid[0]))
    distances[start[0]][start[1]] = 1

    queue = PriorityQueue()
    queue.put((0, start))
    shortest_path = float("inf")
    a_s = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'a':
                a_s.append((i, j))

    for a in a_s:
        visited = set()
        distances =  empty_grid_x_by_y(float('inf'),len(grid), len(grid[0]))
        distances[start[0]][start[1]] = 1

        queue = PriorityQueue()
        queue.put((0, a))
        while not queue.empty():
            current_dist, current = queue.get()
            if end in visited:
                break
            if current not in visited:
                visited.add(current)

                neighbours = [
                    (current[0] -1, current[1]),
                    (current[0]+1, current[1]),
                    (current[0], current[1]-1),
                    (current[0], current[1]+1),
                ]
                for n in neighbours:
                    if n[0] < 0 or n[1] < 0 or n[0] >= len(grid) or n[1] >= len(grid[0]):
                        continue

                    neighbour_height = grid[n[0]][n[1]]
                    current_height = grid[current[0]][current[1]]

                    nh_int = string.ascii_lowercase.index(neighbour_height)
                    ch_int = string.ascii_lowercase.index(current_height)

                    if nh_int <= ch_int or (nh_int-ch_int == 1):
                        old_dist = distances[n[0]][n[1]]
                        new_dist = current_dist + 1
                        if new_dist <= old_dist:
                            distances[n[0]][n[1]] = new_dist
                            queue.put((new_dist, n))
        if distances[end[0]][end[1]] < shortest_path:
            shortest_path = distances[end[0]][end[1]]
    print("Part2: ", shortest_path)
    return shortest_path


def main():
    input_text = open('input.txt', 'r')
    input: str = input_text.read()


    part1(input)
    part2(input)

main()