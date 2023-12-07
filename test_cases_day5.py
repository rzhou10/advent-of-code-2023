from days import day5
import unittest

class TestDays(unittest.TestCase):
    def test_day4_part_one(self):
        self.assertEqual(sum(day5.check_cards_part_one("inputs/day5/day5.txt")), 28538)
        self.assertEqual(sum(day5.check_cards_part_one("inputs/day5/day5example.txt")), 35)

    def test_day4_part_two(self):
        self.assertEqual(sum(day5.check_cards_part_two("inputs/day5/day5.txt")), 9425061)
        self.assertEqual(sum(day5.check_cards_part_two("inputs/day5/day5example.txt")), 30)


if __name__ == '__main__':
    unittest.main()