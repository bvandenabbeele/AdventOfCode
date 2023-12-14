import unittest

from main import Mapping


class TestCases(unittest.TestCase):
    def test_part_2(self):
        maps = [
            [10, 20, 5]
        ]
        mapping = Mapping("1", "2", maps)

        new_seed = mapping.get_mapped_value_part_2(20, 5)
        self.assertCountEqual(new_seed, [(10, 5)])

        new_seed = mapping.get_mapped_value_part_2(20, 2)
        self.assertCountEqual(new_seed, [(10, 2)])

        new_seed = mapping.get_mapped_value_part_2(22, 2)
        self.assertCountEqual(new_seed, [(12, 2)])

        new_seed = mapping.get_mapped_value_part_2(22, 3)
        self.assertCountEqual(new_seed, [(12, 3)])

        new_seed = mapping.get_mapped_value_part_2(15, 6)
        self.assertCountEqual(new_seed, [(15, 5), (10, 1)])

        new_seed = mapping.get_mapped_value_part_2(15, 5)
        self.assertCountEqual(new_seed, [(15, 5)])

        new_seed = mapping.get_mapped_value_part_2(15, 10)
        self.assertCountEqual(new_seed, [(15, 5), (10, 5)])

        new_seed = mapping.get_mapped_value_part_2(20, 6)
        self.assertCountEqual(new_seed, [(10, 5), (25, 1)])

        new_seed = mapping.get_mapped_value_part_2(25, 5)
        self.assertCountEqual(new_seed, [(25, 5)])

        new_seed = mapping.get_mapped_value_part_2(22, 5)
        self.assertCountEqual(new_seed, [(12, 3), (25, 2)])

        new_seed = mapping.get_mapped_value_part_2(15, 15)
        self.assertCountEqual(new_seed, [(15, 5), (10, 5), (25, 5)])


if __name__ == "__main__":
    unittest.main()