import pathlib


def read_file(fp):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        raw = f.readlines()

    data = list()
    for i in range(0, len(raw), 3):
        l1 = raw[i]
        l2 = raw[i+1]

        data.append((eval(l1.strip("\n")), eval(l2.strip("\n"))))

    return data


def check_order(l1, l2):
    if l1 == l2:
        return

    for i in range(min(len(l1), len(l2))):
        if isinstance(l1[i], list):
            if isinstance(l2[i], list):
                c = check_order(l1[i], l2[i])

            else:
                c = check_order(l1[i], [l2[i]])
            
            if c is not None:
                return c

        else:
            if isinstance(l2[i], list):
                c = check_order([l1[i]], l2[i])

                if c is not None:
                    return c

            else:
                if l1[i] < l2[i]:
                    return 0

                elif l1[i] > l2[i]:
                    return 1

    return 0 if len(l1) <= len(l2) else 1


def part_1(data):
    total = 0
    for i, packets in enumerate(data):
        index = check_order(*packets)
        if index == 0:
            total += i + 1

    return total


def part_2(in_data):
    divider_packets = [[[2]], [[6]]]
    data = list()
    for p1, p2 in in_data:
        data += [p1, p2]
    data = divider_packets + data
    
    done = False
    while not done:
        done = True
        for i in range(len(data) - 1):
            index = check_order(data[i], data[i+1])
            if index == 0:
                continue

            data[i], data[i+1] = data[i+1], data[i]
            done = False

    return (data.index(divider_packets[0]) + 1) * (data.index(divider_packets[1]) + 1)


def main(fp):
    data = read_file(fp)
    print(f"Part 1:\n{part_1(data)}")
    print(f"Part 2:\n{part_2(data)}")


if __name__ == "__main__":
    main("input.txt")