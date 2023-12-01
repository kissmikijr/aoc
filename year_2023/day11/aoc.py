import subprocess
from functools import reduce
from operator import add, mul
import math

def test(item,monkey_items, divisor, on_true, on_false):


    if item % divisor == 0:
        monkey_items[on_true].append(item)
    else:
        monkey_items[on_false].append(item)

    return monkey_items

def part1(input: str):
    result = 0
    i = 0
    monkey_items = [
        [63, 84, 80, 83, 84, 53, 88, 72],
        [67, 56, 92, 88, 84],
        [52],
        [59, 53, 60, 92, 69, 72],
        [61, 52, 55, 61],
        [79, 53],
        [59, 86, 67, 95, 92, 77, 91],
        [58, 83, 89],
    ]
    inspect_counts = [0,0,0,0,0,0,0,0]
    monkeys = [
        {
            "opeartion": lambda o: o*11,
            "test": lambda item, monkeys: test(item, monkeys, 13, 4, 7)
        },
        {
            "opeartion": lambda o: o+4,
            "test": lambda item, monkeys: test(item, monkeys, 11, 5, 3)
        },
                {
            "opeartion": lambda o: o*o,
            "test": lambda item, monkeys: test( item, monkeys, 2, 3, 1)
        },
                {
            "opeartion": lambda o: o+2,
            "test": lambda  item, monkeys: test( item, monkeys, 5, 5, 6)
        },
                {
            "opeartion": lambda o: o+3,
            "test": lambda item, monkeys: test( item, monkeys, 7, 7, 2)
        },
                {
            "opeartion": lambda o: o+1,
            "test": lambda  item, monkeys: test( item, monkeys, 3, 0, 6)
        }
        ,
                {
            "opeartion": lambda o: o+5,
            "test": lambda  item, monkeys: test( item, monkeys, 19, 4, 0)
        },
        {
            "opeartion": lambda o: o*19,
            "test": lambda item, monkeys: test( item, monkeys, 17, 2, 1)
        }
    ]
    max_rounds = 20
    round = 0
    while round < max_rounds:
        for i, m in enumerate(monkeys):
            for item in monkey_items[i]:
                inspect_counts[i] += 1
                # inspect
                new_worry = m["opeartion"](item)
                #reliefe
                new_worry = new_worry // 3
                #throw
                m["test"](new_worry, monkey_items)
            monkey_items[i] = []
        round += 1

    s = sorted(inspect_counts, reverse=True)
    result = s[0] * s[1]
    print("Part1: ", result)
    return result

def part2(input: str):
    result = 0
    i = 0
    monkey_items = [
        [63, 84, 80, 83, 84, 53, 88, 72],
        [67, 56, 92, 88, 84],
        [52],
        [59, 53, 60, 92, 69, 72],
        [61, 52, 55, 61],
        [79, 53],
        [59, 86, 67, 95, 92, 77, 91],
        [58, 83, 89],
    ]
    inspect_counts = [0,0,0,0,0,0,0,0]
    monkeys = [
        {
            "opeartion": lambda o: o*11,
            "test": lambda item, monkeys: test(item, monkeys, 13, 4, 7)
        },
        {
            "opeartion": lambda o: o+4,
            "test": lambda item, monkeys: test(item, monkeys, 11, 5, 3)
        },
                {
            "opeartion": lambda o: o*o,
            "test": lambda item, monkeys: test( item, monkeys, 2, 3, 1)
        },
                {
            "opeartion": lambda o: o+2,
            "test": lambda  item, monkeys: test( item, monkeys, 5, 5, 6)
        },
                {
            "opeartion": lambda o: o+3,
            "test": lambda item, monkeys: test( item, monkeys, 7, 7, 2)
        },
                {
            "opeartion": lambda o: o+1,
            "test": lambda  item, monkeys: test( item, monkeys, 3, 0, 6)
        }
        ,
                {
            "opeartion": lambda o: o+5,
            "test": lambda  item, monkeys: test( item, monkeys, 19, 4, 0)
        },
        {
            "opeartion": lambda o: o*19,
            "test": lambda item, monkeys: test( item, monkeys, 17, 2, 1)
        }
    ]
    max_rounds = 10000
    round = 0
    # least common multiple
    lcm = math.lcm(13, 11, 2, 5, 7, 3, 19, 17) 
    while round < max_rounds:
        for i, m in enumerate(monkeys):
            for item in monkey_items[i]:
                inspect_counts[i] += 1
                # inspect
                new_worry = m["opeartion"](item)
                #reliefe
                new_worry = new_worry % lcm
                #throw
                m["test"](new_worry, monkey_items)
            monkey_items[i] = []
        round += 1

    s = sorted(inspect_counts, reverse=True)
    result = s[0] * s[1]
    print("Part2: ", result)
    return result



def main():
    input_text = open('input.txt', 'r')
    input: str = input_text.read()

    result = part1(input)
    result = part2(input)
    if not result:
        subprocess.run(['pbcopy'], input=str(result).encode('utf-8'))


main()