def main():
    matrix = []
    with open('input.txt') as matrix:
        matrix = [y for y in matrix.read().split("\n")]

    print(matrix)


if __name__ == "__main__":
    main()