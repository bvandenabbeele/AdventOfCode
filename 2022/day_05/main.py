import pathlib

from collections import defaultdict
from copy import deepcopy


def read_file(fp):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        part = 0
        stacks = defaultdict(list)
        operations = list()
        for line in f:
            if part == 0:
                if line[1] == "1":
                    part = 1

                    [lst.reverse() for lst in stacks.values()]
                    sorted(stacks)
                    continue

                for index in range(1, len(line), 4):
                    if line[index] != " ":
                        stacks[(index - 1)//4 + 1].append(line[index])

            else:
                if line != "\n":
                    op = line.lstrip("move ").rstrip("\n").replace(" from ", ",").replace(" to ", ",")
                    operations.append([int(x) for x in op.split(",")])

    return stacks, operations


def part_1(stacks, operations, reverse=True):
    for op in operations:        
        stacks[op[1]], moving = stacks[op[1]][:-op[0]:], stacks[op[1]][-op[0]::]

        if reverse:
            moving.reverse()

        stacks[op[2]] += moving
        a = 0

    top = len(stacks) * [0]
    for i, stack in stacks.items():
        top[i-1] = stack[-1]

    return "".join(top)


if __name__ == "__main__":
    stacks, operations = read_file("input.txt")
    
    print(f"Part 1:\n{part_1(deepcopy(stacks), operations)}")
    print(f"Part 2:\n{part_1(deepcopy(stacks), operations, reverse=False)}")
