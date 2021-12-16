def main():
    matrix = []
    with open('input.txt') as matrix:
        matrix = [[int(x) for x in list(y)] for y in matrix.read().split("\n")]

    for i, row in enumerate(matrix):
        for j, _ in enumerate(row):
            if i == 0 and j == 0:
                continue
            elif j - 1 < 0:
                matrix[i][j] += matrix[i - 1][j]
            elif i - 1 < 0:
                matrix[i][j] += matrix[i][j - 1]
            else:
                matrix[i][j] += min(matrix[i][j - 1], matrix[i - 1][j])
    # for r in matrix:
    #     print(r)
    print(matrix[len(matrix) - 1][len(matrix) - 1] - matrix[0][0])


if __name__ == "__main__":
    main()