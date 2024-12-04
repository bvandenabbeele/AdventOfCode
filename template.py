import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).parents[2]))

from functions import get_input


def read_input(fp: str):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        pass


def part_1(data):
    pass


def part_2(data):
    pass


if __name__ == "__main__":
    get_input(2024, 1)

    data = read_input("input.txt")

    print(f"Part 1:\n{part_1(data)}")
    print(f"Part 2:\n{part_2(data)}")