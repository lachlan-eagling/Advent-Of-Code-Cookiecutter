from os import mkdir
from os.path import basename, abspath, join, exists
from jinja2 import Template

def generate_solution_files():
    for i in range(1, 26):
        answers_path = abspath(f'./advent_of_Code/data/answers')
        day_path = join(answers_path, f"day_{i}")
        if not exists(day_path):
            mkdir(day_path)
        with open(join(answers_path, f"day_{i}", "part_1.txt"), "w+") as f:
            pass

        with open(join(answers_path, f"day_{i}", "part_2.txt"), "w+") as f:
            pass
        continue


def generate_input_files():
    for i in range(1, 26):
        with open(abspath(f'./advent_of_Code/data/input/day_{i}'), "w+") as f:
            pass
        continue


def generate_test_files():
    for i in range(1, 26):
        with open(abspath(f"./generate/templates/test.tmpl")) as f:
            template = Template(f.read())
            with open(abspath(f"./advent_of_Code/challenges/tests/test_day_{i}.py"), "w+") as f:
                f.write(template.render(day=i))
        continue


def generate_challenge_files():
    for i in range(1, 26):
        with open(abspath(f"./generate/templates/challenge.tmpl")) as f:
            template = Template(f.read())
            with open(abspath(f"./advent_of_Code/challenges/day_{i}.py"), "w+") as f:
                f.write(template.render(day=i))
        continue


def generate_all():
    generate_solution_files()
    generate_input_files()
    generate_test_files()
    generate_challenge_files()


def main():
    generate_all()

if __name__ == "__main__":
    main()