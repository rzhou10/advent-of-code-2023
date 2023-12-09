from days import day8
import unittest

class TestDays(unittest.TestCase):
    def test_day1_part_one(self):
        self.assertEqual(day8.part_one("inputs/day8/day8.txt"), 16579)
        self.assertEqual(day8.part_one("inputs/day8/day8example.txt"), 2)
        self.assertEqual(day8.part_one("inputs/day8/day8example2.txt"), 6)

    # def test_day1_part_two(self):
    #     self.assertEqual(day8.part2("inputs/day8/day8.txt"), 54473)
    #     self.assertEqual(day8.part2("inputs/day8/day8example.txt"), 142)
    #     self.assertEqual(day8.part2("inputs/day8/day1examplept2.txt"), 281)


if __name__ == '__main__':
    unittest.main()