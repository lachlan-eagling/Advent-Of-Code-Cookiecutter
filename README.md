<link href="https://fonts.googleapis.com/css?family=Mountains+of+Christmas&display=swap" rel="stylesheet">

<h1 style="text-align: center; font-family: 'Mountains of Christmas', cursive;"><b>Advent of Code Cookiecutter</b></h1>


![Christmas Tree](https://images.unsplash.com/photo-1482289141412-c3c400927db2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2287&q=80)
<p style="text-align: center"><em>Photo by Thomas Kelley on Unsplash</em></p>

-----------

This project is intended to bootstrap the <a href="https://adventofcode.com/">Advent of Code</a> challenges a provide quick and easy experience to get up and running with them.

The following utilities have been provided out of the box:

- Function stubs for each of the challenges.
- Empty files to drop challenge inputs and solutions into.
- Unit test stubs for all of the challenges.
- Helper functions for loading challenge inputs and solutions.

--------

### Getting Started
To get up and running, simply fork this repository and clone it to your local development environment.

Next, to get the environment setup run `pip install -e .` in the root directory of the project containing the `setup.py` file. This is recomended to be done in a virtual environment.

For each days challenge, get the input from the Advent of Code website and paste it into the corresponding input file in `.advent_of_code\data\input` directory.

The next step is to implement the code to solve the challenge in the `part1()` & `part2()` functions in the corresponding days `day_{n}.py` file in the `.advent_of_code\challenges` directory. Output from the implemented solution will be written to file when the days challenges are executed in the `day_{n}.py` file. Answers are also output to the console so you they can be easily pasted into the Advent of Code website for validation.

Challenges can be executed by simply running the days challenge file. E.g. run `python day_1.py` in the `challenges` directory.

Now the answer is available unit tests can be executed against the correct solution to refactor solutions with confidence.

---------

### Modifying Generated File Templates

In addition to the out of the box utilites, templates are provided so the generated function and unit test stubs can be modified and regenerated according to the templates. Templates are written using [Jinja2](https://jinja.palletsprojects.com/en/2.10.x/).

1. Install the required dependencies into your Python environment by executing `pip install -r requirements.txt` in the root directory of the project containing the `requiements.txt` file. 
2. Modify the generated code modify the provided templates in the `.\generate\templates` directory as required.
4. Execute `generate.py`.

### Contributing

Contributions are very welcome and appreciated, Please see [the contribution guidelines](CONTRIBUTING.md) for for further details.