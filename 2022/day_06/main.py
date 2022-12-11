import pathlib


def read_file(fp):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        return [line.strip("\n") for line in f.readlines()]


def part_1(data, length):
    first_marker = list()
    for line in data:
        hist = str()
        for i in range(len(line)):
            hist += line[i]
            hist = hist[-length::]

            if len(set(hist)) == length:
                first_marker.append(i + 1)
                break

    return first_marker
    

if __name__ == "__main__":
    data = read_file("input.txt")
    
    print(f"Part 1:\n{part_1(data, 4)}")
    print(f"Part 1:\n{part_1(data, 14)}")
