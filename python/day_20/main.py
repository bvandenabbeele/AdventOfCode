def between(i0, i1, i):
    return i0 <= i < i1


class SparseBinaryImage:

    one = "#"
    zero = "."

    def __init__(self, inf, algorithm, step):
        self.inf = inf
        self.algorithm = algorithm
        self.step = step

        self.ones = set()
        self.size = ((0, 0), (0, 0))

    @classmethod
    def create(cls, algorithm, step=0):
        inf0 = cls.zero
        for _ in range(step):
            inf0 = algorithm[0] if inf0 == cls.zero else algorithm[-1]

        return cls(inf0, algorithm, step)

    @classmethod
    def from_image(cls, instance):
        new = cls.create(instance.algorithm, instance.step+1)

        ((i0, i1), (j0, j1)) = instance.size
        new.size = ((i0-1, i1+1), (j0-1, j1+1))

        return new

    def show(self, extra=0):
        s = ""
        for i in range(self.size[0][0] - extra, self.size[0][1] + extra):
            for j in range(self.size[1][0] - extra, self.size[1][1] + extra):
                s += self[(i, j)]

            s += "\n"

        print(s)

    @property
    def n_ones(self):
        return len(self.ones)

    def surrounding(self, i, j):
        return "".join(
            [
                self[i-1, j-1], self[i-1, j], self[i-1, j+1],
                self[i, j-1],   self[i, j],   self[i, j+1],
                self[i+1, j-1], self[i+1, j], self[i+1, j+1]
            ]
        )

    def __getitem__(self, key):
        if all([between(*self.size[i], key[i]) for i in range(2)]):
            return self.one if key in self.ones else self.zero

        return self.inf

    def __setitem__(self, key, value):
        if (value == self.one):
            self.ones.add(key)

        elif (value == self.zero):
            self.ones.discard(key)


def read_file(fp):
    with open(fp) as f:
        algorithm = f.readline().strip()

        f.readline()

        image = SparseBinaryImage.create(algorithm)
        for i, line in enumerate(f):
            for j, c in enumerate(line):
                image[i, j] = c

    image.size = ((0, i + 1), (0, j + 1))
    return image, algorithm


def binary_to_decimal(s):
    l = len(s)
    d = 0
    for i in range(l):
        d += int(s[i]) * 2**(l - i - 1)

    return d


def enhance(image, algorithm):
    new_image = SparseBinaryImage.from_image(image)

    for i in range(*new_image.size[0]):
        for j in range(*new_image.size[1]):
            s = image.surrounding(i, j)
            s = s.replace(".", "0").replace("#", "1")
            index = binary_to_decimal(s)
            new_image[i, j] = algorithm[index]

    return new_image


def enhance_x(image, algorithm, steps):
    for _ in range(steps):
        image = enhance(image, algorithm)

    return image


if __name__ == "__main__":
    image, algorithm = read_file("input.txt")

    new_image = enhance_x(image, algorithm, 2)
    print(new_image.n_ones)

    new_image = enhance_x(image, algorithm, 50)
    print(new_image.n_ones)
