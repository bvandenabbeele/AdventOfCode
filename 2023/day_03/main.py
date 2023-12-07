import pathlib


def read_input(fp):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        return [line.strip("\n") for line in f.readlines()]


def part_1(data: list[str]):
    total = 0

    for i in range(len(data)):

        digit = False
        number = ""
        surrounding = list()

        for j in range(len(data[i])):

            ch = data[i][j]

            if ch.isdigit():
                if not digit:
                    if j > 0:
                        surrounding.append((i, j-1))
                        if i > 0: surrounding.append((i-1, j-1))
                        if i < len(data) - 1: surrounding.append((i+1, j-1))

                if i > 0: surrounding.append((i-1, j))
                if i < len(data) - 1: surrounding.append((i+1, j))

                digit = True
                number += ch

            if (not ch.isdigit()) or (digit and (j == len(data[i]) - 1)):
                if digit:
                    if i > 0: surrounding.append((i-1, j))
                    surrounding.append((i, j))
                    if i < len(data) - 1: surrounding.append((i+1, j))

                    special = False
                    for ii, jj in surrounding:
                        if (data[ii][jj] != ".") and (not data[ii][jj].isdigit()):
                            special = True
                            break

                    if special:
                        total += int(number)

                    surrounding.clear()

                    number = ""
                digit = False

    return total


def find_number(data_i: str, j):
    number = data_i[j]
    digit = True
    ji = j-1
    while digit and ji >= 0:
        if data_i[ji].isdigit():
            number = data_i[ji] + number
            ji -= 1

        else:
            digit = False

    digit = True
    ji = j + 1
    while digit and ji <= len(data_i) - 1:
        if data_i[ji].isdigit():
            number += data_i[ji]
            ji += 1

        else:
            digit = False

    return number


def part_2(data: list[str]):
    total = 0
    surrounding = list()
    numbers = list()

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "*":
                surrounding.clear()
                if j > 0:
                    if i > 0: surrounding.append((i-1, j-1))
                    surrounding.append((i, j-1))
                    if i < len(data) - 1: surrounding.append((i+1, j-1))

                if j < len(data[i]) - 1:
                    if i > 0: surrounding.append((i-1, j+1))
                    surrounding.append((i, j+1))
                    if i < len(data) - 1: surrounding.append((i+1, j+1))

                if i > 0: surrounding.append((i-1, j))
                if i < len(data) - 1: surrounding.append((i+1, j))

                for ii, jj in surrounding:
                    if data[ii][jj].isdigit():
                        number = find_number(data[ii], jj)
                        if number not in numbers:
                            numbers.append(number)

                        print(number)
                if len(numbers) == 2:
                    total += int(numbers[0]) * int(numbers[1])
                numbers.clear()

    return total


if __name__ == "__main__":
    data = read_input("input.txt")
    print(f"Part 1:\n{part_1(data)}")
    print(f"Part 2:\n{part_2(data)}")
