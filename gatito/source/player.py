import pygame
from settings import *
from tools import *

CAT_STATUS = ['right_jump', 'left_jump', 'right_fall', 'left_fall',
              'right_idle', 'left_idle', 'right_walk', 'left_walk']


class Player(pygame.sprite.Sprite):
    def __init__(self, topleft: tuple[int], *groups: pygame.sprite.Group, colliders: pygame.sprite.Group):
        super().__init__(groups)

        self.import_assets()
        self.status = 'left_idle'
        self.frame_index = 0

        # geneal setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft=topleft)

        # move player
        self.direction = pygame.math.Vector2()
        self.speed = 8
        self.jump_speed = 16
        self.gravity = 0.8
        self.on_floor = False

        self.colliders = colliders

    def import_assets(self):

        self.animations = dict(((status, []) for status in CAT_STATUS))

        for animation in self.animations.keys():
            relative_path = 'gatito/assets/graphics/character/' + animation
            self.animations[animation] = import_folder(relative_path)

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

    def animate(self, x):
        new_direction = ['left', self.status.split('_')[0], 'right']
        new_direction = new_direction[int(self.direction.x) + 1]
        if self.on_floor:
            new_status = '_idle' if self.direction.x == 0 else '_walk'
        else:
            new_status = '_jump' if self.direction.y < 0 else '_fall'

        self.status = new_direction + new_status
        print(self.status)

        self.frame_index += x % 4
        self.image = self.animations[self.status][int(self.frame_index)]

    def update(self):
        self.input()

        # horizontal movement
        self.rect.x += self.direction.x * self.speed
        self.horizontal_collisions()

        # vertical movement
        if not self.on_floor:
            self.apply_gravity()
        self.vertical_collisions()
        
        # animation
        self.animate(0)
