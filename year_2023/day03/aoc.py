import re

def ints(input: str):
    return [int(x) for x in re.findall(r'-?\d+', input)]

def main():
    input_text = open('input.txt', 'r')
    score = 0

    for line in input_text.read().split('\n'):
        print(line)
    print(score)


main()