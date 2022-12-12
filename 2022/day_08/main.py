import numpy as np
import pathlib


def read_file(fp):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        return np.array([[int(r) for r in line.strip("\n")] for line in f])


def is_visible_row(row, i):
    return (max(row[:i]) < row[i]) or (max(row[i+1:]) < row[i])


def is_visible(data, i, j):
    return is_visible_row(data[i], j) or is_visible_row(data[:, j], i)


def part_1(data):
    n_visible = 2*(len(data[0]) + len(data[:, 0]) - 2)

    for i in range(len(data[0, 1:-1])):
        for j in range(len(data[1:-1, 0])):
            if is_visible(data, i+1, j+1):
                n_visible += 1

    return n_visible


def get_score_left(left_row, h):
    i = 0
    s = 0
    done = False

    while not done:
        s += 1

        if (not left_row[i] < h) or (i == len(left_row) - 1):
            done = True
            return s

        i += 1

def get_score_row(row, i):
    return get_score_left(row[:i][::-1], row[i]) * get_score_left(row[i+1:], row[i])


def get_score(data, i, j):
    return get_score_row(data[i], j) * get_score_row(data[:, j], i)


def part_2(data):
    max_scenic_score = 0

    for i in range(len(data[0, 1:-1])):
        for j in range(len(data[1:-1, 0])):
            scenic_score = get_score(data, i+1, j+1)
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score

    return max_scenic_score


def main(fp):
    data = read_file(fp)
    print(f"Part 1:\n{part_1(data)}")
    print(f"Part 2:\n{part_2(data)}")


if __name__ == "__main__":
    main("input.txt")