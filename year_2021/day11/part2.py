def flash(i, j, matrix, flashes, flashed):
    if matrix[i][j] > 9:
        if (i, j) in flashed:
            return flashes
        matrix[i][j] = 0
        flashes += 1
        flashed.add((i, j))

        if i - 1 >= 0:
            matrix[i - 1][j] += 1
            flashes = flash(i - 1, j, matrix, flashes, flashed)

            if j - 1 >= 0:
                matrix[i - 1][j - 1] += 1
                flashes = flash(i - 1, j - 1, matrix, flashes, flashed)

            if j + 1 < len(matrix):
                matrix[i - 1][j + 1] += 1
                flashes = flash(i - 1, j + 1, matrix, flashes, flashed)

        if i + 1 < len(matrix):
            matrix[i + 1][j] += 1
            flashes = flash(i + 1, j, matrix, flashes, flashed)

            if j + 1 < len(matrix):
                matrix[i + 1][j + 1] += 1
                flashes = flash(i + 1, j + 1, matrix, flashes, flashed)
            if j - 1 >= 0:
                matrix[i + 1][j - 1] += 1
                flashes = flash(i + 1, j - 1, matrix, flashes, flashed)

        if j - 1 >= 0:
            matrix[i][j - 1] += 1
            flashes = flash(i, j - 1, matrix, flashes, flashed)

        if j + 1 < len(matrix):
            matrix[i][j + 1] += 1
            flashes = flash(i, j + 1, matrix, flashes, flashed)
    return flashes


def main():
    matrix = []
    with open('input.txt') as matrix:
        matrix = [[int(x) for x in y] for y in matrix.read().split("\n")]
    step = 0
    max_step = 300
    flashes = 0
    while (step < max_step):
        flashed = set()
        for i, row in enumerate(matrix):
            for j, _ in enumerate(row):
                matrix[i][j] += 1

        for i, row in enumerate(matrix):
            for j, _ in enumerate(row):
                flashes = flash(i, j, matrix, flashes, flashed)
        for i, j in flashed:
            matrix[i][j] = 0

        step += 1

        if len(flashed) == 100:
            print("STEP: ", step + 1)
            break


if __name__ == "__main__":
    main()