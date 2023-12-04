def main():
    input = []
    with open('input.txt') as input:
        input = [[int(x) for x in y]for y in input.read().split("\n")]
    print(input)



if __name__ == "__main__":
    main()