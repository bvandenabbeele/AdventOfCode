def read_file(fp):
    with open(fp) as f:
        data = list()
        for line in f:
            data.append([int(x) for x in line.strip("\n")])

    return data


def incremenent(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            field [i][j] += 1


def increment_surrounding(field, x, y, nines):
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if (x + i >= 0) and (y + j >= 0) and (x + i, y + j) not in nines:
                try:
                    field[x + i][y + j] += 1

                except IndexError:
                    pass


def step(field):
    incremenent(field)
    nine_in_field = True
    flashes = list()

    while nine_in_field:
        nine_in_field = False

        for i in range(len(field)):
            for j in range(len(field[i])):

                if field[i][j] >= 10:
                    field[i][j] = 0
                    flashes.append((i, j))
                    increment_surrounding(field, i, j, flashes)
                    nine_in_field = True

    return len(flashes)


def print_data(field):
    [print(l) for l in field]
    print()


def part_1(field, steps):
    flashes = 0
    for _ in range(steps):
        flashes += step(field)

    return flashes


def part_2(field):
    flashes = 0
    steps = 0
    field_size = len(field)*len(field[0])

    while not flashes == field_size:
        flashes = step(field)
        steps += 1

    return steps


if __name__ == "__main__":
    from copy import deepcopy

    data = read_file("input.txt")
    print(part_1(deepcopy(data), 100))
    print(part_2(deepcopy(data)))
