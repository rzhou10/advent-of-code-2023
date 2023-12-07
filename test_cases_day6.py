from days import day6
import unittest
from functools import reduce

class TestDays(unittest.TestCase):
    def test_day6_part_one(self):
        self.assertEqual(reduce(lambda x, y: x * y, day6.part_one("inputs/day6/day6.txt")), 211904)
        self.assertEqual(reduce(lambda x, y: x * y, day6.part_one("inputs/day6/day6example.txt")), 288)

    def test_day6_part_two(self):
        self.assertEqual(reduce(lambda x, y: x * y, day6.part_two("inputs/day6/day6.txt")), 71503)
        self.assertEqual(reduce(lambda x, y: x * y, day6.part_two("inputs/day6/day6example.txt")), 71503)


if __name__ == '__main__':
    unittest.main()