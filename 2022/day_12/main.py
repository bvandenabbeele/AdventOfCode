import numpy as np
import pathlib

def read_file(fp):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        return np.array([[x for x in l.strip("\n")] for l in f.readlines()])


def find_adjacent(coor):
    adjacent = [
        (coor[0] + 1, coor[1]),
        (coor[0] - 1, coor[1]),
        (coor[0], coor[1] + 1),
        (coor[0], coor[1] - 1)
    ]

    return adjacent
    

def find_path(data_in):
    data = data_in.copy()

    start = tuple(np.concatenate(np.where(data == "S")))
    end = tuple(np.concatenate(np.where(data == "E")))

    data[start] = "a"
    data[end] = "z"

    mx = np.product(data.shape)
    cost = mx * np.ones(data.shape, dtype=int)
    steps = 0
    cost[start] = steps
    all_visited = set()
    all_visited.add(start)
    visited = all_visited.copy()

    done = False
    while not done:
        steps += 1
        new_visited = set()

        for index_0 in visited:
            surroundings = find_adjacent(index_0)
            for index_i in surroundings:
                if (index_i in all_visited) or \
                    (min(index_i) < 0) or \
                    (index_i[0] >= cost.shape[0]) or \
                    (index_i[1] >= cost.shape[1]):
                    continue
                
                if ord(data[index_i]) - ord(data[index_0]) <= 1:
                    cost[index_i] = min(cost[index_i], steps)
                    new_visited.add(index_i)

        all_visited |= new_visited
        visited = new_visited
        done = (len(new_visited) == 0) or (cost[end] < mx)
    
    return cost[end]


def part_2(data):
    start = tuple(np.concatenate(np.where(data == "S")))
    data[start] = "a"

    cost = np.product(data.shape)
    for x, y in np.column_stack(np.where(data == "a")):
        data[x, y] = "S"
        c = find_path(data)
        if c < cost:
            cost = c
        data[x, y] = "a"

    return cost
        

def main(fp):
    data = read_file(fp)
    print(f"Part 1:\n{find_path(data.copy())}")
    print(f"Part 2:\n{part_2(data)}")


if __name__ == "__main__":
    main("input.txt")
