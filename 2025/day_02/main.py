import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).parents[2]))

from functions import get_input


def read_input(fp: str) -> list[list[int]]:
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        return [[int(x) for x in id_range.split("-")] for id_range in f.read().strip("\n").split(",")]


def part_1(data: list[list[int]]) -> int:
    invalid = 0
    for id0, id1 in data:
        str_id0 = str(id0)
        str_id1 = str(id1)

        # make sure we start below id0 and end above id1 (in terms of length)
        repeat_id0 = len(str_id0)//2
        repeat_id1 = len(str_id1)//2 + len(str_id1)%2

        for x in range(int(str_id0[:repeat_id0]) if repeat_id0 else 0, int(str_id1[:repeat_id1]) + 1):
            xx = int(2*str(x))
            if id0 <= xx <= id1:
                invalid += xx

    return invalid


def part_2(data: list[list[int]]) -> int:
    invalid = set()
    for id0, id1 in data:
        str_id0 = str(id0)
        str_id1 = str(id1)

        len_id0 = len(str_id0)
        len_id1 = len(str_id1)

        repeat_id1 = len_id1//2 + len_id1%2

        for len_x in range(1, repeat_id1 + 1):
            x = int(str_id0[:len_x])
            end = int(str_id1[:len_x])
            done = False
            while not done:
                for repeats in range(max(2, len_id0//len_x), len_id1//len_x + 1):
                    xx = int(repeats*str(x))
                    if id0 <= xx <= id1:
                        invalid.add(xx)

                done = x == end
                x = (x + 1)%10**len_x

    return sum(invalid)


if __name__ == "__main__":
    get_input(2025, 2)

    data = read_input("input.txt")

    print(f"Part 1:\n{part_1(data)}")
    print(f"Part 2:\n{part_2(data)}")