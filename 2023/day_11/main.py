import pathlib


class Universe:
    def __init__(self, galaxy_map:list[str]) -> None:
        self.galaxies = dict()
        self.rows = len(galaxy_map)
        self.columns = len(galaxy_map[0])

        cntr = 1

        for i in range(self.rows):
            for j in range(self.columns):
                if galaxy_map[i][j] == "#":
                    self.galaxies[(i, j)] = cntr
                    cntr += 1

    def expand_row(self, index, scale=2):
        for galaxy in self.galaxies.copy().keys():
            if galaxy[0] > index:
                cntr = self.galaxies.pop(galaxy)
                self.galaxies[(galaxy[0] + scale - 1, galaxy[1])] = cntr

        self.rows += scale - 1

    def expand_column(self, index, scale=2):
        for galaxy in self.galaxies.copy().keys():
            if galaxy[1] > index:
                cntr = self.galaxies.pop(galaxy)
                self.galaxies[(galaxy[0], galaxy[1] + scale - 1)] = cntr

        self.columns += scale - 1

    def galaxies_in_row(self, index):
        total = 0
        for galaxy in self.galaxies.keys():
            if galaxy[0] == index:
                total += 1

        return total

    def galaxies_in_column(self, index):
        total = 0
        for galaxy in self.galaxies.keys():
            if galaxy[1] == index:
                total += 1

        return total

    def print_row(self, index, enum=False):
        return "".join([((f"{self.galaxies[(index, j)]}" if enum else "#") if (index, j) in self.galaxies else ".") for j in range(self.columns)])

    def print_column(self, index, enum=False):
        return "".join([((f"{self.galaxies[(i, index)]}" if enum else "#") if (i, index) in self.galaxies else ".") for i in range(self.rows)])

    def __iter__(self):
        for galaxy, cntr in self.galaxies.items():
            yield galaxy, cntr

    def __str__(self):
        return "\n".join([self.print_row(i, enum=True) for i in range(self.rows)])


def read_input(fp):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        return Universe([line.strip("\n") for line in f.readlines()])


def part_1(universe:Universe, scale=1):
    i = 0
    while i < universe.rows:
        if universe.galaxies_in_row(i) == 0:
            universe.expand_row(i, scale)
            i += scale - 1

        i += 1

    j = 0
    while j < universe.columns:
        if universe.galaxies_in_column(j) == 0:
            universe.expand_column(j, scale)
            j += scale - 1

        j += 1

    # print(universe.rows, universe.columns)
    # print(universe)

    distances = dict()
    for g1, v1 in universe:
        for g2, v2 in universe:
            if v2 <= v1:
                continue

            distances[(v1, v2)] = abs(g2[0] - g1[0]) + abs(g2[1] - g1[1])
            # print(f"{v1} -> {v2} = {distances[((v1, v2))]}")

    return sum(distances.values())


def part_2(universe:Universe):
    return part_1(universe, scale=1000000)


if __name__ == "__main__":
    fp = "input.txt"

    print(f"Part 1:\n{part_1(read_input(fp))}")
    print(f"Part 2:\n{part_2(read_input(fp))}")
