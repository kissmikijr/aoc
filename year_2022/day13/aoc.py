import math
import string
from collections import defaultdict, deque
from queue import PriorityQueue
from functools import lru_cache

def compare(left, right):
    p = 0
    in_order = False
    could_decide = False
    while True:
        if p == len(left) and p < len(right):
            #left array ran out first
            could_decide = True
            in_order = True
            break
        elif p < len(left) and p == len(right):
            #right array ran out first
            could_decide = True
            in_order = False
            break
        elif (p == len(left)) and (p == len(right)):
            break

        left_value = left[p]
        right_value = right[p]
        if isinstance(left_value, int) and isinstance(right_value, list):
            left_value = [left_value]
        elif isinstance(left_value, list) and isinstance(right_value, int):
            right_value = [right_value]

        if isinstance(left_value, int) and isinstance(right_value, int):
            if left_value < right_value:
                in_order = True
                could_decide = True
                break
            elif left_value > right_value:
                in_order = False
                could_decide = True
                break
            else:
                in_order = True
                could_decide = False
        elif isinstance(left_value, list) and isinstance(right_value, list):
            in_order, could_decide = compare(left_value, right_value)
            if not in_order and could_decide:
                break
            if could_decide:
                break

        p += 1

    return in_order, could_decide

def part1(input: str):
    packets = defaultdict(list)
    i = 1
    for l in input.split('\n'):
        if l == '':
            i += 1
            continue
        packets[i].append(eval(l))
    result = 0
    for k, v in packets.items():
        r, _ = compare(v[0], v[1])

        if r:
            result += k

    print("Part1: ", result)
    return result


def part2(input: str):
    result = None
    packets = []
    i = 1
    for l in input.split('\n'):
        if l == '':
            continue
        packets.append(eval(l))
    packets.append([[6]]) 
    packets.append([[2]]) 

    swap = True
    while swap:
        i = 0
        swap = False
        while i < len(packets)-1:
            p = packets[i]
            next_p = packets[i+1]
            in_order, _ = compare(p, next_p)
            if not in_order:
                packets[i], packets[i+1] = packets[i+1], packets[i]
                swap = True

            i+=1 

    result = 1
    for i, p in enumerate(packets):
        if p == [[6]]:
            print('6', i +1)
            result *= (i + 1)
        elif p == [[2]]:
            print('2', i +1)
            result *= (i + 1)



    print("Part2: ", result)
    return result


def main():
    input_text = open('input.txt', 'r')
    input: str = input_text.read()


    part1(input)
    part2(input)

main()