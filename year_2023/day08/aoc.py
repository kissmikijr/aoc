import re
from collections import Counter

def ints(input: str):
    return [int(x) for x in re.findall(r'-?\d', input)]



def main():
    input_text = open('input.txt', 'r')
    read = input_text.read().split('\n')
    instructions = ints(read[0].replace('L', '0').replace('R', '1'))
    print(instructions)
    read = read[2:]
    network = {}
    score = 0
    for line in read[2:]:
        print(line)
        key, value = line.split(' = ')
        l, r = value.split(', ')
        network[key] = [l.replace('(',''), r.replace(')', '')]
    print(instructions, network)



    print('part1:', score)
def main2():
    input_text = open('input.txt', 'r')
    score = 0
    for line in input_text.read().split('\n'):
        pass
        
    print('part2:', score)


main()
main2()