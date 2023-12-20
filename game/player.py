import pygame
from game.settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, position: tuple):
        # Initialization
        super().__init__()

        # Sprite
        self.image = pygame.Surface(PLAYER_SIZE)
        self.image.fill(colors['tomato'])
        self.rect = self.image.get_rect(topleft=position)

        # Position
        self.position = position
        self.direction = pygame.math.Vector2()

    def handle_inputs(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            pass
        elif keys[pygame.K_d]:
            pass
        else:
            pass
