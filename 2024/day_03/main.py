import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).parents[2]))

from functions import get_input


def read_input(fp: str):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        data = f.readlines()

    data = [d.strip() for d in data]

    return data


def process(line: str, check_condition=False, do=True):
    total = 0
    mul_key = "mul("
    l_mul_key = len(mul_key)
    i0 = 0
    do = do
    do_key = "do()"
    l_do_key = len(do_key)
    dont_key = "don't()"
    l_dont_key = len(dont_key)

    while i0 < len(line) - l_mul_key - 3:
        if (line[i0:i0 + l_mul_key] == mul_key) and (not(check_condition) or do):
            # print(line[i0:i0+15], end=", ")
            i0 += l_mul_key

            f0 = ""
            while line[i0].isdigit():
                f0 += line[i0]
                i0 += 1

            f0 = int(f0)
            # print(f0, end=", ")

            if not line[i0] == ",":
                # print()
                continue

            i0 += 1

            f1 = ""
            while line[i0].isdigit():
                f1 += line[i0]
                i0 += 1

            f1 = int(f1)
            # print(f1, end=", ")

            if line[i0] == ")":
                total += f0 * f1
                # print(f0*f1, end=", ")
                i0 += 1

            # print()

        elif line[i0:i0 + l_do_key] == do_key:
            do = True
            i0 += l_do_key

        elif line[i0:i0 + l_dont_key] == dont_key:
            do = False
            i0 += l_dont_key

        else:
            i0 += 1

    return total, do


def part_1(data: list[str]):
    total = 0

    for line in data:
        total += process(line)[0]

    return total


def part_2(data):
    total = 0
    do = True

    for line in data:
        t, do = process(line, check_condition=True, do=do)
        total += t

    return total


if __name__ == "__main__":
    get_input(2024, 3)

    data = read_input("input.txt")

    print(f"Part 1:\n{part_1(data)}")
    print(f"Part 2:\n{part_2(data)}")