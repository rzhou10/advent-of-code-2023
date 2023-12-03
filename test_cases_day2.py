from days import day2
import unittest

class TestDays(unittest.TestCase):
    def test_day2_part_one(self):
        self.assertEqual(sum(day2.part_one("inputs/day2/day2.txt")), 2207)
        self.assertEqual(sum(day2.part_one("inputs/day2/day2example.txt")), 8)

    def test_day2_part_two(self):
        self.assertEqual(sum(day2.part_two("inputs/day2/day2.txt")), 62241)
        self.assertEqual(sum(day2.part_two("inputs/day2/day2example.txt")), 2286)


if __name__ == '__main__':
    unittest.main()