from dataclasses import dataclass


class Instruction():
    def __init__(self, on=None, x=None, y=None, z=None):
        self.on = on
        self.x = x
        self.y = y
        self.z = z


@dataclass
class Cube():
    x1: int
    x2: int
    y1: int
    y2: int
    z1: int
    z2: int

    def is_overlap(self, cube):
        if self.x1 > cube.x2 or self.x2 < cube.x1 or self.y2 < cube.y1 or self.y1 > cube.y2 or self.z1 > cube.z2 or self.z2 < cube.z1:
            return False
        return True

    def volume(self):
        return (self.x2 - self.x1 + 1) * (self.y2 - self.y1 +
                                          1) * (self.z2 - self.z1 + 1)


def main():
    instructions = []
    with open('input.txt') as matrix:
        rows = [y for y in matrix.read().split("\n")]
        for row in rows:
            instruction = Instruction()
            coords = []
            if row.startswith("on "):
                isOn = True
                coords = row[3:].split(",")
                instruction.on = isOn
            elif row.startswith("off "):
                isOn = False
                coords = row[4:].split(",")
                instruction.on = isOn
            for c in coords:
                if c.startswith("x"):
                    start, finish = c[2:].split("..")

                    x = (int(start), int(finish))
                    instruction.x = x
                elif c.startswith("y"):
                    start, finish = c[2:].split("..")

                    y = (int(start), int(finish))
                    instruction.y = y
                elif c.startswith("z"):
                    start, finish = c[2:].split("..")

                    z = (int(start), int(finish))
                    instruction.z = z
            if instruction.x:
                instructions.append(instruction)

    cubes = []
    for instruction in instructions:
        new_cube = Cube(
            min(instruction.x),
            max(instruction.x),
            min(instruction.y),
            max(instruction.y),
            min(instruction.z),
            max(instruction.z),
        )
        for i in range(len(cubes)):
            cube = cubes[i]
            if not cube.is_overlap(new_cube):
                continue
            cubes[i] = None
            if new_cube.x1 > cube.x1:
                cubes.append(
                    Cube(cube.x1, new_cube.x1 - 1, cube.y1, cube.y2, cube.z1,
                         cube.z2))
            if new_cube.x2 < cube.x2:
                cubes.append(
                    Cube(new_cube.x2 + 1, cube.x2, cube.y1, cube.y2, cube.z1,
                         cube.z2))

            if new_cube.y1 > cube.y1:
                cubes.append(
                    Cube(max(cube.x1, new_cube.x1), min(cube.x2, new_cube.x2),
                         cube.y1, new_cube.y1 - 1, cube.z1, cube.z2))

            if new_cube.y2 < cube.y2:
                cubes.append(
                    Cube(max(cube.x1, new_cube.x1), min(cube.x2, new_cube.x2),
                         new_cube.y2 + 1, cube.y2, cube.z1, cube.z2))

            if new_cube.z1 > cube.z1:
                cubes.append(
                    Cube(max(cube.x1, new_cube.x1), min(cube.x2, new_cube.x2),
                         max(new_cube.y1, cube.y1), min(new_cube.y2, cube.y2),
                         cube.z1, new_cube.z1 - 1))

            if new_cube.z2 < cube.z2:
                cubes.append(
                    Cube(max(cube.x1, new_cube.x1), min(cube.x2, new_cube.x2),
                         max(new_cube.y1, cube.y1), min(new_cube.y2, cube.y2),
                         new_cube.z2 + 1, cube.z2))
        if instruction.on:
            cubes.append(new_cube)
        cubes = [x for x in cubes if x is not None]

    result = 0
    for c in cubes:
        result += c.volume()
    print(result)


if __name__ == "__main__":
    main()