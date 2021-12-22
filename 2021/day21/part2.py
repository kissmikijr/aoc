from itertools import product
from functools import lru_cache

cache = {}


@lru_cache(None)
def roll(scores, pos, turn):
    wins = [0, 0]
    current_pos = [x for x in pos]
    current_scores = [x for x in scores]

    for first, second, third in product((1, 2, 3), (1, 2, 3), (1, 2, 3)):
        value = first + second + third

        current_pos[turn] = ((value + pos[turn]) % 10)
        if current_pos[turn] == 0:
            current_pos[turn] = 10

        current_scores[turn] = scores[turn] + current_pos[turn]

        if current_scores[turn] >= 21:
            wins[turn] += 1
        else:
            p1, p2 = roll((current_scores[0], current_scores[1]),
                          (current_pos[0], current_pos[1]), 1 - turn)
            wins[0] += p1
            wins[1] += p2
    return wins


def main():
    p1 = 6
    p2 = 8
    result = roll((0, 0), (p1, p2), 0)

    print("RESULT: ", max(result))


if __name__ == "__main__":
    main()