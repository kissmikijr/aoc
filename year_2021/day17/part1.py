import numpy as np


def main():
    x1, x2 = 56, 76
    y1, y2 = -162, -134
    target_area = set()

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            target_area.add((i, j))
    paths = []

    for x in range(9, 77):
        for y in range(9, 200):
            vel_x, vel_y = x, y
            coord_x, coord_y = 0, 0
            path = [(coord_x, coord_y)]
            while True:
                if (coord_x, coord_y) in target_area:
                    paths.append(path)
                    break
                if coord_y < y2:
                    break
                coord_x += vel_x
                coord_y += vel_y

                path.append((coord_x, coord_y))
                if vel_x > 0:
                    vel_x -= 1
                elif vel_x < 0:
                    vel_x += 1
                else:
                    vel_x = 0
                vel_y -= 1
    # print(paths)
    max_y = 0
    for p in paths:
        my = max(p, key=lambda x: x[1])
        if my[1] > max_y:
            max_y = my[1]
    print(max_y)


if __name__ == "__main__":
    main()