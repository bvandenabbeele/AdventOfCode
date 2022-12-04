import pathlib


def read_file(fp):
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        raw = f.readlines()

    data = [r.strip("\n").split(" ") for r in raw]
    return data


def solve_game_p1(*h):
    h = list(h)

    if h in (["A", "C"], ["B", "A"], ["C", "B"]):
        return 0

    elif h in [2*["A"], 2*["B"], 2*["C"]]:
        return -1

    return 1


def solve_tournament_p1(guide, mapping):
    score = 0
    for game in guide:
        my_hand = mapping[game[1]]
        result = solve_game_p1(game[0], my_hand)

        score += ord(my_hand) - 64
        if result == 1:
            score += 6

        elif result == -1:
            score += 3

    return score


def solve_game_p2(player_1, outcome):
    # draw
    if outcome == "Y":
        return player_1

    # loss
    elif outcome == "X":
        if player_1 == "A":
            return "C"

        elif player_1 == "B":
            return "A"

        else:  # player_1 == "C"
            return "B"

    # win
    elif outcome == "Z":
        if player_1 == "A":
            return "B"

        elif player_1 == "B":
            return "C"

        else:  # player_1 == "C"
            return "A"


def solve_tournament_p2(guide):
    score = 0
    for game in guide:
        my_hand = solve_game_p2(*game)

        score += ord(my_hand) - 64
        if game[1] == "Y":
            score += 3

        elif game[1] == "Z":
            score += 6

    return score


if __name__ == "__main__":
    data = read_file("input.txt")
    mapping = {"X": "A", "Y": "B", "Z": "C"}
    print(f"Part 1:\n{solve_tournament_p1(data, mapping)}")
    print(f"Part 2:\n{solve_tournament_p2(data)}")
    a = 0