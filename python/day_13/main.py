import numpy as np


def read_file(fp):
    dots = list()
    instructions = list()
    all_points = False
    with open(fp) as f:
        for line in f:
            if line == "\n":
                all_points = True
                continue

            if not all_points:
                dots.append(tuple([int(x) for x in line.strip("\n").split(",")]))

            else:
                l = line.strip("fold along ").split("=")
                instructions.append((l[0], int(l[1])))

    return dots, instructions


def fold_x(dot, value):
    return (dot[0] if dot[0] < value else 2*value - dot[0]), dot[1]


def fold_y(dot, value):
    return dot[0], dot[1] if dot[1] < value else 2*value - dot[1]


def fold_dot(dot, axis, value):
    if axis == 'x':
        return fold_x(dot, value)

    else:
        return fold_y(dot, value)


def fold_dots(dots, axis, value):
    for i in range(len(dots) - 1, -1, -1):
        dots[i] = fold_dot(dots[i], axis, value)

    return list(set(dots))


def fold_all(dots, instructions):
    for instruction in instructions:
        dots = fold_dots(dots, *instruction)

    return dots


def plot(dots):
    max_x = max_y = 0

    for x, y in dots:
        if x > max_x:
            max_x = x

        if y > max_y:
            max_y = y

    field = np.empty((max_y + 1, max_x + 1), dtype="U1")

    for x, y in dots:
        field[y, x] = '█'

    field[field != '█'] = ' '

    [print("".join(f)) for f in field]


if __name__ == "__main__":
    dots, instructions = read_file("input.txt")

    print(len(fold_dots(dots.copy(), *instructions[0])))

    new_dots = fold_all(dots.copy(), instructions)
    plot(new_dots)