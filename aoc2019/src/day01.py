from math import floor
from common.util import read_input


def calculate_fuel_requirements(fuel, total=0):
    fuel_requirement = floor(fuel / 3) - 2
    if fuel_requirement <= 0:
        return total
    else:
        return calculate_fuel_requirements(fuel_requirement, total + fuel_requirement)


def main():
    # Part day1
    modules = [int(number) for number in read_input('input', '\n')]
    fuel_requirements = [floor(module / 3) - 2 for module in modules]
    total_fuel_requirement = sum(fuel_requirements)
    print('Answer for Part day1: {}'.format(total_fuel_requirement))

    # Part day2
    new_fuel_requirements = [calculate_fuel_requirements(module) for module in modules]
    print('Answer for Part day2: {}'.format(sum(new_fuel_requirements)))


if __name__ == "__main__":
    main()
