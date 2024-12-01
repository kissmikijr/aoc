import re
from collections import Counter

def ints(input: str):
    return [int(x) for x in re.findall(r'-?\d+', input)]



def main():
    input_text = open('input.txt', 'r')
    score = 0
    hand_in_ints = []
    for line in input_text.read().split('\n'):
        history  = ints(line)
        next_seq = history
        last_values = [history[-1]]
        ii = 0
        while ii < len(history):
            print(next_seq,'#')
            if sum(next_seq) == 0:
                break
            tmp = []
            for i in range(len(next_seq)-1):
                j = i + 1
                tmp.append(next_seq[j]-next_seq[i])
            if tmp or sum(next_seq) == 0:
                last_values.append(tmp[-1])
                next_seq = [x for x in tmp]
            ii += 1

        if sum(next_seq) == 0:
            score += sum(last_values)


    print('part1:', score)
def main2():
    input_text = open('input.txt', 'r')
    score = 0
    for line in input_text.read().split('\n'):
        pass
        
    print('part2:', score)


main()
main2()