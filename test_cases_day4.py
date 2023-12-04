from days import day4
import unittest

class TestDays(unittest.TestCase):
    def test_day4_part_one(self):
        self.assertEqual(sum(day4.check_cards_part_one("inputs/day4/day4.txt")), 28538)
        self.assertEqual(sum(day4.check_cards_part_one("inputs/day4/day4example.txt")), 13)

    def test_day4_part_two(self):
        self.assertEqual(sum(day4.check_cards_part_two("inputs/day4/day4.txt")), 9425061)
        self.assertEqual(sum(day4.check_cards_part_two("inputs/day4/day4example.txt")), 30)


if __name__ == '__main__':
    unittest.main()