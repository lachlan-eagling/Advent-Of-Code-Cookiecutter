from unittest import TestCase
from challenges import day_16 as challenge
from utils import load_answer


class TestDay16(TestCase):

    def __init__(self):
        self.answer = load_answer(16)
        super().__init__()

    def test_part_1(self):
        result = challenge.part1()
        self.assertEqual(result, self.answer)

    def test_part_2(self):
        result = challenge.part1()
        self.assertEqual(result, self.answer)