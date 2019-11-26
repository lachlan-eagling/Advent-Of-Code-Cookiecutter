from unittest import TestCase
from advent_of_code.challenges import day_20 as challenge

from advent_of_code.utils import load_answer


class TestDay20(TestCase):

    def test_part_1(self):
        result = challenge.part1()
        answer = load_answer(20, 1)
        self.assertEqual(str(result), answer)

    def test_part_2(self):
        result = challenge.part1()
        answer = load_answer(20, 2)
        self.assertEqual(str(result), answer)