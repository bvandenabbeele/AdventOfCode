import pathlib


def read_file(fp):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        raw = f.readlines()

    data = [[[int(x) for x in r2.split("-")] for r2 in r.strip("\n").split(",")] for r in raw]
    return data


def contained_in(p1, p2):
    return (p1[0] <= p2[0]) and (p2[1] <= p1[1])


def contained_either_way(p1, p2):
    return contained_in(p1, p2) or (contained_in(p2, p1))


def part_1(data):
    cntr = 0
    for p1, p2 in data:
        if contained_either_way(p1, p2):
            cntr += 1

    return cntr


def overlap_one(p1, p2):
    return (p1[0] <= p2[0] <= p1[1]) or (p1[0] <= p2[1] <= p1[1])


def overlap(p1, p2):
    return overlap_one(p1, p2) or overlap_one(p2, p1)


def part_2(data):
    cntr = 0
    for p1, p2 in data:
        if overlap(p1, p2):
            cntr += 1

    return cntr


if __name__ == "__main__":
    data = read_file("input.txt")
    print(f"Part 1:\n{part_1(data)}")
    print(f"Part 2:\n{part_2(data)}")