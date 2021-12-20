def print_grid(grid):
    print("----------------------")
    for r in grid:
        print(" ".join(r))


def enhance(image, row, j):
    enhancement_algo = "#..##..#.#.#.###.#..##.####..##..##.##.#.###.......##..#..#.#.#.#..#...##....#.#.##.###....###.#.##.##..##.#...##.##...#...##......##.#...#.......##.#.#..####.##..#.#.#.....##.....#....#.#.#.##..##..##.##.....###...#.#..###.#######.#.....###....#......#.###.#...#.#####.#.#.###..#...##.##.#..#...######.###.#.##...####..####.###...####........##...##.##.####...##.#.#...##.#####.#....#.....##..#......###..###.#.#..###..#.####......#.....#.#.#.###..#.#..#..#...##..##..#.##....#....#.##..###..#....##.##..#.###.."

    binary = [
        image[row - 1][j - 1], image[row - 1][j], image[row - 1][j + 1],
        image[row][j - 1], image[row][j], image[row][j + 1],
        image[row + 1][j - 1], image[row + 1][j], image[row + 1][j + 1]
    ]
    number = int("".join(binary).replace(".", "0").replace("#", "1"), 2)
    return enhancement_algo[number]


def extend_matrix(image, times, i):
    image = [[x for x in y] for y in image]
    pixel_to_extend = "#" if i % 2 == 0 else "."
    for _ in range(times):
        start_image = []
        for x in image:
            x.insert(0, pixel_to_extend)
            x.append(pixel_to_extend)
            start_image.append(x)

        black_row = [pixel_to_extend] * (len(image[0]))
        start_image.insert(0, black_row)
        start_image.append(black_row)
        image = [[x for x in y] for y in start_image]
    return image


def main():
    image = []
    with open('input.txt') as matrix:
        image = [[x for x in y] for y in matrix.read().split("\n")]

    for i in range(1, 3):
        image = extend_matrix(image, 1, i)
        enhanced_image = [[x for x in y] for y in image]
        extended_image = extend_matrix(enhanced_image, 1, i)
        for row in range(len(image)):
            for j in range(len(image[0])):
                enhanced_pixel = enhance(extended_image, row + 1, j + 1)
                enhanced_image[row][j] = enhanced_pixel
        image = [[x for x in y] for y in enhanced_image]

    light_pixels = 0
    for row in range(len(image)):
        for j in range(len(image[0])):
            if image[row][j] == "#":
                light_pixels += 1
    print(light_pixels)


if __name__ == "__main__":
    main()