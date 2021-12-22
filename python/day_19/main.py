import numpy as np
from numpy.lib.shape_base import apply_along_axis


def read_file(fp):
    with open(fp) as f:
        scanners = list()

        for line in f:

            if line.startswith("---"):
                scanner_beacons = list()
                continue

            if line == "\n":
                scanners.append(np.array(scanner_beacons))
                continue

            scanner_beacons.append([int(x) for x in line.strip().split(",")])

    scanners.append(np.array(scanner_beacons, dtype=int))
    return scanners


def translate(pos, vector):
    return pos + vector


def rotation(alpha, beta, gamma):
    return rotation_z(alpha) @ rotation_y(beta) @ rotation_x(gamma)


def rotation_x(alpha):
    s = int(np.sin(alpha))
    c = int(np.cos(alpha))
    return np.array([
        [1, 0, 0],
        [0, c, -s],
        [0, s, c]
    ], dtype=int)


def rotation_y(beta):
    s = int(np.sin(beta))
    c = int(np.cos(beta))
    return np.array([
        [c, 0, s],
        [0, 1, 0],
        [-s, 0, c]
    ], dtype=int)


def rotation_z(gamma):
    s = int(np.sin(gamma))
    c = int(np.cos(gamma))
    return np.array([
        [c, -s, 0],
        [s, c, 0],
        [0, 0, 1]
    ], dtype=int)


def rotate(rotation, matrix):
    return np.transpose(rotation @ np.transpose(matrix))


def get_rotation_matrices():
    matrix_set = []
    for alpha in np.arange(4)*np.pi/2:
        for beta in np.arange(4)*np.pi/2:
            for gamma in np.arange(4)*np.pi/2:
                r = rotation(alpha, beta, gamma)
                if not any([np.all(r == m) for m in matrix_set]):
                    matrix_set.append(r)

    return matrix_set


ROTATIONS = get_rotation_matrices()


def common_array_elements(s1, s2):
    return np.array([x for x in set(tuple(x) for x in s1) & set(tuple(x) for x in s2)])


def translate_match(s1, s2, min_len):
    for i, r1 in enumerate(s1):
        for r2 in s2[i:]:
            d = r2 - r1
            s1t = translate(s1, d)
            c = common_array_elements(s1t, s2)
            if len(c) >= min_len:
                return d


def match_one_to_one(s1, s2, min_len):
    for rotation in ROTATIONS:
        s2r = rotate(rotation, s2)
        t = translate_match(s1, s2r, min_len)

        if t is not None:
            return t, s2r - t


def part_1(scanners, min_len):
    scanner_pos = {0: np.zeros(len(scanners[0][0]))}
    beacon_pos = {0: scanners[0]}
    all_beacons = list(scanners[0])

    done = False

    while not done:

        for i in range(len(scanners)):

            if i not in scanner_pos:
                continue

            for j in range(len(scanners)):

                if i == j:
                    continue

                if j in scanner_pos:
                    continue

                result = match_one_to_one(beacon_pos[i], scanners[j], min_len)

                if result is not None:
                    print(f"matched {j} to {i}")
                    t, s2rt = result

                    scanner_pos[j] = - t
                    beacon_pos[j] = s2rt

                    for beacon in s2rt:
                        if not any([np.all(beacon == b) for b in all_beacons]):
                            all_beacons.append(beacon)

        done = len(scanner_pos) == len(scanners)

    print(len(all_beacons))
    dist = 0
    for i, pi in scanner_pos.items():
        for j, pj in scanner_pos.items():
            d = sum([abs(x) for x in pi - pj])
            if d > dist:
                dist = d
    print(dist)


if __name__ == "__main__":
    data = read_file("input.txt")

    part_1(data, 12)
