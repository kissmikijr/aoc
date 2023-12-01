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

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []

    paths = []
    for node in graph[start]['neighbours']:
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)
            for np in new_paths:
                if 
                paths.append(np)
    return paths

def part1(input: str):
    result = 0
    graph = {}
    for l in input.split('\n'):
        caps = capitals(l)
        flow = ints(l)
        graph[caps[0]] = {'flow': flow[0], 'neighbours': caps[1:]}

    d = {}
    for key in graph.keys():
        routes = []
        stack = [(key, [key])]

        
        while stack:
            v, path = stack.pop()
            routes.append(path)
            valve = graph[v]
            for n in valve['neighbours']:
                if n not in path:
                    stack.append((n, path+[n]))
        d[key] = routes

    important_nodes = ['AA']
    for k, v in graph.items():
        if v['flow'] != 0:
            important_nodes.append(k)
    print(important_nodes)
    all_paths = defaultdict(list)
    for i, imp in enumerate(important_nodes):
        if i+1 >= len(important_nodes):
            continue
        all_paths[imp].append(find_all_paths(graph, imp, important_nodes[i+1]))
    print(all_paths)
    pressure_released = []

    # opened_valves = set()
    # for key in d.keys():
    #     for route in d[key]:
    #         pressure = 0
    #         minutes = 31
    #         for valve in route:
    #             minutes -= 1
    #             flow = graph[valve]['flow']
    #             if flow > 0:
    #                 minutes -= 1
    #                 pressure += minutes * flow
    #                 opened_valves.add(valve)
            

    #         pressure_released.append((pressure, 30 - minutes, route))
    print(pressure_released)




    return result


def part2(input: str):
    result = 0

    print('Part2: ',result)
    return result


def main():
    input_text = open('input-test.txt', 'r')
    input: str = input_text.read()


    part1(input)
    part2(input)

main()