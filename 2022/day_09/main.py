import numpy as np
import pathlib

from matplotlib import pyplot as plt


def read_file(fp):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        raw = [line.strip("\n").split(" ") for line in f.readlines()]
        return [(line[0], int(line[1])) for line in raw]


def move_head(c, h):
    if c[0] == "U":
        h += np.array([0, c[1]])

    elif c[0] == "D":
        h -= np.array([0, c[1]])

    elif c[0] == "L":
        h -= np.array([c[1], 0])

    elif c[0] == "R":
        h += np.array([c[1], 0])

    else:
        raise ValueError(c)

    return h


def move_tail(c, h, t):
    tail_hist = set()
    tail_hist.add(tuple(t))

    for _ in range(c[1]):
        d = h - t
        if np.sum((d)**2) <= 2:
            break

        t += np.sign(d)
        tail_hist.add(tuple(t))

    return t, tail_hist


def part_1(data):
    h = np.array([0, 0])
    t = np.array([0, 0])

    tail_hist = set()
    tail_hist.add(tuple(t))

    for c in data:
        h = move_head(c, h)
        t, hist = move_tail(c, h, t)
        tail_hist |= hist

    return len(tail_hist)


def part_2(data):
    knots = np.array(10*[[0, 0]])

    tail_hist = set()
    tail_hist.add(tuple(knots[-1]))

    for c in data:
        for _ in range(c[1]):
            ci = (c[0], 1)
            knots[0] = move_head(ci, knots[0])

            for i in range(1, len(knots)):
                knots[i], hist = move_tail(ci, knots[i-1], knots[i])

                if i == len(knots) - 1:
                    tail_hist |= hist

    return len(tail_hist)


def main(fp):
    data = read_file(fp)
    print(f"Part 1:\n{part_1(data)}")
    print(f"Part 2:\n{part_2(data)}")


if __name__ == "__main__":
    main("input.txt")