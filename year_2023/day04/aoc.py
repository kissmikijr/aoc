import re
from collections import defaultdict

def ints(input: str):
    return [int(x) for x in re.findall(r'-?\d+', input)]


def main():
    input_text = open('input.txt', 'r')
    score = 0
    for line in input_text.read().split('\n'):
        a = line.split(':')
        winning = a[1].split('|')[0]
        mine = a[1].split('|')[1]
        w = ints(winning)
        m = ints(mine)
        power = 0
        s = 0
        for i in range(len(m)):
            if m[i] in w:
                s = pow(2, power)
                power+=1
        score += s
    print('part1:', score)

def main2():
    input_text = open('input.txt', 'r')
    score = 0
    scratch_cards = []
    idx = 1
    for line in input_text.read().split('\n'):
        a = line.split(':')
        winning = a[1].split('|')[0]
        mine = a[1].split('|')[1]
        scratch_cards.append((idx, ints(winning), ints(mine)))
        idx += 1

    copies = defaultdict(lambda: 1)
    for cards in scratch_cards:
        card_id, w, m = cards
        c = 1
        for ii in range(len(m)):
            if m[ii] in w: 
                copies[card_id+c] += 1*copies[card_id]
                c += 1

    for cards in scratch_cards:
        idx, _,_ = cards
        score += copies[idx]

    print('part2:', score)


main()
main2()