import numpy as np
import pygame
import math

from common.intcode import Intcode


class Game:
    def __init__(self, game: Intcode, size=(660, 345), fps_limit=60):
        pygame.init()
        pygame.display.set_caption('Asteroids')

        self.game = game
        self.fps_limit = fps_limit
        self.score = 0
        self.unit_size = 0
        self.joystick_pos = 0
        self.paused = False
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('freesansbold.ttf', 24)

        self.screen = pygame.display.set_mode(size)
        self.surface = pygame.Surface(size)

        self.background_color = (0, 0, 0)
        self.border_color = (0, 255, 0)
        self.paddle_color = (34, 255, 45)
        self.ball_color = (255, 255, 0)
        self.asteroid_color = (245, 222, 179)
        self.text_color = (255, 0, 0)

        self.ball_pos = (-1, -1)
        self.paddle_pos = (-1, -1)
        self.init_game()

    def run(self):
        running = True

        while running:
            dt = self.clock.tick(self.fps_limit)
            running = self.handle_events()

            self.render()
            self.draw()

        return self.score

    def init_game(self):
        self.surface.fill(self.background_color)
        self.game.reset()
        # Memory address 0 represents the number of quarters that have been inserted; set it to 2 to play for free.
        self.game.store(0, 2)
        self.update_score()

    def render(self):
        if not self.paused and not self.game.is_halted():
            if self.ball_pos != (-1, -1):
                if self.ball_pos[0] < self.paddle_pos[0]:
                    screen_data = self.game.execute(-1)
                elif self.ball_pos[0] > self.paddle_pos[0]:
                    screen_data = self.game.execute(1)
                else:
                    screen_data = self.game.execute(0)
            else:
                screen_data = self.game.execute(0)

            # screen_data = self.game.run(self.joystick_pos)

            if self.unit_size == 0:
                self.unit_size = self.get_unit_size(screen_data)

            if screen_data is not None:

                for i in range(0, len(screen_data), 3):
                    x, y, tile = screen_data[i], screen_data[i + 1], screen_data[i + 2]

                    if x < 0:
                        self.score = tile
                        self.update_score()
                    elif y < 0:
                        continue
                    else:
                        rect = (x * self.unit_size, y * self.unit_size, self.unit_size, self.unit_size)
                        if tile == 0:
                            pygame.draw.rect(self.surface, self.background_color, rect)
                        elif tile == 1:
                            pygame.draw.rect(self.surface, self.border_color, rect)
                        elif tile == 2:
                            pygame.draw.rect(self.surface, self.asteroid_color, rect)
                        elif tile == 3:
                            pygame.draw.rect(self.surface, self.paddle_color, rect)
                            self.paddle_pos = (x, y)
                        elif tile == 4:
                            pygame.draw.rect(self.surface, self.ball_color, rect)
                            self.ball_pos = (x, y)

        elif self.paused:
            text = self.font.render('Paused', True, self.text_color, self.background_color)
            rect = text.get_rect()
            rect.top = self.surface.get_height() - rect.height - 5
            rect.left = 30
            self.surface.blit(text, rect)
        elif self.game.is_halted():
            text = self.font.render('GAME OVER', True, self.text_color, self.background_color)
            rect = text.get_rect()
            rect.center = self.surface.get_width() / 2, self.surface.get_height() / 2
            self.surface.blit(text, rect)

    def get_unit_size(self, screen_data):
        width, height = 0, 0
        for i in range(0, len(screen_data), 3):
            x, y, _ = screen_data[i], screen_data[i + 1], screen_data[i + 2]
            width = max(width, x)
            height = max(height, y)

        return max(10,
                   math.floor(max(self.surface.get_width(), self.surface.get_height()) / max(width + 1, height + 1)))

    def draw(self):
        self.screen.blit(self.surface, (0, 0))
        pygame.display.update()

    def update_score(self):
        text = self.font.render(str(self.score), True, self.text_color, self.background_color)
        rect = text.get_rect()

        rect.top = 5
        rect.right = self.surface.get_width() - 30

        self.surface.blit(text, rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_LEFT:
                    self.joystick_pos = -1
                if event.key == pygame.K_RIGHT:
                    self.joystick_pos = 1
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                if event.key == pygame.K_BACKSPACE:
                    self.init_game()
            elif event.type == pygame.KEYUP:
                self.joystick_pos = 0

        return True


def render_array(game: Intcode):
    screen_data = game.execute()

    if len(screen_data) % 3 != 0:
        raise RuntimeError('Corrupted screen data')

    # convert raw data into organized layout
    width, height = 0, 0
    converted_data = []

    for i in range(0, len(screen_data), 3):
        x, y, tile = screen_data[i], screen_data[i + 1], screen_data[i + 2]
        width = max(width, x)
        height = max(height, y)
        converted_data.append((x, y, tile))

    width += 1
    height += 1

    # convert data to screen
    screen = np.zeros((height, width), dtype=int)

    for data in converted_data:
        x, y, tile = data
        if x >= 0 and y >= 0:
            screen[y][x] = tile

    return screen


def print_array(screen):
    for row in screen:
        print('{}'.format(''.join(map(str, row)).replace('0', ' ')))


def main():
    game = Intcode('input')
    screen = render_array(game)
    print_array(screen)
    print('Answer for Day13 - Part 1: {}'.format(np.count_nonzero(screen == 2)))

    game = Game(Intcode('input'))
    score = game.run()

    print('Answer for Day13 - Part 2: {}'.format(score))


if __name__ == "__main__":
    main()
