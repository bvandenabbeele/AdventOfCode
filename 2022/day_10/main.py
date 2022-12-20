import pathlib


def read_file(fp):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        return [(l[:4], l[5:-1]) for l in f.readlines()]


def part_1(data):
    t = 0
    x = 1
    hist = dict()
    for command, n in data:
        if command == "noop":
            t += 1
            continue

        elif command == "addx":
            t += 2
            x += int(n)
            hist[t+1] = x

    t_hist = list(hist.keys())
    signal_strength = dict()
    i = 0
    for ti in range(20, 221, 40):
        found = False
        while not found:
            if t_hist[i] >= ti:
                found = True
                index = i-1*(t_hist[i]!=ti)  # i if t_hist[i] == ti, i-1 otherwise
                signal_strength[ti] = ti*hist[t_hist[index]]
                continue

            i += 1

    return sum(signal_strength.values())


def part_2(data):
    x = 1
    data_i = 0
    new_line = True
    cpu = 240*["."]
    queue = dict()
    for t in range(240):
        if t in queue:
            x += queue[t]
            del queue[t]

        if new_line:
            command, number = data[data_i]
            new_line = False
            data_i += 1

            if command == "noop":
                new_line = True

            elif command == "addx":
                queue[t+2] = int(number)

        else:
            new_line = True

        if x-1 <= t <= x+1:
            cpu[t] = "#"

    cpu_string = "".join(cpu)
    new_cpu = ""
    for i in range(0, 240, 40):
        new_cpu += cpu_string[i:i+40] + "\n"

    return new_cpu


def main(fp):
    data = read_file(fp)
    print(f"Part 1:\n{part_1(data)}")
    print(f"Part 2:\n{part_2(data)}")


if __name__ == "__main__":
    main("test_input.txt")