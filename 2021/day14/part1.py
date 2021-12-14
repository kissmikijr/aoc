from collections import Counter


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
    while step > 0:
        print(step)
        new_template = ""
        for i, c in enumerate(template):
            new_template += c
            if i + 1 >= len(template):
                break
            try:
                new_template += mapping[template[i:i + 2]]
            except KeyError:
                continue
        template = new_template
        step -= 1

    c = Counter(template)
    print(c[max(c, key=c.get)] - c[min(c, key=c.get)])
    # print(template)


if __name__ == "__main__":
    main()