import pathlib


def read_file(fp):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        raw = f.readlines()

    data = [r.strip("\n") for r in raw]
    return data


def intersect(*sets):
    for item in sets[0]:
        common = True
        for set_i in sets[1::]:
            common = common and (item in set_i)

        if common:
            return item


def get_priority(item):
    if item.islower():
        # a = 1
        return ord(item) - 96

    elif item.isupper():
        # A = 27
        return ord(item) - 38


def part_1(data):
    priority = 0
    for rucksack in data:
        size = len(rucksack)
        comp1, comp2 = rucksack[:size//2], rucksack[size//2::]
        common = intersect(comp1, comp2)
        priority += get_priority(common)

    return priority


def part_2(data):
    priority = 0
    for i in range(0, len(data), 3):
        r1, r2, r3 = data[i], data[i+1], data[i+2]
        common = intersect(r1, r2, r3)
        p = get_priority(common)
        priority += p

    return priority


if __name__ == "__main__":
    data = read_file("input.txt")
    print(f"Part 1:\n{part_1(data)}")
    print(f"Part 2:\n{part_2(data)}")