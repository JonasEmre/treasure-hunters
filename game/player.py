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
        self.direction = pygame.math.Vector2(0, 0)

        # Stats
        self.speed = 6
        self.movement_speed = self.speed

        # Jump modifiers
        self.jump_speed = -16
        self.is_ground = True

    def handle_inputs(self):
        keys = pygame.key.get_pressed()

        # Movement
        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        # Jump
        if keys[pygame.K_SPACE] and self.is_ground:
            self.direction.y = self.jump_speed
            self.is_ground = False

    def check_collision(self, objects):
        for object in objects:
            if self.rect.colliderect(object):
                print(f'{self.rect.bottom} : {object.rect.top}')
                if self.rect.bottom - self.rect.height / 2 < object.rect.top and not self.is_ground:
                    self.is_ground = True
                    self.rect.bottom = object.rect.top
                else:
                    self.is_ground = False
            

    def apply_gravity(self):
        if not self.is_ground:
            if self.direction.y > MAX_G:
                self.direction.y = MAX_G
            else:
                self.direction.y += G  # Gravity constant from settings.
        else:
            self.direction.y = 0
        self.rect.y += self.direction.y

    def update(self):
        self.handle_inputs()
        self.rect.x += self.direction.x * self.movement_speed
        self.apply_gravity()
