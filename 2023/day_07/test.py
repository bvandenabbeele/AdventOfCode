import unittest

from main import CamelCard


class TestCase(unittest.TestCase):
    def test_five_of_a_kind(self):
        bid = 100
        for ch in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]:
            hand = 5*ch
            card = CamelCard(hand, bid)
            self.assertEqual(card.rank, 7)

    def test_one_pair(self):
        # without joker
        card = CamelCard("229Q5", 100, joker=False)
        self.assertEqual(card.hand, [2, 2, 9, 12, 5])
        self.assertEqual(card.rank, 2)

        # with joker
        card = CamelCard("J375Q", 100, joker=True)
        self.assertEqual(card.hand, [1, 3, 7, 5, 12])
        self.assertEqual(card.rank, 2)

    def test_four_of_a_kind(self):
        # with joker
        card = CamelCard("JJ956", bid=100, joker=True)
        self.assertEqual(card.hand, [1, 1, 9, 5, 6])
        self.assertEqual(card.rank, 4)

        card = CamelCard("JJ959", bid=100, joker=True)
        self.assertEqual(card.hand, [1, 1, 9, 5, 9])
        self.assertEqual(card.rank, 6)

if __name__ == "__main__":
    unittest.main()