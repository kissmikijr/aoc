def main():
    with open('input.txt') as nodes:
        for n in nodes.read().splitlines():
            print(n)


if __name__ == "__main__":
    main()