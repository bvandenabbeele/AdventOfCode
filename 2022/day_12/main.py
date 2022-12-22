import numpy as np
import pathlib

def read_file(fp):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        return np.array([[x for x in l.strip("\n")] for l in f.readlines()])


def find_path(data):
    start = tuple(np.concatenate(np.where(data == "S")))
    end = tuple(np.concatenate(np.where(data == "E")))

    data[start] = "a"
    data[end] = "z"

    mx = np.product(np.shape)
    cost = mx * np.ones(data.shape)
    cost[start] = 0

    done = False
    while not done:
        for i in len(data):
            for j in len(data[0]):
                


def part_1(data):
    start = tuple(np.concatenate(np.where(data == "S")))
    end = tuple(np.concatenate(np.where(data == "E")))

    data[start] = "a"
    data[end] = "z"
    
    paths = [[start]]
    done = False
    while not done:
        new_paths = list()
        for path in paths:
            new_paths += find_options(path, data)
        
        paths = new_paths
        print(len(paths))
        finished = [end in path for path in paths]
        done = any(finished)

    return len(paths[finished.index(True)]) - 1


def main(fp):
    data = read_file(fp)
    print(f"Part 1:\n{part_1(data)}")
    # print(f"Part 2:\n{part_1(data, False, 10000)}")


if __name__ == "__main__":
    main("test_input.txt")
