import pathlib


def read_input(fp) -> tuple[list[int], dict[str, list[str]]]:
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        directions = f.readline().strip("\n").replace("L", "0").replace("R", "1")
        directions = [int(x) for x in directions]
        f.readline()
        mapping = dict()
        for line in f.readlines():
            o, d = line.strip("\n").split(" = ")
            mapping[o] = d.lstrip("(").rstrip(")").split(", ")

    return directions, mapping


def part_1(directions: list[int], mapping: dict[str, list[str]]):
    len_d = len(directions)
    done = False
    i = 0
    pos = "AAA"
    while not done:
        pos = mapping[pos][directions[i%len_d]]
        i += 1
        if pos == "ZZZ":
            done = True
            return i


def part_2(directions: list[int], mapping: dict[str, list[str]]):
    len_d = len(directions)
    done = False
    i = 0
    pos = [p for p in mapping.keys() if p[-1] == "A"]
    while not done:
        for j in range(len(pos)):
            pos[j] = mapping[pos[j]][directions[i%len_d]]
        i += 1
        print(f"\r{i} {pos}", end="")
        done = all([p[-1] == "Z" for p in pos])

    return i


if __name__ == "__main__":
    directions, mapping = read_input("input.txt")
    # print(f"Part 1:\n{part_1(directions, mapping)}")
    print(f"Part 2:\n{part_2(directions, mapping)}")
