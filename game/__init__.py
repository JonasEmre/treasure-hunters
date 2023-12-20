import pygame
import sys
from game.settings import *
from game.level import Level


class Game():
    def __init__(self):
        # Initialization
        pygame.init()
        self.start = True

        # Screen, surface
        self.screen = pygame.display.set_mode(
            (WIDTH, HEIGHT))

        # Delta time
        self.clock = pygame.time.Clock()

        # World Setup
        self.level = Level(level_data, self.screen)
        self.x_shift = 0

    def run(self):
        while self.start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.start = False
                    sys.exit()

            self.screen.fill('black')
            self.level.run(self.x_shift)

            pygame.display.update()
            self.clock.tick(FPS)
