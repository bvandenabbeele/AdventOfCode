import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).parents[2]))

from functions import get_input


def read_input(fp: str):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        return [[int(x) for x in line.strip()] for line in f.readlines()]


def find_highest_number(lst: list[int], length: int) -> int:
    number = 0
    n = length
    i0 = 0

    while n > 0:
        max_i = max(lst[i0:len(lst)-n+1])
        number += max_i * 10**(n-1)

        i0 = lst.index(max_i, i0) + 1
        n -= 1

    return number


def part_i(data: list[list[int]], digits: int) -> int:
    joltage = 0
    for bank in data:
        joltage += find_highest_number(bank, digits)

    return joltage


if __name__ == "__main__":
    get_input(2025, 3)

    data = read_input("input.txt")

    print(f"Part 1:\n{part_i(data, 2)}")
    print(f"Part 2:\n{part_i(data, 12)}")