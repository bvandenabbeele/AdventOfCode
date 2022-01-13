def read_file(fp):
    with open(fp) as f:
        return f.read().strip()


def part_1(directions):
    houses = set()
    i = 0
    j = 0

    for d in directions:
        houses.add((i, j))

        if d == "^":
            j += 1
        
        elif d == "v":
            j -= 1
        
        elif d == ">":
            i += 1

        elif d == "<":
            i -= 1

    return houses


def part_2(directions):
    houses1 = part_1(directions[0::2])
    houses2 = part_1(directions[1::2])
    
    return houses1 | houses2


if __name__ == "__main__":
    directions = read_file("input.txt")
    print(len(part_1(directions)))
    print(len(part_2(directions)))
