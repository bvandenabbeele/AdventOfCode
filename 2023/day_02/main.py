import pathlib


def read_input(fp):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        data = dict()

        for game in f.readlines():
            id, hands = game.lstrip("Game ").rstrip("\n").split(": ")
            lst = list()
            for hand in hands.split("; "):
                dct = dict()
                lst.append(dct)
                for cubes in hand.split(", "):
                    cnt, color = cubes.split(" ")
                    dct[color] = int(cnt)

            data[int(id)] = lst

    return data


def part_1(data, red, green, blue):
    colors = ("red", "green", "blue")
    counts = (red, green, blue)

    total = 0
    for id, hands in data.items():
        possible = True

        i = 0
        while possible and (i < len(hands)):
            hand = hands[i]

            j = 0
            while possible and (j < 3):
                try:
                    possible = hand[colors[j]] <= counts[j]

                except KeyError:
                    pass

                finally:
                    j += 1

            i += 1

        if possible:
            total += id

    return total


def part_2(data):
    colors = ("red", "green", "blue")

    total = 0
    for hands in data.values():
        possible = True
        mins = [0, 0, 0]

        for hand in hands:
            for i in range(len(colors)):
                try:
                    mins[i] = max(mins[i], hand[colors[i]])

                except KeyError:
                    pass

        if possible:
            total += mins[0] * mins[1] * mins[2]

    return total


if __name__ == "__main__":
    data = read_input("input.txt")
    print(f"Part 1:\n{part_1(data, 12, 13, 14)}")
    print(f"Part 2:\n{part_2(data)}")
