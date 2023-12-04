from collections import deque


def main():
    p1 = 6
    p2 = 8
    pos = [p1, p2]
    scores = [0, 0]
    turn = 0
    rolls = 0
    q = deque(range(1, 101))

    while scores[0] < 1000 and scores[1] < 1000:
        value = sum(list(q)[:3])
        q.rotate(-3)

        current_pos = ((value + pos[turn]) % 10)
        if current_pos == 0:
            current_pos = 10
        scores[turn] += current_pos
        pos[turn] = current_pos

        rolls += 3
        turn = 1 - turn
    print("RESULT: ", min(scores) * rolls)


if __name__ == "__main__":
    main()