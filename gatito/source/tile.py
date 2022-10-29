import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, topleft: tuple[int],
                 *groups: pygame.sprite.AbstractGroup) -> None:
        super().__init__(*groups)
