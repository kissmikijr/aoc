from itertools import product


class Instruction():
    def __init__(self, on=None, x=None, y=None, z=None):
        self.on = on
        self.x = x
        self.y = y
        self.z = z


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
                    if int(start) < -50 or int(finish) > 50:
                        continue
                    x = (int(start), int(finish))
                    instruction.x = x
                elif c.startswith("y"):
                    start, finish = c[2:].split("..")

                    if int(start) < -50 or int(finish) > 50:
                        continue
                    y = (int(start), int(finish))
                    instruction.y = y
                elif c.startswith("z"):
                    start, finish = c[2:].split("..")
                    if int(start) < -50 or int(finish) > 50:
                        continue
                    z = (int(start), int(finish))
                    instruction.z = z
            if instruction.x:
                instructions.append(instruction)
    result = set()
    for instruction in instructions:
        x_possibilities = [
            x for x in range(instruction.x[0], instruction.x[1] + 1)
        ]
        y_possibilities = [
            x for x in range(instruction.y[0], instruction.y[1] + 1)
        ]
        z_possibilities = [
            x for x in range(instruction.z[0], instruction.z[1] + 1)
        ]
        all_cubes = product(x_possibilities, y_possibilities, z_possibilities)
        if instruction.on:
            result.update(all_cubes)
        elif not instruction.on:
            for cube in all_cubes:
                if cube in result:
                    result.remove(cube)
    print(len(result))


if __name__ == "__main__":
    main()