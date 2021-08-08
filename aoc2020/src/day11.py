import pygame

from src.common.util import read_input

def occupied_adjacent(seats, coordinate):
    count = 0

    for y in range(max(0, coordinate[1] - 1), min(coordinate[1] + 2, len(seats))):
        for x in range(max(0, coordinate[0] - 1), min(coordinate[0] + 2, len(seats[y]))):
            if (x, y) != coordinate and seats[y][x] == '#':
                count += 1

    return count

def scan_seats(seats, location, xdir, ydir):
    x, y = location[0] + xdir, location[1] + ydir

    while y >= 0 and y < len(seats) and x >= 0 and x < len(seats[y]):
        seat = seats[y][x]
        if seat == '#':
            return 1
        elif seat == 'L':
            break
        
        x += xdir
        y += ydir

    return 0

def occupied_visible(seats, location):
    count = 0
    
    count += scan_seats(seats, location, 1, 0)
    count += scan_seats(seats, location, 0, 1)
    count += scan_seats(seats, location, -1, 0)
    count += scan_seats(seats, location, 0, -1)
    count += scan_seats(seats, location, 1, 1)
    count += scan_seats(seats, location, -1, 1)
    count += scan_seats(seats, location, 1, -1)
    count += scan_seats(seats, location, -1, -1)

    return count

class Simulation:
    def __init__(self, input, size=(700, 700), unit_size=6, fps_limit=60, p2=False):
        pygame.init()
        pygame.display.set_caption('Seating System')

        self.paused = False
        self.unit_size = unit_size
        self.view_center = (int(size[0] / 2), int(size[1] / 2))
        self.view_center = self.view_center[0] - (len(input) * self.unit_size) / 2, self.view_center[1] - (len(input) * self.unit_size) / 2

        self.screen = pygame.display.set_mode(size)
        self.surface = pygame.Surface(size)
        self.clock = pygame.time.Clock()
        self.fps_limit = fps_limit

        self.big_font = pygame.font.Font('freesansbold.ttf', 24)
        self.normal_font = pygame.font.Font('freesansbold.ttf', 14)

        self.background_color = (0, 0, 0)
        self.empty_color = (0, 255, 0)
        self.occupied_color = (255, 0, 0)
        self.floor_color = (245, 222, 179)

        self.p2 = p2

        self.input = input
        self.seats = input

        self.surface.fill(self.background_color)

    def run(self):
        running = True

        while running:
            self.clock.tick(self.fps_limit)
            running = self.handle_events()

            if self.p2:
                changes = self.tock()
            else:
                changes = self.tick()

            if not self.paused and changes == 0:
                break

            self.render()
            self.draw()

        return sum([row.count('#') for row in self.seats])



    def tick(self):
        changes = 0
        seats_next_round = []

        if not self.paused:
            for y, row in enumerate(self.seats):
                next_round_row = []
                for x, seat in enumerate(row):
                    adjacent = occupied_adjacent(self.seats, (x, y))
                    if seat == 'L' and adjacent == 0:
                        next_round_row.append('#')
                        changes += 1
                    elif seat == '#' and adjacent >= 4:
                        next_round_row.append('L')
                        changes += 1
                    else:
                        next_round_row.append(seat)
                seats_next_round.append(next_round_row)
            
            self.seats = seats_next_round

        return changes

    def tock(self):
        changes = 0
        seats_next_round = []

        if not self.paused:
            for y, row in enumerate(self.seats):
                next_round_row = []
                for x, seat in enumerate(row):
                    adjacent = occupied_visible(self.seats, (x, y))
                    if seat == 'L' and adjacent == 0:
                        next_round_row.append('#')
                        changes += 1
                    elif seat == '#' and adjacent >= 5:
                        next_round_row.append('L')
                        changes += 1
                    else:
                        next_round_row.append(seat)
                seats_next_round.append(next_round_row)
            
            self.seats = seats_next_round

            # print('')

            # for seat in self.seats:
            #     print(''.join(seat))

        return changes

    def render(self):
        self.surface.fill(self.background_color)

        for y, row in enumerate(self.seats):
            for x, seat in enumerate(row):
                if seat == 'L':
                    self.draw_units(self.empty_color, (x, y))
                elif seat == '#':
                    self.draw_units(self.occupied_color, (x, y))
                elif seat == '.':
                    self.draw_units(self.floor_color, (x, y))

        if self.paused:
            self.draw_text(self.big_font, 'Paused')

    def draw(self):
        self.screen.blit(self.surface, (0, 0))
        pygame.display.update()

    def draw_units(self, color, *args):
        for arg in args:
            pygame.draw.rect(self.surface, color, (arg[0] * self.unit_size + self.view_center[0],
                                                   arg[1] * self.unit_size + self.view_center[1], self.unit_size, self.unit_size))

    def draw_text(self, font, text, color=(255, 255, 255), pos=None):
        text = font.render(text, True, color, self.background_color)
        rect = text.get_rect()
        if pos is None:
            rect.center = self.surface.get_width() / 2, 20
        else:
            rect.left = pos[0]
            rect.top = pos[1]

        self.surface.blit(text, rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_UP:
                    self.view_center = (
                        self.view_center[0], self.view_center[1] + 2 * self.unit_size)
                if event.key == pygame.K_DOWN:
                    self.view_center = (
                        self.view_center[0], self.view_center[1] - 2 * self.unit_size)
                if event.key == pygame.K_LEFT:
                    self.view_center = (
                        self.view_center[0] + 2 * self.unit_size, self.view_center[1])
                if event.key == pygame.K_RIGHT:
                    self.view_center = (
                        self.view_center[0] - 2 * self.unit_size, self.view_center[1])
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                if event.key == pygame.K_BACKSPACE:
                    self.__init__(self.input)

        return True


def part_one(input, unit_size=6, fps_limit=4):
    seat_simulation = Simulation(input, unit_size=unit_size, fps_limit=fps_limit)
    return seat_simulation.run()


def part_two(input, unit_size=6, fps_limit=4):
    seat_simulation = Simulation(input, unit_size=unit_size, fps_limit=fps_limit, p2=True)
    return seat_simulation.run()


def main():
    print('Day 11: Answer for Part 1 {}'.format(
        part_one(read_input('inputs/input_day11.txt', '\n'), fps_limit=60)))
    print('Day 11: Answer for Part 2: {}'.format(
        part_two(read_input('inputs/input_day11.txt', '\n'))))


if __name__ == "__main__":
    main()
