from days import day2
import unittest

class TestDays(unittest.TestCase):
    def test_day2_part_one(self):
        with open("inputs/day2/day2.txt", 'r') as f:
            txt_nums = f.readlines()

        txt_nums = list(map(lambda s : s.replace('\n', ''), txt_nums))

        self.assertEqual(sum(day2.part_one(txt_nums)), 2207)

    def test_day2_part_one_example(self):
        with open("inputs/day2/day2example.txt", 'r') as f1:
            txt_nums = f1.readlines()

        txt_nums = list(map(lambda s : s.replace('\n', ''), txt_nums))

        self.assertEqual(sum(day2.part_one(txt_nums)), 8)

    def test_day2_part_two(self):
        with open("inputs/day2/day2.txt", 'r') as f:
            txt_nums1 = f.readlines()

        txt_nums1 = list(map(lambda s : s.replace('\n', ''), txt_nums1))
        self.assertEqual(sum(day2.part_two(txt_nums1)), 62241)

    def test_day2_part_two_example(self):
        with open("inputs/day2/day2example.txt", 'r') as f:
            txt_nums1 = f.readlines()

        txt_nums1 = list(map(lambda s : s.replace('\n', ''), txt_nums1))
        self.assertEqual(sum(day2.part_two(txt_nums1)), 2286)



if __name__ == '__main__':
    unittest.main()