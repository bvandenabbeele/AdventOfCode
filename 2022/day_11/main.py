import pathlib


class Monkey:
    def __init__(self, operation, test, move_true, move_false) -> None:
        self._op = operation
        self._test = test
        self._move_true = move_true
        self._move_false = move_false
        self.counter = 0
    
    def operation(self, lvl, divide):
        new_lvl = eval(self._op.replace("old", str(lvl)))        
        if divide:
            new_lvl //= 3
        
        self.counter += 1
        
        return new_lvl

    def test(self, lvl):
        if lvl % self._test == 0:
            return self._move_true

        else:
            return self._move_false


def read_file(fp):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        raw = f.readlines()

    monkeys = dict()
    item_dict = dict()
    for i in range(0, len(raw), 7):
        id = int(raw[i].strip("\n")[7:-1])
        items = [int(x) for x in raw[i+1].strip("\n")[18:].split(", ")]
        operation = raw[i+2].strip("\n")[19:]
        test = int(raw[i+3].strip("\n")[21:])
        move_true = int(raw[i+4].strip("\n")[29:])
        move_false = int(raw[i+5].strip("\n")[30:])

        monkeys[id] = Monkey(operation, test, move_true, move_false)
        item_dict[id] = items

    return monkeys, item_dict


def part_1(monkeys, item_dict, divide, rounds):
    for _ in range(rounds):
        for monkey_id in range(len(item_dict)):
            monkey = monkeys[monkey_id]

            for item in item_dict[monkey_id]:
                item = monkey.operation(item, divide)
                new_id = monkey.test(item)
                item_dict[new_id].append(item)
            
            item_dict[monkey_id].clear()

    counters = [monkey.counter for monkey in monkeys.values()]
    print(counters)
    counters.sort()
    return counters[-2] * counters[-1]


# def part_2(data):
#     for i in range(10000):
#         for monkey in data.values():
#             for _ in range(len(monkey.items)):
#                 new_lvl = eval(self._op.replace("old", str(self.items[index])))
#                 items[index] = new_lvl
#                 self.counter += 1


def main(fp):
    data = read_file(fp)
    print(f"Part 1:\n{part_1(*data, True, 20)}")
    # print(f"Part 2:\n{part_1(data, False, 10000)}")


if __name__ == "__main__":
    import time

    t1 = time.time()
    main("test_input.txt")
    t2 = time.time()
    print(f"Execution Time: {t2-t1}")