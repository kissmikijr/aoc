import re
from collections import Counter

def ints(input: str):
    return [int(x) for x in re.findall(r'-?\d+', input)]


values = {
    '2':2,
    '3':3,
    '4': 4,
    '5':5,
    '6': 6,
    '7':7,
    '8':8,
    '9':9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

def hand_type(hand):
    counts = Counter(hand)
    is_full_house = False
    two_pair = False
    rank = 0
    for card, count in sorted(counts.items(), key= lambda x: x[1], reverse=True):
        if rank > 0:
            break
        if is_full_house:
            # full house
            if count == 2:
                rank = 5
            # three of a kind
            else:
                rank = 4
        elif two_pair == True:
            # two pair
            if count == 2:
                rank = 3
            # one pair
            elif count == 1:
                rank = 2
        # Five of a kind
        elif count == 5:
            rank = 7
        # Five four of a kind
        elif count == 4:
            rank = 6
        elif count == 3:
            is_full_house = True
        elif count == 2:
            two_pair = True
        #high card
        elif count == 1:
            rank = 1
    return rank






def main():
    input_text = open('input.txt', 'r')
    score = 0
    hand_in_ints = []
    for line in input_text.read().split('\n'):
        hand, bid = line.split(' ')
        tmp = []
        for c in hand:
            tmp.append(values[c])
        hand_in_ints.append([tmp, bid])
    sorted_hands = sorted(hand_in_ints, key=lambda x: (hand_type(x[0]), x[0][0], x[0][1], x[0][2], x[0][3], x[0][4]))
    for i, hand in enumerate(sorted_hands):
        score += int(hand[1]) * (i+1)


    print('part1:', score)

values2 = {
    '2':2,
    '3':3,
    '4': 4,
    '5':5,
    '6': 6,
    '7':7,
    '8':8,
    '9':9,
    'T': 10,
    'J': 1,
    'Q': 12,
    'K': 13,
    'A': 14
}


def hand_type2(hand):
    counts = Counter(hand)
    jokers = 0
    if 1 in hand:
        jokers = counts[1]
        counts.pop(1)

    if jokers == 5:
        return 7

    counts_tuple = sorted(counts.items(), key= lambda x: x[1], reverse=True)
    counts_list = [list(x) for x in counts_tuple]
    counts_list[0][1] += jokers

    is_full_house = False
    two_pair = False
    rank = 0
    for card, count in counts_list:
        if rank > 0:
            break
        if is_full_house:
            # full house
            if count == 2:
                rank = 5
            # three of a kind
            else:
                rank = 4
        elif two_pair == True:
            # two pair
            if count == 2:
                rank = 3
            # one pair
            elif count == 1:
                rank = 2
        # Five of a kind
        elif count == 5:
            rank = 7
        # Five four of a kind
        elif count == 4:
            rank = 6
        elif count == 3:
            is_full_house = True
        elif count == 2:
            two_pair = True
        #high card
        elif count == 1:
            rank = 1
    return rank

def main2():
    input_text = open('input.txt', 'r')
    score = 0
    hand_in_ints = []
    for line in input_text.read().split('\n'):
        hand, bid = line.split(' ')
        tmp = []
        for c in hand:
            tmp.append(values2[c])
        hand_in_ints.append([tmp, bid])
    sorted_hands = sorted(hand_in_ints, key=lambda x: (hand_type2(x[0]), x[0][0], x[0][1], x[0][2], x[0][3], x[0][4]))
    for i, hand in enumerate(sorted_hands):
        score += int(hand[1]) * (i+1)

    print('part2:', score)


main()
main2()