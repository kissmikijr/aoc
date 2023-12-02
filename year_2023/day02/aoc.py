import re

def ints(input: str):
    return [int(x) for x in re.findall(r'-?\d+', input)]

max_cubes = {
    'red':12,
    'green':13,
    'blue':14
}

def main():
    input_text = open('input.txt', 'r')
    score = 0
    for line in input_text.read().split('\n'):
        game = line.split(':')
        id = ints(game[0])
        sets = game[1].split(';')
        valid = True
        for sett in sets:
            cubes = sett.split(',')
            for cube in cubes:
                value = ints(cube)[0]
                if value > max_cubes[re.findall(r'red|green|blue',cube)[0]]:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            score += id[0]


def main2():
    input_text = open('input.txt', 'r')
    score = 0
    for line in input_text.read().split('\n'):
        game = line.split(':')
        id = ints(game[0])
        sets = game[1].split(';')
        valid = True
        max_red = 0
        max_green = 0
        max_blue = 0
        for sett in sets:
            cubes = sett.split(',')
            for cube in cubes:
                value = ints(cube)[0]
                color = re.findall(r'red|green|blue',cube)[0]
                if color == 'red':
                    if value > max_red:
                        max_red = value
                if color == 'green':
                    if value > max_green:
                        max_green = value
                if color == 'blue':
                    if value > max_blue:
                        max_blue = value

        score += max_red * max_green * max_blue
    print(score)

main()
main2()