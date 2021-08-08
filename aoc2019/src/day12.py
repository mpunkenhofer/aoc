from common.util import read_input
import numpy as np
import re


class System:
    def __init__(self, filename):
        positions = read_input(filename, separator='\n')
        regex = r"x=(-?\d+).+y=(-?\d+).+z=(-?\d+)"
        self.bodies = []

        for body_pos in positions:
            match = re.search(regex, body_pos)
            pos = int(match.group(1)), int(match.group(2)), int(match.group(3))
            self.bodies.append(CelestialBody(pos))

    def simulate(self, steps=1):
        for i in range(steps):
            for body in self.bodies:
                body.calculate(self.bodies)
            for body in self.bodies:
                body.apply()

    def energy(self):
        return sum([body.energy() for body in self.bodies])

    def stationary(self):
        for body in self.bodies:
            if body.kinetic_energy() > 0:
                return False
        return True

    def __str__(self):
        return '{}'.format('\n'.join(map(str, self.bodies)))


class CelestialBody:
    def __init__(self, pos=None):
        if pos is not None:
            self.position = np.array(pos, dtype=float)
        else:
            self.position = np.zeros(3, dtype=float)

        self.velocity = np.zeros(3, dtype=float)

    def __str__(self):
        return 'pos=<x={:5}, y={:5}, z={:5}>, vel=<x={:5}, y={:5}, z={:5}>'.format(
            self.position[0], self.position[1], self.position[2],
            self.velocity[0], self.velocity[1], self.velocity[2])

    def calculate(self, moons):
        for moon in moons:
            if moon == self:
                continue

            for i in range(len(self.position)):
                if self.position[i] != moon.position[i]:
                    change = 1 if self.position[i] < moon.position[i] else -1
                    self.velocity[i] += change

    def apply(self):
        self.position += self.velocity

    def potential_energy(self):
        return np.sum(np.abs(self.position))

    def kinetic_energy(self):
        return np.sum(np.abs(self.velocity))

    def energy(self):
        return self.potential_energy() * self.kinetic_energy()


def calculate_loop_length(system):
    system.simulate()
    step_count = 1

    while not system.stationary():
        system.simulate()
        step_count += 1

    return step_count


def main():
    filename = 'input'
    steps = 1000

    system = System(filename)

    print('Initial System:')
    print(system)

    system.simulate(steps)
    print('After {} steps'.format(steps))
    print(system)

    print('Answer for Day12 - Part 1: {}'.format(system.energy()))

    system = System(filename)

    loop_length = calculate_loop_length(system)
    print('After loop:')
    print(system)

    print('Answer for Day12 - Part 2: {} * 2 = {}'.format(loop_length, loop_length * 2))


if __name__ == "__main__":
    main()
