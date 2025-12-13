import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).parents[2]))

from functions import get_input


def read_input(fp: str) -> list[list[int]]:
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        return [[int(x) for x in line.strip("\n").replace("@", "1").replace(".", "0")] for line in f.readlines()]


def box_sum(box, i_rng, j_rng):
    total = 0
    for line in box[i_rng[0]:i_rng[1]+1]:
        total += sum(line[j_rng[0]:j_rng[1]+1])

    return total


def part_1(data: list[list[int]]) -> int:
    rolls = 0
    for i in range(len(data)):
        i_rng = max(0, i-1), min(i+1, len(data)-1)
        for j in range(len(data[i])):
            if data[i][j]:
                j_rng = max(0, j-1), min(j+1, len(data[i])-1)
                if box_sum(data, i_rng, j_rng) < 5:
                    rolls += 1

    return rolls


def part_2(data):
    done = False
    total_rolls = 0
    while not done:
        rolls_i = 0
        for i in range(len(data)):
            i_rng = max(0, i-1), min(i+1, len(data)-1)
            for j in range(len(data[i])):
                if data[i][j]:
                    j_rng = max(0, j-1), min(j+1, len(data[i])-1)
                    if box_sum(data, i_rng, j_rng) < 5:
                        data[i][j] = 0
                        rolls_i += 1

        total_rolls += rolls_i
        done = rolls_i == 0

    return total_rolls


if __name__ == "__main__":
    get_input(2025, 4)

    data = read_input("input.txt")

    print(f"Part 1:\n{part_1(data)}")
    print(f"Part 2:\n{part_2(data)}")
