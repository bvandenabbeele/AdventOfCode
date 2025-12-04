import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).parents[2]))

from functions import get_input


def read_input(fp: str) -> list[int]:
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        raw = [(line[0], int(line[1::].strip("\n"))) for line in f.readlines()]

    data = list()
    for rot in raw:
        if rot[0] == "R":
            data.append(rot[1])
        elif rot[0] == "L":
            data.append(-rot[1])
        else:
            raise ValueError(f"Unexpected data: {rot[0]}")

    return data


def part_1(data: list[int]) -> int:
    x = 50
    zeros = 0
    for y in data:
        x = (x + y)%100
        if x == 0:
            zeros += 1

    return zeros


def part_2(data: list[int]) -> int:
    x = 50
    zeros = 0
    for y in data:
        # means x > y
        # if y negative, never a crossover
        if x + y > 0:
            zeros += (x+y)//100
        # means x < y and y negative
        # if x == -y after rotation i, and y < 0 for rotation i + 1, crossover is counted twice.
        # hence the if statement
        else:
            zeros += abs(x+y)//100 + (1 if x != 0 else 0)

        x = (x + y)%100

    return zeros

if __name__ == "__main__":
    get_input(2025, 1)

    data = read_input("input.txt")

    print(f"Part 1:\n{part_1(data)}")
    print(f"Part 2:\n{part_2(data)}")