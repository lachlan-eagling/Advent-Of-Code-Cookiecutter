from unittest import TestCase
from challenges import day_3 as challenge
from utils import load_answer


class TestDay3(TestCase):

    def __init__(self):
        self.answer = load_answer(3)
        super().__init__()

    def test_part_1(self):
        result = challenge.part1()
        self.assertEqual(result, self.answer)

    def test_part_2(self):
        result = challenge.part1()
        self.assertEqual(result, self.answer)