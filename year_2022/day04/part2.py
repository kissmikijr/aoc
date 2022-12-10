import string

def main():
    input_text = open('input.txt', 'r')
    lines = input_text.read().split(
        '\n'
    )
    contains = 0
    for line in lines:
        left, right = line.split(',')

        # left 6-6
        # right 4-6
        # left 2-6
        # right 4-8
        l1, l2 = left.split('-')
        r1, r2 = right.split('-')

        left1 = int(l1)
        left2 = int(l2)
        right1 = int(r1)
        right2 = int(r2)

        if (right1 >= left1 and right1 <= left2) or (left1 >= right1 and left1 <= right2):
            contains += 1
    print(contains)

main()