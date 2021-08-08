from collections import Counter


def only_double_digits(digits):
    for v in Counter(digits).values():
        if v == 2:
            return True

    return False


def double_digits(digits):
    for i in range(len(digits) - 1):
        if digits[i] == digits[i + 1]:
            return True
    return False


def increasing_digits(digits):
    for i in range(len(digits) - 1):
        if digits[i] > digits[i + 1]:
            return False

    return True


def valid_passwords_p1(start, end):
    valid_pws = []

    for number in range(start, end):
        digits = list(str(number))

        if increasing_digits(digits) and double_digits(digits):
            valid_pws.append(number)

    return valid_pws


def valid_passwords_p2(start, end):
    valid_pws = []

    for number in range(start, end):
        digits = list(str(number))
        if increasing_digits(digits) and only_double_digits(digits):
            valid_pws.append(number)

    return valid_pws


def main():
    valid_passwords1 = valid_passwords_p1(245182, 790572)
    print('Answer to Day 4 - Part 1: {}'.format(len(valid_passwords1)))

    valid_passwords2 = valid_passwords_p2(245182, 790572)
    print('Answer to Day 4 - Part 2: {}'.format(len(valid_passwords2)))


if __name__ == "__main__":
    main()
