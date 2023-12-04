from copy import deepcopy


def main():
    matrix = []
    with open('input.txt') as matrix:
        matrix = [[int(x) for x in y.split(",")]
                  for y in matrix.read().split("\n")]
    x_max, y_max = max(matrix, key=lambda a: a[0])[0] + 1, max(
        matrix, key=lambda a: a[1])[1] + 1
    paper = [["."] * x_max] * y_max
    paper = [row[:] for row in paper]

    for row in matrix:
        x, y = row[0], row[1]
        paper[y][x] = "#"

    # fold_y = 7
    # new_paper = paper[:fold_y]
    # half = paper[fold_y + 1:]
    # for i, row in enumerate(reversed(half)):
    #     for j, s in enumerate(row):
    #         if s == "#":
    #             new_paper[i][j] = s

    fold_x = 655
    new_paper = paper
    half = [row[fold_x + 1:] for row in new_paper]
    new_paper = [row[:fold_x] for row in new_paper]
    for i, row in enumerate(half):
        for j, s in enumerate(reversed(row)):
            if s == "#":
                new_paper[i][j] = s
    result = 0
    for row in new_paper:
        for x in row:
            if x == "#":
                result += 1
    # print(new_paper)
    print(result)


if __name__ == "__main__":
    main()