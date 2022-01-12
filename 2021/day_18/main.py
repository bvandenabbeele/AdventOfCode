import string


def read_file(fp):
    data = list()
    with open(fp) as f:
        for line in f:
            data.append(line.strip())

    return data


def parse(raw):
    level = -1
    number = list()

    for i in range(len(raw)):
        if raw[i] == "[":
            level += 1

        elif raw[i] == "]":
            level -= 1

        if raw[i] in string.digits:
            number.append([int(raw[i]), level])

    return number


def add(n1, n2):
    n3 = list()
    for x, level in n1 + n2:
        n3.append([x, level + 1])

    return n3


def reduce(n):
    done = False

    while not done:
        done = True

        e = explode(n)
        if e:
            done = False
            n = e
            continue

        s = split(n)
        if s:
            done = False
            n = s
            continue

    return n


def explode(n):
    for i in range(len(n) - 1):
        if n[i][1] == n[i + 1][1] == 4:
            return _explode(n, i, i+1)


def _explode(n, i1, i2):
    x1, level = n[i1]
    x2, _ = n[i2]

    if i1 != 0:
        n[i1 - 1][0] += x1

    if i2 != len(n) - 1:
        n[i2 + 1][0] += x2

    n = n[:i1] + [[0, level - 1]] + n[i2+1:]

    return n


def split(n):
    for i in range(len(n)):
        if n[i][0] > 9:
            return _split(n, i)


def _split(n, i):
    x, level = n[i]
    return n[:i] + [[x//2, level + 1], [(x+1)//2, level +1]] + n[i + 1:]


def sum_all(numbers):
    n = numbers[0]

    for n2 in numbers[1:]:
        n = reduce(add(n, n2))

    return n


def magnitude(n):
    done = False
    i = 0
    while not done:
        x1, l1 = n[i]
        x2, l2 = n[i+1]

        if l1 == l2:
            n = n[:i] + [[3*x1 + 2*x2, l1 - 1]] + n[i+2:]
            i = 0

        else:
            i += 1

        if max([x[1] for x in n]) == 0:
            done = True

    return 3*n[0][0] + 2*n[1][0]


def largest_sum(numbers):
    m = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue

            s = magnitude(reduce(add(numbers[i], numbers[j])))
            if s > m:
                m = s

    return m


if __name__ == "__main__":
    raw = read_file("input.txt")
    numbers = [parse(r) for r in raw]

    sum_n = sum_all(numbers)
    print(magnitude(sum_n))

    print(largest_sum(numbers))