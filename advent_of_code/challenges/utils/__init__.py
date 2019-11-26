from typing import List, Any
from os.path import abspath


def load_input(day: int) -> List[str]:
    filepath = abspath('./advent_of_Code/data/input/day_1.txt')
    with open(filepath) as f:
        return input_as_list(f.read())


def load_answer(day, part: int) -> str:
    filepath = abspath(f'./advent_of_Code/data/answers/day_{day}/part_{part}.txt')
    with open(filepath) as f:
        return f.read()

def input_as_list(data: str):
    return data.splitlines()


def save_answers(answer: Any, day, part: int):
    filepath = abspath(f'./advent_of_Code/data/answers/day_{day}/part_{part}.txt')
    with open(filepath, 'w+') as f:
        return f.write(str(answer))