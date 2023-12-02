from days import day1
import unittest

class TestDays(unittest.TestCase):
    def test_day1_part_one(self):
        with open("inputs/day1/day1.txt", 'r') as f:
            txt_nums = f.readlines()

        txt_nums = list(map(lambda s : s.replace('\n', ''), txt_nums))

        self.assertEqual(sum(day1.part1(txt_nums)), 54990)

    def test_day1_part_one_example(self):
        with open("inputs/day1/day1example.txt", 'r') as f1:
            txt_nums = f1.readlines()

        txt_nums = list(map(lambda s : s.replace('\n', ''), txt_nums))

        self.assertEqual(sum(day1.part1(txt_nums)), 142)

    def test_day1_part_two(self):
        with open("inputs/day1/day1.txt", 'r') as f:
            txt_nums1 = f.readlines()

        txt_nums1 = list(map(lambda s : s.replace('\n', ''), txt_nums1))
        self.assertEqual(sum(day1.part2(txt_nums1)), 54473)

    def test_day1_part_two_example(self):
        with open("inputs/day1/day1example.txt", 'r') as f:
            txt_nums1 = f.readlines()

        txt_nums1 = list(map(lambda s : s.replace('\n', ''), txt_nums1))
        self.assertEqual(sum(day1.part2(txt_nums1)), 142)

    def test_day1_part_two_example_p2(self):
        with open("inputs/day1/day1examplept2.txt", 'r') as f:
            txt_nums1 = f.readlines()

        txt_nums1 = list(map(lambda s : s.replace('\n', ''), txt_nums1))
        self.assertEqual(sum(day1.part2(txt_nums1)), 281)



if __name__ == '__main__':
    unittest.main()