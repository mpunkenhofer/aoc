import itertools

from common.intcode import Intcode


def amplifier(program_filename, phase_setting, value):
    program = Intcode(program_filename)
    output = program.execute(phase_setting, value)

    if output is None:
        raise RuntimeError('Expected output but got none.')

    return output


def amplify(program, phase_setting_sequence):
    if len(phase_setting_sequence) < 1:
        return 0

    value = amplifier(program, phase_setting_sequence[0], 0)

    for i in range(1, len(phase_setting_sequence)):
        value = amplifier(program, phase_setting_sequence[i], value)

    return value


def feedback_amplify(program, phase_setting_sequence):
    amplifiers = [Intcode(program, ps) for ps in phase_setting_sequence]

    last_output = 0

    while not amplifiers[-1].is_halted():
        for amp in amplifiers:
            last_output = amp.execute(last_output)

    return last_output


def max_thruster_signal(program_filename, amp_function, phase_setting_range):
    max_ts = 0

    for sequence in itertools.permutations(phase_setting_range, len(phase_setting_range)):
        max_ts = max(amp_function(program_filename, sequence), max_ts)

    return max_ts


def main():
    print('Answer for Day7 - Part 1: {}'.format(max_thruster_signal('input', amplify, range(5))))
    print('Answer for Day7 - Part 2: {}'.format(max_thruster_signal('input', feedback_amplify, range(5, 10))))


if __name__ == "__main__":
    main()
