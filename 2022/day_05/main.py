import pathlib

from collections import defaultdict


def read_file(fp):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        part = 0
        stacks = defaultdict(list)
        for line in f:
            if part == 0:
                for index in range(1, len(line), 4):
                    if line[index] != " ":
                        stacks[(index - 1)//4 + 1].append(line[index])

    return stacks


if __name__ == "__main__":
    data = read_file("test_input.txt")
    print(data)
