import pathlib


class Monkey:
    def __init__(self, items, operation, test, move_true, move_false) -> None:
        self.items = items
        self._op = operation
        self._test = test
        self._move_true = move_true
        self._move_false = move_false
        self.counter = 0
    
    def operation(self, index, divide):
        new_lvl = eval(self._op.replace("old", str(self.items[index])))
        if divide:
            new_lvl //= 3
        self.items[index] = new_lvl
        self.counter += 1

    def test(self, index):
        if self.items[index] % self._test == 0:
            return self._move_true

        else:
            return self._move_false

    def throw(self, index, to_monkey):
        item = self.items.pop(index)
        to_monkey.items.append(item)


def read_file(fp):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        raw = f.readlines()

    monkeys = dict()
    for i in range(0, len(raw), 7):
        id = int(raw[i].strip("\n")[7:-1])
        items = [int(x) for x in raw[i+1].strip("\n")[18:].split(", ")]
        operation = raw[i+2].strip("\n")[19:]
        test = int(raw[i+3].strip("\n")[21:])
        move_true = int(raw[i+4].strip("\n")[29:])
        move_false = int(raw[i+5].strip("\n")[30:])
        monkeys[id] = Monkey(items, operation, test, move_true, move_false)

    return monkeys


def part_1(data, divide, rounds):
    for i in range(rounds):
        print(f"\r{i}", end="")
        for monkey in data.values():
            for _ in range(len(monkey.items)):
                monkey.operation(0, divide)
                monkey_id = monkey.test(0)
                monkey.throw(0, data[monkey_id])

    counters = [monkey.counter for monkey in data.values()]
    counters.sort()
    return counters[-2] * counters[-1]


def main(fp):
    data = read_file(fp)
    print(f"Part 1:\n{part_1(data, True, 20)}")
    print(f"Part 2:\n{part_1(data, False, 10000)}")


if __name__ == "__main__":
    main("test_input.txt")