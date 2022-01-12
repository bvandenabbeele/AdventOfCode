def read_file(fp):
    with open(fp) as f:
        return f.read().strip()


def part_1(directions):
    return directions.count("(") - directions.count(")")


def part_2(directions):
    current_floor = 0
    for i, d in enumerate(directions):
        if d == "(":
            current_floor += 1

        else:
            current_floor -=1

        if current_floor == -1:
            return i + 1


if __name__ == "__main__":
    directions = read_file("input.txt")
    print(part_1(directions))
    print(part_2(directions))
