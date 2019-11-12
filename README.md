<link href="https://fonts.googleapis.com/css?family=Mountains+of+Christmas&display=swap" rel="stylesheet">

<h1 style="text-align: center; font-family: 'Mountains of Christmas', cursive;"><b>Advent of Code Cookiecutter</b></h1>


![Christmas Tree](https://images.unsplash.com/photo-1482289141412-c3c400927db2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2287&q=80)
<p style="text-align: center"><em>Photo by Thomas Kelley on Unsplash</em></p>

-----------

This project is here to get up and running with the <a href="https://adventofcode.com/">Advent of Code</a> challenges a quick and easy experience.

The following utilities have been provided out of the box:

- Function stubs for each of the challenges.
- Empty files to drop challenge inputs and solutions into.
- Unit test stubs for all of the challenges.
- Helper functions for loading challenge inputs and solutions.

--------

### Getting Started
To get up and running, simply fork this repository and clone it to your local development environment.

For each days challenge, get the input from the Advent of Code website and paste it into the corresponding input file in `.\data\inputs` directory.

Next implement the code to solve the challenge in the `part1()` & `part2()` functions in the corresponding days challenge file in the `.\challenges` directory.

Once you have succesfully solved the challenge and validated it in the Advent of Code website, paste your answer text into the corresponding `part1.txt` or `part2.txt` solution file in the `.\data\answers\day{n}` directory.

Now the answer is available unit tests can be executed against the correct solution to refactor solutions with confidence.

---------

### Modifying Generated File Templates

In addition to the out of the box utilites, templates are provided so the generated function and unit test stubs can be modified and regenerated according to the templates. Templates are written using [Jinja2](https://jinja.palletsprojects.com/en/2.10.x/)