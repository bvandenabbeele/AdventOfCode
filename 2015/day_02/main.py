from os import read


def read_file(fp):
    with open(fp) as f:
        presents = list()
        for line in f:
            presents.append([int(x) for x in line.strip().split("x")])
    
    return presents


def area(d):
    return 2*(d[0]*d[1] + d[0]*d[2] + d[1]*d[2])


def smallest_face_area(d):
    ds = d.copy()
    ds.remove(max(d))
    return ds[0] * ds[1]


def smallest_face_circumference(d):
    ds = d.copy()
    ds.remove(max(d))
    return 2*(ds[0] + ds[1])


def volume(d):
    return d[0]*d[1]*d[2]


def part_1(presents):
    total = 0
    for p in presents:
        total += area(p) + smallest_face_area(p)

    return total


def part_2(presents):
    total = 0
    for p in presents:
        total += smallest_face_circumference(p) + volume(p)

    return total


if __name__ == "__main__":
    presents = read_file("input.txt")
    print(part_1(presents))
    print(part_2(presents))
