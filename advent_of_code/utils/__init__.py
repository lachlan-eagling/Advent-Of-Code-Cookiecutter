from os.path import abspath


def load_input(day: int) -> str:
    filepath = abspath('./advent_of_Code/data/input/day_1.txt')
    with open(filepath) as f:
        return f.read()


def load_answer(day, part: int) -> str:
    filepath = abspath(f'./advent_of_Code/data/answers/day_{day}/part_{part}.txt')
    with open(filepath) as f:
        return f.read()


def main():
    data = load_answer(1,2)
    print(data)


if __name__ == "__main__":
    main()