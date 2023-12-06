import re
from collections import defaultdict

def ints(input: str):
    return [int(x) for x in re.findall(r'-?\d+', input)]


def main():
    score = 1
    input = """Time:        59     79     65     75
Distance:   597   1234   1032   1328
""".split('\n')
    times  = ints(input[0])
    distances = ints(input[1])
    for i, time in enumerate(times):
        winning = []
        old_record = distances[i]
        hold = 0
        while time > 0:
            speed = hold
            total_distance = time*speed
            if total_distance > old_record:
                winning.append(hold)
            hold += 1
            time -= 1
        score *=  len(winning)


    

    print('part1:', score)

def main2():
    score = 1
    input = """Time:        59796575
Distance:   597123410321328
""".split('\n')
    times  = ints(input[0])
    distances = ints(input[1])
    for i, time in enumerate(times):
        winning = []
        old_record = distances[i]
        hold = 0
        while time > 0:
            speed = hold
            total_distance = time*speed
            if total_distance > old_record:
                winning.append(hold)
            hold += 1
            time -= 1
        score *=  len(winning)
    print('part2:', score)
main()
main2()