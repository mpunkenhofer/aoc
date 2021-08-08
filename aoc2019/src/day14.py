from common.util import read_input
import re
import math

def parse_reactions(reactions):
    regex = r"\s*(\d+)\s(\w+)"
    reaction_dict = {}

    for reaction in reactions:
        inputs, output = reaction.split('=>')
        inputs = [(re.match(regex, i).group(2), int(re.match(regex, i).group(1))) for i in inputs.split(',')]
        output = (re.match(regex, output).group(2), int(re.match(regex, output).group(1)))
        chemical, quantity = output
        reaction_dict[chemical] = (quantity, inputs)

    return reaction_dict


def sum_requirements(requirement_list):
    chemical_dict = {}

    for requirement in requirement_list:
        chemical, chemical_amount = requirement
        if chemical in chemical_dict:
            chemical_dict[chemical] += chemical_amount
        else:
            chemical_dict[chemical] = chemical_amount

    summed_requirements = []

    for chemical, chemical_amount in chemical_dict.items():
        summed_requirements.append((chemical, chemical_amount))

    return summed_requirements


def is_base_chemical(reactions, chemical):
    if chemical not in reactions:
        return True

    _, requirements = reactions[chemical]

    if len(requirements) != 1:
        return False

    chemical, _ = requirements[0]

    return not(chemical in reactions)


def calculate_requirements(reactions, target):
    base_requirements = []

    if target in reactions:
        quantity, requirements = reactions[target]

        while len(requirements) > 0:
            chemical, chemical_amount = requirements.pop()

            if chemical in reactions and not is_base_chemical(reactions, chemical):
                reaction_quantity, reaction_requirements = reactions[chemical]

                i = 0
                while i < chemical_amount:
                    requirements += reaction_requirements
                    i += reaction_quantity
            else:
                base_requirements += [(chemical, chemical_amount)]

            requirements = sum_requirements(requirements)

    base_requirements = sum_requirements(base_requirements)
    resource_requirements = []
    # return base_requirements

    while len(base_requirements) > 0:
        chemical, chemical_amount = base_requirements.pop()

        if chemical in reactions:
            quantity, resource = reactions[chemical]

            i = 0
            while i < chemical_amount:
                resource_requirements += resource
                i += quantity

    return sum_requirements(resource_requirements)
    # while amount > 0:
    #         for requirement in requirements:
    #             chemical, chemical_amount = requirement
    #             chemical_requirements = calculate_requirements(reactions, chemical, chemical_amount)
    #
    #             for base, base_amount in chemical_requirements.items():
    #                 if base in ret:
    #                     ret[base] += base_amount
    #                 else:
    #                     ret[base] = base_amount
    #
    #         amount -= quantity
    #
    #     return ret
    # else:
    #     return {target: amount}


def main():
    reaction_list = read_input('test_input3', '\n')
    reactions = parse_reactions(reaction_list)
    print('Answer for Day11 - Part 1: {}'.format(calculate_requirements(reactions, 'FUEL')))
    print('Answer for Day11 - Part 2: {}'.format(2))


if __name__ == "__main__":
    main()
