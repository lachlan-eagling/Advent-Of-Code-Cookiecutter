from advent_of_code.utils import load_input, save_answers
import math

# Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

modules = load_input(1)
part1_individual = []
part2_individual = []

def part1():

    for module in modules:
        fuel = ( math.floor( int(module) / 3 ) ) - 2
        part1_individual.append(fuel)
        # print(fuel)

    total = sum(part1_individual)
    return total


def part2():
    # for each module mass, calculate its fuel and add it to the total
    # treat the fuel amount you just calculated as the input mass and repeat the process, 
    # continuing until a fuel requirement is zero or negative.
    def check_fuel(fuel, module_total):
        print(f'calculating fuel for volume: {fuel}')
        volume = math.floor(fuel / 3) - 2
        
        if volume >= 0:
            print(f'Adding {volume} for a total of {module_total}')
            module_total += volume
            print(f'Recursing for remaining {volume}')
            check_fuel(volume, module_total)
        else:
            print(f'Returning {module_total}')
            part2_individual.append(module_total)
            return module_total

    for module in modules:
        print(f'STARTING ========================== {int(module)}')
        fuel = check_fuel(int(module), 0)

    return sum(part2_individual)
    # return "Challenge not completed."


if __name__ == "__main__":
    answer1 = part1()
    answer2 = part2()
    print(f"Day 1 - Part 1 Answer: {answer1}")
    print(f"Day 1 - Part 2 Answer: {answer2}")
    save_answers(answer1, 1, 1)
    save_answers(answer2, 1, 2)
