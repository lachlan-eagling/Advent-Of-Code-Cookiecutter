from unittest import TestCase
from advent_of_code.challenges import day_5 as challenge

from advent_of_code.utils import load_answer


class TestDay5(TestCase):

    def test_part_1(self):
        result = challenge.part1()
        answer = load_answer(5, 1)
        self.assertEqual(str(result), answer)

    def test_part_2(self):
        result = challenge.part1()
        answer = load_answer(5, 2)
        self.assertEqual(str(result), answer)