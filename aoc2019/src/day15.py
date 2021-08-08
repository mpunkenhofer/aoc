import pygame

from common.intcode import Intcode
from enum import Enum

import networkx as nx


class Movement(Enum):
    STOP = 0
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4


class Status(Enum):
    UNKNOWN = -1
    WALL = 0
    MOVED = 1
    OXYGEN_SYSTEM_FOUND = 2


class Mode(Enum):
    MANUAL = 0
    AUTOMATIC = 1


class Game:
    def __init__(self, game: Intcode, size=(700, 700), fps_limit=60, task1=True):
        pygame.init()
        pygame.display.set_caption('Maze')

        self.game = game
        self.game.reset()

        self.fps_limit = fps_limit
        self.task1 = task1
        self.unit_size = 15
        self.direction = Movement.STOP
        self.paused = False
        self.status_text = False
        self.explored = False
        self.mode = Mode.AUTOMATIC
        self.clock = pygame.time.Clock()
        self.big_font = pygame.font.Font('freesansbold.ttf', 24)
        self.normal_font = pygame.font.Font('freesansbold.ttf', 14)

        self.screen = pygame.display.set_mode(size)
        self.surface = pygame.Surface(size)

        self.view_center = (int(size[0] / 2), int(size[1] / 2))
        self.background_color = (0, 0, 0)
        self.wall_color = (245, 222, 179)
        self.floor_color = (0, 255, 0)
        self.robot_color = (255, 255, 0)
        self.oxygen_color = (255, 0, 0)
        self.text_color = (255, 255, 255)

        self.robot_pos = (0, 0)
        self.oxygen_pos = None
        self.oxygen_timer = 0

        self.floors = []
        self.walls = []
        self.filled = []
        self.to_fill = []

        self.junctions = []
        self.graph = nx.Graph()
        self.current_path = []

        self.surface.fill(self.background_color)

    def run(self):
        running = True

        while running:
            dt = self.clock.tick(self.fps_limit)
            running = self.handle_events()

            self.tick()
            self.render()
            self.draw()

        if self.task1:
            path = nx.shortest_path(self.graph, (0, 0), self.oxygen_pos)
            return len(path) - 1
        else:
            return self.oxygen_timer

    @staticmethod
    def opposite_direction(direction):
        opposite = Movement.STOP

        if direction == Movement.NORTH:
            opposite = Movement.SOUTH
        elif direction == Movement.SOUTH:
            opposite = Movement.NORTH
        elif direction == Movement.EAST:
            opposite = Movement.WEST
        elif direction == Movement.WEST:
            opposite = Movement.EAST

        return opposite

    def scan(self):
        next_pos = self.robot_pos
        paths = []

        for direction in Movement:
            if direction == Movement.STOP:
                continue

            status = self.game.execute(direction.value)

            if direction == Movement.NORTH:
                next_pos = (self.robot_pos[0], self.robot_pos[1] - 1)
            elif direction == Movement.SOUTH:
                next_pos = (self.robot_pos[0], self.robot_pos[1] + 1)
            elif direction == Movement.EAST:
                next_pos = (self.robot_pos[0] + 1, self.robot_pos[1])
            elif direction == Movement.WEST:
                next_pos = (self.robot_pos[0] - 1, self.robot_pos[1])

            if status == Status.MOVED.value or status == Status.OXYGEN_SYSTEM_FOUND.value:
                paths += [(direction, next_pos)]
                self.game.execute(self.opposite_direction(direction).value)
            elif status == Status.WALL.value:
                self.walls += [next_pos]

        return paths

    def tick(self):
        if not self.paused and not self.game.is_halted() and not self.explored:
            status = Status.UNKNOWN

            if self.mode == Mode.MANUAL and self.direction != Movement.STOP:
                status = self.game.execute(self.direction.value)
            elif self.mode == Mode.AUTOMATIC:
                if self.direction == Movement.STOP:
                    self.direction = Movement.NORTH

                if self.current_path:
                    next_node = self.current_path.pop(0)
                    ew, ns = (self.robot_pos[0] - next_node[0], self.robot_pos[1] - next_node[1])

                    if ns == -1:
                        self.direction = Movement.SOUTH
                    elif ns == 1:
                        self.direction = Movement.NORTH
                    elif ew == -1:
                        self.direction = Movement.EAST
                    elif ew == 1:
                        self.direction = Movement.WEST

                    status = self.game.execute(self.direction.value)

                    if status != Status.MOVED.value:
                        raise RuntimeError('This should not happen when pathing!')
                else:
                    paths = self.scan()
                    unexplored_paths = list(filter(lambda p: p[1] not in self.floors, paths))

                    if not unexplored_paths and self.junctions:
                        junction = self.junctions.pop()
                        self.current_path = nx.shortest_path(self.graph, self.robot_pos, junction)
                        self.current_path = self.current_path[1:]
                    elif unexplored_paths:
                        direction, _ = unexplored_paths.pop(0)
                        self.direction = direction
                        if unexplored_paths:
                            self.junctions.append(self.robot_pos)
                    else:
                        self.explored = True
                        self.center_view()

                    status = self.game.execute(self.direction.value)

            if status != Status.UNKNOWN:
                next_pos = self.robot_pos
                if self.direction == Movement.NORTH:
                    next_pos = (self.robot_pos[0], self.robot_pos[1] - 1)
                elif self.direction == Movement.SOUTH:
                    next_pos = (self.robot_pos[0], self.robot_pos[1] + 1)
                elif self.direction == Movement.EAST:
                    next_pos = (self.robot_pos[0] + 1, self.robot_pos[1])
                elif self.direction == Movement.WEST:
                    next_pos = (self.robot_pos[0] - 1, self.robot_pos[1])

                if status == Status.MOVED.value or status == Status.OXYGEN_SYSTEM_FOUND.value:
                    self.graph.add_edge(self.robot_pos, next_pos)
                    if self.robot_pos not in self.floors:
                        self.floors += [self.robot_pos]
                    self.robot_pos = next_pos
                    if status == Status.OXYGEN_SYSTEM_FOUND.value:
                        self.oxygen_pos = next_pos
                        self.filled.append(self.oxygen_pos)
                        if self.task1:
                            self.game.halt()
                elif status == Status.WALL.value:
                    if next_pos not in self.walls:
                        self.walls += [next_pos]

                if self.mode == Mode.MANUAL:
                    self.direction = Movement.STOP
        elif self.explored:
            if not self.to_fill and len(self.filled) <= 1:
                self.to_fill = list(self.graph[self.oxygen_pos])
            else:
                if self.to_fill:
                    self.oxygen_timer += 1

                next_to_fill = []

                while self.to_fill:
                    node = self.to_fill.pop()
                    self.filled.append(node)
                    next_to_fill += list(filter(lambda p: p not in self.filled, self.graph[node]))

                self.to_fill = next_to_fill

    def render(self):
        self.surface.fill(self.background_color)

        self.draw_units(self.wall_color, *self.walls)
        self.draw_units(self.floor_color, *self.floors)
        self.draw_units(self.oxygen_color, self.oxygen_pos)
        self.draw_units(self.robot_color, self.robot_pos)
        self.draw_units(self.oxygen_color, *self.filled)

        if self.status_text:
            self.draw_status_text()

        if self.paused:
            self.draw_text(self.big_font, 'Paused')

        if self.explored:
            self.draw_text(self.big_font,
                           'Oxygen Level: {:.2f}, Time: {}'.format(((len(self.filled) - 1) / len(self.floors)) * 100,
                                                                   self.oxygen_timer))
        if self.game.is_halted() and self.task1:
            try:
                path = nx.shortest_path(self.graph, (0, 0), self.oxygen_pos)
                self.draw_text(self.big_font, 'Task 1 done: {} steps.'.format(len(path) - 1))
                self.draw_small_units((255, 0, 240), *path)
            except nx.NodeNotFound:
                print('Node not found.')

        elif self.game.is_halted():
            self.draw_text(self.big_font, 'Game Over')

    def draw_units(self, color, *args):
        for arg in args:
            if arg is None:
                break
            pygame.draw.rect(self.surface, color, ((arg[0] - self.robot_pos[0]) * self.unit_size + self.view_center[0],
                                                   (arg[1] - self.robot_pos[1]) * self.unit_size + self.view_center[1],
                                                   self.unit_size, self.unit_size))

    def draw_small_units(self, color, *args):
        for arg in args:
            if arg is None:
                break
            pygame.draw.rect(self.surface, color, ((arg[0] - self.robot_pos[0]) * self.unit_size + self.view_center[0],
                                                   (arg[1] - self.robot_pos[1]) * self.unit_size + self.view_center[1],
                                                   int(self.unit_size / 3), int(self.unit_size / 3)))

    def draw_text(self, font, text, color=(255, 255, 255), pos=None):
        text = font.render(text, True, color, self.background_color)
        rect = text.get_rect()
        if pos is None:
            rect.center = self.surface.get_width() / 2, 20
        else:
            rect.left = pos[0]
            rect.top = pos[1]

        self.surface.blit(text, rect)

    def draw_status_text(self):
        color = (255, 240, 230)
        x = self.surface.get_width() - 150
        y = 20
        spacing = 18

        self.draw_text(self.normal_font, 'Mode: {}'.format('Automatic' if self.mode == Mode.AUTOMATIC else 'Manual'),
                       color, (x, y))
        self.draw_text(self.normal_font, 'Pos: {}'.format(self.robot_pos), color, (x, y + spacing))
        self.draw_text(self.normal_font, 'Pathing: {}'.format(len(self.current_path)), color, (x, y + spacing * 2))
        self.draw_text(self.normal_font, 'Floor Tiles: {}'.format(len(self.floors)), color, (x, y + spacing * 3))
        self.draw_text(self.normal_font, 'Wall Tiles: {}'.format(len(self.walls)), color, (x, y + spacing * 4))
        self.draw_text(self.normal_font, 'Oxygen Filled: {}'.format(len(self.filled)), color, (x, y + spacing * 5))

    def draw(self):
        self.screen.blit(self.surface, (0, 0))
        pygame.display.update()

    def center_view(self):
        self.view_center = (self.view_center[0] + self.robot_pos[0] * self.unit_size,
                            self.view_center[1] + self.robot_pos[1] * self.unit_size)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_F1:
                    self.status_text = not self.status_text
                if event.key == pygame.K_w:
                    self.view_center = (self.view_center[0], self.view_center[1] + 2 * self.unit_size)
                if event.key == pygame.K_s:
                    self.view_center = (self.view_center[0], self.view_center[1] - 2 * self.unit_size)
                if event.key == pygame.K_a:
                    self.view_center = (self.view_center[0] + 2 * self.unit_size, self.view_center[1])
                if event.key == pygame.K_d:
                    self.view_center = (self.view_center[0] - 2 * self.unit_size, self.view_center[1])
                if event.key == pygame.K_LEFT:
                    self.direction = Movement.WEST
                if event.key == pygame.K_RIGHT:
                    self.direction = Movement.EAST
                if event.key == pygame.K_UP:
                    self.direction = Movement.NORTH
                if event.key == pygame.K_DOWN:
                    self.direction = Movement.SOUTH
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                if event.key == pygame.K_BACKSPACE:
                    self.__init__(self.game)
                if event.key == pygame.K_1:
                    if self.mode == Mode.MANUAL:
                        self.mode = Mode.AUTOMATIC
                    else:
                        self.mode = Mode.MANUAL
                    print('Mode: {}'.format(self.mode))

        return True


def main():
    game = Game(Intcode('input'), task1=True)
    fewest_movement_commands = game.run()
    print('Answer for Day15 - Part 1: {}'.format(fewest_movement_commands))

    game = Game(Intcode('input'), fps_limit=90, task1=False)
    minutes_until_filled = game.run()
    print('Answer for Day15 - Part 2: {}'.format(minutes_until_filled))


if __name__ == "__main__":
    main()
