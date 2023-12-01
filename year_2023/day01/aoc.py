import re

def ints(input: str):
    return [int(x) for x in re.findall(r'-?\d', input)]

word_digits = {
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'one': 1,
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9,
}
def rev_ints_and_words(input: str):
    return [word_digits[x[::-1]] for x in re.findall(r"\d|thgie|eno|owt|eerht|ruof|evif|xis|neves|enin", input[::-1])][::-1]

def ints_and_words(input: str):
    return [word_digits[x] for x in re.findall(r'\d|eight|one|two|three|four|five|six|seven|nine', input)]


def main2():
    input_text = open('input.txt', 'r')
    score = 0
    for line in input_text.read().split('\n'):
        start_digits = ints_and_words(line)[0]
        end_digits = rev_ints_and_words(line)[-1]
        score += start_digits*10+end_digits

    print('part2:', score)

def main():
    input_text = open('input.txt', 'r')
    score = 0
    for line in input_text.read().split('\n'):
        start_digit = ints(line)[0]
        end_digit = ints(line)[-1]
        score += start_digit*10+end_digit

    print('part1:', score)
main()
main2()