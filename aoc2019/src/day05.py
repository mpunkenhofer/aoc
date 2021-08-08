from common.intcode import Intcode


def main():
    program = Intcode('input')
    print('Answer for Day5 - Part 1: {}'.format(program.execute(1)))
    program.reset()
    print('Answer for Day5 - Part 2: {}'.format(program.execute(5)))


if __name__ == "__main__":
    main()
