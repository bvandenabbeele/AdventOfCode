import pathlib
import numpy as np

from matplotlib import pyplot as plt


def read_file(fp):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        raw = f.readlines()
    
    data = set()
    for line in raw:
        points = [tuple([int(c) for c in co.split(",")]) for co in line.strip("\n").split(" -> ")]
        for i in range(len(points) - 1):
            p1 = points[i]
            p2 = points[i+1]

            if p1[0] == p2[0]:
                rge = range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1)
                data |= set((x, y) for x, y in zip(len(rge)*[p1[0]], rge))

            else:
                rge = range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1)
                data |= set((x, y) for x, y in zip(rge, len(rge)*[p1[1]]))

    return data


def part_1(in_data, mode=1):
    data = in_data.copy()
    done = False

    floor = max([d[1] for d in data])
    total_sand = 0

    while not done:
        sand = (500, 0)
        below = (500, 1)
        rest = False

        while not rest:
            touch = False
            while not touch:
                touch = below in data
                if touch: continue

                if (below[1] >= floor) and (mode == 1): break
                if (below[1] == floor + 2) and (mode == 2): break

                sand = below
                below = (below[0], below[1] + 1)
            
            if not touch:
                rest = True
                if mode == 1:
                    done = True

                elif mode == 2:
                    data.add(sand)
                    total_sand += 1
                
                continue

            below_left = (below[0] - 1, below[1])
            if not (below_left in data):
                sand = below_left
                below = (sand[0], sand[1] + 1)
                continue

            below_right = (below[0] + 1, below[1])
            if not (below_right in data):
                sand = below_right
                below = (sand[0], sand[1] + 1)
                continue

            rest = True
            data.add(sand)
            total_sand += 1

            # print(f"\r{total_sand}", end="")
            if total_sand == 24:
                plt.scatter(*np.transpose(np.array(list(data))))
                plt.scatter(*np.transpose(np.array(list(in_data))))
                plt.gca().invert_yaxis()
                continue

            done = (sand == (500, 0)) and (mode == 2)

    return total_sand


def main(fp):
    data = read_file(fp)
    print(f"Part 1:\n{part_1(data, mode=1)}")
    print(f"Part 2:\n{part_1(data, mode=2)}")


if __name__ == "__main__":
    main("input.txt")