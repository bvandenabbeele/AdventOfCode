def read_file(fp):
    with open(fp, "r") as f:
        raw = f.readlines()

    signals = list()
    numbers = list()
    for line in raw:
        s, n = line.split(" | ")
        signals.append(["".join(sorted(ss)) for ss in s.split(" ")])
        numbers.append(["".join(sorted(nn)) for nn in n.strip("\n").split(" ")])

    return signals, numbers


def find_x(signal, digit_length, single=True):
    digits = list()
    for s in signal:
        if len(s) == digit_length:
            digits.append(s)

        if single and len(digits) == 1:
            return digits[0]

    return digits


def find_one(signal):
    return find_x(signal, 2)


def find_seven(signal):
    return find_x(signal, 3)


def find_four(signal):
    return find_x(signal, 4)


def find_eight(signals):
    return find_x(signals, 7)


def part_1(signals, numbers):
    cntr = 0

    for s_list, n_list in zip(signals, numbers):
        unique_digits = [
            find_one(s_list), find_four(s_list), find_seven(s_list), find_eight(s_list)
        ]

        for n in n_list:
            if n in unique_digits:
                cntr += 1

    return cntr


def subtract_strings(a, b):
    for x in b:
        if x in a:
            a = a.replace(x, "")

    return a


def find_a(seven, one):
    return subtract_strings(seven, one)


def find_three(signal, one):
    five_length = find_x(signal, 5, single=False)
    residuals = list()
    for x in five_length:
        residuals.append(len(subtract_strings(x, one)))

    return five_length[residuals.index(3)]

def find_five(signal, four, seven, three):
    five_length = find_x(signal, 5, single=False)
    five_length.remove(three)
    residuals = list()
    for x in five_length:
        residuals.append(len(subtract_strings(subtract_strings(x, four), seven)))

    return five_length[residuals.index(1)]


def find_two(signal, five, three):
    five_length = find_x(signal, 5, single=False)
    five_length.remove(five)
    five_length.remove(three)
    return five_length[0]


def find_six(signal, one):
    six_length = find_x(signal, 6, single=False)
    residuals = list()
    for x in six_length:
        residuals.append(len(subtract_strings(x, one)))

    return six_length[residuals.index(5)]


def find_nine(signal, four):
    six_length = find_x(signal, 6, single=False)
    residuals = list()
    for x in six_length:
        residuals.append(len(subtract_strings(x, four)))

    return six_length[residuals.index(2)]


def find_zero(signal, six, nine):
    five_length = find_x(signal, 6, single=False)
    five_length.remove(six)
    five_length.remove(nine)
    return five_length[0]


def find_digits(signal):
    one = find_one(signal)
    four = find_four(signal)
    seven = find_seven(signal)
    eight = find_eight(signal)

    three = find_three(signal, one)
    five = find_five(signal, four, seven, three)
    two = find_two(signal, five, three)

    six = find_six(signal, one)
    nine = find_nine(signal, four)
    zero = find_zero(signal, six, nine)

    return {
        zero: 0,
        one: 1,
        two: 2,
        three: 3,
        four: 4,
        five: 5,
        six: 6,
        seven: 7,
        eight: 8,
        nine: 9
    }


def decode(number, digits):
    return [digits[n] for n in number]


def base_10(number_list):
    x = 0
    l = len(number_list)
    for i, n in enumerate(number_list):
        x += n * 10**(l-i-1)

    return x


def part_2(signals, numbers):
    total = 0
    for s_list, n_list in zip(signals, numbers):
        digits = find_digits(s_list)
        total += base_10(decode(n_list, digits))

    return total


if __name__ == "__main__":
    s, n = read_file("input.txt")
    print(part_1(s, n))

    print(part_2(s, n))
