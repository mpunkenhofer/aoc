import pygame
import networkx as nx
from common.intcode import Intcode
from enum import Enum


class Direction(Enum):
    UNKNOWN = 0
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4


class Game:
    def __init__(self, game: Intcode, size=(600, 600), fps_limit=60, task1=True):
        pygame.init()
        pygame.display.set_caption('Day 17')

        self.game = game
        self.game.reset()

        self.fps_limit = fps_limit
        self.unit_size = 10
        self.paused = False
        self.status_text = False
        self.task1 = task1
        self.clock = pygame.time.Clock()
        self.big_font = pygame.font.Font('freesansbold.ttf', 24)
        self.normal_font = pygame.font.Font('freesansbold.ttf', 14)

        self.screen = pygame.display.set_mode(size)
        self.surface = pygame.Surface(size)

        self.view_center = (int(size[0] / 2), int(size[1] / 2))
        self.background_color = (0, 0, 0)
        self.floor_color = (0, 255, 0)
        self.intersection_color = (255, 0, 0)
        self.robot_color = (255, 255, 0)
        self.text_color = (255, 255, 255)

        self.robot_pos = (0, 0)
        self.robot_direction = Direction.UNKNOWN

        self.score = 0

        self.graph = nx.Graph()

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
            alignment_parameters = []
            for intersection in self.get_intersections():
                alignment_parameters.append(intersection[0] * intersection[1])
            return sum(alignment_parameters)
        else:
            return self.score

    def create_graph(self):
        if self.graph.size() == 0:
            for node in self.graph:
                if (node[0], node[1] + 1) in self.graph:
                    self.graph.add_edge(node, (node[0], node[1] + 1))
                if (node[0], node[1] - 1) in self.graph:
                    self.graph.add_edge(node, (node[0], node[1] - 1))
                if (node[0] + 1, node[1]) in self.graph:
                    self.graph.add_edge(node, (node[0] + 1, node[1]))
                if (node[0] - 1, node[1]) in self.graph:
                    self.graph.add_edge(node, (node[0] - 1, node[1]))

    def get_intersections(self):
        intersections = []

        for node in self.graph:
            neighbors = list(self.graph.neighbors(node))
            if len(neighbors) > 3:
                intersections.append(node)

        return intersections

    def calculate_path(self):
        robot = self.robot_pos

    def tick(self):
        if self.graph.size() == 0:
            screen_data = self.game.execute()

            if screen_data:
                x, y = 0, 0

                for data in screen_data:
                    if data == 10:
                        x = 0
                        y += 1
                        continue
                    elif data == ord('#'):
                        self.graph.add_node((x, y))
                    elif data == ord('<'):
                        self.robot_direction = Direction.WEST
                        self.robot_pos = (x, y)
                    elif data == ord('>'):
                        self.robot_direction = Direction.EAST
                        self.robot_pos = (x, y)
                    elif data == ord('^'):
                        self.robot_direction = Direction.NORTH
                        self.robot_pos = (x, y)
                    elif data == ord('v'):
                        self.robot_direction = Direction.SOUTH
                        self.robot_pos = (x, y)
                    elif data == ord('X'):
                        self.robot_direction = Direction.UNKNOWN
                        self.robot_pos = (x, y)

                    x += 1

                self.create_graph()
                self.center_view((-20, 10))

                if not self.task1:
                    path = self.calculate_path()

    def render(self):
        self.surface.fill(self.background_color)

        self.draw_units(self.floor_color, *self.graph.nodes)
        self.draw_units(self.robot_color, self.robot_pos)

        if self.status_text:
            self.draw_status_text()

        if self.paused:
            self.draw_text(self.big_font, 'Paused')

        if self.game.is_halted():
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
                                                   int(self.unit_size / 2), int(self.unit_size / 2)))

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

        # self.draw_text(self.normal_font, 'Pos: {}'.format(self.robot_pos), color, (x, y + spacing))

    def draw(self):
        self.screen.blit(self.surface, (0, 0))
        pygame.display.update()

    def center_view(self, node=None):
        if node is not None:
            center_node = node
        else:
            center_node = (0, 0)
        self.view_center = (self.view_center[0] + center_node[0] * self.unit_size,
                            self.view_center[1] + center_node[1] * self.unit_size)

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
                    pass
                if event.key == pygame.K_RIGHT:
                    pass
                if event.key == pygame.K_UP:
                    pass
                if event.key == pygame.K_DOWN:
                    pass
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                if event.key == pygame.K_BACKSPACE:
                    self.__init__(self.game)

        return True


def main():
    # game = Game(Intcode('input'))
    # calibration_parameter = game.run()
    # print('Answer for Day17 - Part 1: {}'.format(calibration_parameter))
    game = Game(Intcode('input'))
    dust = game.run()
    print('Answer for Day17 - Part 2: {}'.format(dust))


if __name__ == "__main__":
    main()
