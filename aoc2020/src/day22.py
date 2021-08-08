import re
from src.common.util import read_input

def prase_input(input):
    decks = [], []
    player_one = True

    for line in input:
        card_match = re.match(r'(\d+)', line)

        if card_match:
            card = int(card_match.group(1))
            decks[0 if player_one else 1].append(card)
        elif not line:
            player_one = not player_one
    
    return decks

def combat(first, second):
    first, second = list(first), list(second)

    while first and second:
        f_card, s_card = first.pop(0), second.pop(0)
        if f_card > s_card:
            first += [f_card, s_card]
        else:
            second += [s_card, f_card]

    return first, second

def score(deck):
    return sum(map(lambda t: t[0] * t[1], zip(deck, range(len(deck), 0, -1))))


def recursive_combat(first, second, game=1):
    seen = set()

    while first and second:
        #same cards & same order rule
        decks = (tuple(first), tuple(second))

        if decks in seen:
            return first, []
        else:
            seen.add(decks)

        # draw top cards
        f_card, s_card = first.pop(0), second.pop(0)

        # sub game rule
        if len(first) >= f_card and len(second) >= s_card:
            # make copies of the decks
            sub_first, _ = recursive_combat(list(first[:f_card]), list(second[:s_card]), game + 1)

            if sub_first:
                first += [f_card, s_card]
            else:
                second += [s_card, f_card]
        else:
            if f_card > s_card:
                first += [f_card, s_card]
            else:
                second += [s_card, f_card]

    return first, second

def play_game(input, game_mode):
    first, second = prase_input(input)

    first, second = game_mode(first, second)

    deck = first if first else second

    return score(deck)

def part_one(input):
    return play_game(input, combat)

def part_two(input):
    return play_game(input, recursive_combat)

def main():
    print('Day 22: Answer for Part 1 {}'.format(
        part_one(read_input('inputs/input_day22.txt', '\n'))))
    print('Day 22: Answer for Part 2: {}'.format(
        part_two(read_input('inputs/input_day22.txt', '\n'))))


if __name__ == "__main__":
    main()
