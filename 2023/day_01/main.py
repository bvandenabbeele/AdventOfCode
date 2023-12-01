import pathlib


digits: dict[str, str] = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}


def read_input(fp):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        return [line.strip() for line in f.readlines()]


def part_1(data: list[str]):
    total = 0

    for line in data:
        i = 0
        done = False
        while not done:
            if line[i].isdigit():
                done = True
                d1 = line[i]

            i += 1

        i = len(line) - 1
        done = False
        while not done:
            if line[i].isdigit():
                done = True
                d2 = line[i]

            i -= 1

        total += int(d1 + d2)

    return total


def part_2(data: list[str]):
    total = 0

    for line in data:
        i = 0
        done = False
        while not done:
            if line[i].isdigit():
                done = True
                d1 = line[i]

            else:
                for word, digit in digits.items():
                    if line[i:i+len(word)] == word:
                        done = True
                        d1 = digit

            i += 1

        i = len(line) - 1
        done = False
        while not done:
            if line[i].isdigit():
                done = True
                d2 = line[i]

            else:
                for word, digit in digits.items():
                    if line[i-len(word)+1:i+1] == word:
                        done = True
                        d2 = digit

            i -= 1

        total += int(d1 + d2)

    return total



if __name__ == "__main__":
    data = read_input("input.txt")
    print(f"Part 1:\n{part_1(data)}")
    print(f"Part 2:\n{part_2(data)}")
