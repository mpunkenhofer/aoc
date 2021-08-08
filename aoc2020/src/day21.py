import re
import heapq
from src.common.util import read_input

def prase_input(input):
    allergens_dict, food_list = {}, []

    for line in input:
            ingredients, allergens = line.split('(')
            allergens_match = re.match(r'contains (.+)\)', allergens)

            if allergens_match:
                allergens = allergens_match.group(1).split(', ')
                ingredients = ingredients.strip().split(' ')

                for allergen in allergens:
                    if allergen in allergens_dict:
                        allergens_dict[allergen] += [ingredients]
                    else:
                        allergens_dict[allergen] = [ingredients]
                
                food_list.append(ingredients)
    
    return allergens_dict, food_list

def food_occurences(allergens):
    result = {}

    for allergen, foods in allergens.items():
        for food in foods:
            if food in result:
                result[food] |= set([allergen])
            else:
                result[food] = set([allergen])
    
    return result

def part_one(input):
    allergens, foods = prase_input(input)

    bound_ingredients = set()

    for allergen in allergens:
        bound_ingredients |= set.intersection(*map(set, allergens[allergen]))

    return sum(map(len, map(lambda f: list(filter(lambda i: i not in bound_ingredients, f)), foods)))

def part_two(input):
    allergens, _ = prase_input(input)

    for allergen in allergens:
        allergens[allergen] = set.intersection(*map(set, allergens[allergen]))
    
    result = {}
    stack = list(food_occurences(allergens).items())

    while stack:
        index = 0

        for i, (_, allergens) in enumerate(stack):
            if len(allergens) == 1:
                index = i
                break

        food, allergen = stack.pop(index)
        result[next(iter(allergen))] = food

        for i, (food, allergens) in enumerate(stack):
            stack[i] = (food, allergens - allergen)

    sorted_result = sorted(result.items(), key=lambda i: i[0])

    return ','.join(map(lambda i: i[1], sorted_result))


def main():
    print('Day 21: Answer for Part 1 {}'.format(
        part_one(read_input('inputs/input_day21.txt', '\n'))))
    print('Day 21: Answer for Part 2: {}'.format(
        part_two(read_input('inputs/input_day21.txt', '\n'))))


if __name__ == "__main__":
    main()
