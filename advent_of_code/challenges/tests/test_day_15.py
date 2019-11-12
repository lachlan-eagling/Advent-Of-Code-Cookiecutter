from unittest import TestCase
from challenges import day_15 as challenge
from utils import load_answer


class TestDay15(TestCase):

    def __init__(self):
        self.answer1 = load_solution(15, 1)
        self.answer2 = load_solution(15, 2)
        super().__init__()

    def test_part_1(self):
        result = challenge.part1()
        self.assertEqual(result, self.answer1)

    def test_part_2(self):
        result = challenge.part1()
        self.assertEqual(result, self.answer2)