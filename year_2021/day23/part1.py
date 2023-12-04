def print_grid(grid):
    for r in grid:
        print(" ".join(r))


class Amphipod():
    def __init__(self, letter, x, y, home):
        self.letter = letter
        self.x = x
        self.y = y
        self.home = home


def amphipod_factory(letter, x, y):

    homes = {
        "A": ((3, 2), (3, 3)),
        "B": ((5, 2), (5, 3)),
        "C": ((7, 2), (7, 3)),
        "D": ((9, 2), (9, 3))
    }
    return Amphipod(letter, x, y, homes[letter])


def main():
    weights = {"A": 1, "B": 10, "C": 100, "D": 1000}
    board = [["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
             ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
             ["#", "#", "#", "A", "#", "D", "#", "B", "#", "D", "#", "#", "#"],
             ["#", "#", "#", "B", "#", "C", "#", "A", "#", "C", "#", "#", "#"],
             ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]]
    print_grid(board)
    amphipods = [
        amphipod_factory("A", 4, 2),
        amphipod_factory("B", 4, 3),
        amphipod_factory("D", 5, 2),
        amphipod_factory("C", 5, 3),
        amphipod_factory("B", 7, 2),
        amphipod_factory("A", 7, 3),
        amphipod_factory("D", 9, 2),
        amphipod_factory("C", 9, 3),
    ]


if __name__ == "__main__":
    main()