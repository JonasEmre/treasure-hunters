import pygame
from game.tile import Tile
from game.player import Player
from game.settings import *


class Level():
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.layout = self.setup_layout(level_data)

        self.x_shift = 0

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

    def scroll_x(self):
        player = self.player.sprite
        direction_x = player.direction.x
        player_x = player.rect.centerx

        if player_x < int(WIDTH * 0.2) and direction_x < 0:
            self.x_shift = player.speed
            player.movement_speed = 0
        elif player_x > int(WIDTH * 0.8) and direction_x > 0:
            self.x_shift = -player.speed
            player.movement_speed = 0
        else:
            self.x_shift = 0
            player.movement_speed = player.speed


    def run(self):
        # Environment tiles
        self.tiles.update(self.x_shift)
        self.tiles.draw(self.display_surface)

        # Player
        self.scroll_x()
        self.player.update()
        self.player.draw(self.display_surface)
        if self.player.sprite.direction != 0:
            self.player.sprite.check_collision(self.tiles)

        # Collisions
