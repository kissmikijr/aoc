import subprocess
# import ../../utils

def part1(input: str):
    lines = input.split('\n')
    zero = 26
    result = set()
    result.add((zero, zero))
    rope = [
        [zero, zero],
        [zero, zero],
        [zero, zero],
        [zero, zero],
        [zero, zero],
        [zero, zero],
        [zero, zero],
        [zero, zero],
        [zero, zero],
        [zero, zero],
    ] 
    for line in lines:
        direction, amount = line.split(' ')
        step = 0

        while step < int(amount):
            # head moves
            head = rope[0]
            if direction == 'R':
                head[1] += 1
            elif direction == 'L':
                head[1] -= 1
            elif direction == 'U':
                head[0] -= 1
            elif direction == 'D':
                head[0] += 1

            for i in range(len(rope)-1):
                tail = rope[i+1]
                head = rope[i]


                if should_tail_move(head, tail):
                    if is_diagonal_move(head, tail):
                        if touching(head, [tail[0]+1, tail[1]+1]):
                            tail[0] += 1
                            tail[1] += 1
                        elif touching(head, [tail[0]+1, tail[1]-1]):
                            tail[0] += 1
                            tail[1] -= 1
                        elif touching(head, [tail[0]-1, tail[1]-1]):
                            tail[0] -= 1
                            tail[1] -= 1
                        elif touching(head, [tail[0]-1, tail[1]+1]):
                            tail[0] -= 1
                            tail[1] += 1

                    elif direction == 'R':
                        tail[1] += 1
                    elif direction == 'L':
                        tail[1] -= 1
                    elif direction == 'U':
                        tail[0] -= 1
                    elif direction == 'D':
                        tail[0] += 1

            result.add(tuple(rope[-1]))

            step += 1

    print('Part1: ',len(result))
    return str(len(result))

def is_diagonal_move(H,T):
    if touching(H,T):
        return False
    elif H[1] == T[1]:
        # same row: (0, 0), (3, 0)
        return False
    elif H[0] == T[0]:
        # same col: (0, 0), (0, 3)
        return False
    return True

def touching(H,T):
    if abs(H[0] - T[0]) <= 1 and abs(H[1] - T[1]) <= 1:
        return True
    return False

def should_tail_move(H, T):
    # same row: (0, 0), (3, 0)
    if abs(H[0] - T[0]) >= 2 or abs(H[1]-T[1]) >= 2:
        return True

    return False

def part2(input: str):
    i = 1
    grid = [[x for x in y] for y in input.split("\n")]
    result = None

    print("Part2: ", result)
    return result


def main():
    input_text = open('input-test.txt', 'r')
    input: str = input_text.read()

    result = part2(input)
    if not result:
        result = part1(input)


    subprocess.run(['pbcopy'], input=str(result).encode('utf-8'))
main()