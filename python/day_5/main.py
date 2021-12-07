def read_file(fp):
    with open(fp, "r") as f:
        vent_lines = list()
        for line in f.readlines():
            coors = line.split(" -> ")
            vent_line = list()
            for co in coors:
                vent_line.append(tuple([int(c) for c in co.split(",")]))
            vent_lines.append(vent_line)

    return vent_lines


def is_horizontal(line):
    return line[0][1] == line [1][1]


def is_vertical(line):
    return line[0][0] == line [1][0]


def is_diagonal(line):
    return abs(line[0][0] - line[1][0]) == abs(line[0][1] - line[1][1])


def is_hor_or_vert(line):
    return is_horizontal(line) or is_vertical(line)


def get_all_line_coors(line):
    all_coors = list()
    if is_horizontal(line):
        y = line[0][1]
        start = min(line[0][0], line[1][0])
        stop = max(line[0][0], line[1][0]) + 1
        for x in range(start, stop):
            all_coors.append((x, y))

    elif is_vertical(line):
        x = line[0][0]
        start = min(line[0][1], line[1][1])
        stop = max(line[0][1], line[1][1]) + 1
        for y in range(start, stop):
            all_coors.append((x, y))

    elif is_diagonal(line):
        start = line[0]
        dist = abs(line[1][0] - line[0][0])
        dir = [(line[1][i] - line[0][i])//dist for i in range(len(line[0]))]

        for d in range(0, dist + 1):
            all_coors.append(tuple([start[i] + dir[i]*d for i in range(len(line[0]))]))

    return all_coors


def update_count(vent_count, line_coors):
    for coor in line_coors:
        if coor in vent_count:
            vent_count[coor] += 1

        else:
            vent_count[coor] = 1


def count_number_of_multiple(vent_count):
    c = 0
    for v in vent_count.values():
        if v > 1:
            c += 1

    return c


def part_1(vent_lines):
    vent_count = dict()
    for line in vent_lines:
        if not is_hor_or_vert(line):
            continue

        line_coors = get_all_line_coors(line)
        update_count(vent_count, line_coors)

    return count_number_of_multiple(vent_count)


def part_2(vent_lines):
    vent_count = dict()
    for line in vent_lines:
        line_coors = get_all_line_coors(line)
        update_count(vent_count, line_coors)

    return count_number_of_multiple(vent_count)


if __name__ == "__main__":
    vent_lines = read_file("input.txt")
    print(part_1(vent_lines))
    print(part_2(vent_lines))
