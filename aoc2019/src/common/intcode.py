from common.util import read_input


class Intcode:
    def __init__(self, filename, *args):
        if type(filename) is str:
            self.__program = self.load(filename)
        else:
            self.__program = filename

        self.__inputs = list(args)

        self.__memory = self.__program.copy()
        self.__outputs = []
        self.__ip = 0
        self.__rb = 0
        self.__halt = False
        self.__awaiting_input = False

    @staticmethod
    def load(filename):
        return list(map(int, read_input(filename=filename, separator=',')))

    def reset(self):
        self.__memory = self.__program.copy()
        self.__outputs = []
        self.__ip = 0
        self.__rb = 0
        self.__halt = False
        self.__awaiting_input = False

    def execute(self, *args):
        self.__awaiting_input = False
        arguments = list(args)
        self.__inputs += arguments

        while not self.__halt and self.__ip < len(self.__memory):
            opcode = self.get_opcode()

            if opcode == 1:
                self.parameter(3, self.parameter(1) + self.parameter(2))
                self.__ip += 4
            elif opcode == 2:
                self.parameter(3, self.parameter(1) * self.parameter(2))
                self.__ip += 4
            elif opcode == 3:
                if len(self.__inputs) > 0:
                    self.parameter(1, self.__inputs.pop(0))
                    self.__ip += 2
                else:
                    self.__awaiting_input = True
                    break
            elif opcode == 4:
                self.__outputs.append(self.parameter(1))
                self.__ip += 2
            elif opcode == 5:
                if self.parameter(1) != 0:
                    self.__ip = self.parameter(2)
                else:
                    self.__ip += 3
            elif opcode == 6:
                if self.parameter(1) == 0:
                    self.__ip = self.parameter(2)
                else:
                    self.__ip += 3
            elif opcode == 7:
                if self.parameter(1) < self.parameter(2):
                    self.parameter(3, 1)
                else:
                    self.parameter(3, 0)
                self.__ip += 4
            elif opcode == 8:
                if self.parameter(1) == self.parameter(2):
                    self.parameter(3, 1)
                else:
                    self.parameter(3, 0)
                self.__ip += 4
            elif opcode == 9:
                self.__rb += self.parameter(1)
                self.__ip += 2
            elif opcode == 99:
                self.halt()
                break
            else:
                raise RuntimeError('Unknown opcode: {}'.format(opcode))

        outputs = self.__outputs
        self.__outputs = []

        if len(outputs) < 1:
            return None
        elif len(outputs) == 1:
            return outputs[0]
        else:
            return outputs

    def get_memory(self, pos=-1):
        if pos >= 0:
            if pos >= len(self.__memory):
                return 0
            else:
                return self.__memory[pos]
        return self.__memory

    def parameter(self, nr=1, value=None):
        instruction = str(self.get_memory(self.__ip))

        if nr + 2 > len(instruction):
            mode = 0
        else:
            mode = int(instruction[-2 - nr:-1 - nr])

        if mode == 1:
            # immediate mode
            return self.get_memory(self.__ip + nr)
        elif mode == 2:
            # relative mode
            relative = self.__rb + self.get_memory(self.__ip + nr)
            if value is not None:
                self.store(relative, value)
            else:
                return self.get_memory(relative)
        else:
            # position mode
            addr = self.get_memory(self.__ip + nr)
            if value is not None:
                self.store(addr, value)
            else:
                return self.get_memory(addr)

    def get_opcode(self):
        if self.__ip > len(self.__memory):
            self.halt()
        else:
            instruction = str(self.get_memory(self.__ip))

            if len(instruction) < 2:
                if len(instruction) < 1:
                    return 99
                else:
                    instruction = '0{}'.format(instruction)

            return int(instruction[-2:])

    def store(self, addr, value):
        if addr >= len(self.__memory):
            self.__memory += [0] * abs((addr + 1) - len(self.__memory))
        if addr >= 0:
            self.__memory[addr] = value

    def halt(self):
        self.__halt = True

    def is_halted(self):
        return self.__halt

    def awaiting_input(self):
        return self.__awaiting_input
