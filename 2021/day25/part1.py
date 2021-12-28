from copy import deepcopy


def print_grid(grid):
    print("----------------------")
    for r in grid:
        print(" ".join(r))


def main():
    matrix = []
    with open('input.txt') as matrix:
        matrix = [[x for x in y] for y in matrix.read().split("\n")]

    step = 0
    moved = True
    while True:
        if moved == False:
            break
        tmp = deepcopy(matrix)
        moved = False
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                curr = matrix[row][col]
                if curr == ">":
                    if col + 1 >= len(matrix[row]):
                        next_col_index = 0
                    else:
                        next_col_index = col + 1
                    if matrix[row][next_col_index] == ".":
                        tmp[row][col] = "."
                        tmp[row][next_col_index] = ">"
                        moved = True

        matrix = deepcopy(tmp)
        tmp = deepcopy(matrix)
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                curr = matrix[row][col]
                if curr == "v":
                    if row + 1 >= len(matrix):
                        next_row_index = 0
                    else:
                        next_row_index = row + 1
                    if matrix[next_row_index][col] == ".":
                        tmp[row][col] = "."
                        tmp[next_row_index][col] = "v"
                        moved = True

        matrix = deepcopy(tmp)

        step += 1
    print(step)


if __name__ == "__main__":
    main()