import pathlib


def read_input(path):
    lst1, lst2 = list(), list()

    with open(pathlib.Path(__file__).parent / path, "r") as f:
        for line in f.readlines():
            n1, n2 = line.strip().split("  ")
            n1, n2 = int(n1), int(n2)

            if len(lst1) == 0:
                lst1.append(n1)
                lst2.append(n2)

            else:
                put_in_list(lst1, n1)
                put_in_list(lst2, n2)

    return lst1, lst2


def put_in_list(lst: list, n: int):
    i = 0
    done = False
    while not done:
        if i == len(lst):
            done = True
            continue

        if n < lst[i]:
            done = True
            continue

        i += 1

    lst.insert(i, n)


def part_1(lst1, lst2):
    total = 0
    for n1, n2 in zip(lst1, lst2):
        total += abs(n1 - n2)

    return total


def part_2(lst1: list, lst2: list):
    total = 0
    for n in lst1:
        total += n * lst2.count(n)

    return total


if __name__ == "__main__":
    lst1, lst2 = read_input("input.txt")

    print(f"Part 1:\n{part_1(lst1, lst2)}")
    print(f"Part 2:\n{part_2(lst1, lst2)}")
