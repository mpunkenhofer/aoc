from common.util import read_input


def run_program(memory, instruction_pointer=0):
    if instruction_pointer + 3 > len(memory):
        return memory

    opcode = memory[instruction_pointer]
    op1_addr, op2_addr = memory[instruction_pointer + 1], memory[instruction_pointer + 2]
    store_addr = memory[instruction_pointer + 3]

    if opcode == 1:
        memory[store_addr] = memory[op1_addr] + memory[op2_addr]
    elif opcode == 2:
        memory[store_addr] = memory[op1_addr] * memory[op2_addr]
    elif opcode == 99:
        return memory
    else:
        return memory

    return run_program(memory, instruction_pointer + 4)


def main():
    program = list(map(int, read_input(separator=',')))
    memory = program.copy()
    memory[1] = 12
    memory[2] = 2
    memory = run_program(memory)
    print('Answer to Day 2 - Part 1: {}'.format(memory[0]))

    for noun in range(99):
        for verb in range(99):
            memory = program.copy()
            memory[1] = noun
            memory[2] = verb
            memory = run_program(memory)
            if memory[0] == 19690720:
                print('Answer to Day 2 - Part 2: noun {} verb {}; Answer: {}'.format(noun, verb, 100 * noun + verb))


if __name__ == "__main__":
    main()
