from days import day1
import unittest

class TestDays(unittest.TestCase):
    def test_day1_part_one(self):
        self.assertEqual(sum(day1.part1("inputs/day1/day1.txt")), 54990)
        self.assertEqual(sum(day1.part1("inputs/day1/day1example.txt")), 142)

    def test_day1_part_two(self):
        self.assertEqual(sum(day1.part2("inputs/day1/day1.txt")), 54473)
        self.assertEqual(sum(day1.part2("inputs/day1/day1example.txt")), 142)
        self.assertEqual(sum(day1.part2("inputs/day1/day1examplept2.txt")), 281)


if __name__ == '__main__':
    unittest.main()