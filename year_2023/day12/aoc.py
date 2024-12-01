import re

def ints(input: str):
    return [int(x) for x in re.findall(r'-?\d', input)]

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



def main():
    input_text = open('input.txt', 'r')
    score = 0
    for line in input_text.read().split('\n'):
        arrangement, ways = line.split(' ')
        possible_ways = ints(ways)
    
    print('part1', score)

def main2():
    input_text = open('input.txt', 'r')

    score = 0
    print('part2', score)

main()
main2()