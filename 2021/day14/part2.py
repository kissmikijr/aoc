from collections import Counter, defaultdict


def main():
    matrix = []
    template = "VCOPVNKPFOOVPVSBKCOF"
    with open('input.txt') as matrix:
        matrix = [y for y in matrix.read().split("\n")]
    mapping = {}
    for x in matrix:
        l, r = x.split(" -> ")
        mapping[l] = r

    step = 40
    pairs = defaultdict(int)

    counter = defaultdict(int)
    for i, c in enumerate(template):
        counter[template[i]] += 1
        if i + 1 >= len(template):
            break
        try:
            pairs[template[i:i + 2]] += 1
        except KeyError:
            continue

    while step > 0:
        tmp = pairs.copy()
        for k in tmp.keys():
            counter[mapping[k]] += 1 * tmp[k]
            pairs[k[0] + mapping[k]] += 1 * tmp[k]
            pairs[mapping[k] + k[1]] += 1 * tmp[k]
            pairs[k] -= 1 * tmp[k]

        step -= 1

    print(counter[max(counter, key=counter.get)] -
          counter[min(counter, key=counter.get)])


if __name__ == "__main__":
    main()