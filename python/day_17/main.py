from collections import defaultdict
from math import comb, sqrt


def read_file(fp):
    with open(fp) as f:
        return tuple([tuple([int(y) for y in x[2::].split("..")]) for x in f.read().strip("\n").lstrip("target area: ").split(", ")])


def max_y0(y_target):
    return max(possible_y0(y_target))


def possible_y0(y_target):
    min_y = min(y_target)
    max_y = - min(y_target) - 1

    return list(range(min_y, max_y + 1))


def y_steps_to_target(y0, y_target):
    step_options = list()
    step = 0
    y = 0
    while y >= min(y_target):
        if max(y_target) >= y >= min(y_target):
            step_options.append(step)

        y += y0 - step
        step += 1

    return step_options


def x_steps_to_target(x0, x_target, max_steps):
    step_options = list()
    step = 0
    x = 0
    while (x <= max(x_target)) and (step <= max_steps):
        if max(x_target) >= x >= min(x_target):
            step_options.append(step)

        x += max(0, x0 - step)
        step += 1

    return step_options


def possible_x0(x_target, max_steps):
    min_x = int(sqrt(2*min(x_target)))
    max_x = max(x_target)

    options = defaultdict(lambda: [], dict())

    for x0 in range(min_x, max_x + 1):
        x_steps = x_steps_to_target(x0, x_target, max_steps)
        for step in x_steps:
            options[step].append(x0)

        a = 1

    return options

def max_alt(y0):
    return y0 * (y0 + 1) // 2


def find_combinations(y0_list, y0_steps, x0_dict):
    combinations = []
    for y0, y0_step in zip(y0_list, y0_steps):
        for y0s in y0_step:
            for x0 in x0_dict[y0s]:
                if (x0, y0) not in combinations:
                    combinations.append((x0, y0))

    return combinations


if __name__ == "__main__":
    target = read_file("input.txt")
    # print(target)

    y0 = max_y0(target[1])
    print(max_alt(y0))

    y0_list = possible_y0(target[1])
    y0_steps = [y_steps_to_target(y, target[1]) for y in y0_list]
    x0_dict = possible_x0(target[0], max([max(v) if v else 0 for v in y0_steps]))

    # print(y0_list)
    # print(y0_steps)
    # print(x0_dict)

    combos = find_combinations(y0_list, y0_steps, x0_dict)
    print(len(combos))
    # print(combos)
