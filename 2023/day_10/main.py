import pathlib

from matplotlib import pyplot as plt


def read_input(fp):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        return [line.strip("\n") for line in f.readlines()]


def find_start(data: list[str]) -> tuple[int]:
    done = False
    si = 0
    while not done:
        done = "S" in data[si]
        if not done:
            si += 1

        else:
            sj = data[si].index("S")

    return si, sj


def first_step(data: list[str], orig_i: int, orig_j: int) -> tuple[int]:
    # find where to go from start
    if (orig_i > 0) and (data[orig_i-1][orig_j] in ["|", "7", "F"]):
        coors = orig_i - 1, orig_j

    elif (orig_i < len(data) - 1) and (data[orig_i+1][orig_j] in ["|", "L", "J"]):
        coors = orig_i + 1, orig_j

    elif (orig_j > 0) and (data[orig_i][orig_j-1] in ["-", "J", "7"]):
        coors = orig_i, orig_j - 1

    elif (orig_j < len(data[0]) - 1) and (data[orig_i][orig_j+1] in ["-", "L", "F"]):
        coors = orig_i, orig_j + 1

    return coors


def next_step(data: list[str], i0: int, j0: int, i1: int, j1: int) -> tuple[int]:
    if i1 - i0 == 1:   # moving down
        match data[i1][j1]:
            case "|":
                return i1, j1, i1 + 1, j1
            case "L":
                return i1, j1, i1, j1 + 1
            case "J":
                return i1, j1, i1, j1 - 1

    elif i1 - i0 == -1:  # moving up
        match data[i1][j1]:
            case "|":
                return i1, j1, i1 - 1, j1
            case "7":
                return i1, j1, i1, j1 - 1
            case "F":
                return i1, j1, i1, j1 + 1

    elif j1 - j0 == 1:  # moving right
        match data[i1][j1]:
            case "-":
                return i1, j1, i1, j1 + 1
            case "J":
                return i1, j1, i1 - 1, j1
            case "7":
                return i1, j1, i1 + 1, j1
    elif j1 - j0 == -1:  # moving left
        match data[i1][j1]:
            case "-":
                return i1, j1, i1, j1 - 1
            case "L":
                return i1, j1, i1 - 1, j1
            case "F":
                return i1, j1, i1 + 1, j1


def part_1(data: list[str]):
    i0, j0 = find_start(data)
    i1, j1 = first_step(data, i0, j0)

    distance = 1

    done = False
    while not done:
        i0, j0, i1, j1 = next_step(data, i0, j0, i1, j1)
        done = (data[i1][j1] == "S")
        if not done:
            distance += 1

    if distance%2 == 0:
        return distance // 2

    else:
        return distance // 2 + 1


def part_2(data: list[str]):
    i0, j0 = find_start(data)
    i1, j1 = first_step(data, i0, j0)

    path = {(i0, j0), (i1, j1)}

    done = False
    while not done:
        i0, j0, i1, j1 = next_step(data, i0, j0, i1, j1)
        path |= {(i1, j1)}

        done = (data[i1][j1] == "S")

    inside_points = 0

    max_i = len(data)
    for i in range(1, len(data) - 1):
        if i > max_i//2:
            rge = range(i+1, max_i, 1)

        else:
            rge = range(0, i, 1)

        for j in range(1, len(data[0]) - 1):
            if (i, j) not in path:
                crossings = 0
                corner_crossing = ""
                # draw a line from the point to infinity. in this case down. odd number of crossings with boundary means inside shape
                # straight horizontal sections are one crossing. vertical is ignored, corners are checked with each other. if it turns back on itself, it's not counted
                for ii in rge:
                    if (ii, j) in path:
                        if data[ii][j] == "-":
                            crossings += 1

                        elif data[ii][j] == "|":
                            continue

                        else:
                            x = {corner_crossing, data[ii][j]}
                            if x in ({"F", "J"}, {"7", "L"}):
                                crossings += 1

                            corner_crossing = data[ii][j]

                if crossings%2 == 1:
                    print((i, j))

                inside_points += crossings%2

    return int(inside_points)


if __name__ == "__main__":
    data = read_input("input.txt")
    print(f"Part 1:\n{part_1(data)}")
    print(f"Part 2:\n{part_2(data)}")
