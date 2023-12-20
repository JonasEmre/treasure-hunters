import pygame
from game.settings import colors


class Tile(pygame.sprite.Sprite):
    def __init__(self, size: int, position: tuple):
        super().__init__()

        # Position
        self.position = position

        # Image, Sprite and Rect
        self.image = pygame.Surface((size, size))
        self.image.fill(colors['corn_flower'])
        self.rect = self.image.get_rect(topleft=position)

    def update(self, x_shift):
        self.rect.x += x_shift
