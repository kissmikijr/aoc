def fold_x(paper, x):
    half = [row[x + 1:] for row in paper]
    new_paper = [row[:x] for row in paper]

    for i, row in enumerate(half):
        row = reversed(row)
        for j, s in enumerate(row):
            if s == "#":
                new_paper[i][j] = s

    return new_paper


def fold_y(paper, y):
    new_paper = paper[:y]

    half = paper[y + 1:]
    half = reversed(half)
    for i, row in enumerate(half):
        for j, s in enumerate(row):
            if s == "#":
                new_paper[i][j] = s
    return new_paper


def main():
    matrix = []
    with open('input.txt') as matrix:
        matrix = [[int(x) for x in y.split(",")]
                  for y in matrix.read().split("\n")]
    x_max, y_max = max(matrix, key=lambda a: a[0])[0] + 1, max(
        matrix, key=lambda a: a[1])[1] + 2
    paper = [[" "] * x_max] * y_max
    paper = [row[:] for row in paper]

    print(x_max, y_max)
    print(len(paper), len(paper[0]))
    for row in matrix:
        x, y = row[0], row[1]
        paper[y][x] = "#"

    new_paper = fold_x(paper, 655)
    new_paper = fold_y(new_paper, 447)
    new_paper = fold_x(new_paper, 327)
    new_paper = fold_y(new_paper, 223)
    new_paper = fold_x(new_paper, 163)
    new_paper = fold_y(new_paper, 111)
    new_paper = fold_x(new_paper, 81)
    new_paper = fold_y(new_paper, 55)
    new_paper = fold_x(new_paper, 40)
    new_paper = fold_y(new_paper, 27)
    new_paper = fold_y(new_paper, 13)
    new_paper = fold_y(new_paper, 6)
    print(
        "------------------------------------------------------------------------------------------------"
    )
    for x in new_paper:
        print(" ".join(x))


def count_hashtags(paper):
    hashtags = 0
    for x in paper:
        for p in x:
            if p == "#":
                hashtags += 1
    return hashtags


if __name__ == "__main__":
    main()