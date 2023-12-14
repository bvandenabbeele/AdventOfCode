import pathlib

from math import sqrt


def read_input_part_1(fp) -> list[tuple[int]]:
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        times = f.readline().lstrip("Time:      ").rstrip("\n")
        distances = f.readline().lstrip("Distance:  ").rstrip("\n")

    def parse(string: str) -> list[int]:
        lst = list()
        digit = False
        number = ""
        for ch in string:
            if ch.isdigit():
                digit = True
                number += ch

            else:
                if digit:
                    lst.append(int(number))
                    number = ""

                digit = False

        lst.append(int(number))
        return lst

    t_list = parse(times)
    d_list = parse(distances)

    return [(t, d) for t, d in zip(t_list, d_list)]


def read_input_part_2(fp) -> tuple[int]:
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        time = int(f.readline().lstrip("Time:      ").rstrip("\n").replace(" ",  ""))
        distance = int(f.readline().lstrip("Distance:  ").rstrip("\n").replace(" ", ""))

        return time, distance


def part_1(data: list[tuple[int]]):
    total = 1
    for time, record_distance in data:
        options = 0

        for t in range(1, time):
            distance = (time - t)*t
            if distance > record_distance:
                options += 1

        total *= options

    return total


def part_2(time:int, record_distance:int) -> int:
    t1 = int((-time + sqrt(time**2 - 4*record_distance))/-2)
    t2 = int((-time - sqrt(time**2 - 4*record_distance))/-2)

    return t2 - t1


if __name__ == "__main__":
    data = read_input_part_1("input.txt")
    print(f"Part 1:\n{part_1(data)}")
    time, distance = read_input_part_2("input.txt")
    print(f"Part 2:\n{part_2(time, distance)}")
