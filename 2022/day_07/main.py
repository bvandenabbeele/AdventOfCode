import pathlib

from collections import defaultdict


# class Tree:
#     def __init__(self) -> None:
#         self.children = list()

#     @property
#     def size(self):
#         return sum([child.size for child in self.children])


def read_file(fp):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        return [l.strip("\n") for l in f.readlines()]


def part_1(data):
    dirs = defaultdict(int)
    path = list()

    for line in data:
        if line[0] == "$":
            if line[2:4] == "cd":
                if line[5] == ".":
                    path = path[:-1]

                else:
                    path.append(line[5:])

            elif line[2:4] == "ls":
                continue

            else:
                raise Exception(line)

        elif line[:3] == "dir":
            continue

        elif line[0].isnumeric():
            size, _ = line.split(" ")
            size = int(size)
            for i in range(len(path)):
                dirs["/".join(path[:i+1])] += size

        else:
            raise Exception(line)

    return sum([s for s in dirs.values() if s <= 1e5]), dirs


def part_2(dirs):
    min_size = int(3e7 - (7e7 - dirs["/"]))
    return min([s for s in dirs.values() if s >= min_size])

if __name__ == "__main__":
    data = read_file("input.txt")
    sol1, dirs = part_1(data)
    print(f"Part 1:\n{sol1}")
    print(f"Part 2:\n{part_2(dirs)}")
