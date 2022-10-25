import pygame
from settings import *
from tools import *

STATUS = [
    'right_jump', 'left_jump', 'right_fall', 'left_fall',
    'right_idle', 'left_idle', 'right_walk', 'left_walk']


class Player(pygame.sprite.Sprite):
    def __init__(self, topleft: tuple[int],
                 *groups: pygame.sprite.Group,
                 colliders: pygame.sprite.Group):
        super().__init__(groups)

        self.import_assets()

        # animation setup
        self.status = 'left_idle'
        self.frame_index = 0
        self.animation_speed = 4  # frame per sec

        # geneal setup
        self.image = self.animations[self.status][self.frame_index]

        x, y = topleft
        w, h = self.image.get_size()
        initial_pos = x + TILE_SIZE - w, y + TILE_SIZE - h
        self.rect = self.image.get_rect(topleft=initial_pos)

        # move player
        self.position = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2()
        self.on_floor = True
        self.speed = 2.5 * TILE_SIZE
        self.jump_speed = -4 * TILE_SIZE
        self.gravity = 7 * TILE_SIZE
        self.terminal_speed = 5 * TILE_SIZE

        # other settings
        self.colliders = colliders

    def import_assets(self) -> None:
        self.animations: dict[str, list[pygame.surface.Surface]]
        self.animations = dict(((status, []) for status in STATUS))

        for animation in self.animations.keys():
            relative_path = 'gatito/assets/graphics/character/' + animation
            self.animations[animation] = import_folder(relative_path)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.on_floor:
            self.jump()

    def apply_gravity(self, dt: float):
        if self.direction.y < self.terminal_speed:
            self.direction.y += self.gravity * dt
        else:
            self.direction.y = self.terminal_speed

        self.position.y += self.direction.y * dt
        self.rect.y = self.position.y

    def jump(self):
        self.direction.y = self.jump_speed

    def horizontal_collisions(self):
        for sprite in self.colliders.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.x < 0:  # collide by left
                    self.rect.left = sprite.rect.right
                if self.direction.x > 0:  # collide by right
                    self.rect.right = sprite.rect.left

                # update control position variable
                self.position.x = self.rect.left

                # action and reaction baby!
                self.direction.x = 0

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
                self.position.y = self.rect.top

        if self.on_floor and self.direction.y:
            self.on_floor = False

    def get_status(self, dt: float):
        new_status_direction = ['left', self.status.split('_')[0], 'right']
        new_status_direction = new_status_direction[int(self.direction.x) + 1]

        if self.direction.y < 0:
            new_status = 'jump'
        elif self.direction.y > dt * self.gravity:
            new_status = 'fall'
        elif self.direction.x:
            new_status = 'walk'
        else:
            new_status = 'idle'

        self.status = new_status_direction + '_' + new_status

    def animate(self, dt: float):
        
        # update status
        
        self.get_status(dt)
        
        # update index

        self.frame_index += self.animation_speed * dt
        self.frame_index %= len(self.animations[self.status])

        self.image = self.animations[self.status][int(self.frame_index)]

    def update(self, dt: float):

        self.get_input()

        # horizontal movement
        self.position.x += self.direction.x * self.speed * dt
        self.rect.x = self.position.x
        self.horizontal_collisions()

        # vertical movement
        self.apply_gravity(dt)
        self.vertical_collisions()

        # animation
        self.animate(dt)
