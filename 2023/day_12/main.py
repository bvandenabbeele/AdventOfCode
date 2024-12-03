import pathlib

from typing import Iterator


def read_input(fp):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        raw = [line.strip("\n").split(" ") for line in f.readlines()]

    data = list()
    for line in raw:
        data.append((line[0], tuple([int(x) for x in line[1].split(",")])))

    return data


def combinations(n, k):
   def backtrack(start, current_combination) -> Iterator[list[int]]:
      if len(current_combination) == k:
         yield current_combination

      for i in range(start, n):
         yield from backtrack(i + 2, current_combination + [i])

   return backtrack(0, list())


def make_all_possibilities(row, pattern):
    poss = 0
    for c in combinations(len(row) - (sum(pattern) - len(pattern)), len(pattern)):
        c.append(len(row)+1)
        r = c[0]*"."

        offset = 0
        l0 = 0
        fit = True

        for i in range(len(c)-1):
            r += pattern[i]*"#"

            offset += pattern[i] - 1
            r += (c[i+1] + offset - len(r))*"."

            l1 = len(r)

            for s1, s2 in zip(row[l0:l1:], r[l0::]):
                fit = fit and (s1 == s2 or s1 == "?")

            l0 = l1

            if not fit:
                break

        if fit:
            poss += 1

    return poss


def part_1(data):
    total = 0
    for row, pattern in data:
        t = make_all_possibilities(row, pattern)
        total += t

    return total


def part_2(data):
    total = 0
    for row, pattern in data:
        t = make_all_possibilities(5*row, 5*pattern)
        total += t

    return total


if __name__ == "__main__":
    fp = "test_input.txt"
    data = read_input(fp)

    # for x in combinations(6, 3):
    #     print(x)

    # print(f"Part 1:\n{part_1(data)}")
    # print(f"Part 2:\n{part_2(data)}")
