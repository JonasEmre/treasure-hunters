import pygame
from game.tile import Tile
from game.player import Player
from game.settings import *


class Level():
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.layout = self.setup_layout(level_data)

    def setup_layout(self, layout):
        # Sprite Groups
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if col == 'x':
                    tile = Tile(TILE_SIZE, (x, y))
                    self.tiles.add(tile)
                if col == 'p':
                    player = Player((x, y))
                    self.player.add(player)


    def run(self, x_shift):
        self.tiles.update(x_shift)
        self.tiles.draw(self.display_surface)
        self.player.draw(self.display_surface)
