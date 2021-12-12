from copy import copy


def read_file(fp):
    with open(fp) as f:
        data = list()
        for line in f:
            data.append(line.strip("\n").split("-"))

    return data


def create_caves(data):
    network = dict()
    for cave_1, cave_2 in data:
        network.setdefault(cave_1, []).append(cave_2)
        network.setdefault(cave_2, []).append(cave_1)

    return network


def is_accepted_part_1(path):
    if path[-1].isupper():
        return True

    if path.count(path[-1]) > 1:
        return False

    return True


def is_accepted_part_2(path):
    if path[-1].isupper():
        return True

    two_visits = None

    for cave in path:
        if cave.isupper():
            continue

        n = path.count(cave)
        if n > 2:
            return False

        if n > 1:
            if cave == 'start':
                return False

            if two_visits not in [None, cave]:
                return False

            two_visits = cave

    return True


def _find_routes(network, path, end, is_accepted):
    if path[-1] == end:
        return 1

    n_paths = 0
    for cave in network[path[-1]]:
        new_path = path.copy()
        new_path.append(cave)
        if is_accepted(new_path):
            n_paths += _find_routes(network, new_path, end, is_accepted)

    return n_paths


def find_routes_part_1(network):
    return _find_routes(network, ['start'], 'end', is_accepted_part_1)

def find_routes_part_2(network):
    return _find_routes(network, ['start'], 'end', is_accepted_part_2)


if __name__ == "__main__":
    import time

    t1 = time.time()

    data = read_file("input.txt")
    caves = create_caves(data)

    paths = find_routes_part_1(caves)
    print(paths)

    paths = find_routes_part_2(caves)
    print(paths)

    t2 = time.time()

    print(t2 - t1)