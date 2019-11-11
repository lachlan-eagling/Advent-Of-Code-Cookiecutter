from os import mkdir
from os.path import basename
from jinja2 import Template

def generate_solution_files():
    for i in range(1, 26):
        mkdir(f"./data/answers/day_{i}/")
        with open(f"./data/answers/day_{i}/part1.txt", "w+") as f:
            pass

        with open(f"./data/answers/day_{i}/part2.txt", "w+") as f:
            pass
        continue


def generate_input_files():
    for i in range(1, 26):
        with open(f"./data/inputs/day_{i}.txt", "w+") as f:
            pass
        continue


def generate_test_files():
    for i in range(1, 26):
        with open("./templates/test.tmpl") as f:
            template = Template(f.read())
            with open(f"./challenges/tests/test_day_{i}.py", "w+") as f:
                f.write(template.render(day=i))
        continue


def generate_challenge_files():
    for i in range(1, 26):
        with open("./templates/challenge.tmpl") as f:
            template = Template(f.read())
            with open(f"./challenges/day_{i}.py", "w+") as f:
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