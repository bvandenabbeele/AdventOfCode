import pathlib


def read_input(fp):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        return f.readlines()


def sign(x):
    try:
        return int(x/abs(x))

    except ZeroDivisionError:
        return 0


def differentiate(x2, x1):
    return x2 - x1


def part_1():
    data = read_input("input.txt")

    data = [int(d.strip("\n")) for d in data]
    diff_data = [differentiate(data[i+1], data[i]) for i in range(len(data) - 1)]
    sign_data = [sign(d) for d in diff_data]

    print(sign_data.count(1))


def part_2():
    data = read_input("input.txt")

    data = [int(d.strip("\n")) for d in data]
    diff_data = [differentiate(sum(data[i+1:i+4]), sum(data[i:i+3])) for i in range(len(data) - 3)]
    sign_data = [sign(d) for d in diff_data]

    print(sign_data.count(1))


if __name__ == "__main__":
    part_1()
    part_2()
