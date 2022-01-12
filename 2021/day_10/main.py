class ParseError(Exception):
    def __init__(self, pos, expected, received):
        self.pos = pos
        self.expected = expected
        self.received = received

        super().__init__(self.message)

    @property
    def message(self):
        return f"Parse Error in line at index {self.pos}: Expected {self.expected} but got {self.received} instead"



def read_file(fp):
    with open(fp) as f:
        data = f.readlines()

    return [d.strip("\n") for d in data]


def is_opening(bracket):
    return bracket in "[{(<"


# def opening_of(closing_bracket):
#     dct = {
#         "}": "{",
#         ")": "(",
#         "]": "[",
#         ">": "<"
#     }
#     return dct[closing_bracket]


def closing_of(opening_bracket):
    dct = {
        "{": "}",
        "(": ")",
        "[": "]",
        "<": ">"
    }
    return dct[opening_bracket]


def parse(line):
    level = -1
    level_chunks = dict()
    for i, c in enumerate(line):
        if is_opening(c):
            level += 1
            level_chunks[level] = c

        else:
            correct_closing = closing_of(level_chunks[level])
            if c == correct_closing:
                level_chunks.pop(level)
                level -= 1

            else:
                raise ParseError(i, correct_closing, c)

    return level_chunks


def complete(line):
    levels = parse(line)
    suffix = ""

    for level in range(max(levels), -1, -1):
        suffix += closing_of(levels[level])

    return suffix


def part_1(data):
    weird_point_system = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    points = 0

    for line in data:
        try:
            parse(line)

        except ParseError as e:
            points += weird_point_system[e.received]

    return points


def part_2(data):
    weird_point_system = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }

    line_points = list()

    for line in data:
        try:
            suffix = complete(line)

        except ParseError as e:
            pass

        else:
            points = 0
            for c in suffix:
                points *= 5
                points += weird_point_system[c]

            line_points.append(points)

    line_points.sort()

    return line_points[len(line_points)//2]


if __name__ == "__main__":
    code = read_file("input.txt")
    print(part_1(code))
    print(part_2(code))