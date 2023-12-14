import pathlib

from typing import Optional


class CamelCard:
    def __init__(self, hand: str, bid: str|int, joker: Optional[bool]=False) -> None:
        self.orig_hand = hand
        self._joker = joker
        self.hand = self.convert_hand(hand)
        self.bid: int = int(bid)
        self.rank = self.rank_hand()
        self.sorting_rank = [self.rank] + self.hand

    @property
    def joker(self):
        return self._joker

    @joker.setter
    def joker(self, bool: bool) -> None:
        self._joker = bool
        self.hand = self.convert_hand(self.orig_hand)
        self.rank = self.rank_hand()
        self.sorting_rank = [self.rank] + self.hand

    def convert_hand(self, hand: str) -> list:
        out = list()
        mapping = {"A": 14, "K": 13, "Q": 12, "J": 11 if not self._joker else 1, "T": 10}
        for ch in hand:
            if ch.isdigit():
                out.append(int(ch))

            else:
                out.append(mapping[ch])

        return out

    def rank_hand(self) -> int:
        types = (self.five_of_a_kind, self.four_of_a_kind, self.full_house, self.three_of_a_kind, self.two_pair, self.one_pair)
        scores = (7, 6, 5, 4, 3, 2)

        for t, s in zip(types, scores):
            if t():
                return s

        return 1

    def five_of_a_kind(self) -> bool:
        result = self.hand.count(self.hand[0]) == 5

        if not self._joker or result:
            return result

        elif self._joker:
            return (len(set(self.hand)) == 2) and (1 in self.hand)

    def four_of_a_kind(self) -> bool:
        j = self.hand.count(1)
        for x in self.hand:
            c = self.hand.count(x)
            if (not self._joker or j == 0) and c == 4:
                return True

            elif self._joker and x != 1 and c + j == 4:
                return True

        return False

    def three_of_a_kind(self) -> bool:
        j = self.hand.count(1)
        for x in self.hand:
            c = self.hand.count(x)
            if (not self._joker or j == 0) and c == 3:
                return True

            elif self._joker and c + j == 3:
                return True

        return False

    def full_house(self) -> bool:
        j = self.hand.count(1)
        s = len(set(self.hand))

        if (not self._joker or j == 0) and self.three_of_a_kind():
            return s == 2

        elif self._joker and j > 0:
            return s == 3

        return False

    def x_pair(self, n_pairs) -> bool:
        j = self.hand.count(1)
        pairs = list()
        for x in self.hand:
            if self.hand.count(x) == 2 and x not in pairs:
                pairs.append(x)

        return (len(pairs) + (j if self._joker else 0)) == n_pairs

    def two_pair(self) -> bool:
        return self.x_pair(2)

    def one_pair(self) -> bool:
        return self.x_pair(1)

    def __str__(self) -> str:
        return f"Hand: {self.orig_hand}, Bid: {self.bid}, Rank: {self.rank}"

    def __lt__(self, other: "CamelCard"):
        return self.sorting_rank < other.sorting_rank


def read_input(fp) -> list[CamelCard]:
    with open(pathlib.Path(__file__).parent / fp, "r") as f:
        data = [CamelCard(*line.strip("\n").split(" ")) for line in f.readlines()]

    return data


def part_1(data: list[CamelCard]):
    data.sort()
    total = 0
    for i in range(len(data)):
        # print(i + 1, data[i])
        total += (i + 1) * data[i].bid

    return total


def part_2(data: list[CamelCard]):
    for card in data:
        card.joker = True

    return part_1(data)


if __name__ == "__main__":
    data = read_input("input.txt")
    print(f"Part 1:\n{part_1(data)}")
    print(f"Part 2:\n{part_2(data)}")
