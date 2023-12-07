import pathlib

from collections import defaultdict


def read_input(fp):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        return {int(line[5:line.index(":")]): [[int(line[i:i+2]) for i in range(line.index(":")+2, line.index("|")-1, 3)], [int(line[j:j+2]) for j in range(line.index("|")+2, len(line)-1, 3)]] for line in f.readlines()}


def part_1(data):
    total = 0
    i = 1
    done = False
    while not done:
        try:
            winner, card = data[i]
            score = 0
            for w in winner:
                if w in card:
                    score += 1

            if score > 0:
                total += 2**(score - 1)

            i += 1

        except KeyError:
            done = True

    return total


def part_2(data):
    def _return():
        return 1
    copies = defaultdict(_return)

    total = 0
    i = 1
    done = False
    while not done:
        try:
            winner, card = data[i]
            total += copies[i]

            matches = 0
            for w in winner:
                if w in card:
                    matches += 1

            for j in range(1, matches+1):
                copies[i+j] += copies[i]

            i += 1

        except KeyError:
            done = True

    return total


if __name__ == "__main__":
    data = read_input("input.txt")
    print(f"Part 1:\n{part_1(data)}")
    print(f"Part 2:\n{part_2(data)}")
