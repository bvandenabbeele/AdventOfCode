from collections import defaultdict


def read_file(fp):
    with open(fp) as f:
        start = f.readline().strip("\n")
        f.readline()

        templates = dict()
        for line in f:
            key, new = line.strip("\n").split(" -> ")
            templates[key] = key[0] + new + key[1]

    return start, templates


def make_polymer(string):
    start_polymer = defaultdict(lambda: 0, {})
    for s in string:
        start_polymer[s] += 1

    return start_polymer


def create_chain(start_string, templates, max_depth):
    polymer = make_polymer(start_string)
    for i in range(len(start_string) - 1):
        # print(f"\r{i+1}/{len(start_string)-1}", end="")
        _create_chain(start_string[i:i+2], polymer, templates, 0, max_depth)

    # print()
    return polymer


def _create_chain(ab, polymer, templates, depth, max_depth):
    if depth == max_depth:
        return

    abc = templates[ab]
    polymer[abc[1]] += 1

    for i in range(2):
        _create_chain(abc[i:i+2], polymer, templates, depth+1, max_depth)


def create_chain_string(start, templates, steps):
    s = start
    for _ in range(steps):
        end = _create_chain_string(s, templates)
        s = end

    return end


def _create_chain_string(start, templates):
    end = str()
    for i in range(len(start) - 1):
        end += templates[start[i:i+2]][:-1]

    return end + start[-1]


def part_1(start_string, templates, max_depth):
    polymer = create_chain(start_string, templates, max_depth)

    maxv = max(list(polymer.values()))
    minv = min(list(polymer.values()))

    return maxv - minv


def part_2(start_string, templates):
    templates_10 = dict()
    counts_10 = dict()
    for key in templates.keys():
        templates_10[key] = create_chain_string(key, templates, 10)
        counts_10[key] = create_chain(key, templates, 10)

    templates_20 = dict()
    counts_20 = dict()
    for key in templates_10.keys():
        templates_20[key] = create_chain_string(key, templates_10, 2)
        counts_20[key] = create_chain(key, templates_10, 2)

    # polymer = create_chain_string(start_string, templates_10, 1)
    polymer = start_string

    counts = defaultdict(lambda: 0, {})
    for i in range(len(polymer) - 1):
        ss = polymer[i:i+2]
        for key, value in counts_10[ss].items():
            counts[key] += value

    print(counts)
    maxv = max(list(counts.values()))
    minv = min(list(counts.values()))

    return maxv - minv


def _part_2(ss, counts_10, counts, templates_10, depth, max_depth):
    if depth == max_depth:
        return

    for i in range(len(ss) - 1):

        iss = ss[i:i+2]
        icounts = counts_10[iss]
        for key, value in icounts.items():
            counts[key] += value

        itemplates = templates_10[iss]
        for j in range(len(itemplates) - 1):
            _part_2(itemplates[j:j+2], counts_10, counts, templates_10, depth+1, max_depth)



if __name__ == "__main__":
    start_string, templates = read_file("test_input.txt")

    print(part_1(start_string, templates, 10))
    print(part_2(start_string, templates))
