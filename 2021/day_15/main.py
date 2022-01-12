from os import path, read
import numpy as np


def read_file(fp):
    with open(fp) as f:
        data = f.readlines()

    arr = list()
    for line in data:
        arr.append([int(l) for l in line.strip("\n")])

    return np.array(arr, dtype=int)


def surrounding_of(i, j, size_i, size_j):
    surr_paths = list()
    if i > 0:
        surr_paths.append((i - 1, j))
    if j > 0:
        surr_paths.append((i, j - 1))
    if i < size_i - 1:
        surr_paths.append((i + 1, j))
    if j < size_j - 1:
        surr_paths.append((i, j + 1))

    return surr_paths


def cheapest_path(field, start):
    inf = int(1e5)
    paths = np.ones(field.shape, dtype=int) * inf
    paths[start] = 0
    visited = np.zeros(field.shape, dtype=int)

    current = start
    tentative_list = [current]

    while not visited[-1, -1]:
        print(f"\r{np.count_nonzero(visited)}/{visited.shape[0]*visited.shape[1]}", end="")
        surr = surrounding_of(*current, *paths.shape)
        for s in surr:
            if not visited[s]:
                paths[s] = min(paths[current] + field[s], paths[s])
                tentative_list.append(s)

        visited[current] = inf
        tentative_list.remove(current)

        tentative_tuple = tuple(tentative_list)
        temp = paths[tentative_tuple]
        current = tentative_list[np.argwhere(temp == np.min(temp))[0, 0]]

        # temp = paths + visited
        # current = tuple(np.argwhere(temp == np.min(temp))[0])

    print()
    return paths[-1, -1]



def large_map(small_field):
    x, y = small_field.shape
    field = np.zeros((5*x, 5*y), dtype=int)

    for i in range(5):
        for j in range(5):
            field[i*x:(i+1)*x, j*y:(j+1)*y] = (small_field + (i + j))

    while np.max(field) > 9:
        field -= (field>9)*9

    return field


if __name__ == "__main__":
    field = read_file("input.txt")

    print(cheapest_path(field, (0, 0)))

    big_field = large_map(field)
    # for row in big_field:
    #     [print(i, end=" ") for i in row]
    #     print()

    print(cheapest_path(big_field, (0, 0)))
