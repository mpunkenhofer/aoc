from src.common.util import read_input


def memory_game(starting_numbers, round):
    memory = {number: [i + 1] for i, number in enumerate(starting_numbers)}
    last_number = 0

    for turn in range(len(memory) + 1, round):
        if last_number in memory:
            memory[last_number].append(turn)
            diff = memory[last_number][-1] - memory[last_number][-2]
            if diff > 0:
                last_number = diff
            else:
                last_number = 0
            
        else:
            memory[last_number] = [turn]
            last_number = 0

    return memory, last_number

def part_one(input):
    return memory_game([int(i) for i in input], 2020)[1]


def part_two(input):
    return memory_game([int(i) for i in input], 30000000)[1]

def main():
    print('Day 15: Answer for Part 1 {}'.format(
        part_one(read_input('inputs/input_day15.txt', ','))))
    print('Day 15: Answer for Part 2: {}'.format(
        part_two(read_input('inputs/input_day15.txt', ','))))


if __name__ == "__main__":
    main()
