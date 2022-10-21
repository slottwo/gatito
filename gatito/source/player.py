import pygame
from settings import *
from tools import *


class Player(pygame.sprite.Sprite):
    def __init__(self, topleft: tuple[int], *groups: pygame.sprite.Group, colliders: pygame.sprite.Group):
        super().__init__(groups)
        
        self.import_assets()
        
        # geneal setup
        self.image = pygame.Surface((TILE_SIZE // 2, TILE_SIZE))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect(topleft=topleft)
        self.colliders = colliders

        # move player
        self.direction = pygame.math.Vector2()
        self.speed = 8
        self.jump_speed = 16
        self.gravity = 0.8
        self.on_floor = False

    def import_assets(self):
        state_list = ['right_jump', 'left_jump', 'right_fall', 'left_fall',
                       'right_idle', 'left_idle', 'right_walk', 'left_walk', ]

        self.animations = dict(((state, []) for state in state_list))

        for animation in self.animations.keys:
            relative_path = 'gatito/assets/character' + animation
            self.animations[animation] = import_folder(relative_path)
            
            if not self.animations[animation]:
                raise Exception("Character sprites not found.")

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.on_floor:
            self.direction.y = -self.jump_speed

    def horizontal_collisions(self):
        for sprite in self.colliders.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left

    def vertical_collisions(self):
        for sprite in self.colliders.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.on_floor = True
                if self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0

        if self.on_floor and self.direction.y:
            self.on_floor = False

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        self.input()

        # horizontal movement
        self.rect.x += self.direction.x * self.speed
        self.horizontal_collisions()

        # vertical movement
        self.apply_gravity()
        self.vertical_collisions()
