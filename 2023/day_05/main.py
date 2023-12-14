import pathlib


class Mapping:
    def __init__(self, source:str, destination:str, mapping:list[list[int]]) -> None:
        self.source = source
        self.destination = destination
        self.mapping = mapping

    def __str__(self) -> str:
        return f"{self.source}->{self.destination}\n{self.mapping}"

    def get_mapped_value_part_1(self, value):
        for map_i in self.mapping:
            if map_i[1] <= value < map_i[1] + map_i[2]:
                diff = value - map_i[1]
                return map_i[0] + diff

        return value

    def get_mapped_value_part_2(self, ss:int, sr:int) -> list[tuple[int]]:
        for m in self.mapping:
            if m[1] <= ss and ss + sr <= m[1] + m[2]:
                return [(m[0] + ss - m[1], sr)]

            elif ss < m[1] and m[1] < ss + sr <= m[1] + m[2]:
                return [
                    (ss, m[1] - ss),
                    (m[0], ss + sr - m[1])
                ]

            elif m[1] <= ss < m[1] + m[2] and m[1] + m[2] < ss + sr:
                return [
                    (m[0] + ss - m[1], m[1] + m[2] - ss),
                    (m[1] + m[2], ss + sr - m[1] - m[2])
                ]

            elif ss < m[1] and m[1] + m[2] < ss + sr:
                return [
                    (ss, m[1] - ss),
                    (m[0], m[2]),
                    (m[1] + m[2], ss + sr - m[1] - m[2])
                ]

        return [(ss, sr)]

def read_input(fp):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        seeds = [int(x) for x in f.readline().lstrip("seeds: ").rstrip("\n").split(" ")]
        f.readline()
        maps = dict()
        map_i = list()

        done = False
        while not done:
            line = f.readline()
            try:
                if line[0].isalpha():
                    source, destination = line.strip(" map:\n").split("-to-")

                elif line[0].isdigit():
                    map_i.append(tuple([int(x) for x in line.strip("\n").split(" ")]))

                else:
                    maps[source] = Mapping(source, destination, map_i.copy())
                    map_i.clear()

            except IndexError:
                done = True
                maps[source] = Mapping(source, destination, map_i.copy())

    return seeds, maps


def part_1(seeds: list[int], maps: dict[str, Mapping]):
    locations = list()
    for value in seeds:
        source = "seed"
        done = False
        while not done:
            mapping = maps[source]
            value = mapping.get_mapped_value_part_1(value)
            source = mapping.destination

            done = (source == "location")

        locations.append(value)

    return min(locations)


def part_2(seeds: list[int], maps: dict[str, Mapping]):
    seed_ranges = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]

    done = False
    source = "seed"
    while not done:
        mapping = maps[source]

        new_ranges = list()
        for ss, sr in seed_ranges:
            new_ranges += mapping.get_mapped_value_part_2(ss, sr)

        source = mapping.destination
        seed_ranges = new_ranges.copy()
        done = (source == "location")

    return min([s[0] for s in seed_ranges])


if __name__ == "__main__":
    seeds, maps = read_input("input.txt")
    print(f"Part 1:\n{part_1(seeds, maps)}")
    print(f"Part 2:\n{part_2(seeds, maps)}")
