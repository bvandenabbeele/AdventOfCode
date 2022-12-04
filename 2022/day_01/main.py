import pathlib


def read_input(fp):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        raw = f.read()

    data = [[int(n) for n in r.split("\n")] for r in raw.split("\n\n")]

    return data


def find_max(d):
    m = 0
    index = 0
    for i, l in enumerate(d):
        ls = sum(l)
        if ls > m:
            m = ls
            index = i

    return m, index


def find_3max(d):
    m_list = []
    for _ in range(3):
        m, index = find_max(d)
        m_list.append(m)
        d.pop(index)

    return m_list




if __name__ == "__main__":
    data = read_input("input.txt")
    print(f"Part 1:\n{find_max(data)[0]}")
    print(f"Part 2:\n{sum(find_3max(data))}")
