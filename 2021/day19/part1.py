from dataclasses import dataclass
import math


class Beacon():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.magnitude = math.sqrt(x**2 + y**2 + z**2)
        self.translated = set()

    def translate(self, beacon):
        if not self.translated:
            # generate all 24 possible beacon coordinates
            pass

        return self.translated


@dataclass
class Scanner:
    beacons: list[Beacon]
    deltas: list[float]

    def sort_beacons(self):
        self.beacons.sort(key=lambda x: x.magnitude)

    def calculate_beacon_deltas(self):
        for i in range(len(self.beacons)):
            b = self.beacons[i]
            if i + 1 >= len(self.beacons):
                nb = self.beacons[0]
            else:
                nb = self.beacons[i + 1]
            delta = math.sqrt((b.x - nb.x)**2 + (b.y - nb.y)**2 +
                              (b.z - nb.z)**2)
            self.deltas.append(delta)


def main():
    scanners = []
    with open('input.txt') as matrix:
        s = None
        for row in matrix.read().split("\n"):
            if row.startswith("---"):
                if s:
                    s.sort_beacons()
                    s.calculate_beacon_deltas()
                    scanners.append(s)
                s = Scanner([], [])
            elif row == "":
                continue
            else:
                x, y, z = row.split(',')
                b = Beacon(int(x), int(y), int(z))
                s.beacons.append(b)
    print(scanners)
    for scanner in scanners:
        print("scanner")
        print(scanner.deltas)
        for b in scanner.beacons:
            pass


if __name__ == "__main__":
    main()