import subprocess

def part1(input: str):
    lines = input.split('\n')
    result = 0
    cycle = 1
    X = 1
    cycles_to_count = [20,60,100,140,180,220]
    for row in lines:
        instruction, value = row.split()
        if instruction == 'noop':
            cycle += 1
            if cycle in cycles_to_count:
                result += X * cycle
        elif instruction == 'addx':
            cycle += 1
            if cycle in cycles_to_count:
                result += X * cycle
            cycle += 1
            X += int(value)
            if cycle in cycles_to_count:
                result += X * cycle


    print("Part1: ", result)
    return result

def empty_grid_x_by_y(filler, x, y):
    r = []
    for _ in range(x):
        t = []
        for _ in range(y):
            t.append(filler)
        r.append(t)
    return r

def draw(cycle, X, crt):
    rr = (cycle - 1) // 40 
    if (cycle - 40 * rr)-1 in [X-1, X, X+1]:
        crt[rr][cycle - 40 * rr - 1] = '#'
    return crt

def part2(input: str):
    lines = input.split('\n')
    result = 0
    cycle = 1
    X = 1
    crt = empty_grid_x_by_y('.', 6, 40)

    crt = draw(cycle, X, crt)

    for row in lines:
        instruction, value = row.split()
        crt = draw(cycle, X, crt)

        if instruction == 'noop':
            cycle += 1

        elif instruction == 'addx':
            cycle += 1
            crt = draw(cycle, X, crt)
            cycle += 1
            X += int(value)


    for c in crt:
        print("".join(c))
    print("Part2: ", result)
    return result



def main():
    input_text = open('input.txt', 'r')
    input: str = input_text.read()

    result = part2(input)
    if not result:
        result = part1(input)


    subprocess.run(['pbcopy'], input=str(result).encode('utf-8'))
main()