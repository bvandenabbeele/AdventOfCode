import pathlib


class Sequence:
    def __init__(self, sequence: list, reverse=False) -> None:
        self.sequence = sequence
        if reverse:
            sequence.reverse()

    def reverse(self):
        self.sequence.reverse()
        return self

    def get_gradients(self) -> list[list[int]]:
        gradients = list()
        done = False
        prev_grad = self.sequence
        while not done:
            grad_i = list()
            for i in range(len(prev_grad) - 1):
                grad_i.append(prev_grad[i+1] - prev_grad[i])

            done = all([g == 0 for g in grad_i])
            prev_grad = grad_i.copy()
            gradients.append(grad_i)

        return gradients

    def predict(self) -> int:
        gradients = self.get_gradients()
        max_i = len(gradients) - 1
        gradients[max_i].append(0)

        for i in range(max_i - 1, -1, -1):
            gradients[i].append(gradients[i][-1] + gradients[i+1][-1])

        return self.sequence[-1] + gradients[0][-1]

    def __str__(self) -> str:
        return str(self.sequence)


def read_input(fp) -> list[Sequence]:
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        return [Sequence([int(l) for l in line.strip("\n").split(" ")]) for line in f.readlines()]


def part_1(data: list[Sequence]):
    return sum([sequence.predict() for sequence in data])


def part_2(data: list[Sequence]):
    return sum([sequence.reverse().predict() for sequence in data])


if __name__ == "__main__":
    data = read_input("input.txt")
    print(f"Part 1:\n{part_1(data)}")
    print(f"Part 2:\n{part_2(data)}")
