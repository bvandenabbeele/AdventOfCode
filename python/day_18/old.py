from os import read
import string


def parse(number, level=0):
    members = list()
    number = number[1:-1]
    i = 0
    while i < len(number):
        if number[i] in string.digits:
            if "," in number[i:]:
                j = number[i:].find(",")
                members.append(int(number[i:j]))
                i += j + 1

            else:
                members.append(int(number[i:]))
                i = len(number)

        elif number[i] == "[":
            j = find_closing(number[i:])
            members.append(SnailFishNumber.from_string(number[i:i+j], level+1))
            i += j + 1

    return members


def find_closing(number):
    opening = 1
    closing = 0
    i = 1
    while (opening != closing) and (i < len(number)):
        if number[i] == "[":
            opening += 1

        elif number[i] == "]":
            closing += 1

        i += 1

    return i


class SnailFishNumber:
    def __init__(self) -> None:
        self.level = None
        self.members = None

    @classmethod
    def from_string(cls, number_string, level=0):
        instance = cls()
        instance.level = level
        instance.members = parse(number_string, instance.level)

        return instance

    @classmethod
    def from_members(cls, members):
        instance = cls()
        instance.level = 0

        for member in members:
            member.increment_level()

        instance.members = members

        return instance

    def increment_level(self):
        self.level += 1
        for member in self.members:
            if isinstance(member, SnailFishNumber):
                member.increment_level()

    def reduce(self):
        done = False
        while not done:
            done = True

    def _reduce(self):
        if self.level == 4:
            pass

    def __repr__(self) -> str:
        return f"[{str(self.members[0])},{str(self.members[1])}]"

    def __add__(self, other):
        return SnailFishNumber.from_members([self, other])


def read_file(fp):
    numbers = list()
    with open(fp) as f:
        for line in f:
            numbers.append(SnailFishNumber.from_string(line.strip()))

    return numbers


if __name__ == "__main__":
    numbers = read_file("test_input.txt")
    print(numbers[0] + numbers[1])
