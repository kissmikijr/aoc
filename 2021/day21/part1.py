def print_grid(grid):
    print("----------------------")
    for r in grid:
        print(" ".join(r))


def main():
    matrix = []
    with open('input.txt') as matrix:
        matrix = [[x for x in y] for y in matrix.read().split("\n")]

    print(matrix)


if __name__ == "__main__":
    main()